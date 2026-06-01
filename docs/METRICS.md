# METRICS — *The Shifting Weight of Nations*

*A numerical tracker of the project, in the spirit of the essay's own Appendix E: a thinking aid
should be auditable. Where a number was directly measured (from a file or this conversation's
transcript) it is marked **[measured]**; where it is reconstructed from artifacts or cited past
chats it is marked **[reconstructed]**; approximate values are marked **≈**. Nothing here is
invented to look complete — unknown counts are stated as unknown.*

Snapshot date: **2026-06-01** · Edition: **8th (first living edition)** · Version: **v8.0**

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
| Conversations across the lineage (editions 1–8) | **≥5 distinct chats**, of which **3** are identifiable by id | [reconstructed]: ed-4 `99de5936`, ed-7 `8d553b33`, ed-8 (this) |
| Total project prompts (all editions) | **not measured** | earlier chats not in the working transcript; do not fabricate |

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

## 5 · How to update this file

Bump on every session: artifact metrics if files changed; the catch count from `LOG.md`; the
version/edition; and any new survival event. Mark new numbers **[measured]** or
**[reconstructed]**; never promote a reconstruction to a measurement.
