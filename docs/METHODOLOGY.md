# METHODOLOGY — *The Shifting Weight of Nations*

*How this essay was made, edition by edition, and the disciplines that carried across them.
Written so a new chair can understand not just the current state but the path that produced it.
The procedural rules live in the `weight-of-nations` orchestrator skill; this document is the
narrative and the rationale behind them.*

---

## 1 · What the essay is, and why it exists

The essay began from a public conversation on the Hoover Institution's *Uncommon Knowledge*
(guest Stephen Kotkin, host Peter Robinson) about the changing economic weight of nations. The
brief was never to transcribe or to debunk it, but to take its memorable GDP-share claims
seriously and **test them against the data, ruler by ruler.**

The thesis that emerged is the spine of every edition: a nation's share of world GDP is not one
number but three multiplied together — its share of the world's **people**, its **price level**
(the ruler you measure with), and its **productivity** (output per person relative to the
world). Strip away population and the price-level ruler, and five centuries of rise, fall, and
"re-convergence" collapse onto a single variable — productivity — which is also the only one
that will decide the next fifty years. Readers (and pundits) switch silently between two rulers,
market-rate **nominal** and price-adjusted **PPP**, and between *size* and *prosperity*; the
essay's job is to separate them and keep them separated.

The reading rule, carried in every edition: **read the ruler first, the direction second, and
the decimal point last.**

---

## 2 · The single-source-of-truth method

From the fourth edition onward the essay has been generated, not hand-written, from one source:

- **`build/data.py`** — every number and the colour palette. The only place numbers live.
- **the manuscript** (`manuscript/the-shifting-weight-of-nations.md`) — all prose, parsed by
  `build/parse_manuscript.py` into **`build/content.py`** (auto-generated; never hand-edited).
- **`build/charts.py`** — 22 figure renderers, drawn from `data.py`.
- three builders — **`build_pdf.py`** (WeasyPrint, typeset print), **`build_html.py`**
  (Chart.js, interactive), **`build_audio.py`** (a screen-reader / TTS edition).

The golden rule: **you never hand-edit a rendered edition.** Change a number once in `data.py`,
or a sentence once in the manuscript, re-run the builders, and all editions follow — so the
three formats can never drift. This is the property that later made the document *livable*: if
the editions are pure functions of one source, then keeping the essay current is just keeping
one file current.

---

## 3 · Edition history

The essay evolved across separate conversations, each prompted by the author re-introducing a
competitor-LLM draft of the same brief and asking to keep Claude's logic and voice as the spine
while absorbing the best of the others and going deeper. The lineage:

- **Editions 1–3 — the argument and the first panels.** The two-ruler thesis, the multiplier,
  and the productivity spine were established and first panel-reviewed. ~10 figures; static
  documents rebuilt by hand.

- **Edition 4 — the build pipeline.** *(chat: "Global GDP share shifts from 1600s to present,"
  2026-05-31.)* The single-source-of-truth pipeline was built — `data.py`, `content.py`,
  `build_html.py`, `build_pdf.py`, the bundled fonts — turning the essay from a hand-assembled
  document into a generated one. Ten live figures; ~20-page PDF; world PPP carried as ~$205T
  (later found to be an error). This chat hit the platform's 100-image / PDF-render limit, which
  is why the project learned to hand off between chats via a bundle and a `HANDOFF.md` — the
  first appearance of the continuity discipline that now governs the living document.

- **Editions 5–6 — deepening.** The analysis was extended and the prose matured; the figure
  count grew toward sixteen.

