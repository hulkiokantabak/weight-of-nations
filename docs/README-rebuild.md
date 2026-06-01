# README — rebuilding the editions from source

The pipeline lives in `build/`. A fresh container needs Python deps + the fonts staged,
then three build commands. `content.py` is already generated; you only re-parse the
manuscript if you edit it.

## 1 · Dependencies
```bash
pip install weasyprint fonttools brotli pypdf cairosvg pyspellchecker matplotlib numpy --break-system-packages
```
(Renderers used by the pipeline that are normally already present: `pdftoppm` (poppler) and
`montage` (ImageMagick) for QA rasterization — not required for the build itself.)

## 2 · Stage the fonts

**(a) TTF for matplotlib charts + cairosvg covers** — register with fontconfig:
```bash
mkdir -p ~/.fonts && cp build/ttf/*.ttf ~/.fonts/ && fc-cache -f
```
`charts.py` also loads them directly from `build/ttf/` by relative path, so run the build
from inside `build/`.

**(b) WOFF2 for the WeasyPrint PDF (@font-face)** — `build_pdf.py` reads them from the
constant `FONTS = "/home/claude/fonts/node_modules/@fontsource"`. Put the bundled woff2
there (preserving the per-family `…/files/` subfolders):
```bash
mkdir -p /home/claude/fonts/node_modules/@fontsource
cp -r build/fonts/@fontsource/* /home/claude/fonts/node_modules/@fontsource/
```
*Or* edit that one line in `build_pdf.py` to point `FONTS` at `build/fonts/@fontsource`.

The interactive **HTML** uses Google Fonts via CDN (no local fonts needed) and inlines the
6 coda figures as base64, so it is self-contained once built.

## 3 · Build
```bash
cd build
python3 build_pdf.py      # renders all 22 chart PNGs (charts.render_all) → assets/, then the PDF
python3 build_html.py      # 16 Chart.js canvases + 6 inlined coda PNGs → self-contained HTML
python3 build_audio.py     # TTS-optimized PDF
```
Outputs land in `/mnt/user-data/outputs/`:
`the-weight-of-nations.pdf`, `the-weight-of-nations.html`, `the-weight-of-nations-audio.pdf`.

## 4 · Regenerate content from the manuscript (only if you edit prose)
`content.py` is auto-generated. To change prose, edit
`manuscript/the-shifting-weight-of-nations.md`, then:
```bash
# in parse_manuscript.py, set SRC to the manuscript path you're using, then:
cd build && python3 parse_manuscript.py    # rewrites content.py
```
The parser prints a block/figure/table report; expect **22 figures** and **3 reference tables**.

## 5 · Covers (optional)
```bash
cd build/covers && python3 make_covers.py   # 5 SVG→PNG covers at 1600×2400 → /mnt/user-data/outputs/
```

## 6 · Quick verify after a build
```bash
cd /mnt/user-data/outputs
grep -oc 'class="chart-img"' the-weight-of-nations.html   # expect 6
grep -oc '<canvas' the-weight-of-nations.html             # expect 16
grep -c '222.8' the-weight-of-nations.html                # present (corrected PPP)
python3 - <<'PY'
from pypdf import PdfReader
t="".join((p.extract_text() or "") for p in PdfReader("the-weight-of-nations.pdf").pages)
print("leaks:", "<cite" in t, "{SW(" in t)            # both False
for s in ["222.8","$170","The cone of outcomes","Demographic destiny","Long Plateau"]:
    print("OK" if s in t else "MISS", s)
PY
```
