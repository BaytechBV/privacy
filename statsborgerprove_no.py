# Privacy + support pages for Statsborgerprøven (statsborgerprove-no/). Separate from build.py because this app
# (1.0) sends no usage statistics: GoogleService-Info.plist is not in the app, so Firebase never starts.
# If analytics is added, switch this page to the Firebase wording in build.py (and add a settings toggle).
import os

CONTACT = "utqsall@gmail.com"
OWNER = "Mustafa Utku Bayık"
UPDATED = "2026-10-15"
SLUG, NAME = "statsborgerprove-no", "Statsborgerprøven"
M = f"<a href='mailto:{CONTACT}'>{CONTACT}</a>"
REFUND = "<a href='https://reportaproblem.apple.com'>reportaproblem.apple.com</a>"

P = {
    "nb": [("Personvernerklæring", "Sist oppdatert"),
           ("Hvem vi er", f"Appen er utgitt av {OWNER}. Kontakt: {M}."),
           ("Hvilke data appen behandler", "Appen trenger ingen konto. Fremgang, innstillinger og resultater fra øvingsprøver lagres bare på enheten din. "
            "Appen sender ingen data til oss eller til andre: ingen bruksstatistikk, ingen reklame, ingen sporing. Den virker uten internett."),
           ("Kjøp", "Engangskjøpet i appen håndteres helt av Apple via App Store. Vi får ikke betalingsopplysningene dine. "
            "Se <a href='https://www.apple.com/no/legal/privacy/'>Apples personvernerklæring</a>."),
           ("Vurderinger", "Appen kan be deg om å vurdere den med Apples vanlige dialog. Vurderinger håndteres av Apple."),
           ("Slette data", "Når du sletter appen, slettes alle data den har lagret på enheten. I Innstillinger kan du også nullstille fremgangen."),
           ("Dine rettigheter", "Har du spørsmål om denne erklæringen eller dataene dine, kontakt oss på adressen over. Vi lagrer ingen data om deg."),
           ("Endringer", "Vi kan endre denne erklæringen. Datoen over viser gjeldende versjon.")],
    "en": [("Privacy Policy", "Last updated"),
           ("Who we are", f"This app is published by {OWNER}. Contact: {M}."),
           ("What data the app processes", "The app does not require an account. Your progress, settings and mock test results are stored only on your device. "
            "The app sends no data to us or anyone else: no usage statistics, no ads, no tracking. It works offline."),
           ("Purchases", "The one-time in-app purchase is handled entirely by Apple via the App Store. We do not receive your payment details. "
            "See <a href='https://www.apple.com/legal/privacy/'>Apple's Privacy Policy</a>."),
           ("Ratings", "The app may ask you to rate it using Apple's standard rating dialog. Ratings are handled by Apple."),
           ("Deleting your data", "Deleting the app removes all data it stored on your device. You can also reset your progress in Settings."),
           ("Your rights", "If you have questions about this policy or your data, contact us at the address above. We do not hold any data about you."),
           ("Changes", "We may update this policy. The date above shows the latest version.")],
    "pl": [("Polityka prywatności", "Ostatnia aktualizacja"),
           ("Kim jesteśmy", f"Aplikację wydaje {OWNER}. Kontakt: {M}."),
           ("Jakie dane przetwarza aplikacja", "Aplikacja nie wymaga konta. Postępy, ustawienia i wyniki egzaminów próbnych są zapisywane tylko na Twoim urządzeniu. "
            "Aplikacja nie wysyła żadnych danych do nas ani nikogo innego: bez statystyk użycia, bez reklam, bez śledzenia. Działa bez internetu."),
           ("Zakupy", "Jednorazowy zakup w aplikacji w całości obsługuje Apple przez App Store. Nie otrzymujemy Twoich danych płatniczych. "
            "Zobacz <a href='https://www.apple.com/pl/legal/privacy/'>Politykę prywatności Apple</a>."),
           ("Oceny", "Aplikacja może poprosić Cię o ocenę za pomocą standardowego okna Apple. Oceny obsługuje Apple."),
           ("Usuwanie danych", "Usunięcie aplikacji usuwa wszystkie dane zapisane przez nią na urządzeniu. Postępy możesz też wyzerować w Ustawieniach."),
           ("Twoje prawa", "Jeśli masz pytania dotyczące tej polityki lub swoich danych, napisz na powyższy adres. Nie przechowujemy żadnych danych o Tobie."),
           ("Zmiany", "Możemy zmienić tę politykę. Data powyżej wskazuje aktualną wersję.")],
    "ar": [("سياسة الخصوصية", "آخر تحديث"),
           ("من نحن", f"ينشر هذا التطبيق {OWNER}. للتواصل: {M}."),
           ("البيانات التي يعالجها التطبيق", "لا يحتاج التطبيق إلى حساب. يُحفظ تقدّمك وإعداداتك ونتائج الامتحانات التجريبية على جهازك فقط. "
            "لا يرسل التطبيق أي بيانات إلينا أو إلى أي جهة أخرى: لا إحصاءات استخدام، لا إعلانات، لا تتبّع. ويعمل دون إنترنت."),
           ("المشتريات", "تتولى Apple عملية الشراء الواحدة داخل التطبيق بالكامل عبر App Store. لا نحصل على بيانات الدفع الخاصة بك. "
            "راجع <a href='https://www.apple.com/legal/privacy/'>سياسة خصوصية Apple</a>."),
           ("التقييمات", "قد يطلب منك التطبيق تقييمه عبر نافذة Apple المعتادة. تتولى Apple التقييمات."),
           ("حذف بياناتك", "حذف التطبيق يحذف كل البيانات التي حفظها على جهازك. ويمكنك أيضًا إعادة ضبط التقدّم من الإعدادات."),
           ("حقوقك", "إذا كانت لديك أسئلة عن هذه السياسة أو عن بياناتك، راسلنا على العنوان أعلاه. لا نحتفظ بأي بيانات عنك."),
           ("التغييرات", "قد نحدّث هذه السياسة. التاريخ أعلاه يبيّن أحدث نسخة.")],
}

