"""
check_consistency.py — math + cross-figure consistency suite for
"The Shifting Weight of Nations". Imports data.py and asserts every
internal relationship the document relies on. Prints PASS/FAIL per check.
Run from build/:  python3 check_consistency.py
"""
import data as D

PASS, FAIL = [], []
def ok(name):  PASS.append(name);  print(f"  PASS  {name}")
def bad(name, detail): FAIL.append((name, detail)); print(f"  FAIL  {name}\n        {detail}")
def near(a, b, tol=0.02): return abs(a - b) <= tol
def hdr(t): print(f"\n=== {t} ===")

# ---------------------------------------------------------------
hdr("1. Multiplier identity  (multiplier = GDP share / population share)")
for e in D.MULT24_ENT:
    nom = D.SHARE24_NOM[D.SHARE24_ENT.index(e)]
    ppp = D.SHARE24_PPP[D.SHARE24_ENT.index(e)]
    pop = D.POP24[D.POP24_ENT.index(e)]
    mn, mp = D.MULT24_NOM[D.MULT24_ENT.index(e)], D.MULT24_PPP[D.MULT24_ENT.index(e)]
    en, ep = nom/pop, ppp/pop
    if near(mn, en, 0.03) and near(mp, ep, 0.03):
        ok(f"{e:14s} nom {mn:.2f}≈{en:.2f}  ppp {mp:.2f}≈{ep:.2f}")
    else:
        bad(f"{e} multiplier", f"nom {mn} vs {en:.3f} | ppp {mp} vs {ep:.3f}")

hdr("2. Ruler gap  (GAP24 = nominal share - PPP share)")
for e in D.GAP24_ENT:
    nom = D.SHARE24_NOM[D.SHARE24_ENT.index(e)]
    ppp = D.SHARE24_PPP[D.SHARE24_ENT.index(e)]
    if near(D.GAP24[e], nom-ppp, 0.001): ok(f"{e:14s} gap {D.GAP24[e]:+.2f}")
    else: bad(f"{e} gap", f"{D.GAP24[e]} vs {nom-ppp:.2f}")

hdr("3. Fig 01/02 long-run PPP shares sum to 100% per benchmark year")
for i, yr in enumerate(D.YEARS_LONG):
    s = sum(D.LONG[k][i] for k in D.LONG)
    if near(s, 100.0, 0.15): ok(f"{yr}: {s:.1f}%")
    else: bad(f"LONG sum {yr}", f"sums to {s:.2f}%")

hdr("4. Fig 14 swing dots land on actual 2024 PPP share  (pop% x multiplier = share%)")
for e in D.SWING_ENT:
    implied = D.SWING_POP[e] * D.SWING_MULT24[e]
    actual  = D.SHARE24_PPP[D.SHARE24_ENT.index(e)]
    if near(implied, actual, 0.25): ok(f"{e:14s} {D.SWING_POP[e]:.2f}×{D.SWING_MULT24[e]:.2f}={implied:.2f} ≈ {actual}")
    else: bad(f"{e} swing dot", f"implied {implied:.2f} vs actual {actual}")

hdr("5. Fig 08 long-run multiplier endpoint (2024) == Fig 11 cross-section multiplier")
m2024 = {k: D.MULT[k][-1] for k in D.MULT}          # last col = 2024
for e in ["United States","Japan","Russia / USSR","China","India"]:
    key = {"Russia / USSR":"Russia"}.get(e, e)
    if key in D.MULT24_ENT:
        a, b = m2024[e], D.MULT24_PPP[D.MULT24_ENT.index(key)]
        if near(a, b, 0.03): ok(f"{e:16s} {a:.2f} ≈ {b:.2f}")
        else: bad(f"{e} mult endpoint", f"Fig08 {a} vs Fig11 {b}")

hdr("6. Fig 07 bloc delta == sum of member deltas (internal additivity)")
west_nom = D.BLOC["West bloc \u2014 nominal"][-1] - D.BLOC["West bloc \u2014 nominal"][0]
mem_nom  = D.DELTA_NOM["United States"] + D.DELTA_NOM["EU-27 + UK"] + D.DELTA_NOM["Japan"]
if near(west_nom, mem_nom, 0.5): ok(f"West nominal Δ {west_nom:+.1f} ≈ Σ(US,EU+UK,JP) {mem_nom:+.1f}")
else: bad("West nominal additivity", f"bloc {west_nom:+.2f} vs members {mem_nom:+.2f}")
ci_nom = D.BLOC["China + India \u2014 nominal"][-1] - D.BLOC["China + India \u2014 nominal"][0]
mem_ci = D.DELTA_NOM["China"] + D.DELTA_NOM["India"]
if near(ci_nom, mem_ci, 0.5): ok(f"China+India nominal Δ {ci_nom:+.1f} ≈ Σ {mem_ci:+.1f}")
else: bad("China+India additivity", f"bloc {ci_nom:+.2f} vs members {mem_ci:+.2f}")

