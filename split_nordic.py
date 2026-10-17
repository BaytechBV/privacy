# Privacy, support and landing pages for Delt / Jaettu (split-nordic/). Separate from build.py because this app
# stores its data in the user's own iCloud (CloudKit sharing) and shares groups with other people.
#   python3 split_nordic.py [~/Documents/Projects/baytech] [APP_STORE_ID]
# The landing page (split-nordic/app/) is written only when the App Store id is given; its text comes from
# split-nordic/ios/AppStore/metadata.json (same copy as the store listing).
import html, json, os, re, sys
from build import CSS  # importing build also rewrites index.html: do not commit index.html (BILGI-GECMISI §1.3)

CONTACT = "utqsall@gmail.com"
OWNER = "Mustafa Utku Bayık"
UPDATED = "2026-10-17"
SLUG = "split-nordic"
SRC = os.path.expanduser(sys.argv[1]) if len(sys.argv) > 1 else os.path.expanduser("~/Documents/Projects/baytech")
APP_ID = sys.argv[2] if len(sys.argv) > 2 else None
M = f"<a href='mailto:{CONTACT}'>{CONTACT}</a>"
NAME = {"nb": "Delt", "da": "Delt", "fi": "Jaettu", "en": "Delt"}

P = {
 "nb": [("Personvernerklæring", "Sist oppdatert"),
  ("Hvem vi er", f"Appen er utgitt av {OWNER}. Kontakt: {M}."),
  ("Hvilke data appen behandler", "Appen trenger ingen konto hos oss. Gruppene dine – navn på personer, utgifter, beløp, notater, kvitteringsbilder og historikk – lagres på enheten din. "
   "Er du logget inn på iCloud, lagres de også i din egen iCloud-konto (Apple CloudKit), slik at de synkes mellom enhetene dine. Vi har ingen server og får aldri tilgang til disse dataene."),
  ("Deling av grupper", "Når du deler en gruppe, bruker appen Apples iCloud-deling. Personene du inviterer, kan se og endre gruppen: medlemsnavn, utgifter, kvitteringsbilder og historikk. "
   "Navnet på den som endret en utgift, vises i historikken. Du kan stoppe delingen når som helst under Medlemmer → Administrer deling. "
   "Personer uten appen legges inn med bare et navn som du skriver selv. Apple behandler iCloud-data etter <a href='https://www.apple.com/no/legal/privacy/'>Apples personvernerklæring</a>."),
  ("Kamera og bilder", "Kameraet og bildene dine brukes bare når du selv tar eller velger et kvitteringsbilde. Bildet lagres med utgiften (på enheten og i iCloud hvis du bruker det)."),
  ("Bruksstatistikk (Google Analytics for Firebase)", "For å se hvilke deler av appen som brukes, sender appen anonyme brukshendelser til Google Analytics for Firebase "
   "(Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irland): hvilke skjermer du åpner, hvilke knapper du trykker på, delingsmåte, antall personer og betalinger, og kjøpstrinn. "
   "Firebase registrerer også tekniske data som appversjon, iOS-versjon, enhetsmodell, land/region (utledet av IP-adressen, som ikke lagres) og en tilfeldig app-instans-ID. "
   "Navn, beløp, tekster og bilder sendes aldri. Dataene knyttes ikke til identiteten din, appen bruker ikke reklame-ID (IDFA) og sporer deg ikke. "
   "Rettslig grunnlag: vår berettigede interesse i å forbedre appen (GDPR art. 6 nr. 1 bokstav f). Google kan behandle data i USA (EU-US Data Privacy Framework). "
   "Hendelsesdata slettes etter 2 måneder. Du kan slå statistikken av i appens innstillinger («Send bruksstatistikk»)."),
  ("Kjøp", "Engangskjøpet håndteres helt av Apple via App Store. Vi får ikke betalingsopplysningene dine."),
  ("Penger og betalinger", "Appen flytter ikke penger og har ingen bankkobling. «Merk som betalt» registrerer bare i gruppen at dere har gjort opp utenfor appen."),
  ("Slette data", "Slett en gruppe i appen (Gruppe → … → Slett gruppen); er den delt, forsvinner den for alle. En gruppe andre har delt med deg, kan du forlate. "
   "Når du sletter appen, slettes dataene på enheten. Data i iCloud kan du slette under Innstillinger → [navnet ditt] → iCloud → Administrer lagring."),
  ("Dine rettigheter", "Har du spørsmål om denne erklæringen eller dataene dine (GDPR art. 15–21), kontakt oss på adressen over. Vi lagrer ingen data om deg på egne servere."),
  ("Endringer", "Vi kan endre denne erklæringen. Datoen over viser gjeldende versjon.")],
 "da": [("Privatlivspolitik", "Sidst opdateret"),
  ("Hvem vi er", f"Appen udgives af {OWNER}. Kontakt: {M}."),
  ("Hvilke data appen behandler", "Appen kræver ingen konto hos os. Dine grupper – navne på personer, udgifter, beløb, noter, kvitteringsbilleder og historik – gemmes på din enhed. "
   "Er du logget ind på iCloud, gemmes de også i din egen iCloud-konto (Apple CloudKit), så de synkroniseres mellem dine enheder. Vi har ingen server og får aldrig adgang til disse data."),
  ("Deling af grupper", "Når du deler en gruppe, bruger appen Apples iCloud-deling. Dem, du inviterer, kan se og ændre gruppen: medlemsnavne, udgifter, kvitteringsbilleder og historik. "
   "Navnet på den, der ændrede en udgift, vises i historikken. Du kan stoppe delingen når som helst under Medlemmer → Administrer deling. "
   "Personer uden appen tilføjes kun med et navn, som du selv skriver. Apple behandler iCloud-data efter <a href='https://www.apple.com/dk/legal/privacy/'>Apples privatlivspolitik</a>."),
  ("Kamera og billeder", "Kameraet og dine billeder bruges kun, når du selv tager eller vælger et kvitteringsbillede. Billedet gemmes med udgiften (på enheden og i iCloud, hvis du bruger det)."),
  ("Brugsstatistik (Google Analytics for Firebase)", "For at se, hvilke dele af appen der bruges, sender appen anonyme brugshændelser til Google Analytics for Firebase "
   "(Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irland): hvilke skærme du åbner, hvilke knapper du trykker på, fordelingsmåde, antal personer og betalinger samt trin i et køb. "
   "Firebase registrerer også tekniske data som appversion, iOS-version, enhedsmodel, land/region (udledt af IP-adressen, som ikke gemmes) og et tilfældigt app-instans-id. "
   "Navne, beløb, tekster og billeder sendes aldrig. Dataene kobles ikke til din identitet, appen bruger ikke reklame-id'et (IDFA) og sporer dig ikke. "
   "Retsgrundlag: vores legitime interesse i at forbedre appen (GDPR art. 6, stk. 1, litra f). Google kan behandle data i USA (EU-US Data Privacy Framework). "
   "Hændelsesdata slettes efter 2 måneder. Du kan slå statistikken fra i appens indstillinger (»Send brugsstatistik«)."),
  ("Køb", "Engangskøbet håndteres helt af Apple via App Store. Vi modtager ikke dine betalingsoplysninger."),
  ("Penge og betalinger", "Appen flytter ikke penge og har ingen bankforbindelse. »Markér som betalt« registrerer kun i gruppen, at I har gjort op uden for appen."),
  ("Slet dine data", "Slet en gruppe i appen (Gruppe → … → Slet gruppen); er den delt, forsvinder den for alle. En gruppe, andre har delt med dig, kan du forlade. "
   "Når du sletter appen, slettes dataene på enheden. Data i iCloud kan du slette under Indstillinger → [dit navn] → iCloud → Administrer lagring."),
  ("Dine rettigheder", "Har du spørgsmål om denne politik eller dine data (GDPR art. 15–21), så kontakt os på adressen ovenfor. Vi gemmer ingen data om dig på egne servere."),
  ("Ændringer", "Vi kan ændre denne politik. Datoen ovenfor viser den gældende version.")],
 "fi": [("Tietosuojaseloste", "Päivitetty"),
  ("Rekisterinpitäjä", f"Sovelluksen julkaisija on {OWNER}. Yhteystiedot: {M}."),
  ("Mitä tietoja sovellus käsittelee", "Sovellus ei vaadi tiliä meillä. Ryhmäsi – henkilöiden nimet, kulut, summat, muistiinpanot, kuittikuvat ja historia – tallennetaan laitteellesi. "
   "Jos olet kirjautunut iCloudiin, ne tallennetaan myös omaan iCloud-tiliisi (Apple CloudKit), jotta ne synkronoituvat laitteidesi välillä. Meillä ei ole palvelinta, emmekä koskaan näe näitä tietoja."),
  ("Ryhmien jakaminen", "Kun jaat ryhmän, sovellus käyttää Applen iCloud-jakoa. Kutsumasi henkilöt voivat nähdä ja muuttaa ryhmää: jäsenten nimet, kulut, kuittikuvat ja historian. "
   "Kulua muuttaneen nimi näkyy historiassa. Voit lopettaa jakamisen milloin tahansa kohdassa Jäsenet → Hallitse jakoa. "
   "Henkilöt ilman sovellusta lisätään pelkällä nimellä, jonka kirjoitat itse. Apple käsittelee iCloud-tietoja <a href='https://www.apple.com/fi/legal/privacy/'>Applen tietosuojakäytännön</a> mukaisesti."),
  ("Kamera ja kuvat", "Kameraa ja kuviasi käytetään vain, kun itse otat tai valitset kuittikuvan. Kuva tallennetaan kulun yhteyteen (laitteelle ja iCloudiin, jos käytät sitä)."),
  ("Käyttötilastot (Google Analytics for Firebase)", "Nähdäksemme, mitä sovelluksen osia käytetään, sovellus lähettää nimettömiä käyttötapahtumia Google Analytics for Firebaseen "
   "(Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irlanti): mitä näkymiä avaat, mitä painikkeita napautat, jakotapa, henkilöiden ja maksujen määrä sekä ostovaiheet. "
   "Firebase kirjaa myös teknisiä tietoja, kuten sovellus- ja iOS-version, laitemallin, maan/alueen (päätelty IP-osoitteesta, jota ei tallenneta) ja satunnaisen sovellusinstanssin tunnuksen. "
   "Nimiä, summia, tekstejä tai kuvia ei koskaan lähetetä. Tietoja ei yhdistetä henkilöllisyyteesi, sovellus ei käytä mainostunnistetta (IDFA) eikä seuraa sinua. "
   "Oikeusperuste: oikeutettu etumme kehittää sovellusta (GDPR 6 artiklan 1 kohdan f alakohta). Google voi käsitellä tietoja Yhdysvalloissa (EU–US Data Privacy Framework). "
   "Tapahtumatiedot poistetaan 2 kuukauden kuluttua. Voit kytkeä tilastot pois sovelluksen asetuksista (”Lähetä käyttötilastoja”)."),
  ("Ostot", "Kertaosto käsitellään kokonaan Applen App Storessa. Emme saa maksutietojasi."),
  ("Raha ja maksut", "Sovellus ei siirrä rahaa eikä ole yhteydessä pankkiin. ”Merkitse maksetuksi” vain kirjaa ryhmään, että velka on maksettu sovelluksen ulkopuolella."),
  ("Tietojen poistaminen", "Poista ryhmä sovelluksessa (Ryhmä → … → Poista ryhmä); jaettu ryhmä katoaa kaikilta. Muiden kanssasi jakamasta ryhmästä voit poistua. "
   "Kun poistat sovelluksen, laitteen tiedot poistetaan. iCloud-tiedot voit poistaa kohdassa Asetukset → [nimesi] → iCloud → Hallitse tallennustilaa."),
  ("Oikeutesi", "Jos sinulla on kysyttävää tästä selosteesta tai tiedoistasi (GDPR 15–21 artikla), ota yhteyttä yllä olevaan osoitteeseen. Emme tallenna sinusta tietoja omille palvelimillemme."),
  ("Muutokset", "Voimme päivittää tätä selostetta. Yllä oleva päivämäärä kertoo voimassa olevan version.")],
 "en": [("Privacy Policy", "Last updated"),
  ("Who we are", f"This app is published by {OWNER}. Contact: {M}."),
  ("What data the app processes", "The app needs no account with us. Your groups – people's names, expenses, amounts, notes, receipt photos and history – are stored on your device. "
   "If you are signed in to iCloud, they are also stored in your own iCloud account (Apple CloudKit) so they sync between your devices. We have no server and never have access to this data."),
  ("Sharing groups", "When you share a group, the app uses Apple's iCloud sharing. The people you invite can see and change the group: member names, expenses, receipt photos and history. "
   "The name of whoever changed an expense is shown in its history. You can stop sharing at any time under Members → Manage sharing. "
   "People without the app are added only with a name you type. Apple processes iCloud data under <a href='https://www.apple.com/legal/privacy/'>Apple's Privacy Policy</a>."),
  ("Camera and photos", "The camera and your photos are used only when you take or pick a receipt photo yourself. The photo is stored with the expense (on the device, and in iCloud if you use it)."),
  ("Usage statistics (Google Analytics for Firebase)", "To see which parts of the app are used, the app sends anonymous usage events to Google Analytics for Firebase "
   "(Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Ireland): which screens you open, which buttons you tap, the split mode, the number of people and payments, and purchase steps. "
   "Firebase also records technical data such as app version, iOS version, device model, country/region (derived from the IP address, which is not stored) and a random app-instance ID. "
   "Names, amounts, texts and photos are never sent. The data is not linked to your identity, the app does not use the advertising identifier (IDFA) and does not track you. "
   "Legal basis: our legitimate interest in improving the app (Art. 6(1)(f) GDPR). Google may process data in the USA (EU-US Data Privacy Framework). "
   "Event data is deleted after 2 months. You can switch the statistics off in the app's settings (“Send usage statistics”)."),
  ("Purchases", "The one-time purchase is handled entirely by Apple via the App Store. We do not receive your payment details."),
  ("Money and payments", "The app does not move money and has no bank connection. “Mark as paid” only records in the group that you settled outside the app."),
  ("Deleting your data", "Delete a group in the app (Group → … → Delete group); if it is shared, it disappears for everyone. You can leave a group someone shared with you. "
   "Deleting the app removes the data on the device. Data in iCloud can be deleted under Settings → [your name] → iCloud → Manage Storage."),
  ("Your rights", "If you have questions about this policy or your data (GDPR Art. 15–21), contact us at the address above. We store no data about you on our own servers."),
  ("Changes", "We may update this policy. The date above shows the latest version.")],
}

