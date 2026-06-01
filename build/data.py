"""
data.py — single numeric source of truth for "The Shifting Weight of Nations".
Every figure in both the interactive HTML and the PDF reads from here.
Sources: Maddison Project (deep history), World Bank WDI country-sum (modern),
IMF WEO 2025-26 vintage (current marker), Bairoch 1982 (manufacturing).
Figures are estimates; read direction and order of magnitude, not decimals.
"""

PALETTE = {
    "paper":"#F4EEE2","paper2":"#FBF7EF","card":"#FCFAF4",
    "ink":"#221C17","ink_soft":"#5C534A","ink_faint":"#8C8273",
    "rule":"#DCD2C1","rule_soft":"#E7DECF","accent":"#993C1D","accent2":"#B9743A",
    "us":"#A23B26","cn":"#D29329","eu":"#2F5573","in":"#2E8B6F",
    "jp":"#8A4F7D","uk":"#C77B43","ru":"#6E7B3E","row":"#A79D90","ss":"#2C6E6B",
}

# ---- Fig 01 / 02 : long-run PPP shares (Maddison-style benchmark years) ----
YEARS_LONG = ["1500","1600","1700","1820","1870","1913","1950","1973","2000","2024"]
LONG_ORDER = ["United States","Western Europe","Japan","Russia / USSR","China","India","Rest of world"]
LONG = {
    "United States":[0.3,0.2,0.1,1.8,8.9,19,27,22,21,15],
    "Western Europe":[18,20,22,23,33,33,26,25,20,15],
    "Japan":[3.1,2.9,4.1,3.0,2.3,2.6,3.0,7.7,7,3.4],
    "Russia / USSR":[3.4,3.5,4.4,5.4,7.6,8.6,9.6,9.4,2.7,3.5],
    "China":[25,29,22,33,17,9,4.5,4.6,12,19],
    "India":[24,22,24,16,12,7.5,4.2,3.1,5,8],
    "Rest of world":[26.2,22.4,23.4,17.8,19.2,20.3,25.7,28.2,32.3,36.1],
}
LONG_COLORKEY = {"United States":"us","Western Europe":"eu","Japan":"jp",
    "Russia / USSR":"ru","China":"cn","India":"in","Rest of world":"row"}

# ---- Fig 03 : Bairoch share of world manufacturing output ----
YEARS_MFG = ["1750","1800","1830","1860","1880","1900"]
MFG_ORDER = ["China","India","Europe (incl. UK)","United States","Japan"]
MFG = {
    "China":[32.8,33.3,29.8,19.7,12.5,6.2],
    "India":[24.5,19.7,17.6,8.6,2.8,1.7],
    "Europe (incl. UK)":[23.2,28.1,34.2,53.2,61.3,62.0],
    "United States":[0.1,0.8,2.4,7.2,14.7,23.6],
    "Japan":[3.8,3.5,2.8,2.6,2.4,2.4],
}
MFG_COLORKEY = {"China":"cn","India":"in","Europe (incl. UK)":"eu","United States":"us","Japan":"jp"}

# ---- Fig 04 : modern nominal shares (market exchange rates) ----
YEARS_NOM = ["1960","1970","1980","1985","1990","1995","2000","2008","2010","2015","2020","2024"]
NOM_ORDER = ["United States","EU (current 27)","Japan","China","United Kingdom","India"]
NOM = {
    "United States":[40,36,26,34,26,25,30,23,23,24,25,26.3],
    "EU (current 27)":[26,28,31,25,30,26,21,30,25,22,18,17.9],
    "Japan":[3,7,10,11,14,17.8,14.5,8.2,8.6,6,6,3.7],
    "China":[4,3,1.7,2.4,1.7,2.4,3.6,7.2,9.2,15,17.4,17.2],
    "United Kingdom":[6.5,5.5,5,4.5,4.5,4,4.7,5.2,3.6,3.9,3.2,3.4],
    "India":[2.7,2.2,1.6,1.8,1.7,1.3,1.4,2,2.6,2.8,3.1,3.6],
}
NOM_COLORKEY = {"United States":"us","EU (current 27)":"eu","Japan":"jp",
    "China":"cn","United Kingdom":"uk","India":"in"}
WEST_BLOC_NOM = [75.5,76.5,72,74.5,74.5,72.8,70.2,66.4,60.2,55.9,52.2,51.3]

