# Exam guide pages (dates, fees, syllabus, pass rate, FAQ), one per exam app, at <lang>/<slug>/ (Article + FAQPage JSON-LD).
#   python3 guide.py [repo-slug]
# Copy lives in guide/<repo-slug>.json; every number in it needs a source in "sources" (official sites only).
# Section bodies are hand-written HTML; FAQ answers are plain text (they go into JSON-LD too).
# Refresh schedule: baytech/_drafts/rehber/TAKVIM.md. Re-run landing.py build first if a web test page was added.
import json, os, re, sys
from landing import BASE, CSS, FREE, TESTS, UI, e

APPS = json.load(open("landing/apps.json"))
SLUGS = json.load(open("landing/slugs.json"))
CSS += """table{border-collapse:collapse;width:100%;margin:8px 0}th,td{text-align:left;padding:6px 8px;border-bottom:1px solid rgba(128,128,128,.25);vertical-align:top}
.upd{color:var(--mu);font-size:.9em}.src{font-size:.9em}.cta{background:var(--card);border-radius:12px;padding:12px 14px;margin:18px 0}"""
# per lang dir: last updated, sources, app box title, read more about the app
T = {"da": ("Sidst opdateret", "Kilder", "Øv med appen", "Læs mere om appen"),
     "nb": ("Sist oppdatert", "Kilder", "Øv med appen", "Les mer om appen"),
     "sv": ("Senast uppdaterad", "Källor", "Öva med appen", "Läs mer om appen"),
     "nl": ("Laatst bijgewerkt", "Bronnen", "Oefenen met de app", "Meer over de app")}


def build(rs):
    c, a = json.load(open(f"guide/{rs}.json")), APPS[rs]
    d, out, u, t = c["dir"], f"{c['dir']}/{c['slug']}/", UI[c["dir"]], T[c["dir"]]
    url, landing = f"{BASE}/{out}", f"../../{d}/{SLUGS[rs][d]}/"
    store = f"https://apps.apple.com/app/id{a['id']}?pt=322891&ct=guide"
    test = TESTS.get(rs)
    test = test if test and test.startswith(d + "/") and os.path.exists(test) else None  # quiztest.py page is live
    lds = [{"@context": "https://schema.org", "@type": "Article", "headline": c["h1"], "description": c["description"],
            "inLanguage": d, "datePublished": c.get("published", c["updated"]), "dateModified": c["updated"],
            "mainEntityOfPage": url, "author": {"@type": "Organization", "name": "Baytech BV"},
            "publisher": {"@type": "Organization", "name": "Baytech BV"}, "citation": [s["url"] for s in c["sources"]]},
           {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
               {"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": q["a"]}} for q in c["faq"]]}]
    jsonld = "".join("<script type='application/ld+json'>" + json.dumps(x, ensure_ascii=False).replace("</", "<\\/") + "</script>" for x in lds)
    badge = f"<a class='badge' href='{store}'><img src='../../landing/app-store-badge.svg' alt='{e(u[0])}' width='162' height='54'></a>"
    cta = (f"<div class='cta'><b>{e(t[2])}: {e(c['app'])}</b><br>{e(c['cta'])}"
           + (f"<p><a class='test' href='../../{test}'>{e(u[3])} →</a></p>" if test else "")
           + f"{badge}<a href='{landing}'>{e(t[3])} →</a></div>")
    body = [f"<h1>{e(c['h1'])}</h1><p class='upd'>{e(t[0])}: <time datetime='{c['updated']}'>{e(c['updated_text'])}</time></p>",
            f"<p class='lead'>{e(c['lead'])}</p>"]
    for i, s in enumerate(c["sections"]):
        body.append(f"<h2>{e(s['h'])}</h2>{s['html']}")
        if i == 1:
            body.append(cta)
    body.append(f"<h2>{e(u[1])}</h2>" + "".join(f"<h3>{e(q['q'])}</h3><p>{e(q['a'])}</p>" for q in c["faq"]))
    body.append(cta)
    body.append(f"<h2>{e(t[1])}</h2><ul class='src'>" + "".join(
        f"<li><a href='{e(s['url'])}' rel='noopener'>{e(s['name'])}</a></li>" for s in c["sources"]) + "</ul>")
    body.append(f"<p class='desc'>{e(c['disclaimer'])}</p><footer><a href='../../{rs}/support/'>{e(u[4])}</a>"
                f"<a href='../../{rs}/'>{e(u[5])}</a><br>© Baytech BV</footer>")
    page = (f"<!doctype html><html lang='{d}'><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width,initial-scale=1'><title>{e(c['title'])}</title>"
            f"<meta name='description' content='{e(c['description'])}'><meta name='apple-itunes-app' content='app-id={a['id']}'>"
            f"<link rel='canonical' href='{url}'><meta property='og:type' content='article'>"
            f"<meta property='og:title' content='{e(c['title'])}'><meta property='og:description' content='{e(c['description'])}'>"
            f"<meta property='og:url' content='{url}'><meta property='article:modified_time' content='{c['updated']}'>"
            f"{jsonld}<style>{CSS}</style></head><body>{''.join(body)}</body></html>")
    seen = FREE.search(re.sub(r"<[^>]+>", " ", page.split("</head>")[1]) + c["title"] + c["description"])
    assert not seen, (rs, seen.group(0))  # PUBLISH-PLAN §3.4: no "free" in our copy
    os.makedirs(out, exist_ok=True)
    open(f"{out}index.html", "w").write(page)
    print(url)


if __name__ == "__main__":
    for f in sorted(os.listdir("guide")):
        if f.endswith(".json") and (len(sys.argv) < 2 or f[:-5] == sys.argv[1]):
            build(f[:-5])
