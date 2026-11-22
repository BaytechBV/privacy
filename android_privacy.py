# Android (Google Play) facts and texts shared by the page generators (build.py, hafta46_pages.py, indfodsretsprove_dk.py,
# statsborgerprove_no.py, landing.py) and by the hand-written privacy pages of the same apps.
#   - PLAY: privacy dir → Google Play package (only apps that are live on Google Play).
#   - android_html(slug, lang): the "Android (Google Play)" privacy paragraph for that app in that language.
#   - play_url(slug), PLAY_LABEL[lang]: the Google Play text button on the app web pages.
# Facts are read from each repo's Android build that is on Play (branch release/android-1.0.1, else feat/android;
# Tirelire: wt/tirelire-android feat/android), checked 2026-11-22. Re-check when an Android build changes:
#   android:allowBackup (all "true" → backup sentence), firebase-analytics + app/google-services.json (else NOFB),
#   AppAnalytics.enabledByDefault (false → OPTIN), com.google.android.play:review (else NOREVIEW),
#   ProductType.SUBS (SUBS), POST_NOTIFICATIONS (else NONOTIF), CAMERA / location / RECORD_AUDIO / biometric (EXTRA),
#   iOS iCloud features that do not exist on Android (LOCAL). The AD_ID permission is removed in every Firebase build.

UPDATED = "2026-11-22"
HEAD = "Android (Google Play)"
GOOGLE_PRIVACY = "https://policies.google.com/privacy"

PLAY = {
    "abonnement-nordic": "com.baytechbv.abonnement", "airfryer-nordic": "com.baytech.airfryer",
    "ajokortti-teoria-fi": "com.baytechbv.ajokortti", "alkohol-servering-eu": "com.baytechbv.serveringsklar",
    "anhuker-nordic": "com.baytechbv.anhukerklar", "antincendio-it": "com.baytechbv.antincendiopronto",
    "ap-traener-dk": "com.baytechbv.apklar", "ausbilderpruefung-at": "com.baytechbv.ausbilderklar",
    "babytegn-nordic": "com.baytechbv.babyhender", "bhv-examen-nl": "com.baytechbv.bhvklaar",
    "bloeddonor-nl": "com.baytechbv.bloedmaatje", "blutgas-eu": "com.baytechbv.gasklar",
    "botekalk-nordic": "com.baytechbv.botekalk", "dosering-nordic": "com.baytechbv.dosisklar",
    "duelighedsbevis-dk": "com.baytechbv.duelighedsbevis", "enummer-nordic": "com.baytechbv.enummer",
    "fischerpruefung-at": "com.baytechbv.fischerpruefungat", "forarintyg-se": "com.baytechbv.forarintyg",
    "golf-greencard-nordic": "com.baytechbv.greencard", "hestegym-eu": "com.baytechbv.hestegym",
    "hygieniapassi-fi": "com.baytechbv.hygieniapassi", "indfodsretsprove-dk": "com.baytechbv.indfodsret",
    "jagdpruefung-at": "com.baytechbv.jagdpruefungat", "karta-wedkarska-pl": "com.baytechbv.kartawedkarska",
    "korkortsteori-sprak-nordic": "com.baytechbv.teoriklar", "lastbil-c-nordic": "com.baytechbv.rekkaklar",
    "lesestart-nordic": "com.baytechbv.lesestart", "medborgarskapsprov-se": "com.baytechbv.medborgarskap",
    "metsastajatutkinto-fi": "com.baytechbv.metsastajatutkinto", "moped-am-eu": "com.baytechbv.amklar",
    "motorsaege-dach": "com.baytechbv.saegeschein", "onskelista-nordic": "com.baytechbv.onskelista",
    "ovningskorning-nordic": "com.baytechbv.ovningskorning", "skismoring-nordic": "com.baytechbv.smorklar",
    "snoskoter-nordic": "com.baytechbv.skoterklar", "src-vhf-nordic": "com.baytechbv.srcklar",
    "statsborgerprove-no": "com.baytechbv.statsborger", "taxiprov-eu": "com.baytechbv.taxiklar",
    "trailerklar-nordic": "com.baytechbv.trailerklar", "traktor-eu": "com.baytechbv.traktorklar",
    "verkeersexamen-eu": "com.baytechbv.verkeersheld", "tirelire": "com.baytechbv.tirelire",
}

