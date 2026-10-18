# Privacy and support pages for Bilboka / Bilboken / Bilbogen / Autokirja (bilbok-nordic/). Car data, receipts and documents stay
# on the device; only anonymous Google Analytics for Firebase events leave it.
#   python3 bilbok_nordic.py
# The landing page (bilbok-nordic/app/) comes from landing.py (IDS entry) and the app's ios/AppStore/metadata.json.
import os
from build import CSS  # importing build also rewrites index.html: do not commit index.html (BILGI-GECMISI §1.3)

CONTACT = "utqsall@gmail.com"
OWNER = "Mustafa Utku Bayık"
UPDATED = "2026-10-18"
SLUG = "bilbok-nordic"
M = f"<a href='mailto:{CONTACT}'>{CONTACT}</a>"
NAME = {"nb": "Bilboka", "sv": "Bilboken", "da": "Bilbogen", "fi": "Autokirja", "en": "Bilboka"}
G = "Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4"

P = {
 "nb": [("Personvernerklæring", "Sist oppdatert"),
  ("Hvem vi er", f"Appen er utgitt av {OWNER}. Kontakt: {M}."),
  ("Hvilke data appen behandler", "Appen trenger ingen konto. Bilene dine (navn, merke, modell, skilt, første registrering, kilometerstand), oppføringer (tanking, lading, service, kostnader), "
   "dekk, skannede kvitteringer og dokumenter lagres bare på enheten din og er med i enhetens sikkerhetskopi (iCloud eller datamaskin). Vi har ingen server og får aldri tilgang til disse dataene. "
   "Appen slår ikke opp skiltet ditt i noe register."),
  ("Kamera, bilder og varsler", "Kameraet brukes bare når du selv skanner en kvittering eller et dokument; bildet du velger brukes bare når du selv velger det. Skanningene lagres på enheten. "
   "Påminnelser er lokale varsler som planlegges på enheten."),
  ("Bruksstatistikk (Google Analytics for Firebase)", f"For å se hvilke deler av appen som brukes, sender appen anonyme brukshendelser til Google Analytics for Firebase ({G}, Irland): "
   "hvilke skjermer du åpner, hvilke knapper du trykker på, type oppføring, land og drivstofftype for bilen, og kjøpstrinn. "
   "Firebase registrerer også tekniske data som appversjon, iOS-versjon, enhetsmodell, land/region (utledet av IP-adressen, som ikke lagres) og en tilfeldig app-instans-ID. "
   "Skilt, bilnavn, beløp, kilometerstand, tekster, kvitteringer og bilder sendes aldri. Dataene knyttes ikke til identiteten din, appen bruker ikke reklame-ID (IDFA) og sporer deg ikke. "
   "Rettslig grunnlag: vår berettigede interesse i å forbedre appen (GDPR art. 6 nr. 1 bokstav f). Google kan behandle data i USA (EU-US Data Privacy Framework). "
   "Hendelsesdata slettes etter 2 måneder. Du kan slå statistikken av i appens innstillinger («Send bruksstatistikk»)."),
  ("Kjøp", "Engangskjøpet håndteres helt av Apple via App Store. Vi får ikke betalingsopplysningene dine."),
  ("Slette data", "Slett en bil i appen (Bilen → blyanten → Slett bil); da slettes også oppføringer, dekk, dokumenter og kvitteringer for bilen. Når du sletter appen, slettes alle dataene på enheten."),
  ("Dine rettigheter", "Har du spørsmål om denne erklæringen eller dataene dine (GDPR art. 15–21), kontakt oss på adressen over. Vi lagrer ingen data om deg på egne servere."),
  ("Endringer", "Vi kan endre denne erklæringen. Datoen over viser gjeldende versjon.")],
 "sv": [("Integritetspolicy", "Senast uppdaterad"),
  ("Vilka vi är", f"Appen ges ut av {OWNER}. Kontakt: {M}."),
  ("Vilka uppgifter appen behandlar", "Appen kräver inget konto. Dina bilar (namn, märke, modell, registreringsnummer, första registrering, mätarställning), poster (tankning, laddning, service, kostnader), "
   "däck, skannade kvitton och dokument sparas bara på din enhet och ingår i enhetens säkerhetskopia (iCloud eller dator). Vi har ingen server och får aldrig tillgång till uppgifterna. "
   "Appen slår inte upp ditt registreringsnummer i något register."),
  ("Kamera, bilder och aviseringar", "Kameran används bara när du själv skannar ett kvitto eller dokument; en bild används bara när du själv väljer den. Skanningarna sparas på enheten. "
   "Påminnelser är lokala aviseringar som planeras på enheten."),
  ("Användningsstatistik (Google Analytics for Firebase)", f"För att se vilka delar av appen som används skickar appen anonyma användningshändelser till Google Analytics for Firebase ({G}, Irland): "
   "vilka skärmar du öppnar, vilka knappar du trycker på, typ av post, bilens land och drivmedel samt steg i ett köp. "
   "Firebase registrerar även tekniska uppgifter som appversion, iOS-version, enhetsmodell, land/region (härlett från IP-adressen, som inte sparas) och ett slumpmässigt app-instans-ID. "
   "Registreringsnummer, bilnamn, belopp, mätarställning, texter, kvitton och bilder skickas aldrig. Uppgifterna kopplas inte till din identitet, appen använder inte annons-ID (IDFA) och spårar dig inte. "
   "Rättslig grund: vårt berättigade intresse av att förbättra appen (GDPR art. 6.1 f). Google kan behandla uppgifter i USA (EU-US Data Privacy Framework). "
   "Händelsedata raderas efter 2 månader. Du kan stänga av statistiken i appens inställningar (”Skicka användningsstatistik”)."),
  ("Köp", "Engångsköpet hanteras helt av Apple via App Store. Vi får inte dina betalningsuppgifter."),
  ("Radera uppgifter", "Radera en bil i appen (Bilen → pennan → Radera bil); då raderas även bilens poster, däck, dokument och kvitton. När du raderar appen raderas alla uppgifter på enheten."),
  ("Dina rättigheter", "Har du frågor om policyn eller dina uppgifter (GDPR art. 15–21), kontakta oss på adressen ovan. Vi sparar inga uppgifter om dig på egna servrar."),
  ("Ändringar", "Vi kan ändra policyn. Datumet ovan visar gällande version.")],
 "da": [("Privatlivspolitik", "Sidst opdateret"),
  ("Hvem vi er", f"Appen udgives af {OWNER}. Kontakt: {M}."),
  ("Hvilke data appen behandler", "Appen kræver ingen konto. Dine biler (navn, mærke, model, nummerplade, første registrering, kilometerstand), registreringer (tankning, opladning, service, udgifter), "
   "dæk, scannede kvitteringer og dokumenter gemmes kun på din enhed og er med i enhedens sikkerhedskopi (iCloud eller computer). Vi har ingen server og får aldrig adgang til disse data. "
   "Appen slår ikke din nummerplade op i noget register."),
  ("Kamera, billeder og notifikationer", "Kameraet bruges kun, når du selv scanner en kvittering eller et dokument; et billede bruges kun, når du selv vælger det. Scanningerne gemmes på enheden. "
   "Påmindelser er lokale notifikationer, der planlægges på enheden."),
  ("Brugsstatistik (Google Analytics for Firebase)", f"For at se, hvilke dele af appen der bruges, sender appen anonyme brugshændelser til Google Analytics for Firebase ({G}, Irland): "
   "hvilke skærme du åbner, hvilke knapper du trykker på, typen af registrering, bilens land og drivmiddel samt trin i et køb. "
   "Firebase registrerer også tekniske data som appversion, iOS-version, enhedsmodel, land/region (udledt af IP-adressen, som ikke gemmes) og et tilfældigt app-instans-id. "
   "Nummerplader, bilnavne, beløb, kilometerstand, tekster, kvitteringer og billeder sendes aldrig. Dataene kobles ikke til din identitet, appen bruger ikke reklame-id'et (IDFA) og sporer dig ikke. "
   "Retsgrundlag: vores legitime interesse i at forbedre appen (GDPR art. 6, stk. 1, litra f). Google kan behandle data i USA (EU-US Data Privacy Framework). "
   "Hændelsesdata slettes efter 2 måneder. Du kan slå statistikken fra i appens indstillinger (»Send brugsstatistik«)."),
  ("Køb", "Engangskøbet håndteres helt af Apple via App Store. Vi modtager ikke dine betalingsoplysninger."),
  ("Slet dine data", "Slet en bil i appen (Bilen → blyanten → Slet bil); så slettes også bilens registreringer, dæk, dokumenter og kvitteringer. Når du sletter appen, slettes alle data på enheden."),
  ("Dine rettigheder", "Har du spørgsmål om politikken eller dine data (GDPR art. 15–21), så kontakt os på adressen ovenfor. Vi gemmer ingen data om dig på egne servere."),
  ("Ændringer", "Vi kan ændre politikken. Datoen ovenfor viser den gældende version.")],
 "fi": [("Tietosuojaseloste", "Päivitetty"),
  ("Rekisterinpitäjä", f"Sovelluksen julkaisija on {OWNER}. Yhteystiedot: {M}."),
  ("Mitä tietoja sovellus käsittelee", "Sovellus ei vaadi tiliä. Autosi (nimi, merkki, malli, rekisterikilpi, käyttöönotto, mittarilukema), merkinnät (tankkaus, lataus, huolto, kulut), "
   "renkaat, skannatut kuitit ja asiakirjat tallennetaan vain laitteellesi, ja ne ovat mukana laitteen varmuuskopiossa (iCloud tai tietokone). Meillä ei ole palvelinta, emmekä koskaan näe näitä tietoja. "
   "Sovellus ei hae rekisterikilpeäsi mistään rekisteristä."),
  ("Kamera, kuvat ja ilmoitukset", "Kameraa käytetään vain, kun itse skannaat kuitin tai asiakirjan; kuvaa käytetään vain, kun itse valitset sen. Skannaukset tallennetaan laitteelle. "
   "Muistutukset ovat laitteella ajastettuja paikallisia ilmoituksia."),
  ("Käyttötilastot (Google Analytics for Firebase)", f"Nähdäksemme, mitä sovelluksen osia käytetään, sovellus lähettää nimettömiä käyttötapahtumia Google Analytics for Firebaseen ({G}, Irlanti): "
   "avatut näkymät, painetut painikkeet, merkinnän tyyppi, auton maa ja käyttövoima sekä oston vaiheet. "
   "Firebase tallentaa myös teknisiä tietoja, kuten sovelluksen ja iOS:n version, laitemallin, maan/alueen (päätelty IP-osoitteesta, jota ei tallenneta) ja satunnaisen sovellusinstanssin tunnisteen. "
   "Rekisterikilpiä, auton nimiä, summia, mittarilukemia, tekstejä, kuitteja tai kuvia ei koskaan lähetetä. Tietoja ei yhdistetä henkilöllisyyteesi, sovellus ei käytä mainostunnistetta (IDFA) eikä seuraa sinua. "
   "Oikeusperuste: oikeutettu etumme parantaa sovellusta (GDPR 6 artiklan 1 kohdan f alakohta). Google voi käsitellä tietoja Yhdysvalloissa (EU–US Data Privacy Framework). "
   "Tapahtumatiedot poistetaan 2 kuukauden kuluttua. Voit kytkeä tilastot pois sovelluksen asetuksista (”Lähetä käyttötilastoja”)."),
  ("Ostot", "Kertaoston käsittelee kokonaan Apple App Storessa. Emme saa maksutietojasi."),
  ("Tietojen poistaminen", "Poista auto sovelluksessa (Auto → kynä → Poista auto); samalla poistuvat auton merkinnät, renkaat, asiakirjat ja kuitit. Kun poistat sovelluksen, kaikki laitteen tiedot poistuvat."),
  ("Oikeutesi", "Jos sinulla on kysyttävää tästä selosteesta tai tiedoistasi (GDPR 15–21 art.), ota yhteyttä yllä olevaan osoitteeseen. Emme tallenna sinusta tietoja omille palvelimillemme."),
  ("Muutokset", "Voimme muuttaa tätä selostetta. Yllä oleva päivämäärä kertoo voimassa olevan version.")],
 "en": [("Privacy Policy", "Last updated"),
  ("Who we are", f"The app is published by {OWNER}. Contact: {M}."),
  ("What data the app handles", "The app needs no account. Your cars (name, make, model, plate, first registration, odometer), entries (fuel, charging, service, costs), "
   "tyres, scanned receipts and documents are stored only on your device and are included in the device backup (iCloud or computer). We have no server and never see this data. "
   "The app does not look up your plate in any register."),
  ("Camera, photos and notifications", "The camera is used only when you scan a receipt or document yourself; a photo is used only when you pick it. Scans are stored on the device. "
   "Reminders are local notifications scheduled on the device."),
  ("Usage statistics (Google Analytics for Firebase)", f"To see which parts of the app are used, the app sends anonymous usage events to Google Analytics for Firebase ({G}, Ireland): "
   "which screens you open, which buttons you tap, the type of entry, the car's country and fuel type, and purchase steps. "
   "Firebase also records technical data such as app version, iOS version, device model, country/region (derived from the IP address, which is not stored) and a random app instance ID. "
   "Plates, car names, amounts, odometer readings, text, receipts and images are never sent. The data is not linked to your identity, the app does not use the advertising ID (IDFA) and does not track you. "
   "Legal basis: our legitimate interest in improving the app (GDPR Art. 6(1)(f)). Google may process data in the USA (EU-US Data Privacy Framework). "
   "Event data is deleted after 2 months. You can switch statistics off in the app's settings (“Send usage statistics”)."),
  ("Purchases", "The one-time purchase is handled entirely by Apple through the App Store. We do not receive your payment details."),
  ("Deleting data", "Delete a car in the app (Car → pencil → Delete car); its entries, tyres, documents and receipts are deleted too. Deleting the app deletes all data on the device."),
  ("Your rights", "If you have questions about this policy or your data (GDPR Art. 15–21), contact us at the address above. We store no data about you on our own servers."),
  ("Changes", "We may change this policy. The date above shows the current version.")],
}

