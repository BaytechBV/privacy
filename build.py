# Generates one static privacy page per app. Edit the APPS texts and re-run; each app's page is independent.
import os

CONTACT = "utqsall@gmail.com"
OWNER = "Mustafa Utku Bayık"
UPDATED = "2026-10-14"

T = {
    "en": dict(
        h="Privacy Policy", upd="Last updated", who="Who we are",
        who_t=f"This app is published by {OWNER}. Contact: <a href='mailto:{CONTACT}'>{CONTACT}</a>.",
        data="What data the app processes",
        data_t="The app does not require an account. Your learning progress, settings and exam results are stored only on your device. "
               "The only data that leaves your device is the anonymous usage statistics described below.",
        no="Usage statistics (Google Analytics for Firebase)",
        no_t="To find out which parts of the app are used and where it can be improved, the app sends anonymous usage events to "
             "Google Analytics for Firebase (Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Ireland): which screens you open, "
             "which buttons you tap, when a practice round or mock exam starts and ends (with the score as a range, e.g. “70–84%”), "
             "and purchase steps. The Firebase SDK also records technical data such as app version, iOS version, device model, "
             "country/region (derived from the IP address, which is not stored) and a random app-instance ID that is reset when you delete the app. "
             "No name, e-mail address, question or answer text, or other content you enter is sent. The data is not linked to your identity. "
             "The app does not use the advertising identifier (IDFA), shows no ads and does not track you across apps or websites. "
             "Legal basis: our legitimate interest in improving the app (Art. 6(1)(f) GDPR). Google may process data in the USA; "
             "Google LLC is certified under the EU-US Data Privacy Framework. Event data is deleted after 2 months. "
             "See <a href='https://policies.google.com/privacy'>Google's Privacy Policy</a> and "
             "<a href='https://firebase.google.com/support/privacy'>Privacy and Security in Firebase</a>.",
        buy="Purchases", buy_t="The one-time in-app purchase is handled entirely by Apple via the App Store. We do not receive your payment details. "
               "See <a href='https://www.apple.com/legal/privacy/'>Apple's Privacy Policy</a>.",
        rate="Ratings", rate_t="The app may ask you to rate it using Apple's standard rating dialog. Ratings are handled by Apple.",
        del_="Deleting your data", del_t="Deleting the app removes all data it stored on your device.",
        rights="Your rights", rights_t="If you have questions about this policy or your data, contact us at the address above. "
               "You can switch the usage statistics off at any time in the app's settings (“Send usage statistics”); from then on no events are sent (Art. 21 GDPR). "
               "Deleting the app also deletes the app-instance ID. "
               "Because the statistics are not linked to your identity, we cannot identify your data in them.",
        chg="Changes", chg_t="We may update this policy. The date above shows the latest version."),
    "de": dict(
        h="Datenschutzerklärung", upd="Stand", who="Verantwortlicher",
        who_t=f"Diese App wird von {OWNER} veröffentlicht. Kontakt: <a href='mailto:{CONTACT}'>{CONTACT}</a>.",
        data="Welche Daten die App verarbeitet",
        data_t="Die App benötigt kein Konto. Lernfortschritt, Einstellungen und Prüfungsergebnisse werden ausschließlich auf deinem Gerät gespeichert. "
               "Dein Gerät verlassen nur die unten beschriebenen anonymen Nutzungsstatistiken.",
        no="Nutzungsstatistik (Google Analytics for Firebase)",
        no_t="Um zu erfahren, welche Teile der App genutzt werden und wo wir sie verbessern können, sendet die App anonyme Nutzungsereignisse an "
             "Google Analytics for Firebase (Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irland): welche Bildschirme du öffnest, "
             "welche Schaltflächen du antippst, wann eine Übungsrunde oder Prüfungssimulation beginnt und endet (mit dem Ergebnis als Spanne, z. B. „70–84 %“) "
             "sowie Kaufschritte. Das Firebase-SDK erfasst außerdem technische Daten wie App-Version, iOS-Version, Gerätemodell, "
             "Land/Region (aus der IP-Adresse abgeleitet, die nicht gespeichert wird) und eine zufällige App-Instanz-ID, die beim Löschen der App zurückgesetzt wird. "
             "Name, E-Mail-Adresse, Frage- oder Antworttexte und andere Inhalte, die du eingibst, werden nicht übertragen. Die Daten werden nicht mit deiner Identität verknüpft. "
             "Die App nutzt keine Werbe-ID (IDFA), zeigt keine Werbung und verfolgt dich nicht über Apps oder Websites hinweg. "
             "Rechtsgrundlage: unser berechtigtes Interesse an der Verbesserung der App (Art. 6 Abs. 1 lit. f DSGVO). Google kann Daten in den USA verarbeiten; "
             "Google LLC ist nach dem EU-US Data Privacy Framework zertifiziert. Ereignisdaten werden nach 2 Monaten gelöscht. "
             "Siehe <a href='https://policies.google.com/privacy?hl=de'>Datenschutzerklärung von Google</a> und "
             "<a href='https://firebase.google.com/support/privacy'>Datenschutz und Sicherheit in Firebase</a>.",
        buy="Käufe", buy_t="Der einmalige In-App-Kauf wird vollständig von Apple über den App Store abgewickelt. Wir erhalten keine Zahlungsdaten. "
               "Siehe <a href='https://www.apple.com/de/legal/privacy/'>Datenschutzrichtlinie von Apple</a>.",
        rate="Bewertungen", rate_t="Die App kann dich über den Standarddialog von Apple um eine Bewertung bitten. Bewertungen verarbeitet Apple.",
        del_="Daten löschen", del_t="Wenn du die App löschst, werden alle von ihr auf deinem Gerät gespeicherten Daten entfernt.",
        rights="Deine Rechte", rights_t="Bei Fragen zu dieser Erklärung oder zu deinen Daten (Art. 15–21 DSGVO) wende dich an die obige Adresse. "
               "Du kannst die Nutzungsstatistik jederzeit in den Einstellungen der App ausschalten („Nutzungsstatistik senden“); danach werden keine Ereignisse mehr gesendet (Art. 21 DSGVO). "
               "Mit dem Löschen der App wird auch die App-Instanz-ID gelöscht. "
               "Da die Statistik nicht mit deiner Identität verknüpft ist, können wir deine Daten darin nicht zuordnen.",
        chg="Änderungen", chg_t="Wir können diese Erklärung anpassen. Das Datum oben zeigt die aktuelle Fassung."),
    "da": dict(
        h="Privatlivspolitik", upd="Sidst opdateret", who="Hvem vi er",
        who_t=f"Appen udgives af {OWNER}. Kontakt: <a href='mailto:{CONTACT}'>{CONTACT}</a>.",
        data="Hvilke data appen behandler",
        data_t="Appen kræver ingen konto. Dine fremskridt, indstillinger og prøveresultater gemmes kun på din enhed. "
               "Det eneste, der forlader din enhed, er den anonyme brugsstatistik, der er beskrevet nedenfor.",
        no="Brugsstatistik (Google Analytics for Firebase)",
        no_t="For at se, hvilke dele af appen der bliver brugt, og hvor den kan blive bedre, sender appen anonyme brugshændelser til "
             "Google Analytics for Firebase (Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irland): hvilke skærme du åbner, "
             "hvilke knapper du trykker på, hvornår en øverunde eller prøveeksamen starter og slutter (med resultatet som et interval, fx “70–84 %”) "
             "og trin i et køb. Firebase-SDK'et registrerer også tekniske data som appversion, iOS-version, enhedsmodel, "
             "land/region (udledt af IP-adressen, som ikke gemmes) og et tilfældigt app-instans-id, der nulstilles, når du sletter appen. "
             "Navn, e-mailadresse, spørgsmåls- eller svartekster og andet indhold, du indtaster, sendes ikke. Dataene kobles ikke til din identitet. "
             "Appen bruger ikke reklame-id'et (IDFA), viser ingen reklamer og sporer dig ikke på tværs af apps eller websteder. "
             "Retsgrundlag: vores legitime interesse i at forbedre appen (GDPR art. 6, stk. 1, litra f). Google kan behandle data i USA; "
             "Google LLC er certificeret under EU-US Data Privacy Framework. Hændelsesdata slettes efter 2 måneder. "
             "Se <a href='https://policies.google.com/privacy?hl=da'>Googles privatlivspolitik</a> og "
             "<a href='https://firebase.google.com/support/privacy'>Privacy and Security in Firebase</a>.",
        buy="Køb", buy_t="Engangskøbet i appen håndteres helt af Apple via App Store. Vi modtager ikke dine betalingsoplysninger. "
               "Se <a href='https://www.apple.com/dk/legal/privacy/'>Apples privatlivspolitik</a>.",
        rate="Bedømmelser", rate_t="Appen kan bede dig om at bedømme den med Apples almindelige dialog. Bedømmelser håndteres af Apple.",
        del_="Slet dine data", del_t="Når du sletter appen, slettes alle data, den har gemt på din enhed. Under Indstillinger kan du også nulstille dine fremskridt.",
        rights="Dine rettigheder", rights_t="Har du spørgsmål om denne politik eller dine data (GDPR art. 15–21), så kontakt os på adressen ovenfor. "
               "Du kan altid slå brugsstatistikken fra i appens indstillinger (“Send brugsstatistik”); derefter sendes ingen hændelser (GDPR art. 21). "
               "Når du sletter appen, slettes app-instans-id'et også. "
               "Da statistikken ikke er koblet til din identitet, kan vi ikke finde dine data i den.",
        chg="Ændringer", chg_t="Vi kan ændre denne politik. Datoen ovenfor viser den gældende version."),
    "nl": dict(
        h="Privacybeleid", upd="Laatst bijgewerkt", who="Wie wij zijn",
        who_t=f"Deze app wordt uitgegeven door {OWNER}. Contact: <a href='mailto:{CONTACT}'>{CONTACT}</a>.",
        data="Welke gegevens de app verwerkt",
        data_t="De app heeft geen account nodig. Je voortgang, instellingen en examenresultaten worden alleen op je apparaat opgeslagen. "
               "Alleen de hieronder beschreven anonieme gebruiksstatistieken verlaten je apparaat.",
        no="Gebruiksstatistieken (Google Analytics for Firebase)",
        no_t="Om te zien welke onderdelen van de app worden gebruikt en wat beter kan, stuurt de app anonieme gebruiksgebeurtenissen naar "
             "Google Analytics for Firebase (Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Ierland): welke schermen je opent, "
             "op welke knoppen je tikt, wanneer een oefenronde of proefexamen begint en eindigt (met de score als bereik, bijv. ‘70–84%’) "
             "en aankoopstappen. De Firebase-SDK legt ook technische gegevens vast zoals appversie, iOS-versie, apparaatmodel, "
             "land/regio (afgeleid van het IP-adres, dat niet wordt bewaard) en een willekeurige app-instantie-ID die opnieuw wordt ingesteld als je de app verwijdert. "
             "Naam, e-mailadres, vraag- of antwoordteksten en andere inhoud die je invoert worden niet verstuurd. De gegevens worden niet aan je identiteit gekoppeld. "
             "De app gebruikt geen advertentie-ID (IDFA), toont geen advertenties en volgt je niet via andere apps of websites. "
             "Rechtsgrond: ons gerechtvaardigd belang bij het verbeteren van de app (art. 6 lid 1 sub f AVG). Google kan gegevens in de VS verwerken; "
             "Google LLC is gecertificeerd onder het EU-VS Data Privacy Framework. Gebeurtenisgegevens worden na 2 maanden verwijderd. "
             "Zie het <a href='https://policies.google.com/privacy?hl=nl'>privacybeleid van Google</a> en "
             "<a href='https://firebase.google.com/support/privacy'>Privacy and Security in Firebase</a>.",
        buy="Aankopen", buy_t="De eenmalige in-app-aankoop wordt volledig door Apple via de App Store afgehandeld. Wij ontvangen geen betaalgegevens. "
               "Zie het <a href='https://www.apple.com/nl/legal/privacy/'>privacybeleid van Apple</a>.",
        rate="Beoordelingen", rate_t="De app kan je via het standaardvenster van Apple om een beoordeling vragen. Beoordelingen worden door Apple verwerkt.",
        del_="Gegevens verwijderen", del_t="Als je de app verwijdert, worden alle gegevens die de app op je apparaat heeft opgeslagen verwijderd.",
        rights="Je rechten", rights_t="Heb je vragen over dit beleid of je gegevens (AVG)? Neem contact op via het adres hierboven. "
               "Je kunt de gebruiksstatistieken op elk moment uitzetten in de instellingen van de app (‘Gebruiksstatistieken versturen’); daarna worden geen gebeurtenissen meer verstuurd (art. 21 AVG). "
               "Als je de app verwijdert, wordt ook de app-instantie-ID verwijderd. "
               "Omdat de statistieken niet aan je identiteit zijn gekoppeld, kunnen wij jouw gegevens daarin niet herkennen.",
        chg="Wijzigingen", chg_t="We kunnen dit beleid aanpassen. De datum hierboven toont de nieuwste versie."),
    "fi": dict(
        h="Tietosuojaseloste", upd="Päivitetty", who="Rekisterinpitäjä",
        who_t=f"Sovelluksen julkaisija on {OWNER}. Yhteystiedot: <a href='mailto:{CONTACT}'>{CONTACT}</a>.",
        data="Mitä tietoja sovellus käsittelee",
        data_t="Sovellus ei vaadi tiliä. Edistymisesi, asetuksesi ja harjoituskokeiden tulokset tallennetaan vain laitteellesi. "
               "Laitteelta lähtevät vain alla kuvatut nimettömät käyttötilastot.",
        no="Käyttötilastot (Google Analytics for Firebase)",
        no_t="Selvittääksemme, mitä sovelluksen osia käytetään ja mitä voisi parantaa, sovellus lähettää nimettömiä käyttötapahtumia "
             "Google Analytics for Firebaseen (Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irlanti): mitkä näkymät avaat, "
             "mitä painikkeita painat, milloin harjoituskierros tai harjoituskoe alkaa ja päättyy (tulos vaihteluvälinä, esim. ”70–84 %”) "
             "sekä ostovaiheet. Firebase-SDK tallentaa myös teknisiä tietoja, kuten sovelluksen ja iOS:n version, laitemallin, "
             "maan/alueen (päätelty IP-osoitteesta, jota ei tallenneta) ja satunnaisen sovellusasennuksen tunnisteen, joka nollautuu, kun poistat sovelluksen. "
             "Nimeä, sähköpostiosoitetta, kysymysten tai vastausten tekstiä tai muuta syöttämääsi sisältöä ei lähetetä. Tietoja ei yhdistetä henkilöllisyyteesi. "
             "Sovellus ei käytä mainostunnistetta (IDFA), ei näytä mainoksia eikä seuraa sinua muissa sovelluksissa tai verkkosivuilla. "
             "Oikeusperuste: oikeutettu etumme parantaa sovellusta (GDPR 6 artiklan 1 kohdan f alakohta). Google voi käsitellä tietoja Yhdysvalloissa; "
             "Google LLC on sertifioitu EU:n ja Yhdysvaltojen välisen tietosuojakehyksen (Data Privacy Framework) mukaisesti. Tapahtumatiedot poistetaan 2 kuukauden kuluttua. "
             "Katso <a href='https://policies.google.com/privacy?hl=fi'>Googlen tietosuojakäytäntö</a> ja "
             "<a href='https://firebase.google.com/support/privacy'>Privacy and Security in Firebase</a>.",
        buy="Ostot", buy_t="Kertaluonteisen sovelluksen sisäisen oston käsittelee kokonaan Apple App Storen kautta. Emme saa maksutietojasi. "
               "Katso <a href='https://www.apple.com/fi/legal/privacy/'>Applen tietosuojakäytäntö</a>.",
        rate="Arviot", rate_t="Sovellus voi pyytää sinua arvioimaan sen Applen tavallisella arviointi-ikkunalla. Arviot käsittelee Apple.",
        del_="Tietojen poistaminen", del_t="Kun poistat sovelluksen, kaikki sen laitteellesi tallentamat tiedot poistuvat.",
        rights="Oikeutesi", rights_t="Jos sinulla on kysyttävää tästä selosteesta tai tiedoistasi, ota yhteyttä yllä olevaan osoitteeseen. "
               "Voit kytkeä käyttötilastot pois milloin tahansa sovelluksen asetuksista (”Lähetä käyttötilastoja”); sen jälkeen tapahtumia ei enää lähetetä (GDPR 21 artikla). "
               "Sovelluksen poistaminen poistaa myös sovellusasennuksen tunnisteen. "
               "Koska tilastoja ei yhdistetä henkilöllisyyteesi, emme pysty tunnistamaan niistä sinun tietojasi.",
        chg="Muutokset", chg_t="Voimme päivittää tätä selostetta. Yllä oleva päivämäärä kertoo uusimman version."),
    "sv": dict(
        h="Integritetspolicy", upd="Uppdaterad", who="Personuppgiftsansvarig",
        who_t=f"Appen ges ut av {OWNER}. Kontakt: <a href='mailto:{CONTACT}'>{CONTACT}</a>.",
        data="Vilka uppgifter appen behandlar",
        data_t="Appen kräver inget konto. Dina framsteg, inställningar och provresultat sparas bara på din enhet. "
               "Det enda som lämnar enheten är den anonyma användningsstatistik som beskrivs nedan.",
        no="Användningsstatistik (Google Analytics for Firebase)",
        no_t="För att ta reda på vilka delar av appen som används och vad som kan förbättras skickar appen anonyma användningshändelser till "
             "Google Analytics for Firebase (Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irland): vilka vyer du öppnar, "
             "vilka knappar du trycker på, när en övningsrunda eller ett övningsprov börjar och slutar (resultatet som intervall, t.ex. ”70–84 %”) "
             "samt köpsteg. Firebase-SDK:n registrerar också tekniska uppgifter som app- och iOS-version, enhetsmodell, "
             "land/region (härlett från IP-adressen, som inte sparas) och ett slumpmässigt app-instans-ID som nollställs när du raderar appen. "
             "Namn, e-postadress, text från frågor eller svar eller annat innehåll du anger skickas inte. Uppgifterna kopplas inte till din identitet. "
             "Appen använder inte reklam-ID (IDFA), visar ingen reklam och spårar dig inte i andra appar eller på webbplatser. "
             "Rättslig grund: vårt berättigade intresse av att förbättra appen (artikel 6.1 f GDPR). Google kan behandla uppgifter i USA; "
             "Google LLC är certifierat enligt EU–USA:s dataskyddsram (Data Privacy Framework). Händelsedata raderas efter 2 månader. "
             "Se <a href='https://policies.google.com/privacy?hl=sv'>Googles integritetspolicy</a> och "
             "<a href='https://firebase.google.com/support/privacy'>Privacy and Security in Firebase</a>.",
        buy="Köp", buy_t="Engångsköpet i appen hanteras helt av Apple via App Store. Vi får inte dina betalningsuppgifter. "
               "Se <a href='https://www.apple.com/se/legal/privacy/'>Apples integritetspolicy</a>.",
        rate="Betyg", rate_t="Appen kan be dig betygsätta den med Apples vanliga betygsdialog. Betygen hanteras av Apple.",
        del_="Radera dina uppgifter", del_t="När du raderar appen tas alla uppgifter som den sparat på din enhet bort.",
        rights="Dina rättigheter", rights_t="Har du frågor om den här policyn eller dina uppgifter kan du kontakta oss på adressen ovan. "
               "Du kan när som helst stänga av användningsstatistiken i appens inställningar (”Skicka användningsstatistik”); därefter skickas inga händelser (artikel 21 GDPR). "
               "När du raderar appen raderas även app-instans-ID:t. "
               "Eftersom statistiken inte är kopplad till din identitet kan vi inte känna igen dina uppgifter i den.",
        chg="Ändringar", chg_t="Vi kan uppdatera den här policyn. Datumet ovan visar den senaste versionen."),
}

