# -*- coding: utf-8 -*-
"""build_pdf.py — render the print/PDF edition with weasyprint, from the same
content + data + the matplotlib charts. Output to outputs/ (override with WON_OUTPUT_DIR)."""
import os, glob
from pathlib import Path
import data as D
import common
import charts

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.environ.get("WON_FONTS_DIR", os.path.join(HERE, "fonts", "@fontsource"))
OUTDIR = os.environ.get("WON_OUTPUT_DIR", os.path.join(HERE, "..", "outputs"))
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "the-shifting-weight-of-nations.pdf")

def _ff(family, rel, weight="400", style="normal"):
    p = os.path.join(FONTS, rel)
    if not os.path.exists(p):
        g = glob.glob(p)
        p = g[0] if g else None
    if not p:
        return ""
    return (f"@font-face{{font-family:'{family}';font-weight:{weight};font-style:{style};"
            f"src:url('{Path(p).as_uri()}') format('woff2');}}\n")

FONT_FACES = "".join([
    _ff("Fraunces","fraunces/files/fraunces-latin-400-normal.woff2","400","normal"),
    _ff("Fraunces","fraunces/files/fraunces-latin-600-normal.woff2","600","normal"),
    _ff("Fraunces","fraunces/files/fraunces-latin-400-italic.woff2","400","italic"),
    _ff("Plex","ibm-plex-sans/files/ibm-plex-sans-latin-400-normal.woff2","400","normal"),
    _ff("Plex","ibm-plex-sans/files/ibm-plex-sans-latin-500-normal.woff2","500","normal"),
    _ff("Plex","ibm-plex-sans/files/ibm-plex-sans-latin-600-normal.woff2","600","normal"),
    _ff("PlexMono","ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2","400","normal"),
])

