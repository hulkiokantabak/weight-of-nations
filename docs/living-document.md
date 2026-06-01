# The Living Document — design rationale, reviews, and decisions

*Why* The Shifting Weight of Nations *is built as a layered public research system rather than a
single PDF, what every reviewer (four LLMs, a nine-expert panel, and the chair) concluded, the
decisions the author ratified, and the learnings now folded into the project's design, GitHub
structure, and website plan. This is the design-rationale document; the reader-facing version of
the same idea is the essay's Appendix F.*

Compiled 2026-06-01 (v8.2), ahead of the hand-off to Code.

---

## 1 · The decision

**Do it — as a layered system, not one endlessly mutating "final document."** Every reviewer
converged on this, and on the same architecture. The essay has outgrown being only a PDF, but
the strongest version is not "a book that gets updated"; it is **a research system with a
book-shaped front end**.

### The author's framing (ratified)

Three decisions the author made that resolve the open questions the reviews raised:

1. **Updating is optional.** The living architecture is built, but it does not have to be
   updated. It can stand exactly as it is, as a dated snapshot, and that is a complete and
   honest terminal state. This removes the "who maintains it?" risk: nothing is *promised*.
2. **It is public and open.** It can be updated by others — a public, openly-licensed report
   that invites reuse, correction, and extension (the BDFL model in §6).
3. **The build is worth it as experience.** The effort of building the system is accepted as
   learning, independent of how often it is later updated.

### The honest "living" claim (the reframing this produces)

> This is a reproducible, openly-licensed public report. Its **canonical editions are dated
> snapshots**. It **can** be updated — by the author or by contributors via fork/PR — but
> updating is **optional and not a promised cadence**. If it is never touched again, the dated
> snapshot stands as an honest, frozen edition.

This is intellectually consistent with the essay's own discipline: the essay *date-stamps its
own perishability* and tells readers to "read the direction, not the decimal." A static edition
that silently goes stale would betray that; a dated, openly-reproducible one does not, whether or
not anyone updates it.

---

## 2 · The three-layer architecture (the consensus)

Keep three related but **distinct** layers. Conflating them is the central risk.

1. **The canonical book / essay — frozen, dated, citable.** Google Books, PDF, (optionally)
   EPUB, plus the screen-reader edition. Has an edition number, date, cover, colophon, stable
   citations. This is what a reader quotes. Google Books is a *milestone stamp*
   (e.g. "2026 Edition"), explicitly **not** living, with front matter pointing to the repo.
2. **The living project repo — the source of truth.** Data scripts, chart definitions,
   methodology, the claim registry, the verified-numbers file, the skills, the changelog, and
   the tagged release history. The repo evolves; **each public release is tagged** (semver).
3. **The "Weight of Nations" skill — the codified reasoning and production protocol.** It knows
   how to answer new GDP-share questions, update charts, audit claims, distinguish the rulers,
   narrate visuals, draft posts, and write edition notes. Crucially, **the skill is the
   interface to the source-of-truth repo, not the source of truth itself.**

Distribution sits on top: **Substack/Medium are outreach, not the archive** (each points back to
the repo and site, and carries a snapshot banner); the **website is the reader-friendly,
navigational, interactive hub**.

---

## 3 · What every reviewer agreed on (convergence)

Across the four external LLM assessments, the nine-expert panel, and the chair:

- **Yes, do it**, because the essay's subject is inherently dynamic (PPP rounds, IMF WEO
  vintages, UN revisions, Maddison refreshes, currency/geopolitical shifts) and a static book
  starts aging the day it ships.
- **Three layers**, as above: frozen editions for authority, a living repo for truth
  maintenance, a skill for repeatable reasoning, public essays for distribution.
- **The ruler-labeling rule is the soul.** Never state a GDP-share claim without labeling the
  ruler (nominal / PPP / population / multiplier / bloc), the **source vintage**, and the
  **uncertainty**. This one rule preserves the project's whole point.
- **A claim registry** turns the project from a book into a *public correction engine* for
  macro-historical claims (now built: `data/claim-registry.md`).
- **A human editorial gate on every official release.** The danger is not bad code; it is
  *automatic confidence*. The instrument must stay disciplined.
- **Form embodies argument.** Publishing the source, the verified numbers, and the audit trail
  makes the thesis ("show your work; the decimal is a costume") *materially* true, not merely
  asserted.
