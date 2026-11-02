# Local-language landing pages, one per app and App Store localization, at <lang>/<slug>/ (SEO entry page → App Store).
#   python3 landing.py fetch ~/Documents/Projects/baytech   # live ASC texts + first 3 store screenshots + rating → landing/apps.json
#   python3 landing.py build [repo-slug]                     # pages from landing/apps.json + landing/content/<repo-slug>.json
# Hand-written SEO copy (h1, benefits, FAQ) lives in landing/content/<repo-slug>.json keyed by ASC locale; locales without it
# get a page from the store texts. Optional citable blocks per locale: "definition" (one paragraph: what the app is,
# for whom, what it covers) and "compare" ({title, head, rows, note}: app vs. official sources vs. competitors, facts checked
# on the App Store). build also writes llms.txt + llms-full.txt (index for AI search engines). URL slugs are pinned in landing/slugs.json (never rename a published one).
# <repo-slug>/app/ (old marketing URL) becomes a redirect to the primary-language page.
import html, json, os, re, sys, unicodedata, urllib.request

BASE = os.environ.get("SITE_BASE", "https://apps.baytech.nl")  # domain switch = this line
SHOTS = 3
MIN_RATINGS = 5  # aggregateRating only with at least this many real App Store ratings
# ASC locale → (URL dir, hreflang, iTunes country)
LOC = {"da": ("da", "da", "dk"), "no": ("nb", "nb", "no"), "sv": ("sv", "sv", "se"),
       "fi": ("fi", "fi", "fi"), "de-DE": ("de", "de", "de"), "nl-NL": ("nl", "nl", "nl"),
       "pl": ("pl", "pl", "pl"), "it": ("it", "it", "it"), "fr-FR": ("fr", "fr", "fr"),
       "fr-CA": ("fr-ca", "fr-CA", "ca"), "en-GB": ("en", "en", "gb"), "en-US": ("en-us", "en-US", "us"),
       "ar-SA": ("ar", "ar", "sa"), "tr": ("tr", "tr", "tr")}
COUNTRY = {"fischerpruefung-at": "at", "jagdpruefung-at": "at", "lkw-theorie-at": "at"}  # home store differs from locale
# Exam apps with a web practice test (quiztest.py): repo slug → path from site root.
TESTS = {"indfodsretsprove-dk": "da/indfodsretsprove-gratis-test/", "statsborgerprove-no": "nb/statsborgerproven-gratis-test/",
         "klein-vaarbewijs-nl": "nl/vaarbewijs-oefenen-gratis/"}
GENRE = {"Education": "EducationalApplication", "Health & Fitness": "HealthApplication", "Medical": "HealthApplication",
         "Finance": "FinanceApplication", "Food & Drink": "LifestyleApplication", "Lifestyle": "LifestyleApplication",
         "Travel": "TravelApplication", "Sports": "SportsApplication", "Reference": "ReferenceApplication",
         "Productivity": "BusinessApplication", "Business": "BusinessApplication", "Games": "GameApplication",
         "Utilities": "UtilitiesApplication", "Navigation": "TravelApplication", "Weather": "UtilitiesApplication"}
# UI strings per URL dir: badge alt, FAQ, more about the app, web test link, support, privacy, languages
UI = {"da": ("Hent i App Store", "Ofte stillede spørgsmål", "Om appen", "Prøv en øveprøve i browseren", "Support", "Privatliv", "Sprog"),
      "nb": ("Last ned fra App Store", "Vanlige spørsmål", "Om appen", "Prøv en øveprøve i nettleseren", "Støtte", "Personvern", "Språk"),
      "sv": ("Hämta i App Store", "Vanliga frågor", "Om appen", "Prova ett övningsprov i webbläsaren", "Support", "Integritet", "Språk"),
      "fi": ("Lataa App Storesta", "Usein kysytyt kysymykset", "Sovelluksesta", "Kokeile harjoituskoetta selaimessa", "Tuki", "Tietosuoja", "Kieli"),
      "de": ("Im App Store laden", "Häufige Fragen", "Über die App", "Probetest im Browser starten", "Support", "Datenschutz", "Sprache"),
      "nl": ("Download in de App Store", "Veelgestelde vragen", "Over de app", "Probeer een oefentoets in je browser", "Support", "Privacy", "Taal"),
      "pl": ("Pobierz z App Store", "Najczęstsze pytania", "O aplikacji", "Spróbuj testu w przeglądarce", "Pomoc", "Prywatność", "Język"),
      "it": ("Scarica su App Store", "Domande frequenti", "L'app", "Prova un test nel browser", "Assistenza", "Privacy", "Lingua"),
      "fr": ("Télécharger dans l'App Store", "Questions fréquentes", "À propos de l'app", "Essayer un test dans le navigateur", "Assistance", "Confidentialité", "Langue"),
      "en": ("Download on the App Store", "Frequently asked questions", "About the app", "Try a practice test in your browser", "Support", "Privacy", "Language"),
      "ar": ("التنزيل من App Store", "الأسئلة الشائعة", "عن التطبيق", "جرّب اختبارًا في المتصفح", "الدعم", "الخصوصية", "اللغة"),
      "tr": ("App Store'dan indir", "Sık sorulan sorular", "Uygulama hakkında", "Tarayıcıda deneme testi çöz", "Destek", "Gizlilik", "Dil")}
