---
name: weight-of-nations-data-refresh
description: >
  The data-update ritual and source map for "The Shifting Weight of Nations" living essay.
  USE whenever the essay's numbers need refreshing for a new data release or an annual update:
  a new IMF World Economic Outlook (April or October), a World Bank WDI refresh, a UN World
  Population Prospects revision, or a Maddison Project update — or when the author says "refresh
  the data," "update the numbers," "new IMF/WEO/WDI/UN release," "annual update," "re-run the
  living document," or asks which figure comes from which source. Gives the field-by-field map
  from build/data.py to its source, the verified-vs-estimate discipline, the exact update
  ritual (edit data.py ONLY → re-run the 52-check suite → rebuild three editions → decide
  decimals-vs-direction → version-bump → commit/PR), and the rule that prose changes only when
  a direction changes. Companion to the weight-of-nations orchestrator and the
  weight-of-nations-panel; pairs with build/update_data.py and .github/workflows/living-update.yml.
---

# weight-of-nations-data-refresh — keeping the numbers current without moving the argument

The living property of this essay is **narrow on purpose**: refreshing it touches only
`build/data.py`. The prose is a method and a set of *directions*; those do not expire when a
denominator is revised. This skill is the ritual and the source map that make the refresh safe.

---

## 1 · The sources and their cadence

| Source | What it feeds | Release cadence | URL |
|---|---|---|---|
| **IMF WEO** (World Economic Outlook + DataMapper) | World nominal & PPP totals; present-day country markers; PPP shares | **April and October**, each year | imf.org/en/publications/weo · imf.org/external/datamapper |
| **World Bank WDI** | 2024-era nominal & PPP country shares (the B1 anchors), population shares, world nominal | Roughly **annual, mid-year**; revised continuously | data.worldbank.org · databank.worldbank.org |
| **UN WPP** | Population shares, projections to 2050 / peak / 2100 (Fig 20) | Roughly **every 2 years** (2022, 2024, …) | population.un.org/wpp |
| **Maddison Project** | Deep-history PPP shares 1500–2000 (Figs 01/02/08) | **Every few years** (2020, 2023, …) | rug.nl/ggdc/historicaldevelopment/maddison |
| **Bairoch** | Manufacturing-output shares 1750–1900 (Fig 03) | **Fixed historical** — does not change | (citation in Appendix C) |

The two that move most often, and matter most, are **IMF WEO** (twice a year) and **WDI**
(annually). Maddison and Bairoch are slow or fixed history — touch them only on a real
methodological revision.

---

## 2 · The field map — data.py → source

Edit only the field; never the rendered editions. `[V]` = verified against source; `[E]` =
benchmark estimate (keep the tag; an estimate must never be silently promoted to verified).

| data.py field(s) | Figure(s) | Source lane | Refresh trigger |
|---|---|---|---|
| `WORLD_NOMINAL_T`, `WORLD_PPP_T` | front-matter totals | IMF WEO (current $) | every WEO |
| `PPP_2026_CURRENT`, `PPP_2024_CURRENT`, `PPP_2024_CONST2021` (the three lanes) | totals / methodology | IMF (current) + WDI (constant-2021) | WEO / WDI |
| `MARKER` | present-day marker | IMF WEO DataMapper | every WEO |
| `SHARE24_NOM`, `SHARE24_PPP` (the B1 anchors) | Figs 07, 09, 10, 11, 14 | WDI country-sum, 2024 | WDI |
| `MULT24_NOM`, `MULT24_PPP` | Figs 11, 14 | derived from shares ÷ population | WDI |
| `POP24`, `POP24_PPP` | Figs 12, 14 | UN WPP / WDI population | WPP / WDI |
| `DELTA_NOM`, `DELTA_PPP` | Fig 07 | WDI, 1990→2024 deltas | WDI |
| `NOM`, `WEST_BLOC_NOM`, `US_NOM` | Figs 04, 05 | WDI-shape nominal series + benchmark `[E]` | WDI (recent points only) |
| `BLOC` | Fig 06 | WDI country-sum, both rulers | WDI |
| `MULT` | Fig 08 | Maddison-based multiplier over time | Maddison |
| `LONG`, `YEARS_LONG` | Figs 01, 02 | Maddison benchmark years | Maddison (rare) |
| `MFG`, `YEARS_MFG` | Fig 03 | Bairoch | fixed (do not touch) |
| `JP_NOM`, `JP_PPP` | Fig 13 | WDI anchors `[V]` + benchmark `[E]` | WDI (endpoints) |
| `CONE`, `SCEN_BARS`, `SCEN`, `AGG_L_POP`, `DEMOG_*`, `DOLLAR_*`, `MULT_SHIFT_*` (coda) | Figs 17–22 | **illustrative — author/panel set, not a data feed** | only on a new analytical edition |
| `AUDIT` | the claims table | author's verdicts | only if a claim's verdict changes |

