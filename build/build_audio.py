# -*- coding: utf-8 -*-
"""build_audio.py — the "audio edition": one clean, TTS-optimized PDF built from the
SAME content.py source as the visual editions.

Why it exists: when the visual PDF is fed to Speechify / Pitch / a screen reader, the
numbers never get spoken — they live inside charts and grids the voice skips, while the
prose stays qualitative. This edition fixes that. Every crucial figure and table is
rendered as a spoken-number NARRATION paragraph (no images, no grids — tables become
sentences). A `narration` field on a block overrides its visual text; otherwise the
number-rich caption is cleaned and spoken. Output: the-weight-of-nations-audio.pdf.
"""
import os, re, html
import data as D
import content
from build_pdf import FONT_FACES

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.environ.get("WON_OUTPUT_DIR", os.path.join(HERE, "..", "outputs"))
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "the-shifting-weight-of-nations-audio.pdf")

# ----------------------------------------------------------------- TTS cleaner
def tts(s):
    """Clean a content string into speakable text: drop markup, expand units/symbols."""
    if s is None:
        return ""
    s = str(s)
    s = re.sub(r'<span class="sw"[^>]*></span>\s*', '', s)   # colour swatches -> nothing
    s = re.sub(r'<[^>]+>', '', s)                            # any other tags -> inner text
    s = html.unescape(s)                                     # &amp; &times; -> & ×
    # money / magnitudes
    s = re.sub(r'\$(\d+(?:\.\d+)?)\s*[Tt]\b', r'$\1 trillion', s)   # $126T -> $126 trillion
    s = re.sub(r'(\d+(?:\.\d+)?)\s*bn\b', r'\1 billion', s)         # 9.7bn -> 9.7 billion
    # approximations
    s = re.sub(r'~\s*(\d)', r'about \1', s)                  # ~18 -> about 18
    s = s.replace('\u2248', 'about ')                        # ≈
    # ranges & dashes
    s = re.sub(r'(\d)\s*\u2013\s*(\d)', r'\1 to \2', s)      # 2025–26 -> 2025 to 26
    s = s.replace('\u2013', ', ')                            # en-dash -> pause
    s = s.replace('\u2014', ', ')                            # em-dash -> pause
    s = s.replace('\u00b7', ', ')                            # middle dot -> pause
    # symbols
    s = s.replace('\u00d7', ' times ')                       # ×
    s = s.replace('\u2192', ' to ')                          # →
    s = s.replace('\u2153', 'one third')                     # ⅓
    s = s.replace('%', ' percent')
    # tidy
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s+([.,;:])', r'\1', s)
    s = re.sub(r'(,\s*){2,}', ', ', s)
    s = re.sub(r'\s{2,}', ' ', s).strip()
    return s

def esc(s):
    return html.escape(s, quote=False)

def P(text, cls=None):
    text = tts(text)
    if not text:
        return ""
    c = f' class="{cls}"' if cls else ""
    return f"<p{c}>{esc(text)}</p>"

