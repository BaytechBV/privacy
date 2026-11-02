// node araclar/build.js — writes the web tools to /<lang>/<slug>/index.html and lists their URLs in araclar/urls.txt.
// Texts: araclar/metin.js. Logic: araclar/<tool>.js (checked by araclar/test.js). Sitemap is not touched.
const fs = require('fs'), path = require('path');
const BASE = process.env.SITE_BASE || 'https://apps.baytech.nl'; // domain switch = this line
const ROOT = path.join(__dirname, '..');
global.D = require('./ortak.js');
const Burc = require('./falci.js'), M = require('./metin.js');
const slugs = require('../landing/slugs.json'), apps = require('../landing/apps.json');

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const json = o => JSON.stringify(o).replace(/</g, '\\u003c');
const src = f => fs.readFileSync(path.join(__dirname, f), 'utf8');
const NAME = { fr: 'Français', en: 'English', da: 'Dansk', nb: 'Norsk', sv: 'Svenska', fi: 'Suomi', de: 'Deutsch', nl: 'Nederlands', ar: 'العربية' };
const LOCALE = { fr: 'fr-FR', en: 'en-GB', da: 'da', nb: 'no', sv: 'sv', fi: 'fi', de: 'de-DE', nl: 'nl-NL' };
const icon = u => u.replace('512x512bb', '128x128bb');
const APP = {
  tirelire: { key: 'tirelire', cat: 'FinanceApplication' },
  vaktplan: { key: 'vaktplan-nordic', cat: 'BusinessApplication' },
  glp1: { key: 'glp1-companion-eu', cat: 'HealthApplication' },
  falci: { id: '685867301', cat: 'LifestyleApplication', name: { en: 'Falci: Coffee Cup Reading', ar: 'Falci' },
    icon: 'https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/cc/f8/15/ccf815d9-8c43-17ee-7ec1-e9042fc34e81/AppIcon-0-0-1x_U007epad-0-1-85-220.png/128x128bb.jpg' }
};
for (const a of Object.values(APP)) if (a.key) Object.assign(a, { id: apps[a.key].id, icon: icon(apps[a.key].icon) });
const appName = (tool, lang) => APP[tool].name ? APP[tool].name[lang] : apps[APP[tool].key].locales[LOCALE[lang]].name;

const CSS = `:root{--bg:#fff;--fg:#1c1c1e;--mu:#6b6b70;--ac:#0a66c2;--acfg:#fff;--card:#f4f4f6;--line:rgba(128,128,128,.35);--wbg:#fdecea;--wfg:#5c1710;--wb:#c0392b}
@media (prefers-color-scheme:dark){:root{--bg:#111;--fg:#eee;--mu:#9a9aa0;--ac:#5aa9ff;--acfg:#0b1a2e;--card:#1d1d20;--wbg:#3a1512;--wfg:#ffd9d4;--wb:#ff7b6b}}
[hidden]{display:none!important}*{box-sizing:border-box}body{background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:760px;margin:0 auto;padding:20px 16px 40px;overflow-wrap:anywhere}
a{color:var(--ac)}h1{font-size:1.75em;line-height:1.2;margin:.1em 0 .3em}.lead{font-size:1.1em;color:var(--mu)}h2{font-size:1.25em;margin-top:1.8em}h3{font-size:1.05em;margin:1.2em 0 .2em}
form{display:grid;gap:14px;background:var(--card);border-radius:14px;padding:16px;margin:18px 0}
label{display:block;font-weight:600;margin-bottom:4px}.row{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(150px,1fr))}
input,select,button{font:inherit;color:var(--fg);background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:10px 12px;min-height:44px;width:100%}
button{background:var(--ac);color:var(--acfg);border:0;font-weight:600;cursor:pointer;width:auto;justify-self:start}button.secondary{background:transparent;color:var(--ac);border:1px solid var(--ac)}
:focus-visible{outline:3px solid var(--ac);outline-offset:2px}fieldset{border:1px solid var(--line);border-radius:12px;padding:10px 12px;display:grid;gap:10px}legend{font-weight:600;padding:0 4px}
#out{font-size:1.05em}#out:focus{outline:none}.warn{border:2px solid var(--wb);background:var(--wbg);color:var(--wfg);border-radius:12px;padding:12px 14px}
.cta{display:flex;gap:14px;align-items:flex-start;background:var(--card);border-radius:14px;padding:14px;margin:18px 0}.cta img.i{border-radius:22%;flex:none}.cta p{margin:0 0 8px}.badge img{display:block}
.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:.9em}th,td{border:1px solid var(--line);padding:4px 3px;text-align:center}td small{display:block;color:var(--mu);font-size:.8em;line-height:1.2}
tr.alt td{background:var(--card)}.today{outline:2px solid var(--ac);outline-offset:-2px}
.c{display:inline-block;min-width:1.7em;border-radius:6px;font-weight:700;padding:0 3px;background:#d6e4ff;color:#0b1f4d}.c-D{background:#ffe08a;color:#3d2c00}.c-K{background:#ffb37a;color:#3d1a00}.c-N{background:#3b4f8f;color:#fff}.c-F,.c-L{background:rgba(128,128,128,.2);color:var(--fg)}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}.days{display:flex;gap:8px;flex-wrap:wrap;margin:14px 0 0}.days button[aria-pressed=true]{background:var(--ac);color:var(--acfg)}
.signs{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));padding:0;list-style:none}.signs li{background:var(--card);border-radius:12px;padding:12px 14px}.signs h3{margin:0}.signs small,.mu{color:var(--mu)}
.lucky{background:var(--card);border-radius:12px;padding:10px 14px}footer{margin-top:40px;font-size:.9em;color:var(--mu)}footer a{margin-right:10px}
@media print{form,.cta,footer,.days,.lead,button{display:none}body{max-width:none}}`;