- **Standard open-source infrastructure:** a license (recommended: CC-BY-4.0 for text + data,
  MIT for code), `CITATION.cff`, `CHANGELOG.md`, `CONTRIBUTING.md`, issue/PR templates, a
  definition of done.

---

## 4 · The reviews, in brief

### The Weight of Nations panel (nine experts + on-call)

**Verdict: endorse the structure**, for two agreed reasons — the argument/data durability split
is real, and transparency makes the thesis literally true — with conditions and two standing
dissents:

- **Parity** (rulers): the living form is *more* honest than static, but only if the three PPP
  lanes and no-decimal-exceeds-source are enforced by the suite, never by memory.
- **Numéraire** (data quality) — *the sharpest catch:* the IMF revises **back-history**, not just
  the latest year. A naive refresh that patches only the 2026 headline leaves 2024/2020 on an
  older vintage — an internally inconsistent document that *looks* authoritative. Rule:
  **re-pull the whole series from one vintage each cycle; never patch the tip.** (Now folded into
  the data-refresh skill.)
- **Strata** (long-run): the **frozen versioned PDF is the fossil that survives**; the repo lives
  only as long as its dependencies (Actions, Pages, WeasyPrint, font CDNs, IMF URLs) do. State
  the last good PDF + `data.py` as the canonical fallback.
- **Ember** (modern): static documents *lie by going stale*; the living form's virtue is that it
  date-stamps perishability — **but every snapshot channel must carry a "snapshot of v8.x; live
  at <url>" banner**, or multi-channel publishing recreates the staleness the essay attacks.
- **Vector** (frontier): correct form for the era — a document that is a pipeline, not a page —
  but the **directions-not-decimals gate** is the load-bearing safety feature against an
  LLM-assisted refresh quietly rewriting an *argument*. Biggest payoff if the skills become a
  reusable template.
- **Grid** (ops) — *the skeptic:* "show me the maintenance." CI that opens PRs only works if
  someone merges them. Wants a defined maintenance ritual and a **graceful-death plan**
  (auto-fall-back to static + a banner) so failure is honest, not silent. *(The author's "static
  is fine" decision answers the maintenance worry directly: nothing is promised, so nothing
  rots into a broken promise.)*
- **Mosaic** (institutions): transparency is the biggest *trust* asset, but be ready for *public*
  error-correction (the first forked bug report is public too — which is good). Frame skills as
  *optional transparency*, not as the report.
- **Hearth** (anthropology) — *the reader-centered dissent:* for 95% of readers the PDF or web
  page *is* the whole experience; the repo/skills/CI are invisible. Put the reader-facing
  "living" energy into the **interactive edition** (toggle the ruler, watch the number move) —
  the only living-ness a reader touches.
