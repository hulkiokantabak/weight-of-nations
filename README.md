# The Shifting Weight of Nations

*A skeptical, interactive data essay on five centuries of world-GDP shares — and a **living
document** that updates itself as the numbers change.*

**Directed and written by Hulki Okan Tabak — with Claude.**

---

## What this is

A long-form essay that takes a memorable claim about the changing economic weight of nations
(originating from a Stephen Kotkin / Hoover *Uncommon Knowledge* conversation) and subjects it
to scrutiny rather than repeating or debunking it. Its spine:

> A nation's share of world GDP is **population × price-level × productivity**. People switch
> silently between two rulers — market-rate **nominal** and price-adjusted **PPP** — and between
> *size* and *prosperity*. Separate the rulers, divide out population, and five centuries of
> rise and fall collapse onto one durable variable: **productivity**.

Reading rule: **read the ruler first, the direction second, and the decimal point last.**

One source of truth renders **three editions**:

- an **interactive** Chart.js page (16 live figures, a West-bloc toggle),
- a **typeset PDF** (WeasyPrint, 63 pages, embedded Fraunces / IBM Plex),
- a **screen-reader** (TTS) PDF.

The finished editions are in [`outputs/`](outputs/).

## Why it's a *living* document

Editions 1–7 were static documents, rebuilt by hand from one chat to the next. The **eighth
edition** is the first to live here, in a public repository whose three editions are pure
functions of one source. The update mechanism is deliberately **narrow**: it touches only the
data file.

- When a new **IMF WEO** (April / October), **World Bank WDI**, or **UN WPP** release lands, the
  numbers are updated in **one place** (`build/data.py`).
- A **52-check consistency suite** re-runs and must stay green.
- All three editions **rebuild** from the corrected source.
- The **prose is not rewritten** — a method and a set of *directions* don't expire when a
  denominator is revised. Only a change of *direction* (a plateau becoming a decline; a laggard
  beginning to converge) reopens the argument, and only through the review body.

The automation lives in [`.github/workflows/living-update.yml`](.github/workflows/living-update.yml);
the ritual and the field-by-field source map live in
[`skills/weight-of-nations-data-refresh/`](skills/weight-of-nations-data-refresh/).

### Three layers, and an honest claim

The project is built as three distinct layers, not one mutating document: (1) **canonical,
dated editions** for readers and citation (Google Books, PDF, EPUB, audio); (2) this **living
public repository** as the source of truth, with tagged releases; and (3) the **Weight of
Nations skill**, which codifies the reasoning and is the *interface* to the repo, not the source
of truth itself.

The "living" claim is deliberately modest and honest: **the canonical editions are dated
snapshots; the report *can* be updated — by the author or by contributors via fork/PR — but
updating is optional and promised to no one.** If it is never touched again, the dated snapshot
stands as a complete, honest edition. And if the automation ever breaks (a dependency dies, a
source URL changes), the **last good PDF plus `build/data.py` is the canonical fallback** — the
frozen edition is the fossil that survives. The full design rationale, the reviews behind it, and
the target structure are in [`docs/living-document.md`](docs/living-document.md); the moral
center is [`CHARTER.md`](CHARTER.md).

## Repository map

```
weight-of-nations/
├── README.md              ← you are here
├── GROUND-RULES.md        operating posture (max effort, no hallucination, references)
├── HANDOFF.md             entry point for a new chair / Code session
├── build/                 the single source of truth + the renderers
│   ├── data.py            ALL numbers (+ palette) — the only place numbers live
│   ├── charts.py          22 figure renderers
│   ├── content.py         AUTO-GENERATED prose (do not hand-edit)
│   ├── parse_manuscript.py  manuscript .md → content.py
│   ├── check_consistency.py the 52-check suite (run before every build)
│   ├── update_data.py     guarded data-refresh harness
│   ├── build_pdf.py / build_html.py / build_audio.py
│   ├── common.py · ttf/ · fonts/ · covers/
├── manuscript/            the final copy (edit here, then re-parse)
├── outputs/               the three rendered editions
├── docs/
│   ├── METHODOLOGY.md     how each edition was made
│   ├── METRICS.md         editions, checks, catches, prompts, survival logic
│   ├── LOG.md             every catch + the standing rule it produced
│   ├── source-research.md the verified numbers (never re-derive)
│   └── README-rebuild.md  environment + build commands
├── skills/                the three project skills (orchestrator · panel · data-refresh)
└── publication/PUBLISH-GUIDE.md   Google Books / Substack / Medium checklist
```

## Build it yourself

Requires Python 3. From a clean checkout:

```bash
# 1. dependencies
pip install weasyprint fonttools brotli pypdf cairosvg pyspellchecker matplotlib numpy

# 2. (optional) stage the bundled fonts for matplotlib/WeasyPrint
mkdir -p ~/.fonts && cp build/ttf/*.ttf ~/.fonts/ && fc-cache -f

# 3. build the three editions (writes to outputs/ by default)
cd build
python3 check_consistency.py          # expect: 52 passed, 0 FAILED
python3 build_pdf.py
python3 build_html.py
python3 build_audio.py
```

Re-run `python3 parse_manuscript.py` **only if you changed the prose** in `manuscript/`. To
write the editions elsewhere, set `WON_OUTPUT_DIR`. Full environment notes in
[`docs/README-rebuild.md`](docs/README-rebuild.md).

## Governance, contributing, and citation

The author (Hulki Okan Tabak) is the maintainer and the gatekeeper of the **canonical** release
(a benevolent-dictator model): the `main` branch and the official editions are the author's
approved versions, but **anyone may fork, extend, translate, or open a pull request**. The one
rule that governs every contribution — never state a GDP-share claim without labeling the ruler,
the source vintage, and the uncertainty — and the contribution lanes are in
[`CONTRIBUTING.md`](CONTRIBUTING.md). Public macro-historical claims and their ruler-labeled
verdicts live in [`data/claim-registry.md`](data/claim-registry.md).

**Licence (recommended, pending the author's confirmation):** prose, figures, and data under
**CC-BY-4.0**; code under **MIT** — see [`LICENSE.md`](LICENSE.md). **Cite** the dated edition
you used; machine-readable metadata is in [`CITATION.cff`](CITATION.cff).

## The golden rule

There is **one source of truth** — the modules in `build/`. Numbers live only in `data.py`;
prose lives only in the manuscript. **You never hand-edit the HTML, the PDF, or the audio
edition.** Edit the source and re-run the builders, so the three formats can never drift.

## Provenance & licence

An independent analysis built from a public *Uncommon Knowledge* conversation (guest Stephen
Kotkin, host Peter Robinson); not a transcript, an endorsement, or a Hoover publication, and it
attributes no specific figure to the conversation. The argument and prose are the author's; the
authorship history across model versions is disclosed in the essay's colophon (Appendix D). Data
is drawn from public sources (IMF, World Bank, UN, Maddison, Bairoch) credited in Appendix C and
in [`docs/source-research.md`](docs/source-research.md).

*This is analysis and a public essay, not financial advice; the scenario coda is explicitly
illustrative, not a forecast.*
