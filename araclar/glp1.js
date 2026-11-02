// Puts the schedule the user typed in onto dates. No dose logic on purpose: labels are shown exactly as entered.
var Plan = {
  MAX: 400,
  // steps: [{label, count}] in order; every injection is `every` days after the previous one.
  build: function (start, every, steps) {
    var list = [], t = start;
    steps.forEach(function (s, si) {
      for (var i = 0; i < s.count && list.length < Plan.MAX; i++) { list.push({ n: list.length + 1, t: t, label: s.label, step: si }); t = D.addDays(t, every); }
    });
    return list;
  },
  next: function (list, today) { for (var i = 0; i < list.length; i++) if (list[i].t >= today) return list[i]; return null; }
};

if (typeof document !== 'undefined') (function () {
  var f = document.getElementById('f'), out = document.getElementById('out'), cta = document.getElementById('cta');
  var rows = document.getElementById('steps'), tpl = document.getElementById('step-tpl'), seq = 0;
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return '&#' + c.charCodeAt(0) + ';'; }); };
  function renumber() {
    [].forEach.call(rows.children, function (r, i) {
      r.querySelector('legend').textContent = T.step + ' ' + (i + 1);
      r.querySelector('.del').hidden = rows.children.length < 2;
    });
  }
  function add() {
    var r = tpl.content.firstElementChild.cloneNode(true), k = ++seq;
    r.querySelectorAll('input').forEach(function (inp) { var id = inp.name + k; inp.id = id; inp.previousElementSibling.htmlFor = id; });
    r.querySelector('.del').addEventListener('click', function () { r.remove(); renumber(); run(); f.querySelector('#add').focus(); });
    rows.appendChild(r); renumber(); return r;
  }
  document.getElementById('add').addEventListener('click', function () { add().querySelector('input').focus(); });
  function run() {
    var start = D.parse(f.start.value), every = +f.every.value;
    var steps = [].map.call(rows.children, function (r) {
      return { label: r.querySelector('[name=label]').value.trim() || '—', count: Math.min(parseInt(r.querySelector('[name=count]').value, 10) || 0, 104) };
    }).filter(function (s) { return s.count > 0; });
    if (isNaN(start) || !steps.length) { out.innerHTML = '<p>' + T.empty + '</p>'; cta.hidden = true; return; }
    var list = Plan.build(start, every, steps), nx = Plan.next(list, D.today()), last = list[list.length - 1];
    var h = '<p>' + T.summary.replace('{n}', list.length).replace('{first}', D.fmt(start, LANG)).replace('{last}', D.fmt(last.t, LANG)) + '</p>';
    if (nx) h += '<p><b>' + T.next.replace('{date}', D.fmt(nx.t, LANG, { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' })).replace('{label}', esc(nx.label)) + '</b></p>';
    h += '<div class="scroll"><table><caption class="sr">' + T.caption + '</caption><thead><tr><th scope="col">#</th><th scope="col">' + T.date +
      '</th><th scope="col">' + T.dose + '</th></tr></thead><tbody>' + list.map(function (x) {
        return '<tr class="' + (x === nx ? 'today ' : '') + (x.step % 2 ? 'alt' : '') + '"><td>' + x.n + '</td><td>' +
          esc(D.fmt(x.t, LANG, { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' })) + '</td><td>' + esc(x.label) + '</td></tr>';
      }).join('') + '</tbody></table></div><p><button type="button" onclick="print()">' + T.print + '</button></p>';
    out.innerHTML = h;
    cta.hidden = false;
  }
  f.addEventListener('input', run);
  f.addEventListener('submit', function (e) { e.preventDefault(); run(); out.focus(); });
  if (!f.start.value) f.start.value = D.iso(D.today());
  add(); run();
})();
if (typeof module !== 'undefined') module.exports = Plan;