# ---- Fig 05 : US nominal share, 1913-2024 (benchmark estimates; wide pre-1960 bands) ----
YEARS_US = ["1913","1929","1938","1945","1960","1973","1985","2000","2011","2024"]
US_NOM = [19,28,25,50,40,26,34,30,21,26]

# ---- Fig 06 : bloc vs bloc, both rulers (WDI country-sum) ----
YEARS_BLOC = ["1990","1995","2000","2005","2010","2015","2020","2024"]
BLOC_ORDER = ["West bloc \u2014 nominal","West bloc \u2014 PPP",
    "China + India \u2014 nominal","China + India \u2014 PPP"]
BLOC = {
    "West bloc \u2014 nominal":[76.4,75,72,68,62,55,52,51.3],
    "West bloc \u2014 PPP":[59,57,54,48,43,39,36,34.9],
    "China + India \u2014 nominal":[3.1,4,5.5,8,11.8,17.5,20.5,20.8],
    "China + India \u2014 PPP":[7.4,9,11,15,20,24,27,28.1],
}

# ---- Fig 07 : who gained / lost world-GDP share, 1990-2024 (percentage points) ----
DELTA_ENT = ["China","India","Russia","United States","Japan","EU-27 + UK"]
DELTA_NOM = {"China":15.5,"India":2.1,"Russia":0.1,"United States":-1.1,"Japan":-10.9,"EU-27 + UK":-13.1}
DELTA_PPP = {"China":16.0,"India":4.7,"Russia":-2.4,"United States":-6.5,"Japan":-5.1,"EU-27 + UK":-13.2}

# ---- Fig 08 : prosperity multiplier over time (PPP, GDP share / population share) ----
YEARS_MULT = ["1820","1870","1913","1950","1973","2000","2024"]
MULT_ORDER = ["United States","Western Europe","Japan","Russia / USSR","China","India"]
MULT = {
    "United States":[2.0,2.87,3.52,4.50,4.07,4.5,3.56],
    "Western Europe":[1.84,2.75,3.30,2.99,3.57,3.17,2.73],
    "Japan":[1.0,0.85,0.90,0.91,2.75,3.33,2.18],
    "Russia / USSR":[1.08,1.09,0.96,1.37,1.49,1.13,2.00],
    "China":[0.89,0.61,0.38,0.20,0.20,0.57,1.13],
    "India":[0.80,0.60,0.44,0.29,0.21,0.29,0.46],
}
MULT_COLORKEY = LONG_COLORKEY

# ---- Fig 09 : 2024 share of world GDP, two rulers (WDI country-sum) ----
SHARE24_ENT = ["United States","China","EU (27)","India","Japan","United Kingdom","Russia"]
SHARE24_NOM = [26.34,17.17,17.88,3.58,3.69,3.38,1.96]
SHARE24_PPP = [15.07,19.72,14.36,8.36,3.35,2.14,3.57]

# ---- Fig 11 : 2024 prosperity multiplier, two rulers ----
MULT24_ENT = ["United States","EU (27)","United Kingdom","Japan","Russia","China","India"]
MULT24_NOM = [6.23,3.20,3.93,2.40,1.10,0.98,0.20]
MULT24_PPP = [3.56,2.57,2.48,2.18,2.00,1.13,0.46]

# ---- Fig 10 : the 2024 ruler gap (nominal share - PPP share, percentage points) ----
# Positive = looks bigger on the nominal/market-rate ruler (high-price, strong-currency, dollar-denominated).
# Negative = lifted by PPP (low domestic prices, populous). Aligned to SHARE24_ENT then sorted desc.
GAP24_ENT = ["United States","EU (27)","United Kingdom","Japan","Russia","China","India"]
GAP24 = {e: round(SHARE24_NOM[SHARE24_ENT.index(e)] - SHARE24_PPP[SHARE24_ENT.index(e)], 2) for e in GAP24_ENT}