hdr("7. ***Fig 18 cone 2050 envelope == Fig 19 scenario-bar [min,max]***")
for ctry in D.CONE:
    lo, mid, hi = D.CONE[ctry][-1]                 # 2050 envelope
    bars = D.SCEN_BARS[ctry]
    bmin, bmax = min(bars), max(bars)
    if near(lo, bmin, 0.05) and near(hi, bmax, 0.05):
        ok(f"{ctry:14s} cone[{lo},{hi}] == bars[{bmin},{bmax}]")
    else:
        bad(f"{ctry} cone vs bars", f"cone 2050 lo/hi = {lo}/{hi}  but scenario bars min/max = {bmin}/{bmax}")

hdr("8. Fig 18 cone 2024 start == actual 2024 PPP share")
for ctry in D.CONE:
    start = D.CONE[ctry][0][1]
    actual = D.SHARE24_PPP[D.SHARE24_ENT.index({"Sub-Saharan Africa":"x"}.get(ctry,ctry))] if ctry in D.SHARE24_ENT else None
    if actual is not None and near(start, round(actual,1), 0.06): ok(f"{ctry:14s} start {start} ≈ {actual}")
    elif actual is None: ok(f"{ctry:14s} start {start} (no 2024 cross-ref)")
    else: bad(f"{ctry} cone start", f"{start} vs SHARE24_PPP {actual}")

hdr("9. ***Fig 19 scenario bars: each scenario column sums to 100% (RoW = residual)***")
for j, sc in enumerate(D.SCEN):
    s = sum(D.SCEN_BARS[a][j] for a in D.SCEN_BARS_ACTORS)
    if near(s, 100.0, 0.6): ok(f"{sc:13s} {s:.1f}%")
    else: bad(f"scenario sum {sc}", f"6 actors sum to {s:.1f}% (must be 100; RoW is the residual)")

hdr("10. Fig 13 Japan PPP line honours prose 'never crosses ~8 percent'")
jp_max = max(D.JP_PPP)
if jp_max <= 8.05: ok(f"max Japan PPP = {jp_max} (<= ~8)")
else: bad("Japan PPP cap", f"prose: 'never crosses ~8%' but JP_PPP peaks at {jp_max} (year {D.JP_YEARS[D.JP_PPP.index(jp_max)]})")

hdr("11. Fig 15 (AGG_L) 1500 population == B3 table 1500 population (0.44bn)")
B3_1500_POP = 0.44
if near(D.AGG_L_POP[0], B3_1500_POP, 0.01): ok(f"AGG_L 1500 pop {D.AGG_L_POP[0]} == B3 {B3_1500_POP}")
else: bad("1500 population", f"Fig15 AGG_L = {D.AGG_L_POP[0]}bn but B3 table = {B3_1500_POP}bn")

hdr("12. World totals: PPP - nominal = the '~$96T gap' stated in front matter")
gap = D.WORLD_PPP_T - D.WORLD_NOMINAL_T
if 95 <= gap <= 98: ok(f"{D.WORLD_PPP_T} - {D.WORLD_NOMINAL_T} = {gap:.1f}T (~$96T) ")
else: bad("world gap", f"{gap}")

hdr("13. Three PPP lanes remain distinct (never merged)")
lanes = {D.PPP_2026_CURRENT, D.PPP_2024_CURRENT, D.PPP_2024_CONST2021}
if len(lanes) == 3: ok(f"distinct lanes: {sorted(lanes)}")
else: bad("PPP lanes", f"collapsed: {lanes}")

hdr("14. Fig 21 dollar paths: all start 58, ordered status>base>frag>rupture at 2050")
starts = {k: D.DOLLAR[k][0] for k in D.DOLLAR}
ends   = {k: D.DOLLAR[k][-1] for k in D.DOLLAR}
if all(v == 58 for v in starts.values()): ok("all paths start at 58%")
else: bad("dollar starts", f"{starts}")
if ends["status-quo-plus"] > ends["base drift"] > ends["fragmentation"] > ends["rupture"]:
    ok(f"2050 ordering correct: {ends}")
else: bad("dollar ordering", f"{ends}")

# ---------------------------------------------------------------
print("\n" + "="*64)
print(f"  RESULT: {len(PASS)} passed, {len(FAIL)} FAILED")
if FAIL:
    print("  FAILURES:")
    for n, d in FAIL: print(f"   - {n}: {d}")
print("="*64)