PRINT_CSS = """
:root{
  --paper:#F4EEE2;--paper-2:#FBF7EF;--card:#FCFAF4;--ink:#221C17;--ink-soft:#52493F;--ink-faint:#857B6C;
  --rule:#D7CCB9;--rule-soft:#E7DECF;--accent:#993C1D;
  --us:#A23B26;--cn:#C0851F;--eu:#2F5573;--in:#2E8B6F;--jp:#8A4F7D;--uk:#B96E37;--ru:#62702F;--row:#9C9285;
}
@page{ size:A4; margin:17mm 16mm 18mm 16mm;
  @bottom-left{ content:"The Shifting Weight of Nations"; font-family:'PlexMono',monospace; font-size:7.5pt; color:#9C9285; }
  @bottom-right{ content:counter(page); font-family:'PlexMono',monospace; font-size:7.5pt; color:#9C9285; }
}
@page:first{ @bottom-left{content:""} @bottom-right{content:""} }
*{box-sizing:border-box}
html{font-size:10.6pt}
body{margin:0;color:var(--ink);background:#fff;font-family:'Plex',sans-serif;line-height:1.5;}
p{margin:0 0 .72em;orphans:2;widows:2;}
h1,h2,h3,h4{font-family:'Fraunces',Georgia,serif;font-weight:600;color:var(--ink);}
i,em{font-style:italic}
b,strong{font-weight:600}
a{color:var(--accent);text-decoration:none}

.masthead{padding:6mm 0 5mm;border-bottom:1.5pt solid var(--accent);margin-bottom:7mm}
.kicker{font-family:'PlexMono',monospace;font-size:8pt;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);margin:0 0 5mm}
h1{font-size:30pt;line-height:1.04;letter-spacing:-.01em;margin:0 0 3mm}
h1 em{font-style:italic;font-weight:400;color:var(--accent)}
.standfirst{font-family:'Fraunces',serif;font-style:italic;font-size:13.5pt;line-height:1.4;color:var(--ink-soft);margin:0 0 5mm;max-width:34em}
.dateline{font-family:'PlexMono',monospace;font-size:8.2pt;color:var(--ink-faint);border-top:.6pt solid var(--rule);padding-top:3mm;line-height:1.6}
.dateline span{margin-right:7mm}.dateline b{color:var(--ink-soft);font-weight:500}

.argument{border:.8pt solid var(--rule);border-radius:3pt;background:var(--paper-2);margin:0 0 7mm;break-inside:avoid}
.arg-row{padding:3.6mm 5mm;border-bottom:.6pt solid var(--rule-soft)}
.arg-row:last-child{border-bottom:none}
.arg-tag{display:block;font-family:'PlexMono',monospace;font-size:7.6pt;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin-bottom:1.4mm}
.arg-row p{margin:0;font-size:10.4pt}
.arg-row:last-child p{font-family:'Fraunces',serif;font-style:italic;font-size:11.6pt;color:var(--ink)}

.section-head{margin:8mm 0 1mm;break-before:page;break-after:avoid}
.keepwith{break-inside:avoid}
.section-head .num{font-family:'PlexMono',monospace;font-size:8pt;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
h2{font-size:19pt;line-height:1.1;margin:1mm 0 2.5mm;break-after:avoid}
h3{font-size:13pt;margin:5mm 0 1.5mm;break-after:avoid}
.lede{font-size:10.8pt;color:var(--ink-soft);margin:0 0 3mm}

.identity{margin:4mm 0;padding:6mm 5mm;background:var(--card);border:.8pt solid var(--rule);border-radius:3pt;text-align:center;break-inside:avoid}
.idt{}
.idt-lhs,.idt-eq,.idt-x,.idt-box{display:inline-block;vertical-align:middle}
.idt-lhs{font-family:'Fraunces',serif;font-size:10pt;line-height:1.2;margin:0 2mm}
.idt-eq,.idt-x{font-family:'Fraunces',serif;font-size:15pt;color:var(--ink-faint);margin:0 2mm}
.idt-box{font-size:8.4pt;line-height:1.25;color:var(--ink-soft);padding:3mm 4mm;border-radius:3pt;border:.8pt solid var(--rule);margin:1mm}
.idt-box b{font-family:'Plex';font-weight:600;color:var(--ink);font-size:9.4pt}
.idt-sub{font-size:7.4pt;color:var(--ink-faint)}
.b-pop{background:rgba(98,112,47,.10)}.b-price{background:rgba(47,85,115,.10)}.b-prod{background:rgba(153,60,29,.10);border-color:rgba(153,60,29,.35)}
.idt-note{font-size:8.6pt;color:var(--ink-faint);margin:4mm auto 0;max-width:40em}

.callout{background:var(--paper-2);border:.8pt solid var(--rule);border-left:2.4pt solid var(--accent);border-radius:2pt;padding:5mm 6mm;margin:6mm 0;break-inside:avoid}
.callout h3{margin-top:0}
.callout .tag{font-family:'PlexMono',monospace;font-size:7.6pt;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:1.5mm}
.callout-intro{font-size:10pt}
.two-col{display:table;width:100%;border-spacing:5mm 0;margin-top:1mm}
.two-col>div{display:table-cell;width:50%;vertical-align:top}
.two-col h4{font-size:11pt;margin:0 0 1mm}
.two-col p{font-size:9.2pt;color:var(--ink-soft);margin:0}

.figure{margin:5mm 0 4mm;background:var(--card);border:.8pt solid var(--rule);border-radius:3pt;padding:4.5mm 5mm 4mm;break-inside:avoid}
.fig-num{font-family:'PlexMono',monospace;font-size:7.8pt;letter-spacing:.14em;color:var(--accent);text-transform:uppercase}
.fig-title{font-family:'Fraunces',serif;font-weight:600;font-size:12.5pt;line-height:1.12;margin:.6mm 0 .4mm}
.fig-sub{font-size:8.6pt;color:var(--ink-faint);margin:0 0 3mm}
.fig-sub .hint{display:none}
.controls{display:none}
.chart-img{width:100%;height:auto;display:block;border:.6pt solid var(--rule-soft);border-radius:2pt;background:#fff}
.fig-caption{font-size:8.4pt;color:var(--ink-soft);line-height:1.5;margin:3mm 0 0}
.fig-caption b{color:var(--ink)}

.scenarios{display:table;width:100%;border-spacing:3mm 0;margin:5mm 0}
.scn{display:table-cell;width:33.33%;vertical-align:top;background:var(--card);border:.8pt solid var(--rule);border-top:2.4pt solid var(--accent);border-radius:2pt;padding:3.5mm}
.scn-name{display:block;font-family:'Fraunces',serif;font-weight:600;font-size:11.5pt}
.scn-lab{font-family:'PlexMono',monospace;font-size:7pt;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.scn-body{font-size:8.4pt;color:var(--ink-soft);margin:2mm 0}
.scn-watch{font-size:7.8pt;color:var(--ink-faint);margin:0;border-top:.6pt solid var(--rule-soft);padding-top:1.5mm}
.scn-watch span{display:block;font-family:'PlexMono',monospace;font-size:6.8pt;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin-bottom:.6mm}

.tbl-wrap{margin:5mm 0 1mm;border:.8pt solid var(--rule);border-radius:3pt;break-inside:avoid;overflow:hidden}
.tbl-wrap.longtable{break-inside:auto;overflow:visible}
.tbl-wrap.longtable table{break-inside:auto}
.tbl-wrap.longtable tr{break-inside:avoid}
.tbl-wrap.longtable thead{display:table-header-group}
table{border-collapse:collapse;width:100%;background:var(--card);font-size:9pt}
caption{caption-side:top;text-align:left;font-family:'Fraunces',serif;font-weight:600;font-size:11.5pt;padding:3.5mm 4mm 2mm}
th,td{padding:2.4mm 4mm;text-align:left;border-bottom:.6pt solid var(--rule-soft);vertical-align:top}
thead th{font-family:'PlexMono',monospace;font-size:7.6pt;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-faint);font-weight:400;background:var(--paper-2)}
tbody tr:last-child td{border-bottom:none}
td.claim{font-weight:500;color:var(--ink)}
td .measure{display:inline-block;font-family:'PlexMono',monospace;font-size:7.4pt;letter-spacing:.04em;text-transform:uppercase;padding:.5mm 1.6mm;border-radius:2pt;background:rgba(47,85,115,.1);color:var(--eu)}
td .measure.nom{background:rgba(162,59,38,.1);color:var(--us)}
td .measure.mix{background:rgba(138,79,125,.12);color:var(--jp)}
.tbl-foot{font-size:7.8pt;color:var(--ink-faint);margin:2mm 0 .72em}

.pull{font-family:'Fraunces',serif;font-style:italic;font-weight:500;font-size:15pt;line-height:1.3;color:var(--ink);border-top:1.5pt solid var(--accent);border-bottom:.6pt solid var(--rule);padding:4mm 0;margin:6mm 0;break-inside:avoid}
.pull span{color:var(--accent)}

.concl-list{list-style:none;padding:0;margin:3mm 0}
.concl-list li{padding:2.6mm 0;border-bottom:.6pt solid var(--rule-soft);break-inside:avoid}
.concl-list li:last-child{border-bottom:none}
.cn-n{float:left;width:9mm;font-family:'PlexMono',monospace;font-size:9.5pt;color:var(--accent)}
.concl-list li>div{margin-left:11mm;font-size:9.6pt;color:var(--ink-soft)}
.concl-list b{font-family:'Fraunces',serif;font-weight:600;font-size:10.4pt;color:var(--ink)}

.sources{margin-top:8mm;border-top:.8pt solid var(--rule);padding-top:4mm}
.sources h2{font-size:15pt}
.src-list{font-size:8.6pt;color:var(--ink-soft);line-height:1.55;padding-left:5mm}
.src-list li{margin-bottom:1.6mm}
footer{margin-top:6mm;padding-top:3mm;border-top:.6pt solid var(--rule);font-family:'PlexMono',monospace;font-size:7.6pt;color:var(--ink-faint);line-height:1.6}

.sw{display:inline-block;width:.66em;height:.66em;border-radius:1.5pt;margin-right:.3em}

.byline{font-family:'Fraunces',serif;font-style:italic;font-size:10.6pt;color:var(--ink);margin:2.5mm 0 0}
.country{margin:3mm 0 1mm}
.cty{padding:2.4mm 0;border-bottom:.6pt solid var(--rule-soft);break-inside:avoid}
.cty:first-child{border-top:.6pt solid var(--rule-soft)}
.cty-h{margin-bottom:.8mm}
.cty-name{font-family:'Fraunces',serif;font-weight:600;font-size:11.4pt;color:var(--ink)}
.cty-stat{font-family:'PlexMono',monospace;font-size:7.6pt;letter-spacing:.02em;color:var(--accent);margin-left:2.5mm}
.cty-body{font-size:9.2pt;color:var(--ink-soft);margin:.7mm 0 0}
.colophon{margin:6mm 0 2mm;background:var(--paper-2);border:.8pt solid var(--rule);border-left:2.4pt solid var(--accent);border-radius:2pt;padding:4.5mm 5mm;break-before:page;break-inside:avoid}
.colophon .tag{font-family:'PlexMono',monospace;font-size:7.6pt;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:1.5mm}
.colophon h3{margin-top:0}
.colo-intro{font-size:9.4pt;color:var(--ink-soft)}
.colo-row{padding:1.8mm 0;border-top:.6pt solid var(--rule-soft)}
.colo-k{display:block;font-family:'PlexMono',monospace;font-size:7.4pt;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-faint);margin-bottom:.6mm}
.colo-v{font-size:9pt;color:var(--ink-soft)}
"""

def fig_inner(key):
    return f'<img class="chart-img" src="assets/{key}.png" alt="{key}">'

def build():
    charts.render_all()  # ensure PNGs are fresh
    body = common.body_html(fig_inner)
    html = (f"<!doctype html><html lang='en'><head><meta charset='utf-8'>"
            f"<style>{FONT_FACES}{PRINT_CSS}</style></head><body>{body}</body></html>")
    from weasyprint import HTML
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    HTML(string=html, base_url=HERE).write_pdf(OUT)
    return OUT, os.path.getsize(OUT)

if __name__ == "__main__":
    p, n = build()
    print("wrote", p, n, "bytes")
