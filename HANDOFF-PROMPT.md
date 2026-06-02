# Weight of Nations — Handoff Prompt

*Paste everything below the line into a fresh Claude Code session to resume the project. (For the
detailed internal handoff, the assistant should read `HANDOFF.md` — this is just the bootstrap.)*

---

You are picking up **The Shifting Weight of Nations** — a published, *living* data essay on five
centuries of world-GDP shares (8th edition, v8.5). The author is Hulki Okan Tabak; you are the
**Code executor** half of the project's dual architecture (a chat-advisor plans/ratifies; you
build/commit).

**Get the project.** Either this handoff zip is already extracted (the repo is the
`weight-of-nations/` folder), or clone it:
`git clone https://github.com/hulkiokantabak/weight-of-nations.git`

**Read first**, in order: `HANDOFF.md` (the entry point) → `skills/weight-of-nations/SKILL.md` (the
orchestrator: the ten invariants, the file map, the four-document loop, the self-update mechanism)
→ `docs/source-research.md` (the verified numbers — never re-derive). The three project skills are
also installed globally under `~/.claude/skills/`; the repo is the source of truth, so re-copy from
`skills/` if you edit them.

**Session-start ritual:**
- `cd build && python check_consistency.py` → expect **52 passed, 0 FAILED**.
- On **Windows** (this project's current machine): use the Windows CPython (not the mingw one that
  the pango package installs); set `$env:PYTHONUTF8="1"` and
  `$env:WEASYPRINT_DLL_DIRECTORIES="C:\msys64\mingw64\bin"`; run `python build/win_fonts.py` once for
  faithful PDF body fonts. Full notes: `docs/README-rebuild.md` §1b.
- Run `conversation_search`/transcript search for "Weight of Nations" to recover any context not in
  the repo. Then surface open items, propose the session's work, and **await the author's
  confirmation** before substantive changes.

**Current state (2026-06-02):** Published. One source of truth (`build/data.py` + the manuscript)
renders the editions in `outputs/`: interactive HTML, print PDF **with cover**, print **interior**
PDF (no cover), and an **audio/TTS** PDF — plus the standalone cover PNG in `build/covers/`. (These
have distinct uses: the with-cover file is the reader's book; the no-cover interior + the cover PNG
suit publishers like Google Books that take a cover separately; the audio strips tables/figures for
Speechify/Peech.) Live site: **https://hulkiokantabak.github.io/weight-of-nations/** (auto-redeploys
on push via `.github/workflows/pages.yml`). Masthead reads "Eighth edition"; the book carries its
own web link (page 1 + Appendix F). Suite 52/0; `main` in sync.

**Golden rules (do not break):** numbers live only in `build/data.py`; prose only in the manuscript
(→ `content.py` via `parse_manuscript.py`). Never hand-edit a rendered edition — edit source, re-run
the builders. Label every GDP-share claim with **ruler + vintage + uncertainty**. *Directions, not
decimals*, reopen the prose, and only through the panel. One change → one commit; commit and push
per `GROUND-RULES.md`. When a rendered value is wrong, grep the **generated** artifact (`content.py`)
and the parser, not only the source.

**Next to-dos (panel-prioritized — see `HANDOFF.md` §6 and `docs/LOG.md`):**
1. **Dry-run the living-update workflow** before the **October 2026 IMF WEO** — the living promise's
   first real test (`update_data.py --validate` → suite → rebuild → PR).
2. **Fork-readiness:** turn `CONTRIBUTING.md` into a concrete fork → edit `build/data.py` → suite →
   rebuild → open-a-PR walkthrough; add a `.gitattributes` (cross-platform line endings); enable repo
   Settings → Actions → write + allow PRs (so the living-update workflow can open PRs).
3. **Zero-fallback print master** before any paid print run — render on Linux/CI (the Windows PDF
   carries minor Lucida/Corsiva edge-glyph fallbacks).
4. **Keep `data/claim-registry.md` + `docs/source-research.md` in sync** on each data refresh.
5. **Website improvements** (author-deferred — keep ruler discipline on the landing page).
