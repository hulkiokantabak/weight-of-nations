# HANDOFF — "The Shifting Weight of Nations," Seventh Edition (fused) → build pipeline

**Paste this into the Claude chat that holds the single-source build pipeline** (the data file + Chart.js interactive + WeasyPrint/PDF render + fonts) that produced the Sixth Edition PDF. The new prose manuscript travels with it as `the-shifting-weight-of-nations.md` (in the same zip).

---

## What this is

This is the **Seventh Edition** — a fusion of the Sixth Edition (the Claude data-essay you last built) with the reporting apparatus of the parallel GPT-5.5 Pro publication edition, plus a corrected IMF figure and a new speculative coda. The attached `.md` is the **complete, final prose + architecture**. Your job is to fold it into the single source of truth, update the data, build six new figures, and regenerate both the interactive and PDF editions.

**Do not re-edit the prose for content.** It has been through an editorial-pass (15 criteria) and a deep-thinkers logical sweep, and three panels (deep-thinkers, fx-experts, wisepersons) developed the coda. Treat the manuscript as final copy. Your work is the data layer, the figures, and the render.

---

## What changed vs the Sixth Edition (the build delta)

### 1. CORRECTION — world PPP total (this is the important one)
The Sixth Edition's world-PPP figure of **~$205T was wrong**. Verified directly against IMF WEO April 2026:

- **World GDP at PPP, 2026 projection = $222.8 trillion** (current international dollars).
  - Derivation/check: the US is the PPP numeraire, so US PPP GDP = US nominal = $32.38T; IMF US PPP share = 14.54%; 32.38 / 0.1454 = $222.8T. Cross-check via China (19.89% share, ~$43.7T) ≈ $220T.
- Update the data file's world-PPP total everywhere it feeds a figure or a denominator. Grep the project for `205` and purge any stale value.

### 2. The three PPP lanes — keep them explicitly separated, never spliced
The manuscript now distinguishes three PPP world totals by lane. Encode them as **distinct fields**, not one variable:

| Lane | Value | Use |
|---|---|---|
| IMF 2026, current int$ | **$222.8T** | the present-day marker (Fig 16, §1A, the new front-matter totals block, B2) |
| 2024, current int$ | **~$195T** | the modern snapshot ("the size of the whole," Fig 16 prose) |
| 2024, WDI constant-2021 int$ | **~$170T** | the **internal** share/multiplier arithmetic lane (B1 shares are computed here; ≈$195T in current terms) |

The B1 country-sum shares are anchored to the **constant-2021** lane (~$170T, ≈$195T current). The B2 marker is **current int$** ($222.8T). The render must never draw a single PPP line that crosses lanes.

### 3. NEW front-matter block — "The World This Essay Divides" (prose only, no new figure)
A short global-totals panel now sits right after "IN ONE LINE," before "How to Read." It states the three headline totals up front (people ~8.2bn; nominal $126.3T; PPP $222.8T; the ~$96T gap). Pure prose + one small table — no chart needed.

### 4. NEW speculative coda — "The Long View: Scenarios and Implications to 2050"
A major new part after §18 (Conclusions), before the appendices. It carries **six new figures (17–22)** that need new data series and chart code. **All six are illustrative/scenario figures, not measured data** — they must be visually and textually flagged as such (dashed envelopes, an "illustrative scenario — not a forecast" caption tag) to preserve the document's honesty discipline. Figure 20 is the exception: it is a near-deterministic demographic projection from UN WPP 2024 and can be labeled "projection (UN WPP 2024)" rather than "illustrative."

---

## The six new figures — specs for the data file + chart code

> Convention: keep the house style (oxblood `#993C1D` on warm paper; Fraunces display, IBM Plex Sans text, IBM Plex Mono labels; ruler labelled on every axis). Figures 17–19, 21, 22 carry an explicit **"illustrative scenario"** tag. Numbers below are **suggested illustrative values** — adjust for visual clarity; they are not claimed projections.

**FIGURE 17 — The scenario space (2×2 conceptual diagram, not a data plot).**
Build as an SVG/diagram. X-axis: the frontier *concentrates* (left) ↔ *diffuses* (right). Y-axis: the order *fragments* (bottom) ↔ *integrates* (top). Quadrant labels: top-left **Frontier Pull-Away**, top-right **The Great Catch-Up**, bottom-left **Two Suns**, bottom-right **Archipelago**. Centre overlay band: **The Long Plateau** (the low-productivity version of all four). No numeric data.

**FIGURE 18 — The cone of outcomes (fan chart).**
Y: world GDP share at PPP (%). X: 2024 → 2050. Three economies, each a shaded fan (min–max envelope across the five scenarios) with a central line. Illustrative envelopes for 2050 PPP share %: **US 12–16** (from ~15.1 in 2024; narrowest fan), **China 18–27** (from ~19.7), **India 9–16** (from ~8.4; widest upside). Label: "illustrative scenario envelopes, not forecasts."

**FIGURE 19 — 2050 PPP shares under each scenario (grouped bars).**
X: actors — US, China, India, Sub-Saharan Africa, EU+UK, Rest of World. Five bars each (Pull-Away / Catch-Up / Two Suns / Archipelago / Long Plateau). Set bar heights to match the directional arrows in the manuscript's scenario table (e.g., India and Africa swing widest between Pull-Away and Catch-Up; the US barely moves). Illustrative tag.