REFUND = "<a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>"
S = {
 "nb": ("Support", f"Spørsmål eller problemer? Skriv til {M}. Vi svarer som regel innen 2 virkedager.", "Vanlige spørsmål", [
  ("Hvordan inviterer jeg de andre?", "Åpne gruppen, trykk på «5 personer» og deretter «Del invitasjon». Send lenken, for eksempel i Meldinger. Den som åpner lenken, trenger appen og iCloud."),
  ("Må alle ha appen?", "Nei. Personer uten appen legges inn med bare navn. Saldoen deres vises for alle i gruppen."),
  ("Hvorfor synkes ikke gruppen?", "Sjekk at du er logget inn på iCloud og at iCloud Drive er på. Endringer gjort uten nett sendes når du er på nett igjen."),
  ("Flytter appen penger?", "Nei. Delt viser hvem som skal betale hvem. Betalingen gjør dere selv, for eksempel i Vipps eller nettbanken."),
  ("Hvordan gjenoppretter jeg kjøpet?", "Innstillinger i appen → «Gjenopprett kjøp». Bruk samme Apple-ID som du kjøpte med."),
  ("Hvordan får jeg pengene tilbake?", f"Refusjon håndteres av Apple: {REFUND}.")], "Personvernerklæring"),
 "da": ("Support", f"Spørgsmål eller problemer? Skriv til {M}. Vi svarer som regel inden for 2 hverdage.", "Ofte stillede spørgsmål", [
  ("Hvordan inviterer jeg de andre?", "Åbn gruppen, tryk på »5 personer« og derefter »Del invitation«. Send linket, fx i Beskeder. Den, der åbner linket, skal have appen og iCloud."),
  ("Skal alle have appen?", "Nej. Personer uden appen tilføjes kun med navn. Deres saldo vises for alle i gruppen."),
  ("Hvorfor synkroniseres gruppen ikke?", "Tjek, at du er logget ind på iCloud, og at iCloud Drive er slået til. Ændringer uden internet sendes, når du er online igen."),
  ("Flytter appen penge?", "Nej. Delt viser, hvem der skal betale hvem. Betalingen klarer I selv, fx med MobilePay eller i netbanken."),
  ("Hvordan gendanner jeg mit køb?", "Indstillinger i appen → »Gendan køb«. Brug det samme Apple-id, som du købte med."),
  ("Hvordan får jeg pengene tilbage?", f"Refusion håndteres af Apple: {REFUND}.")], "Privatlivspolitik"),
 "fi": ("Tuki", f"Kysyttävää tai ongelmia? Kirjoita osoitteeseen {M}. Vastaamme yleensä kahden arkipäivän kuluessa.", "Usein kysyttyä", [
  ("Miten kutsun muut?", "Avaa ryhmä, napauta ”5 henkilöä” ja sitten ”Jaa kutsu”. Lähetä linkki esimerkiksi Viesteillä. Linkin avaaja tarvitsee sovelluksen ja iCloudin."),
  ("Tarvitsevatko kaikki sovelluksen?", "Eivät. Henkilöt ilman sovellusta lisätään pelkällä nimellä. Heidän saldonsa näkyy kaikille ryhmässä."),
  ("Miksi ryhmä ei synkronoidu?", "Tarkista, että olet kirjautunut iCloudiin ja iCloud Drive on päällä. Ilman verkkoa tehdyt muutokset lähtevät, kun olet taas verkossa."),
  ("Siirtääkö sovellus rahaa?", "Ei. Jaettu näyttää, kuka maksaa kenelle. Maksatte itse, esimerkiksi MobilePaylla tai verkkopankissa."),
  ("Miten palautan oston?", "Sovelluksen Asetukset → ”Palauta ostot”. Käytä samaa Apple ID:tä, jolla ostit."),
  ("Miten saan rahat takaisin?", f"Hyvityksiä käsittelee Apple: {REFUND}.")], "Tietosuojaseloste"),
 "en": ("Support", f"Questions or problems? Email {M}. We usually reply within 2 business days.", "Frequently asked questions", [
  ("How do I invite the others?", "Open the group, tap “5 people” and then “Share invitation”. Send the link, for example in Messages. Whoever opens it needs the app and iCloud."),
  ("Does everyone need the app?", "No. People without the app are added by name only. Their balance is visible to everyone in the group."),
  ("Why does the group not sync?", "Check that you are signed in to iCloud and iCloud Drive is on. Changes made offline are sent when you are back online."),
  ("Does the app move money?", "No. Delt shows who pays whom. You pay each other yourselves, for example with Vipps, MobilePay or your bank app."),
  ("How do I restore my purchase?", "Settings in the app → “Restore purchases”. Use the same Apple ID you bought with."),
  ("How do I get a refund?", f"Refunds are handled by Apple: {REFUND}.")], "Privacy Policy"),
}
LANGS = ["nb", "da", "fi", "en"]

