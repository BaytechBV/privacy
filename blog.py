# Blog articles per app (one search keyword each) at <lang>/blog/<slug>/, plus a <lang>/blog/ index (Article + FAQPage JSON-LD).
#   python3 blog.py            # all apps in blog/*.json, then the indexes and llms.txt
# Copy lives in blog/<repo-slug>.json ({dir, app, updated (ISO date), authority, cta, articles: [{slug, kw, title, description, h1, lead,
# sections: [{h, html}], faq: [{q, a}], sources: [{name, url}]}]}); every number needs an official source in its article.
# The app's landing page links all its articles (landing.py reads the same JSON); re-run `landing.py build <repo-slug>` after adding one.
import datetime, json, os, re, sys

import android_privacy  # Google Play package per app (PLAY) and button label
import landing
from landing import BASE, CSS, FREE, UI, e

APPS = json.load(open("landing/apps.json"))
SLUGS = json.load(open("landing/slugs.json"))
CSS += """.upd{color:var(--mu);font-size:.9em}.src{font-size:.9em}.cta{background:var(--card);border-radius:12px;padding:12px 14px;margin:18px 0}
.crumb{font-size:.9em;color:var(--mu)}table{border-collapse:collapse;width:100%;margin:8px 0}th,td{text-align:left;padding:6px 8px;
border-bottom:1px solid rgba(128,128,128,.25);vertical-align:top}.rel li{margin:4px 0}"""
# per lang dir: blog, last updated, sources, app box title, read more about the app, more articles, disclaimer (independent app, {a}=authority)
T = {"nl": ("Blog", "Laatst bijgewerkt", "Bronnen", "Oefenen met de app", "Meer over de app", "Meer artikelen",
            "{app} is een onafhankelijke app van Baytech BV en is niet verbonden aan {a}. Controleer actuele regels altijd bij de officiële bron."),
     "da": ("Blog", "Sidst opdateret", "Kilder", "Øv med appen", "Læs mere om appen", "Flere artikler",
            "{app} er en uafhængig app fra Baytech BV og har ingen forbindelse til {a}. Tjek altid de gældende regler hos den officielle kilde.")}
TAGS = re.compile(r"</?(p|ul|ol|li|strong|em|a|table|tr|th|td|thead|tbody|br)\b[^>]*>")
MONTHS = {"nl": "januari februari maart april mei juni juli augustus september oktober november december",
          "da": "januar februar marts april maj juni juli august september oktober november december"}


def words(a):
    text = " ".join([a["lead"]] + [s["h"] + " " + s["html"] for s in a["sections"]] + [q["q"] + " " + q["a"] for q in a["faq"]])
    return len(re.sub(r"<[^>]+>", " ", text).split())


def check(rs, c):
    slugs = [a["slug"] for a in c["articles"]]
    assert len(set(slugs)) == len(slugs) and len({a["kw"].lower() for a in c["articles"]}) == len(slugs), (rs, "duplicate slug/keyword")
    for a in c["articles"]:
        assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a["slug"]), a["slug"]
        assert a["sources"] and all(s["url"].startswith("https://") for s in a["sources"]), (rs, a["slug"], "sources")
        for s in a["sections"]:
            left = TAGS.sub("", s["html"])
            assert "<" not in left, (rs, a["slug"], "tag", left[left.index("<"):][:40])
            for href in re.findall(r"href=['\"]([^'\"]+)", s["html"]):  # siblings or listed sources only
                assert href.startswith("https://") and href in {x["url"] for x in a["sources"]} or \
                    re.fullmatch(r"\.\./([a-z0-9-]+)/(#[\w-]+)?", href) and href[3:].split("/")[0] in slugs, (rs, a["slug"], href)
        n = words(a)
        if not 550 <= n <= 1300:
            print("WARN words", rs, a["slug"], n, file=sys.stderr)
        seen = FREE.search(json.dumps(a, ensure_ascii=False))
        assert not seen, (rs, a["slug"], seen.group(0))  # PUBLISH-PLAN §3.4: no "free" in our copy


def store_btns(rs, a, d, u):
    btn = (f"<a class='badge' href='https://apps.apple.com/app/id{a['id']}?pt=322891&ct=blog-{d}'><img src='../../../landing/app-store-badge.svg'"
           f" alt='{e(u[0])}' width='162' height='54'></a>")
    if rs in android_privacy.PLAY:  # text button next to the App Store badge, like the landing page
        btn += f"<a class='play' href='{android_privacy.play_url(rs)}'>{e(android_privacy.PLAY_LABEL[d])}</a>"
    return btn


