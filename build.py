# Generates one static privacy page per app. Edit the APPS texts and re-run; each app's page is independent.
import os

CONTACT = "utqsall@gmail.com"
OWNER = "Mustafa Utku Bayık"
UPDATED = "2026-10-11"

T = {
    "en": dict(
        h="Privacy Policy", upd="Last updated", who="Who we are",
        who_t=f"This app is published by {OWNER}. Contact: <a href='mailto:{CONTACT}'>{CONTACT}</a>.",
        data="What data the app processes",
        data_t="The app does not require an account and does not collect, store on servers or share any personal data. "
               "Your learning progress, settings and exam results are stored only on your device.",
        no="No tracking, analytics or ads",
        no_t="The app contains no advertising, no analytics or crash-reporting SDKs and does not track you across apps or websites.",
        buy="Purchases", buy_t="The one-time in-app purchase is handled entirely by Apple via the App Store. We do not receive your payment details. "
               "See <a href='https://www.apple.com/legal/privacy/'>Apple's Privacy Policy</a>.",
        rate="Ratings", rate_t="The app may ask you to rate it using Apple's standard rating dialog. Ratings are handled by Apple.",
        del_="Deleting your data", del_t="Deleting the app removes all data it stored on your device.",
        rights="Your rights", rights_t="If you have questions about this policy or your data, contact us at the address above. "
               "Since we hold no personal data about you, there is nothing for us to access, correct or delete.",
        chg="Changes", chg_t="We may update this policy. The date above shows the latest version."),
    "de": dict(
        h="Datenschutzerklärung", upd="Stand", who="Verantwortlicher",
        who_t=f"Diese App wird von {OWNER} veröffentlicht. Kontakt: <a href='mailto:{CONTACT}'>{CONTACT}</a>.",
        data="Welche Daten die App verarbeitet",
        data_t="Die App benötigt kein Konto und erhebt, speichert auf Servern oder teilt keine personenbezogenen Daten. "
               "Lernfortschritt, Einstellungen und Prüfungsergebnisse werden ausschließlich auf deinem Gerät gespeichert.",
        no="Kein Tracking, keine Analyse, keine Werbung",
        no_t="Die App enthält keine Werbung, keine Analyse- oder Absturzberichts-SDKs und verfolgt dich nicht über Apps oder Websites hinweg.",
        buy="Käufe", buy_t="Der einmalige In-App-Kauf wird vollständig von Apple über den App Store abgewickelt. Wir erhalten keine Zahlungsdaten. "
               "Siehe <a href='https://www.apple.com/de/legal/privacy/'>Datenschutzrichtlinie von Apple</a>.",
        rate="Bewertungen", rate_t="Die App kann dich über den Standarddialog von Apple um eine Bewertung bitten. Bewertungen verarbeitet Apple.",
        del_="Daten löschen", del_t="Wenn du die App löschst, werden alle von ihr auf deinem Gerät gespeicherten Daten entfernt.",
        rights="Deine Rechte", rights_t="Bei Fragen zu dieser Erklärung oder zu deinen Daten (Art. 15–21 DSGVO) wende dich an die obige Adresse. "
               "Da wir keine personenbezogenen Daten über dich speichern, gibt es nichts, worüber wir Auskunft geben oder was wir berichtigen oder löschen müssten.",
        chg="Änderungen", chg_t="Wir können diese Erklärung anpassen. Das Datum oben zeigt die aktuelle Fassung."),
    "nl": dict(
        h="Privacybeleid", upd="Laatst bijgewerkt", who="Wie wij zijn",
        who_t=f"Deze app wordt uitgegeven door {OWNER}. Contact: <a href='mailto:{CONTACT}'>{CONTACT}</a>.",
        data="Welke gegevens de app verwerkt",
        data_t="De app heeft geen account nodig en verzamelt, bewaart op servers of deelt geen persoonsgegevens. "
               "Je voortgang, instellingen en examenresultaten worden alleen op je apparaat opgeslagen.",
        no="Geen tracking, analyse of advertenties",
        no_t="De app bevat geen advertenties, geen analyse- of crashrapportage-SDK's en volgt je niet via andere apps of websites.",
        buy="Aankopen", buy_t="De eenmalige in-app-aankoop wordt volledig door Apple via de App Store afgehandeld. Wij ontvangen geen betaalgegevens. "
               "Zie het <a href='https://www.apple.com/nl/legal/privacy/'>privacybeleid van Apple</a>.",
        rate="Beoordelingen", rate_t="De app kan je via het standaardvenster van Apple om een beoordeling vragen. Beoordelingen worden door Apple verwerkt.",
        del_="Gegevens verwijderen", del_t="Als je de app verwijdert, worden alle gegevens die de app op je apparaat heeft opgeslagen verwijderd.",
        rights="Je rechten", rights_t="Heb je vragen over dit beleid of je gegevens (AVG)? Neem contact op via het adres hierboven. "
               "Omdat wij geen persoonsgegevens over je bewaren, is er niets om in te zien, te corrigeren of te verwijderen.",
        chg="Wijzigingen", chg_t="We kunnen dit beleid aanpassen. De datum hierboven toont de nieuwste versie."),
}