# No usage statistics on Android: no Firebase at all (lesestart, verkeersexamen) or firebase-analytics without
# google-services.json, so Firebase never starts and nothing is sent (blutgas, botekalk, fischer, jagd, snoskoter).
NOFB = {"lesestart-nordic", "verkeersexamen-eu", "blutgas-eu", "botekalk-nordic", "fischerpruefung-at", "jagdpruefung-at",
        "snoskoter-nordic"}
OPTIN = {"ajokortti-teoria-fi", "indfodsretsprove-dk", "medborgarskapsprov-se", "ovningskorning-nordic", "statsborgerprove-no",
         "tirelire"}
NOREVIEW = {"blutgas-eu", "botekalk-nordic", "lesestart-nordic"}
SUBS = {"abonnement-nordic", "airfryer-nordic"}
NONOTIF = {"enummer-nordic", "fischerpruefung-at", "golf-greencard-nordic", "lesestart-nordic", "statsborgerprove-no"}
LOCAL = {"onskelista-nordic", "tirelire"}  # iOS syncs/shares through iCloud; Android keeps everything on the phone
EXTRA = {"abonnement-nordic": "biometric", "enummer-nordic": "camera", "ovningskorning-nordic": "location",
         "src-vhf-nordic": "mic", "onskelista-nordic": "share", "tirelire": "family"}

PLAY_LABEL = {"da": "Hent på Google Play", "nb": "Last ned på Google Play", "sv": "Ladda ned på Google Play",
              "fi": "Lataa Google Playsta", "de": "Jetzt bei Google Play", "nl": "Download op Google Play",
              "pl": "Pobierz z Google Play", "it": "Disponibile su Google Play", "fr": "Disponible sur Google Play",
              "en": "Get it on Google Play", "ar": "احصل عليه من Google Play", "tr": "Google Play'den indir"}
PLAY_LABEL["fr-ca"], PLAY_LABEL["en-us"], PLAY_LABEL["no"] = PLAY_LABEL["fr"], PLAY_LABEL["en"], PLAY_LABEL["nb"]


def gp(text):
    return f"<a href='{GOOGLE_PRIVACY}'>{text}</a>"