# ---- Fig 12 : population weight vs real-output weight, 2024 (the multiplier as geometry) ----
# x = share of world population %, y = share of world GDP (PPP) %. Diagonal y=x is parity (multiplier 1.0).
# Above the line => PPP output per person above the world average; below => under it.
POP24_ENT = ["United States","China","EU (27)","India","Japan","United Kingdom","Russia"]
POP24 = [4.23, 17.51, 5.59, 18.03, 1.54, 0.86, 1.78]   # share of world population, % (UN / WDI)
POP24_PPP = [SHARE24_PPP[SHARE24_ENT.index(e)] for e in POP24_ENT]
POP24_COLORKEY = {"United States":"us","China":"cn","EU (27)":"eu","India":"in",
                  "Japan":"jp","United Kingdom":"uk","Russia":"ru"}

# ---- Fig 13 : Japan, the warning label (nominal vs PPP share over time) ----
# The cleanest single illustration of the two-ruler thesis: the nominal "mountain"
# of the mid-1990s (super-yen + asset bubble) has no counterpart on PPP.
# Anchors: 1994 nominal peak ~18.2% [V]; 2024 PPP 3.35% [V]; PPP "never exceeded ~8%" [V].
# In-between points are benchmark estimates [E] consistent with WDI country-sum shape.
JP_YEARS = ["1990","1994","1998","2002","2006","2010","2014","2018","2024"]
JP_NOM   = [14.3, 18.2, 13.0, 12.0, 9.0, 8.6, 6.0, 5.8, 3.7]   # nominal share %, market rates
JP_PPP   = [7.9,  8.0,  7.0,  6.3,  5.6, 4.8, 4.4, 3.9, 3.35]   # PPP share %  (2024 = SHARE24_PPP); 1990 trimmed so the line honours prose "never crosses ~8%"

# ---- Fig 14 : multiplier arithmetic — why India is the swing variable ----
# Pure arithmetic from existing data: implied world-GDP share = population share x multiplier.
# Each entity's 2024 dot = POP24 x its 2024 PPP multiplier (lands on its actual PPP share).
# A small multiplier move on a huge population base re-slices the world; India has the steepest slope.
SWING_ENT = ["India","China","United States","EU (27)"]
SWING_POP = {e: POP24[POP24_ENT.index(e)] for e in SWING_ENT}            # population share, %
SWING_MULT24 = {e: MULT24_PPP[MULT24_ENT.index(e)] for e in SWING_ENT}   # 2024 PPP multiplier
SWING_COLORKEY = {"India":"in","China":"cn","United States":"us","EU (27)":"eu"}
SWING_XMAX = 5.0   # sweep assumed PPP multiplier 0 -> 5

# ---- IMF WEO 2025-26 marker (current snapshot; world nominal ~$126T) ----
# (entity, PPP share %, nominal $ trillions, nominal share %)
MARKER = [
    ("United States","14.54","32.38","25.64"),
    ("China","19.89","20.85","16.51"),
    ("India","8.49","4.15","3.29"),
    ("European Union","13.77","23.03","18.23"),
    ("EU + UK","15.89","27.30","21.62"),
    ("United Kingdom","2.12","4.26","3.37"),
    ("Japan","3.26","4.38","3.47"),
    ("Russia","3.38","2.66","2.11"),
]

# ---- Audit table (Kotkin's claims) ----
# (claim, ruler, ruler_class, verdict_html)
AUDIT = [
    ("US \u2248 25% of world GDP since ~1880","Nominal","nom",
     "<b>Holds.</b> Long-run average near a quarter; ~26% nominal in 2024\u201325, ~14.5% on PPP. The 2011 trough was ~21\u201323%, and the line has recovered since."),
    ("Postwar peak ~50% was the anomaly","Both","mix",
     "<b>Holds \u2014 and is more ruler-dependent than it sounds.</b> ~50% nominal in 1945 (a rubble artifact), ~40% nominal by 1960, but only ~27% on PPP around 1950. The \u201canomaly\u201d framing is exactly right."),
    ("Japan: ~18% \u2192 4%","Nominal","nom",
     "<b>Holds.</b> Peak ~18% in 1994\u201395 (super-yen + bubble); ~3.7% in 2024. On PPP, Japan never exceeded ~8% \u2014 most of the \u201cfall\u201d is currency unwinding plus slow growth."),
    ("Europe (incl. UK): ~30% (1992) \u2192 ~17%","Mixed","mix",
     "<b>Roughly holds, but blended.</b> The \u201c~17%\u201d matches PPP for Europe; nominal EU+UK today is closer to ~21%. The \u201c~30% in 1992\u201d is nominal. Two rulers in one sentence."),
    ("China \u2248 40% before the 1800s","PPP","ppp",
     "<b>High-end estimate.</b> Maddison\u2019s GDP peak for China is closer to a third (~33% in 1820). The bigger \u201c\u2248\u2153\u201340%\u201d figure is often the <i>manufacturing</i> share (Fig. 03), not GDP. Contested on level and timing."),
    ("US: 5% of population, 25% of GDP","Both","mix",
     "<b>Holds.</b> Multiplier \u2248 6 nominal, \u2248 3.6 PPP. (The US is ~4.2% of world population \u2014 so the per-capita lead is, if anything, understated by \u201c5%.\u201d)"),
    ("India left out of the story","PPP","ppp",
     "<b>The omission.</b> India was ~24% of world GDP in 1700, fell to ~3%, and is back to ~8% PPP \u2014 the 4th-largest economy by nominal size in 2025, yet at a multiplier of just ~0.46, a stage behind China."),
]