UI["fr-ca"], UI["en-us"] = UI["fr"], UI["en"]
NAME = {"da": "Dansk", "nb": "Norsk", "sv": "Svenska", "fi": "Suomi", "de": "Deutsch", "nl": "Nederlands", "pl": "Polski", "it": "Italiano",
        "fr": "Français", "fr-ca": "Français (CA)", "en": "English", "en-us": "English (US)", "ar": "العربية", "tr": "Türkçe"}
FREE = re.compile(r"\b(free|gratis|gratuit\w*|kostenlos\w*|ilmai\w*|maksuton\w*|darmow\w*|bezpłatn\w*|ücretsiz|مجان\w*)\b", re.I)
# Campaign from the incoming link (app share card sends ?ct=share) replaces the page's own ct on the store buttons.
CT_JS = ("<script>var c=new URLSearchParams(location.search).get('ct');if(c&&/^[\\w-]{1,40}$/.test(c))"
         "document.querySelectorAll(\"a[href*='apps.apple.com']\").forEach(function(a){a.href=a.href.replace(/ct=[^&]*/,'ct='+c)})</script>")
CSS = """:root{--bg:#fff;--fg:#1c1c1e;--mu:#6b6b70;--ac:#0a66c2;--card:#f4f4f6}
@media (prefers-color-scheme:dark){:root{--bg:#111;--fg:#eee;--mu:#9a9aa0;--ac:#5aa9ff;--card:#1d1d20}}
*{box-sizing:border-box}body{background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:760px;
margin:0 auto;padding:20px 16px 40px;overflow-wrap:anywhere}a{color:var(--ac)}header{display:flex;gap:14px;align-items:center}
header img{border-radius:22%;flex:none}h1{font-size:1.75em;line-height:1.2;margin:.1em 0}.lead{font-size:1.1em;color:var(--mu)}
h2{font-size:1.25em;margin-top:1.8em}h3{font-size:1em;margin:1.2em 0 .2em}.badge img{display:block;margin:18px 0}
.shots{display:flex;gap:12px;overflow-x:auto;margin:8px -16px;padding:4px 16px 10px;scroll-snap-type:x mandatory}
.shots img{width:min(62vw,240px);height:auto;border-radius:18px;flex:none;scroll-snap-align:start;border:1px solid rgba(128,128,128,.25)}
.ben{list-style:none;padding:0;display:grid;gap:10px}.ben li{background:var(--card);border-radius:12px;padding:12px 14px}
.test{display:inline-block;background:var(--card);border-radius:12px;padding:10px 14px;font-weight:600;text-decoration:none}
.desc{color:var(--mu);font-size:.95em}.def{border-left:3px solid var(--ac);padding:2px 0 2px 12px}
.cmp{overflow-x:auto;margin:0 -16px;padding:0 16px}.cmp table{border-collapse:collapse;font-size:.9em;min-width:560px}
.cmp th,.cmp td{border-bottom:1px solid rgba(128,128,128,.3);padding:6px 8px;text-align:left;vertical-align:top}.cmp small{color:var(--mu)}
@media (max-width:600px){.cmp table{min-width:0}.cmp thead{display:none}.cmp tr{display:block;background:var(--card);border-radius:12px;
padding:8px 12px;margin-bottom:10px}.cmp td{display:flex;gap:10px;border:0;padding:3px 0}.cmp td:first-child{font-weight:600}
.cmp td[data-l]:before{content:attr(data-l);flex:0 0 40%;color:var(--mu)}}footer{margin-top:40px;font-size:.9em;color:var(--mu)}footer a{margin-right:10px}"""
e = html.escape