T = {
    "en": dict(
        base="The Android version from Google Play works the same way: what you enter stays on your Android device.",
        local="The Android version from Google Play does not use iCloud: what you enter stays on your Android device.",
        backup="If backup is switched on in your phone's settings, Android may include the app's data in your backup to your Google account; that backup is handled by Google, not by us.",
        buy=f"Purchases go through Google Play Billing; we receive no payment details. Google's {gp('privacy policy')} applies.",
        subs="You can manage or cancel the subscription in Google Play › Payments & subscriptions.",
        fb="The same usage statistics are collected on Android, with technical data such as the Android version, device model and a random app-instance ID; the Android advertising ID is not used.",
        optout="You can switch them off at any time in the app's settings.",
        optin="They are sent only if you switch them on in the app, and you can switch them off again at any time.",
        nofb="The Android version sends no usage statistics.",
        review="Ratings use Google Play's in-app review dialog, which is handled by Google.",
        notif="Reminders are local notifications on your device; on Android 13 and later the app first asks for permission to show notifications.",
        biometric="If you turn on the app lock, Android checks your fingerprint, face or screen lock; the app never receives biometric data.",
        camera="The label scanner uses the camera only while it is open; the text is recognised on your phone and no image is saved or sent.",
        location="Location is used only while a practice drive is being recorded, and Android shows a notification during the recording; the positions are stored only on your device and never sent.",
        mic="For the spoken calls the app uses the microphone and Android's on-device speech recognition; the audio is not recorded, stored or sent. If your phone has no on-device recognition, you type the call instead.",
        share="To share a list, the app creates a link that contains the list (without photos) after the # in the address; browsers do not send that part to any server, but anyone with the link can see the list. Link previews work as on iPhone: the request goes from your phone directly to the shop's website.",
        family="The family is kept on this phone only; sharing with the other parent through iCloud is not available on Android. The parent lock uses your phone's screen lock; we receive no biometric data."),
    "sv": dict(
        base="Androidversionen från Google Play fungerar på samma sätt: det du lägger in stannar på din Android-enhet.",
        local="Androidversionen från Google Play använder inte iCloud: det du lägger in stannar på din Android-enhet.",
        backup="Om säkerhetskopiering är påslagen i telefonens inställningar kan Android ta med appens data i din säkerhetskopia på ditt Google-konto; den hanteras av Google, inte av oss.",
        buy=f"Köp går via Google Play Billing; vi får inga betaluppgifter. Googles {gp('integritetspolicy')} gäller.",
        subs="Du hanterar eller avslutar prenumerationen i Google Play › Betalningar och prenumerationer.",
        fb="Samma användningsstatistik samlas in på Android, med tekniska uppgifter som Android-version, enhetsmodell och ett slumpmässigt installations-id; Androids annons-id används inte.",
        optout="Du kan stänga av den när som helst i appens inställningar.",
        optin="Den skickas bara om du slår på den i appen, och du kan stänga av den igen när som helst.",
        nofb="Androidversionen skickar ingen användningsstatistik.",
        review="Betyg ges i Google Plays dialogruta för omdömen i appen, som hanteras av Google.",
        notif="Påminnelser är lokala aviseringar på din enhet; på Android 13 och senare ber appen först om lov att visa aviseringar.",
        biometric="Om du slår på applåset kontrollerar Android ditt fingeravtryck, ansikte eller skärmlås; appen får aldrig några biometriska data.",
        camera="Etikettskannern använder kameran bara medan den är öppen; texten läses av på telefonen och ingen bild sparas eller skickas.",
        location="Platsen används bara medan en övningskörning spelas in, och Android visar en avisering under inspelningen; positionerna sparas bara på din enhet och skickas aldrig.",
        mic="När du övar anrop högt använder appen mikrofonen och Androids taligenkänning på enheten; ljudet spelas inte in, sparas inte och skickas inte. Har telefonen ingen taligenkänning på enheten skriver du anropet i stället.",
        share="För att dela en lista skapar appen en länk där listan (utan bilder) ligger efter # i adressen; den delen skickar webbläsare inte till någon server, men alla som har länken kan se listan. Länkförhandsvisningar fungerar som på iPhone: förfrågan går direkt från telefonen till butikens webbplats.",
        family="Familjen sparas bara på den här telefonen; delning med den andra föräldern via iCloud finns inte på Android. Föräldralåset använder telefonens skärmlås; vi får inga biometriska data."),
    "nb": dict(
        base="Android-versjonen fra Google Play fungerer på samme måte: det du legger inn, blir på Android-enheten din.",
        local="Android-versjonen fra Google Play bruker ikke iCloud: det du legger inn, blir på Android-enheten din.",
        backup="Hvis sikkerhetskopiering er slått på i telefonens innstillinger, kan Android ta med appens data i sikkerhetskopien på Google-kontoen din; den håndteres av Google, ikke av oss.",
        buy=f"Kjøp går gjennom Google Play Billing; vi mottar ingen betalingsopplysninger. Googles {gp('personvernerklæring')} gjelder.",
        subs="Du administrerer eller avslutter abonnementet i Google Play › Betalinger og abonnementer.",
        fb="Den samme bruksstatistikken samles inn på Android, med tekniske data som Android-versjon, enhetsmodell og en tilfeldig installasjons-ID; Androids reklame-ID brukes ikke.",
        optout="Du kan slå den av når som helst i appens innstillinger.",
        optin="Den sendes bare hvis du slår den på i appen, og du kan slå den av igjen når som helst.",
        nofb="Android-versjonen sender ingen bruksstatistikk.",
        review="Vurderinger gis i Google Plays vurderingsdialog i appen, som håndteres av Google.",
        notif="Påminnelser er lokale varsler på enheten din; på Android 13 og nyere ber appen først om tillatelse til å vise varsler.",
        biometric="Slår du på applåsen, sjekker Android fingeravtrykket, ansiktet eller skjermlåsen din; appen får aldri biometriske data.",
        camera="Etikettskanneren bruker kameraet bare mens den er åpen; teksten leses på telefonen, og ingen bilder lagres eller sendes.",
        location="Posisjonen brukes bare mens en øvelseskjøring tas opp, og Android viser et varsel under opptaket; posisjonene lagres bare på enheten din og sendes aldri.",
        mic="Når du øver anrop høyt, bruker appen mikrofonen og Androids talegjenkjenning på enheten; lyden blir ikke tatt opp, lagret eller sendt. Har telefonen ikke talegjenkjenning på enheten, skriver du anropet i stedet.",
        share="For å dele en liste lager appen en lenke der listen (uten bilder) står etter # i adressen; den delen sender nettlesere ikke til noen server, men alle som har lenken, kan se listen. Forhåndsvisning av lenker fungerer som på iPhone: forespørselen går direkte fra telefonen til butikkens nettside.",
        family="Familien lagres bare på denne telefonen; deling med den andre forelderen via iCloud finnes ikke på Android. Foreldrelåsen bruker telefonens skjermlås; vi mottar ingen biometriske data."),
    "da": dict(
        base="Android-versionen fra Google Play fungerer på samme måde: det, du indtaster, bliver på din Android-enhed.",
        local="Android-versionen fra Google Play bruger ikke iCloud: det, du indtaster, bliver på din Android-enhed.",
        backup="Hvis sikkerhedskopiering er slået til i telefonens indstillinger, kan Android tage appens data med i din sikkerhedskopi på din Google-konto; den håndteres af Google, ikke af os.",
        buy=f"Køb går gennem Google Play Billing; vi modtager ingen betalingsoplysninger. Googles {gp('privatlivspolitik')} gælder.",
        subs="Du administrerer eller opsiger abonnementet i Google Play › Betalinger og abonnementer.",
        fb="Den samme brugsstatistik indsamles på Android, med tekniske data som Android-version, enhedsmodel og et tilfældigt installations-id; Androids annonce-id bruges ikke.",
        optout="Du kan slå den fra når som helst i appens indstillinger.",
        optin="Den sendes kun, hvis du slår den til i appen, og du kan slå den fra igen når som helst.",
        nofb="Android-versionen sender ingen brugsstatistik.",
        review="Bedømmelser sker i Google Plays bedømmelsesdialog i appen, som håndteres af Google.",
        notif="Påmindelser er lokale notifikationer på din enhed; på Android 13 og nyere beder appen først om tilladelse til at vise notifikationer.",
        biometric="Slår du applåsen til, tjekker Android dit fingeraftryk, dit ansigt eller din skærmlås; appen modtager aldrig biometriske data.",
        camera="Etiketscanneren bruger kun kameraet, mens den er åben; teksten aflæses på telefonen, og intet billede gemmes eller sendes.",
        location="Placeringen bruges kun, mens en øvelseskørsel optages, og Android viser en notifikation under optagelsen; positionerne gemmes kun på din enhed og sendes aldrig.",
        mic="Når du øver opkald højt, bruger appen mikrofonen og Androids talegenkendelse på enheden; lyden bliver ikke optaget, gemt eller sendt. Har telefonen ingen talegenkendelse på enheden, skriver du opkaldet i stedet.",
        share="For at dele en liste laver appen et link, hvor listen (uden billeder) står efter # i adressen; den del sender browsere ikke til nogen server, men alle med linket kan se listen. Forhåndsvisning af links fungerer som på iPhone: forespørgslen går direkte fra telefonen til butikkens hjemmeside.",
        family="Familien gemmes kun på denne telefon; deling med den anden forælder via iCloud findes ikke på Android. Forælderlåsen bruger telefonens skærmlås; vi modtager ingen biometriske data."),
    "fi": dict(
        base="Google Playn Android-versio toimii samalla tavalla: tallentamasi tiedot pysyvät Android-laitteessasi.",
        local="Google Playn Android-versio ei käytä iCloudia: tallentamasi tiedot pysyvät Android-laitteessasi.",
        backup="Jos varmuuskopiointi on päällä puhelimen asetuksissa, Android voi sisällyttää sovelluksen tiedot Google-tilisi varmuuskopioon; sitä hoitaa Google, ei me.",
        buy=f"Ostot tehdään Google Play Billingin kautta; emme saa maksutietojasi. Sovelletaan Googlen {gp('tietosuojakäytäntöä')}.",
        subs="Voit hallita tilausta tai peruuttaa sen Google Playssa kohdassa Maksut ja tilaukset.",
        fb="Androidilla kerätään samat käyttötilastot sekä teknisiä tietoja, kuten Android-versio, laitemalli ja satunnainen asennustunnus; Androidin mainostunnusta ei käytetä.",
        optout="Voit kytkeä ne pois milloin tahansa sovelluksen asetuksista.",
        optin="Niitä lähetetään vain, jos kytket ne päälle sovelluksessa, ja voit kytkeä ne pois milloin tahansa.",
        nofb="Android-versio ei lähetä käyttötilastoja.",
        review="Arviot annetaan Google Playn sovelluksen sisäisessä arviointi-ikkunassa, jota hoitaa Google.",
        notif="Muistutukset ovat laitteesi paikallisia ilmoituksia; Android 13:ssa ja uudemmissa sovellus pyytää ensin luvan näyttää ilmoituksia.",
        biometric="Jos otat sovelluslukituksen käyttöön, Android tarkistaa sormenjälkesi, kasvosi tai näytön lukituksen; sovellus ei koskaan saa biometrisiä tietoja.",
        camera="Etikettiskanneri käyttää kameraa vain, kun se on auki; teksti tunnistetaan puhelimessa, eikä kuvia tallenneta tai lähetetä.",
        location="Sijaintia käytetään vain, kun opetusajoa tallennetaan, ja Android näyttää tallennuksen ajan ilmoituksen; sijainnit tallennetaan vain laitteellesi eikä niitä lähetetä minnekään.",
        mic="Kun harjoittelet kutsuja ääneen, sovellus käyttää mikrofonia ja Androidin laitteella toimivaa puheentunnistusta; ääntä ei tallenneta eikä lähetetä. Jos puhelimessa ei ole laitteella toimivaa puheentunnistusta, kirjoitat kutsun.",
        share="Listan jakamista varten sovellus luo linkin, jossa lista (ilman kuvia) on osoitteessa #-merkin jälkeen; selaimet eivät lähetä sitä osaa millekään palvelimelle, mutta kuka tahansa linkin saanut näkee listan. Linkkien esikatselut toimivat kuten iPhonessa: pyyntö menee puhelimesta suoraan kaupan verkkosivulle.",
        family="Perhe tallennetaan vain tähän puhelimeen; jakaminen toisen vanhemman kanssa iCloudin kautta ei ole Androidilla käytettävissä. Vanhemman lukitus käyttää puhelimen näytön lukitusta; emme saa biometrisiä tietoja."),
    "de": dict(
        base="Die Android-Version aus Google Play funktioniert genauso: Was du eingibst, bleibt auf deinem Android-Gerät.",
        local="Die Android-Version aus Google Play nutzt keine iCloud: Was du eingibst, bleibt auf deinem Android-Gerät.",
        backup="Ist die Sicherung in den Einstellungen deines Handys eingeschaltet, kann Android die Daten der App in deine Sicherung im Google-Konto aufnehmen; diese Sicherung verwaltet Google, nicht wir.",
        buy=f"Käufe laufen über Google Play Billing; wir erhalten keine Zahlungsdaten. Es gilt die {gp('Datenschutzerklärung von Google')}.",
        subs="Das Abo verwaltest oder kündigst du in Google Play › Zahlungen und Abos.",
        fb="Auf Android wird dieselbe Nutzungsstatistik erhoben, mit technischen Daten wie Android-Version, Gerätemodell und einer zufälligen App-Instanz-ID; die Werbe-ID von Android wird nicht verwendet.",
        optout="Du kannst sie jederzeit in den Einstellungen der App ausschalten.",
        optin="Sie wird nur gesendet, wenn du sie in der App einschaltest, und du kannst sie jederzeit wieder ausschalten.",
        nofb="Die Android-Version sendet keine Nutzungsstatistik.",
        review="Bewertungen laufen über den In-App-Bewertungsdialog von Google Play, den Google verwaltet.",
        notif="Erinnerungen sind lokale Mitteilungen auf deinem Gerät; ab Android 13 fragt die App vorher um Erlaubnis, Mitteilungen anzuzeigen.",
        biometric="Schaltest du die App-Sperre ein, prüft Android deinen Fingerabdruck, dein Gesicht oder deine Displaysperre; die App erhält nie biometrische Daten.",
        camera="Der Etikettenscanner nutzt die Kamera nur, solange er geöffnet ist; der Text wird auf dem Handy erkannt, und kein Bild wird gespeichert oder gesendet.",
        location="Der Standort wird nur verwendet, solange eine Übungsfahrt aufgezeichnet wird, und Android zeigt währenddessen eine Mitteilung an; die Positionen werden nur auf deinem Gerät gespeichert und nie gesendet.",
        mic="Beim lauten Üben von Funksprüchen nutzt die App das Mikrofon und die Spracherkennung von Android auf dem Gerät; der Ton wird nicht aufgenommen, gespeichert oder gesendet. Hat dein Handy keine Spracherkennung auf dem Gerät, tippst du den Funkspruch stattdessen ein.",
        share="Zum Teilen einer Liste erstellt die App einen Link, in dem die Liste (ohne Fotos) hinter dem # der Adresse steht; diesen Teil senden Browser an keinen Server, aber alle mit dem Link können die Liste sehen. Linkvorschauen funktionieren wie auf dem iPhone: Die Anfrage geht direkt vom Handy an die Website des Shops.",
        family="Die Familie wird nur auf diesem Handy gespeichert; das Teilen mit dem anderen Elternteil über iCloud gibt es auf Android nicht. Die Elternsperre nutzt die Displaysperre des Handys; wir erhalten keine biometrischen Daten."),
    "nl": dict(
        base="De Android-versie uit Google Play werkt op dezelfde manier: wat je invoert, blijft op je Android-apparaat.",
        local="De Android-versie uit Google Play gebruikt geen iCloud: wat je invoert, blijft op je Android-apparaat.",
        backup="Als back-up in de instellingen van je telefoon aanstaat, kan Android de gegevens van de app opnemen in je back-up in je Google-account; die back-up wordt door Google beheerd, niet door ons.",
        buy=f"Aankopen lopen via Google Play Billing; we ontvangen geen betaalgegevens. Het {gp('privacybeleid van Google')} is van toepassing.",
        subs="Je beheert of annuleert het abonnement in Google Play › Betalingen en abonnementen.",
        fb="Op Android worden dezelfde gebruiksstatistieken verzameld, met technische gegevens zoals de Android-versie, het apparaatmodel en een willekeurige app-instantie-ID; de advertentie-ID van Android wordt niet gebruikt.",
        optout="Je kunt ze op elk moment uitzetten in de instellingen van de app.",
        optin="Ze worden alleen verstuurd als je ze in de app aanzet, en je kunt ze op elk moment weer uitzetten.",
        nofb="De Android-versie verstuurt geen gebruiksstatistieken.",
        review="Beoordelingen lopen via het beoordelingsvenster van Google Play in de app, dat door Google wordt beheerd.",
        notif="Herinneringen zijn lokale meldingen op je apparaat; vanaf Android 13 vraagt de app eerst toestemming om meldingen te tonen.",
        biometric="Als je de app-vergrendeling aanzet, controleert Android je vingerafdruk, gezicht of schermvergrendeling; de app ontvangt nooit biometrische gegevens.",
        camera="De etiketscanner gebruikt de camera alleen zolang hij open is; de tekst wordt op je telefoon herkend en er wordt geen foto bewaard of verstuurd.",
        location="Je locatie wordt alleen gebruikt terwijl een oefenrit wordt opgenomen, en Android toont tijdens de opname een melding; de posities worden alleen op je apparaat bewaard en nooit verstuurd.",
        mic="Als je oproepen hardop oefent, gebruikt de app de microfoon en de spraakherkenning van Android op het apparaat; het geluid wordt niet opgenomen, bewaard of verstuurd. Heeft je telefoon geen spraakherkenning op het apparaat, dan typ je de oproep.",
        share="Om een lijst te delen maakt de app een link waarin de lijst (zonder foto's) na het #-teken in het adres staat; browsers sturen dat deel naar geen enkele server, maar iedereen met de link kan de lijst zien. Linkvoorbeelden werken zoals op de iPhone: het verzoek gaat rechtstreeks van je telefoon naar de website van de winkel.",
        family="Het gezin wordt alleen op deze telefoon bewaard; delen met de andere ouder via iCloud kan op Android niet. De ouderlijke vergrendeling gebruikt de schermvergrendeling van je telefoon; we ontvangen geen biometrische gegevens."),
    "pl": dict(
        base="Wersja na Androida z Google Play działa tak samo: to, co wprowadzasz, zostaje na Twoim urządzeniu z Androidem.",
        local="Wersja na Androida z Google Play nie korzysta z iCloud: to, co wprowadzasz, zostaje na Twoim urządzeniu z Androidem.",
        backup="Jeśli w ustawieniach telefonu włączona jest kopia zapasowa, Android może dołączyć dane aplikacji do kopii zapasowej na Twoim koncie Google; tą kopią zarządza Google, nie my.",
        buy=f"Zakupy odbywają się przez Google Play Billing; nie otrzymujemy danych płatniczych. Obowiązuje {gp('polityka prywatności Google')}.",
        subs="Subskrypcją zarządzasz lub ją anulujesz w Google Play › Płatności i subskrypcje.",
        fb="Na Androidzie zbierane są te same statystyki użytkowania wraz z danymi technicznymi, takimi jak wersja Androida, model urządzenia i losowy identyfikator instancji aplikacji; identyfikator reklamowy Androida nie jest używany.",
        optout="Możesz je w każdej chwili wyłączyć w ustawieniach aplikacji.",
        optin="Są wysyłane tylko wtedy, gdy włączysz je w aplikacji, i w każdej chwili możesz je znowu wyłączyć.",
        nofb="Wersja na Androida nie wysyła statystyk użytkowania.",
        review="Oceny są wystawiane w okienku oceny Google Play w aplikacji, którym zarządza Google.",
        notif="Przypomnienia to lokalne powiadomienia na Twoim urządzeniu; na Androidzie 13 i nowszym aplikacja najpierw prosi o zgodę na wyświetlanie powiadomień."),
    "it": dict(
        base="La versione Android da Google Play funziona allo stesso modo: ciò che inserisci resta sul tuo dispositivo Android.",
        local="La versione Android da Google Play non usa iCloud: ciò che inserisci resta sul tuo dispositivo Android.",
        backup="Se il backup è attivo nelle impostazioni del telefono, Android può includere i dati dell'app nel backup sul tuo account Google; quel backup è gestito da Google, non da noi.",
        buy=f"Gli acquisti passano da Google Play Billing; non riceviamo dati di pagamento. Si applica l'{gp('informativa sulla privacy di Google')}.",
        subs="Puoi gestire o annullare l'abbonamento in Google Play › Pagamenti e abbonamenti.",
        fb="Su Android vengono raccolte le stesse statistiche d'uso, con dati tecnici come la versione di Android, il modello del dispositivo e un ID casuale dell'istanza dell'app; l'ID pubblicità di Android non viene usato.",
        optout="Puoi disattivarle in qualsiasi momento nelle impostazioni dell'app.",
        optin="Vengono inviate solo se le attivi nell'app, e puoi disattivarle di nuovo in qualsiasi momento.",
        nofb="La versione Android non invia statistiche d'uso.",
        review="Le valutazioni usano la finestra di recensione in-app di Google Play, gestita da Google.",
        notif="I promemoria sono notifiche locali sul tuo dispositivo; da Android 13 l'app chiede prima il permesso di mostrare notifiche."),
    "fr": dict(
        base="La version Android de Google Play fonctionne de la même façon : ce que vous saisissez reste sur votre appareil Android.",
        local="La version Android de Google Play n’utilise pas iCloud : ce que vous saisissez reste sur votre appareil Android.",
        backup="Si la sauvegarde est activée dans les réglages du téléphone, Android peut inclure les données de l’app dans votre sauvegarde sur votre compte Google ; cette sauvegarde est gérée par Google, pas par nous.",
        buy=f"Les achats passent par Google Play Billing ; nous ne recevons aucune donnée de paiement. La {gp('politique de confidentialité de Google')} s’applique.",
        subs="Vous gérez ou résiliez l’abonnement dans Google Play › Paiements et abonnements.",
        fb="Les mêmes statistiques d’utilisation sont collectées sur Android, avec des données techniques comme la version d’Android, le modèle de l’appareil et un identifiant aléatoire d’instance de l’app ; l’identifiant publicitaire d’Android n’est pas utilisé.",
        optout="Vous pouvez les désactiver à tout moment dans les réglages de l’app.",
        optin="Elles ne sont envoyées que si vous les activez dans l’app, et vous pouvez les désactiver à tout moment.",
        nofb="La version Android n’envoie aucune statistique d’utilisation.",
        review="Les notes passent par la fenêtre d’avis intégrée de Google Play, gérée par Google.",
        notif="Les rappels sont des notifications locales sur votre appareil ; à partir d’Android 13, l’app demande d’abord l’autorisation d’afficher des notifications.",
        family="La famille est enregistrée uniquement sur ce téléphone ; le partage avec l’autre parent via iCloud n’existe pas sur Android. Le verrouillage parental utilise le verrouillage d’écran du téléphone ; nous ne recevons aucune donnée biométrique."),
    "tr": dict(
        base="Google Play'deki Android sürümü de aynı şekilde çalışır: girdiğin bilgiler Android cihazında kalır.",
        local="Google Play'deki Android sürümü iCloud kullanmaz: girdiğin bilgiler Android cihazında kalır.",
        backup="Telefonunun ayarlarında yedekleme açıksa Android, uygulamanın verilerini Google hesabındaki yedeğe ekleyebilir; bu yedeği biz değil Google yönetir.",
        buy=f"Satın alımlar Google Play Faturalandırma üzerinden yapılır; ödeme bilgilerini almayız. Google'ın {gp('gizlilik politikası')} geçerlidir.",
        subs="Aboneliği Google Play › Ödemeler ve abonelikler bölümünden yönetebilir veya iptal edebilirsin.",
        fb="Android'de de aynı kullanım istatistikleri toplanır; Android sürümü, cihaz modeli ve rastgele bir uygulama örneği kimliği gibi teknik veriler de buna dahildir. Android reklam kimliği kullanılmaz.",
        optout="İstatistikleri uygulamanın ayarlarından istediğin zaman kapatabilirsin.",
        optin="Yalnızca uygulamada açarsan gönderilir ve istediğin zaman yeniden kapatabilirsin.",
        nofb="Android sürümü kullanım istatistiği göndermez.",
        review="Değerlendirmeler, Google'ın yönettiği Google Play uygulama içi değerlendirme penceresiyle yapılır.",
        notif="Hatırlatıcılar cihazındaki yerel bildirimlerdir; Android 13 ve sonrasında uygulama bildirim göstermek için önce izin ister."),
    "ar": dict(
        base="تعمل نسخة Android من Google Play بالطريقة نفسها: ما تُدخله يبقى على جهاز Android الخاص بك.",
        local="لا تستخدم نسخة Android من Google Play خدمة iCloud: ما تُدخله يبقى على جهاز Android الخاص بك.",
        backup="إذا كان النسخ الاحتياطي مفعّلًا في إعدادات هاتفك، فقد يضمّن Android بيانات التطبيق في نسختك الاحتياطية على حساب Google الخاص بك؛ وتتولى Google إدارة هذه النسخة، لا نحن.",
        buy=f"تتم عمليات الشراء عبر نظام الفوترة في Google Play، ولا نتلقى أي بيانات دفع. وتسري {gp('سياسة خصوصية Google')}.",
        subs="يمكنك إدارة الاشتراك أو إلغاؤه في Google Play › الدفعات والاشتراكات.",
        fb="تُجمع إحصاءات الاستخدام نفسها على Android، مع بيانات تقنية مثل إصدار Android وطراز الجهاز ومعرّف عشوائي لنسخة التطبيق؛ ولا يُستخدم معرّف الإعلانات في Android.",
        optout="يمكنك إيقافها في أي وقت من إعدادات التطبيق.",
        optin="لا تُرسل إلا إذا فعّلتها في التطبيق، ويمكنك إيقافها مرة أخرى في أي وقت.",
        nofb="لا ترسل نسخة Android أي إحصاءات استخدام.",
        review="تتم التقييمات عبر نافذة التقييم داخل التطبيق من Google Play، وتتولاها Google.",
        notif="التذكيرات إشعارات محلية على جهازك؛ وفي Android 13 والإصدارات الأحدث يطلب التطبيق أولًا الإذن بعرض الإشعارات."),
}