- **Compass** (demography + geopolitics): the living form is *especially* justified here because
  the variables are moving *now* (India's rise, the China-plateau debate, demographic turns), so
  the next 3–5 years will likely change *directions*, earning the living status through real
  revisions. Future wrinkle: fragmentation could make the *sources themselves* contested (rival
  statistical regimes) — the doc should be ready to footnote that.

### ChatGPT (GPT-5.5 Pro)

The most architectural review. Pushed the **three-layer separation** hardest ("a research system
with a book-shaped front end"), supplied a full **repo tree** (book/editions, essays, data/
snapshots, src, notebooks, figures, website, skill/references), the **claim-registry** design
(with fields and example verdicts), a **website information architecture**, an 8-post **Substack
sequence**, a **patch/minor/major release rhythm**, and — its headline recommendation — a
one-page **Project Charter** as "the moral center" that becomes the README intro and the skill's
core promise. Also: design for **one maintainer first**, make community help easy if it appears.

### Gemini

Framed it as moving "from artifact to living infrastructure" — a version-controlled, reproducible
*data product* where the **identity (Share = Population × Price × Productivity) is permanent
software logic** that auto-recompiles when coordinates change. Recommended the **Hybrid BDFL**
governance model (author = benevolent dictator over the canonical release; public forks and PRs
welcome) to prevent **narrative drift**. Stressed the skill as an **authoritative parser** of the
framework (compute the exact multiplier impact of a shock, not a generic answer), and asked a
design question: should the skill prioritise **dynamic recalculation** or **critical
stress-testing** of the user's assumptions? (See §9.)

### Grok

Endorsed strongly and practically. Emphasised **governance/canonical status** (main branch =
approved release; semantic versioning; a CHANGELOG explaining every material update with source
and ruler labels), recommended **starting closed for 12–18 months** and opening the gates only
after strong CI checks and a trusted reviewer circle, flagged that **Claude is great for
narrative but a hybrid workflow** (occasional precise-tabular help from other models) is optimal
for the data layer, and pushed for a **modular skill** (separate data-ingestion, ruler engine,
chart generator, narrative templates, citation system, output formatter) so a future vintage
touches only the relevant module. Concrete licensing: **CC-BY-4.0 (text+data) + MIT (code)**.

### Chair (my own assessment)

For — the argument/data split is a *real seam* in this specific work (the method doesn't expire;
the decimals do), and the transparency makes the thesis materially true, which is rare. The
honest case *against* is operational, not conceptual: a "living" doc that quietly goes stale is
worse than an honest static one; "refresh" still needs a human reading the release (the IMF
ships no clean diff); and multi-channel publishing risks three different numbers in three places.
The author's "static-is-fine, optional-update, public" decision dissolves most of the against —
it stops over-claiming. Bottom line: do it, frame it as a *human-tended-or-frozen, CI-assisted*
reproducible report whose canonical home is the repo and whose reach is the channels.

---

## 5 · Decisions ratified, and learnings folded in now

| Learning (and who pressed it) | Status in the repo |
|---|---|
| Three layers: frozen editions / living repo / skill (all) | Documented here + in README; the repo already separates source (`build/`), editions (`outputs/`), and skills (`skills/`). |
| Ruler-labeling rule is the soul (ChatGPT, Parity) | Strengthened in the orchestrator skill (the full label set, not just nominal/PPP). |
| Claim registry as a public correction engine (ChatGPT, Gemini) | **Built:** `data/claim-registry.md`, seeded from the audit data. |
| Whole-series single-vintage refresh; never patch the tip (Numéraire) | **Added** to the data-refresh skill as a hard rule. |
| Snapshot banner on every distribution channel (Ember) | **Added** to the publish guide as mandatory. |
| Semver + release cadence (Grok, ChatGPT) | **Added** to the data-refresh skill and publish guide. |
| BDFL governance; start closed, open later (Gemini, Grok) | **Added:** `CONTRIBUTING.md` + governance note in README. |
| Graceful death / canonical fallback = last good PDF + `data.py` (Strata, Grid) | **Added** to README and the orchestrator skill. |
| Human editorial gate on every release; no automatic confidence (all) | Reinforced in `GROUND-RULES.md` and the orchestrator. |
| Project Charter as the moral center (ChatGPT) | **Built:** `CHARTER.md` (also seeds the README intro and the skill core promise). |
| OSS infra: license, CITATION, CONTRIBUTING (Grok, ChatGPT) | **Added:** `LICENSE.md` (recommended dual license), `CITATION.cff`, `CONTRIBUTING.md`. |
| Put reader-facing "living" energy into the interactive edition (Hearth) | Recorded as the website priority (§8). |
| Skill as interface to the repo, modular, with output modes (ChatGPT, Grok, Gemini) | Output-mode list added to the orchestrator; modular refactor noted for Code (§7). |

---

## 6 · Governance model (BDFL)

- **Canonical control (the author = benevolent dictator).** The `main` branch and the official
  Google Books / Substack editions are the author's approved releases. Only the author merges to
  the canonical manuscript and data.
- **Public forks.** Anyone may fork, swap datasets (e.g. an alternative historical
  reconstruction), or build new visual modules.
- **Contribution lane.** Pull requests for data fixes, current-year chart updates, claim audits,
  translations, and accessibility — reviewed against the invariants and the ruler rule.
- **Start closed, open gradually.** For the first ~12–18 months the author controls all merges;
  the gates open wider once CI checks, contribution templates, and a small trusted reviewer
  circle are in place. Designed disagreement does **not** mean an editable comments section.

---

## 7 · Proposed GitHub structure (target for Code)

The current repo (flat, proven, green) is the **starting point**; the elaborated three-layer
layout below is the **target** for Code to grow into without breaking the single-source build.
Marked *(now)* = already present, *(add)* = for Code.

```
weight-of-nations/
  README.md  CHARTER.md  GROUND-RULES.md  HANDOFF.md            (now)
  LICENSE.md  CITATION.cff  CONTRIBUTING.md  CHANGELOG.md        (now: LICENSE/CITATION/CONTRIBUTING; add CHANGELOG)
  .github/workflows/living-update.yml                           (now)
  .github/ISSUE_TEMPLATE/{data,chart,claim,essay}.md            (add)
  book/                                                         (add — relocate frozen editions)
    current/ {pdf, epub, audio-pdf}
    editions/ v8.0/ v8.1/ …                                     (tagged snapshots)
  build/                                                        (now — the source of truth)
    data.py charts.py content.py parse_manuscript.py
    check_consistency.py update_data.py build_{pdf,html,audio}.py
    (optional modular refactor: ingest / normalize / ruler_engine / figures / validate)  (add, Grok)
  data/
    claim-registry.md                                           (now)
    source-register.md  snapshots/2026-04/ 2026-10/             (add — per-vintage source pulls)
  docs/ METHODOLOGY METRICS LOG source-research living-document README-rebuild  (now)
  essays/ substack/ medium/ country-briefs/                     (add — distribution drafts)
  skills/ weight-of-nations{,-panel,-data-refresh}/SKILL.md     (now)
  website/ index.html assets/ charts/ data/                     (add — reader hub; seed = interactive edition)
  outputs/                                                      (now — current rendered editions)
```

A single master data file feeds both the web build and the print build (already true); the
target layout just gives editions, snapshots, distribution drafts, and the site their own homes.

## 8 · Proposed website information architecture

The website is the **reader-friendly** face of the system (the book stays literary; the site is
navigational, interactive, updatable). Reader-facing "living-ness" lives here (Hearth's point) —
the interactive ruler switcher is the only living-ness most readers will ever touch.

```
Home              — the thesis in one screen
Read the Essay    — web essay · PDF · EPUB · audio edition
The Two Rulers    — nominal vs PPP explainer (interactive)
The Multiplier    — GDP share ÷ population share
Charts            — interactive charts + downloadable static figures
Country Readings  — US · China · India · Europe/UK · Japan · Russia · Africa · Rest of World
Claim Audit       — the claim registry, ruler-labeled verdicts
Data & Method     — sources, vintages, uncertainty, code, repo link
Updates           — release notes / data-watch
Contribute        — how to suggest fixes, add sources, propose charts
```

Seed: the existing `outputs/the-shifting-weight-of-nations.html` is already a single-file
interactive edition → it becomes the site's `Read the Essay` / `Charts` core, published via
GitHub Pages by the existing workflow. This dovetails with the separate website-rebuild project
if the essay is to live under the author's own domain.

## 9 · Release cadence & versioning

Semantic versioning for a data essay:
- **Patch** (v8.0 → v8.1): typo, layout, link, citation, or metadata-only change (this is what
  v8.1/v8.2 were).
- **Minor** (v8.x → v8.(x+1)): new WDI/IMF/UN data, refreshed charts, **no thesis change** —
  decimals only.
- **Major** (v8 → v9): new Maddison/PWT benchmark, a new framework, a new country section, or a
  *direction* change — gated through the panel.

Suggested rhythm (none promised; all optional): *quarterly* small notes / claim audits;
*twice-yearly* IMF WEO pass; *annual* full chart refresh; *every 2–3 years* a major revision if
the thesis needs it. The repo preserves every edition; history is never silently overwritten.

## 10 · Open design question for the author (the skill's primary posture)

Gemini's question, sharpened: when a user invokes the skill, should it default to
**(a) dynamic recalculation** — recompute the 2024–2026 arrays and charts on the fly — or
**(b) critical analytical partner** — stress-test the user's own claim/assumption against the
ruler discipline and the established scenarios?

**Chair recommendation:** default to **(b), with (a) as an explicit mode.** The project's soul is
*measurement discipline*, not auto-recalculation, and the agreed "human editorial gate / no
automatic confidence" caution points the same way. So the skill's first move on any prompt should
be to **label the ruler and check the claim**, and only **recompute on explicit request**
(`data_update_memo` / `chart_update` modes). The canonical output modes for the skill:

`claim_audit · country_reading · data_update_memo · chart_update · essay_revision ·
website_article · audio_narration · release_notes · source_review · contributor_review`

This is the one decision left genuinely open for the author before Code builds out the skill's
behaviour.

---

## 11 · Bottom line

Build it as a layered system — **frozen dated editions for authority, a living public repo for
truth maintenance, a disciplined skill for repeatable reasoning, and public essays for
distribution** — and frame the "living" claim honestly: reproducible and open, updatable by
anyone, promised to no one, and complete as a dated snapshot even if never touched again. That is
more durable than any single PDF, and it is consistent with the essay's own argument about
rulers, directions, and the humility a number deserves.