def slugify(s):
    s = s.lower().translate(str.maketrans({"æ": "ae", "ø": "oe", "å": "aa", "ß": "ss", "ł": "l", "ı": "i"}))
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read()


def fetch(src):
    sys.path.insert(0, f"{src}/tools")
    import asc_pub
    apps = {}
    for a in asc_pub.get("/apps?limit=200&fields[apps]=name,primaryLocale")["data"]:
        v = asc_pub.get(f"/apps/{a['id']}/appStoreVersions?filter[platform]=IOS&filter[appStoreState]=READY_FOR_SALE&limit=1")["data"]
        if not v:
            continue
        info = asc_pub.get(f"/apps/{a['id']}/appInfos?include=appInfoLocalizations")
        names = {}
        for l in info.get("included", []):
            names.setdefault(l["attributes"]["locale"], l["attributes"])
        pl = a["attributes"]["primaryLocale"]
        m = re.search(r"github\.io/privacy/([^/]+)/", (names.get(pl) or {}).get("privacyPolicyUrl") or "")
        if not m:  # own website (Falcı, Sohbet, Transcribe, Tıngır)
            continue
        slug, locs = m.group(1), {}
        for l in asc_pub.get(f"/appStoreVersions/{v[0]['id']}/appStoreVersionLocalizations?limit=50")["data"]:
            loc, at = l["attributes"]["locale"], l["attributes"]
            if loc not in LOC or not at.get("description"):
                continue
            sets = asc_pub.get(f"/appStoreVersionLocalizations/{l['id']}/appScreenshotSets?include=appScreenshots&limit=50")
            urls = {s["id"]: s["attributes"]["imageAsset"]["templateUrl"] for s in sets.get("included", []) if s["attributes"].get("imageAsset")}
            shots = []
            for s in sets["data"]:
                if s["attributes"]["screenshotDisplayType"] in ("APP_IPHONE_67", "APP_IPHONE_69"):
                    shots = [urls[x["id"]] for x in s["relationships"]["appScreenshots"]["data"] if x["id"] in urls][:SHOTS]
            locs[loc] = {"name": names.get(loc, {}).get("name"), "subtitle": names.get(loc, {}).get("subtitle"),
                         "promo": at.get("promotionalText") or "", "description": at["description"], "shots": shots}
        country = COUNTRY.get(slug, LOC.get(pl, LOC["en-GB"])[2])
        r = json.loads(get(f"https://itunes.apple.com/lookup?id={a['id']}&country={country}"))["results"]
        r = r[0] if r else {}
        apps[slug] = {"id": a["id"], "primary": pl, "country": country, "genre": r.get("primaryGenreName", ""),
                      "price": r.get("price", 0), "currency": r.get("currency", ""), "icon": r.get("artworkUrl512", ""),
                      "rating": round(r.get("averageUserRating", 0), 2), "ratings": r.get("userRatingCount", 0), "locales": locs}
        print(slug, len(locs), file=sys.stderr)
    json.dump(apps, open("landing/apps.json", "w"), ensure_ascii=False, indent=1, sort_keys=True)
    print(len(apps), "apps")


