# Contributing

Thank you for your interest in *The Shifting Weight of Nations*. This is a public, reproducible
report; contributions that improve its accuracy, clarity, and reach are welcome — within a
discipline that protects the project's measurement integrity and voice.

## Governance (BDFL — start closed, open gradually)

The author (Hulki Okan Tabak) is the maintainer and the gatekeeper of the **canonical** release.

- The `main` branch and the official Google Books / Substack / Medium editions are the author's
  **approved** releases. Only the author merges to the canonical manuscript and `build/data.py`.
- **Anyone may fork** — swap in alternative datasets, build new visual modules, translate, or
  extend. That is encouraged.
- **Pull requests** are reviewed against the project invariants and the ruler rule (below).
- For the project's first ~12–18 months the author controls all merges; the gates open wider as
  CI checks, templates, and a small trusted reviewer circle mature. Designed disagreement is not
  an editable comments section.

## The one rule that governs every contribution

**Never state or change a GDP-share claim without labeling the ruler.** Every number must carry:
its **ruler** (nominal current-dollar / PPP-international-dollar / population share / multiplier
/ bloc construction), its **source vintage**, and its **uncertainty**. A figure true on one
ruler is routinely false on another — splicing rulers, or hiding a dataset break, is the one
thing that breaks the project.

## Contribution lanes

- **Good first issue** — broken link, typo, unclear wording.
- **Data issue** — a new IMF/WDI/UN release, a source mismatch, a country-code problem. Follow
  the data-refresh ritual (`skills/weight-of-nations-data-refresh`): **re-pull the whole series
  from one vintage; never patch only the latest year.**
- **Chart issue** — an unclear visual, a better denominator, a missing bloc.
- **Claim issue** — a public claim that needs a ruler-labeled audit (add it to
  `data/claim-registry.md` and `build/data.py`'s `AUDIT`).
- **Essay issue** — prose, structure, explanation, accessibility. A change of *direction* (not
  just decimals) is a new analytical edition and goes through the review panel first.

## Definition of done (every PR)

1. Source changed in the **right place only** — numbers in `build/data.py`, prose in the
   manuscript. **Never hand-edit a rendered edition.**
2. New numbers recorded in `docs/source-research.md` with source, vintage, and URL.
3. `cd build && python3 check_consistency.py` → **52 passed, 0 FAILED** (add a check if your
   change implies a new standing rule).
4. The three editions rebuild clean (re-run `parse_manuscript.py` only if prose changed).
5. The change is classified **patch / minor / major** (see `docs/living-document.md` §9); a
   *direction* change is flagged for panel review.
6. `docs/LOG.md` updated if a catch was found; `CHANGELOG.md` updated for any material change.
7. Commit message describes the change; one logical change per PR.

## Updating the data when a new release lands

When the IMF (April / October WEO), the World Bank (WDI), or the UN (WPP) publishes new figures:

1. **Fork** the repository (or branch, if you are the maintainer).
2. **Re-pull the whole series from the new vintage** into `build/data.py` — never patch only the
   latest year, and never splice two vintages of the same ruler. Record the new numbers, with
   source and URL, in `docs/source-research.md`.
3. `cd build && python check_consistency.py` → **52 passed, 0 FAILED**.
4. Rebuild the editions: `python build_pdf.py && python build_html.py && python build_audio.py`
   (run `parse_manuscript.py` first **only** if you changed prose).
5. Decide **decimals vs direction**: a refreshed denominator that leaves every *direction* intact
   is a *minor* release (bump the version, update `CHANGELOG.md`); a changed *direction* is a new
   analytical *edition* and goes through the review panel first.
6. Bump the version, tag the release, and **open a pull request** — the living-update workflow
   opens one automatically on a `build/data.py` change. The full ritual is in
   `skills/weight-of-nations-data-refresh`.

## Editions are versioned, never overwritten

Every edition is a **tagged release** (`v8.0`, `v8.1`, …). A refresh adds a new tag; it does not
erase the old one. The dated PDF and the data file at each tag stay readable on GitHub indefinitely,
and the site links its [version history](https://github.com/hulkiokantabak/weight-of-nations/tags).
An old edition remains a complete, citable artifact even after a newer one ships.

## Canonical control (what a fork can and cannot do)

The licence (CC-BY-4.0) lets anyone fork, copy, translate, or re-publish — that is encouraged. But
the **canonical** edition, the `main` branch, and the official site
(`hulkiokantabak.github.io/weight-of-nations`) are altered **only by the author**. A fork is a
separate repository: it may go its own way, but it cannot change this one or take over this site.
Updating the canonical is the author's prerogative alone; `main` is branch-protected against
force-pushes and deletion.

## What not to submit

- Unsupported forecasts presented as data.
- Partisan "who is winning" claims without ruler labels.
- Stitched long-run series that hide dataset breaks.
- Exact-looking decimals beyond what a weak historical source can bear.
- Investment advice or policy prescription without uncertainty language.
