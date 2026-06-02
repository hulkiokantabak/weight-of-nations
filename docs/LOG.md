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

## Email scrub · SE-fit · site improvements · governance (2026-06-02)

**Privacy — personal email scrubbed from history (🔒).** A parallel session's GoatCounter commit
(`15e9018`) was authored with the personal gmail. `git filter-branch --env-filter` (range
`667e6dd..HEAD`) rewrote it to the `noreply` address, then `git push --force-with-lease`.
`origin/main` verified clean (every author/committer email is now noreply; file tree byte-identical).
GitHub may cache the old SHA until its own GC. **Standing rule:** every session's git must use
`hotabak@users.noreply.github.com` (global config) — and `main` is now branch-protected (below).

**iPhone SE 3rd gen — 375 px table fit (W-07, sev 2).** The page fit (no page overflow) but the wide
data tables required sideways swiping. A two-tier mobile compaction (`@media ≤600 px` font .84rem /
pad 8·11; `≤400 px` font .76rem / pad 6·8) + `-webkit-overflow-scrolling:touch` now fits most tables;
**1–2 genuinely wide 4-column reference tables still scroll** (inherent at 375 px — a zero-scroll fix
needs a stacked-card / `table-layout:fixed` restructure, offered to the author, not imposed).
`build_html.py`, presentation-only.

**Website improvements + governance (author-directed; landing + `CONTRIBUTING` only).** Implemented
the chosen menu (A/B/C/D/F) plus the author's seven site asks:
editions reframed and differentiated (Read online · Download PDF · Read-aloud TTS — the online edition
no longer mis-sold as a separate "interactive" thing; "Audio" → "Read-aloud (text-to-speech)");
hero payoff line; a status block (edition + data vintages + last-updated + what-changed); Sources now
**links** IMF/World Bank/UN/Maddison + the Kotkin interview + the claim registry + source-research, with
a PPP-uncertainty note; a **"Read it elsewhere"** section (Google Books/Substack/Medium/X/LinkedIn,
labelled dated snapshots vs the living canonical) + JSON-LD `sameAs`; a "5-minute version" path +
reading times; a **version-history (tags)** link (editions are never overwritten); an explicit
**canonical-control** line. `CONTRIBUTING` gained a data-update quickstart, an editions-versioning
section, and a canonical-control section.

