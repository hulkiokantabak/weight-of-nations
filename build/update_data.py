# -*- coding: utf-8 -*-
"""
update_data.py — a guarded harness for the annual/release data refresh.

Philosophy (see skills/weight-of-nations-data-refresh): the living document updates by
editing build/data.py ONLY, then re-running the 52-check suite and rebuilding. This tool does
NOT silently rewrite data.py — the dual architecture keeps a human (or the Code executor) in
the loop for every edit. Instead it:

  --show       print the current value of every source-fed field, with its source lane
  --validate   sanity-check proposed values (KEY=VALUE ...) against ranges, before you edit
  --check      run check_consistency.py and report pass/fail

Usage:
  python3 update_data.py --show
  python3 update_data.py --validate WORLD_PPP_T=231.4 WORLD_NOMINAL_T=131.0
  python3 update_data.py --check
"""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import data as D

# field -> (source lane, refresh trigger). Derived fields are intentionally excluded:
# update their inputs, not them (the suite enforces this).
SOURCE_FED = {
    "WORLD_NOMINAL_T":      ("IMF WEO (current US$)",                "every WEO (Apr/Oct)"),
    "WORLD_PPP_T":          ("IMF WEO (current int$)",               "every WEO (Apr/Oct)"),
    "PPP_2026_CURRENT":     ("IMF (current int$, present marker)",   "WEO"),
    "PPP_2024_CURRENT":     ("WDI/IMF (current int$, 2024)",         "WDI"),
    "PPP_2024_CONST2021":   ("WDI (constant-2021 int$)",             "WDI"),
    "SHARE24_NOM":          ("WDI country-sum, 2024 nominal",        "WDI"),
    "SHARE24_PPP":          ("WDI country-sum, 2024 PPP",            "WDI"),
    "MULT24_NOM":           ("derived: nominal share / pop share",   "WDI (inputs)"),
    "MULT24_PPP":           ("derived: PPP share / pop share",       "WDI (inputs)"),
    "POP24":                ("UN WPP / WDI population share",        "WPP / WDI"),
    "DELTA_NOM":            ("WDI 1990->2024 nominal deltas",        "WDI"),
    "DELTA_PPP":            ("WDI 1990->2024 PPP deltas",            "WDI"),
    "JP_NOM":               ("WDI anchors [V] + benchmark [E]",      "WDI (endpoints)"),
    "JP_PPP":               ("WDI anchors [V] + benchmark [E]",      "WDI (endpoints)"),
}

# sane ranges for scalar sanity-checks
SCALAR_RANGES = {
    "WORLD_NOMINAL_T":    (80, 200),
    "WORLD_PPP_T":        (150, 350),
    "PPP_2026_CURRENT":   (150, 350),
    "PPP_2024_CURRENT":   (150, 300),
    "PPP_2024_CONST2021": (120, 260),
}

def show():
    print("=== Source-fed fields in data.py (edit these; leave derived fields alone) ===\n")
    for k, (src, trig) in SOURCE_FED.items():
        v = getattr(D, k, "(absent)")
        vs = v if not isinstance(v, (list, dict)) else f"{type(v).__name__} len={len(v)}"
        print(f"  {k:20} = {vs}")
        print(f"  {'':20}   source: {src}   | refresh: {trig}\n")
    print("Derived (DO NOT hand-edit; update inputs and the suite recomputes):")
    print("  GAP24, SWING_*, CONE midpoints, SCEN_BARS 'Rest of World' residual\n")
    print("Coda (illustrative; NOT a data feed; move only on a new analytical edition):")
    print("  CONE, SCEN_BARS, SCEN, AGG_L_POP, DEMOG_*, DOLLAR_*, MULT_SHIFT_*")

def validate(pairs):
    print("=== Validating proposed values (no file is written) ===\n")
    ok = True
    parsed = {}
    for p in pairs:
        if "=" not in p:
            print(f"  ! skip '{p}' (need KEY=VALUE)"); ok = False; continue
        k, raw = p.split("=", 1)
        k = k.strip()
        if k not in SOURCE_FED:
            print(f"  ! {k}: not a recognised source-fed field (or it is derived). "
                  f"Edit its inputs instead." ); ok = False; continue
        try:
            val = float(raw)
        except ValueError:
            print(f"  ~ {k}: '{raw}' is not scalar — validate arrays by eye against source."); 
            parsed[k] = raw; continue
        lo, hi = SCALAR_RANGES.get(k, (None, None))
        if lo is not None and not (lo <= val <= hi):
            print(f"  ! {k} = {val}: OUTSIDE sane range [{lo}, {hi}] — double-check the source/vintage."); ok = False
        else:
            print(f"  OK {k} = {val}  (source: {SOURCE_FED[k][0]})")
        parsed[k] = val
    # cross-checks
    if "WORLD_PPP_T" in parsed and "WORLD_NOMINAL_T" in parsed:
        try:
            if float(parsed["WORLD_PPP_T"]) <= float(parsed["WORLD_NOMINAL_T"]):
                print("  ! world PPP must exceed world nominal (PPP lifts low-price economies)."); ok = False
            else:
                gap = float(parsed["WORLD_PPP_T"]) - float(parsed["WORLD_NOMINAL_T"])
                print(f"  note: implied PPP-nominal world gap = ${gap:.1f}T "
                      f"(front-matter text states this gap; update prose ONLY if the direction changes).")
        except ValueError:
            pass
    print()
    print("Reminder: PPP carries +/-5-10%; keep three PPP lanes distinct; estimates stay [E];")
    print("after editing data.py, run:  python3 update_data.py --check")
    print("\nVALIDATION:", "PASS" if ok else "ISSUES FOUND")
    return ok

def check():
    print("=== Running check_consistency.py ===\n")
    r = subprocess.run([sys.executable, os.path.join(HERE, "check_consistency.py")],
                       capture_output=True, text=True)
    print(r.stdout[-1500:])
    if r.returncode != 0 or "FAILED" in r.stdout and "0 FAILED" not in r.stdout:
        print("\n>>> Suite not green. Fix the DATA (not the check) and re-run.")
        return False
    print(">>> Suite green." if "0 FAILED" in r.stdout else ">>> See output above.")
    return True

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or "--show" in args:
        show()
    if "--validate" in args:
        i = args.index("--validate")
        validate(args[i+1:])
    if "--check" in args:
        check()
