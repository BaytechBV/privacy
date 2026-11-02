// Shared date helpers. Dates are UTC midnights so a DST switch never moves a day.
var D = {
  parse: function (s) { var p = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s || ''); return p ? Date.UTC(+p[1], p[2] - 1, +p[3]) : NaN; },
  iso: function (t) { return new Date(t).toISOString().slice(0, 10); },
  addDays: function (t, n) { return t + n * 864e5; },
  addMonths: function (t, n) {
    var d = new Date(t), y = d.getUTCFullYear(), m = d.getUTCMonth() + n;
    var last = new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
    return Date.UTC(y, m, Math.min(d.getUTCDate(), last));
  },
  days: function (a, b) { return Math.round((b - a) / 864e5); },
  dow: function (t) { return (new Date(t).getUTCDay() + 6) % 7; }, // 0 = Monday
  today: function () { var n = new Date(); return Date.UTC(n.getFullYear(), n.getMonth(), n.getDate()); },
  fmt: function (t, lang, o) {
    return new Intl.DateTimeFormat(lang, Object.assign({ timeZone: 'UTC' }, o || { day: 'numeric', month: 'long', year: 'numeric' })).format(t);
  }
};
if (typeof module !== 'undefined') module.exports = D;