const urls = [];
function page(o) {
  const depth = o.path.split('/').filter(Boolean).length, up = '../'.repeat(depth), url = BASE + '/' + o.path, ui = M.ui[o.lang], app = APP[o.tool];
  const store = `https://apps.apple.com/app/id${app.id}?pt=322891&ct=tool`, alts = Object.entries(o.alts);
  const xdef = o.alts.en || alts[0][1];
  const landing = app.key && slugs[app.key] && slugs[app.key][o.lang];
  const ld = [{ '@context': 'https://schema.org', '@type': 'WebApplication', name: o.h1, description: o.desc, url, inLanguage: o.lang,
    applicationCategory: app.cat, operatingSystem: 'Any', browserRequirements: 'Requires JavaScript', publisher: { '@type': 'Organization', name: 'Baytech BV' } },
  { '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: o.faq.map(([q, a]) => ({ '@type': 'Question', name: q, acceptedAnswer: { '@type': 'Answer', text: a } })) }];
  const html = `<!doctype html><html lang="${o.lang}"${o.dir ? ` dir="${o.dir}"` : ''}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(o.title)}</title><meta name="description" content="${esc(o.desc)}"><meta name="apple-itunes-app" content="app-id=${app.id}">
<link rel="canonical" href="${url}">${alts.map(([l, p]) => `<link rel="alternate" hreflang="${l}" href="${BASE}/${p}">`).join('')}<link rel="alternate" hreflang="x-default" href="${BASE}/${xdef}">
<meta property="og:type" content="website"><meta property="og:title" content="${esc(o.title)}"><meta property="og:description" content="${esc(o.desc)}"><meta property="og:url" content="${url}"><meta property="og:image" content="${app.icon.replace('128x128bb', '512x512bb')}">
${ld.map(x => `<script type="application/ld+json">${json(x)}</script>`).join('')}<style>${CSS}</style></head><body>
<main><h1>${esc(o.h1)}</h1>${o.warn ? `<p class="warn" role="note">${o.warn}</p>` : ''}<p class="lead">${esc(o.lead)}</p>
${o.main}
<aside id="cta" class="cta"${o.ctaHidden ? ' hidden' : ''}><img class="i" src="${app.icon}" alt="" width="64" height="64"><div><p><b>${esc(appName(o.tool, o.lang))}</b><br>${esc(o.cta)}</p>
<a class="badge" href="${store}"><img src="${up}landing/app-store-badge.svg" alt="${esc(ui.badge)}" width="135" height="45"></a></div></aside>
<h2>${ui.faq}</h2>${o.faq.map(([q, a]) => `<h3>${esc(q)}</h3><p>${esc(a)}</p>`).join('')}${o.after || ''}</main>
<footer>${landing ? `<a href="${up}${o.lang}/${landing}/">${ui.about}</a>` : ''}${app.key ? `<a href="${up}${app.key}/">${ui.privacy}</a>` : ''}<br>
${ui.lang}: ${alts.map(([l, p]) => l === o.lang ? `<b>${NAME[l]}</b>` : `<a href="${up}${p}" hreflang="${l}">${NAME[l]}</a>`).join(' ')}<br>© Baytech BV</footer>
<script>var LANG=${json(o.fmtLang || (o.lang === 'en' ? 'en-GB' : o.lang))};${Object.entries(o.data).map(([k, v]) => `var ${k}=${json(v)};`).join('')}
${src('ortak.js')}${src(o.tool + '.js')}</script></body></html>`;
  const file = path.join(ROOT, o.path, 'index.html');
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, html);
  urls.push(url);
}
const field = (id, label, attrs) => `<div><label for="${id}">${esc(label)}</label><input id="${id}" name="${id}" ${attrs}></div>`;
const num = 'type="number" inputmode="decimal" min="0" step="0.01"';
const altsOf = (tool, sub = '') => Object.fromEntries(Object.entries(M[tool]).map(([l, x]) => [l, `${l}/${x.slug}/${sub}`]));

// Tirelire
for (const [lang, x] of Object.entries(M.tirelire)) {
  const big = ['DKK', 'NOK', 'SEK'].includes(x.cur);
  page({ tool: 'tirelire', lang, path: `${lang}/${x.slug}/`, alts: altsOf('tirelire'), ...x, ctaHidden: true, data: { T: x.t, CUR: x.cur },
    main: `<form id="f"><div class="row">${field('goal', x.f.goal, `${num} value="${big ? 600 : 60}"`)}${field('saved', x.f.saved, `${num} value="0"`)}</div>
<div class="row"><div><label for="freq">${esc(x.f.freq)}</label><select id="freq" name="freq"><option value="w">${esc(x.f.w)}</option><option value="m">${esc(x.f.m)}</option></select></div>
${field('per', x.f.per, `${num} value="${big ? 50 : 5}"`)}</div>${field('end', x.f.end, 'type="date"')}<button>${esc(x.f.go)}</button></form>
<section id="out" tabindex="-1" aria-live="polite"></section>` });
}

// Vaktplan
for (const [lang, x] of Object.entries(M.vaktplan)) {
  page({ tool: 'vaktplan', lang, path: `${lang}/${x.slug}/`, alts: altsOf('vaktplan'), ...x, ctaHidden: true, data: { T: x.t },
    main: `<form id="f"><div><label for="preset">${esc(x.f.preset)}</label><select id="preset" name="preset"><option value="">${esc(x.f.choose)}</option>
${x.presets.map(([n, p]) => `<option value="${p}">${esc(n)}</option>`).join('')}</select></div>
${field('pattern', x.f.pattern, `type="text" autocomplete="off" autocapitalize="characters" spellcheck="false" value="${x.presets[0][1]}"`)}
<div class="row">${field('start', x.f.start, 'type="date"')}${field('weeks', x.f.weeks, 'type="number" inputmode="numeric" min="1" max="104" value="8"')}${field('hours', x.f.hours, `${num} step="0.25" value="7.5"`)}</div>
<button>${esc(x.f.go)}</button></form><section id="out" tabindex="-1" aria-live="polite"></section>` });
}

// GLP-1
for (const [lang, x] of Object.entries(M.glp1)) {
  page({ tool: 'glp1', lang, path: `${lang}/${x.slug}/`, alts: altsOf('glp1'), ...x, ctaHidden: true, data: { T: x.t },
    main: `<form id="f"><div class="row">${field('start', x.f.start, 'type="date"')}<div><label for="every">${esc(x.f.every)}</label><select id="every" name="every"><option value="7">${esc(x.f.weekly)}</option><option value="1">${esc(x.f.daily)}</option></select></div></div>
<div id="steps"></div><button type="button" id="add" class="secondary">${esc(x.f.add)}</button><button>${esc(x.f.go)}</button></form>
<template id="step-tpl"><fieldset><legend></legend><div class="row"><div><label>${esc(x.f.label)}</label><input name="label" type="text" autocomplete="off" maxlength="60"></div>
<div><label>${esc(x.f.count)}</label><input name="count" type="number" inputmode="numeric" min="1" max="104" value="4"></div></div><button type="button" class="del secondary">${esc(x.f.del)}</button></fieldset></template>
<section id="out" tabindex="-1" aria-live="polite"></section><p class="warn" role="note">${x.warn}</p>` });
}

// Falcı: hub + one page per sign. Static text is for the build date; the browser redraws it for the reader's own day.
const SIGN = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'];
const RANGE = [[3, 21, 4, 19], [4, 20, 5, 20], [5, 21, 6, 20], [6, 21, 7, 22], [7, 23, 8, 22], [8, 23, 9, 22], [9, 23, 10, 22], [10, 23, 11, 21], [11, 22, 12, 21], [12, 22, 1, 19], [1, 20, 2, 18], [2, 19, 3, 20]];
const today = D.today();
for (const [lang, x] of Object.entries(M.falci)) {
  const P = x.p, md = (m, d) => D.fmt(Date.UTC(2001, m - 1, d), x.fmtLang, { day: 'numeric', month: 'long' });
  const dates = RANGE.map(([a, b, c, d]) => `${md(a, b)} – ${md(c, d)}`);
  const sub = (s, i) => s.replace(/\{sign\}/g, P.signs[i]).replace(/\{dates\}/g, dates[i]);
  const day = `<div class="days" role="group">${P.days.map((d, i) => `<button type="button" class="secondary" data-off="${i - 1}" aria-pressed="${i === 1}">${esc(d)}</button>`).join('')}</div>
<h2 id="day" aria-live="polite">${esc(P.days[1] + ' · ' + D.fmt(today, x.fmtLang, { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' }))}</h2>`;
  const common = { tool: 'falci', lang, dir: x.dir, fmtLang: x.fmtLang, cta: x.cta, data: { P }, after: `<p class="mu">${esc(x.note)}</p>` };
  page({ ...common, path: `${lang}/${x.slug}/`, alts: altsOf('falci'), title: x.title, desc: x.desc, h1: x.h1, lead: x.lead, faq: x.faq,
    main: `${day}<ul class="signs">${SIGN.map((s, i) => `<li><h3><a href="${s}/">${esc(P.signs[i])}</a></h3><small>${esc(dates[i])}</small>
<div data-sign="${i}" data-full="0">${Burc.html(today, i, P, false)}</div><a href="${s}/">${esc(sub(x.more, i))}</a></li>`).join('')}</ul>` });
  SIGN.forEach((s, i) => page({ ...common, path: `${lang}/${x.slug}/${s}/`, alts: altsOf('falci', s + '/'),
    title: sub(x.signTitle, i), desc: sub(x.signDesc, i), h1: sub(x.signH1, i), lead: dates[i], faq: [...x.signFaq.map(([q, a]) => [sub(q, i), sub(a, i)]), ...x.faq],
    main: `${day}<div data-sign="${i}" data-full="1">${Burc.html(today, i, P, true)}</div>
<nav aria-label="${esc(x.others)}"><h2>${esc(x.others)}</h2><p>${SIGN.map((o, j) => [o, j]).filter(([, j]) => j !== i).map(([o, j]) => `<a href="../${o}/">${esc(P.signs[j])}</a>`).join(' · ')} · <a href="../">${esc(x.all)}</a></p></nav>` }));
}

fs.writeFileSync(path.join(__dirname, 'urls.txt'), urls.join('\n') + '\n');
console.log(urls.length + ' pages');
