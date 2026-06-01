# source-research.md — the verified numbers

*The decided memory of the project's data. Recorded so no future session re-derives or
hallucinates a figure. When refreshing the data, copy from here (and from the cited source),
never from memory. `[V]` = verified against source; `[E]` = benchmark estimate, wide bands.*

Last verified: **2026-06-01** against **IMF WEO April 2026** ("Global Economy in the Shadow of
War") and **World Bank WDI 2024**. Update the date and the changed rows on each refresh; keep
historical entries unless a source outright contradicts them.

---

## World totals

| Quantity | Value | Source | Tag |
|---|---|---|---|
| World population, 2026 | ~8.2 billion | UN WPP 2024 | [V] |
| World GDP, nominal, 2026 | **$126.3T** (current US$) | IMF WEO Apr 2026 | [V] |
| World GDP, PPP, 2026 | **$222.8T** (current int$) | IMF WEO Apr 2026 | [V] |
| World GDP, nominal, 2024 | $111.3T (current US$) | World Bank WDI | [V] |
| Nominal↔PPP world gap, 2026 | ~$96T | derived (222.8 − 126.3) | [V] |

**The IMF $222.8T verification (the seventh-edition correction).** The US is the PPP numeraire,
so its PPP GDP equals its nominal GDP, $32.38T. At the IMF's stated US PPP share of 14.5%, the
world PPP total is 32.38 / 0.145 = **$222.8T**. This corrected the sixth edition's erroneous
~$205T. Recorded so the arithmetic can be re-checked, not re-guessed.

## The three PPP lanes (NEVER spliced — orchestrator invariant 2)

| Lane | Value | Meaning |
|---|---|---|
| 2026 current int$ | **$222.8T** | present-day marker (IMF WEO Apr 2026) |
| 2024 current int$ | **~$195T** | 2024 in current international dollars |
| 2024 constant-2021 int$ | **~$170T** | the internal arithmetic lane (WDI constant-2021) |

## 2024 country shares — WDI country-sum (the B1 anchors)

| Entity | Nominal share % | PPP share % | Population share % |
|---|---|---|---|
| United States | 26.34 | 15.07 | 4.23 |
| China | 17.17 | 19.72 | 17.51 |
| EU (27) | 17.88 | 14.36 | 5.59 |
| India | 3.58 | 8.36 | 18.03 |
| Japan | 3.69 | 3.35 | 1.54 |
| United Kingdom | 3.38 | 2.14 | 0.86 |
| Russia | 1.96 | 3.57 | 1.78 |

All `[V]` against WDI 2024. These drive Figs 07, 09, 10, 11, 12, 14 and tables B1–B3.

## 2024 prosperity multipliers (share ÷ population share)

| Entity | Nominal mult | PPP mult |
|---|---|---|
| United States | 6.23 | 3.56 |
| EU (27) | 3.20 | 2.57 |
| United Kingdom | 3.93 | 2.48 |
| Japan | 2.40 | 2.18 |
| Russia | 1.10 | 2.00 |
| China | 0.98 | 1.13 |
| India | 0.20 | 0.46 |

Derived from the shares and population above; the consistency suite checks
`multiplier ≈ share / population` to ±0.03.

## Japan, the warning label (Fig 13)

- 1994 nominal peak: **~18.2%** [V]
- 2024 PPP share: **3.35%** [V] (= SHARE24_PPP)
- PPP share **never exceeded ~8%** [V] — so `JP_PPP[1990]` is set to **7.9** (trimmed from a
  prior 8.x so the rendered line honours the prose; max in the series is 8.0).

## Deep history & manufacturing (slow / fixed lanes)

- Long-run PPP shares (Figs 01/02/08): **Maddison Project Database 2023**. Benchmark years
  1500–2024; reconstructions with wide error bars `[E]`. Suite checks each year's shares sum to
  100% (±0.15).
- Manufacturing-output shares (Fig 03): **Bairoch**, 1750–1900. **Fixed historical — do not
  update.**

## Scenario coda (Figs 17–22) — ILLUSTRATIVE, NOT A DATA FEED

Author/panel-set scenario values; not sourced from any release and not refreshed by a new WEO.
Recorded so the consistency relationships are preserved on any future analytical edition:

- All five 2050 scenario paths share a common 2024 origin (the suite checks "all paths start
  at 58%" for the aggregate, and each country's cone begins at its 2024 value).
- **Cone (Fig 18) = envelope of the five scenario bars (Fig 19)** per country: the 2050 fan is
  exactly `(min, mean, max)` of that country's bars.
  - US: bars → fan `(13.0, 14.3, 15.5)`; China `(19.5, 21.4, 24.5)`; India `(9.5, 12.1, 15.5)`.
- **Each scenario column sums to 100%** with a residual "Rest of World" (Fig 19 RoW across the
  five scenarios = `[37.5, 28.5, 31.5, 33.5, 38.5]`).

## Sources & URLs (full list in manuscript Appendix C)

| Source | URL / identifier |
|---|---|
| IMF WEO April 2026 | imf.org/en/publications/weo/issues/2026/04/14 |
| IMF DataMapper (PPPSH, NGDPD, PPPGDP, LP) | imf.org/external/datamapper (@WEO) |
| World Bank WDI — nominal | data.worldbank.org/indicator/NY.GDP.MKTP.CD |
| World Bank WDI — PPP (constant 2021 int$) | databank.worldbank.org — NY.GDP.MKTP.PP.KD |
| World Bank WDI — population | databank.worldbank.org — SP.POP.TOTL |
| World Bank ICP methodology | worldbank.org/en/programs/icp/methodology |
| UN World Population Prospects 2024 | population.un.org/wpp |
| Maddison Project Database 2023 | rug.nl/ggdc/historicaldevelopment/maddison |
| Bairoch (manufacturing) | "International Industrialization Levels from 1750 to 1980" |
| Hoover inspiration | *Uncommon Knowledge*, Hoover Institution (guest Stephen Kotkin, host Peter Robinson) |

*Scholarly context used in interpretation: the Great Divergence debate (Pomeranz; Broadberry et
al.), industrialisation/manufacturing-share histories, the middle-income transition literature,
the Balassa–Samuelson framework, and Frankel's rule on matching the ruler to the question.*