**Derived fields recompute themselves** — `GAP24`, the `SWING_*` family, the cone midpoints,
the `SCEN_BARS` "Rest of World" residual — so update their *inputs*, not the derived value.
The consistency suite enforces this; if you hand-type a derived value it will go red.

---

## 3 · The refresh ritual

1. **Stage the new numbers in `docs/source-research.md` first**, with the source, the vintage,
   and the URL. Never edit `data.py` from memory — copy from the recorded source. Mark `[V]`.
2. **Edit `build/data.py` only.** Change the inputs that moved; leave derived fields alone.
   Use `build/update_data.py` for the structured fields (it validates types and ranges).
3. **Re-run the suite:** `cd build && python3 check_consistency.py`. Expect `52 passed, 0
   FAILED`. A red check **blocks** the build — fix the data, not the check (unless the check
   itself encoded a now-obsolete assumption, in which case escalate to the orchestrator).
4. **Rebuild the three editions:** `python3 build_pdf.py && python3 build_html.py &&
   python3 build_audio.py`. (Re-run `parse_manuscript.py` **only if prose changed** — for a
   pure data refresh it did not.)
5. **Decide: decimals or direction?**
   - *Decimals only* (every direction in the prose still holds) → bump the **patch** version
     (e.g. v8.0 → v8.1), update `docs/METRICS.md` and `docs/LOG.md`, commit, done.
   - *A direction changed* (a plateau became a decline; a laggard began to converge; a ruler
     crossover flipped) → **stop.** This is a new analytical edition. Route it through
     `weight-of-nations-panel`, let the author ratify the prose change, then re-parse, rebuild,
     bump the **edition** number, and commit.
6. **Commit / open a PR.** The GitHub Action opens a PR rather than committing blind, so a
   human ratifies before publication. Push to the project repo.

---

## 4 · The discipline (why this stays honest)

- **Directions, not decimals.** The test for "does the prose change?" is never "did a number
  move?" — it is "did a *direction* move?" Most refreshes are decimals; the prose stands.
- **Two rulers, three lanes, never spliced.** A WEO current-$ PPP total never overwrites the
  constant-2021 lane, and vice-versa. Keep `PPP_2026_CURRENT`, `PPP_2024_CURRENT`, and
  `PPP_2024_CONST2021` as three separate fields forever (orchestrator invariant 2).
- **No decimal exceeds its source.** PPP carries ±5–10%; deep history has wide bands. If a new
  release reports more precision than the lane can bear, round to what the lane supports.
- **Estimates stay estimates.** A `[E]` benchmark point becomes `[V]` only when a real source
  confirms it. Never quietly promote.
- **The coda is not a data feed.** Figures 17–22 are illustrative scenarios; a new WEO does not
  "update" them. They move only when the author and panel revise the analytical edition.
- **Audit trail.** Every refresh leaves a trace: a `source-research.md` entry (the new number),
  a `LOG.md` line (what moved), a `METRICS.md` bump (the version), and a commit message.

---

## 5 · Quick checklist

```
[ ] New numbers recorded in docs/source-research.md (source + vintage + URL, [V])
[ ] build/data.py inputs updated (derived fields left alone)
[ ] check_consistency.py → 52 passed, 0 FAILED
[ ] three editions rebuilt clean (parse only if prose changed)
[ ] decimals-or-direction decided; panel convened if a direction moved
[ ] version/edition bumped; METRICS.md + LOG.md updated
[ ] committed / PR opened; pushed to the project repo
```