# ----------------------------------------------------------------- block -> spoken HTML
def render(b):
    k = b.get("k")

    if k == "masthead":
        dl = {lab: val for lab, val in b["dateline"]}
        out = [f'<h1>{esc(tts(b["h1"]))}</h1>']
        out.append(P(b["kicker"], "kick"))
        out.append(P(b["standfirst"], "stand"))
        out.append('<p class="aud">An audio edition — figures and tables read aloud with their numbers.</p>')
        if b.get("byline"):
            out.append(P(b["byline"], "by"))
        insp = dl.get("Inspired by")
        if insp:
            out.append(P(f"Inspired by {insp}.", "by"))
        ed = dl.get("Edition")
        span = dl.get("Span")
        tail = []
        if span: tail.append(f"Spanning {span}")
        if ed: tail.append(ed.replace("·", "edition,"))
        if tail:
            out.append(P(". ".join(tail) + ".", "by"))
        return "\n".join(x for x in out if x)

    if k == "argument":
        return "\n".join([
            P(f"Hypothesis. {b['hyp']}"),
            P(f"Approach. {b['approach']}"),
            P(f"In one line. {b['concl']}"),
        ])

    if k == "identity":
        return P("The spine of the essay is one identity. A country's share of world GDP "
                 "equals its share of world population, times the price level — the ruler you "
                 "measure with — times its productivity, meaning output per person relative to "
                 "the world. Population is why old Asia looked huge; the price level is the whole "
                 "nominal-versus-PPP gap; productivity is what the essay is about.")

    if k == "section":
        num = tts(b.get("num", ""))
        title = tts(b["title"])
        lead = f"{num}. " if num else ""
        return f'<h2>{esc(lead + title)}</h2>'

    if k == "lede":
        return P(b.get("narration") or b["t"], "lede")
    if k == "p":
        return P(b.get("narration") or b["t"])
    if k == "h3":
        return f'<h3>{esc(tts(b["t"]))}</h3>'
    if k == "pull":
        return P(b.get("narration") or b["t"], "pull")

    if k == "callout":
        out = [f'<h3>{esc(tts(b["title"]))}</h3>']
        if b.get("intro"):
            out.append(P(b["intro"]))
        if "cols" in b:
            for h, p in b["cols"]:
                out.append(P(f"{h}. {p}"))
        elif b.get("body"):
            out.append(P(b["body"]))
        return "\n".join(out)

    if k == "fig":
        label = tts(b.get("num", "")).replace("Fig.", "Figure")
        title = tts(b["title"])
        body = tts(b.get("narration") or b.get("caption") or "")
        return f'<p class="fig"><span class="lbl">{esc(label)}.</span> {esc(title)}. {esc(body)}</p>'

    if k == "scenarios":
        out = []
        for name, lab, body, watch in b["items"]:
            out.append(P(f"{name} — {lab}. {body} Watch: {watch}", "scn"))
        return "\n".join(out)

    if k == "country":
        out = []
        for name, stat, body in b["items"]:
            out.append(P(f"{name}, {stat}. {body}", "cty"))
        return "\n".join(out)

    if k == "conclusions":
        items = "".join(f"<li>{esc(tts(lead + ' ' + body))}</li>" for lead, body in b["items"])
        return f'<ol class="concl">{items}</ol>'

    if k == "table_marker":
        out = [P("A present-day marker, the IMF's 2025 to 2026 vintage, kept separate from the "
                 "long-run series. World output at market rates is about $126 trillion. For each "
                 "actor: its share of world output on the PPP ruler, its output in trillions of "
                 "dollars at market rates, and its share at market rates.", "tcap")]
        for ent, ppp, nomt, noms in D.MARKER:
            out.append(P(f"{ent}: {ppp} percent on the PPP ruler; "
                         f"{nomt} trillion dollars at market rates; "
                         f"{noms} percent of world output at market rates.", "trow"))
        return "\n".join(out)

    if k == "table_audit":
        out = [P("The audit. For each of Kotkin's claims: the claim, the ruler it leans on, "
                 "and the verdict against the data.", "tcap")]
        for claim, ruler, rcls, verdict in D.AUDIT:
            out.append(P(f"Claim: {claim}. Ruler: {ruler}. {verdict}", "trow"))
        return "\n".join(out)

    if k == "table":
        cap = b.get("caption", "")
        # skip the pure-production metrics/colophon table in the audio edition
        if cap.strip().lower().startswith("inputs, process"):
            return ""
        out = []
        if cap:
            out.append(P(cap, "tcap"))
        # bespoke spoken form for the heavy 2024 numeric table
        if "two rulers and two multipliers" in cap.lower():
            for r in b["rows"]:
                ent = tts(r[0])
                nom = re.sub(r"\..*", "", r[1]); ppp = re.sub(r"\..*", "", r[2]); pop = r[3]
                nomx = tts(r[4]); pppx = tts(r[5])
                out.append(P(f"{ent}: about {nom} percent of world output at market rates, "
                             f"about {ppp} percent on the PPP ruler, and {pop} percent of world "
                             f"population. Its output-per-person multiplier is {nomx} at market "
                             f"rates and {pppx} on PPP.", "trow"))
        else:
            # qualitative tables: speak the subject, then the remaining cells as sentences
            for r in b["rows"]:
                subj = tts(r[0])
                rest = ". ".join(tts(c) for c in r[1:] if str(c).strip())
                out.append(P(f"{subj}. {rest}", "trow"))
        if b.get("foot"):
            out.append(P(b["foot"], "tfoot"))
        return "\n".join(out)

    if k == "sources":
        return P("Sources and method. The essay draws on the Maddison Project for the long run, "
                 "World Bank World Development Indicators for the modern shares, IMF World Economic "
                 "Outlook for the present-day marker, UN World Population Prospects 2024 for "
                 "population, and Bairoch for manufacturing. Throughout, read the direction and the "
                 "order of magnitude, not the decimals; purchasing-power-parity figures carry a "
                 "margin of roughly five to ten percent.", "src")

    if k == "colophon":
        return ""   # production colophon omitted from the spoken edition

    return ""

