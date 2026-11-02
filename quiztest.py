# Free 25-question web practice test per exam app at <lang>/<slug>/ (SEO entry page → App Store, ct=web-test).
# Questions are read from the app repo's origin/main (git show), so the page follows the shipped question bank:
#   python3 quiztest.py ~/Documents/Projects/baytech [key]   (key: only that test)
# New app: add an entry to TESTS (and a UI dict to UI if the language is new). Only text questions are used (no image/input).
import html, json, random, subprocess, sys

SRC = sys.argv[1] if len(sys.argv) > 1 else "../baytech"
from landing import BASE  # single base URL (SITE_BASE env)
N = 25

TESTS = {
    "indfodsret": dict(
        repo="indfodsretsprove-dk", app_id=6823126416, app="Indfødsretsprøven", lang="da", slug="indfodsretsprove-gratis-test",
        quiz=["ios/Content/indfodsret.json"], count=["ios/Content/indfodsret.json", "ios/Content/medborgerskab.json"],
        title="Indfødsretsprøven: gratis prøvetest med 25 spørgsmål og svar",
        desc="Test din viden før indfødsretsprøven: 25 gratis spørgsmål om Danmarks historie, grundlov og samfund, med svar og forklaring. Ingen tilmelding.",
        h1="Gratis prøvetest til indfødsretsprøven",
        intro="Øv dig gratis på 25 spørgsmål om de samme emner som indfødsretsprøven: Danmarks historie, kultur, grundloven, "
              "samfundet og danske værdier. Vælg et svar og se med det samme, om det er rigtigt, og hvorfor.",
        about="Indfødsretsprøven"),
    "statsborger": dict(
        repo="statsborgerprove-no", app_id=6823126983, app="Statsborgerprøven", lang="nb", slug="statsborgerproven-gratis-test",
        quiz=["ios/Content/statsborger.json"], count=["ios/Content/statsborger.json"],
        title="Statsborgerprøven: gratis prøvetest med 25 spørsmål og svar",
        desc="Øv gratis til statsborgerprøven: 25 spørsmål om norsk historie, demokrati og samfunn, med svar og forklaring. Ingen registrering.",
        h1="Gratis prøvetest til statsborgerprøven",
        intro="Øv gratis på 25 spørsmål om de samme temaene som statsborgerprøven: historie, demokrati, rettigheter og plikter, "
              "arbeidsliv, helse og familie. Velg et svar og se med en gang om det er riktig, og hvorfor.",
        about="Statsborgerprøven"),
    "kvb": dict(
        repo="klein-vaarbewijs-nl", app_id=6824009558, app="Vaarbewijs KVB 1 & 2 Oefenen", lang="nl", slug="vaarbewijs-oefenen-gratis",
        quiz="ios/Content/questions/", count="ios/Content/questions/", skip_kinds={"kaart"},
        title="Vaarbewijs oefenen gratis: KVB oefenexamen met 25 vragen",
        desc="Oefen gratis voor je klein vaarbewijs: 25 vragen over vaarregels, verlichting, betonning en veiligheid, met antwoord en uitleg. Zonder account.",
        h1="Gratis oefenexamen klein vaarbewijs (KVB 1 & 2)",
        intro="Oefen gratis met 25 vragen over de onderwerpen van het CBR-examen klein vaarbewijs: vaarregels, verlichting, "
              "geluidsseinen, borden, betonning en veiligheid. Kies een antwoord en zie meteen of het goed is, en waarom.",
        about="Klein vaarbewijs"),
}

UI = {
    "da": dict(prog="{n} af {t} besvaret · {c} rigtige", right="Rigtigt!", wrong="Forkert. Rigtigt svar:",
               res="Du fik {c} af {t} rigtige ({p} %).", hi="Flot! Du er godt på vej.", mid="Godt begyndt. Øv de emner, du missede.",
               lo="Bliv ved med at øve, det kommer.", cta="Der er {r} spørgsmål mere i appen, med træning per emne og prøveeksamen på tid.",
               retry="Prøv igen", badge="Hent i App Store",
               note="Spørgsmålene er skrevet af os og er ikke de officielle prøvespørgsmål. Dette er ikke en officiel side."),
    "nb": dict(prog="{n} av {t} besvart · {c} riktige", right="Riktig!", wrong="Feil. Riktig svar:",
               res="Du fikk {c} av {t} riktige ({p} %).", hi="Bra! Du er godt i gang.", mid="God start. Øv mer på temaene du bommet på.",
               lo="Fortsett å øve, det kommer.", cta="Det er {r} spørsmål til i appen, med øving per tema og prøveeksamen på tid.",
               retry="Prøv igjen", badge="Last ned fra App Store",
               note="Spørsmålene er skrevet av oss og er ikke de offisielle prøvespørsmålene. Dette er ikke en offisiell side."),
    "nl": dict(prog="{n} van {t} beantwoord · {c} goed", right="Goed!", wrong="Fout. Juiste antwoord:",
               res="Je hebt {c} van de {t} goed ({p}%).", hi="Top! Je bent goed op weg.", mid="Goed begin. Oefen de onderwerpen die je miste.",
               lo="Blijf oefenen, het komt goed.", cta="In de app staan nog {r} vragen, met oefenen per onderwerp, kaartvragen en oefenexamens zoals bij het CBR.",
               retry="Opnieuw", badge="Download in de App Store",
               note="De vragen zijn door ons geschreven; het zijn geen officiële CBR-examenvragen. Dit is geen officiële CBR-site."),
}