- **Edition 7 — the fusion and the IMF correction.** *(chat: "Comparing LLM essays on global GDP
  and population," 2026-06-01.)* Two parallel "final" editions — Claude's sixth-edition spine and
  a GPT-5.5 Pro publication edition — were fused. The merge was deliberately **asymmetric**: the
  spine, prose, and original analysis are Claude's; the reporting apparatus (an up-front
  denominator section, the full PPP strengths-and-limits chapter, the source-lane methodology,
  the bibliography with URLs, and the provenance trail) was ingested from the GPT draft where it
  strengthened defensibility, while that draft's scaffolding bloat and redundant tables were
  left out. Because Claude was the author of one of the two documents, the comparison that drove
  the fusion was run as **designed disagreement** (a `deep-thinkers` roundtable in full-panel
  posture, with adversarial voices deliberately assigned to attack Claude's own essay and defend
  the other), and the conflict of interest was disclosed rather than hidden. Five independent
  evaluations (ChatGPT, Gemini, Grok, DeepSeek, and Claude's own panel) converged on the same
  finding: Claude produced the stronger *essay*, GPT the stronger *dossier* — and the ranking
  flips between evaluators traced entirely to weighting assumptions about the artifact's purpose,
  not to disagreement about the documents. The material correction came out of this scrutiny:
  the world PPP figure was verified directly against **IMF WEO April 2026** and corrected from
  **~$205T to $222.8T**. The three PPP lanes were made explicit and never-spliced; a global-
  totals block ("The World This Essay Divides") was surfaced up front; and a speculative coda —
  *The Long View: Scenarios and Implications to 2050* — was added, developed through **three
  designed-disagreement panels** (`deep-thinkers`, `fx-experts`, `wisepersons`) at five rounds
  each, lifting the figure count from 16 to 22.

- **Edition 8 — finalisation and the living document.** *(this conversation, 2026-06-01.)* The
  document was finalised and migrated to a code-first, self-updating architecture. See §4–§6.

**The arc, across models.** The project ran from **Sunday, 31 May 2026** across **nine
conversations and five models** — five Claude chats (the fifth being this finalisation-and-
migration session) plus four other-LLM lines (GPT-5.5 Pro, Gemini, Grok, DeepSeek). The shape
was: four initial LLM synthesis documents from a shared brief; several iterated versions, with
ChatGPT and Claude carrying the deepest authoring; and a final line that culminated with
Claude, whose spine and prose are the canonical essay's and whose ingested reporting apparatus
came from the GPT line. The full cross-model accounting — prompts, output volume, and the
provenance of every figure — is in `docs/METRICS.md` §5.

---

## 4 · The eighth edition: finalisation

Two things happened, in order.

**A four-pass finalisation.** The whole document was put through four review passes, each a
designed-disagreement panel in which the chair synthesises but does not vote:

1. **Logic & mathematics** — a logic economist and a quantitative analyst swept the identity
   arithmetic and every numerical claim.
2. **Figures, between and within** — two figure-literate reviewers checked every chart against
   every other and against its own internal logic. This pass began from the author's own catch:
   that the cone of outcomes (Fig 18) and the 2050 scenario bars (Fig 19) appeared to disagree
   about the US range.
3. **Literary** — an extended-masters pass on voice and cadence.
4. **Editorial** — the fifteen-criterion editorial pass (consistency, cross-references,
   typography, front/back matter, no-decimal-exceeds-its-source).

These passes surfaced **ten catches, all in the coda data layer** — none in the analytical
prose, which was already final copy. The catches were corrected in `data.py` only; the four
load-bearing ones are recorded in `LOG.md`. The prose did not change, because the coda speaks in
*directions*, not point forecasts.

**A 52-check consistency suite.** The relationships the document relies on were encoded as a
machine-readable suite (`build/check_consistency.py`) that imports `data.py` and asserts each
one: the multiplier identity (share ÷ population), the ruler gap, the long-run shares summing to
100% per benchmark year, the swing dots landing on actual 2024 shares, the Fig 08 long-run
multiplier endpoint matching the Fig 11 cross-section, the cone-as-envelope-of-bars relation,
and the scenario columns summing to 100%. The suite runs **before every build** and currently
reports **52 passed, 0 failed**. Every future catch that implies a rule is escalated into a new
check, so the document's defences grow monotonically.

---

## 5 · The eighth edition: migration to a living document

The finalised essay was moved into a public, version-controlled repository whose three editions
are pure functions of one source. The mechanism that keeps it current is deliberately **narrow**:
a data refresh touches only `data.py`. When a new IMF, World Bank, or UN release lands, the
numbers are updated in one place, the 52 checks re-run, and all three editions rebuild — and the
prose is *not* rewritten, because methods and directions do not expire when a denominator is
revised. A move large enough to change a *direction* (a plateau becoming a decline; a laggard
beginning to converge) is treated as a new analytical edition and routed back through the review
body first. The ritual and the field-by-field source map live in the
`weight-of-nations-data-refresh` skill; the automation lives in `.github/workflows/`.

## 6 · The dual architecture and the standing review body

Two operating decisions were formalised in the eighth edition.

**Dual architecture (ChatAdvisor / Code).** A *chat advisor* plans, reads figures as a critic,
convenes the panel, ratifies changes against the invariants, and writes the exact instruction
for a change — but never edits the source. A *code executor* receives the instruction, makes the
single change, re-runs the checks, rebuilds, and commits (one change → one commit). The advisor
thinks; the executor builds. This is the division of labour that produced the editions, now
written down as the operating rule.

**The standing review body.** The ad-hoc panels of earlier editions were consolidated into a
resident body of **nine experts** (two economists, an economic anthropologist, two technologists,
an institutions-and-culture specialist, two historians, and a demographer-geopolitical
synthesist) plus **fifteen on-call advisors**, run as designed disagreement — the chair
synthesises, the author ratifies. Full composition and triggers are in the
`weight-of-nations-panel` skill.

---

## 7 · Disciplines that carried across every edition

- **One source of truth; never hand-edit a rendered edition.**
- **Two rulers, always labelled; three PPP lanes, never spliced.**
- **Source lanes kept separate** (Maddison, WDI/QoG, IMF WEO, UN WPP, Bairoch).
- **No decimal exceeds its source;** PPP carries ±5–10%, deep history has wide bands.
- **Designed disagreement, not theatre;** the chair does not vote, the author ratifies.
- **The verified numbers are consolidated** (`docs/source-research.md`) so they are never
  re-derived or hallucinated.
- **Continuity survives any single chat** via the bundle, the handoff, and past-chat search —
  a discipline learned the hard way when edition 4 hit the render limit mid-build.
- **Catches become rules:** every error caught is logged and, where it implies a standing rule,
  escalated into an invariant or a consistency check.