def page(title, lang, nav, body, extra_head=""):
    return (f"<!doctype html><html lang='{lang}'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{title}</title>{extra_head}<style>{CSS}</style></head><body><nav>{nav}</nav>{body}</body></html>")

nav = "".join(f"<a href='#{l}'>{l.upper()}</a>" for l in LANGS)
secs = []
for l in LANGS:
    (h, upd), *rest = P[l]
    secs.append(f"<section id='{l}' lang='{l}'><h1>{h} – {NAME[l]}</h1><p class='mu'>{upd}: {UPDATED}</p>"
                + "".join(f"<h2>{a}</h2><p>{b}</p>" for a, b in rest) + "</section>")
os.makedirs(f"{SLUG}/support", exist_ok=True)
open(f"{SLUG}/index.html", "w").write(page("Delt – Privacy", "nb", nav, "<hr>".join(secs)))
secs = []
for l in LANGS:
    h, contact, faq, qs, priv = S[l]
    secs.append(f"<section id='{l}' lang='{l}'><h1>{h} – {NAME[l]}</h1><p>{contact}</p><h2>{faq}</h2>"
                + "".join(f"<p><b>{q}</b><br>{a}</p>" for q, a in qs) + f"<p><a href='../'>{priv}</a></p></section>")
open(f"{SLUG}/support/index.html", "w").write(page("Delt – Support", "nb", nav, "<hr>".join(secs)))

