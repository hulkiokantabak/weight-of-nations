# LOG — catches & standing rules

*Every error caught on this project, what it was, how severe, how it was resolved, and the
standing rule it produced. A catch that implies a rule is escalated into a `data.py` consistency
check or an orchestrator invariant — a learning that lives only in prose has not yet shaped
behaviour. Comprehensive catch-by-catch tracking begins with the eighth edition (the first
living edition); pre-repository catches from earlier editions are recorded from the changelog
where known.*

**Severity scale:** 1 = cosmetic · 2 = minor (wording/label) · 3 = real but caught pre-build ·
4 = would mislead a careful reader · 5 = would ship wrong numbers.

**Status legend:** ✅ resolved · 🔒 now enforced by a check or invariant.

---

## Eighth edition — finalisation pass (2026-06-01)

The four-pass finalisation surfaced ten catches, all in the coda **data layer**; none in the
analytical prose. The four load-bearing ones:

| # | Catch | Sev | Where | Resolution | Standing rule |
|---|---|---|---|---|---|
| C-01 | **Cone vs bars mismatch.** Fig 18 (cone of outcomes) and Fig 19 (2050 scenario bars) implied different US ranges (~12–16% vs ~13–15.5%). *Author's own catch.* | 4 | charts/data | Cone redrawn so each country's 2050 fan is exactly `(min, mean, max)` of its five Fig 19 bars. | 🔒 Invariant 5 + suite check: cone = envelope of bars. |
| C-02 | **Scenario columns did not sum to 100%.** Fig 19 named-actor shares plus residual did not total 100% in every scenario. | 4 | data | "Rest of World" made the computed residual per scenario (`[37.5, 28.5, 31.5, 33.5, 38.5]`); columns now sum to 100%. | 🔒 Invariant 6 + suite check: `scenario sum {sc}` = 6 actors sum to 100. |
| C-03 | **Japan PPP line crossed its stated ceiling.** The prose says Japan's PPP share "never crosses ~8%," but `JP_PPP[1990]` sat above 8. | 4 | data | `JP_PPP[1990]` trimmed to **7.9** (series max 8.0) so the rendered line honours the prose. | 🔒 source-research note; verified anchors `[V]`. |
| C-04 | **Deep-history population/share figure out of step with its table.** A 1500-benchmark long-run figure did not align to its own table. | 3 | data | Aligned to the table; long-run shares re-checked to sum to 100% per year. | 🔒 Suite check 3: `LONG sum {yr}` ≈ 100% (±0.15). |

The remaining six catches were minor coda-data alignments (scenario-bar y-axis limits and
tick spacing, the common 2024 origin of all paths, and cross-figure label consistency),
resolved in the same data-layer pass and now covered by the suite's "all paths start at 58%"
and cross-figure checks. **No analytical prose changed.** Suite after the pass: **52 passed,
0 failed.**

---

## Seventh edition — fusion & IMF correction (2026-06-01, prior chat)

| # | Catch | Sev | Resolution | Standing rule |
|---|---|---|---|---|
| C-05 | **World PPP denominator wrong.** Sixth edition carried world PPP ≈ **$205T**. | 5 | Verified against IMF WEO April 2026 and corrected to **$222.8T** (US PPP numeraire: $32.38T ÷ 14.5% US share). | 🔒 Invariant 8 + `source-research.md` records the arithmetic so it is re-checked, not re-guessed. |
| C-06 | **Two denominator-lane labels misattributed.** Two figures' totals were labelled to the wrong PPP lane. | 4 | Aligned both to the constant-2021 lane. | 🔒 Invariant 2: three PPP lanes are distinct fields, never spliced. |
| C-07 | **Growth-multiple inconsistent with the centuries table.** One stated growth multiple disagreed with the long-run table. | 3 | Corrected to **fourteenfold** to match the table. | 🔒 Cross-figure consistency now in the suite. |

---

## Earlier editions (pre-repository)

Edition 4 ("Global GDP share shifts from 1600s to present," 2026-05-31) hit the platform's
**100-image / PDF-render limit** mid-build — not a data error but an operational one. It
produced the project's most consequential operational rule:

| # | Event | Sev | Resolution | Standing rule |
|---|---|---|---|---|
| O-01 | Chat hit the render-image ceiling mid-build; work at risk of being stranded in one chat. | — | Bundled all source + outputs + verified numbers + skills and handed off to a fresh chat via `HANDOFF.md`. | 🔒 Continuity discipline: bundle-as-portable-memory, `HANDOFF.md` entry point, past-chat-search reflex (now in `weight-of-nations` §6 and the `project-continuity` skill). |

Catch-by-catch logs for editions 1–6 were not kept in a single tracker; their corrections are
folded into the prose and the changelog. From the eighth edition onward, every catch is logged
here.

---

## How to add a catch (for future sessions)

1. Add a row: id, one-line description, severity, where found, resolution.
2. If it implies a rule, **escalate**: add a check to `check_consistency.py` *or* an invariant
   to the `weight-of-nations` orchestrator, and mark the row 🔒.
3. Bump the catch count in `docs/METRICS.md`.
4. Commit with a message naming the catch.
