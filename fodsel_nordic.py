# Privacy + support pages for Fødselsklar / Synnytysvalmis (fodsel-nordic/). Separate from build.py: a health app with
# partner sharing through the user's own iCloud and analytics that never contain health values.
# Button names quoted here must match the app (ios/scripts/strings.py in BaytechBV/fodsel-nordic).
import os

CONTACT = "utqsall@gmail.com"
OWNER = "Mustafa Utku Bayık"
UPDATED = "2026-10-17"
SLUG, NAME = "fodsel-nordic", "Fødselsklar"
M = f"<a href='mailto:{CONTACT}'>{CONTACT}</a>"
REFUND = "<a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>"
GA = ("<a href='https://policies.google.com/privacy'>Google</a>", "<a href='https://firebase.google.com/support/privacy'>Firebase</a>")

P = {
    "nb": [("Personvernerklæring", "Sist oppdatert"),
           ("Hvem vi er", f"Appen er utgitt av {OWNER}. Kontakt: {M}."),
           ("Det du skriver inn", "Appen trenger ingen konto. Rier, regelen fra jordmor, sykehusbag, fødselsplan, kontakter, bevegelsesdagbok og termin "
            "lagres bare på telefonen din. Vi har ingen server og får aldri tilgang til disse opplysningene."),
           ("Deling med partner (iCloud)", "Velger du å dele, lagres det du har valgt i Partner-skjermen i din egen iCloud-konto og deles med personen du "
            "inviterer, via Apples CloudKit. Vi har ikke tilgang til dataene. Du kan når som helst trykke «Stopp deling»; partneren kan trykke «Forlat delingen». "
            "Se <a href='https://www.apple.com/no/legal/privacy/'>Apples personvernerklæring</a>."),
           ("Bruksstatistikk (Google Analytics for Firebase)", "For å se hvilke deler av appen som brukes, sender appen anonyme hendelser til Google Analytics for "
            "Firebase (Google Ireland Ltd.): hvilke skjermer som åpnes, hvilke knapper som trykkes, kjøpssteg og kjøpshendelser (produkt og pris). Hendelsene inneholder aldri helseopplysninger: "
            "ingen tider, rier, intervaller, termin, uke, regel, plan, bevegelser, kontakter eller annen tekst du skriver. SDK-en registrerer også tekniske data "
            "(appversjon, iOS-versjon, enhetsmodell, omtrentlig plassering – land/region – som Google utleder fra IP-adressen, og tekniske installasjonsdata fra Firebase Installations) og en tilfeldig app-ID som nullstilles når du sletter appen. "
            "Ingen reklame-ID (IDFA), ingen reklame, ingen sporing. Rettslig grunnlag: berettiget interesse i å forbedre appen (GDPR art. 6(1)(f)). "
            f"Hendelsesdata slettes etter 2 måneder. Slå av under Innstillinger › «Send bruksstatistikk». Mer: {GA[0]}, {GA[1]}."),
           ("Kjøp", "Engangskjøpet håndteres helt av Apple via App Store. Vi får ikke betalingsopplysningene dine."),
           ("Telefonsamtaler", "Ringeknappene åpner telefonappen med nummeret du selv har skrevet inn. Appen har ingen innebygde numre utenom nødnummeret."),
           ("Vurderinger", "Appen kan be om en vurdering med Apples vanlige dialog, bare etter at du har markert at babyen er født."),
           ("Slette data", "Innstillinger › «Slett alle data» sletter alt fra telefonen. Når du sletter appen, slettes også alt den har lagret på enheten. "
            "Delte data i iCloud fjernes med «Stopp deling»."),
           ("Dine rettigheter", "Har du spørsmål, kontakt oss på adressen over. Fordi statistikken ikke er knyttet til deg, kan vi ikke finne dine data i den."),
           ("Ikke medisinske råd", "Appen fører logg og hjelper deg å huske. Den gir ikke medisinske råd. Ring jordmor eller fødeavdelingen hvis du er usikker."),
           ("Endringer", "Vi kan endre denne erklæringen. Datoen over viser gjeldende versjon.")],
    "da": [("Privatlivspolitik", "Sidst opdateret"),
           ("Hvem vi er", f"Appen udgives af {OWNER}. Kontakt: {M}."),
           ("Det, du skriver", "Appen kræver ingen konto. Veer, jordemoderens regel, hospitalstaske, fødeplan, kontakter, bevægelsesdagbog og termin "
            "gemmes kun på din telefon. Vi har ingen server og får aldrig adgang til disse oplysninger."),
           ("Deling med partner (iCloud)", "Vælger du at dele, gemmes det, du har valgt på Partner-skærmen, i din egen iCloud-konto og deles med den person, du "
            "inviterer, via Apples CloudKit. Vi har ikke adgang til dataene. Du kan når som helst trykke »Stop deling«; din partner kan trykke »Forlad delingen«. "
            "Se <a href='https://www.apple.com/dk/legal/privacy/'>Apples privatlivspolitik</a>."),
           ("Brugsstatistik (Google Analytics for Firebase)", "For at se, hvilke dele af appen der bruges, sender appen anonyme hændelser til Google Analytics for "
            "Firebase (Google Ireland Ltd.): hvilke skærme der åbnes, hvilke knapper der trykkes på, købstrin og købshændelser (produkt og pris). Hændelserne indeholder aldrig helbredsoplysninger: "
            "ingen tider, veer, intervaller, termin, uge, regel, plan, bevægelser, kontakter eller anden tekst, du skriver. SDK'et registrerer også tekniske data "
            "(appversion, iOS-version, enhedsmodel, omtrentlig placering – land/region – som Google udleder af IP-adressen, og tekniske installationsdata fra Firebase Installations) og et tilfældigt app-id, der nulstilles, når du sletter appen. "
            "Intet reklame-id (IDFA), ingen reklamer, ingen sporing. Retsgrundlag: legitim interesse i at forbedre appen (GDPR art. 6, stk. 1, litra f). "
            f"Hændelsesdata slettes efter 2 måneder. Slå fra under Indstillinger › »Send brugsstatistik«. Mere: {GA[0]}, {GA[1]}."),
           ("Køb", "Engangskøbet håndteres helt af Apple via App Store. Vi får ikke dine betalingsoplysninger."),
           ("Opkald", "Ringeknapperne åbner telefonappen med det nummer, du selv har skrevet. Appen har ingen indbyggede numre ud over alarmnummeret."),
           ("Bedømmelser", "Appen kan bede om en bedømmelse med Apples almindelige dialog, kun efter at du har markeret, at barnet er født."),
           ("Slet data", "Indstillinger › »Slet alle data« sletter alt fra telefonen. Når du sletter appen, slettes også alt, den har gemt på enheden. "
            "Delte data i iCloud fjernes med »Stop deling«."),
           ("Dine rettigheder", "Har du spørgsmål, så kontakt os på adressen ovenfor. Da statistikken ikke er knyttet til dig, kan vi ikke finde dine data i den."),
           ("Ikke medicinsk rådgivning", "Appen fører log og hjælper dig med at huske. Den giver ikke medicinsk rådgivning. Ring til jordemoderen eller fødestedet, hvis du er i tvivl."),
           ("Ændringer", "Vi kan ændre denne politik. Datoen ovenfor viser den gældende version.")],
    "fi": [("Tietosuojaseloste", "Päivitetty"),
           ("Keitä olemme", f"Sovelluksen julkaisija on {OWNER}. Yhteystiedot: {M}."),
           ("Kirjoittamasi tiedot", "Sovellus ei vaadi tiliä. Supistukset, kätilön ohje, sairaalakassi, synnytystoiveet, yhteystiedot, liikepäiväkirja ja laskettu aika "
            "tallentuvat vain puhelimeesi. Meillä ei ole palvelinta, emmekä koskaan näe näitä tietoja."),
           ("Jakaminen kumppanin kanssa (iCloud)", "Jos valitset jakamisen, Kumppani-näkymässä valitsemasi tiedot tallentuvat omaan iCloud-tiliisi ja jaetaan "
            "kutsumallesi henkilölle Applen CloudKitin kautta. Meillä ei ole pääsyä tietoihin. Voit milloin tahansa painaa ”Lopeta jakaminen”; kumppani voi painaa ”Poistu jaosta”. "
            "Katso <a href='https://www.apple.com/fi/legal/privacy/'>Applen tietosuojakäytäntö</a>."),
           ("Käyttötilastot (Google Analytics for Firebase)", "Nähdäksemme, mitä sovelluksen osia käytetään, sovellus lähettää nimettömiä tapahtumia Google Analytics for "
            "Firebaseen (Google Ireland Ltd.): mitä näyttöjä avataan, mitä painikkeita painetaan, ostovaiheet ja ostotapahtumat (tuote ja hinta). Tapahtumat eivät koskaan sisällä terveystietoja: "
            "ei aikoja, supistuksia, välejä, laskettua aikaa, viikkoa, ohjetta, toiveita, liikkeitä, yhteystietoja tai muuta kirjoittamaasi tekstiä. SDK tallentaa myös "
            "teknisiä tietoja (sovellusversio, iOS-versio, laitemalli, likimääräinen sijainti – maa/alue – jonka Google päättelee IP-osoitteesta, ja Firebase Installationsin tekniset asennustiedot) ja satunnaisen sovellustunnuksen, joka "
            "nollautuu, kun poistat sovelluksen. Ei mainostunnistetta (IDFA), ei mainoksia, ei seurantaa. Oikeusperuste: oikeutettu etu kehittää sovellusta "
            f"(GDPR 6 artiklan 1 f kohta). Tapahtumatiedot poistetaan 2 kuukauden jälkeen. Kytke pois: Asetukset › ”Lähetä käyttötilastoja”. Lisää: {GA[0]}, {GA[1]}."),
           ("Ostot", "Kertaoston käsittelee kokonaan Apple App Storen kautta. Emme saa maksutietojasi."),
           ("Puhelut", "Soittopainikkeet avaavat puhelinsovelluksen itse kirjoittamallasi numerolla. Sovelluksessa ei ole valmiita numeroita hätänumeroa lukuun ottamatta."),
           ("Arviot", "Sovellus voi pyytää arviota Applen tavallisella ikkunalla, vasta kun olet merkinnyt vauvan syntyneeksi."),
           ("Tietojen poistaminen", "Asetukset › ”Poista kaikki tiedot” poistaa kaiken puhelimesta. Kun poistat sovelluksen, myös sen laitteelle tallentamat tiedot poistuvat. "
            "Jaetut tiedot iCloudissa poistuvat painikkeella ”Lopeta jakaminen”."),
           ("Oikeutesi", "Jos sinulla on kysyttävää, ota yhteyttä yllä olevaan osoitteeseen. Koska tilastot eivät liity sinuun, emme voi tunnistaa tietojasi niistä."),
           ("Ei lääketieteellisiä neuvoja", "Sovellus kirjaa ja auttaa muistamaan. Se ei anna lääketieteellisiä neuvoja. Soita kätilölle tai synnytyssairaalaan, jos olet epävarma."),
           ("Muutokset", "Voimme päivittää tätä selostetta. Yllä oleva päivämäärä kertoo voimassa olevan version.")],
    "en": [("Privacy Policy", "Last updated"),
           ("Who we are", f"This app is published by {OWNER}. Contact: {M}."),
           ("What you enter", "The app needs no account. Contractions, your midwife's rule, hospital bag, birth plan, contacts, movement diary and due date "
            "are stored only on your phone. We have no server and never get access to this information."),
           ("Sharing with your partner (iCloud)", "If you choose to share, what you selected on the Partner screen is stored in your own iCloud account and shared "
            "with the person you invite, through Apple's CloudKit. We have no access to it. You can tap “Stop sharing” at any time; your partner can tap “Leave the share”. "
            "See <a href='https://www.apple.com/legal/privacy/'>Apple's Privacy Policy</a>."),
           ("Usage statistics (Google Analytics for Firebase)", "To see which parts of the app are used, the app sends anonymous events to Google Analytics for "
            "Firebase (Google Ireland Ltd.): which screens are opened, which buttons are tapped, purchase steps and purchase events (product and price). Events never contain health information: "
            "no times, contractions, intervals, due date, week, rule, plan, movements, contacts or any text you type. The SDK also records technical data "
            "(app version, iOS version, device model, approximate location – country/region – that Google derives from the IP address, and technical installation data from Firebase Installations) and a random app-instance ID that is reset when you "
            "delete the app. No advertising identifier (IDFA), no ads, no tracking. Legal basis: legitimate interest in improving the app (Art. 6(1)(f) GDPR). "
            f"Event data is deleted after 2 months. Switch off under Settings › “Send usage statistics”. More: {GA[0]}, {GA[1]}."),
           ("Purchases", "The one-time purchase is handled entirely by Apple via the App Store. We do not receive your payment details."),
           ("Phone calls", "The call buttons open the Phone app with the number you typed yourself. The app has no built-in numbers apart from the emergency number."),
           ("Ratings", "The app may ask for a rating with Apple's standard dialog, only after you mark that the baby is born."),
           ("Deleting your data", "Settings › “Delete all data” removes everything from the phone. Deleting the app also removes everything it stored on the device. "
            "Shared data in iCloud is removed with “Stop sharing”."),
           ("Your rights", "If you have questions, contact us at the address above. Because the statistics are not linked to you, we cannot find your data in them."),
           ("Not medical advice", "The app keeps a log and helps you remember. It gives no medical advice. Call your midwife or birth unit if you are unsure."),
           ("Changes", "We may update this policy. The date above shows the current version.")],
}

