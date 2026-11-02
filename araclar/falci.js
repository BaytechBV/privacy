// Daily horoscope: real Sun/Moon positions for the day + text picked from fixed pools with a date+sign seed.
// Same date and sign always give the same text, so the static HTML and the browser agree; no API involved.
var Burc = {
  // Low-precision ecliptic longitudes at 12:00 UTC (Moon within ~0.5°; enough to name its sign and phase).
  sky: function (t) {
    var d = (t + 432e5) / 864e5 - 10957.5, r = Math.PI / 180, n = function (x) { return ((x % 360) + 360) % 360; };
    var L = 218.316 + 13.176396 * d, M = 134.963 + 13.064993 * d, F = 93.272 + 13.22935 * d;
    var E = 297.85 + 12.190749 * d, S = 357.529 + 0.98560028 * d;
    var moon = n(L + 6.289 * Math.sin(M * r) + 1.274 * Math.sin((2 * E - M) * r) + 0.658 * Math.sin(2 * E * r) +
      0.214 * Math.sin(2 * M * r) - 0.186 * Math.sin(S * r) - 0.114 * Math.sin(2 * F * r));
    var sun = n(280.46 + 0.9856474 * d + 1.915 * Math.sin(S * r) + 0.02 * Math.sin(2 * S * r));
    var elong = n(moon - sun);
    return { sun: Math.floor(sun / 30), moon: Math.floor(moon / 30), elong: elong, phase: Math.floor(((elong + 22.5) % 360) / 45) };
  },
  // Aspect of the Moon's sign to the reader's sign: 0 same, 1 trine, 2 sextile, 3 square, 4 opposite, 5 none.
  aspect: function (moon, sign) { return [0, 5, 2, 3, 1, 5, 4, 5, 1, 3, 2, 5][(moon - sign + 12) % 12]; },
  rng: function (str) {
    for (var h = 2166136261, i = 0; i < str.length; i++) h = Math.imul(h ^ str.charCodeAt(i), 16777619);
    return function () { h += 0x6D2B79F5; var x = Math.imul(h ^ (h >>> 15), 1 | h); x ^= x + Math.imul(x ^ (x >>> 7), 61 | x); return ((x ^ (x >>> 14)) >>> 0) / 4294967296; };
  },
  reading: function (t, sign, P) {
    var s = Burc.sky(t), R = Burc.rng(D.iso(t) + ':' + sign + ':' + P.lang), pick = function (a) { return a[Math.floor(R() * a.length)]; };
    return {
      sky: P.moonIn.replace('{moon}', P.signs[s.moon]).replace('{phase}', P.phases[s.phase]) + ' ' + pick(P.aspects[Burc.aspect(s.moon, sign)]),
      trait: pick(P.elements[sign % 4]),
      love: pick(P.love), work: pick(P.work), mood: pick(P.mood), advice: pick(P.advice),
      number: 1 + Math.floor(R() * 49), color: pick(P.colors)
    };
  },
  html: function (t, sign, P, full) {
    var r = Burc.reading(t, sign, P), p = function (k, v) { return '<p><b>' + P.h[k] + ':</b> ' + v + '</p>'; };
    if (!full) return '<p>' + r.sky + '</p><p>' + r.advice + '</p>';
    return '<p>' + r.sky + ' ' + r.trait + '</p>' + p('love', r.love) + p('work', r.work) + p('mood', r.mood) +
      p('advice', r.advice) + '<p class="lucky">' + P.h.number + ': <b>' + r.number + '</b> · ' + P.h.color + ': <b>' + r.color + '</b></p>';
  }
};

if (typeof document !== 'undefined') (function () {
  var title = document.getElementById('day');
  function show(off) {
    var t = D.addDays(D.today(), off);
    title.textContent = P.days[off + 1] + ' · ' + D.fmt(t, LANG, { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
    document.querySelectorAll('[data-sign]').forEach(function (el) { el.innerHTML = Burc.html(t, +el.dataset.sign, P, el.dataset.full === '1'); });
    document.querySelectorAll('[data-off]').forEach(function (b) { b.setAttribute('aria-pressed', +b.dataset.off === off); });
  }
  document.querySelectorAll('[data-off]').forEach(function (b) { b.addEventListener('click', function () { show(+b.dataset.off); }); });
  show(0);
})();
if (typeof module !== 'undefined') module.exports = Burc;
