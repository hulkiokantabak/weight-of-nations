# -*- coding: utf-8 -*-
"""Parse the Seventh-Edition manuscript (.md) into content.SECTIONS blocks.
Faithful: prose is taken verbatim; only structure is mapped. Figures map to the
existing 16 chart renderers (resequenced) + 6 new coda renderers."""
import re, pprint, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("WON_MANUSCRIPT", os.path.join(HERE, "..", "manuscript", "the-shifting-weight-of-nations.md"))
OUT = os.path.join(HERE, "content.py")

FIGKEY = {1:"long_bar",2:"long_area",3:"mfg",4:"nom",5:"us",6:"mult",7:"share24",
          8:"gap24",9:"mult24",10:"scatter24",11:"jp",12:"bloc",13:"delta",14:"swing24",
          15:"world_long",16:"world_modern",17:"scenario_space",18:"cone",
          19:"scenario_bars",20:"demography",21:"dollar",22:"multiplier_shift"}
FIGSUB = {17:"Conceptual map \u2014 not a data plot",
          18:"Illustrative scenario \u2014 not a forecast",
          19:"Illustrative scenario \u2014 not a forecast",
          20:"Projection \u00b7 UN WPP 2024 (medium variant)",
          21:"Illustrative scenario \u2014 not a forecast",
          22:"Illustrative scenario \u2014 not a forecast"}

ACR = {"US","UK","EU","PPP","GDP","FX","AI","UN","IMF","WDI","II","I","USSR","NYU","B1","B2","B3"}
SMALL = {"the","of","and","a","an","to","vs","for","in","on","by","with","from","as","at","but","or","nor"}

def _cap(w):
    w = re.sub(r'[A-Za-z]+', lambda m: m.group(0).capitalize(), w)
    w = re.sub(r"'([A-Za-z]+)", lambda m: "'" + m.group(1).lower(), w)
    return w

def titlecase(s):
    words = s.split(" "); out = []; prev = ""
    for i, w in enumerate(words):
        is_first = (i == 0) or prev in {"\u2014", "\u2013", ":"} or prev.endswith(":")
        bare = re.sub(r'[^A-Za-z]', '', w)
        if bare and bare.upper() in ACR:
            out.append(w.upper())
        elif (not is_first) and bare.lower() in SMALL:
            out.append(w.lower())
        else:
            out.append(_cap(w))
        prev = w
    return " ".join(out)

def esc_amp(s): return s.replace("&", "&amp;")

def inline(s):
    """markdown -> inline HTML (escape &, then bold, then italic). No raw < > in source."""
    s = s.strip().replace("&", "&amp;")
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    return s

# ---- read + locate masthead vs body ----
raw = open(SRC, encoding="utf-8").read().split("\n")
idx_hyp = next(i for i, l in enumerate(raw) if l.strip() == "## HYPOTHESIS")
mast_lines = raw[:idx_hyp]
body_lines = raw[idx_hyp:]

# ---- masthead ----
h1 = mast_lines[0].lstrip("#").strip()
standfirst = ""
dateline = []; byline = ""
for l in mast_lines[1:]:
    t = l.strip()
    if not standfirst and re.match(r'^\*[^*].*\*$', t):
        standfirst = inline(t)
        continue
    m = re.match(r'^\*\*(.+?)\*\* (.+)$', t)
    if m:
        label, val = m.group(1), m.group(2)
        if "Directed" in label:
            byline = inline(label + " " + val)
        else:
            dateline.append((label, inline(val)))
masthead = {"k": "masthead",
            "kicker": "A data essay \u00b7 economic history \u00b7 eighth edition",
            "h1": h1, "standfirst": standfirst, "byline": byline, "dateline": dateline}

# ---- tokenize body ----
SECTIONS = [masthead]
state = "front"
cur_section = ""
arg = {}; arg_key = None
pend_country = []   # §15
pend_concl = []     # §18
last_head = False

def flush():
    global pend_country, pend_concl
    if pend_country:
        SECTIONS.append({"k": "country", "items": pend_country}); pend_country = []
    if pend_concl:
        SECTIONS.append({"k": "conclusions", "items": pend_concl}); pend_concl = []

