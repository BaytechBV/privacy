# Privacy + support pages for Indfødsretsprøven (indfodsretsprove-dk/). Separate from build.py because the wording is
# app-specific. Since 1.1.1 the app sends anonymous usage statistics (Google Analytics for Firebase, FirebaseAnalyticsCore,
# no IDFA) while the "Send usage statistics" switch in Settings is on (default on, opt-out). Texts follow
# docs/privacy-page-draft-1.1.1.md in the app repo and match the App Store privacy label (usage data, identifier,
# coarse location, purchases, diagnostics; analytics only, not linked, no tracking).
import os

CONTACT = "utqsall@gmail.com"
OWNER = "Mustafa Utku Bayık"
UPDATED = "2026-10-19"
SLUG, NAME = "indfodsretsprove-dk", "Indfødsretsprøven"
M = f"<a href='mailto:{CONTACT}'>{CONTACT}</a>"
REFUND = "<a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>"


def GP(t):  # Google's Privacy Policy
    return f"<a href='https://policies.google.com/privacy'>{t}</a>"


def FB(t):  # Privacy and Security in Firebase
    return f"<a href='https://firebase.google.com/support/privacy'>{t}</a>"


P = {
    "da": [("Privatlivspolitik", "Sidst opdateret"),
           ("Hvem vi er", f"Appen udgives af {OWNER}. Kontakt: {M}."),
           ("Hvilke data appen behandler", "Appen kræver ingen konto. Dine fremskridt, indstillinger og resultater fra øveprøver gemmes kun på din enhed. "
            "Det eneste, der forlader din enhed, er den anonyme brugsstatistik, der er beskrevet nedenfor, og kun så længe »Send brugsstatistik« er slået til."),
           ("Brugsstatistik (Google Analytics for Firebase)",
            "For at se, hvilke dele af appen der bliver brugt, og hvor den kan blive bedre, sender appen anonyme brugshændelser til Google Analytics for Firebase "
            "(Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irland): hvilke skærme du åbner, hvilke knapper du trykker på, "
            "hvornår en øverunde eller øveprøve starter og slutter (med resultatet som et interval, fx »70–84 %«), om et link fra en App Store-begivenhed åbnede appen, "
            "og trin i et køb. Firebase-SDK'et registrerer også tekniske data og diagnosedata som appversion, iOS-version, enhedsmodel, land/region "
            "(udledt af IP-adressen, som ikke gemmes) og et tilfældigt app-instans-id, der nulstilles, når du sletter appen. "
            "Navn, e-mailadresse, spørgsmåls- eller svartekster, prøvedato og andet indhold sendes ikke. Dataene kobles ikke til din identitet. "
            "Appen bruger ikke reklame-id'et (IDFA), viser ingen reklamer og sporer dig ikke på tværs af apps eller websteder. "
            "Retsgrundlag: vores legitime interesse i at forbedre appen (GDPR art. 6, stk. 1, litra f). Google kan behandle data i USA; "
            "Google LLC er certificeret under EU-US Data Privacy Framework. Hændelsesdata slettes efter 2 måneder. "
            f"Se {GP('Googles privatlivspolitik')} og »{FB('Privacy and Security in Firebase')}«."),
           ("Køb", "Engangskøbet i appen håndteres helt af Apple via App Store. Vi modtager ikke dine betalingsoplysninger. "
            "Se <a href='https://www.apple.com/dk/legal/privacy/'>Apples privatlivspolitik</a>."),
           ("Bedømmelser", "Appen kan bede dig om at bedømme den med Apples almindelige dialog. Bedømmelser håndteres af Apple."),
           ("Slet dine data", "Når du sletter appen, slettes alle data, den har gemt på din enhed. Under Indstillinger kan du også nulstille dine fremskridt."),
           ("Dine rettigheder", "Har du spørgsmål om denne politik eller dine data (GDPR art. 15–21), så kontakt os på adressen ovenfor. "
            "Du kan altid slå brugsstatistikken fra i appens indstillinger (»Send brugsstatistik«); derefter sendes ingen hændelser (GDPR art. 21). "
            "Når du sletter appen, slettes app-instans-id'et også. Da statistikken ikke er koblet til din identitet, kan vi ikke finde dine data i den."),
           ("Ændringer", "Vi kan ændre denne politik. Datoen ovenfor viser den gældende version.")],
    "en": [("Privacy Policy", "Last updated"),
           ("Who we are", f"This app is published by {OWNER}. Contact: {M}."),
           ("What data the app processes", "The app does not require an account. Your progress, settings and mock test results are stored only on your device. "
            "The only data that leaves your device is the anonymous usage statistics described below, and only while “Send usage statistics” is switched on."),
           ("Usage statistics (Google Analytics for Firebase)",
            "To find out which parts of the app are used and where it can be improved, the app sends anonymous usage events to Google Analytics for Firebase "
            "(Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Ireland): which screens you open, which buttons you tap, "
            "when a practice round or mock test starts and ends (with the score as a range, e.g. “70–84%”), whether a link from an App Store event opened the app, "
            "and purchase steps. The Firebase SDK also records technical and diagnostic data such as app version, iOS version, device model, country/region "
            "(derived from the IP address, which is not stored) and a random app-instance ID that is reset when you delete the app. "
            "No name, e-mail address, question or answer text, exam date or other content is sent. The data is not linked to your identity. "
            "The app does not use the advertising identifier (IDFA), shows no ads and does not track you across apps or websites. "
            "Legal basis: our legitimate interest in improving the app (Art. 6(1)(f) GDPR). Google may process data in the USA; "
            "Google LLC is certified under the EU-US Data Privacy Framework. Event data is deleted after 2 months. "
            f"See {GP('Google&#39;s Privacy Policy')} and “{FB('Privacy and Security in Firebase')}”."),
           ("Purchases", "The one-time in-app purchase is handled entirely by Apple via the App Store. We do not receive your payment details. "
            "See <a href='https://www.apple.com/legal/privacy/'>Apple's Privacy Policy</a>."),
           ("Ratings", "The app may ask you to rate it using Apple's standard rating dialog. Ratings are handled by Apple."),
           ("Deleting your data", "Deleting the app removes all data it stored on your device. You can also reset your progress in Settings."),
           ("Your rights", "If you have questions about this policy or your data, contact us at the address above. "
            "You can switch the usage statistics off at any time in the app's settings (“Send usage statistics”); from then on no events are sent (Art. 21 GDPR). "
            "Deleting the app also deletes the app-instance ID. Because the statistics are not linked to your identity, we cannot identify your data in them."),
           ("Changes", "We may update this policy. The date above shows the latest version.")],
    "tr": [("Gizlilik Politikası", "Son güncelleme"),
           ("Biz kimiz", f"Bu uygulamayı {OWNER} yayınlamaktadır. İletişim: {M}."),
           ("Uygulamanın işlediği veriler", "Uygulama hesap gerektirmez. İlerlemen, ayarların ve deneme sınavı sonuçların yalnızca cihazında saklanır. "
            "Cihazından çıkan tek şey aşağıda açıklanan anonim kullanım istatistikleridir ve yalnızca “Kullanım istatistiği gönder” açıkken gönderilir."),
           ("Kullanım istatistikleri (Google Analytics for Firebase)",
            "Uygulamanın hangi bölümlerinin kullanıldığını ve nerede iyileştirilebileceğini görmek için uygulama, Google Analytics for Firebase'e "
            "(Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, İrlanda) anonim kullanım olayları gönderir: hangi ekranları açtığın, hangi düğmelere dokunduğun, "
            "bir alıştırma turunun veya deneme sınavının ne zaman başlayıp bittiği (sonuç bir aralık olarak, ör. “%70–84”), uygulamanın bir App Store etkinliği bağlantısıyla açılıp açılmadığı "
            "ve satın alma adımları. Firebase SDK ayrıca uygulama sürümü, iOS sürümü, cihaz modeli, ülke/bölge (IP adresinden çıkarılır, IP saklanmaz) "
            "ve uygulamayı sildiğinde sıfırlanan rastgele bir uygulama örneği kimliği gibi teknik ve tanılama verilerini kaydeder. "
            "Ad, e-posta adresi, soru veya cevap metinleri, sınav tarihi ya da başka içerik gönderilmez. Veriler kimliğinle ilişkilendirilmez. "
            "Uygulama reklam kimliğini (IDFA) kullanmaz, reklam göstermez ve seni başka uygulama veya sitelerde izlemez. "
            "Hukuki dayanak: uygulamayı iyileştirmeye yönelik meşru menfaatimiz (GDPR md. 6(1)(f)). Google verileri ABD'de işleyebilir; "
            "Google LLC, EU-US Data Privacy Framework kapsamında sertifikalıdır. Olay verileri 2 ay sonra silinir. "
            f"Bkz. {GP('Google Gizlilik Politikası')} ve “{FB('Privacy and Security in Firebase')}”."),
           ("Satın alma", "Uygulama içindeki tek seferlik satın alma tamamen Apple tarafından App Store üzerinden yürütülür. Ödeme bilgilerin bize ulaşmaz. "
            "Bkz. <a href='https://www.apple.com/tr/legal/privacy/'>Apple Gizlilik Politikası</a>."),
           ("Değerlendirmeler", "Uygulama, Apple'ın standart penceresiyle senden değerlendirme isteyebilir. Değerlendirmeleri Apple yönetir."),
           ("Verilerini silme", "Uygulamayı sildiğinde cihazında sakladığı tüm veriler silinir. İlerlemeni Ayarlar'dan da sıfırlayabilirsin."),
           ("Hakların", "Bu politika veya verilerin hakkında sorun varsa yukarıdaki adresten bize yaz (GDPR md. 15–21). "
            "Kullanım istatistiklerini uygulamanın ayarlarından (“Kullanım istatistiği gönder”) istediğin zaman kapatabilirsin; bundan sonra hiçbir olay gönderilmez (GDPR md. 21). "
            "Uygulamayı silmek uygulama örneği kimliğini de siler. İstatistikler kimliğinle ilişkili olmadığı için içlerinde senin verilerini bulamayız."),
           ("Değişiklikler", "Bu politikayı değiştirebiliriz. Yukarıdaki tarih geçerli sürümü gösterir.")],
    "ar": [("سياسة الخصوصية", "آخر تحديث"),
           ("من نحن", f"ينشر هذا التطبيق {OWNER}. للتواصل: {M}."),
           ("البيانات التي يعالجها التطبيق", "لا يحتاج التطبيق إلى حساب. يُحفظ تقدّمك وإعداداتك ونتائج الامتحانات التجريبية على جهازك فقط. "
            "الشيء الوحيد الذي يغادر جهازك هو إحصاءات الاستخدام المجهولة الموضّحة أدناه، وذلك فقط ما دام خيار «إرسال إحصاءات الاستخدام» مفعّلًا."),
           ("إحصاءات الاستخدام (Google Analytics for Firebase)",
            "لمعرفة أجزاء التطبيق المستخدمة وأين يمكن تحسينه، يرسل التطبيق أحداث استخدام مجهولة إلى Google Analytics for Firebase "
            "(Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Ireland): الشاشات التي تفتحها، والأزرار التي تضغطها، "
            "ومتى تبدأ جولة التدريب أو الامتحان التجريبي وتنتهي (مع النتيجة كنطاق، مثل «70–84٪»)، وما إذا فُتح التطبيق من رابط فعالية في App Store، "
            "وخطوات الشراء. يسجّل Firebase SDK أيضًا بيانات تقنية وتشخيصية مثل إصدار التطبيق وإصدار iOS وطراز الجهاز والبلد/المنطقة "
            "(مستنتجة من عنوان IP الذي لا يُحفظ) ومعرّفًا عشوائيًا لنسخة التطبيق يُعاد ضبطه عند حذف التطبيق. "
            "لا يُرسل الاسم أو البريد الإلكتروني أو نصوص الأسئلة والإجابات أو تاريخ الاختبار أو أي محتوى آخر. لا ترتبط البيانات بهويتك. "
            "لا يستخدم التطبيق معرّف الإعلانات (IDFA) ولا يعرض إعلانات ولا يتتبّعك عبر التطبيقات أو المواقع. "
            "الأساس القانوني: مصلحتنا المشروعة في تحسين التطبيق (المادة 6(1)(f) من اللائحة العامة لحماية البيانات). قد تعالج Google البيانات في الولايات المتحدة؛ "
            "وGoogle LLC معتمدة ضمن EU-US Data Privacy Framework. تُحذف بيانات الأحداث بعد شهرين. "
            f"راجع {GP('سياسة خصوصية Google')} و«{FB('Privacy and Security in Firebase')}»."),
           ("المشتريات", "تتولى Apple عملية الشراء الواحدة داخل التطبيق بالكامل عبر App Store. لا نحصل على بيانات الدفع الخاصة بك. "
            "راجع <a href='https://www.apple.com/legal/privacy/'>سياسة خصوصية Apple</a>."),
           ("التقييمات", "قد يطلب منك التطبيق تقييمه عبر نافذة Apple المعتادة. تتولى Apple التقييمات."),
           ("حذف بياناتك", "حذف التطبيق يحذف كل البيانات التي حفظها على جهازك. ويمكنك أيضًا إعادة ضبط التقدّم من الإعدادات."),
           ("حقوقك", "إذا كانت لديك أسئلة عن هذه السياسة أو عن بياناتك، راسلنا على العنوان أعلاه. "
            "يمكنك إيقاف إحصاءات الاستخدام في أي وقت من إعدادات التطبيق («إرسال إحصاءات الاستخدام»)؛ وبعدها لا يُرسل أي حدث (المادة 21). "
            "حذف التطبيق يحذف أيضًا معرّف نسخة التطبيق. ولأن الإحصاءات غير مرتبطة بهويتك، لا يمكننا العثور على بياناتك فيها."),
           ("التغييرات", "قد نحدّث هذه السياسة. التاريخ أعلاه يبيّن أحدث نسخة.")],
    "de": [("Datenschutzerklärung", "Stand"),
           ("Verantwortlicher", f"Diese App wird von {OWNER} veröffentlicht. Kontakt: {M}."),
           ("Welche Daten die App verarbeitet", "Die App benötigt kein Konto. Fortschritt, Einstellungen und Ergebnisse der Probetests werden ausschließlich auf deinem Gerät gespeichert. "
            "Dein Gerät verlassen nur die unten beschriebenen anonymen Nutzungsstatistiken, und nur solange „Nutzungsstatistik senden“ eingeschaltet ist."),
           ("Nutzungsstatistik (Google Analytics for Firebase)",
            "Um zu erfahren, welche Teile der App genutzt werden und wo wir sie verbessern können, sendet die App anonyme Nutzungsereignisse an Google Analytics for Firebase "
            "(Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irland): welche Bildschirme du öffnest, welche Schaltflächen du antippst, "
            "wann eine Übungsrunde oder ein Probetest beginnt und endet (mit dem Ergebnis als Spanne, z. B. „70–84 %“), ob ein Link aus einem App-Store-Event die App geöffnet hat, "
            "sowie Kaufschritte. Das Firebase-SDK erfasst außerdem technische und Diagnosedaten wie App-Version, iOS-Version, Gerätemodell, Land/Region "
            "(aus der IP-Adresse abgeleitet, die nicht gespeichert wird) und eine zufällige App-Instanz-ID, die beim Löschen der App zurückgesetzt wird. "
            "Name, E-Mail-Adresse, Frage- oder Antworttexte, Prüfungsdatum und andere Inhalte werden nicht übertragen. Die Daten werden nicht mit deiner Identität verknüpft. "
            "Die App nutzt keine Werbe-ID (IDFA), zeigt keine Werbung und verfolgt dich nicht über Apps oder Websites hinweg. "
            "Rechtsgrundlage: unser berechtigtes Interesse an der Verbesserung der App (Art. 6 Abs. 1 lit. f DSGVO). Google kann Daten in den USA verarbeiten; "
            "Google LLC ist nach dem EU-US Data Privacy Framework zertifiziert. Ereignisdaten werden nach 2 Monaten gelöscht. "
            f"Siehe {GP('Datenschutzerklärung von Google')} und „{FB('Datenschutz und Sicherheit in Firebase')}“."),
           ("Käufe", "Der einmalige In-App-Kauf wird vollständig von Apple über den App Store abgewickelt. Wir erhalten keine Zahlungsdaten. "
            "Siehe <a href='https://www.apple.com/de/legal/privacy/'>Datenschutzrichtlinie von Apple</a>."),
           ("Bewertungen", "Die App kann dich über den Standarddialog von Apple um eine Bewertung bitten. Bewertungen verarbeitet Apple."),
           ("Daten löschen", "Wenn du die App löschst, werden alle von ihr auf deinem Gerät gespeicherten Daten entfernt. In den Einstellungen kannst du deinen Fortschritt auch zurücksetzen."),
           ("Deine Rechte", "Bei Fragen zu dieser Erklärung oder zu deinen Daten (Art. 15–21 DSGVO) wende dich an die obige Adresse. "
            "Du kannst die Nutzungsstatistik jederzeit in den Einstellungen der App ausschalten („Nutzungsstatistik senden“); danach werden keine Ereignisse mehr gesendet (Art. 21 DSGVO). "
            "Mit dem Löschen der App wird auch die App-Instanz-ID gelöscht. Da die Statistik nicht mit deiner Identität verknüpft ist, können wir deine Daten darin nicht zuordnen."),
           ("Änderungen", "Wir können diese Erklärung anpassen. Das Datum oben zeigt die aktuelle Fassung.")],
    "pl": [("Polityka prywatności", "Ostatnia aktualizacja"),
           ("Kim jesteśmy", f"Aplikację wydaje {OWNER}. Kontakt: {M}."),
           ("Jakie dane przetwarza aplikacja", "Aplikacja nie wymaga konta. Twoje postępy, ustawienia i wyniki egzaminów próbnych są zapisywane tylko na Twoim urządzeniu. "
            "Urządzenie opuszczają jedynie anonimowe statystyki użycia opisane poniżej i tylko wtedy, gdy opcja „Wysyłaj statystyki użycia” jest włączona."),
           ("Statystyki użycia (Google Analytics for Firebase)",
            "Aby wiedzieć, które części aplikacji są używane i co można poprawić, aplikacja wysyła anonimowe zdarzenia do Google Analytics for Firebase "
            "(Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irlandia): które ekrany otwierasz, które przyciski naciskasz, "
            "kiedy zaczyna się i kończy runda ćwiczeń lub egzamin próbny (z wynikiem jako przedziałem, np. „70–84%”), czy aplikację otworzył link z wydarzenia w App Store, "
            "oraz etapy zakupu. SDK Firebase zapisuje też dane techniczne i diagnostyczne, takie jak wersja aplikacji i iOS, model urządzenia, kraj/region "
            "(ustalony na podstawie adresu IP, który nie jest zapisywany) oraz losowy identyfikator instancji aplikacji, resetowany po jej usunięciu. "
            "Imię, adres e-mail, treść pytań i odpowiedzi ani inne treści nie są wysyłane. Dane nie są powiązane z Twoją tożsamością. "
            "Aplikacja nie używa identyfikatora reklamowego (IDFA), nie wyświetla reklam i nie śledzi Cię w innych aplikacjach ani witrynach. "
            "Podstawa prawna: nasz prawnie uzasadniony interes w ulepszaniu aplikacji (art. 6 ust. 1 lit. f RODO). Google może przetwarzać dane w USA; "
            "Google LLC ma certyfikat EU-US Data Privacy Framework. Dane zdarzeń są usuwane po 2 miesiącach. "
            f"Zobacz {GP('Politykę prywatności Google')} oraz „{FB('Privacy and Security in Firebase')}”."),
           ("Zakupy", "Jednorazowy zakup w aplikacji w całości obsługuje Apple przez App Store. Nie otrzymujemy Twoich danych płatniczych. "
            "Zobacz <a href='https://www.apple.com/pl/legal/privacy/'>Politykę prywatności Apple</a>."),
           ("Oceny", "Aplikacja może poprosić Cię o ocenę za pomocą standardowego okna Apple. Oceny obsługuje Apple."),
           ("Usuwanie danych", "Usunięcie aplikacji usuwa wszystkie dane zapisane przez nią na urządzeniu. Postępy możesz też wyzerować w Ustawieniach."),
           ("Twoje prawa", "Jeśli masz pytania o tę politykę lub swoje dane (art. 15–21 RODO), napisz na adres powyżej. "
            "Statystyki użycia możesz w każdej chwili wyłączyć w ustawieniach aplikacji („Wysyłaj statystyki użycia”); od tej chwili żadne zdarzenia nie są wysyłane (art. 21 RODO). "
            "Usunięcie aplikacji usuwa też identyfikator instancji. Ponieważ statystyki nie są powiązane z Twoją tożsamością, nie możemy w nich odnaleźć Twoich danych."),
           ("Zmiany", "Możemy zmienić tę politykę. Data powyżej wskazuje aktualną wersję.")],
}