S = {
    "nb": ("Support", f"Spørsmål eller problemer? Skriv til {M}. Vi svarer vanligvis innen 2 virkedager.", "Vanlige spørsmål",
           [("Hvordan gjenoppretter jeg kjøpet?", "Åpne Innstillinger i appen og trykk «Gjenopprett kjøp». Bruk samme Apple-ID som da du kjøpte."),
            ("Virker fullversjonen på mine andre enheter?", "Ja. Engangskjøpet er knyttet til Apple-ID-en din. Gjenopprett det på hver enhet."),
            ("Hvordan får jeg pengene tilbake?", f"Refusjon håndteres av Apple: {REFUND}."),
            ("Hvor lagres fremgangen min?", "Bare på enheten din. Sletter du appen, slettes også fremgangen.")], "Personvernerklæring"),
    "en": ("Support", f"Questions or problems? Email us at {M}. We usually reply within 2 business days.", "Frequently asked questions",
           [("How do I restore my purchase?", "Open Settings in the app and tap “Restore purchase”. Use the same Apple ID you bought with."),
            ("Does the full version work on my other devices?", "Yes. The one-time purchase is linked to your Apple ID. Restore it on each device."),
            ("How do I get a refund?", f"Refunds are handled by Apple: {REFUND}."),
            ("Where is my progress stored?", "Only on your device. Deleting the app deletes your progress.")], "Privacy Policy"),
    "pl": ("Pomoc", f"Pytania lub problemy? Napisz do nas: {M}. Zwykle odpowiadamy w ciągu 2 dni roboczych.", "Najczęstsze pytania",
           [("Jak przywrócić zakup?", "Otwórz Ustawienia w aplikacji i stuknij „Przywróć zakup”. Użyj tego samego Apple ID co przy zakupie."),
            ("Czy pełna wersja działa na moich innych urządzeniach?", "Tak. Jednorazowy zakup jest powiązany z Twoim Apple ID. Przywróć go na każdym urządzeniu."),
            ("Jak odzyskać pieniądze?", f"Zwrotami zajmuje się Apple: {REFUND}."),
            ("Gdzie są zapisane moje postępy?", "Tylko na Twoim urządzeniu. Usunięcie aplikacji usuwa też postępy.")], "Polityka prywatności"),
    "ar": ("الدعم", f"لديك سؤال أو مشكلة؟ راسلنا على {M}. نردّ عادةً خلال يومي عمل.", "الأسئلة الشائعة",
           [("كيف أستعيد عملية الشراء؟", "افتح الإعدادات في التطبيق واضغط «استعادة الشراء». استخدم معرّف Apple نفسه الذي اشتريت به."),
            ("هل تعمل النسخة الكاملة على أجهزتي الأخرى؟", "نعم. الشراء مرتبط بمعرّف Apple الخاص بك. استعده على كل جهاز."),
            ("كيف أسترد المبلغ؟", f"تتولى Apple عمليات الاسترداد: {REFUND}."),
            ("أين يُحفظ تقدّمي؟", "على جهازك فقط. حذف التطبيق يحذف تقدّمك أيضًا.")], "سياسة الخصوصية"),
}

CSS = """:root{--bg:#fff;--fg:#1c1c1e;--mu:#6b6b70;--ac:#0a66c2}
@media (prefers-color-scheme:dark){:root{--bg:#111;--fg:#eee;--mu:#9a9aa0;--ac:#5aa9ff}}
body{background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:720px;margin:0 auto;padding:24px 16px}
h1{font-size:1.6em;margin-bottom:.2em}h2{font-size:1.15em;margin-top:1.6em}h3{font-size:1em;margin-bottom:0}a{color:var(--ac)}
.mu{color:var(--mu)}nav a{margin-right:12px}hr{border:0;border-top:1px solid var(--mu);opacity:.3;margin:40px 0}"""


def page(title, sections):
    nav = "".join(f"<a href='#{l}'>{l.upper()}</a>" for l in P)
    return (f"<!doctype html><html lang='nb'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
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
    assert CONTACT in s and "Apple" in s and s.count("<section") == 4, f
print("ok", SLUG)