WORLD_NOMINAL_T = 126.3   # IMF WEO April 2026, 2026 projection, current US$
WORLD_PPP_T = 222.8       # IMF WEO April 2026, 2026 projection, current int$ (corrects the old 205)

# --- the three PPP lanes, kept as DISTINCT fields and never spliced ---
PPP_2026_CURRENT   = 222.8   # IMF 2026 marker, current international $ (present-day marker)
PPP_2024_CURRENT   = 195.0   # 2024, current international $ (modern snapshot, Fig 16)
PPP_2024_CONST2021 = 170.0   # 2024, WDI constant-2021 international $ (internal share/multiplier lane)
NOM_2026           = 126.3   # IMF 2026 marker, current US$
NOM_2024_WB        = 111.3   # World Bank 2024, current US$
NOM_2024_SUM       = 110.0   # report country-sum, 2024

# ===================================================================
#  AGGREGATES — the size of the whole pie (edition 6, Fig 15 & 16)
# ===================================================================
# Fig 15 : five centuries of the whole, in REAL terms (Maddison Project,
# constant 2011 international dollars, PPP). World population in billions,
# world real GDP in trillions of 2011 int'l-$. Benchmark years, ending at
# 2000 — deliberately NOT carried to 2024 in real units, and NOT spliced to
# the current-dollar modern totals in Fig 16 (different unit, different lane).
AGG_L_YEARS = ["1500","1600","1700","1820","1870","1913","1950","1973","2000"]
AGG_L_POP   = [0.44, 0.55, 0.60, 1.04, 1.27, 1.79, 2.54, 3.93, 6.15]   # billions (1500 aligned to B3 table = 0.44bn, Maddison)
AGG_L_GDP   = [0.43, 0.58, 0.64, 1.20, 1.92, 4.74, 9.25, 24.0, 58.0]   # trillions, 2011 int'l-$ PPP
# implied real GDP/person (int'l-$): ~860, 1055, 1070, 1150, 1510, 2650, 3640, 6110, 9430

# Fig 16 : the modern totals and the road to 2050, in CURRENT-dollar terms.
# Population (billions): actual 1900–2024, then UN WPP-2024 *median* projection.
# World GDP at current prices: nominal (current US$, WDI, from 1960) and PPP
# (current int'l-$, from 1990), in trillions. Two rulers at world scale.
AGG_M_POP_X    = [1900, 1925, 1950, 1975, 2000, 2024]
AGG_M_POP      = [1.65, 2.00, 2.54, 4.07, 6.15, 8.20]            # billions, actual
AGG_M_POP_PX   = [2024, 2035, 2050]
AGG_M_POP_PROJ = [8.20, 8.90, 9.70]                             # billions, UN WPP-2024 median
AGG_M_NOM_X    = [1960, 1980, 2000, 2010, 2024]
AGG_M_NOM      = [1.4, 11.3, 33.8, 66.0, 110.0]                 # world nominal GDP, current US$ tn
AGG_M_PPP_X    = [1990, 2000, 2010, 2024]
AGG_M_PPP      = [29.0, 46.0, 95.0, 195.0]                      # world PPP GDP, current int'l-$ tn
AGG_POP_2024 = 8.2    # billions
AGG_POP_2050 = 9.7    # billions, UN WPP-2024 median (peak ~10.3bn mid-2080s)
AGG_NOM_2024 = 110    # ~$110T nominal world GDP, 2024 (IMF)
AGG_PPP_2024 = 195    # ~$195T PPP world GDP, 2024 (IMF int'l-$)