def ld(x):
    return "<script type='application/ld+json'>" + json.dumps(x, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def page(d, title, desc, url, body, extra="", app_id=None):
    return (f"<!doctype html><html lang='{d}'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{e(title)}</title><meta name='description' content='{e(desc)}'>"
            + (f"<meta name='apple-itunes-app' content='app-id={app_id}'>" if app_id else "") +
            f"<link rel='canonical' href='{url}'><meta property='og:type' content='{'article' if app_id else 'website'}'>"
            f"<meta property='og:title' content='{e(title)}'><meta property='og:description' content='{e(desc)}'><meta property='og:url' content='{url}'>"
            f"{extra}<style>{CSS}</style></head><body>{body}</body></html>")


def build(rs, c, updated):
    a, d = APPS[rs], c["dir"]
    u, t = UI[d], T[d]
    landing_url = f"../../{SLUGS[rs][d]}/"
    btn = store_btns(rs, a, d, u)
    day = datetime.date.fromisoformat(updated)
    when = f"{day.day}. {MONTHS[d].split()[day.month - 1]} {day.year}" if d == "da" else f"{day.day} {MONTHS[d].split()[day.month - 1]} {day.year}"
    cta = (f"<div class='cta'><b>{e(t[3])}: {e(c['app'])}</b><br>{e(c['cta'])}{btn}<a href='{landing_url}'>{e(t[4])} →</a></div>")
    urls = []
    for art in c["articles"]:
        out = f"{d}/blog/{art['slug']}/"
        url = f"{BASE}/{out}"
        lds = [{"@context": "https://schema.org", "@type": "Article", "headline": art["h1"], "description": art["description"],
                "inLanguage": d, "datePublished": art.get("published", updated), "dateModified": updated, "mainEntityOfPage": url,
                "keywords": art["kw"], "author": {"@type": "Organization", "name": "Baytech BV"},
                "publisher": {"@type": "Organization", "name": "Baytech BV"}, "citation": [s["url"] for s in art["sources"]]},
               {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                   {"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": q["a"]}} for q in art["faq"]]},
               {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                   {"@type": "ListItem", "position": 1, "name": t[0], "item": f"{BASE}/{d}/blog/"},
                   {"@type": "ListItem", "position": 2, "name": c["app"], "item": f"{BASE}/{d}/{SLUGS[rs][d]}/"},
                   {"@type": "ListItem", "position": 3, "name": art["h1"]}]}]
        body = [f"<p class='crumb'><a href='../'>{e(t[0])}</a> › <a href='{landing_url}'>{e(c['app'])}</a></p>",
                f"<h1>{e(art['h1'])}</h1><p class='upd'>{e(t[1])}: <time datetime='{updated}'>{e(when)}</time></p>",
                f"<p class='lead'>{e(art['lead'])}</p>"]
        for i, s in enumerate(art["sections"]):
            body.append(f"<h2>{e(s['h'])}</h2>{s['html']}")
            if i == 1:
                body.append(cta)
        body.append(f"<h2>{e(u[1])}</h2>" + "".join(f"<h3>{e(q['q'])}</h3><p>{e(q['a'])}</p>" for q in art["faq"]))
        body.append(cta)
        body.append(f"<h2>{e(t[2])}</h2><ul class='src'>" + "".join(
            f"<li><a href='{e(s['url'])}' rel='noopener'>{e(s['name'])}</a></li>" for s in art["sources"]) + "</ul>")
        body.append(f"<h2>{e(t[5])}</h2><ul class='rel'>" + "".join(
            f"<li><a href='../{x['slug']}/'>{e(x['h1'])}</a></li>" for x in c["articles"] if x is not art) + "</ul>")
        body.append(f"<p class='desc'>{e(t[6].format(app=c['app'], a=c['authority']))}</p><footer><a href='../../../{rs}/support/'>{e(u[4])}</a>"
                    f"<a href='../../../{rs}/'>{e(u[5])}</a><br>© Baytech BV</footer>")
        html = page(d, art["title"], art["description"], url, "".join(body),
                    f"<meta property='article:modified_time' content='{updated}'>" + "".join(ld(x) for x in lds), a["id"])
        assert not FREE.search(re.sub(r"<[^>]+>|href='[^']*'", " ", html)), (rs, art["slug"])
        os.makedirs(out, exist_ok=True)
        open(f"{out}index.html", "w").write(html)
        urls.append(url)
    return urls


def index(d, groups):
    """<lang>/blog/: every app's articles in that language, grouped by app."""
    t = T[d]
    url = f"{BASE}/{d}/blog/"
    body = [f"<h1>{e(t[0])}</h1>"]
    for rs, c in groups:
        body.append(f"<h2 id='{rs}'><a href='../{SLUGS[rs][d]}/'>{e(c['app'])}</a></h2><ul class='rel'>"
                    + "".join(f"<li><a href='{x['slug']}/'>{e(x['h1'])}</a></li>" for x in c["articles"]) + "</ul>")
    body.append("<footer>© Baytech BV</footer>")
    names = ", ".join(c["app"] for _, c in groups)
    desc = {"nl": f"Artikelen en uitleg bij examens en regels: {names}.", "da": f"Artikler og forklaringer om prøver og regler: {names}."}[d][:155]
    os.makedirs(f"{d}/blog", exist_ok=True)
    open(f"{d}/blog/index.html", "w").write(page(d, f"{t[0]} – Baytech apps", desc, url, "".join(body)))


if __name__ == "__main__":
    groups = {}
    for f in sorted(os.listdir("blog")):
        if f.endswith(".json"):
            rs, c = f[:-5], json.load(open(f"blog/{f}"))
            check(rs, c)
            urls = build(rs, c, c["updated"])
            groups.setdefault(c["dir"], []).append((rs, c))
            print(rs, len(urls), "articles")
    for d, g in groups.items():
        index(d, g)
    landing.llms(APPS, SLUGS)  # adds the blog lines
