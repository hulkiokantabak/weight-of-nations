---
name: weight-of-nations
description: >
  Orchestrating skill for "The Shifting Weight of Nations" — the living, self-updating
  data essay on five centuries of world-GDP shares (PPP vs nominal, the multiplier,
  productivity as the durable variable). Carries the project's architectural canon, the
  single-source-of-truth build, the dual ChatAdvisor/Code workflow, the consistency suite,
  the four-document loop, and the self-update mechanism. USE whenever the work touches this
  essay — editing the manuscript or data file, rebuilding the three editions, refreshing the
  numbers for a new IMF/World-Bank/UN release, planning a new edition, preparing a Code
  handoff, or reasoning about the living-document repository. Triggers: "Weight of Nations,"
  "the shifting weight of nations," "the data essay," "the living document/book," "the GDP
  essay," "won project," any reference to data.py / charts.py / the cone / the rulers / the
  multiplier in this project, or a HANDOFF for it. Routes to weight-of-nations-panel (the
  nine-expert review body) and weight-of-nations-data-refresh (the annual update ritual).
  Honors the project invariants below as immutable ground truth.
---

# weight-of-nations — the living-document orchestrator

This is the chair's operating manual for *The Shifting Weight of Nations*. It is the entry
point for any session on the essay. It holds what must not drift (the invariants), how the
work is done (the dual architecture and the loop), and how the document keeps itself alive
(the self-update mechanism). Two companion skills do the specialised work:
`weight-of-nations-panel` (the standing review body) and `weight-of-nations-data-refresh`
(the data-update ritual and source map).

Two tiers below: **project canon** (immutable ground truth for this essay) and
**operating practice** (transferable discipline, shared with `project-continuity`).

---

## 0 · What the project is

A skeptical, interactive data essay that takes a memorable claim about national economic
weight (originating from a Stephen Kotkin / Hoover *Uncommon Knowledge* conversation) and
subjects it to scrutiny rather than repeating or debunking it. The spine: a nation's share
of world GDP is **population × price-level × productivity**, and people switch silently
between two rulers (market-rate **nominal** and price-adjusted **PPP**) and between *size*
and *prosperity*. The essay separates the rulers, adds a population-adjusted **multiplier**,
and argues that the one durable variable under five centuries of rise/fall/re-convergence —
and the one that decides the next fifty years — is **productivity**.

One source of truth renders **three editions**: an interactive Chart.js page, a typeset
WeasyPrint PDF, and a screen-reader (TTS) PDF. The eighth edition is the first to live in a
public, version-controlled repository that rebuilds itself when the source data updates.

Read-order for a new chair: this skill → `docs/METHODOLOGY.md` → `docs/source-research.md`
(the verified numbers, so you never re-derive or hallucinate them) → `build/` modules →
(only if needed) the other two skills.

---

## 1 · PROJECT INVARIANTS (do not drift)

Each is non-negotiable without the author explicitly re-opening it.

1. **Label the ruler — always, fully.** No GDP-share claim, in prose or a figure, without
   naming its **ruler** (nominal current-dollar / PPP-international-dollar / population share /
   multiplier / bloc construction), its **source vintage**, and its **uncertainty**. Never an
   unlabelled "share of world GDP." This one rule preserves the project's whole point; a figure
   true on one ruler is routinely false on another.
2. **Three PPP totals are distinct fields, never merged.** 2026 current ($222.8T) ·
   2024 current (~$195T) · 2024 constant-2021 (~$170T, the internal arithmetic lane). They
   live as separate values in `data.py` and are never spliced or averaged.
3. **Source lanes never spliced.** Maddison (deep history) · World Bank WDI / QoG
   country-sum (modern) · IMF WEO (present-day marker) · UN WPP (population) · Bairoch
   (manufacturing). A single line never blends two lanes.
4. **The coda is illustrative, not forecast.** Figures 17–22 carry "illustrative — not a
   forecast" (except Fig 20 = "projection · UN WPP 2024"). This flag survives every render.
5. **The cone is the envelope of the bars.** Fig 18's 2050 fan for each country is exactly
   `(min, mean, max)` of that country's five Fig 19 scenario bars. They cannot disagree.
6. **Scenario columns sum to 100%.** In Fig 19 each scenario's named-actor shares plus a
   residual "Rest of World" total 100%. RoW is the residual, computed, never typed by hand.
7. **One source of truth; never hand-edit a rendered edition.** Numbers live only in
   `build/data.py`; prose lives only in the manuscript (→ `build/content.py` via the parser).
   You edit the source and re-run the builders. The HTML, PDF, and audio are outputs, never
   inputs.