if APP_ID:
    meta = json.load(open(f"{SRC}/{SLUG}/ios/AppStore/metadata.json"))
    LOC = {"nb": "nb", "da": "da", "fi": "fi", "en-GB": "en"}
    BTN = {"nb": "Last ned i App Store", "da": "Hent i App Store", "fi": "Lataa App Storesta", "en": "Download on the App Store"}
    store = f"https://apps.apple.com/app/id{APP_ID}"
    def desc(text):
        out = []
        for para in text.strip().split("\n\n"):
            lines = para.split("\n")
            if re.search(r"https?://", para):
                out.append("<p class='mu'>" + "<br>".join(re.sub(r"(https?://\S+)", r"<a href='\1'>\1</a>", html.escape(x, quote=False)) for x in lines) + "</p>")
                continue
            if len(lines) > 1 and lines[0] == lines[0].upper():
                out.append(f"<h2>{html.escape(lines[0])}</h2>"); lines = lines[1:]
            items = [x[2:] for x in lines if x.startswith("• ")]
            out.append("<ul>" + "".join(f"<li>{html.escape(x)}</li>" for x in items) + "</ul>" if items and len(items) == len(lines)
                       else "<p>" + "<br>".join(html.escape(x) for x in lines) + "</p>")
        return "".join(out)
    os.makedirs(f"{SLUG}/app", exist_ok=True)
    secs, lnav, shots_html = [], [], {}
    for loc, m in meta.items():
        l = LOC[loc]
        src = f"{SRC}/{SLUG}/store/screenshots/{'no' if loc == 'nb' else loc}/iphone-6.9"
        imgs = []
        if os.path.isdir(src):
            for i, f in enumerate(sorted(x for x in os.listdir(src) if x.endswith(".png"))[:3], 1):
                name = f"{l}-{i}.jpg"
                os.system(f"sips -s format jpeg -s formatOptions 75 --resampleWidth 600 '{src}/{f}' --out '{SLUG}/app/{name}' >/dev/null")
                imgs.append(f"<img src='{name}' alt='{html.escape(m['name'])} – {i}' loading='lazy' width='600' height='1304'>")
        secs.append(f"<section id='{l}' lang='{l}'><h1>{html.escape(m['name'])}</h1><p class='lead'>{html.escape(m['subtitle'])}</p>"
                    f"<p><a class='btn' href='{store}?pt=322891&ct=landing-{l}'>{BTN[l]}</a></p><div class='shots'>{''.join(imgs)}</div>"
                    f"{desc(m['description'])}<footer><a href='../support/'>Support</a></footer></section>")
        lnav.append(f"<a href='#{l}'>{l.upper()}</a>")
    p = meta["nb"]
    title = html.escape(f"{p['name']} – {p['subtitle']}")
    lcss = (".lead{font-size:1.15em;color:var(--mu);margin-top:0}.btn{display:inline-block;background:var(--fg);color:var(--bg);text-decoration:none;"
            "padding:10px 18px;border-radius:10px;font-weight:600}.shots{display:flex;gap:12px;overflow-x:auto;margin:24px 0}"
            ".shots img{width:200px;height:auto;border-radius:16px;flex:none}")
    head = (f"<meta name='description' content='{html.escape(p['promotionalText'])}'><meta name='apple-itunes-app' content='app-id={APP_ID}'>"
            f"<link rel='canonical' href='https://baytechbv.github.io/privacy/{SLUG}/app/'><style>{lcss}</style>")
    open(f"{SLUG}/app/index.html", "w").write(page(title, "nb", "".join(lnav), "<hr>".join(secs), head))
for f in (f"{SLUG}/index.html", f"{SLUG}/support/index.html"):
    s = open(f).read(); assert CONTACT in s and "Apple" in s and "iCloud" in s, f
print("ok", SLUG, "landing" if APP_ID else "(no landing yet: needs App Store id)")