def android_html(slug, lang):
    """The 'Android (Google Play)' paragraph (HTML, no wrapping tag) for one app in one language."""
    t = T[lang]
    s = [t["local"] if slug in LOCAL else t["base"]]
    if slug in EXTRA and EXTRA[slug] in ("share", "family"):
        s.append(t[EXTRA[slug]])
    s.append(t["backup"])
    s.append(t["buy"] + (" " + t["subs"] if slug in SUBS else ""))
    if slug in NOFB:
        s.append(t["nofb"])
    else:
        s.append(t["fb"] + " " + (t["optin"] if slug in OPTIN else t["optout"]))
    if slug not in NOREVIEW:
        s.append(t["review"])
    if slug not in NONOTIF:
        s.append(t["notif"])
    if slug in EXTRA and EXTRA[slug] not in ("share", "family"):
        s.append(t[EXTRA[slug]])
    return " ".join(s)


def play_url(slug):
    return f"https://play.google.com/store/apps/details?id={PLAY[slug]}"


if __name__ == "__main__":  # print every paragraph for review
    import sys
    for slug in sorted(PLAY) if len(sys.argv) < 2 else sys.argv[1:]:
        for lang in T:
            try:
                print(slug, lang, android_html(slug, lang))
            except KeyError:
                pass
