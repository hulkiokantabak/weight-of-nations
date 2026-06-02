# HANDOFF — *The Shifting Weight of Nations* (living data essay)

**You are the new chair (or the Code executor).** This is the entry point. Read it first.

- **Project:** a skeptical, interactive data essay on five centuries of world-GDP shares.
- **Edition / version:** **8th — first living edition · v8.5** (2026-06-02; v8.5 = long-table layout fix + Appendix F living-doc prose + authorship co-credit; editions rebuilt, PDF 62 pp). *Post-v8.5 (2026-06-02): published with cover; web link added to page 1 + Appendix F; Appendix E metrics corrected; cover compacted; README rebuilt in house style — see `CHANGELOG.md`.*
- **State:** finalised and migrated to this repository. Suite green (52/0). Three editions built.
  *2026-06-02 (Windows workstation):* reproducibility verified (suite + parser + HTML rebuild
  deterministically; PDF/audio build natively via MSYS2 GTK); build tooling hardened for Windows
  (commits `8003029`, `020eaa6`); release tags **v8.0–v8.3** created; repository **published to
  GitHub** (`https://github.com/hulkiokantabak/weight-of-nations`, `main` + tags).
  *2026-06-02 (v8.5):* applied the author-authorised code-update kit — long-table layout fix
  (PDF 63→62 pp), Appendix F living-doc prose, and the authorship co-credit ("written by Claude 4.8
  and Hulki Okan Tabak"); shipped the kit's faithful editions; suite 52/0; tagged v8.5.
- **Architecture:** dual — a **chat advisor** plans and ratifies; a **Code executor** builds and
  commits. Keep them separate (see `GROUND-RULES.md` §4).

---

## 0 · Read order

1. this `HANDOFF.md`
2. `skills/weight-of-nations/SKILL.md` — the orchestrator (invariants, file map, loop, self-update)
3. `docs/source-research.md` — the verified numbers (never re-derive)
4. `docs/METHODOLOGY.md` — how the editions were made (context, not required to act)
   - `docs/living-document.md` — the design rationale + target GitHub/website structure (read before any restructure); `CHARTER.md` — the project's moral center
5. `build/` modules — only as deep as the task needs
6. the other two skills — `weight-of-nations-panel` (review body), `weight-of-nations-data-refresh` (update ritual)

## 1 · Session start (do this every time)

```bash
cd build && python3 check_consistency.py     # confirm the repo is green (expect 52/0)
```
- Run `conversation_search` for "Weight of Nations" + the current phase to recover any context
  not in the repo.
- Surface open items (below). Propose the session's work. **Await the author's confirmation.**

## 2 · The golden rules (do not break)

- **One source of truth.** Numbers live only in `build/data.py`; prose only in
  `manuscript/the-shifting-weight-of-nations.md` (→ `content.py` via the parser). **Never
  hand-edit a rendered edition.**
- **Two rulers labelled; three PPP lanes never spliced; source lanes never spliced; coda is
  illustrative; cone = envelope of bars; scenario columns sum to 100%; no decimal exceeds its
  source.** Full list: orchestrator §1 (ten invariants).
- **Chair never edits source; executor never redesigns.** One change → one commit.
- **Directions, not decimals, reopen the prose** — and only through the review body.

## 3 · The two things you'll most likely be asked to do

**A. Refresh the data (a new IMF/WDI/UN release).** Follow `weight-of-nations-data-refresh`:
record the new numbers in `source-research.md` → edit `data.py` **only** (use
`build/update_data.py --validate`) → `python3 check_consistency.py` (52/0) → rebuild the three
editions → decide *decimals vs direction* → bump version, update `METRICS.md`/`LOG.md`, commit /
open PR.

**B. A new analytical edition (a direction changed, or new analysis).** Convene
`weight-of-nations-panel` → ratify the prose change with the author → edit the manuscript →
`python3 parse_manuscript.py` → `check_consistency.py` → rebuild → bump the **edition** number →
update all four docs → commit.

## 4 · Build commands

```bash
cd build
python3 check_consistency.py                       # 52 passed, 0 FAILED
python3 parse_manuscript.py                         # ONLY if prose changed
python3 build_pdf.py && python3 build_html.py && python3 build_audio.py
```
Outputs go to `outputs/` by default (override with `WON_OUTPUT_DIR`). Environment + font setup:
`docs/README-rebuild.md`.

## 5 · Session end (do this every time)

- Confirm the three editions rebuilt clean and the suite is green.
- Update `docs/METHODOLOGY.md`, `docs/METRICS.md`, `docs/LOG.md`, and **this `HANDOFF.md`** with
  the new state and the next open items.
- **Commit and push.** One change → one commit, descriptive message.
- State what the next session should pick up.

## 6 · Open items (keep current)

**Recently done & open items (2026-06-02 publication round; the panel ran a 3-round retrospective, logged in `docs/LOG.md`):**

0. **Publishing copy received & committed (2026-06-02).** ✅ The author's cover
   (`build/covers/the-shifting-weight-of-nations-cover.png`) and the **with-cover publishing PDF**
   (`outputs/...-with-cover.pdf`, 63 pp = cover + the 62-pp essay) are committed; the without-cover
   and audio editions were byte-identical to the v8.5 build outputs. **Done since:** (a) ✅ masthead corrected (manuscript "Edition" field + the hardcoded
   `parse_manuscript.py` kicker → "eighth edition") and all three editions **re-rendered faithfully
   on Windows** — 62-pp PDF with real IBM Plex Sans at every weight, via `build/win_fonts.py` (unifies
   the @fontsource per-weight Plex Sans for the MSYS2 fontconfig) + a `'IBM Plex Sans'` CSS fallback
   in `build_pdf.py`; the live site redeploys via the Pages workflow on push. (b) ✅ reproducible
   cover-merge is `build/build_cover.py` (cover image + essay PDF → with-cover, 63 pp).
   (c) ✅ Appendix E "Build size" metrics corrected (~4,000 lines / ~17,200 words / 62 pp).
   (d) ✅ **web link added to the book** — page-1 masthead + Appendix F (live site + repo URLs).
   (e) ✅ cover compacted to a JPEG embed (`build_cover.py`; with-cover 5.1→2.6 MB; set
   `WON_COVER_LOSSLESS=1` for a lossless print master; the standalone cover PNG stays the high-res
   asset). (f) ✅ README rebuilt in the author's house style. *(The Windows print PDF still carries
   minor Lucida/Corsiva fallbacks for a few symbol/edge-italic glyphs — see the zero-fallback to-do.)*
