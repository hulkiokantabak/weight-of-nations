# Claim registry

*A ruler-labeled, source-aware registry of public macro-historical claims about national
economic weight — and this project's verdict on each. The essay began as a response to claims
from a Stephen Kotkin / Hoover* Uncommon Knowledge *conversation; this registry generalises that
into a standing "public correction engine": any claim of the form "country X is Y% of world
GDP" can be entered, labeled by ruler, and adjudicated against a dated source.*

*This file is the human-readable registry; the same rows live as structured data in `data.py`'s
`AUDIT` field and can be exported to `claims.csv` for machine use. Seeded 2026-06-01 from the
eighth-edition audit table.*

## Schema

Each claim carries: `claim_id` · `claim_text` · `source` · `date` · `entity` · `period` ·
**`ruler_required`** (nominal / PPP / population / multiplier / bloc) · `dataset` ·
`latest_value` · **`verdict`** · `notes` · `last_checked`.

The non-negotiable field is **`ruler_required`**: no claim is adjudicated without naming the
ruler it implicitly uses. A claim true on one ruler is routinely false on another — that is the
whole point of the project.

---

## Seed entries (from the eighth-edition audit)

### KOTKIN-US-25 · "The US is ~25% of world GDP since ~1880"
- **ruler:** nominal current-dollar · **dataset:** WDI / IMF · **last_checked:** 2026-06
- **verdict — Holds.** Long-run average near a quarter; ~26% nominal in 2024–25, ~14.5% on PPP.
  The 2011 trough was ~21–23%, and the line has recovered since.

### POSTWAR-PEAK-50 · "The postwar peak of ~50% was the anomaly"
- **ruler:** both (nominal vs PPP) · **dataset:** Maddison / WDI · **last_checked:** 2026-06
- **verdict — Holds, and is more ruler-dependent than it sounds.** ~50% nominal in 1945 (a
  rubble artifact), ~40% nominal by 1960, but only ~27% on PPP around 1950. The "anomaly"
  framing is exactly right.

### JAPAN-18-4 · "Japan went from ~18% to ~4% of world GDP"
- **ruler:** nominal current-dollar · **dataset:** WDI · **last_checked:** 2026-06
- **verdict — Holds as a market-weight story; misleading as real-output collapse.** Peak ~18%
  in 1994–95 (super-yen + bubble); ~3.7% in 2024. On PPP, Japan never exceeded ~8% — most of
  the "fall" is currency unwinding plus slow growth.

### EUROPE-30-17 · "Europe (incl. UK) went from ~30% (1992) to ~17%"
- **ruler:** mixed (the sentence blends two) · **dataset:** WDI · **last_checked:** 2026-06
- **verdict — Roughly holds, but blended.** The "~17%" matches PPP for Europe; nominal EU+UK
  today is closer to ~21%. The "~30% in 1992" is nominal. Two rulers in one sentence.

### CHINA-40-PRE1800 · "China was ~40% of world output before the 1800s"
- **ruler:** PPP · **dataset:** Maddison / Bairoch · **last_checked:** 2026-06
- **verdict — High-end estimate.** Maddison's GDP peak for China is closer to a third (~33% in
  1820). The bigger "~⅓–40%" figure is often the *manufacturing* share (Fig 03), not GDP.
  Contested on level and timing.

### US-5POP-25GDP · "The US is 5% of population but 25% of GDP"
- **ruler:** both (the claim *is* a multiplier) · **dataset:** WDI / UN · **last_checked:** 2026-06
- **verdict — Holds.** Multiplier ≈ 6 nominal, ≈ 3.6 PPP. (The US is ~4.2% of world population —
  so the per-capita lead is, if anything, understated by "5%.")

### INDIA-OMITTED · "India is left out of the story"
- **ruler:** PPP · **dataset:** Maddison / WDI · **last_checked:** 2026-06
- **verdict — The omission.** India was ~24% of world GDP in 1700, fell to ~3%, and is back to
  ~8% PPP — the 4th-largest economy by nominal size in 2025, yet at a multiplier of just ~0.46,
  a stage behind China.

---

## How to add a claim (for future sessions / contributors)

1. Assign a `claim_id` (`SOURCE-ENTITY-SHORT`). Quote the `claim_text` verbatim.
2. **Name the `ruler_required`** — the single most important field. If the claim is ambiguous
   between rulers, say so and adjudicate each.
3. Cite the `dataset` and a dated `latest_value` from `docs/source-research.md` (never from
   memory).
4. Write a `verdict` that leads with Holds / Misleading / False / Contested, then the ruler
   reason.
5. Update `data.py`'s `AUDIT` field so the registry and the rendered audit table stay in sync;
   re-run the consistency suite; rebuild.
6. Set `last_checked` and commit.

*A claim's verdict can change as data is revised — that is expected. Update the `latest_value`
and `last_checked`, keep the history.*
