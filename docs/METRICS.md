# METRICS — *The Shifting Weight of Nations*

*A numerical tracker of the project, in the spirit of the essay's own Appendix E: a thinking aid
should be auditable. Where a number was directly measured (from a file or this conversation's
transcript) it is marked **[measured]**; where it is reconstructed from artifacts or cited past
chats it is marked **[reconstructed]**; approximate values are marked **≈**. Nothing here is
invented to look complete — unknown counts are stated as unknown.*

Snapshot date: **2026-06-01** · Edition: **8th (first living edition)** · Version: **v8.1**
(v8.1 adds the cross-model effort metrics in §5; the essay itself is unchanged from v8.0.)
Project timeline: work began **Sunday, 31 May 2026**.

---

## 1 · Artifact metrics [measured]

| Metric | Value | Source of measurement |
|---|---|---|
| Manuscript length | **16,713 words** | `wc -w` on the manuscript (was 15,374 pre-eighth-edition; +1,339 of back matter) |
| Figures | **22** chart placements | renderer count in `charts.py`; figure callouts in manuscript |
| Reference tables | **3** (B1–B3) | manuscript |
| Print edition | **63 pages** PDF, 2.32 MB | `pypdf` page count; `stat` on output (was 59 pages) |
| Interactive edition | **16** live canvases, ≈0.88 MB | `<canvas>` count in the HTML |
| Screen-reader edition | 1 TTS PDF, ≈0.15 MB | `stat` on output |
| Build pipeline | **3,827 lines** of Python | `wc -l build/*.py` |
| Consistency suite | **52 checks**, 0 failing | `check_consistency.py` result |
| Project skills | **3** SKILL.md files, **487 lines** total | `wc -l skills/*/SKILL.md` |
| Review-body personas | **24** (9 standing experts + 15 on-call advisors) | `weight-of-nations-panel` skill |

## 2 · Quality / process metrics [measured + reconstructed]

| Metric | Value | Notes |
|---|---|---|
| Editions to date | **8** | 1–7 static; 8th is the first living edition [reconstructed from changelog + past chats] |
| Catches, eighth-edition finalisation | **10** found & cleared (4 load-bearing logged) | all in the coda data layer; no prose changed [measured this session] |
| Catches, seventh edition | **3** logged (incl. the $205T→$222.8T correction) | from the changelog [reconstructed] |
| Material data corrections, lifetime | ≥4 (world PPP; two lane labels; one growth multiple) | `LOG.md` |
| Review passes, eighth edition | **4** (logic/math · figures · literary · editorial) | [measured this session] |
| Designed-disagreement panels, coda (7th ed) | **3** panels × **5 rounds** = 15 rounds | deep-thinkers · fx-experts · wisepersons [reconstructed] |
| Source lanes kept separate | **5** (Maddison · WDI/QoG · IMF WEO · UN WPP · Bairoch) | invariant 3 |
| PPP lanes kept distinct | **3** (2026 current · 2024 current · 2024 const-2021) | invariant 2 |
| Standing invariants | **10** | `weight-of-nations` orchestrator §1 |

## 3 · Prompt & effort metrics

The essay's prior editions were authored across **separate conversations**; only this
finalisation-and-migration conversation is directly measurable from a transcript. Honest
accounting:

| Metric | Value | Tag |
|---|---|---|
| Driving user prompts, **this conversation** | **2** | [measured] — a finalisation brief and a migration brief |
| — finalisation brief length | **172 words** (964 chars) | [measured] from transcript |
| — migration brief length | ≈440 words | ≈ (this message; structured, 3 goals + 6 build items + rules) |
| Assistant tool calls, this conversation (pre-compaction) | **18** | [measured] from transcript |
| Claude conversations in the lineage | **5** (this is the 5th; 4 prior), of which **3** are identifiable by id | [author-confirmed count]; ed-4 `99de5936`, ed-7 `8d553b33`, ed-8 (this). See §5 for the full cross-model accounting. |
| Total project prompts (all editions, all models) | see **§5** | not fully transcript-measured; estimated per the author's heuristics, labelled there |

*Per-prompt density is high and low-count: the author works in a few long, structured prompts
that delegate large multi-step builds, then reviews — rather than many short turns. The
172-word finalisation brief alone specified four review passes and a consistency-check
methodology; the migration brief specified the entire code-first living architecture.*

## 4 · Survival / continuity logic

The number that matters for a *living* document is not how many tokens it cost but **how much it
survives** — loss of a chat, compaction of context, the death of a platform, the revision of a
denominator.

| Survival dimension | State |
|---|---|
| **Context compaction** | This conversation underwent context compaction (the working summary notes up to **2** compaction events); the project's decided state survived because it was written to durable artifacts (manuscript, `data.py`, docs) rather than held in chat memory. |
| **Chat-to-chat handoff** | Survived a **forced** handoff in edition 4, which hit the platform's 100-image / PDF-render limit mid-build. The bundle + `HANDOFF.md` + past-chat-search reflex were the recovery; they are now standing discipline. |
| **Single-chat loss** | Mitigated: the repository (source + docs + skills + verified numbers) is self-sufficient. `docs/source-research.md` carries the verified numbers so no figure is ever re-derived from memory. |
| **Platform mortality** | Active external links only to high-continuity sources (IMF, World Bank, UN, Maddison). Earlier-LLM provenance recorded as historical fact in the colophon, not as a live dependency. |
| **Data staleness** | The living mechanism (`weight-of-nations-data-refresh` + `.github/workflows/living-update.yml`) refreshes `data.py` on each release and rebuilds; the 52 checks block a bad refresh. |
| **Argument drift** | Guarded by invariant 9: only a *direction* change (not a decimal) reopens the prose, and only through the review body. |