8. **No decimal exceeds its source.** PPP carries ±5–10% structural uncertainty; deep-history
   figures are reconstructions with wide error bars. The reading rule — *ruler first,
   direction second, decimal last* — governs both prose and figures.
9. **Directions, not decimals, gate editions.** A data refresh that moves only decimals does
   not change the prose. A move large enough to change a *direction* (a plateau becoming a
   decline, a laggard beginning to converge) is a new analytical edition and must pass the
   review body first (see §4, and `weight-of-nations-panel`).
10. **Authorship & tone.** Directed by Hulki Okan Tabak; written by Claude 4.8 and Hulki Okan Tabak (co-authorship
    ratified by the author at v8.5; cross-model provenance disclosed in Appendix D and METRICS §5).
    Register is understated,
    ruler-obsessed, humane; the body (a clinic, a haircut, a life) appears where the
    abstraction would otherwise win. Earlier-LLM provenance is disclosed in the colophon, not
    hidden.

---

## 2 · The repository (file map)

```
weight-of-nations/
├── README.md                  # project overview + living-document explainer
├── GROUND-RULES.md            # how the chair and executor operate (max effort, no hallucination)
├── HANDOFF.md                 # entry point for a new chair/Code session
├── build/
│   ├── data.py                # SINGLE SOURCE OF TRUTH for numbers + palette
│   ├── charts.py              # 22 figure renderers (matplotlib for PDF, specs for HTML)
│   ├── content.py             # AUTO-GENERATED prose blocks (do not hand-edit)
│   ├── parse_manuscript.py    # manuscript .md -> content.py
│   ├── check_consistency.py   # the 52-check suite (run before every build)
│   ├── update_data.py         # data-refresh harness (see data-refresh skill)
│   ├── build_pdf.py / build_html.py / build_audio.py
│   ├── build_cover.py        # prepend the cover -> with-cover PDF (compact JPEG; WON_COVER_LOSSLESS)
│   ├── win_fonts.py          # Windows-only: faithful IBM Plex Sans for WeasyPrint
│   ├── common.py              # shared block renderer
│   ├── ttf/  fonts/           # bundled fonts (matplotlib TTF + WeasyPrint woff2)
│   └── covers/               # make_covers.py + the canonical cover PNG
├── manuscript/
│   └── the-shifting-weight-of-nations.md   # the final copy (edit here, then re-parse)
├── outputs/                   # the rendered editions (interactive, print ±cover, audio)
├── website/                   # GitHub Pages site (landing + interactive edition); live at github.io
├── docs/
│   ├── METHODOLOGY.md         # how each edition was made
│   ├── METRICS.md             # editions, checks, catches, prompts, survival
│   ├── LOG.md                 # every catch + the standing rule it produced
│   ├── source-research.md     # the verified numbers (never re-derive)
│   └── README-rebuild.md      # environment + build commands
├── skills/                    # this skill + panel + data-refresh
├── publication/PUBLISH-GUIDE.md
└── .github/workflows/   # living-update.yml (self-update PR) + pages.yml (deploy the live site)
```

---

## 3 · The dual architecture (ChatAdvisor / Code)

Two instances of the assistant, two jobs, kept strictly separate — this is what keeps the
living document disciplined.

- **Chat advisor (this seat).** Plans, reads figures as a critic, convenes the panel,
  ratifies changes against the invariants, and writes the *exact* instruction for a change —
  a precise diff, the location anchors, the verification checks, and the commit message. The
  advisor **never** edits `data.py`, the manuscript, or any rendered edition directly.
- **Code executor (separate session).** Receives the instruction, makes the single change,
  re-runs `check_consistency.py`, rebuilds the three editions, and commits with a message that
  records what moved and why. One change → one commit. Pre-flight verification before, a
  dry-run/grep check after.

Hand-off discipline: every Code session begins from `HANDOFF.md`; every Code session ends by
committing and updating `HANDOFF.md` with the new state. The advisor prepares the handoff; the
executor honours it.

---

## 4 · The four-document loop (self-catching errors)

The system that turns mistakes into standing rules. The loop must produce concrete artifact
updates, not acknowledgments.

- **Catches → `docs/LOG.md`.** Every error caught (in review, in the consistency suite, by a
  panelist) is logged with date, severity (1 cosmetic … 5 ships-wrong-numbers), where found,
  and resolution. The cone/bars mismatch, the scenario-sum failure, the Japan-PPP overshoot,
  and the deep-history population mismatch are the founding entries.
- **Learnings.** When a catch implies a standing rule, escalate it to an invariant (§1) or a
  consistency check (`check_consistency.py`). A learning that lives only in prose has not yet
  shaped behaviour — it must become a check or an invariant.