i = 0; N = len(body_lines)
while i < N:
    ln = body_lines[i]; t = ln.strip()
    if t == "" or t == "---":
        i += 1; continue

    # headings
    if t.startswith("#"):
        flush()
        level = len(t) - len(t.lstrip("#"))
        text = t.lstrip("#").strip()
        if level == 1:  # the coda divider
            parts = text.split(" \u00b7 ", 1)
            num = titlecase(parts[0]); title = titlecase(parts[1]) if len(parts) > 1 else ""
            SECTIONS.append({"k": "section", "num": num, "title": esc_amp(title)})
            state = "coda"; cur_section = num; last_head = True; i += 1; continue
        # level 2
        if text in ("HYPOTHESIS", "APPROACH", "IN ONE LINE"):
            arg_key = text; last_head = True; i += 1; continue
        if text.startswith("SECTION "):
            m = re.match(r'^SECTION (\S+) \u00b7 (.+)$', text)
            num = f"Section {m.group(1)}"; title = titlecase(m.group(2))
            SECTIONS.append({"k": "section", "num": num, "title": esc_amp(title)})
            state = "body"; cur_section = num; last_head = True; i += 1; continue
        if text.startswith("APPENDIX "):
            m = re.match(r'^APPENDIX (\S+) \u00b7 (.+)$', text)
            num = f"Appendix {m.group(1)}"; title = titlecase(m.group(2))
            SECTIONS.append({"k": "section", "num": num, "title": esc_amp(title)})
            state = "appendix"; cur_section = num; last_head = True; i += 1; continue
        if text == "THE WORLD THIS ESSAY DIVIDES":
            SECTIONS.append({"k": "section", "num": "Totals", "title": "The World This Essay Divides"})
            state = "front"; cur_section = "Totals"; last_head = True; i += 1; continue
        if text == "HOW TO READ THIS ESSAY":
            SECTIONS.append({"k": "section", "num": "Reading", "title": "How to Read This Essay"})
            state = "front"; cur_section = "Reading"; last_head = True; i += 1; continue
        # otherwise: coda subsection -> h3
        SECTIONS.append({"k": "h3", "t": esc_amp(titlecase(text))})
        last_head = True; i += 1; continue

    # figure callout
    mf = re.match(r'^\[\*\*FIGURE (\d+)\*\*\s*[\u2014\u2013-]+\s*(.+)\]\s*$', t)
    if mf:
        flush()
        num = int(mf.group(1)); desc = mf.group(2).strip()
        if ". " in desc:
            title, caption = desc.split(". ", 1)
        else:
            title, caption = desc, ""
        blk = {"k": "fig", "key": FIGKEY[num], "num": f"Fig. {num:02d}",
               "title": inline(title), "sub": inline(FIGSUB.get(num, "")), "caption": inline(caption)}
        if num == 4:
            blk["controls"] = True
        SECTIONS.append(blk); last_head = False; i += 1; continue

    # table
    if t.startswith("|"):
        flush()
        rowlines = []
        while i < N and body_lines[i].strip().startswith("|"):
            rowlines.append(body_lines[i].strip()); i += 1
        rows = []
        for rl in rowlines:
            cells = [c.strip() for c in rl.strip("|").split("|")]
            rows.append(cells)
        def issep(r): return all(re.match(r'^:?-{2,}:?$', (c or "-")) for c in r)
        rows = [r for r in rows if not issep(r)]
        headers = [inline(c) for c in rows[0]]
        data = [[inline(c) for c in r] for r in rows[1:]]
        SECTIONS.append({"k": "table", "headers": headers, "rows": data})
        last_head = False; continue

    # blockquote
    if t.startswith(">"):
        flush()
        ql = []
        while i < N and body_lines[i].strip().startswith(">"):
            ql.append(body_lines[i].strip().lstrip(">").strip()); i += 1
        qt = " ".join(x for x in ql if x)
        if "share of world GDP" in qt:
            SECTIONS.append({"k": "identity"})
        else:
            SECTIONS.append({"k": "pull", "t": inline(qt)})
        last_head = False; continue

    # paragraph (single line)
    para = t
    # argument capture
    if arg_key is not None:
        arg[arg_key] = inline(para); arg_key = None
        if len(arg) == 3:
            SECTIONS.append({"k": "argument", "hyp": arg["HYPOTHESIS"],
                             "approach": arg["APPROACH"], "concl": arg["IN ONE LINE"]})
            arg = {}
        last_head = False; i += 1; continue

    # §15 country cards
    if cur_section == "Section 15":
        mc = re.match(r'^\*\*([^*]+)\*\* \u2014 (.+)$', para)
        if mc:
            name = mc.group(1).strip(); rest = mc.group(2)
            if ". " in rest:
                stat, bdy = rest.split(". ", 1)
            else:
                stat, bdy = rest, ""
            pend_country.append((name, inline(stat), inline(bdy)))
            last_head = False; i += 1; continue

    # §18 conclusions
    if cur_section == "Section 18":
        mn = re.match(r'^\*\*(\d+) \u00b7 (.+?)\*\* (.+)$', para)
        if mn:
            pend_concl.append((inline(mn.group(2)), inline(mn.group(3))))
            last_head = False; i += 1; continue
        else:
            flush()  # the trailing summary paragraph

    # italic-only standfirst right after a heading -> lede
    if last_head and re.match(r'^\*[^*].*\*$', para):
        SECTIONS.append({"k": "lede", "t": inline(para)})
    else:
        SECTIONS.append({"k": "p", "t": inline(para)})
    last_head = False; i += 1

flush()

# ---- write content.py ----
hdr = ("# -*- coding: utf-8 -*-\n"
       "# AUTO-GENERATED from the Seventh-Edition manuscript by parse_manuscript.py.\n"
       "# Edit the manuscript + re-run the parser; do not hand-edit.\n"
       "SECTIONS = ")
with open(OUT, "w", encoding="utf-8") as f:
    f.write(hdr + pprint.pformat(SECTIONS, width=118, sort_dicts=False) + "\n")

# ---- quick report ----
from collections import Counter
ct = Counter(b["k"] for b in SECTIONS)
figs = [b for b in SECTIONS if b["k"] == "fig"]
print("blocks:", len(SECTIONS))
print("by type:", dict(ct))
print("figures:", len(figs), "->", [b["num"].split()[-1] for b in figs])
print("tables:", ct["table"], " sections:", ct["section"], " country items:",
      sum(len(b["items"]) for b in SECTIONS if b["k"] == "country"),
      " conclusions:", sum(len(b["items"]) for b in SECTIONS if b["k"] == "conclusions"))