**Canonical safeguard (🔒).** `main` branch protection enabled via API (force-push + deletion blocked;
no PR gate, so the author's own pushes still work). With GitHub's model (only the owner can push; forks
are separate repos) the canonical edition and site can be altered **only by the author**; a fork can
copy/extend freely under CC-BY but can never take over the original. *(A focused, "explore-only"
interactive edition was scoped but deferred on cost, at the author's direction.)*

---

## Cross-device display audit — small-iPhone reading fix (2026-06-02)

Triggered by "reads poorly on an older small iPhone." The website-experts panel designed the audit
(5-round prep), the checks ran across a device matrix (320–1440 + landscape + 200% + reduced-motion +
dark), fixes shipped, and a 3-round post-mortem followed. **Presentation-only; data, charts, prose,
PDF, and audio editions untouched; suite 52/0.**

| # | Catch | Sev | Where | Resolution | Standing rule |
|---|---|---|---|---|---|
| W-03 | **Interactive edition overflowed horizontally at ≤347 px** (320 px iPhone): live Chart.js canvases fell back to their 300 px HTML default instead of the 222 px box, pushing the page to 349 px. | 3 | edition (build_html.py) | Post-build `rAF → Chart.getChart().resize()` nudge + `.chart-box canvas{max-width:100%}` + `body{overflow-x:hidden}`. Charts now fit the box at every width. | 🔒 responsive canvases can fall back to 300 px — guard with resize() + max-width + page overflow-x:hidden. |
| W-04 | **Edition faint text `#8C8273` = 3.3:1** — fails WCAG AA. | 2 | edition | Darkened to `#6E6456` (~5:1), matching the landing. | 🔒 faint UI text ≥4.5:1 on paper. |
| W-05 | **Figure rise-animation had no reduced-motion guard.** | 2 | edition | `@media (prefers-reduced-motion:reduce){.figure{opacity:1;transform:none;animation:none}}`. | 🔒 every animation carries a reduced-motion guard. |

**Method learning (🔒).** A CSS/JS-only edit to a *generated* edition is safe to ship only after a
temp-dir rebuild is **byte-identical** to the committed artifact (the feasibility gate). Confirmed here
before editing `build_html.py`; the post-edit diff was confined to the 4 CSS lines + 1 JS line, data
byte-unchanged.

**Repo-hygiene learning (🔒).** To un-track a file while keeping it on disk: `git rm --cached` then a
**bare** `git commit` — never `git reset` after (re-tracks it), never `git commit <pathspec>` (re-adds
the working-tree copy). `website/edition.html` is now genuinely un-tracked (two earlier attempts had
silently failed). **Multi-seat:** when another session pushes to `main` mid-flight (the GoatCounter
commit), **rebase, never force-push.**

**Flagged for the author (privacy, out of panel scope).** Commit `15e9018` (GoatCounter, another
session) is authored `hotabak@gmail.com` — the personal email is now in public commit history. Earlier
audit was correct at the time; this landed afterward. Fix options: scrub via history-rewrite +
force-push, or set that session's git to the `noreply` address and leave history. Not actioned here.

---

## Website improvement session — panels + landing-layer pass (2026-06-02)

A standalone website round, **no edition / manuscript / data / PDF change**. The **website-experts**
panel (Vinh chair, 5 rounds) and the **Weight-of-Nations** panel (Compass chair, 5 rounds) ran
separately; a joint 5-round session (chair: Code) ratified a landing-layer list. Shipped to
`website/` only:

- **Self-hosted fonts.** The landing loaded Google Fonts render-blocking though the exact 7 woff2
  already ship in the repo — now self-hosted from `website/assets/fonts/` (faster, private, durable).
  The interactive *edition* keeps its own stack — untouched.
- **Image weight.** Hero cover 2.98 MB PNG → 210 KB JPEG; added a composed 1200×630 Open Graph card;
  removed the duplicate `website/assets/cover.png` (canonical stays in `build/covers/`).
- **A11y floor** (Soueidan): `:focus-visible` outlines, AA-contrast faint text
  (`#857B6C`→`#6E6456`, ≈3.7→≈5:1), `theme-color`, `prefers-reduced-motion` gating of smooth scroll.
- **Identity / discoverability:** favicon (SVG + PNG monogram), in-style `404.html`, `robots.txt`,
  `sitemap.xml`, bibliographic JSON-LD + OG/Twitter metadata — **no GDP figures** (Parity/Numéraire:
  ruler discipline applies to metadata too).
- **The body behind the aggregate** (Hearth): one ruler-aware human sentence on the landing, drawn
  from the essay's register, no decimal.

| # | Catch | Sev | Where | Resolution | Standing rule |
|---|---|---|---|---|---|
| W-01 | **A second Pages job in `living-update.yml` deployed the raw edition as `index.html`** on any push to `build/data.py` — a data refresh would silently replace the landing page with the bare edition. | 3 | CI/website | Removed the job + its `pages`/`id-token` perms; `pages.yml` is the sole deployer. | 🔒 one deployer for the site; rebuild workflows open PRs, they don't deploy. |
| W-02 | **2.98 MB hero PNG + an 813 KB tracked `edition.html` duplicate** (byte-identical to `outputs/`, overwritten at deploy) bloated the site/repo and could silently drift. | 2 | website | Optimized imagery; un-tracked + gitignored the generated edition copy (deploy / `build_html.py` own it). | 🔒 don't track a file the deploy regenerates; ship imagery at display resolution. |

**Security/privacy audit (same day).** The public repo carries **no keys, no private email** (commits
use the GitHub `noreply` address; `hotabak@gmail.com` never appears in tree or history), **no machine
username**, no stray secret files; CI uses the built-in `GITHUB_TOKEN` via scoped permissions. Added a
secret-blocking `.gitignore`, a `SECURITY.md`, and a gitignored `local-notes/`. Recommendation on
record: **keep the process docs (handoff / ground-rules / skills) public** — nothing private, and
transparency + fork-readiness are the project's brand; a one-command private-split recipe is staged in
`local-notes/PRIVATE-SPLIT-HOWTO.md`.

---

## Publication round + panel retrospective (2026-06-02)

Published with cover, three editions, and a live site; added the website link to the book (masthead +
Appendix F); corrected the Appendix E self-metrics; compacted the cover (with-cover 5.1→2.6 MB). A
3-round panel retrospective surfaced the prioritized to-dos now in `HANDOFF.md` §6 (dry-run the
living-update before the October 2026 IMF WEO is #1).

**Learning (escalated to practice).** A value that *looks* like it comes from the single source of
truth may be **hardcoded in the generator**: the visible "SEVENTH EDITION" masthead kicker lived in
`parse_manuscript.py`, not the manuscript, so a manuscript-only fix didn't move it. 🔒 Standing rule:
when a *rendered* value is wrong, grep the **generated** artifact (`content.py`) and the parser, not
only the manuscript/data source.

---

## v8.5 — layout (keep-with-next for tables) + living-document prose (2026-06-02)

An author-authorised chat-advisor session generalised the keep-with-next grouper (`build/common.py`)
so a heading/caption-lead binds to a following **table**, not only a figure — fixing four
stranded-heading/caption cases (the scenario-map heading, "What to Watch", and the Appendix B2/B3
captions) plus three further lead+table instances of the same defect, and adding a `longtable` class
so the one multi-page table (Appendix E) breaks across pages with a repeating header instead of
orphaning its heading (typeset PDF 63→62 pp). No data, figure, or direction changed; suite 52/0.
Logged for the trail — a presentation defect (stranded headings), not a data catch. Severity 1–2.

---

## Living-repository operations — Windows portability (2026-06-02)

Migrating the bundle to a Windows workstation surfaced two **operational** catches in the build
tooling — neither in the data nor the prose. Both are environment-portability issues; the canonical
editions and the 52-check suite were unaffected.

| # | Catch | Sev | Where | Resolution | Standing rule |
|---|---|---|---|---|---|
| O-02 | **`check_consistency.py` crashed on a Windows console.** The multiplier check prints `≈` (U+2248); the default cp1252 console codec raised `UnicodeEncodeError` and aborted the suite mid-run — a platform quirk, not a data error. | 3 | build tooling | Reconfigure stdout/stderr to UTF-8 at startup (commit `8003029`); suite runs on any platform without a `PYTHONUTF8` env var. Still 52/0. | 🔒 build entry points must not assume a UTF-8 console. |
| O-03 | **PDF/audio fell back to system fonts off the authoring box.** `build_pdf.py` defaulted `FONTS` to a stale authoring path (`/home/claude/…`) present on no checkout, so the bundled woff2 were never used by default; its `@font-face` `src` also used a POSIX-only `file://` URL (malformed on Windows). | 3 | build tooling | Default `FONTS` to the bundled repo path; emit URLs via `pathlib.Path(p).as_uri()` (commit `020eaa6`). Fraunces + IBM Plex Mono now embed cross-platform. | 🔒 bundled assets are addressed by repo-relative path + portable URIs, never an absolute authoring path. |

**Residual (open).** On a freshly-installed MSYS2 Pango/fontconfig (WeasyPrint's Windows native
stack), the body font **IBM Plex Sans** can still fall back: the @fontsource per-weight files name
each weight as a distinct internal family (`IBM Plex Sans` / `…Medium` / `…SemiBold`), which that
stack mis-matches against the single `@font-face` family `Plex` (the rendered PDF runs ~3 pages
long). Display (Fraunces) and mono (Plex Mono) are unaffected. The **canonical committed PDF is the
faithful reference** (built on the original pipeline); a Windows-faithful rebuild is a follow-up.
Recorded so it is not rediscovered.

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