S = {
    "nb": ("Support", f"Spørsmål eller problemer? Skriv til {M}. Vi svarer vanligvis innen 2 virkedager.", "Vanlige spørsmål",
           [("Er rietimeren alltid tilgjengelig?", "Ja. Rietimeren, historikken, sykehusbagen og kontaktene kan brukes uten kjøp, og kjøpssiden vises aldri i fødemodus."),
            ("Hvordan deler jeg med partneren?", "Hjem › Partner › «Inviter partneren». Partneren åpner lenken på sin iPhone med Fødselsklar installert. Begge må være logget inn på iCloud."),
            ("Hvorfor står det «sist oppdatert»?", "Partnerens kopi oppdateres via iCloud og kan være noen minutter gammel. Er den eldre enn 10 minutter, vises en advarsel."),
            ("Når skal jeg dra til sykehuset?", "Det avgjør du sammen med jordmor eller fødeavdelingen. Appen viser bare når regelen du selv har skrevet inn, er nådd."),
            ("Hvordan gjenoppretter jeg kjøpet?", "Innstillinger › «Gjenopprett kjøp», eller på kjøpssiden. Bruk samme Apple-ID som da du kjøpte."),
            ("Hvordan får jeg pengene tilbake?", f"Refusjon håndteres av Apple: {REFUND}.")], "Personvernerklæring"),
    "da": ("Support", f"Spørgsmål eller problemer? Skriv til {M}. Vi svarer normalt inden for 2 hverdage.", "Ofte stillede spørgsmål",
           [("Er veer-timeren altid tilgængelig?", "Ja. Veer-timeren, historikken, hospitalstasken og kontakterne kan bruges uden køb, og købssiden vises aldrig i fødselstilstand."),
            ("Hvordan deler jeg med min partner?", "Hjem › Partner › »Inviter din partner«. Din partner åbner linket på sin iPhone med Fødselsklar installeret. I skal begge være logget ind på iCloud."),
            ("Hvorfor står der »opdateret for … siden«?", "Partnerens kopi opdateres via iCloud og kan være nogle minutter gammel. Er den ældre end 10 minutter, vises en advarsel."),
            ("Hvornår skal jeg tage på hospitalet?", "Det aftaler du med jordemoderen eller fødestedet. Appen viser kun, hvornår den regel, du selv har skrevet, er nået."),
            ("Hvordan gendanner jeg mit køb?", "Indstillinger › »Gendan køb« eller på købssiden. Brug samme Apple-id, som du købte med."),
            ("Hvordan får jeg pengene tilbage?", f"Refusion håndteres af Apple: {REFUND}.")], "Privatlivspolitik"),
    "fi": ("Tuki", f"Kysyttävää tai ongelmia? Kirjoita osoitteeseen {M}. Vastaamme yleensä 2 arkipäivän kuluessa.", "Usein kysyttyä",
           [("Onko supistusajastin aina käytettävissä?", "Kyllä. Ajastinta, historiaa, sairaalakassia ja yhteystietoja voi käyttää ilman ostoa, eikä ostonäkymää näytetä synnytystilassa."),
            ("Miten jaan kumppanin kanssa?", "Koti › Kumppani › ”Kutsu kumppani”. Kumppani avaa linkin iPhonella, jossa on Synnytysvalmis. Molempien on oltava kirjautuneena iCloudiin."),
            ("Miksi näkyy ”päivitetty … sitten”?", "Kumppanin kopio päivittyy iCloudin kautta ja voi olla muutaman minuutin vanha. Yli 10 minuuttia vanhasta tiedosta näytetään varoitus."),
            ("Milloin lähden sairaalaan?", "Sen päätät yhdessä kätilön tai synnytyssairaalan kanssa. Sovellus näyttää vain, milloin itse kirjoittamasi ohje täyttyy."),
            ("Miten palautan oston?", "Asetukset › ”Palauta osto” tai ostonäkymässä. Käytä samaa Apple ID:tä kuin ostaessa."),
            ("Miten saan rahat takaisin?", f"Palautukset hoitaa Apple: {REFUND}.")], "Tietosuojaseloste"),
    "en": ("Support", f"Questions or problems? Email us at {M}. We usually reply within 2 business days.", "Frequently asked questions",
           [("Is the contraction timer always available?", "Yes. The timer, history, hospital bag and contacts work without a purchase, and the purchase screen never opens in labour mode."),
            ("How do I share with my partner?", "Home › Partner › “Invite your partner”. Your partner opens the link on their iPhone with the app installed. You both need to be signed in to iCloud."),
            ("Why does it say “updated … ago”?", "Your partner's copy updates through iCloud and can be a few minutes old. If it is older than 10 minutes, a warning is shown."),
            ("When should I go to hospital?", "You decide that with your midwife or birth unit. The app only shows when the rule you typed in yourself is reached."),
            ("How do I restore my purchase?", "Settings › “Restore purchase”, or on the purchase screen. Use the same Apple ID you bought with."),
            ("How do I get a refund?", f"Refunds are handled by Apple: {REFUND}.")], "Privacy Policy"),
}