def desc_html(text):
    out = []
    for para in text.strip().split("\n\n"):
        lines = [x for x in para.split("\n") if x.strip()]
        if not lines or re.search(r"https?://", para):  # privacy/EULA links are on the footer already
            continue
        items = [x[2:] for x in lines if x[:2] in ("- ", "• ", "– ")]
        if items and len(items) == len(lines):
            out.append("<ul>" + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>")
        else:
            out.append("<p>" + "<br>".join(e(x) for x in lines) + "</p>")
    return "".join(out)


def clean(text):
    """Store texts may say "free" (description only); the web copy drops those sentences."""
    return "\n".join(" ".join(s for s in re.split(r"(?<=[.!?])\s+", line) if not FREE.search(s)) for line in text.split("\n"))


def bullets(text):
    return [x[2:].strip() for x in text.split("\n") if x[:2] in ("- ", "• ", "– ")][:5]


def save_img(url, path, w, h):
    if not os.path.exists(path):
        open(path, "wb").write(get(url.replace("{w}", str(w)).replace("{h}", str(h)).replace("{f}", "jpg")))


def build(only=None):
    apps = json.load(open("landing/apps.json"))
    slugs = json.load(open("landing/slugs.json")) if os.path.exists("landing/slugs.json") else {}
    taken = {(d, s): k for k, v in slugs.items() for d, s in v.items()}
    for rs, a in apps.items():  # pin a URL slug for every page first, so hreflang links are complete
        content = json.load(open(f"landing/content/{rs}.json")) if os.path.exists(f"landing/content/{rs}.json") else {}
        for loc, m in a["locales"].items():
            d = LOC[loc][0]
            if d in slugs.get(rs, {}):
                continue
            s = slugify(content.get(loc, {}).get("slug") or m["name"])
            if taken.get((d, s), rs) != rs:
                s = slugify(m["name"])
            if len(re.sub(r"[^a-z]", "", s)) < 3:  # Arabic name or bare year → repo slug
                s = rs
            assert taken.get((d, s), rs) == rs, (rs, d, s)
            slugs.setdefault(rs, {})[d] = s
            taken[(d, s)] = rs
    json.dump(slugs, open("landing/slugs.json", "w"), ensure_ascii=False, indent=1, sort_keys=True)
    urls = []
    for rs, a in apps.items():
        if only and rs != only:
            continue
        content = json.load(open(f"landing/content/{rs}.json")) if os.path.exists(f"landing/content/{rs}.json") else {}
        pages = {LOC[loc][0]: f"{LOC[loc][0]}/{slugs[rs][LOC[loc][0]]}/" for loc in a["locales"]}
        primary = pages[LOC[a["primary"]][0]] if a["primary"] in a["locales"] else next(iter(pages.values()))
        alts = "".join(f"<link rel='alternate' hreflang='{LOC[loc][1]}' href='{BASE}/{pages[LOC[loc][0]]}'>" for loc in a["locales"])
        alts += f"<link rel='alternate' hreflang='x-default' href='{BASE}/{primary}'>"
        for loc, m in a["locales"].items():
            m = dict(m, promo=clean(m["promo"]), description=clean(m["description"]))
            d, hl = LOC[loc][:2]
            out, c, u = pages[d], content.get(loc, {}), UI[d]
            os.makedirs(out, exist_ok=True)
            store = f"https://apps.apple.com/app/id{a['id']}?pt=322891&ct=landing-{d}"
            shots = m["shots"] or a["locales"].get(a["primary"], {}).get("shots", [])
            for i, url in enumerate(shots, 1):
                save_img(url, f"{out}{i}.jpg", 450, 978)
            if a["icon"]:
                save_img(re.sub(r"/\d+x\d+bb\.\w+$", "/{w}x{h}bb.{f}", a["icon"]), f"{out}icon.jpg", 128, 128)
            h1 = c.get("h1") or m["name"]
            lead = c.get("lead") or " ".join(x if x[-1:] in ".!?" else x + "." for x in (m["subtitle"], m["promo"]) if x)
            title = c.get("title") or (f"{m['name']} – {m['subtitle']}" if m["subtitle"] else m["name"])
            meta = c.get("description") or (m["promo"] or m["description"].split("\n")[0])[:155]
            bens = c.get("benefits") or [{"t": x, "d": ""} for x in bullets(m["description"])]
            faq = c.get("faq", [])
            url = f"{BASE}/{out}"
            img = f"{url}1.jpg" if shots else ""
            ld = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": m["name"], "description": meta,
                  "operatingSystem": "iOS", "applicationCategory": GENRE.get(a["genre"], "MobileApplication"), "inLanguage": hl,
                  "url": url, "downloadUrl": f"https://apps.apple.com/app/id{a['id']}", "image": img or None,
                  "publisher": {"@type": "Organization", "name": "Baytech BV"},
                  "offers": {"@type": "Offer", "price": f"{a['price']:g}", "priceCurrency": a["currency"]} if a["currency"] else None}
            if a["ratings"] >= MIN_RATINGS and a["rating"]:
                ld["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": a["rating"], "ratingCount": a["ratings"],
                                         "bestRating": 5, "worstRating": 1}
            ld = {k: v for k, v in ld.items() if v is not None}
            lds = [ld]
            if faq:
                lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                    {"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": q["a"]}} for q in faq]})
            jsonld = "".join("<script type='application/ld+json'>" + json.dumps(x, ensure_ascii=False).replace("</", "<\\/") + "</script>" for x in lds)
            icon = f"<img src='icon.jpg' alt='' width='64' height='64'>" if a["icon"] else ""
            imgs = "".join(f"<img src='{i}.jpg' alt='{e(m['name'])} – {i}' width='450' height='978'{' loading=lazy' if i > 1 else ''}>"
                           for i in range(1, len(shots) + 1))
            btn = (f"<a class='badge' href='{store}'><img src='../../landing/app-store-badge.svg'"
                   f" alt='{e(u[0])}' width='162' height='54'></a>")
            body = [f"<header>{icon}<div><h1>{e(h1)}</h1></div></header><p class='lead'>{e(lead)}</p>{btn}<div class='shots'>{imgs}</div>"]
            if c.get("definition"):
                body.append(f"<p class='def'>{e(c['definition'])}</p>")
            if bens:
                body.append("<ul class='ben'>" + "".join(f"<li><b>{e(b['t'])}</b>{'<br>' + e(b['d']) if b['d'] else ''}</li>" for b in bens) + "</ul>")
            cmp = c.get("compare")
            if cmp:
                th = "".join(f"<th>{e(x)}</th>" for x in cmp["head"])  # data-l = column label for the stacked mobile layout
                tds = "".join("<tr>" + "".join(f"<td{f' data-l={chr(39)}{e(h)}{chr(39)}' if h and i else ''}>{e(x)}</td>"
                                               for i, (h, x) in enumerate(zip(cmp["head"], r))) + "</tr>" for r in cmp["rows"])
                body.append(f"<h2>{e(cmp['title'])}</h2><div class='cmp'><table><thead><tr>{th}</tr></thead><tbody>{tds}</tbody></table></div>"
                            f"<p><small>{e(cmp['note'])}</small></p>")
            if rs in TESTS and TESTS[rs].startswith(d + "/") and os.path.exists(TESTS[rs]):  # quiztest.py page is live
                body.append(f"<p><a class='test' href='../../{TESTS[rs]}'>{e(u[3])} →</a></p>")
            if faq:
                body.append(f"<h2>{e(u[1])}</h2>" + "".join(f"<h3>{e(q['q'])}</h3><p>{e(q['a'])}</p>" for q in faq))
            body.append(f"<h2>{e(u[2])}</h2><div class='desc'>{desc_html(m['description'])}</div>{btn}")
            langs = " ".join(f"<a href='../../{p}' hreflang='{LOC[l][1]}'>{NAME[LOC[l][0]]}</a>" for l, p in
                             ((l, pages[LOC[l][0]]) for l in a["locales"]) if LOC[l][0] != d)
            body.append(f"<footer><a href='../../{rs}/support/'>{e(u[4])}</a><a href='../../{rs}/'>{e(u[5])}</a>"
                        f"{'<br>' + e(u[6]) + ': ' + langs if langs else ''}<br>© Baytech BV</footer>")
            page = (f"<!doctype html><html lang='{hl}'{' dir=rtl' if d == 'ar' else ''}><head><meta charset='utf-8'>"
                    f"<meta name='viewport' content='width=device-width,initial-scale=1'><title>{e(title)}</title>"
                    f"<meta name='description' content='{e(meta)}'><meta name='apple-itunes-app' content='app-id={a['id']}'>"
                    f"<link rel='canonical' href='{url}'>{alts}<meta property='og:type' content='website'>"
                    f"<meta property='og:title' content='{e(title)}'><meta property='og:description' content='{e(meta)}'>"
                    f"<meta property='og:url' content='{url}'>" + (f"<meta property='og:image' content='{img}'>" if img else "") +
                    f"<meta name='twitter:card' content='summary_large_image'>{jsonld}<style>{CSS}</style></head>"
                    f"<body>{''.join(body)}{CT_JS}</body></html>")
            hand = " ".join([title, meta, h1, lead, c.get("definition", ""), json.dumps([bens, faq, cmp], ensure_ascii=False)])
            seen = FREE.search(hand + re.sub(r"href='[^']*'", "", page))  # test-page URLs may say "gratis"; visible text may not
            assert not seen, (rs, loc, seen and seen.group(0))  # PUBLISH-PLAN §3.4: no "free" in sales copy
            open(f"{out}index.html", "w").write(page)
            urls.append(url)
        # old marketing URL: keep it working, send people and crawlers to the right language
        os.makedirs(f"{rs}/app", exist_ok=True)
        for f in os.listdir(f"{rs}/app"):
            os.remove(f"{rs}/app/{f}")
        hashes = json.dumps({LOC[l][0][:2] if LOC[l][0] != "nb" else "no": pages[LOC[l][0]] for l in a["locales"]})
        open(f"{rs}/app/index.html", "w").write(
            f"<!doctype html><html><head><meta charset='utf-8'><title>{e(apps[rs]['locales'][a['primary']]['name'] if a['primary'] in a['locales'] else rs)}</title>"
            f"<link rel='canonical' href='{BASE}/{primary}'><meta name='robots' content='noindex'>"
            f"<meta http-equiv='refresh' content='0;url=../../{primary}'><script>var m={hashes};"
            f"location.replace('../../'+(m[location.hash.slice(1)]||'{primary}')+location.search)</script></head>"
            f"<body><a href='../../{primary}'>{BASE}/{primary}</a></body></html>")
        print("ok", rs, len(pages), "pages")
    if not only:
        open("landing/urls.txt", "w").write("\n".join(sorted(urls)) + "\n")
        print(len(urls), "pages")
        llms(apps, slugs)


