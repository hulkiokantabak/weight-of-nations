# Changelog

All material changes to *The Shifting Weight of Nations*, newest first. Semantic versioning for
a data essay: **patch** = typo/layout/metadata; **minor** = new data, no thesis change;
**major** = new benchmark/framework/country section, or a *direction* change (panel-gated).
Every release is tagged; history is never silently overwritten. Each entry names the change and,
for data, its source and ruler labels.

## v8.5 — 2026-06-02 (patch · layout + living-document prose + authorship)
- LAYOUT (typeset PDF, 63→62 pp): generalised the keep-with-next grouper in `build/common.py` so a
  heading/caption-lead binds to a following *table*, not only a figure (fixes the scenario-map
  heading, "What to Watch", and the Appendix B2/B3 captions, plus three further lead+table cases of
  the same defect). Long tables (≥15 rows or ≥2,500 cell chars — currently only Appendix E) break
  across pages with a repeating header (`.tbl-wrap.longtable` CSS in `build/build_pdf.py`), removing
  the orphan page that stranded the Appendix E heading.
- PROSE (Appendix F): the repository paragraph now names the public GitHub repository, the
  fork-and-open-a-request-to-merge update path, and the option-not-obligation framing; removed the
  redundant "anyone may fork or improve" clause from the close. +65 words; no change to argument,
  data, figures, or directions.
- AUTHORSHIP: byline now reads "Directed by Hulki Okan Tabak; written by Claude 4.8 and Hulki Okan
  Tabak" (masthead + Appendix D); invariant 10, CHARTER, and README updated to match. Cross-model
  provenance remains disclosed in Appendix D and METRICS §5. *(Folded in from the v8.4 chat-advisor
  line, which had not been committed to this repository.)*
- Editions: shipped the chat-advisor's faithfully-rendered v8.5 editions (PDF 62 pp, HTML, audio
  49 pp). `build/build_pdf.py` retains this repo's Windows font-portability fix (`Path.as_uri()` +
  bundled-font default) — the v8.5 long-table CSS was applied *over* it via patch, not by drop-in.
  Suite 52/0.
- LINEAGE: the repository went **v8.3 → v8.5** directly; "v8.4" existed only in the chat-advisor
  line (the authorship change + a stale-word-count correction) and its substance is folded in here.
- STILL FLAGGED (pre-existing, out of scope): the first-page masthead reads "Seventh (fused &
  panel-reviewed)" while the edition is the eighth.

## v8.3 — 2026-06-01 (minor · publication back matter)
- Essay back matter updated for the static publishing editions: Appendix E gains cross-model
  effort, architecture & governance, and publication-layer rows; Appendix F gains a "shape of
  the project" paragraph (the three-layer model + website + the honest, optional living claim).
- Rebuilt all three editions (PDF 63 pp, HTML, audio); consistency suite 52/0. Analytical prose
  unchanged.

## v8.2 — 2026-06-01 (patch · design consolidation)
- Added `docs/living-document.md`: full design rationale synthesising four external LLM reviews
  (GPT-5.5 Pro, Gemini, Grok), the nine-expert panel, and the chair, with decisions and target
  structure.
- Added `CHARTER.md` (project charter / moral center), `data/claim-registry.md` (ruler-labeled
  public-claim registry, seeded from the audit data), `CITATION.cff`, `CONTRIBUTING.md`,
  `LICENSE.md` (recommended CC-BY-4.0 prose+data / MIT code).
- Folded learnings into the skills, README, and publish guide: full ruler-label rule; whole-
  series single-vintage refresh; mandatory snapshot banners on every channel; semver + release
  cadence; BDFL governance; graceful-death / canonical-fallback; the skill's output modes.
- The essay and its data are **unchanged**; the consistency suite remains 52/0.

## v8.1 — 2026-06-01 (patch · metrics)
- Added the cross-model effort metrics (§5 of `docs/METRICS.md`): five Claude chats + four
  other-LLM lines (GPT-5.5 Pro, Gemini, Grok, DeepSeek), with strict provenance labels
  (measured / self-reported / estimate). Essay unchanged.

## v8.0 — 2026-06-01 (major · first living edition)
- Finalised the eighth edition and migrated the project to a code-first, self-updating public
  repository (single source of truth → three editions: interactive, print, screen-reader).
- Manuscript back matter: added Appendix F ("This Is a Living Document") and seven project-metric
  rows to Appendix E. Analytical prose unchanged.
- Four-pass finalisation (logic/math · figures · literary · editorial) cleared ten coda-data
  catches; the 52-check consistency suite reports 52/0.
- Established three project skills (orchestrator · nine-expert + fifteen-advisor panel ·
  data-refresh ritual), the data-refresh harness, and the GitHub Actions living-update workflow.
- Canonical slug set to `the-shifting-weight-of-nations`; output paths made repo-relative.

## Editions 1–7 (pre-repository, May–June 2026)
- Built across separate conversations; lineage recorded in `docs/METHODOLOGY.md`. Highlights:
  ed-4 built the single-source pipeline; ed-7 fused the Claude spine with an ingested GPT-5.5 Pro
  apparatus and corrected world PPP from ~$205T to $222.8T (IMF WEO April 2026), adding the
  speculative coda (figures 17–22).