REF = "<a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>"
S = {
 "nb": ("Støtte", f"Spørsmål eller problemer? Skriv til {M}. Vi svarer vanligvis innen 2 virkedager.", "Ofte stilte spørsmål", [
  ("Hvordan regnes neste EU-kontroll ut?", "Ut fra første registrering og Statens vegvesens regel: første kontroll innen 4 år, deretter minst hvert 2. år. Har du registrert en kontroll, regner appen fra den. Kilden står i appen under EU-kontroll."),
  ("Brevet mitt har en annen dato. Hva gjelder?", "Brevet gjelder alltid. Trykk «Endre etter brevet» på EU-kontroll-skjermen og skriv inn datoen; appen bruker den til du registrerer en kontroll."),
  ("Kan jeg bruke mil i stedet for km?", "Ja: Innstillinger → Avstand → Mil (10 km). Kilometerstanden skriver du fortsatt i km, slik den står på dashbordet."),
  ("Hvorfor vises ikke forbruket?", "Forbruket regnes fra full tank til full tank (eller full lading). Slå på «Fylt helt opp» / «Ladet til 100 %» når det stemmer."),
  ("Hvordan får jeg dataene med til en ny telefon?", "Dataene er med i iPhone-sikkerhetskopien (iCloud eller datamaskin). Gjenopprett den nye telefonen fra sikkerhetskopien. Du kan også eksportere alt som CSV."),
  ("Hvordan gjenoppretter jeg kjøpet?", "Innstillinger → «Gjenopprett kjøp», med samme Apple-ID som du kjøpte med."),
  ("Hvordan får jeg pengene tilbake?", f"Refusjon håndteres av Apple: {REF}.")], "Personvernerklæring"),
 "sv": ("Support", f"Frågor eller problem? Skriv till {M}. Vi svarar oftast inom 2 arbetsdagar.", "Vanliga frågor", [
  ("Hur räknas nästa besiktning ut?", "Från månaden bilen togs i trafik och Transportstyrelsens regel: första senast efter 36 månader, sedan 24 och därefter var 14:e månad, räknat från månaden du besiktade. Källan finns i appen."),
  ("Mitt brev har ett annat datum. Vad gäller?", "Brevet gäller alltid. Tryck på ”Ändra enligt brevet” och skriv in datumet; appen använder det tills du registrerar en besiktning."),
  ("Kan jag använda mil i stället för km?", "Ja: Inställningar → Avstånd → Mil (10 km). Mätarställningen skriver du fortfarande i km."),
  ("Varför visas ingen förbrukning?", "Förbrukningen räknas från full tank till full tank (eller full laddning). Slå på ”Fulltankad” / ”Laddad till 100 %” när det stämmer."),
  ("Hur flyttar jag uppgifterna till en ny telefon?", "Uppgifterna ingår i iPhone-säkerhetskopian (iCloud eller dator). Återställ den nya telefonen från säkerhetskopian. Du kan också exportera allt som CSV."),
  ("Hur återställer jag köpet?", "Inställningar → ”Återställ köp”, med samma Apple-ID som du köpte med."),
  ("Hur får jag pengarna tillbaka?", f"Återbetalning hanteras av Apple: {REF}.")], "Integritetspolicy"),
 "da": ("Support", f"Spørgsmål eller problemer? Skriv til {M}. Vi svarer som regel inden for 2 hverdage.", "Ofte stillede spørgsmål", [
  ("Hvordan regnes næste syn ud?", "Ud fra første registrering og Færdselsstyrelsens regel: første periodiske syn efter 4 år, derefter hvert 2. år. Kilden står i appen."),
  ("Mit brev har en anden dato. Hvad gælder?", "Brevet gælder altid. Tryk på »Ret efter brevet«, og skriv datoen; appen bruger den, til du registrerer et syn."),
  ("Hvorfor vises intet forbrug?", "Forbruget regnes fra fuld tank til fuld tank (eller fuld opladning). Slå »Tanket helt op« / »Opladet til 100 %« til, når det passer."),
  ("Hvordan flytter jeg data til en ny telefon?", "Dataene er med i iPhone-sikkerhedskopien (iCloud eller computer). Gendan den nye telefon fra sikkerhedskopien. Du kan også eksportere alt som CSV."),
  ("Hvordan gendanner jeg købet?", "Indstillinger → »Gendan køb« med det samme Apple-id, som du købte med."),
  ("Hvordan får jeg pengene tilbage?", f"Refusion håndteres af Apple: {REF}.")], "Privatlivspolitik"),
 "fi": ("Tuki", f"Kysyttävää tai ongelmia? Kirjoita osoitteeseen {M}. Vastaamme yleensä 2 arkipäivän kuluessa.", "Usein kysyttyä", [
  ("Miten seuraava katsastus lasketaan?", "Käyttöönotosta Traficomin säännöllä: ensimmäinen viimeistään 4 vuoden kuluttua, sitten 6 ja 8 vuoden iässä ja 10 vuodesta alkaen vuosittain. Lähde näkyy sovelluksessa."),
  ("Kirjeessäni on eri päivä. Mikä pätee?", "Kirje on aina ratkaiseva. Napauta ”Muuta kirjeen mukaan” ja syötä päivä; sovellus käyttää sitä, kunnes kirjaat katsastuksen."),
  ("Miksi kulutusta ei näy?", "Kulutus lasketaan täydestä tankista täyteen tankkiin (tai täydestä latauksesta). Valitse ”Täyteen tankattu” / ”Ladattu 100 %:iin”, kun se pitää paikkansa."),
  ("Miten siirrän tiedot uuteen puhelimeen?", "Tiedot ovat mukana iPhonen varmuuskopiossa (iCloud tai tietokone). Palauta uusi puhelin varmuuskopiosta. Voit myös viedä kaiken CSV-tiedostona."),
  ("Miten palautan oston?", "Asetukset → ”Palauta osto” samalla Apple ID:llä, jolla ostit."),
  ("Miten saan rahat takaisin?", f"Hyvityksiä käsittelee Apple: {REF}.")], "Tietosuojaseloste"),
 "en": ("Support", f"Questions or problems? Email {M}. We usually reply within 2 business days.", "Frequently asked questions", [
  ("How is the next inspection worked out?", "From the first registration and the country's official rule (Statens vegvesen, Transportstyrelsen, Færdselsstyrelsen or Traficom). If you logged an inspection, the app counts from it. The source is shown in the app."),
  ("My letter shows a different date. Which one applies?", "The letter always applies. Tap “Change from the letter” on the inspection screen and type the date; the app uses it until you log an inspection."),
  ("Can I use mil instead of km?", "Yes: Settings → Distance → Mil (10 km). Odometer readings are still typed in km, as on the dashboard."),
  ("Why is no consumption shown?", "Consumption is calculated from full tank to full tank (or full charge). Turn on “Filled to full” / “Charged to 100 %” when that is true."),
  ("How do I move my data to a new phone?", "Your data is in the iPhone backup (iCloud or computer). Restore the new phone from the backup. You can also export everything as CSV."),
  ("How do I restore my purchase?", "Settings → “Restore purchase”, with the Apple ID you bought with."),
  ("How do I get a refund?", f"Refunds are handled by Apple: {REF}.")], "Privacy Policy"),
}
LANGS = ["nb", "sv", "da", "fi", "en"]


