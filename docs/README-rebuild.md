# README — rebuilding the editions from source

The pipeline lives in `build/`. A fresh container needs Python deps + the fonts staged,
then three build commands. `content.py` is already generated; you only re-parse the
manuscript if you edit it.

## 1 · Dependencies
```bash
pip install weasyprint fonttools brotli pypdf cairosvg pyspellchecker matplotlib numpy
```
(Renderers used by the pipeline that are normally already present: `pdftoppm` (poppler) and
`montage` (ImageMagick) for QA rasterization — not required for the build itself.)

## 1b · Windows (MSYS2 GTK + UTF-8)

The pure-Python parts (the 52-check suite, the parser, the interactive HTML) work on Windows with
just `pip install weasyprint fonttools brotli pypdf matplotlib numpy` and the **Windows CPython**
interpreter (`python`). Two extra steps enable the **PDF/audio** editions:

- **WeasyPrint native libs.** WeasyPrint needs GTK/Pango. Install MSYS2 (`winget install --source
  winget MSYS2.MSYS2`), then the Pango stack:
  `C:\msys64\usr\bin\bash -lc "pacman -S --needed --noconfirm mingw-w64-x86_64-pango"`. Point
  WeasyPrint at the DLLs with `WEASYPRINT_DLL_DIRECTORIES=C:\msys64\mingw64\bin`, and keep calling
  the **Windows** CPython explicitly (the pango package pulls a *mingw* Python that would otherwise
  shadow it on `PATH`). *(If pacman can't verify mirror TLS on a fresh MSYS2, set its `XferCommand`
  to `curl … -k`; package GPG signatures are still verified by `SigLevel = Required`.)*
- **Console encoding.** `check_consistency.py` self-reconfigures stdout to UTF-8; if you run other
  scripts that print non-ASCII, set `PYTHONUTF8=1`.
- **Known residual:** the body font (IBM Plex Sans) can fall back under fresh MSYS2 fontconfig
  (rendered PDF ~3 pp long); the canonical committed PDF is the faithful reference (see
  `docs/LOG.md` O-03).

## 2 · Stage the fonts

**(a) TTF for matplotlib charts + cairosvg covers** — register with fontconfig:
```bash
mkdir -p ~/.fonts && cp build/ttf/*.ttf ~/.fonts/ && fc-cache -f
```
`charts.py` also loads them directly from `build/ttf/` by relative path, so run the build
from inside `build/`.

**(b) WOFF2 for the WeasyPrint PDF (@font-face)** — `build_pdf.py` now loads them from the
bundled repo path **`build/fonts/@fontsource`** by default (no copying needed). Override with the
`WON_FONTS_DIR` env var if your woff2 live elsewhere.

The interactive **HTML** uses Google Fonts via CDN (no local fonts needed) and inlines the
6 coda figures as base64, so it is self-contained once built.

## 3 · Build
```bash
cd build
python3 build_pdf.py      # renders all 22 chart PNGs (charts.render_all) → assets/, then the PDF
python3 build_html.py      # 16 Chart.js canvases + 6 inlined coda PNGs → self-contained HTML
python3 build_audio.py     # TTS-optimized PDF
```
Outputs land in `outputs/` by default (override with `WON_OUTPUT_DIR`):
`the-shifting-weight-of-nations.pdf`, `the-shifting-weight-of-nations.html`, `the-shifting-weight-of-nations-audio.pdf`.

## 4 · Regenerate content from the manuscript (only if you edit prose)
`content.py` is auto-generated. To change prose, edit
`manuscript/the-shifting-weight-of-nations.md`, then:
```bash
# in parse_manuscript.py, set SRC to the manuscript path you're using, then:
cd build && python3 parse_manuscript.py    # rewrites content.py
```
The parser prints a block/figure/table report; expect **22 figures**, **20 tables**, **28 sections**.

## 5 · Covers (optional)
```bash
cd build/covers && python3 make_covers.py   # 5 programmatic SVG→PNG alt-covers (1600×2400) → build/covers/
```

## 6 · Quick verify after a build
```bash
cd ../outputs
grep -oc 'class="chart-img"' the-shifting-weight-of-nations.html   # expect 6
grep -oc '<canvas' the-shifting-weight-of-nations.html             # expect 16
grep -c '222.8' the-shifting-weight-of-nations.html                # present (corrected PPP)
python3 - <<'PY'
from pypdf import PdfReader
t="".join((p.extract_text() or "") for p in PdfReader("the-shifting-weight-of-nations.pdf").pages)
print("leaks:", "<cite" in t, "{SW(" in t)            # both False
for s in ["222.8","$170","The cone of outcomes","Demographic destiny","Long Plateau"]:
    print("OK" if s in t else "MISS", s)
PY
```