CSS = """:root{--bg:#fff;--fg:#1c1c1e;--mu:#6b6b70;--ac:#5b3fa8}
@media (prefers-color-scheme:dark){:root{--bg:#111;--fg:#eee;--mu:#9a9aa0;--ac:#b8a6ee}}
body{background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:720px;margin:0 auto;padding:24px 16px}
h1{font-size:1.6em;margin-bottom:.2em}h2{font-size:1.15em;margin-top:1.6em}h3{font-size:1em;margin-bottom:0}a{color:var(--ac)}
.mu{color:var(--mu)}nav a{margin-right:12px}hr{border:0;border-top:1px solid var(--mu);opacity:.3;margin:40px 0}"""


def page(title, sections):
    nav = "".join(f"<a href='#{l}'>{l.upper()}</a>" for l in P)
    return (f"<!doctype html><html lang='nb'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{NAME} – {title}</title><style>{CSS}</style></head><body><nav>{nav}</nav>{'<hr>'.join(sections)}</body></html>")


def sec(l, inner):
    return f"<section id='{l}' lang='{l}'>{inner}</section>"


app = lambda l: "Synnytysvalmis" if l == "fi" else NAME
privacy = [sec(l, f"<h1>{p[0][0]} – {app(l)}</h1><p class='mu'>{p[0][1]}: {UPDATED}</p>" + "".join(f"<h2>{h}</h2><p>{t}</p>" for h, t in p[1:]))
           for l, p in P.items()]
support = [sec(l, f"<h1>{h} – {app(l)}</h1><p>{c}</p><h2>{faq}</h2>" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in qa) + f"<p><a href='../'>{priv}</a></p>")
           for l, (h, c, faq, qa, priv) in S.items()]

os.makedirs(f"{SLUG}/support", exist_ok=True)
open(f"{SLUG}/index.html", "w").write(page("Privacy", privacy))
open(f"{SLUG}/support/index.html", "w").write(page("Support", support))
for f in (f"{SLUG}/index.html", f"{SLUG}/support/index.html"):
    s = open(f).read()
    assert CONTACT in s and "Apple" in s and s.count("<section") == 4 and "[" not in s.replace("[0]", ""), f
print("ok", SLUG)
