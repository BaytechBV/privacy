// node araclar/test.js — assert checks for the tool maths.
var assert = require('assert');
global.D = require('./ortak.js');
var E = require('./tirelire.js'), T = require('./vaktplan.js'), P = require('./glp1.js'), B = require('./falci.js');
var d = D.parse;

// dates
assert.strictEqual(D.iso(D.addMonths(d('2027-01-31'), 1)), '2027-02-28');
assert.strictEqual(D.days(d('2026-03-28'), d('2026-03-30')), 2); // across EU DST switch
assert.strictEqual(D.dow(d('2026-11-02')), 0); // Monday

// Tirelire
assert.strictEqual(E.periods(100, 0, 5), 20);
assert.strictEqual(E.periods(100, 1, 5), 20);
assert.strictEqual(E.periods(0.3, 0, 0.1), 3); // no float drift
assert.strictEqual(E.periods(50, 60, 5), 0);
assert.strictEqual(E.periods(50, 0, 0), Infinity);
assert.strictEqual(D.iso(E.reach(d('2026-11-02'), 3, 'w')), '2026-11-23');
assert.strictEqual(D.iso(E.reach(d('2026-11-30'), 3, 'm')), '2027-02-28');
assert.strictEqual(E.between(d('2027-01-31'), d('2027-02-28'), 'm'), 1);
assert.strictEqual(E.between(d('2027-01-15'), d('2027-03-14'), 'm'), 1);
assert.strictEqual(E.needed(100, 0, d('2026-11-02'), d('2026-11-30'), 'w'), 25);
assert.strictEqual(E.needed(100, 0, d('2026-11-02'), d('2026-11-23'), 'w'), 33.34);
assert.ok(isNaN(E.needed(100, 0, d('2026-11-02'), d('2026-11-05'), 'w')));

// Vaktplan
var pan = T.parse('d d f f d d d f f d d f f f');
assert.strictEqual(pan.length, 14);
assert.strictEqual(T.on(d('2026-11-02'), pan, d('2026-11-16')), 'D');
assert.strictEqual(T.on(d('2026-11-02'), pan, d('2026-11-04')), 'F');
assert.strictEqual(T.on(d('2026-11-02'), pan, d('2026-11-01')), 'F'); // before start, wraps back
assert.strictEqual(T.isoWeek(d('2026-11-02')), 45);
assert.strictEqual(T.isoWeek(d('2027-01-01')), 53);
assert.strictEqual(T.isoWeek(d('2025-12-29')), 1);
var s = T.stats(d('2026-11-02'), pan, 14, 'F', 12);
assert.strictEqual(s.work, 7); assert.strictEqual(s.hours, 84); assert.strictEqual(s.perWeek, 42);
var w = T.weeks(d('2026-11-04'), pan, 2);
assert.strictEqual(w[0].days[0].code, ''); // Monday before the start date is empty
assert.strictEqual(w[0].days[2].code, 'D');

// GLP-1
var l = P.build(d('2026-11-02'), 7, [{ label: 'A', count: 4 }, { label: 'B', count: 2 }]);
assert.strictEqual(l.length, 6);
assert.strictEqual(D.iso(l[4].t), '2026-11-30'); assert.strictEqual(l[4].label, 'B');
assert.strictEqual(P.next(l, d('2026-11-10')).n, 3);
assert.strictEqual(P.next(l, d('2027-01-01')), null);
assert.strictEqual(P.build(d('2026-11-02'), 1, [{ label: 'x', count: 999 }]).length, P.MAX);

// Falcı: total solar eclipse 2024-04-08 (Moon and Sun in Aries), full moon 2024-04-23/24 (Moon in Scorpio)
var e = B.sky(d('2024-04-08'));
assert.strictEqual(e.moon, 0); assert.strictEqual(e.sun, 0); assert.strictEqual(e.phase, 0);
var fm = B.sky(d('2024-04-24'));
assert.strictEqual(fm.moon, 7); assert.strictEqual(fm.phase, 4);
assert.strictEqual(B.aspect(3, 3), 0); assert.strictEqual(B.aspect(0, 6), 4); assert.strictEqual(B.aspect(4, 0), 1);
var a = B.rng('2026-11-02:1:en'), b = B.rng('2026-11-02:1:en');
assert.strictEqual(a(), b()); // deterministic
console.log('ok');