**FIGURE 20 — Demographic destiny (line chart; projection, UN WPP 2024).**
Y: working-age (15–64) population, indexed to 2024 = 100. X: 2024 → 2050. Lines (medium-variant, UN WPP 2024): **Sub-Saharan Africa** steep up (~+90–100%), **India** up (~+15–20%, peaking late-2040s), **United States** roughly flat (~+3–5%), **China** down (~−12 to −15%), **EU+UK** down (~−8 to −10%), **Japan** down most (~−18 to −22%). Label "projection (UN WPP 2024)" — this one is near-deterministic, not illustrative.

**FIGURE 21 — The dollar's reserve share to 2050 (line chart, scenarios).**
Y: USD share of global FX reserves (%). X: 2024 → 2050. Start ~58% (IMF COFER, 2024). Four lines: **status-quo-plus** (~55%), **base drift** (~48%), **fragmentation** (~40%), **rupture** (steeper, disorderly fall toward ~30%, drawn breaking late rather than gliding). Illustrative tag; note the rupture line is a low-probability tail.

**FIGURE 22 — Diffuse vs concentrate, on the multiplier (grouped bars or paired small-multiples).**
Change in PPP multiplier (output per head vs world average), 2024 → 2050, for **frontier** economies (US, EU) vs **catch-up** economies (India, Sub-Saharan Africa), under two cases. *Concentrate:* frontier bars positive, catch-up bars ~flat-to-negative (gap widens). *Diffuse:* catch-up bars strongly positive, frontier bars ~flat (gap narrows). Illustrative tag. The visual point is the reversal between the two panels.

---

## The verified data the pipeline should hold (confirm/update the data file)

**World totals**
- World nominal GDP, IMF 2026 = **$126.3T** ($126,295,331M). World nominal, World Bank 2024 = **$111.3T**; report country-sum ~$110T.
- World PPP: 2026 IMF **$222.8T** (current int$) · 2024 **~$195T** (current int$) · 2024 **~$170T** (constant-2021 int$, internal lane).
- Population (UN WPP 2024): **8.16bn** (2024) → **~9.66bn** (2050) → peak **~10.3bn** (mid-2080s) → **~10.18bn** (2100).

**IMF April 2026 marker (B2) — verified nominal; PPP shares from IMF DataMapper**
| Entity | PPP share % | Nominal $tn | Nominal share % |
|---|---|---|---|
| United States | 14.54 | 32.38 | 25.64 |
| China | 19.89 | 20.85 | 16.51 |
| India | 8.49 | 4.15 | 3.29 |
| EU | 13.77 | 23.03 | 18.23 |
| EU + UK | 15.89 | 27.30 | 21.62 |
| United Kingdom | 2.12 | 4.26 | 3.37 |
| Japan | 3.26 | 4.38 | 3.47 |
| Russia | 3.38 | 2.66 | 2.11 |

(World nominal $126.3T; world PPP $222.8T. Individually verified against Wikipedia's IMF-sourced lists / IMF DataMapper, April 2026 vintage.)

**2024 WDI country-sum (B1) — unchanged from the Sixth Edition; confirm against your data file**
US 26.34 nom / 15.07 PPP / 4.23 pop → ×6.23 / ×3.56 · China 17.17 / 19.72 / 17.51 → ×0.98 / ×1.13 · EU-27 17.88 / 14.36 / 5.59 → ×3.20 / ×2.57 · EU-27+UK 21.25 / 16.49 / 6.45 · UK 3.38 / 2.14 / 0.86 · India 3.58 / 8.36 / 18.03 → ×0.20 / ×0.46 · Japan 3.69 / 3.35 / 1.54 · Russia 1.96 / 3.57 / 1.78 → ×1.10 / ×2.00.

**Centuries table (B3) — unchanged** (Maddison-style, 1990 int$): 1500 0.44bn/$0.25T · 1700 0.60bn/$0.37T · 1820 1.04bn/$0.69T · 1870 1.27bn/$1.11T · 1913 1.79bn/$2.73T · 1950 2.53bn/$5.34T · 1973 3.92bn/$16.02T · 2000 6.15bn/$36.69T · 2008 6.71bn/$50.97T.

---

## Build invariants (unchanged — re-state for the render)

- **Single source of truth.** Same numbers, same prose render twice — interactive Chart.js + typeset PDF. Every figure drawn from the data file, never hand-placed.
- **Lanes never spliced.** Maddison (deep history) / WDI country-sum (modern) / IMF 2026 (marker) / UN WPP (population) stay on separate scales. No continuous 1500→2026 line.
- **Ruler on every figure.** Nominal vs PPP labelled; uncertainty noted where it bites (PPP ±5–10%; pre-1900 reconstructions).
- **Figures 17–22 are speculative** (except 20). Visually + textually flag them so they are not mistaken for measured data — this is load-bearing for the document's credibility.
- **Typography.** Fraunces display/italic, IBM Plex Sans text, IBM Plex Mono labels; oxblood `#993C1D` on warm paper.
- **Verify after build:** figure count = 22 + 3 tables; grep for stale `205`; confirm B1 (constant-2021) and B2 ($222.8T current) totals are distinct fields; spot-check that no PPP figure crosses lanes.

---

## Suggested first message to that chat

> "Updating our data-essay to the Seventh (fused) edition. Attached is the final prose manuscript. Please (1) update the data file: world PPP 2026 = $222.8T (correcting the old $205T), and split the three PPP lanes into distinct fields per the handoff; (2) build six new figures (17–22) for the new speculative coda using the specs in the handoff, flagging 17–19/21/22 as illustrative scenarios and 20 as a UN WPP projection; (3) regenerate the interactive Chart.js page and the PDF from the single source; (4) run the verify checklist. Don't re-edit the prose — it's final."