S = {
    "da": ("Support", f"Spørgsmål eller problemer? Skriv til {M}. Vi svarer normalt inden for 2 hverdage.", "Ofte stillede spørgsmål",
           [("Hvordan gendanner jeg mit køb?", "Åbn Indstillinger i appen, og tryk på »Gendan køb«. Brug det samme Apple-id, som du købte med."),
            ("Virker den fulde version på mine andre enheder?", "Ja. Engangskøbet er knyttet til dit Apple-id. Gendan det på hver enhed."),
            ("Hvordan får jeg pengene tilbage?", f"Refusion håndteres af Apple: {REFUND}."),
            ("Hvor gemmes mine fremskridt?", "Kun på din enhed. Sletter du appen, slettes dine fremskridt også."),
            ("Hvordan slår jeg brugsstatistikken fra?", "Åbn Indstillinger i appen, og slå »Send brugsstatistik« fra (kontakten over »Nulstil fremskridt«). "
             "Derefter sendes ingen hændelser.")], "Privatlivspolitik"),
    "en": ("Support", f"Questions or problems? Email us at {M}. We usually reply within 2 business days.", "Frequently asked questions",
           [("How do I restore my purchase?", "Open Settings in the app and tap “Restore purchase”. Use the same Apple ID you bought with."),
            ("Does the full version work on my other devices?", "Yes. The one-time purchase is linked to your Apple ID. Restore it on each device."),
            ("How do I get a refund?", f"Refunds are handled by Apple: {REFUND}."),
            ("Where is my progress stored?", "Only on your device. Deleting the app deletes your progress."),
            ("How do I switch off usage statistics?", "Open Settings in the app and switch off “Send usage statistics” (the switch above “Reset progress”). "
             "From then on no events are sent.")], "Privacy Policy"),
    "tr": ("Destek", f"Sorunun ya da bir problemin mi var? {M} adresine yaz. Genellikle 2 iş günü içinde yanıt veririz.", "Sık sorulan sorular",
           [("Satın alımımı nasıl geri yüklerim?", "Uygulamada Ayarlar'ı aç ve “Satın alımı geri yükle”ye dokun. Satın aldığın Apple Kimliği'ni kullan."),
            ("Tam sürüm diğer cihazlarımda çalışır mı?", "Evet. Tek seferlik satın alma Apple Kimliğine bağlıdır. Her cihazda geri yükle."),
            ("Paramı nasıl geri alırım?", f"İadeleri Apple yürütür: {REFUND}."),
            ("İlerlemem nerede saklanıyor?", "Yalnızca cihazında. Uygulamayı silersen ilerlemen de silinir."),
            ("Kullanım istatistiklerini nasıl kapatırım?", "Uygulamada Ayarlar'ı aç ve “Kullanım istatistiği gönder” anahtarını kapat (“İlerlemeyi sıfırla”nın üstündeki anahtar). "
             "Bundan sonra hiçbir olay gönderilmez.")], "Gizlilik Politikası"),
    "ar": ("الدعم", f"لديك سؤال أو مشكلة؟ راسلنا على {M}. نردّ عادةً خلال يومي عمل.", "الأسئلة الشائعة",
           [("كيف أستعيد عملية الشراء؟", "افتح الإعدادات في التطبيق واضغط «استعادة الشراء». استخدم معرّف Apple نفسه الذي اشتريت به."),
            ("هل تعمل النسخة الكاملة على أجهزتي الأخرى؟", "نعم. الشراء مرتبط بمعرّف Apple الخاص بك. استعده على كل جهاز."),
            ("كيف أسترد المبلغ؟", f"تتولى Apple عمليات الاسترداد: {REFUND}."),
            ("أين يُحفظ تقدّمي؟", "على جهازك فقط. حذف التطبيق يحذف تقدّمك أيضًا."),
            ("كيف أوقف إحصاءات الاستخدام؟", "افتح الإعدادات في التطبيق وأوقف «إرسال إحصاءات الاستخدام» (المفتاح فوق «إعادة ضبط التقدّم»). "
             "بعدها لا يُرسل أي حدث.")], "سياسة الخصوصية"),
    "de": ("Support", f"Fragen oder Probleme? Schreib uns an {M}. Wir antworten meist innerhalb von 2 Werktagen.", "Häufige Fragen",
           [("Wie stelle ich meinen Kauf wieder her?", "Öffne in der App die Einstellungen und tippe auf „Kauf wiederherstellen“. Verwende dieselbe Apple-ID wie beim Kauf."),
            ("Gilt die Vollversion auch auf meinen anderen Geräten?", "Ja. Der einmalige Kauf ist an deine Apple-ID gebunden. Stelle ihn auf jedem Gerät wieder her."),
            ("Wie bekomme ich eine Erstattung?", f"Erstattungen laufen über Apple: {REFUND}."),
            ("Wo wird mein Fortschritt gespeichert?", "Nur auf deinem Gerät. Wenn du die App löschst, wird auch dein Fortschritt gelöscht."),
            ("Wie schalte ich die Nutzungsstatistik aus?", "Öffne in der App die Einstellungen und schalte „Nutzungsstatistik senden“ aus (der Schalter über „Fortschritt zurücksetzen“). "
             "Danach werden keine Ereignisse mehr gesendet.")], "Datenschutzerklärung"),
    "pl": ("Pomoc", f"Pytania lub problemy? Napisz do nas: {M}. Zwykle odpowiadamy w ciągu 2 dni roboczych.", "Najczęstsze pytania",
           [("Jak przywrócić zakup?", "Otwórz Ustawienia w aplikacji i stuknij „Przywróć zakup”. Użyj tego samego Apple ID co przy zakupie."),
            ("Czy pełna wersja działa na moich innych urządzeniach?", "Tak. Jednorazowy zakup jest powiązany z Twoim Apple ID. Przywróć go na każdym urządzeniu."),
            ("Jak odzyskać pieniądze?", f"Zwrotami zajmuje się Apple: {REFUND}."),
            ("Gdzie są zapisane moje postępy?", "Tylko na Twoim urządzeniu. Usunięcie aplikacji usuwa też postępy."),
            ("Jak wyłączyć statystyki użycia?", "Otwórz Ustawienia w aplikacji i wyłącz „Wysyłaj statystyki użycia” (przełącznik nad „Zresetuj postęp”). "
             "Od tej chwili żadne zdarzenia nie są wysyłane.")], "Polityka prywatności"),
}

