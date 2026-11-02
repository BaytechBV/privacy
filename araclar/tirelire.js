// Savings goal maths. Amounts are worked in cents to avoid 0.1 + 0.2 drift; freq 'w' = weekly, 'm' = monthly.
var Epargne = {
  cents: function (x) { return Math.round(x * 100); },
  // Periods until the goal is reached: 0 if already there, Infinity if nothing is put aside.
  periods: function (goal, saved, per) {
    var rest = Epargne.cents(goal) - Epargne.cents(saved), p = Epargne.cents(per);
    if (rest <= 0) return 0;
    return p > 0 ? Math.ceil(rest / p) : Infinity;
  },
  reach: function (start, n, freq) { return freq === 'm' ? D.addMonths(start, n) : D.addDays(start, 7 * n); },
  // Whole periods that fit between start and end.
  between: function (start, end, freq) {
    if (freq !== 'm') return Math.floor(D.days(start, end) / 7);
    var a = new Date(start), b = new Date(end);
    var m = (b.getUTCFullYear() - a.getUTCFullYear()) * 12 + b.getUTCMonth() - a.getUTCMonth();
    while (m > 0 && D.addMonths(start, m) > end) m--;
    return Math.max(m, 0);
  },
  // Amount to put aside each period to reach the goal by end (rounded up to the cent); NaN if no full period fits.
  needed: function (goal, saved, start, end, freq) {
    var rest = Epargne.cents(goal) - Epargne.cents(saved), n = Epargne.between(start, end, freq);
    if (rest <= 0) return 0;
    return n >= 1 ? Math.ceil(rest / n) / 100 : NaN;
  }
};

if (typeof document !== 'undefined') (function () {
  var f = document.getElementById('f'), out = document.getElementById('out'), cta = document.getElementById('cta');
  var money = new Intl.NumberFormat(LANG, { style: 'currency', currency: CUR });
  var num = function (id) { var v = parseFloat(String(f[id].value).replace(',', '.')); return isNaN(v) ? 0 : v; };
  function run() {
    var goal = num('goal'), saved = num('saved'), per = num('per'), freq = f.freq.value, start = D.today();
    var every = T['e' + freq], lines = [];
    if (goal <= 0) { out.innerHTML = ''; cta.hidden = true; return; }
    if (saved >= goal) lines.push(T.done);
    else {
      var n = Epargne.periods(goal, saved, per);
      if (n === Infinity) lines.push(T.noPer);
      else lines.push(T.reach.replace('{per}', money.format(per)).replace('{every}', every).replace('{n}', n)
        .replace('{units}', T[n === 1 ? freq : freq + 's']).replace('{date}', D.fmt(Epargne.reach(start, n, freq), LANG)));
      var end = D.parse(f.end.value);
      if (!isNaN(end)) {
        var need = Epargne.needed(goal, saved, start, end, freq);
        lines.push(isNaN(need) ? T.tooSoon : T.need.replace('{date}', D.fmt(end, LANG)).replace('{amt}', money.format(need)).replace('{every}', every));
      }
      lines.push(T.rest.replace('{amt}', money.format(goal - saved)));
    }
    out.innerHTML = lines.map(function (l) { return '<p>' + l + '</p>'; }).join('');
    cta.hidden = false;
  }
  f.addEventListener('input', run);
  f.addEventListener('submit', function (e) { e.preventDefault(); run(); out.focus(); });
  run();
})();
if (typeof module !== 'undefined') module.exports = Epargne;