# ===================================================================
#  THE LONG VIEW — speculative coda figures (17-22). Illustrative
#  scenario values (NOT forecasts) except demography (UN WPP 2024).
# ===================================================================

# Fig 18 - cone of outcomes: world PPP GDP share %, 2024->2050, (lo, mid, hi) envelopes
CONE_X = [2024, 2037, 2050]
# 2050 mouth of each fan is pinned to the [min, mean, max] of that economy's five
# SCEN_BARS scenarios (the caption promises the fan "spans the five scenarios");
# 2037 is the linear midpoint of the 2024 anchor and the 2050 mouth.
CONE = {
    "United States": [(15.1, 15.1, 15.1), (14.1, 14.7, 15.3), (13.0, 14.3, 15.5)],
    "China":         [(19.7, 19.7, 19.7), (19.6, 20.6, 22.1), (19.5, 21.4, 24.5)],
    "India":         [(8.4, 8.4, 8.4),    (9.0, 10.3, 12.0),  (9.5, 12.1, 15.5)],
}
CONE_CK = {"United States": "us", "China": "cn", "India": "in"}

# Fig 19 - 2050 PPP share % under each scenario (illustrative)
SCEN = ["Pull-Away", "Catch-Up", "Two Suns", "Archipelago", "Long Plateau"]
SCEN_BARS_ACTORS = ["United States", "China", "India", "Sub-Saharan Africa", "EU + UK", "Rest of World"]
SCEN_BARS = {
    "United States":      [15.5, 13.0, 15.0, 13.5, 14.5],
    "China":              [20.0, 22.0, 24.5, 21.0, 19.5],
    "India":              [9.5, 15.5, 12.0, 13.0, 10.5],
    "Sub-Saharan Africa": [3.5, 8.0, 5.0, 6.5, 4.5],
    "EU + UK":            [14.0, 13.0, 12.0, 12.5, 12.5],
    # Rest of World is the residual: 100 - (the five named actors), per scenario,
    # so every scenario column is an exhaustive partition that sums to exactly 100.
    "Rest of World":      [37.5, 28.5, 31.5, 33.5, 38.5],
}
SCEN_BARS_CK = {"United States":"us","China":"cn","India":"in","Sub-Saharan Africa":"ss","EU + UK":"eu","Rest of World":"row"}

# Fig 20 - demographic destiny: working-age (15-64) index, 2024=100 -> 2050 (UN WPP 2024 medium)
DEMO_X = [2024, 2030, 2035, 2040, 2045, 2050]
DEMO = {
    "Sub-Saharan Africa": [100, 118, 135, 153, 172, 193],
    "India":              [100, 106, 111, 115, 117, 117],
    "United States":      [100, 101, 102, 103, 104, 104],
    "EU + UK":            [100, 98, 96, 94, 92, 91],
    "China":              [100, 98, 96, 93, 90, 86],
    "Japan":              [100, 97, 93, 89, 85, 80],
}
DEMO_CK = {"Sub-Saharan Africa":"ss","India":"in","United States":"us","EU + UK":"eu","China":"cn","Japan":"jp"}

# Fig 21 - USD share of global FX reserves %, 2024->2050 (illustrative scenarios)
DOLLAR_X = [2024, 2030, 2035, 2040, 2045, 2050]
DOLLAR = {
    "status-quo-plus": [58, 57, 56.5, 56, 55.5, 55],
    "base drift":      [58, 55, 53, 51, 49, 48],
    "fragmentation":   [58, 54, 50, 46, 43, 40],
    "rupture":         [58, 56, 54, 50, 42, 30],
}

# Fig 22 - change in PPP multiplier (output/head vs world avg), 2024->2050, two AI cases (illustrative)
MULT_SHIFT_ACTORS = ["United States", "EU + UK", "India", "Sub-Saharan Africa"]
MULT_SHIFT = {
    "Concentrate": [0.55, 0.20, -0.05, -0.10],
    "Diffuse":     [0.05, 0.05, 0.45, 0.30],
}
MULT_SHIFT_CK = {"United States":"us","EU + UK":"eu","India":"in","Sub-Saharan Africa":"ss"}