CSS = """:root{--bg:#fff;--fg:#1c1c1e;--mu:#6b6b70;--ac:#0a66c2}
@media (prefers-color-scheme:dark){:root{--bg:#111;--fg:#eee;--mu:#9a9aa0;--ac:#5aa9ff}}
body{background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:720px;margin:0 auto;padding:24px 16px}
h1{font-size:1.6em;margin-bottom:.2em}h2{font-size:1.15em;margin-top:1.6em}h3{font-size:1em;margin-bottom:0}a{color:var(--ac)}
.mu{color:var(--mu)}nav a{margin-right:12px}hr{border:0;border-top:1px solid var(--mu);opacity:.3;margin:40px 0}"""


def page(title, sections):
    nav = "".join(f"<a href='#{l}'>{l.upper()}</a>" for l in P)
    return (f"<!doctype html><html lang='da'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{NAME} – {title}</title><style>{CSS}</style></head><body><nav>{nav}</nav>{'<hr>'.join(sections)}</body></html>")


def sec(l, inner):
    return f"<section id='{l}' lang='{l}'{' dir=rtl' if l == 'ar' else ''}>{inner}</section>"


privacy = [sec(l, f"<h1>{p[0][0]} – {NAME}</h1><p class='mu'>{p[0][1]}: {UPDATED}</p>" + "".join(f"<h2>{h}</h2><p>{t}</p>" for h, t in p[1:]))
           for l, p in P.items()]
