// Page texts per tool and language. No "free/gratis" wording (store copy rule).
module.exports = {
  ui: {
    fr: { badge: "Télécharger dans l'App Store", lang: 'Langue', privacy: 'Confidentialité', about: "À propos de l'app", faq: 'Questions fréquentes' },
    en: { badge: 'Download on the App Store', lang: 'Language', privacy: 'Privacy', about: 'About the app', faq: 'Frequently asked questions' },
    da: { badge: 'Hent i App Store', lang: 'Sprog', privacy: 'Privatliv', about: 'Om appen', faq: 'Ofte stillede spørgsmål' },
    nb: { badge: 'Last ned fra App Store', lang: 'Språk', privacy: 'Personvern', about: 'Om appen', faq: 'Ofte stilte spørsmål' },
    sv: { badge: 'Hämta i App Store', lang: 'Språk', privacy: 'Integritet', about: 'Om appen', faq: 'Vanliga frågor' },
    fi: { badge: 'Lataa App Storesta', lang: 'Kieli', privacy: 'Tietosuoja', about: 'Tietoa sovelluksesta', faq: 'Usein kysytyt kysymykset' },
    de: { badge: 'Laden im App Store', lang: 'Sprache', privacy: 'Datenschutz', about: 'Über die App', faq: 'Häufige Fragen' },
    nl: { badge: 'Download in de App Store', lang: 'Taal', privacy: 'Privacy', about: 'Over de app', faq: 'Veelgestelde vragen' },
    ar: { badge: 'تنزيل من App Store', lang: 'اللغة', privacy: 'الخصوصية', about: 'عن التطبيق', faq: 'أسئلة شائعة' }
  },

  // ---------------------------------------------------------------- Tirelire
  tirelire: {
    fr: {
      slug: 'calculateur-epargne-enfant', cur: 'EUR',
      title: "Calculateur d'épargne enfant : objectif, argent de poche et date",
      desc: "Combien de semaines pour s'offrir un vélo avec son argent de poche ? Entrez le prix, ce qu'il y a déjà dans la tirelire et l'épargne par semaine ou par mois.",
      h1: "Calculateur d'objectif d'épargne pour enfant",
      lead: "Votre enfant rêve d'un vélo, d'un jeu ou d'une sortie ? Indiquez le prix, ce qu'il a déjà et ce qu'il met de côté : vous voyez quand l'objectif sera atteint, et combien épargner pour y arriver avant une date.",
      f: { goal: "Prix de l'objectif", saved: 'Déjà dans la tirelire', freq: 'Rythme', w: 'Chaque semaine', m: 'Chaque mois', per: 'Montant mis de côté', end: "Atteindre l'objectif avant le (facultatif)", go: 'Calculer' },
      t: { w: 'semaine', ws: 'semaines', m: 'mois', ms: 'mois', ew: 'par semaine', em: 'par mois',
        reach: "En mettant {per} de côté {every}, l'objectif est atteint en <b>{n} {units}</b>, vers le <b>{date}</b>.",
        need: "Pour l'atteindre avant le {date} : <b>{amt} {every}</b>.",
        tooSoon: 'Cette date est trop proche : choisissez-la au moins une période plus tard.',
        noPer: 'Indiquez le montant mis de côté pour voir la date.', done: "Bravo, l'objectif est déjà atteint !", rest: 'Il reste {amt} à économiser.' },
      cta: "Dans Tirelire, l'anneau de l'objectif avance à chaque argent de poche et à chaque tâche validée, avec la date estimée à son rythme.",
      faq: [
        ["Comment calculer le temps pour atteindre un objectif d'épargne ?", "Prenez ce qu'il reste à économiser (le prix moins ce qui est déjà dans la tirelire) et divisez-le par le montant mis de côté à chaque période, puis arrondissez à l'entier supérieur. Exemple : 60 € restants à 5 € par semaine = 12 semaines."],
        ["Faut-il épargner chaque semaine ou chaque mois ?", "Pour les plus jeunes, la semaine rend l'objectif plus concret : ils voient la tirelire se remplir plus souvent. Les ados gèrent souvent mieux un rythme mensuel. Le calculateur fait les deux."],
        ["Comment aider un enfant à atteindre son objectif plus vite ?", "Des petites tâches rémunérées en plus de l'argent de poche, ou une partie des cadeaux d'anniversaire mise de côté. Montrez-lui où il en est : voir l'objectif avancer motive."],
        ["Mes chiffres sont-ils enregistrés ?", "Non. Le calcul se fait dans votre navigateur ; rien n'est enregistré ni envoyé."]
      ]
    },
    en: {
      slug: 'kids-savings-goal-calculator', cur: 'GBP',
      title: "Kids' Savings Goal Calculator – pocket money and target date",
      desc: "How many weeks until your child can buy that bike? Enter the price, what's already in the piggy bank and what they save each week or month to see the date.",
      h1: "Kids' savings goal calculator",
      lead: "Saving up for a bike, a game or a day out? Enter the price, what your child already has and what they put aside – see when they'll get there, and how much to save to make it by a date.",
      f: { goal: 'Price of the goal', saved: 'Already in the piggy bank', freq: 'How often', w: 'Every week', m: 'Every month', per: 'Amount put aside', end: 'Reach the goal by (optional)', go: 'Calculate' },
      t: { w: 'week', ws: 'weeks', m: 'month', ms: 'months', ew: 'a week', em: 'a month',
        reach: 'Putting aside {per} {every}, the goal is reached in <b>{n} {units}</b>, around <b>{date}</b>.',
        need: 'To get there by {date}: <b>{amt} {every}</b>.',
        tooSoon: 'That date is too close – pick one at least one period later.',
        noPer: 'Enter the amount put aside to see the date.', done: 'Well done – the goal is already reached!', rest: '{amt} left to save.' },
      cta: "In Tirelire the goal ring fills up with every bit of pocket money and every approved chore, and shows the expected date at your child's pace.",
      faq: [
        ['How do I work out how long it takes to reach a savings goal?', "Take what's left to save (the price minus what's already in the piggy bank), divide it by the amount saved each period and round up. Example: £60 left at £5 a week = 12 weeks."],
        ['Should children save weekly or monthly?', 'For younger children weekly makes the goal feel real – they see the piggy bank grow more often. Teenagers often handle a monthly rhythm better. The calculator does both.'],
        ['How can my child reach the goal faster?', 'Small paid chores on top of pocket money, or putting part of birthday money aside. Show them their progress: seeing the goal get closer is motivating.'],
        ['Are my numbers saved anywhere?', 'No. Everything is calculated in your browser; nothing is stored or sent.']
      ]
    },
    da: {
      slug: 'opsparingsberegner-boern', cur: 'DKK',
      title: 'Opsparingsberegner til børn – lommepenge og sparemål',
      desc: 'Hvor mange uger før barnet kan købe cyklen for lommepengene? Indtast prisen, hvad der allerede er i sparegrisen, og hvad der spares op om ugen eller måneden.',
      h1: 'Opsparingsberegner til børn',
      lead: 'Sparer dit barn op til en cykel, et spil eller en tur? Indtast prisen, hvad barnet har, og hvad der lægges til side – så ser du, hvornår målet nås, og hvor meget der skal spares for at nå det til en bestemt dato.',
      f: { goal: 'Pris på målet', saved: 'Allerede i sparegrisen', freq: 'Hvor tit', w: 'Hver uge', m: 'Hver måned', per: 'Beløb, der spares', end: 'Nå målet senest (valgfrit)', go: 'Beregn' },
      t: { w: 'uge', ws: 'uger', m: 'måned', ms: 'måneder', ew: 'om ugen', em: 'om måneden',
        reach: 'Med {per} {every} nås målet om <b>{n} {units}</b>, omkring <b>{date}</b>.',
        need: 'For at nå det senest {date}: <b>{amt} {every}</b>.',
        tooSoon: 'Datoen er for tæt på – vælg en dato mindst én periode senere.',
        noPer: 'Indtast beløbet, der spares, for at se datoen.', done: 'Flot – målet er allerede nået!', rest: 'Der mangler {amt}.' },
      cta: 'I Tirelire fyldes målringen op med hver udbetaling af lommepenge og hver godkendt pligt, og den viser den forventede dato i barnets tempo.',
      faq: [
        ['Hvordan regner man ud, hvor lang tid et sparemål tager?', 'Tag det beløb, der mangler (prisen minus det, der allerede er sparet), del det med beløbet, der spares hver periode, og rund op. Eksempel: 600 kr. tilbage med 50 kr. om ugen = 12 uger.'],
        ['Skal børn spare hver uge eller hver måned?', 'For de mindste gør en ugentlig rytme målet mere konkret – de ser sparegrisen vokse oftere. Teenagere har det ofte bedre med en månedlig rytme. Beregneren kan begge dele.'],
        ['Hvordan når barnet målet hurtigere?', 'Små betalte pligter oven i lommepengene, eller en del af fødselsdagspengene lagt til side. Vis barnet, hvor langt det er: det motiverer at se målet komme tættere på.'],
        ['Bliver mine tal gemt?', 'Nej. Alt beregnes i din browser; intet gemmes eller sendes.']
      ]
    },
    nb: {
      slug: 'spareberegner-barn', cur: 'NOK',
      title: 'Spareberegner for barn – lommepenger og sparemål',
      desc: 'Hvor mange uker før barnet kan kjøpe sykkelen for lommepengene? Skriv inn prisen, hva som allerede er i sparegrisen og hva som spares hver uke eller måned.',
      h1: 'Spareberegner for barn',
      lead: 'Sparer barnet ditt til en sykkel, et spill eller en tur? Skriv inn prisen, hva barnet har og hva som settes av – så ser du når målet nås, og hvor mye som må spares for å nå det innen en dato.',
      f: { goal: 'Pris på målet', saved: 'Allerede i sparegrisen', freq: 'Hvor ofte', w: 'Hver uke', m: 'Hver måned', per: 'Beløp som settes av', end: 'Nå målet innen (valgfritt)', go: 'Beregn' },
      t: { w: 'uke', ws: 'uker', m: 'måned', ms: 'måneder', ew: 'i uken', em: 'i måneden',
        reach: 'Med {per} {every} nås målet om <b>{n} {units}</b>, rundt <b>{date}</b>.',
        need: 'For å nå det innen {date}: <b>{amt} {every}</b>.',
        tooSoon: 'Datoen er for nær – velg en dato minst én periode senere.',
        noPer: 'Skriv inn beløpet som settes av for å se datoen.', done: 'Bra jobbet – målet er allerede nådd!', rest: 'Det gjenstår {amt}.' },
      cta: 'I Tirelire fylles målringen for hver utbetaling av lommepenger og hvert godkjente gjøremål, og den viser forventet dato i barnets tempo.',
      faq: [
        ['Hvordan regner man ut hvor lang tid et sparemål tar?', 'Ta beløpet som gjenstår (prisen minus det som allerede er spart), del det på beløpet som spares hver periode, og rund opp. Eksempel: 600 kr igjen med 50 kr i uken = 12 uker.'],
        ['Bør barn spare hver uke eller hver måned?', 'For de minste gjør ukentlig sparing målet mer konkret – de ser sparegrisen vokse oftere. Tenåringer har det ofte bedre med en månedlig rytme. Beregneren gjør begge deler.'],
        ['Hvordan kan barnet nå målet raskere?', 'Små betalte gjøremål i tillegg til lommepengene, eller en del av bursdagspengene satt til side. Vis barnet hvor langt det har kommet: det motiverer å se målet nærme seg.'],
        ['Blir tallene mine lagret?', 'Nei. Alt regnes ut i nettleseren din; ingenting lagres eller sendes.']
      ]
    },
    sv: {
      slug: 'sparkalkylator-barn', cur: 'SEK',
      title: 'Sparkalkylator för barn – veckopeng och sparmål',
      desc: 'Hur många veckor tills barnet kan köpa cykeln för veckopengen? Fyll i priset, vad som redan finns i spargrisen och vad som sparas varje vecka eller månad.',
      h1: 'Sparkalkylator för barn',
      lead: 'Sparar ditt barn till en cykel, ett spel eller en utflykt? Fyll i priset, vad barnet har och vad som läggs undan – så ser du när målet nås och hur mycket som behöver sparas för att hinna till ett visst datum.',
      f: { goal: 'Pris på målet', saved: 'Redan i spargrisen', freq: 'Hur ofta', w: 'Varje vecka', m: 'Varje månad', per: 'Belopp som läggs undan', end: 'Nå målet senast (valfritt)', go: 'Räkna' },
      t: { w: 'vecka', ws: 'veckor', m: 'månad', ms: 'månader', ew: 'i veckan', em: 'i månaden',
        reach: 'Med {per} {every} nås målet om <b>{n} {units}</b>, runt <b>{date}</b>.',
        need: 'För att nå det senast {date}: <b>{amt} {every}</b>.',
        tooSoon: 'Datumet är för nära – välj ett datum minst en period senare.',
        noPer: 'Fyll i beloppet som läggs undan för att se datumet.', done: 'Snyggt – målet är redan nått!', rest: 'Det fattas {amt}.' },
      cta: 'I Tirelire fylls målringen på för varje veckopeng och varje godkänd syssla, och den visar beräknat datum i barnets takt.',
      faq: [
        ['Hur räknar man ut hur lång tid ett sparmål tar?', 'Ta det som fattas (priset minus det som redan är sparat), dela med beloppet som sparas varje period och avrunda uppåt. Exempel: 600 kr kvar med 50 kr i veckan = 12 veckor.'],
        ['Ska barn spara varje vecka eller varje månad?', 'För de yngsta gör veckosparande målet mer konkret – de ser spargrisen växa oftare. Tonåringar klarar ofta en månadsrytm bättre. Kalkylatorn räknar på båda.'],
        ['Hur kan barnet nå målet snabbare?', 'Små betalda sysslor utöver veckopengen, eller en del av födelsedagspengarna undanlagd. Visa barnet hur långt det har kommit: det motiverar att se målet komma närmare.'],
        ['Sparas mina siffror?', 'Nej. Allt räknas ut i din webbläsare; inget sparas eller skickas.']
      ]
    },
    fi: {
      slug: 'saastolaskuri-lapselle', cur: 'EUR',
      title: 'Säästölaskuri lapselle – viikkoraha ja säästötavoite',
      desc: 'Montako viikkoa, ennen kuin lapsi saa pyörän viikkorahoillaan? Syötä hinta, mitä säästöpossussa jo on ja paljonko säästetään viikossa tai kuukaudessa.',
      h1: 'Säästölaskuri lapselle',
      lead: 'Säästääkö lapsesi pyörään, peliin tai retkeen? Syötä hinta, mitä lapsella jo on ja paljonko hän laittaa sivuun – näet, milloin tavoite täyttyy ja paljonko pitää säästää, jotta se täyttyy tiettyyn päivään mennessä.',
      f: { goal: 'Tavoitteen hinta', saved: 'Jo säästöpossussa', freq: 'Kuinka usein', w: 'Joka viikko', m: 'Joka kuukausi', per: 'Säästettävä summa', end: 'Tavoite täytettävä viimeistään (valinnainen)', go: 'Laske' },
      t: { w: 'viikon', ws: 'viikon', m: 'kuukauden', ms: 'kuukauden', ew: 'viikossa', em: 'kuukaudessa',
        reach: 'Säästämällä {per} {every} tavoite täyttyy <b>{n} {units}</b> kuluttua, noin <b>{date}</b>.',
        need: 'Jotta tavoite täyttyy {date} mennessä: <b>{amt} {every}</b>.',
        tooSoon: 'Päivä on liian lähellä – valitse vähintään yhtä jaksoa myöhäisempi päivä.',
        noPer: 'Syötä säästettävä summa, niin näet päivän.', done: 'Hienoa – tavoite on jo täynnä!', rest: 'Puuttuu vielä {amt}.' },
      cta: 'Tirelire-sovelluksessa tavoitteen rengas täyttyy jokaisesta viikkorahasta ja hyväksytystä kotityöstä, ja se näyttää arvioidun päivän lapsen omassa tahdissa.',
      faq: [
        ['Miten lasken, kauanko säästötavoitteeseen menee?', 'Ota puuttuva summa (hinta miinus jo säästetty), jaa se kunkin jakson säästösummalla ja pyöristä ylöspäin. Esimerkki: 60 € puuttuu ja säästö on 5 € viikossa = 12 viikkoa.'],
        ['Kannattaako lapsen säästää viikoittain vai kuukausittain?', 'Pienille viikkorytmi tekee tavoitteesta konkreettisen – säästöpossu kasvaa useammin. Teini-ikäiset pärjäävät usein paremmin kuukausirytmillä. Laskuri laskee molemmat.'],
        ['Miten lapsi pääsee tavoitteeseen nopeammin?', 'Pieniä palkallisia kotitöitä viikkorahan lisäksi tai osa syntymäpäivärahoista sivuun. Näytä lapselle, missä hän menee: tavoitteen lähestyminen motivoi.'],
        ['Tallennetaanko lukuni?', 'Ei. Kaikki lasketaan selaimessasi; mitään ei tallenneta eikä lähetetä.']
      ]
    }
  },

  // ---------------------------------------------------------------- Vaktplan
  vaktplan: {
    nb: {
      slug: 'turnuskalkulator', off: 'F',
      title: 'Turnuskalkulator – se turnusen i kalender med ukenummer',
      desc: 'Skriv inn turnusen (f.eks. 2-2-3), velg startdato og se hvilken vakt du har hver dag, med ukenummer, antall vakter og gjennomsnittlig arbeidstid per uke.',
      h1: 'Turnuskalkulator',
      lead: 'Legg inn rotasjonen én gang og se vaktene uke for uke. Bruk D for dag, K for kveld, N for natt og F for fri – eller egne bokstaver.',
      f: { preset: 'Ferdig mal', choose: 'Velg en mal …', pattern: 'Turnus (én bokstav per dag, med mellomrom)', start: 'Første dag i turnusen', weeks: 'Antall uker som vises', hours: 'Timer per vakt', go: 'Vis turnus' },
      presets: [['2-2-3 (Panama)', 'D D F F D D D F F D D F F F'], ['4 på, 4 av', 'D D D D F F F F'], ['Dag, mandag–fredag', 'D D D D D F F'], ['Dag–kveld–natt (2-2-2-4)', 'D D K K N N F F F F'], ['Kveld og helg hver 3. uke', 'D D D D D F F D D D D D F F K K K F F K K']],
      t: { off: 'F', week: 'Uke', caption: 'Turnus per uke', empty: 'Skriv inn turnusen og en startdato.',
        summary: 'Turnusen går over {len} dager. På {days} dager har du <b>{work} vakter</b> og {hours} timer – i snitt <b>{avg} timer per uke</b>.' },
      cta: 'I Vaktplan legger du inn turnus på 1–8 uker opptil to år frem og ser timene fordelt på kveld, natt, helg og helligdag.',
      faq: [
        ['Hva er en 2-2-3-turnus?', 'Også kalt Panama-turnus: 2 dager på, 2 av, 3 på, 2 av, 2 på og 3 av. Den går over 14 dager, og du jobber annenhver helg.'],
        ['Hvordan regner jeg ut gjennomsnittlig arbeidstid i en turnus?', 'Legg sammen timene for hele turnusperioden og del på antall uker. Eksempel: 7 vakter à 12 timer på 14 dager = 84 timer / 2 uker = 42 timer per uke. Kalkulatoren gjør dette for perioden som vises.'],
        ['Kan jeg se hvilken vakt jeg har på en bestemt dato?', 'Ja. Øk antall uker (opptil 104) og finn datoen i tabellen. Ukenummeret står i første kolonne.'],
        ['Kan jeg bruke egne vakttyper?', 'Ja. Alle bokstaver eller korte koder fungerer, for eksempel L for langvakt eller H for hjemmevakt. Bare F regnes som fri.'],
        ['Blir turnusen min lagret?', 'Nei. Alt regnes ut i nettleseren din og sendes ingen steder.']
      ]
    },
    sv: {
      slug: 'skiftschema-kalkylator', off: 'L',
      title: 'Skiftschema-kalkylator – rullande schema i kalender',
      desc: 'Skriv in ditt rullande schema (t.ex. 2-2-3), välj startdag och se vilket pass du har varje dag, med veckonummer, antal pass och snittid per vecka.',
      h1: 'Skiftschema-kalkylator',
      lead: 'Skriv in ditt rullande schema en gång och se passen vecka för vecka. Använd D för dag, K för kväll, N för natt och L för ledig – eller egna bokstäver.',
      f: { preset: 'Färdig mall', choose: 'Välj en mall …', pattern: 'Schema (en bokstav per dag, med mellanslag)', start: 'Första dagen i schemat', weeks: 'Antal veckor som visas', hours: 'Timmar per pass', go: 'Visa schema' },
      presets: [['2-2-3 (Panama)', 'D D L L D D D L L D D L L L'], ['4 på, 4 av', 'D D D D L L L L'], ['Dag, måndag–fredag', 'D D D D D L L'], ['Treskift (2-2-2-4)', 'D D K K N N L L L L'], ['Kväll och helg var 3:e vecka', 'D D D D D L L D D D D D L L K K K L L K K']],
      t: { off: 'L', week: 'V.', caption: 'Schema per vecka', empty: 'Skriv in schemat och en startdag.',
        summary: 'Schemat rullar över {len} dagar. På {days} dagar har du <b>{work} pass</b> och {hours} timmar – i snitt <b>{avg} timmar per vecka</b>.' },
      cta: 'I Vaktplan lägger du in ett rullande schema på 1–8 veckor upp till två år framåt och ser timmarna fördelade på kväll, natt, helg och helgdag.',
      faq: [
        ['Vad är ett 2-2-3-schema?', 'Kallas också Panama-schema: 2 dagar på, 2 lediga, 3 på, 2 lediga, 2 på och 3 lediga. Det rullar över 14 dagar och du jobbar varannan helg.'],
        ['Hur räknar jag ut snittiden per vecka i ett rullande schema?', 'Summera timmarna för hela schemaperioden och dela med antalet veckor. Exempel: 7 pass à 12 timmar på 14 dagar = 84 timmar / 2 veckor = 42 timmar per vecka. Kalkylatorn gör det för perioden som visas.'],
        ['Kan jag se vilket pass jag har ett visst datum?', 'Ja. Öka antalet veckor (upp till 104) och leta upp datumet i tabellen. Veckonumret står i första kolumnen.'],
        ['Kan jag använda egna passtyper?', 'Ja. Alla bokstäver eller korta koder fungerar, till exempel B för beredskap. Bara L räknas som ledig.'],
        ['Sparas mitt schema?', 'Nej. Allt räknas ut i din webbläsare och skickas ingenstans.']
      ]
    }
  },

  // ---------------------------------------------------------------- GLP-1
  glp1: {
    en: {
      slug: 'glp-1-injection-calendar',
      title: 'GLP-1 Injection Calendar – your prescribed schedule on dates',
      desc: 'Type in the schedule your doctor gave you and see every injection date for a weekly or daily GLP-1 medicine. No dose advice – a calendar only.',
      h1: 'GLP-1 injection calendar',
      warn: '<b>This is not medical advice.</b> This calendar gives no dose recommendations. It only shows the schedule you type in as dates. Always follow your doctor’s or pharmacist’s instructions and talk to them before changing anything.',
      lead: 'Enter the date of your first injection and each step of the schedule on your prescription – the dose exactly as your doctor wrote it and how many injections at that dose. The calendar lists every date.',
      f: { start: 'First injection', every: 'How often', weekly: 'Once a week', daily: 'Once a day', label: 'Dose (as written on your prescription)', count: 'Number of injections at this dose', add: 'Add a step', del: 'Remove this step', go: 'Show calendar' },
      t: { step: 'Step', empty: 'Enter a start date and at least one step.', summary: '{n} injections from {first} to {last}.', next: 'Next injection: {date} – {label}', date: 'Date', dose: 'Dose (as you entered it)', caption: 'Injection dates', print: 'Print or save as PDF' },
      cta: 'GLP-1 Diary reminds you on your injection day, helps you rotate injection sites and makes a PDF report for your doctor.',
      faq: [
        ['Does this tool tell me which dose to take?', 'No. It gives no dose, titration or missed-dose advice. It only puts the schedule you type in onto dates. Your doctor or pharmacist decides your dose.'],
        ['Which medicines can I use it with?', 'Any weekly or daily injection your doctor prescribed, for example Wegovy®, Ozempic®, Mounjaro®, Saxenda®, Trulicity® or Victoza®. Not affiliated with any manufacturer; trademarks belong to their owners.'],
        ['What if I missed an injection?', 'Read the patient information leaflet and ask your doctor or pharmacist. This calendar cannot advise on missed doses.'],
        ['Is my information saved or sent?', 'No. Everything is calculated in your browser; nothing is stored or sent.']
      ]
    },
    de: {
      slug: 'glp-1-spritzenkalender',
      title: 'GLP-1 Spritzenkalender – dein verordneter Plan als Termine',
      desc: 'Gib den Plan aus deiner Verordnung ein und sieh jeden Injektionstermin für ein wöchentliches oder tägliches GLP-1-Medikament. Keine Dosisempfehlung – nur ein Kalender.',
      h1: 'GLP-1 Spritzenkalender',
      warn: '<b>Keine medizinische Beratung.</b> Dieser Kalender gibt keine Dosisempfehlungen. Er zeigt nur den Plan, den du eingibst, als Termine. Halte dich immer an die Anweisungen deiner Ärztin, deines Arztes oder deiner Apotheke und sprich mit ihnen, bevor du etwas änderst.',
      lead: 'Gib das Datum deiner ersten Injektion ein und jede Stufe aus deiner Verordnung – die Dosis genau so, wie sie verordnet wurde, und wie viele Injektionen mit dieser Dosis. Der Kalender listet jeden Termin auf.',
      f: { start: 'Erste Injektion', every: 'Wie oft', weekly: 'Einmal pro Woche', daily: 'Einmal täglich', label: 'Dosis (wie in deiner Verordnung)', count: 'Anzahl Injektionen mit dieser Dosis', add: 'Stufe hinzufügen', del: 'Diese Stufe entfernen', go: 'Kalender anzeigen' },
      t: { step: 'Stufe', empty: 'Gib ein Startdatum und mindestens eine Stufe ein.', summary: '{n} Injektionen vom {first} bis zum {last}.', next: 'Nächste Injektion: {date} – {label}', date: 'Datum', dose: 'Dosis (wie eingegeben)', caption: 'Injektionstermine', print: 'Drucken oder als PDF sichern' },
      cta: 'GLP-1 Tagebuch erinnert dich an deinem Spritzentag, hilft beim Wechseln der Einstichstellen und erstellt einen PDF-Bericht für deine Arztpraxis.',
      faq: [
        ['Sagt mir dieses Tool, welche Dosis ich nehmen soll?', 'Nein. Es gibt keine Empfehlungen zu Dosis, Dosissteigerung oder vergessenen Injektionen. Es zeigt nur den Plan, den du eingibst, als Termine. Über deine Dosis entscheiden deine Ärztin, dein Arzt oder deine Apotheke.'],
        ['Mit welchen Medikamenten kann ich es nutzen?', 'Mit jeder wöchentlichen oder täglichen Injektion, die dir verordnet wurde, zum Beispiel Wegovy®, Ozempic®, Mounjaro®, Saxenda®, Trulicity® oder Victoza®. Keine Verbindung zu einem Hersteller; Marken gehören ihren Inhabern.'],
        ['Was, wenn ich eine Injektion vergessen habe?', 'Lies die Packungsbeilage und frag deine Ärztin, deinen Arzt oder deine Apotheke. Dieser Kalender kann dazu nicht beraten.'],
        ['Werden meine Angaben gespeichert oder gesendet?', 'Nein. Alles wird in deinem Browser berechnet; nichts wird gespeichert oder gesendet.']
      ]
    },
    fr: {
      slug: 'calendrier-injections-glp-1',
      title: 'Calendrier des injections GLP-1 – votre schéma prescrit en dates',
      desc: "Saisissez le schéma donné par votre médecin et voyez chaque date d'injection d'un traitement GLP-1 hebdomadaire ou quotidien. Aucun conseil de dose : un calendrier seulement.",
      h1: 'Calendrier des injections GLP-1',
      warn: "<b>Ceci n'est pas un avis médical.</b> Ce calendrier ne recommande aucune dose. Il affiche seulement en dates le schéma que vous saisissez. Suivez toujours les instructions de votre médecin ou de votre pharmacien et parlez-leur avant de changer quoi que ce soit.",
      lead: "Indiquez la date de votre première injection et chaque palier de votre ordonnance : la dose telle que votre médecin l'a écrite et le nombre d'injections à cette dose. Le calendrier liste chaque date.",
      f: { start: 'Première injection', every: 'Fréquence', weekly: 'Une fois par semaine', daily: 'Une fois par jour', label: 'Dose (telle que sur votre ordonnance)', count: "Nombre d'injections à cette dose", add: 'Ajouter un palier', del: 'Supprimer ce palier', go: 'Afficher le calendrier' },
      t: { step: 'Palier', empty: 'Indiquez une date de début et au moins un palier.', summary: '{n} injections du {first} au {last}.', next: 'Prochaine injection : {date} – {label}', date: 'Date', dose: 'Dose (telle que saisie)', caption: "Dates d'injection", print: 'Imprimer ou enregistrer en PDF' },
      cta: "Journal GLP-1 vous rappelle votre jour d'injection, vous aide à alterner les sites d'injection et crée un rapport PDF pour votre médecin.",
      faq: [
        ['Cet outil me dit-il quelle dose prendre ?', "Non. Il ne donne aucun conseil de dose, de palier ni d'oubli. Il place seulement en dates le schéma que vous saisissez. C'est votre médecin ou votre pharmacien qui décide de la dose."],
        ['Avec quels médicaments puis-je l’utiliser ?', 'Avec toute injection hebdomadaire ou quotidienne prescrite par votre médecin, par exemple Wegovy®, Ozempic®, Mounjaro®, Saxenda®, Trulicity® ou Victoza®. Sans lien avec un fabricant ; les marques appartiennent à leurs propriétaires.'],
        ["Et si j'ai oublié une injection ?", 'Lisez la notice et demandez à votre médecin ou à votre pharmacien. Ce calendrier ne peut pas conseiller sur les oublis.'],
        ['Mes informations sont-elles enregistrées ou envoyées ?', "Non. Tout est calculé dans votre navigateur ; rien n'est enregistré ni envoyé."]
      ]
    },
    nl: {
      slug: 'glp-1-injectiekalender',
      title: 'GLP-1 injectiekalender – je voorgeschreven schema in datums',
      desc: 'Vul het schema van je arts in en zie elke injectiedatum voor een wekelijks of dagelijks GLP-1-middel. Geen doseringsadvies – alleen een kalender.',
      h1: 'GLP-1 injectiekalender',
      warn: '<b>Dit is geen medisch advies.</b> Deze kalender geeft geen doseringsadvies. Hij zet alleen het schema dat je invult om in datums. Volg altijd de instructies van je arts of apotheker en overleg met hen voordat je iets verandert.',
      lead: 'Vul de datum van je eerste injectie in en elke stap van je voorschrift: de dosis precies zoals je arts die heeft opgeschreven en hoeveel injecties met die dosis. De kalender toont elke datum.',
      f: { start: 'Eerste injectie', every: 'Hoe vaak', weekly: 'Eén keer per week', daily: 'Eén keer per dag', label: 'Dosis (zoals op je voorschrift)', count: 'Aantal injecties met deze dosis', add: 'Stap toevoegen', del: 'Deze stap verwijderen', go: 'Kalender tonen' },
      t: { step: 'Stap', empty: 'Vul een startdatum en minstens één stap in.', summary: '{n} injecties van {first} tot {last}.', next: 'Volgende injectie: {date} – {label}', date: 'Datum', dose: 'Dosis (zoals ingevuld)', caption: 'Injectiedatums', print: 'Afdrukken of als pdf bewaren' },
      cta: 'GLP-1 dagboek herinnert je op je injectiedag, helpt je injectieplekken af te wisselen en maakt een pdf-rapport voor je arts.',
      faq: [
        ['Vertelt deze tool welke dosis ik moet nemen?', 'Nee. Hij geeft geen advies over dosis, opbouw of een vergeten injectie. Hij zet alleen het schema dat je invult om in datums. Je arts of apotheker bepaalt je dosis.'],
        ['Met welke middelen kan ik hem gebruiken?', 'Met elke wekelijkse of dagelijkse injectie die je arts heeft voorgeschreven, bijvoorbeeld Wegovy®, Ozempic®, Mounjaro®, Saxenda®, Trulicity® of Victoza®. Niet verbonden aan een fabrikant; merken zijn van hun eigenaars.'],
        ['Wat als ik een injectie ben vergeten?', 'Lees de bijsluiter en vraag het je arts of apotheker. Deze kalender kan daar geen advies over geven.'],
        ['Worden mijn gegevens opgeslagen of verstuurd?', 'Nee. Alles wordt in je browser berekend; er wordt niets opgeslagen of verstuurd.']
      ]
    },
    sv: {
      slug: 'glp-1-injektionskalender',
      title: 'GLP-1 injektionskalender – ditt ordinerade schema som datum',
      desc: 'Skriv in schemat du fått av din läkare och se varje injektionsdatum för ett GLP-1-läkemedel varje vecka eller dag. Inga dosråd – bara en kalender.',
      h1: 'GLP-1 injektionskalender',
      warn: '<b>Detta är inte medicinsk rådgivning.</b> Kalendern ger inga dosrekommendationer. Den visar bara schemat du skriver in som datum. Följ alltid din läkares eller farmaceuts instruktioner och prata med dem innan du ändrar något.',
      lead: 'Fyll i datumet för din första injektion och varje steg i din ordination: dosen exakt som din läkare skrev den och hur många injektioner med den dosen. Kalendern listar varje datum.',
      f: { start: 'Första injektionen', every: 'Hur ofta', weekly: 'En gång i veckan', daily: 'En gång om dagen', label: 'Dos (som på din ordination)', count: 'Antal injektioner med denna dos', add: 'Lägg till ett steg', del: 'Ta bort steget', go: 'Visa kalender' },
      t: { step: 'Steg', empty: 'Fyll i ett startdatum och minst ett steg.', summary: '{n} injektioner från {first} till {last}.', next: 'Nästa injektion: {date} – {label}', date: 'Datum', dose: 'Dos (som du skrev in)', caption: 'Injektionsdatum', print: 'Skriv ut eller spara som PDF' },
      cta: 'GLP-1 dagbok påminner dig på injektionsdagen, hjälper dig att växla injektionsställe och gör en PDF-rapport till din läkare.',
      faq: [
        ['Säger verktyget vilken dos jag ska ta?', 'Nej. Det ger inga råd om dos, upptrappning eller missad dos. Det lägger bara schemat du skriver in på datum. Din läkare eller farmaceut bestämmer dosen.'],
        ['Vilka läkemedel kan jag använda det med?', 'Alla injektioner varje vecka eller dag som din läkare ordinerat, till exempel Wegovy®, Ozempic®, Mounjaro®, Saxenda®, Trulicity® eller Victoza®. Ingen koppling till någon tillverkare; varumärkena tillhör sina ägare.'],
        ['Vad gör jag om jag missat en injektion?', 'Läs bipacksedeln och fråga din läkare eller farmaceut. Kalendern kan inte ge råd om missade doser.'],
        ['Sparas eller skickas mina uppgifter?', 'Nej. Allt räknas ut i din webbläsare; inget sparas eller skickas.']
      ]
    }
  },

  // ---------------------------------------------------------------- Falcı
  falci: {
    en: {
      slug: 'daily-horoscope', fmtLang: 'en-GB',
      title: 'Daily Horoscope Today – all 12 zodiac signs',
      desc: "Today's horoscope for all 12 signs, matched to where the Moon is and its phase. Love, work and wellbeing for today, yesterday and tomorrow.",
      h1: 'Daily horoscope',
      lead: "Today's reading for every sign, with the real position of the Moon and its phase for the day. Pick your sign for love, work, wellbeing and your lucky number.",
      signTitle: '{sign} Horoscope Today – love, work and lucky number',
      signDesc: '{sign} daily horoscope ({dates}): love, work, wellbeing, lucky number and colour, matched to today’s Moon sign and phase.',
      signH1: '{sign} horoscope today', more: 'Read the full {sign} horoscope', others: 'Other signs', all: 'All signs',
      note: 'For entertainment. Not medical, legal or financial advice.',
      cta: 'Want a reading that is about you? Falci reads your coffee cup, your tarot spread and your full birth chart.',
      faq: [
        ['Is the daily horoscope based on the real sky?', 'The Moon part is: its sign and phase are calculated for each day. The texts are written in advance and matched to the day and to your sign. For entertainment.'],
        ['When does the horoscope change?', 'At midnight in your own time zone. You can also look at yesterday and tomorrow.'],
        ['How do I get a personal reading?', 'In the Falci app you can get readings based on your full birth chart, a coffee cup photo or a tarot spread.']
      ],
      signFaq: [
        ['What are the dates for {sign}?', '{sign}: {dates}. The exact switch day can move by one day depending on the year.'],
        ['Is the {sign} horoscope the same every day?', 'No. Each day uses where the Moon is and its phase, and the texts change daily.']
      ],
      p: {
        lang: 'en', days: ['Yesterday', 'Today', 'Tomorrow'],
        signs: ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'],
        phases: ['new moon', 'waxing crescent', 'first quarter', 'waxing gibbous', 'full moon', 'waning gibbous', 'last quarter', 'waning crescent'],
        moonIn: 'The Moon is in {moon} ({phase}).',
        h: { love: 'Love', work: 'Work and money', mood: 'Wellbeing', advice: 'Tip of the day', number: 'Lucky number', color: 'Lucky colour' },
        aspects: [
          ['With the Moon in your own sign, your feelings are close to the surface – trust your first instinct.', 'The Moon passing through your sign puts you in the spotlight; people notice your mood, so lead with warmth.', 'A good day to start something small that is just for you.'],
          ['It sits in a sign that flows easily with yours, so things fall into place with less effort.', 'A harmonious angle to your sign makes conversations smoother than usual.', 'The sky is on your side today; say yes to an invitation.'],
          ['A friendly angle to your sign opens a small door – look for it in an everyday conversation.', 'Opportunities come through people you already know.', 'A light, helpful sky: a short message can lead somewhere.'],
          ['It makes a tense angle to your sign, so slow down before reacting.', 'Some friction is possible; pick your battles and keep plans flexible.', 'A challenging angle pushes you to fix something you have been avoiding.'],
          ['It sits opposite your sign, so other people’s needs pull at you – look for the balance.', 'Relationships are your mirror today; listen more than you speak.', 'The opposite sign lights up partnerships: a talk you have put off goes better now.'],
          ['It makes no strong angle to your sign, so you can set your own pace.', 'A quieter sky for you – good for routine and catching up.', 'Little outside pressure today; use it to plan the week.']
        ],
        elements: [
          ['Your fire wants action, so put it into one clear goal.', 'Your energy is high; move your body before big decisions.', 'Your courage is an asset – just finish what you start.'],
          ['Your practical side shines; small, steady steps pay off.', 'Take care of money and home matters first.', 'Patience is your strength today; do not rush the result.'],
          ['Your mind is quick; write ideas down before they fly away.', 'A good day for learning, messages and short trips.', 'Talk it through – a conversation clears the air.'],
          ['Your intuition is strong; listen to your gut.', 'Protect your energy and choose who you share it with.', 'Feelings run deep; a quiet evening restores you.']
        ],
        love: ['Small gestures count more than big words today.', 'If you are single, someone from your wider circle may catch your eye.', 'Say clearly what you need; your partner cannot read minds.', 'An old memory comes back – let it go gently.', 'Plan something simple together, like a walk or a meal.', 'Flirting comes easily; keep it light.', 'Give space when it is asked for; closeness returns.', 'A kind message to someone you care about lands well.'],
        work: ['Finish one open task before starting a new one.', 'A colleague’s idea is worth hearing out.', 'Check the details twice, especially numbers and dates.', 'A good day to ask for feedback.', 'Hold off on big purchases; compare first.', 'Your work gets noticed when you share your progress.', 'Clear your inbox and the afternoon will feel lighter.', 'A new skill you practise today pays off later.'],
        mood: ['Drink water and get some daylight.', 'Sleep matters more than usual tonight.', 'A short walk resets your mood.', 'Make room for a hobby, even for twenty minutes.', 'Do not take on other people’s stress.', 'Stretch your back and shoulders between tasks.', 'Laughing with a friend does you good today.', 'Eat slowly and enjoy it.'],
        advice: ['Keep it simple.', 'Say no to one thing so you can say yes to another.', 'Trust the timing.', 'Ask, do not assume.', 'Start before you feel ready.', 'Be kind to yourself first.', 'Leave room for surprises.', 'One step at a time.'],
        colors: ['red', 'gold', 'green', 'blue', 'purple', 'white', 'silver', 'orange', 'turquoise', 'pink']
      }
    },
    ar: {
      slug: 'abraj-alyawm', fmtLang: 'ar-u-ca-gregory', dir: 'rtl',
      title: 'حظك اليوم – الأبراج اليومية لكل الأبراج الاثني عشر',
      desc: 'حظك اليوم لكل الأبراج الاثني عشر، مرتبط بموقع القمر الحقيقي وطوره. الحب والعمل والصحة النفسية لليوم والأمس والغد.',
      h1: 'حظك اليوم',
      lead: 'قراءة اليوم لكل برج، مع موقع القمر الحقيقي وطوره في هذا اليوم. اختر برجك لتقرأ عن الحب والعمل والراحة ورقم حظك.',
      signTitle: 'برج {sign} اليوم – حظك في الحب والعمل ورقم الحظ',
      signDesc: 'حظك اليوم لبرج {sign} ({dates}): الحب والعمل والراحة ورقم الحظ ولونه، مرتبط ببرج القمر وطوره اليوم.',
      signH1: 'برج {sign} اليوم', more: 'اقرأ حظ برج {sign} كاملًا', others: 'أبراج أخرى', all: 'كل الأبراج',
      note: 'للترفيه فقط. ليست نصيحة طبية أو قانونية أو مالية.',
      cta: 'تريد قراءة تخصّك أنت؟ تطبيق Falci يقرأ فنجان قهوتك وأوراق التاروت وخريطتك الفلكية كاملة.',
      faq: [
        ['هل حظك اليوم مبني على السماء الحقيقية؟', 'جزء القمر نعم: برجه وطوره يُحسبان لكل يوم. النصوص مكتوبة مسبقًا وتُطابَق مع اليوم ومع برجك. للترفيه فقط.'],
        ['متى يتغيّر حظ اليوم؟', 'عند منتصف الليل حسب توقيتك. يمكنك أيضًا قراءة حظ الأمس والغد.'],
        ['كيف أحصل على قراءة شخصية؟', 'في تطبيق Falci تحصل على قراءات مبنية على خريطتك الفلكية كاملة أو صورة فنجان قهوتك أو فرد أوراق التاروت.']
      ],
      signFaq: [
        ['ما تواريخ برج {sign}؟', 'برج {sign}: {dates}. قد يتغيّر يوم الانتقال يومًا واحدًا حسب السنة.'],
        ['هل حظ برج {sign} نفسه كل يوم؟', 'لا. كل يوم يعتمد على موقع القمر وطوره، والنصوص تتغيّر يوميًا.']
      ],
      p: {
        lang: 'ar', days: ['أمس', 'اليوم', 'غدًا'],
        signs: ['الحمل', 'الثور', 'الجوزاء', 'السرطان', 'الأسد', 'العذراء', 'الميزان', 'العقرب', 'القوس', 'الجدي', 'الدلو', 'الحوت'],
        phases: ['محاق', 'هلال متزايد', 'تربيع أول', 'أحدب متزايد', 'بدر', 'أحدب متناقص', 'تربيع أخير', 'هلال متناقص'],
        moonIn: 'القمر في برج {moon} ({phase}).',
        h: { love: 'الحب', work: 'العمل والمال', mood: 'الراحة', advice: 'نصيحة اليوم', number: 'رقم الحظ', color: 'لون الحظ' },
        aspects: [
          ['القمر في برجك، فمشاعرك قريبة من السطح؛ ثق بإحساسك الأول.', 'مرور القمر في برجك يضعك تحت الأضواء؛ الناس يلاحظون مزاجك، فابدأ بالدفء.', 'يوم مناسب لتبدأ شيئًا صغيرًا لنفسك فقط.'],
          ['القمر في برج منسجم مع برجك، فتسير الأمور بجهد أقل.', 'زاوية متناغمة مع برجك تجعل الحديث أسهل من المعتاد.', 'السماء في صفّك اليوم؛ اقبل الدعوة.'],
          ['زاوية ودّية مع برجك تفتح بابًا صغيرًا؛ ابحث عنه في حديث عادي.', 'الفرص تأتي عن طريق أشخاص تعرفهم بالفعل.', 'سماء خفيفة ومساعِدة: رسالة قصيرة قد تقودك إلى شيء جميل.'],
          ['القمر في زاوية متوترة مع برجك، فتمهّل قبل أن تردّ.', 'قد يحدث بعض الاحتكاك؛ اختر معاركك واجعل خططك مرنة.', 'زاوية صعبة تدفعك لإصلاح أمر كنت تؤجّله.'],
          ['القمر في البرج المقابل لبرجك، فاحتياجات الآخرين تشدّك؛ ابحث عن التوازن.', 'العلاقات مرآتك اليوم؛ استمع أكثر مما تتكلم.', 'البرج المقابل يضيء الشراكات: حديث أجّلته سيكون أسهل الآن.'],
          ['لا زاوية قوية بين القمر وبرجك، فأنت حر في اختيار إيقاعك.', 'سماء أهدأ لك؛ مناسبة للروتين وإنهاء المتأخر.', 'ضغط خارجي قليل اليوم؛ استغلّه لتخطيط الأسبوع.']
        ],
        elements: [
          ['نارك تريد الحركة، فضعها في هدف واحد واضح.', 'طاقتك عالية؛ حرّك جسمك قبل القرارات الكبيرة.', 'شجاعتك نقطة قوة؛ فقط أكمل ما تبدأه.'],
          ['جانبك العملي يلمع؛ الخطوات الصغيرة الثابتة تؤتي ثمارها.', 'اهتم بأمور المال والبيت أولًا.', 'الصبر قوتك اليوم؛ لا تستعجل النتيجة.'],
          ['ذهنك سريع؛ اكتب أفكارك قبل أن تطير.', 'يوم جيد للتعلّم والرسائل والمشاوير القصيرة.', 'تكلّم بصراحة؛ الحديث يصفّي الأجواء.'],
          ['حدسك قوي؛ استمع لإحساسك.', 'احمِ طاقتك واختر مع من تشاركها.', 'مشاعرك عميقة؛ أمسية هادئة تعيد إليك توازنك.']
        ],
        love: ['اللفتات الصغيرة أهم من الكلمات الكبيرة اليوم.', 'إن كنت أعزب، قد يلفت انتباهك شخص من دائرة معارفك.', 'قل بوضوح ما تحتاجه؛ شريكك لا يقرأ الأفكار.', 'ذكرى قديمة تعود؛ دعها تمضي بلطف.', 'خطّطا لشيء بسيط معًا، مثل نزهة أو وجبة.', 'الغزل يأتيك بسهولة؛ اجعله خفيفًا.', 'امنح المساحة حين تُطلب؛ القرب سيعود.', 'رسالة لطيفة لشخص تحبه ستصل إلى قلبه.'],
        work: ['أنهِ مهمة مفتوحة قبل أن تبدأ أخرى.', 'فكرة زميل تستحق الاستماع.', 'راجع التفاصيل مرتين، خاصة الأرقام والتواريخ.', 'يوم مناسب لطلب رأي الآخرين في عملك.', 'أجّل المشتريات الكبيرة وقارن أولًا.', 'عملك يُلاحَظ حين تشارك تقدّمك.', 'رتّب بريدك وسيكون المساء أخف.', 'مهارة جديدة تتدرّب عليها اليوم ستفيدك لاحقًا.'],
        mood: ['اشرب الماء وتعرّض لضوء النهار.', 'النوم أهم من المعتاد الليلة.', 'مشية قصيرة تعيد ضبط مزاجك.', 'خصّص وقتًا لهواية، ولو عشرين دقيقة.', 'لا تحمل توتر الآخرين على كتفيك.', 'مدّد ظهرك وكتفيك بين المهام.', 'الضحك مع صديق يفيدك اليوم.', 'كُل ببطء واستمتع.'],
        advice: ['اجعلها بسيطة.', 'قل لا لشيء واحد لتقول نعم لآخر.', 'ثق بالتوقيت.', 'اسأل ولا تفترض.', 'ابدأ قبل أن تشعر أنك جاهز تمامًا.', 'كن لطيفًا مع نفسك أولًا.', 'اترك مكانًا للمفاجآت.', 'خطوة بخطوة.'],
        colors: ['الأحمر', 'الذهبي', 'الأخضر', 'الأزرق', 'البنفسجي', 'الأبيض', 'الفضي', 'البرتقالي', 'الفيروزي', 'الوردي']
      }
    }
  }
};
