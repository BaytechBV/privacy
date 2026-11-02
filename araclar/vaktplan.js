// Rotation (turnus) maths: a pattern is a list of shift codes repeated from the start date.
var Turnus = {
  parse: function (s) { return String(s || '').toUpperCase().split(/[\s,;]+/).filter(Boolean); },
  on: function (start, pattern, t) { var L = pattern.length, i = D.days(start, t) % L; return pattern[(i + L) % L]; },
  isoWeek: function (t) {
    var d = new Date(D.addDays(t, 3 - D.dow(t))), y = d.getUTCFullYear(); // Thursday of this week decides the year
    return 1 + Math.floor(D.days(Date.UTC(y, 0, 1), d.getTime()) / 7);
  },
  // Rows of Monday–Sunday weeks covering n weeks from the week of start.
  weeks: function (start, pattern, n) {
    var mon = D.addDays(start, -D.dow(start)), rows = [];
    for (var w = 0; w < n; w++) {
      var days = [];
      for (var i = 0; i < 7; i++) { var t = D.addDays(mon, 7 * w + i); days.push({ t: t, code: t < start ? '' : Turnus.on(start, pattern, t) }); }
      rows.push({ week: Turnus.isoWeek(D.addDays(mon, 7 * w)), days: days });
    }
    return rows;
  },
  // Counts per code, worked shifts, hours and average hours per week over `days` days from start.
  stats: function (start, pattern, days, off, hours) {
    var count = {}, work = 0;
    for (var i = 0; i < days; i++) { var c = Turnus.on(start, pattern, D.addDays(start, i)); count[c] = (count[c] || 0) + 1; if (c !== off) work++; }
    return { count: count, work: work, hours: work * hours, perWeek: days ? work * hours * 7 / days : 0 };
  }
};

if (typeof document !== 'undefined') (function () {
  var f = document.getElementById('f'), out = document.getElementById('out'), cta = document.getElementById('cta');
  var nf = new Intl.NumberFormat(LANG, { maximumFractionDigits: 1 });
  var dayNames = [0, 1, 2, 3, 4, 5, 6].map(function (i) { return D.fmt(Date.UTC(2024, 0, 1 + i), LANG, { weekday: 'short' }); });
  var esc = function (s) { return s.replace(/[&<>"]/g, function (c) { return '&#' + c.charCodeAt(0) + ';'; }); };
  f.preset.addEventListener('change', function () { if (f.preset.value) { f.pattern.value = f.preset.value; run(); } });
  function run() {
    var pattern = Turnus.parse(f.pattern.value), start = D.parse(f.start.value);
    var n = Math.min(Math.max(parseInt(f.weeks.value, 10) || 8, 1), 104), hours = parseFloat(String(f.hours.value).replace(',', '.')) || 0;
    if (!pattern.length || isNaN(start)) { out.innerHTML = '<p>' + T.empty + '</p>'; cta.hidden = true; return; }
    var rows = Turnus.weeks(start, pattern, n), s = Turnus.stats(start, pattern, n * 7, T.off, hours), today = D.today();
    var h = '<p>' + T.summary.replace('{len}', pattern.length).replace('{work}', s.work).replace('{days}', n * 7)
      .replace('{hours}', nf.format(s.hours)).replace('{avg}', nf.format(s.perWeek)) + '</p>';
    h += '<p class="codes">' + Object.keys(s.count).map(function (c) { return '<span class="c c-' + esc(c) + '">' + esc(c) + '</span> ' + s.count[c]; }).join(' · ') + '</p>';
    h += '<div class="scroll"><table><caption class="sr">' + T.caption + '</caption><thead><tr><th scope="col">' + T.week + '</th>' +
      dayNames.map(function (d) { return '<th scope="col">' + d + '</th>'; }).join('') + '</tr></thead><tbody>';
    rows.forEach(function (r, ri) {
      h += '<tr><th scope="row">' + r.week + '</th>' + r.days.map(function (d, di) {
        var first = new Date(d.t).getUTCDate() === 1 || (ri === 0 && di === 0);
        var label = D.fmt(d.t, LANG, first ? { day: 'numeric', month: 'short' } : { day: 'numeric' });
        return '<td' + (d.t === today ? ' class="today"' : '') + ' title="' + esc(D.fmt(d.t, LANG, { weekday: 'long', day: 'numeric', month: 'long' })) + '">' +
          '<small>' + esc(label) + '</small>' + (d.code ? '<span class="c c-' + esc(d.code) + '">' + esc(d.code) + '</span>' : '') + '</td>';
      }).join('') + '</tr>';
    });
    out.innerHTML = h + '</tbody></table></div>';
    cta.hidden = false;
  }
  f.addEventListener('input', run);
  f.addEventListener('submit', function (e) { e.preventDefault(); run(); out.focus(); });
  if (!f.start.value) f.start.value = D.iso(D.today());
  run();
})();
if (typeof module !== 'undefined') module.exports = Turnus;