support = [sec(l, f"<h1>{h} – {NAME}</h1><p>{c}</p><h2>{faq}</h2>" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in qa) + f"<p><a href='../'>{priv}</a></p>")
           for l, (h, c, faq, qa, priv) in S.items()]

os.makedirs(f"{SLUG}/support", exist_ok=True)
open(f"{SLUG}/index.html", "w").write(page("Privacy", privacy))
open(f"{SLUG}/support/index.html", "w").write(page("Support", support))
for f in (f"{SLUG}/index.html", f"{SLUG}/support/index.html"):
    s = open(f).read()
    assert CONTACT in s and "Apple" in s and s.count("<section") == len(P) == len(S) == 6, f
    assert list(P) == list(S) == ["da", "en", "tr", "ar", "de", "pl"], f
    for l in P:
        assert f"<a href='#{l}'>{l.upper()}</a>" in s and f"<section id='{l}' lang='{l}'" in s, (f, l)
    assert s.count(" dir=rtl") == 1 and "<section id='ar' lang='ar' dir=rtl>" in s, f
p = open(f"{SLUG}/index.html").read()
assert p.count("https://policies.google.com/privacy") == len(P) and p.count("https://firebase.google.com/support/privacy") == len(P)
assert p.count("<h2>") == 8 * len(P)
print("ok", SLUG)
