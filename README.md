# The Shifting Weight of Nations

[![Deploy Pages](https://github.com/hulkiokantabak/weight-of-nations/actions/workflows/pages.yml/badge.svg)](https://github.com/hulkiokantabak/weight-of-nations/actions/workflows/pages.yml)
[![Living update](https://github.com/hulkiokantabak/weight-of-nations/actions/workflows/living-update.yml/badge.svg)](https://github.com/hulkiokantabak/weight-of-nations/actions/workflows/living-update.yml)
[![Prose & data: CC BY 4.0](https://img.shields.io/badge/prose%20%26%20data-CC--BY--4.0-green.svg)](./LICENSE.md)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](./LICENSE.md)

A skeptical, interactive data essay on five centuries of world-GDP shares — and a **living document** that rebuilds itself when the numbers change. One source of truth renders three editions: interactive, print, and screen-reader.

**Directed by Hulki Okan Tabak; written by Claude 4.8 and Hulki Okan Tabak.**

## Read It

- **Read online (interactive edition):** **<https://hulkiokantabak.github.io/weight-of-nations/>**
- **The book (PDF, with cover):** [`the-shifting-weight-of-nations-with-cover.pdf`](outputs/the-shifting-weight-of-nations-with-cover.pdf)
- **Print interior (PDF, no cover):** [`the-shifting-weight-of-nations.pdf`](outputs/the-shifting-weight-of-nations.pdf)
- **Audio / screen-reader edition (TTS):** [`the-shifting-weight-of-nations-audio.pdf`](outputs/the-shifting-weight-of-nations-audio.pdf)
- **Cover art (PNG):** [`build/covers/…-cover.png`](build/covers/the-shifting-weight-of-nations-cover.png)
- **Project:** [Changelog](CHANGELOG.md) · [Charter](CHARTER.md) · [Contributing](CONTRIBUTING.md) · [Citation](CITATION.cff)

## What It Is

A long-form essay that takes a memorable claim about the changing economic weight of nations (originating from a Stephen Kotkin / Hoover *Uncommon Knowledge* conversation) and subjects it to scrutiny rather than repeating or debunking it. Its spine:

> A nation's share of world GDP is **population × price-level × productivity**. People switch silently between two rulers — market-rate **nominal** and price-adjusted **PPP** — and between *size* and *prosperity*. Separate the rulers, divide out population, and five centuries of rise and fall collapse onto one durable variable: **productivity**.

Reading rule: **read the ruler first, the direction second, and the decimal point last.**

## The Editions

One source of truth (`build/data.py` + the manuscript) renders every edition, so the formats can never drift. The three PDFs have **distinct uses**:

| Edition | File | For |
|---|---|---|
| **Interactive** | [live site](https://hulkiokantabak.github.io/weight-of-nations/) · `outputs/…​.html` | reading and exploring in a browser — 16 live figures + a West-bloc toggle |
| **Book (with cover)** | `outputs/…-with-cover.pdf` (63 pp) | the reader's book — download, quote, cite |
| **Print interior (no cover)** | `outputs/…​.pdf` (62 pp) | publishers that attach a cover separately (e.g. Google Books) |
| **Audio / TTS** | `outputs/…-audio.pdf` | spoken-aloud reading — numbers narrated, no tables/figure scaffolding (Speechify, Peech) |
| **Cover** | `build/covers/…-cover.png` | the standalone, high-resolution cover art |

You never hand-edit a rendered edition — edit the source and re-run the builders.

## A Living Document

Editions 1–7 were static documents, rebuilt by hand from one chat to the next. The **eighth edition** is the first to live here, in a public repository whose editions are pure functions of one source. The update mechanism is deliberately **narrow** — it touches only the data file:

- A new **IMF WEO** (April / October), **World Bank WDI**, or **UN WPP** release → numbers updated in **one place** (`build/data.py`).
- A **52-check consistency suite** re-runs and must stay green.
- All editions **rebuild** from the corrected source.
- The **prose is not rewritten** — a method and a set of *directions* don't expire when a denominator is revised. Only a change of *direction* (a plateau becoming a decline; a laggard converging) reopens the argument, and only through the review body.

The automation is in [`.github/workflows/living-update.yml`](.github/workflows/living-update.yml); the field-by-field source map and the update ritual live in [`skills/weight-of-nations-data-refresh/`](skills/weight-of-nations-data-refresh/).

**Three layers, one honest claim.** (1) **Dated editions** for readers and citation (this PDF, the audio, the interactive page); (2) this **living public repository** as the source of truth, with tagged releases; (3) the **Weight of Nations skill**, which codifies the reasoning and is the *interface* to the repo, not a second source of truth. The "living" claim is modest: the editions are dated snapshots; the report **can** be updated — by the author or by contributors via fork/PR — but updating is **optional and promised to no one**. If it is never touched again, the dated snapshot stands as a complete edition; and if the automation ever breaks, the last good PDF plus `build/data.py` is the canonical fallback. The full rationale is in [`docs/living-document.md`](docs/living-document.md); the moral center is [`CHARTER.md`](CHARTER.md).

## Repository Map

```
weight-of-nations/
├── README.md              ← you are here
├── HANDOFF.md             entry point for a new chair / Code session
├── GROUND-RULES.md        operating posture (max effort, no hallucination, references)
├── CHARTER.md             the project's moral center
├── build/                 the single source of truth + the renderers
│   ├── data.py            ALL numbers (+ palette) — the only place numbers live
│   ├── charts.py          22 figure renderers (matplotlib; bundled fonts in ttf/)
│   ├── content.py         AUTO-GENERATED prose blocks (do not hand-edit)
│   ├── parse_manuscript.py  manuscript .md → content.py
│   ├── check_consistency.py the 52-check suite (run before every build)
│   ├── update_data.py     guarded data-refresh harness
│   ├── build_pdf.py / build_html.py / build_audio.py   the three edition renderers
│   ├── build_cover.py     prepend the cover → the with-cover PDF
│   ├── win_fonts.py        Windows-only: faithful IBM Plex Sans for WeasyPrint
│   ├── common.py · ttf/ · fonts/@fontsource/ · covers/
├── manuscript/            the final copy (edit here, then re-parse)
├── outputs/               the rendered editions (interactive, print ±cover, audio)
├── website/               the GitHub Pages site (landing + interactive edition)
├── docs/                  METHODOLOGY · METRICS · LOG · source-research · README-rebuild · living-document
├── data/claim-registry.md ruler-labeled public-claim registry
├── skills/                the three project skills (orchestrator · panel · data-refresh)
├── publication/PUBLISH-GUIDE.md   Google Books / Substack / Medium checklist
└── .github/workflows/     living-update.yml (PR-on-refresh) · pages.yml (deploy the site)
```

## Build It Yourself

Requires Python 3. From a clean checkout:

```bash
# 1. dependencies
pip install weasyprint fonttools brotli pypdf cairosvg pyspellchecker matplotlib numpy img2pdf pillow

# 2. (optional) stage the bundled fonts for matplotlib/WeasyPrint
mkdir -p ~/.fonts && cp build/ttf/*.ttf ~/.fonts/ && fc-cache -f

# 3. build the editions (writes to outputs/ by default; override with WON_OUTPUT_DIR)
cd build
python3 check_consistency.py          # expect: 52 passed, 0 FAILED
python3 build_pdf.py
python3 build_html.py
python3 build_audio.py
python3 build_cover.py                 # the with-cover PDF
```

Re-run `python3 parse_manuscript.py` **only if you changed the prose** in `manuscript/`. On **Windows**, WeasyPrint needs the MSYS2 GTK runtime and a one-time `python build/win_fonts.py` for faithful body fonts — full notes in [`docs/README-rebuild.md`](docs/README-rebuild.md).

## Governance, Contributing & Citation

The author (Hulki Okan Tabak) gatekeeps the **canonical** release (a benevolent-dictator model): `main` and the official editions are the author's approved versions, but **anyone may fork, extend, translate, or open a pull request**. The one rule that governs every contribution — never state a GDP-share claim without labeling the **ruler**, the **source vintage**, and the **uncertainty** — and the contribution lanes are in [`CONTRIBUTING.md`](CONTRIBUTING.md). Public macro-historical claims and their ruler-labeled verdicts live in [`data/claim-registry.md`](data/claim-registry.md).

**Licence:** prose, figures, and data under **CC-BY-4.0**; code under **MIT** — see [`LICENSE.md`](LICENSE.md). **Cite** the dated edition you used; machine-readable metadata is in [`CITATION.cff`](CITATION.cff).

## Provenance & Licence Note

An independent analysis built from a public *Uncommon Knowledge* conversation (guest Stephen Kotkin, host Peter Robinson); not a transcript, an endorsement, or a Hoover publication, and it attributes no specific figure to the conversation. Directed by Hulki Okan Tabak and written by Claude 4.8 with him; the full authorship history across model versions is disclosed in the essay's colophon (Appendix D). Data is drawn from public sources (IMF, World Bank, UN, Maddison, Bairoch), credited in Appendix C and in [`docs/source-research.md`](docs/source-research.md).

*This is analysis and a public essay, **not financial advice**; the scenario coda is explicitly illustrative, not a forecast.*