CSS = """:root{--bg:#fff;--fg:#1c1c1e;--mu:#6b6b70;--ac:#0a66c2;--bd:#d9d9de;--ok:#1a7f37;--ko:#c62828;--okb:#e8f5ec;--kob:#fdecea}
@media (prefers-color-scheme:dark){:root{--bg:#121214;--fg:#ececf0;--mu:#a0a0a8;--ac:#6cb2ff;--bd:#3a3a40;--ok:#5cd17f;--ko:#ff7b72;--okb:#14301d;--kob:#3a1716}}
body{font:17px/1.55 -apple-system,system-ui,sans-serif;max-width:680px;margin:0 auto;padding:16px;background:var(--bg);color:var(--fg);overflow-wrap:anywhere}
h1{font-size:1.6em;line-height:1.25;margin:.4em 0}.lead{color:var(--mu)}a{color:var(--ac)}
ol{padding:0;list-style:none;counter-reset:q}li.q{counter-increment:q;border-top:1px solid var(--bd);padding:16px 0}li.q:first-child{border-top:0}
li.q>p:first-child::before{content:counter(q) ". ";font-weight:600}
button{font:inherit;display:block;width:100%;text-align:left;margin:8px 0;padding:10px 14px;border:1px solid var(--bd);border-radius:10px;background:none;color:inherit;cursor:pointer}
button:disabled{cursor:default}.ok{border-color:var(--ok);background:var(--okb)}.ko{border-color:var(--ko);background:var(--kob)}
.x{color:var(--mu);margin:8px 0 0}.bar{position:sticky;top:0;background:var(--bg);padding:8px 0;border-bottom:1px solid var(--bd);font-weight:600}
#res{border:2px solid var(--ac);border-radius:14px;padding:16px;margin:24px 0}#res .big{font-size:1.3em;font-weight:700;margin:0}
.badge{display:inline-block;margin:8px 0}.badge img{display:block;height:54px;width:auto}.retry{width:auto;display:inline-block}
small{color:var(--mu)}"""

JS = """const L=document.querySelectorAll('li.q'),T=L.length,U=JSON.parse(document.getElementById('ui').textContent);let n=0,c=0;
function bar(){document.getElementById('bar').textContent=U.prog.replace('{n}',n).replace('{t}',T).replace('{c}',c)}
L.forEach(li=>li.querySelectorAll('button').forEach(b=>b.onclick=()=>{const bs=li.querySelectorAll('button'),k=+li.dataset.k,ok=b.dataset.i==k;
bs.forEach(x=>{x.disabled=true;if(x.dataset.i==k)x.classList.add('ok')});if(!ok)b.classList.add('ko');n++;if(ok)c++;
const x=li.querySelector('.x');x.querySelector('b').textContent=ok?U.right:U.wrong+' '+bs[k].textContent+'.';x.hidden=false;bar();
if(n==T){const r=document.getElementById('res'),p=Math.round(100*c/T);r.querySelector('.big').textContent=U.res.replace('{c}',c).replace('{t}',T).replace('{p}',p);
r.querySelector('.msg').textContent=p>=80?U.hi:p>=50?U.mid:U.lo;r.hidden=false;r.scrollIntoView({behavior:'smooth'})}}));
document.querySelector('.retry').onclick=()=>location.reload();bar();"""


def git_json(repo, path):
    return json.loads(subprocess.check_output(["git", "-C", f"{SRC}/{repo}", "show", f"origin/main:{path}"]))


def load(repo, paths):
    if isinstance(paths, str):  # a folder: every .json in it
        ls = subprocess.check_output(["git", "-C", f"{SRC}/{repo}", "ls-tree", "--name-only", "origin/main", paths], text=True)
        paths = sorted(p for p in ls.split() if p.endswith(".json"))
    return [q for p in paths for q in git_json(repo, p)["questions"]]