# ----------------------------------------------------------------- CSS
CSS = """
:root{--paper:#FBF7EF;--ink:#221C17;--ink-soft:#52493F;--ink-faint:#857B6C;--rule:#D7CCB9;--accent:#993C1D;}
@page{ size:A4; margin:20mm 22mm 20mm 22mm; }
*{box-sizing:border-box}
body{ background:#fff; color:var(--ink); font-family:'Plex',sans-serif; font-size:12.2pt;
  line-height:1.72; max-width:none; }
h1{ font-family:'Fraunces',serif; font-weight:600; font-size:25pt; line-height:1.12;
  margin:0 0 4mm; color:var(--ink); }
h2{ font-family:'Fraunces',serif; font-weight:600; font-size:15.5pt; margin:9mm 0 2.5mm;
  padding-top:3mm; border-top:1px solid var(--rule); color:var(--ink); break-after:avoid; }
h3{ font-family:'Fraunces',serif; font-weight:600; font-size:12.5pt; margin:5mm 0 1.5mm; color:var(--ink); break-after:avoid; }
p{ margin:0 0 3.2mm; orphans:2; widows:2; }
p.kick{ font-family:'PlexMono',monospace; font-size:8.4pt; letter-spacing:.08em;
  text-transform:uppercase; color:var(--ink-faint); margin-bottom:2mm; }
p.stand{ font-size:13.5pt; color:var(--ink-soft); line-height:1.5; }
p.aud{ font-family:'PlexMono',monospace; font-size:8.6pt; letter-spacing:.05em;
  color:var(--accent); margin:1mm 0 3mm; }
p.by{ font-size:10.5pt; color:var(--ink-faint); margin-bottom:1mm; }
p.lede{ font-size:13pt; color:var(--ink-soft); }
p.pull{ font-family:'Fraunces',serif; font-style:italic; font-size:13.5pt; color:var(--accent);
  margin:4mm 0; padding-left:5mm; border-left:2px solid var(--rule); }
p.fig{ }
p.fig .lbl{ font-family:'PlexMono',monospace; font-size:10pt; letter-spacing:.04em;
  color:var(--accent); }
p.tcap{ font-weight:500; }
p.trow{ padding-left:5mm; margin-bottom:2mm; }
p.tfoot{ font-size:10.5pt; color:var(--ink-faint); }
p.scn, p.cty{ padding-left:0; }
p.src{ font-size:11pt; color:var(--ink-soft); }
ol.concl{ margin:0 0 3mm; padding-left:7mm; }
ol.concl li{ margin-bottom:2.5mm; }
"""

# ----------------------------------------------------------------- build
def build():
    body = "\n".join(filter(None, (render(b) for b in content.SECTIONS)))
    doc = (f"<!doctype html><html lang='en'><head><meta charset='utf-8'>"
           f"<style>{FONT_FACES}{CSS}</style></head><body>{body}</body></html>")
    from weasyprint import HTML
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    HTML(string=doc, base_url=HERE).write_pdf(OUT)
    return OUT, os.path.getsize(OUT)

if __name__ == "__main__":
    path, size = build()
    print("audio edition:", path, f"{size/1024:.0f} KB")