def llms(apps, slugs):
    """llms.txt (llmstxt.org): one line per app; llms-full.txt: definition, facts and FAQ per app, in the page languages."""
    short, full = [], []
    for rs, a in sorted(apps.items(), key=lambda x: x[1]["locales"].get("en-GB", x[1]["locales"].get(x[1]["primary"], {})).get("name") or x[0]):
        content = json.load(open(f"landing/content/{rs}.json")) if os.path.exists(f"landing/content/{rs}.json") else {}
        loc = "en-GB" if "en-GB" in a["locales"] else a["primary"] if a["primary"] in a["locales"] else next(iter(a["locales"]))
        m, c = a["locales"][loc], content.get(loc, {})
        url = f"{BASE}/{LOC[loc][0]}/{slugs[rs][LOC[loc][0]]}/"
        line = c.get("definition") or m["subtitle"] or ""
        short.append(f"- [{m['name']}]({url}): {line}".rstrip(": "))
        full.append(f"## {m['name']}\n\nApp Store: https://apps.apple.com/app/id{a['id']}\n")
        for l in a["locales"]:
            mm, cc = a["locales"][l], content.get(l, {})
            full.append(f"### {mm['name']} ({LOC[l][1]})\n\n{BASE}/{LOC[l][0]}/{slugs[rs][LOC[l][0]]}/\n")
            text = cc.get("definition") or cc.get("lead") or clean(mm["subtitle"] + ". " + mm["promo"]).strip(". ")
            if text:
                full.append(text + "\n")
            full += [f"- {b['t']}{': ' + b['d'] if b['d'] else ''}" for b in cc.get("benefits", [])] + [""] if cc.get("benefits") else []
            full += [f"Q: {q['q']}\nA: {q['a']}\n" for q in cc.get("faq", [])]
            if cc.get("compare"):
                cm = cc["compare"]
                full += [f"{cm['title']}\n", "| " + " | ".join(cm["head"]) + " |", "|" + "---|" * len(cm["head"])]
                full += ["| " + " | ".join(r) + " |" for r in cm["rows"]] + [f"\n{cm['note']}\n"]
    head = ("# Baytech BV apps\n\n> Independent iOS apps by Baytech BV (Amsterdam), mostly exam and test preparation for Northern and Western"
            " Europe: citizenship tests, boating, hunting, driving and trade licences. Each app has a page per App Store language."
            " The apps are not official and not affiliated with the exam authorities.\n\n"
            f"Full text with facts and FAQ per app: {BASE}/llms-full.txt\n\n## Apps\n\n")
    open("llms.txt", "w").write(head + "\n".join(short) + "\n")
    open("llms-full.txt", "w").write(head.split("Full text")[0] + "\n".join(full) + "\n")
    print("llms.txt", len(short), "apps")


if __name__ == "__main__":
    if sys.argv[1] == "fetch":
        fetch(sys.argv[2])
    else:
        build(sys.argv[2] if len(sys.argv) > 2 else None)