def pick(t):
    qs = [q for q in load(t["repo"], t["quiz"]) if "image" not in q and "input" not in q and q.get("kind") not in t.get("skip_kinds", ())]
    rnd, topics = random.Random(t["slug"]), {}
    for q in sorted(qs, key=lambda q: q["id"]):
        topics.setdefault(q["topic"], []).append(q)
    for v in topics.values():
        rnd.shuffle(v)
    out = []
    while len(out) < N:  # round-robin over topics so every topic is in the test
        for v in topics.values():
            if v and len(out) < N:
                out.append(v.pop())
    res = []
    for q in out:
        k = q["correctIndex"] if "correctIndex" in q else q["correct"][0]
        opts = list(enumerate(q["options"]))
        random.Random(q["id"]).shuffle(opts)  # bank stores the answer first; stable order per question
        ex = q["explanation"]
        res.append(dict(prompt=q["prompt"], options=[o for _, o in opts], k=[i for i, _ in opts].index(k),
                        x=ex.get(t["lang"]) or next(iter(ex.values())) if isinstance(ex, dict) else ex))
    return res


def page(key, t):
    u, e = UI[t["lang"]], html.escape
    qs, total = pick(t), len(load(t["repo"], t["count"]))
    url = f"{BASE}/{t['lang']}/{t['slug']}/"
    store = f"https://apps.apple.com/app/id{t['app_id']}?pt=322891&ct=web-test"
    badge = (f"<a class='badge' href='{store}'><img src='https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg' alt='{e(u['badge'])}' width='162' height='54'></a>")
    items = "".join(
        f"<li class='q' data-k='{q['k']}'><p>{e(q['prompt'])}</p>"
        + "".join(f"<button type='button' data-i='{i}'>{e(o)}</button>" for i, o in enumerate(q["options"]))
        + f"<p class='x' hidden><b></b> {e(q['x'])}</p></li>" for q in qs)
    ld = {"@context": "https://schema.org", "@type": "Quiz", "name": t["h1"], "description": t["desc"], "inLanguage": t["lang"],
          "url": url, "isAccessibleForFree": True, "about": {"@type": "Thing", "name": t["about"]},
          "provider": {"@type": "Organization", "name": "Baytech BV"},
          "hasPart": [{"@type": "Question", "eduQuestionType": "Multiple choice", "text": q["prompt"],
                       "suggestedAnswer": [{"@type": "Answer", "text": o} for i, o in enumerate(q["options"]) if i != q["k"]],
                       "acceptedAnswer": {"@type": "Answer", "text": q["options"][q["k"]],
                                          "answerExplanation": {"@type": "Comment", "text": q["x"]}}} for q in qs]}
    ld = json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")
    ui = {k: u[k] for k in ("prog", "right", "wrong", "res", "hi", "mid", "lo")}
    return (f"<!doctype html><html lang='{t['lang']}'><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width,initial-scale=1'><title>{e(t['title'])}</title>"
            f"<meta name='description' content='{e(t['desc'])}'><link rel='canonical' href='{url}'>"
            f"<meta name='apple-itunes-app' content='app-id={t['app_id']}'>"
            f"<meta property='og:title' content='{e(t['title'])}'><meta property='og:description' content='{e(t['desc'])}'>"
            f"<meta property='og:url' content='{url}'><meta property='og:type' content='website'>"
            f"<script type='application/ld+json'>{ld}</script>"
            f"<style>{CSS}</style></head><body><h1>{e(t['h1'])}</h1><p class='lead'>{e(t['intro'])}</p>{badge}"
            f"<div class='bar' id='bar'></div><ol>{items}</ol>"
            f"<section id='res' hidden><p class='big'></p><p class='msg'></p>"
            f"<p>{e(u['cta'].format(r=total - N))}</p>{badge}<p><button type='button' class='retry'>{e(u['retry'])}</button></p></section>"
            f"<p><small>{e(u['note'])} <a href='../../{t['repo']}/app/'>{e(t['app'])}</a> · "
            f"<a href='../../{t['repo']}/'>Privacy</a></small></p>"
            f"<script type='application/json' id='ui'>{json.dumps(ui, ensure_ascii=False)}</script><script>{JS}</script></body></html>")


if __name__ == "__main__":
    import os
    for key, t in TESTS.items():
        if len(sys.argv) > 2 and key != sys.argv[2]:
            continue
        out = f"{t['lang']}/{t['slug']}"
        os.makedirs(out, exist_ok=True)
        doc = page(key, t)
        assert doc.count("class='q'") == N, key
        open(f"{out}/index.html", "w").write(doc)
        print(f"{out}/index.html", len(doc) // 1024, "KB")
