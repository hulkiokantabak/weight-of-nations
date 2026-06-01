# HANDOFF — *The Shifting Weight of Nations* (living data essay)

**You are the new chair (or the Code executor).** This is the entry point. Read it first.

- **Project:** a skeptical, interactive data essay on five centuries of world-GDP shares.
- **Edition / version:** **8th — first living edition · v8.2** (2026-06-01; v8.2 = design consolidation, essay unchanged).
- **State:** finalised and migrated to this repository. Suite green (52/0). Three editions built.
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

- [ ] **Publish** the v8.0 editions to Google Books, Substack, and Medium — see
  `publication/PUBLISH-GUIDE.md`. *Requires the author's accounts; the chair prepares, the author
  publishes.*
- [ ] **Create the GitHub repo and push** — see `publication/PUBLISH-GUIDE.md` §"GitHub setup."
  *Requires the author's GitHub auth; local commit history is ready.*
- [ ] **Enable GitHub Pages** (optional, toward a dedicated website) — serve the interactive
  edition as the site; workflow already builds it.
- [ ] First scheduled **data refresh** will be the next IMF WEO (October 2026) — dry-run the
  living-update workflow before then.

## 7 · Provenance note for whoever picks this up

The essay has an authorship history across model versions (Claude spine + an ingested GPT
apparatus at the seventh edition), disclosed in the colophon. The eighth edition's finalisation
and migration were done on Claude Opus 4.8. Don't erase or overstate that history; it's recorded
honestly in `docs/METHODOLOGY.md` and Appendix D.