# Per-app extras (keyed by language). Keep app-specific facts here so pages can diverge later.
APPS = {
    "inburgering-examen": ("Inburgering Examen", ["nl", "en"], {}),
    "vca-examen": ("VCA Examen – Basis & VOL", ["nl", "en"], {
        "nl": ("Voorlezen", "De voorleesfunctie gebruikt de spraakfunctie van iOS op je apparaat. Er wordt geen audio opgenomen of verstuurd."),
        "en": ("Read aloud", "The read-aloud feature uses the on-device iOS speech engine. No audio is recorded or sent anywhere."),
    }),
    "sachkunde-34a": ("34a Sachkunde Prüfung", ["de", "en"], {
        "de": ("Externe Links", "Gesetzesverweise öffnen öffentliche Webseiten (z. B. gesetze-im-internet.de) in deinem Browser. Dort gelten die Datenschutzbestimmungen des jeweiligen Anbieters."),
        "en": ("External links", "Legal references open public websites (e.g. gesetze-im-internet.de) in your browser. Those sites' own privacy policies apply."),
    }),
    "fischereischein": ("Fischereischein: Angelschein", ["de", "en"], {}),
    "golf-platzreife": ("Platzreife: Golfregeln Quiz", ["de", "nl", "en"], {}),
}

CSS = """:root{--bg:#fff;--fg:#1c1c1e;--mu:#6b6b70;--ac:#0a66c2}
@media (prefers-color-scheme:dark){:root{--bg:#111;--fg:#eee;--mu:#9a9aa0;--ac:#5aa9ff}}
body{background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:720px;margin:0 auto;padding:24px 16px}
h1{font-size:1.6em;margin-bottom:.2em}h2{font-size:1.15em;margin-top:1.6em}a{color:var(--ac)}
.mu{color:var(--mu)}nav a{margin-right:12px}hr{border:0;border-top:1px solid var(--mu);opacity:.3;margin:40px 0}"""


def section(lang, name, extra):
    t = T[lang]
    parts = [f"<section id='{lang}' lang='{lang}'><h1>{t['h']} – {name}</h1><p class='mu'>{t['upd']}: {UPDATED}</p>"]
    for k in ("who", "data", "no", "buy", "rate"):
        parts.append(f"<h2>{t[k]}</h2><p>{t[k + '_t']}</p>")
    if lang in extra:
        parts.append(f"<h2>{extra[lang][0]}</h2><p>{extra[lang][1]}</p>")
    for k in ("del_", "rights", "chg"):
        parts.append(f"<h2>{t[k]}</h2><p>{t[k.rstrip('_') + '_t']}</p>")
    return "".join(parts) + "</section>"


for slug, (name, langs, extra) in APPS.items():
    os.makedirs(slug, exist_ok=True)
    nav = "".join(f"<a href='#{l}'>{l.upper()}</a>" for l in langs)
    body = "<hr>".join(section(l, name, extra) for l in langs)
    with open(f"{slug}/index.html", "w") as f:
        f.write(f"<!doctype html><html lang='{langs[0]}'><head><meta charset='utf-8'>"
                f"<meta name='viewport' content='width=device-width,initial-scale=1'>"
                f"<title>{name} – Privacy</title><style>{CSS}</style></head>"
                f"<body><nav>{nav}</nav>{body}</body></html>")

links = "".join(f"<li><a href='{s}/'>{n}</a></li>" for s, (n, _, _) in APPS.items())
with open("index.html", "w") as f:
    f.write(f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>Privacy Policies</title><style>{CSS}</style></head><body><h1>Privacy Policies</h1><ul>{links}</ul></body></html>")

if __name__ == "__main__":
    for slug in APPS:
        s = open(f"{slug}/index.html").read()
        assert CONTACT in s and "Apple" in s, slug
    print("ok", list(APPS))
