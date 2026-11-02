# Technical SEO for the whole site, read from the built HTML (landing, web tests, guides, tools — any generator).
#   python3 seo.py sitemap          # sitemap.xml: every indexable page, <lastmod> from git, hreflang alternates from the page
#   python3 seo.py audit [out.md]   # broken links, canonical/hreflang errors, duplicate title/description, noindex, size
#   python3 seo.py indexnow <rev>   # ping IndexNow (Bing, Yandex, Seznam, Naver) with sitemap URLs changed since git <rev>
# Base URL comes from landing.BASE (SITE_BASE env); pages are found by walking the repo, so new page types need no change here.
# Not in the sitemap: noindex pages, pages whose canonical points elsewhere, the privacy-policy list (/) and per-app
# privacy/support pages (<repo>/, <repo>/support/). .github/workflows/seo.yml runs this on every push/PR.
import collections, datetime, html.parser, json, os, re, subprocess, sys, urllib.parse, urllib.request
from landing import BASE, LOC

LANGS = {v[0] for v in LOC.values()}
MAX_HTML = 150_000  # bytes; flag heavier HTML (images are counted separately)
MAX_IMG = 400_000


class Page(html.parser.HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.title, self.desc, self.canonical, self.robots, self.lang = path, None, None, None, "", None
        self.alts, self.links, self._t = {}, [], False
        self.feed(open(path, encoding="utf-8").read())

    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._t, self.title = True, ""
        elif tag == "meta" and a.get("name") == "description":
            self.desc = a.get("content")
        elif tag == "meta" and a.get("name") == "robots":
            self.robots = a.get("content", "")
        elif tag == "meta" and a.get("http-equiv", "").lower() == "refresh":
            self.links.append(a.get("content", "").partition("url=")[2])
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        elif tag == "link" and a.get("rel") == "alternate" and a.get("hreflang"):
            self.alts[a["hreflang"]] = a.get("href")
        if tag in ("a", "link") and a.get("href") and a.get("rel") not in ("canonical", "alternate"):
            self.links.append(a["href"])
        if tag in ("img", "script") and a.get("src"):
            self.links.append(a["src"])

    def handle_data(self, d):
        if self._t:
            self.title += d

    def handle_endtag(self, tag):
        self._t = self._t and tag != "title"

    @property
    def url(self):
        return f"{BASE}/{self.path.removesuffix('index.html')}"

    @property
    def indexable(self):
        return "noindex" not in self.robots.lower() and self.canonical in (None, self.url)

    @property
    def in_sitemap(self):
        parts = self.path.split("/")
        utility = len(parts) == 1 or parts[0] not in LANGS and (len(parts) == 2 or parts[1:] == ["support", "index.html"])
        return self.indexable and not utility


def pages():
    out = []
    for root, dirs, files in os.walk("."):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        out += [Page(os.path.join(root, f)[2:]) for f in sorted(files) if f.endswith(".html")]
    return out


def lastmod():
    """Latest commit date per file (one git call); uncommitted files get today."""
    log = subprocess.run(["git", "log", "--format=@%cs", "--name-only", "--no-renames"], capture_output=True, text=True).stdout
    seen, day = {}, None
    for line in log.splitlines():
        if line.startswith("@"):
            day = line[1:]
        elif line:
            seen.setdefault(line, day)
    return seen


def local(page, href):
    """Repo path a same-site link points to, or None for external/anchor/mailto links."""
    if href.startswith(BASE + "/"):
        href = href[len(BASE) + 1:]
        base = ""
    elif re.match(r"^[a-z]+:|^//|^#", href) or not href:
        return None
    else:
        base = os.path.dirname(page.path)
    p = os.path.normpath(os.path.join(base, urllib.parse.unquote(href.split("#")[0].split("?")[0])))
    return os.path.join(p, "index.html") if href.split("#")[0].split("?")[0].endswith("/") or os.path.isdir(p) else p


def sitemap():
    days, today = lastmod(), datetime.date.today().isoformat()
    ps = [p for p in pages() if p.in_sitemap]
    assert len(ps) < 50_000, "split into a sitemap index"  # ponytail: one file until the 50k-URL limit
    rows = []
    for p in ps:
        alts = "".join(f"\n  <xhtml:link rel=\"alternate\" hreflang=\"{h}\" href=\"{u}\"/>" for h, u in sorted(p.alts.items()))
        rows.append(f"<url>\n  <loc>{p.url}</loc>\n  <lastmod>{days.get(p.path, today)}</lastmod>{alts}\n</url>")
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                                   'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
    print(len(ps), "URLs → sitemap.xml")


def audit(out="DENETIM.md"):
    ps = pages()
    by_url, by_path = {p.url: p for p in ps}, {p.path: p for p in ps}
    idx = [p for p in ps if p.indexable]
    issues = collections.defaultdict(list)
    for p in ps:
        for h in set(p.links):
            t = local(p, h)
            if t and not os.path.exists(t):
                issues["Kırık iç link"].append(f"`{p.path}` → `{h}`")
        if not p.title:
            issues["Title yok"].append(f"`{p.path}`")
        if p.canonical and not p.canonical.startswith(BASE + "/"):
            issues["Canonical başka alan adında"].append(f"`{p.path}` → {p.canonical}")
        elif p.canonical and p.canonical != p.url and "noindex" not in p.robots:
            issues["Canonical başka sayfaya (noindex değil)"].append(f"`{p.path}` → {p.canonical}")
        if p.canonical and p.canonical != p.url and p.canonical not in by_url:
            issues["Canonical hedefi yok"].append(f"`{p.path}` → {p.canonical}")
        size = os.path.getsize(p.path)
        if size > MAX_HTML:
            issues[f"HTML > {MAX_HTML // 1000} KB"].append(f"`{p.path}` {size // 1000} KB")
        for h in set(p.links):
            t = local(p, h)
            if t and os.path.isfile(t) and t.endswith((".jpg", ".png", ".webp")) and os.path.getsize(t) > MAX_IMG:
                issues[f"Görsel > {MAX_IMG // 1000} KB"].append(f"`{t}` {os.path.getsize(t) // 1000} KB")
    for p in idx:
        if not p.lang:
            issues["`<html lang>` yok"].append(f"`{p.path}`")
        if p.in_sitemap and not p.canonical:
            issues["Canonical yok (sitemap sayfası)"].append(f"`{p.path}`")
        if p.in_sitemap and not p.desc:
            issues["Meta description yok (sitemap sayfası)"].append(f"`{p.path}`")
        if p.alts:
            if "x-default" not in p.alts:
                issues["hreflang var, x-default yok"].append(f"`{p.path}`")
            if p.url not in p.alts.values():
                issues["hreflang kümesinde kendisi yok"].append(f"`{p.path}`")
            for h, u in p.alts.items():
                q = by_url.get(u)
                if not q:
                    issues["hreflang hedefi yok"].append(f"`{p.path}` {h} → {u}")
                elif not q.indexable:
                    issues["hreflang hedefi noindex/canonical başka"].append(f"`{p.path}` {h} → {u}")
                elif h != "x-default" and p.url not in q.alts.values():
                    issues["hreflang karşılığı yok (geri dönüş linki)"].append(f"`{p.path}` {h} → {u}")
                elif h != "x-default" and q.lang and q.lang.lower() != h.lower():
                    issues["hreflang ≠ hedefin `<html lang>`"].append(f"`{p.path}` {h} → {u} (lang={q.lang})")
    for key, name in (("title", "Çift title"), ("desc", "Çift meta description")):
        groups = collections.defaultdict(list)
        for p in idx:
            if getattr(p, key):
                groups[getattr(p, key).strip()].append(p.path)
        for v, paths in groups.items():
            if len(paths) > 1 and not set(BASE + "/" + x.removesuffix("index.html") for x in paths) <= set(by_path[paths[0]].alts.values()):
                issues[name].append(f"{len(paths)}× “{v[:80]}”: " + ", ".join(f"`{x}`" for x in paths[:6]) + (" …" if len(paths) > 6 else ""))
    noindex = [p for p in ps if "noindex" in p.robots.lower()]
    in_map = [p for p in ps if p.in_sitemap]
    util = [p for p in idx if not p.in_sitemap and (not p.canonical or not p.desc)]
    lines = [f"# Teknik SEO denetimi — {BASE}/", "", f"Üretici: `python3 seo.py audit` (repo `BaytechBV/privacy`).", "",
             "| | Sayı |", "|---|---|", f"| HTML sayfası | {len(ps)} |", f"| İndekslenebilir | {len(idx)} |",
             f"| Sitemap'te | {len(in_map)} |", f"| noindex | {len(noindex)} |",
             f"| hreflang kümeli sayfa | {sum(1 for p in idx if p.alts)} |", ""]
    lines += ["## Bulgular", ""] + ([f"- **{k}**: {len(v)}" for k, v in sorted(issues.items())] or ["- Hata yok."]) + [""]
    for k, v in sorted(issues.items()):
        lines += [f"### {k} ({len(v)})", ""] + [f"- {x}" for x in v[:40]] + ([f"- … +{len(v) - 40}"] if len(v) > 40 else []) + [""]
    lines += ["### Privacy/support sayfaları (bilgi)", "", f"- {len(util)} indekslenebilir privacy/support sayfasında canonical veya description yok. "
              "Sitemap'e bilerek alınmadı (60+ benzer yasal metin = ince/çift içerik); App Store linkleri için açık kalır.", ""]
    noi = collections.Counter(re.sub(r"^[^/]+/", "*/", p.path) for p in noindex)
    lines += ["### noindex sayfalar (bilgi; kasıtlı mı kontrol et)", ""] + [f"- `{k}` × {n}" for k, n in noi.most_common()] + [""]
    open(out, "w").write("\n".join(lines))
    print(out, {k: len(v) for k, v in sorted(issues.items())})
    return issues


def indexnow(rev):
    key = os.environ["INDEXNOW_KEY"]
    assert os.path.exists(f"{key}.txt"), f"{key}.txt must be published at the site root first"
    changed = set(subprocess.run(["git", "diff", "--name-only", rev, "HEAD"], capture_output=True, text=True).stdout.split())
    urls = [p.url for p in pages() if p.in_sitemap and p.path in changed][:10_000]
    if not urls:
        return print("no changed pages")
    host = urllib.parse.urlparse(BASE).netloc
    body = json.dumps({"host": host, "key": key, "keyLocation": f"{BASE}/{key}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", body, {"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow", r.status, len(urls), "URLs")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "sitemap"
    {"sitemap": sitemap, "audit": audit, "indexnow": indexnow}[cmd](*sys.argv[2:])