1. **Website built & LIVE (2026-06-02).** ✅ Public site at
   **https://hulkiokantabak.github.io/weight-of-nations/** — landing `index.html` (read online /
   download / fork / cite, in the essay's type + palette) plus the interactive edition, in
   `website/`, deployed by `.github/workflows/pages.yml`. Pages is enabled with **Source = GitHub
   Actions**; the workflow auto-deploys on every push to `main` (paths `website/**` or the interactive
   edition) and on manual run, copying the current `outputs/` edition in at deploy time. Optional
   polish: a custom `hulkiokantabak.com` subpage (Settings → Pages → Custom domain); a future
   data-refresh will redeploy the site automatically.
2. **Make the repo fork-ready** for outside contributors. Turn `CONTRIBUTING.md` into a concrete
   fork → edit `build/data.py` → run the 52-check suite → rebuild → open-a-PR walkthrough; add a
   `.gitattributes` (LF for code/text) so line endings stay stable across Windows/macOS/Linux clones
   (this machine is `core.autocrlf=true`); confirm the living-update workflow opens PRs (needs the
   Actions write/PR permission below); consider issue/PR templates. Goal: a stranger can fork,
   update, and change it without reading this whole file.
3. **Make the one-year revisit easy.** Walk the `weight-of-nations-data-refresh` ritual end-to-end
   (`update_data.py --validate` → suite → rebuild → decimals-vs-direction → version bump) and smooth
   any friction, so a future IMF/WDI/UN update is a short, safe pass. Dry-run before the October 2026
   IMF WEO.

**Standing items:**

- [x] **Release tags v8.0–v8.3 created** and **repository pushed to GitHub** (2026-06-02):
  `https://github.com/hulkiokantabak/weight-of-nations` (`main` + tags). *Next: in repo Settings →
  Actions → General, enable "Read and write permissions" + allow Actions to create PRs, so the
  living-update workflow can open PRs (PUBLISH-GUIDE §A).*
- [ ] **Publish** the editions to Google Books, Substack, and Medium — see
  `publication/PUBLISH-GUIDE.md`. *Requires the author's accounts; the chair prepares, the author
  publishes.*
- [ ] **Zero-fallback print master** (before any paid print run) — render the print PDF on Linux/CI
  or the publishing pipeline (the Windows PDF carries minor Lucida/Corsiva edge-glyph fallbacks). *[panel]*
- [ ] **Keep the claim-registry / `source-research.md` in sync** on each data refresh — ruler-labeled
  public claims current. *[panel]*
- [ ] First scheduled **data refresh** will be the next IMF WEO (October 2026) — dry-run the
  living-update workflow before then.

## 7 · Provenance note for whoever picks this up

The essay has an authorship history across model versions (Claude spine + an ingested GPT
apparatus at the seventh edition), disclosed in the colophon. The eighth edition's finalisation
and migration were done on Claude Opus 4.8. Don't erase or overstate that history; it's recorded
honestly in `docs/METHODOLOGY.md` and Appendix D.