# Per-app extras (keyed by language). Keep app-specific facts here so pages can diverge later.
APPS = {
    "inburgering-examen": ("Inburgering Examen", ["nl", "en"], {
        "nl": ('Spreken, luisteren en voorlezen', "Luisterteksten, woorden en voorbeeldantwoorden worden voorgelezen met de spraakfunctie van iOS op je apparaat; daarvoor wordt niets verstuurd. Bij de spreekopdrachten gebruikt de app de microfoon en de spraakherkenning van Apple, alleen als je daar in iOS toestemming voor geeft. Op iPhones die het ondersteunen gebeurt de herkenning volledig op het apparaat. Op andere apparaten stuurt iOS je gesproken antwoord naar Apple om er tekst van te maken; dat is de enige uitzondering op ‘alleen de gebruiksstatistieken verlaten je apparaat’. Apple verwerkt die audio volgens het <a href='https://www.apple.com/nl/legal/privacy/'>privacybeleid van Apple</a>. Wij ontvangen je stem en je antwoord nooit: de app neemt geen audio op in een bestand, slaat je gesproken of getypte antwoord niet op en controleert de tekst alleen op je apparaat. Je kunt in plaats van spreken ook typen, en je kunt de toegang tot microfoon en spraakherkenning altijd intrekken in de iOS-instellingen."),
        "en": ('Speaking, listening and read-aloud', "Listening texts, words and model answers are read aloud with the iOS speech engine on your device; nothing is sent for this. For the speaking tasks the app uses the microphone and Apple's speech recognition, only if you allow this in iOS. On iPhones that support it, recognition happens entirely on the device. On other devices iOS sends your spoken answer to Apple to turn it into text; this is the only exception to “only the usage statistics leave your device”. Apple processes that audio under <a href='https://www.apple.com/legal/privacy/'>Apple's Privacy Policy</a>. We never receive your voice or your answer: the app does not record audio to a file, does not store your spoken or typed answer, and checks the text only on your device. You can type instead of speaking, and you can withdraw microphone and speech-recognition access at any time in iOS Settings."),
    }),
    "vca-examen": ("VeiligExamen – Basis & VOL", ["nl", "en"], {
        "nl": ("Voorlezen", "De voorleesfunctie gebruikt de spraakfunctie van iOS op je apparaat. Er wordt geen audio opgenomen of verstuurd."),
        "en": ("Read aloud", "The read-aloud feature uses the on-device iOS speech engine. No audio is recorded or sent anywhere."),
    }),
    "sachkunde-34a": ("34a Sachkunde Prüfung", ["de", "en"], {
        "de": ("Externe Links", "Gesetzesverweise öffnen öffentliche Webseiten (z. B. gesetze-im-internet.de) in deinem Browser. Dort gelten die Datenschutzbestimmungen des jeweiligen Anbieters."),
        "en": ("External links", "Legal references open public websites (e.g. gesetze-im-internet.de) in your browser. Those sites' own privacy policies apply."),
    }),
    "klein-vaarbewijs-nl": ("Klein Vaarbewijs 1 & 2", ["nl", "en", "de"], {
        "nl": ("Herinneringen en geluid", "De dagelijkse herinnering is een lokale melding die je iPhone zelf plant; daarvoor wordt niets verstuurd. Geluidsseinen worden op je apparaat als toon gemaakt; de app gebruikt geen microfoon."),
        "en": ("Reminders and sound", "The daily reminder is a local notification scheduled by your iPhone; nothing is sent for it. Sound signals are generated as tones on your device; the app does not use the microphone."),
        "de": ("Erinnerungen und Ton", "Die tägliche Erinnerung ist eine lokale Mitteilung, die dein iPhone selbst plant; dafür wird nichts gesendet. Schallsignale werden auf deinem Gerät als Ton erzeugt; die App nutzt kein Mikrofon."),
    }),
    "fischereischein": ("Fischereischein: Angelschein", ["de", "en"], {}),
    "golf-platzreife": ("Platzreife: Golfregeln Quiz", ["de", "nl", "en"], {}),
    "duelighedsbevis-dk": ("Duelighedsbevis – Teori & Test", ["da", "en", "de"], {}),
    "metsastajatutkinto-fi": ("Metsästäjätutkinto 2026", ["fi", "sv", "en"], {
        "fi": ("Metsästysajat", "Lajikorttien metsästysajat ja rauhoitustiedot ovat sovelluksen mukana; sovellus ei hae tietoja verkosta. Tarkista voimassa oleva tilanne ennen metsälle lähtöä."),
        "sv": ("Jakttider", "Jakttiderna och fredningsuppgifterna på artkorten följer med appen; appen hämtar inga uppgifter från nätet. Kontrollera gällande läge före jakten."),
        "en": ("Hunting seasons", "The hunting seasons and protection status on the species cards are bundled with the app; it does not fetch anything from the internet. Check the current rules before you go hunting."),
    }),
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
links += "<li><a href='statsborgerprove-no/'>Statsborgerprøven</a></li>"  # page from statsborgerprove_no.py
links += "<li><a href='indfodsretsprove-dk/'>Indfødsretsprøven</a></li>"  # page from indfodsretsprove_dk.py
with open("index.html", "w") as f:
    f.write(f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>Privacy Policies</title><style>{CSS}</style></head><body><h1>Privacy Policies</h1><ul>{links}</ul></body></html>")

if __name__ == "__main__":
    for slug in APPS:
        s = open(f"{slug}/index.html").read()
        assert CONTACT in s and "Apple" in s, slug
    print("ok", list(APPS))


# --- Support pages: <slug>/support/ (App Store "Support URL"). Independent per app, like the privacy pages.
S = {
    "en": dict(h="Support", contact="Questions or problems? Email us at <a href='mailto:{c}'>{c}</a>. We usually reply within 2 business days.",
               faq="Frequently asked questions",
               q=[("How do I restore my purchase?", "Open Settings in the app and tap “Restore purchases”. Use the same Apple ID you bought with."),
                  ("Does the full version work on my other devices?", "Yes. The one-time purchase is linked to your Apple ID. Restore it on each device."),
                  ("How do I get a refund?", "Refunds are handled by Apple: <a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>."),
                  ("Where is my progress stored?", "Only on your device. Deleting the app deletes your progress.")],
               priv="Privacy Policy"),
    "de": dict(h="Support", contact="Fragen oder Probleme? Schreib uns an <a href='mailto:{c}'>{c}</a>. Wir antworten meist innerhalb von 2 Werktagen.",
               faq="Häufige Fragen",
               q=[("Wie stelle ich meinen Kauf wieder her?", "Öffne in der App die Einstellungen und tippe auf „Käufe wiederherstellen“. Verwende dieselbe Apple-ID wie beim Kauf."),
                  ("Gilt die Vollversion auch auf meinen anderen Geräten?", "Ja. Der einmalige Kauf ist an deine Apple-ID gebunden. Stelle ihn auf jedem Gerät wieder her."),
                  ("Wie bekomme ich eine Erstattung?", "Erstattungen laufen über Apple: <a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>."),
                  ("Wo wird mein Fortschritt gespeichert?", "Nur auf deinem Gerät. Wenn du die App löschst, wird auch dein Fortschritt gelöscht.")],
               priv="Datenschutzerklärung"),
    "da": dict(h="Support", contact="Spørgsmål eller problemer? Skriv til os på <a href='mailto:{c}'>{c}</a>. Vi svarer som regel inden for 2 hverdage.",
               faq="Ofte stillede spørgsmål",
               q=[("Hvordan gendanner jeg mit køb?", "Åbn Indstillinger i appen, og tryk på “Gendan køb”. Brug det samme Apple-id, som du købte med."),
                  ("Virker den fulde version også på mine andre enheder?", "Ja. Engangskøbet er knyttet til dit Apple-id. Gendan det på hver enhed."),
                  ("Hvordan får jeg pengene tilbage?", "Refusion håndteres af Apple: <a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>."),
                  ("Hvor gemmes mine fremskridt?", "Kun på din enhed. Sletter du appen, slettes dine fremskridt også.")],
               priv="Privatlivspolitik"),
    "nl": dict(h="Support", contact="Vragen of problemen? Mail ons via <a href='mailto:{c}'>{c}</a>. We antwoorden meestal binnen 2 werkdagen.",
               faq="Veelgestelde vragen",
               q=[("Hoe herstel ik mijn aankoop?", "Open Instellingen in de app en tik op ‘Aankopen herstellen’. Gebruik dezelfde Apple ID als bij de aankoop."),
                  ("Werkt de volledige versie ook op mijn andere apparaten?", "Ja. De eenmalige aankoop is gekoppeld aan je Apple ID. Herstel hem op elk apparaat."),
                  ("Hoe krijg ik mijn geld terug?", "Terugbetalingen lopen via Apple: <a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>."),
                  ("Waar wordt mijn voortgang opgeslagen?", "Alleen op je apparaat. Als je de app verwijdert, is je voortgang ook weg.")],
               priv="Privacybeleid"),
    "fi": dict(h="Tuki", contact="Kysyttävää tai ongelmia? Lähetä sähköpostia osoitteeseen <a href='mailto:{c}'>{c}</a>. Vastaamme yleensä kahden arkipäivän kuluessa.",
               faq="Usein kysyttyä",
               q=[("Miten palautan ostokseni?", "Avaa sovelluksessa Asetukset ja napauta ”Palauta ostos”. Käytä samaa Apple ID:tä, jolla ostit."),
                  ("Toimiiko täysi versio myös muilla laitteillani?", "Kyllä. Kertaosto on sidottu Apple ID:hesi. Palauta se jokaisella laitteella."),
                  ("Miten saan rahani takaisin?", "Hyvitykset hoitaa Apple: <a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>."),
                  ("Mihin edistymiseni tallennetaan?", "Vain laitteellesi. Jos poistat sovelluksen, myös edistymisesi poistuu.")],
               priv="Tietosuojaseloste"),
    "sv": dict(h="Support", contact="Frågor eller problem? Mejla oss på <a href='mailto:{c}'>{c}</a>. Vi svarar oftast inom 2 arbetsdagar.",
               faq="Vanliga frågor",
               q=[("Hur återställer jag mitt köp?", "Öppna Inställningar i appen och tryck på ”Återställ köp”. Använd samma Apple-ID som du köpte med."),
                  ("Fungerar fullversionen på mina andra enheter?", "Ja. Engångsköpet är kopplat till ditt Apple-ID. Återställ det på varje enhet."),
                  ("Hur får jag pengarna tillbaka?", "Återbetalningar hanteras av Apple: <a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>."),
                  ("Var sparas mina framsteg?", "Bara på din enhet. Om du raderar appen raderas även dina framsteg.")],
               priv="Integritetspolicy"),
}

for slug, (name, langs, _) in APPS.items():
    os.makedirs(f"{slug}/support", exist_ok=True)
    secs = []
    for l in langs:
        s = S[l]
        qa = "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in s["q"])
        secs.append(f"<section id='{l}' lang='{l}'><h1>{s['h']} – {name}</h1><p>{s['contact'].format(c=CONTACT)}</p>"
                    f"<h2>{s['faq']}</h2>{qa}<p><a href='../'>{s['priv']}</a></p></section>")
    nav = "".join(f"<a href='#{l}'>{l.upper()}</a>" for l in langs)
    with open(f"{slug}/support/index.html", "w") as f:
        f.write(f"<!doctype html><html lang='{langs[0]}'><head><meta charset='utf-8'>"
                f"<meta name='viewport' content='width=device-width,initial-scale=1'><title>{name} – Support</title>"
                f"<style>{CSS}h3{{font-size:1em;margin-bottom:0}}</style></head><body><nav>{nav}</nav>{'<hr>'.join(secs)}</body></html>")
    assert CONTACT in open(f"{slug}/support/index.html").read(), slug
print("support ok")