def page(title, lang, nav, body):
    return (f"<!doctype html><html lang='{lang}'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{title}</title><style>{CSS}</style></head><body><nav>{nav}</nav>{body}</body></html>")


nav = "".join(f"<a href='#{l}'>{l.upper()}</a>" for l in LANGS)
secs = []
for l in LANGS:
    (h, upd), *rest = P[l]
    secs.append(f"<section id='{l}' lang='{l}'><h1>{h} – {NAME[l]}</h1><p class='mu'>{upd}: {UPDATED}</p>"
                + "".join(f"<h2>{a}</h2><p>{b}</p>" for a, b in rest) + "</section>")
os.makedirs(f"{SLUG}/support", exist_ok=True)
open(f"{SLUG}/index.html", "w").write(page("Bilboka – Privacy", "nb", nav, "<hr>".join(secs)))
secs = []
for l in LANGS:
    h, contact, faq, qs, priv = S[l]
    secs.append(f"<section id='{l}' lang='{l}'><h1>{h} – {NAME[l]}</h1><p>{contact}</p><h2>{faq}</h2>"
                + "".join(f"<p><b>{q}</b><br>{a}</p>" for q, a in qs) + f"<p><a href='../'>{priv}</a></p></section>")
open(f"{SLUG}/support/index.html", "w").write(page("Bilboka – Support", "nb", nav, "<hr>".join(secs)))
for f in (f"{SLUG}/index.html", f"{SLUG}/support/index.html"):
    s = open(f).read(); assert CONTACT in s and "Apple" in s, f
print("ok", SLUG)