- **Metrics → `docs/METRICS.md`.** Editions, figures, words, checks, catches, prompts,
  context-survival events. Updated each session.
- **Methodology → `docs/METHODOLOGY.md`.** The procedural manual; updated when a learning
  becomes operational.

---

## 5 · The self-update mechanism (how the document stays alive)

The living property is deliberately **narrow**: the mechanism touches only `data.py`.

1. A new source release lands (IMF WEO April or October, World Bank WDI, UN WPP, or a
   Maddison update). The `weight-of-nations-data-refresh` skill maps every `data.py` field to
   its source and gives the update ritual.
2. Numbers are updated **in one place** (`data.py`), via `update_data.py` where structured.
3. `check_consistency.py` re-runs its 52 checks. A red check blocks the build.
4. All three editions rebuild from the corrected source. Prose is **not** rewritten.
5. If a *direction* changed (invariant 9), the change is escalated to a new analytical edition
   and routed through `weight-of-nations-panel` before shipping. Otherwise it is a decimals-
   only refresh: bump the patch version, commit, done.
6. `.github/workflows/living-update.yml` automates steps 3–4 (and can be scheduled annually or
   triggered on a data-file change), opening a pull request rather than committing blind, so a
   human ratifies before publication.

**Commit/push rule (project-wide):** push to the project repo whenever something material
happens and at the end of every session. One change → one commit with a descriptive message.

---

## 6 · Session lifecycle

**Start.** Read `HANDOFF.md`, then this skill, then `docs/source-research.md`. Run
`conversation_search` for "Weight of Nations" and the current phase to recover any context not
in the bundle. Run `check_consistency.py` to confirm the repo is green. Surface open items;
propose the session's work; await the author's confirmation.

**Mid.** Apply the invariants. Catch errors as they appear; log severity in `LOG.md`; resolve
in-session where possible. Convene `weight-of-nations-panel` for substantive analytical
questions; invoke on-call advisors at their triggers. Edit source only (never rendered
editions); re-parse if prose changed; re-run the suite; rebuild. Escalate catches to checks or
invariants when a pattern emerges.

**End.** Update `METHODOLOGY.md`, `METRICS.md`, `LOG.md`, and `HANDOFF.md`. Confirm the three
editions rebuilt clean and the suite is green. Commit and push. State what the next session
should pick up.

---

## 7 · Guardrails specific to this project

- This is a **thinking aid and a public essay**, not financial advice; the coda is explicitly
  illustrative. Keep that framing in any derivative output.
- Believe verified source numbers over memory; when a figure feels surprising, check
  `source-research.md` or the source itself before asserting. Never invent a denominator.
- The essay has an authorship history across models; the colophon discloses it. Do not erase
  or overstate it.
- When in doubt about whether a change is "decimals" or "direction," treat it as a direction
  and route it through the panel. The cost of an unnecessary panel pass is small; the cost of
  silently shifting the argument is the whole project's credibility.

---

## 8 · Tasks, releases, governance, survival

**Canonical tasks (the skill's output modes).** The skill is the *interface* to the repo, not
the source of truth. Default posture on any prompt: **label the ruler and check the claim
first; recompute only on explicit request** (the project's soul is measurement discipline, not
auto-recalculation). The canonical modes:
`claim_audit · country_reading · data_update_memo · chart_update · essay_revision ·
website_article · audio_narration · release_notes · source_review · contributor_review`.

**The claim registry.** Public macro-historical claims and their ruler-labeled verdicts live in
`data/claim-registry.md` (mirrored in `data.py`'s `AUDIT`). A `claim_audit` adds/updates a row,
names the ruler, cites a dated value from `source-research.md`, and keeps the two in sync.

**Releases (semver for a data essay).** *Patch* = typo/layout/metadata. *Minor* = new
WDI/IMF/UN data, refreshed charts, no thesis change (decimals only). *Major* = new
Maddison/PWT benchmark, new framework or country section, or a *direction* change (panel-gated).
Every public release is tagged; history is never silently overwritten; `CHANGELOG.md` records
each material change with its source and ruler labels.

**Governance (BDFL — see `CONTRIBUTING.md`).** The author is the gatekeeper of the canonical
`main` branch and the official editions; anyone may fork/PR; gates open gradually as CI and a
reviewer circle mature. Every official release passes a **human editorial gate** — the danger is
not bad code but automatic confidence.

**Survival / graceful death.** The repo lives only as long as its dependencies (Actions, Pages,
WeasyPrint, font CDNs, source URLs). The **frozen versioned PDF + `data.py` is the canonical
fallback**: if the automation breaks, fall back to the last good edition with an honest dated
banner rather than letting the document silently go stale. Updating is *optional and promised to
no one*; a dated snapshot is a complete terminal state.