## 5 · The multi-model effort (cross-system metrics)

This essay was produced not in one chat but across a **nine-conversation, five-model effort**:
five Claude chats (this is the fifth) plus four other-LLM lines — ChatGPT (GPT-5.5 Pro),
Gemini, Grok, and DeepSeek. The numbers below characterise the **scale and shape** of that
effort. Provenance is labelled strictly:

- **[measured]** — from this conversation's transcript or the repo files.
- **[self-reported]** — ChatGPT/GPT-5.5 Pro's own metrics assessment, supplied by the author;
  **not independently verified.**
- **[estimate]** — derived from the author's stated heuristics (the non-Claude models as
  fractions of ChatGPT; the prior Claude chats as ≈4× this one).

> **Commensurability caveat.** The Claude line's canonical deliverable is *this living essay and
> its repository* (a 16,713-word essay → three editions, plus ~490 lines of skills and ~860
> lines of docs). ChatGPT's self-report counts *report-PDF iterations and their words*. These
> are different units of work; the cross-model word figures index volume/effort, **not** a
> single corpus of unique words, and report iterations overlap heavily.

### Tier A — Claude line (5 chats)

| Chat | Role | Prompts | Prompt words | Output |
|---|---|---|---|---|
| #5 (this one) | finalisation + migration to the living document | **2** driving [measured] | **~612** (172 + ~440) [measured] | the repository (3 skills, all docs, the workflow, the refresh harness), +1,339 manuscript words, three rebuilt editions; canonical essay **16,713 words / 63-pp PDF** |
| #1–#4 | editions 1–7 authoring, the 22-figure pipeline build, the 7th-edition fusion | not transcript-counted | not transcript-counted | **≈4× this chat's output in aggregate** [author estimate] |
| **Claude total** | — | — | — | **≈5× this chat** [author estimate] |

### Tier B — ChatGPT / GPT-5.5 Pro (parallel authoring line) — [self-reported]

| Metric | Value |
|---|---|
| Visible user prompts | **15** (14 production + 1 metrics) |
| User-prompt words | **~1,348** |
| Major report PDFs | **8** · 231 pages · **~56,757 words** |
| Audio-upload PDFs | **3** · 34 pages · ~14,934 words |
| Combined report + audio | **265 pages · ~71,691 words** |
| Persisted deliverable files | **21** · ~77 MB |
| Cover / concept images | **27** |
| Model named in *its* colophon | GPT-5.5 Pro |

*This is the GPT line that produced the publication-edition apparatus the seventh Claude edition
fused in; the figures are ChatGPT's own count, not verified here.*

### Tier C — Gemini / Grok / DeepSeek (evaluation + synthesis lines) — [estimate]

Per the author's heuristic: Gemini and Grok ≈ **1/6** of ChatGPT each; DeepSeek ≈ **1/10**.

| Model | Scale vs ChatGPT | ~Prompts | ~Prompt words | ~Output words |
|---|---|---|---|---|
| Gemini | 1/6 | ~2–3 | ~225 | ~11,950 |
| Grok | 1/6 | ~2–3 | ~225 | ~11,950 |
| DeepSeek | 1/10 | ~1–2 | ~135 | ~7,170 |

### Cross-model totals (mixed provenance — read with the caveat above)

| Metric | Value | Composition |
|---|---|---|
| Non-Claude visible prompts | **~21–22** | ChatGPT 15 + Gemini ~2.5 + Grok ~2.5 + DeepSeek ~1.5 |
| Non-Claude prompt words | **~1,933** | 1,348 + 225 + 225 + 135 |
| Non-Claude output words | **~102,800** | 71,691 + 11,948 + 11,948 + 7,169 (iterations overlap; not unique) |
| Conversations, all models | **9** | 5 Claude + 4 other-LLM |
| Distinct models | **5** | Claude (Opus 4.8), GPT-5.5 Pro, Gemini, Grok, DeepSeek |

### The document flow (author-described)

1. **Four LLM synthesis documents** — each model produced a synthesis from the shared Hoover/
   Kotkin brief (the initial ~400-word request went to all of them).
2. **Iterative versions by ChatGPT and Claude** — the two systems that carried the deepest
   authoring, each producing several editions.
3. **Final documents culminating with Claude** — the canonical essay in this repository, whose
   spine is Claude's and whose ingested apparatus is GPT-5.5 Pro's (Appendix D records this).

### Timeline

Work began **Sunday, 31 May 2026**; the essay was finalised and migrated to this living
repository **Monday, 1 June 2026**.

---

## 6 · How to update this file

Bump on every session: artifact metrics if files changed; the catch count from `LOG.md`; the
version/edition; and any new survival event. Mark every number with its provenance —
**[measured]**, **[reconstructed]**, **[self-reported]**, or **[estimate]** — and **never
promote** a reconstruction, a self-report, or an estimate to a measurement. When an external
figure contradicts a measured one, keep the measured value canonical and note the discrepancy.
