# -*- coding: utf-8 -*-
"""common.py — render content.SECTIONS blocks to HTML. Shared by both builders.
The only per-format difference is the chart element, passed in as fig_inner(key)."""
import data as D

_RCLS = {"nom":"nom","ppp":"","mix":"mix"}

def _is_long_table(b):
    """A table tall enough to span more than one printed page. Such a table must be
    allowed to break (break-inside:auto in print) and must never be pulled into a
    keep-with-next group — doing so would re-strand its heading on an otherwise-empty
    page (the orphan this module exists to prevent). The thresholds isolate the single
    multi-page reference table; every other table stays kept-together."""
    if b.get("k") != "table":
        return False
    rows = b.get("rows") or []
    chars = sum(len(c) for r in rows for c in r)
    return len(rows) >= 15 or chars >= 2500

def block_html(b, fig_inner):
    k = b["k"]

    if k == "masthead":
        dl = "".join(f"<span><b>{l}</b> {v}</span>" for l, v in b["dateline"])
        by = f'<p class="byline">{b["byline"]}</p>' if b.get("byline") else ""
        return (f'<header class="masthead"><p class="kicker">{b["kicker"]}</p>'
                f'<h1>{b["h1"]}</h1><p class="standfirst">{b["standfirst"]}</p>'
                f'{by}<div class="dateline">{dl}</div></header>')

    if k == "argument":
        return ('<section class="argument">'
                f'<div class="arg-row"><span class="arg-tag">Hypothesis</span><p>{b["hyp"]}</p></div>'
                f'<div class="arg-row"><span class="arg-tag">Approach</span><p>{b["approach"]}</p></div>'
                f'<div class="arg-row"><span class="arg-tag">In one line</span><p>{b["concl"]}</p></div>'
                '</section>')

    if k == "identity":
        return ('<div class="identity"><div class="idt">'
                '<span class="idt-lhs">share of<br>world GDP</span><span class="idt-eq">=</span>'
                '<span class="idt-box b-pop">share of world<br><b>population</b></span><span class="idt-x">\u00d7</span>'
                '<span class="idt-box b-price"><b>price level</b><br><span class="idt-sub">the ruler</span></span><span class="idt-x">\u00d7</span>'
                '<span class="idt-box b-prod"><b>productivity</b><br><span class="idt-sub">output per person<br>vs the world</span></span>'
                '</div><p class="idt-note">Population \u2014 why old Asia was \u201chuge.\u201d &nbsp;Price level \u2014 the whole nominal-vs-PPP gap. &nbsp;Productivity \u2014 what the essay is about.</p></div>')

    if k == "section":
        return f'<div class="section-head"><span class="num">{b["num"]}</span><h2>{b["title"]}</h2></div>'
    if k == "lede":
        return f'<p class="lede">{b["t"]}</p>'
    if k == "p":
        return f'<p>{b["t"]}</p>'
    if k == "h3":
        return f'<h3>{b["t"]}</h3>'
    if k == "pull":
        return f'<div class="pull">{b["t"]}</div>'

    if k == "callout":
        intro = f'<p class="callout-intro">{b["intro"]}</p>' if b.get("intro") else ""
        if "cols" in b:
            cols = "".join(f"<div><h4>{h}</h4><p>{p}</p></div>" for h, p in b["cols"])
            inner = f'<div class="two-col">{cols}</div>'
        else:
            inner = f'<p>{b.get("body","")}</p>'
        return (f'<div class="callout"><span class="tag">{b["tag"]}</span>'
                f'<h3>{b["title"]}</h3>{intro}{inner}</div>')

    if k == "scenarios":
        cards = ""
        for name, lab, body, watch in b["items"]:
            cards += (f'<div class="scn"><div class="scn-h"><span class="scn-name">{name}</span>'
                      f'<span class="scn-lab">{lab}</span></div>'
                      f'<p class="scn-body">{body}</p>'
                      f'<p class="scn-watch"><span>Watch</span> {watch}</p></div>')
        return f'<div class="scenarios">{cards}</div>'

    if k == "fig":
        ctrl = ('<div class="controls"><button class="btn" id="westBtn" aria-pressed="false">'
                '+ Show the \u201cWest\u201d bloc (US + EU + UK + Japan)</button></div>') if b.get("controls") else ""
        return (f'<div class="figure" id="fig_{b["key"]}">'
                f'<div class="fig-head"><div><div class="fig-num">{b["num"]}</div>'
                f'<div class="fig-title">{b["title"]}</div></div></div>{ctrl}'
                f'<p class="fig-sub">{b["sub"]}</p>{fig_inner(b["key"])}'
                f'<p class="fig-caption">{b["caption"]}</p></div>')

    if k == "table_marker":
        rows = ""
        for ent, ppp, nomt, noms in D.MARKER:
            rows += (f'<tr><td class="claim">{ent}</td><td>{ppp}%</td>'
                     f'<td>${nomt}T</td><td>{noms}%</td></tr>')
        return ('<div class="tbl-wrap"><table>'
                '<caption>IMF 2025\u201326 marker \u2014 PPP share, nominal size, nominal share</caption>'
                '<thead><tr><th>Entity</th><th>PPP share</th><th>Nominal GDP</th><th>Nominal share</th></tr></thead>'
                f'<tbody>{rows}</tbody></table></div>'
                f'<p class="tbl-foot">World nominal \u2248 ${D.WORLD_NOMINAL_T}T. Nominal shares computed from IMF current-dollar GDP; EU+UK is a constructed sum. A current marker only \u2014 deliberately not stitched into the long-run series.</p>')

    if k == "table_audit":
        rows = ""
        for claim, ruler, rcls, verdict in D.AUDIT:
            rows += (f'<tr><td class="claim">{claim}</td>'
                     f'<td><span class="measure {_RCLS[rcls]}">{ruler}</span></td>'
                     f'<td>{verdict}</td></tr>')
        return ('<div class="tbl-wrap"><table>'
                '<caption>What he said, which ruler he used, and what the sources show</caption>'
                '<thead><tr><th>His claim</th><th>Ruler</th><th>Verdict &amp; the figures</th></tr></thead>'
                f'<tbody>{rows}</tbody></table></div>')

    if k == "conclusions":
        lis = ""
        for i, (lead, body) in enumerate(b["items"], 1):
            lis += f'<li><span class="cn-n">{i:02d}</span><div><b>{lead}</b> {body}</div></li>'
        return f'<ol class="concl-list">{lis}</ol>'

    if k == "sources":
        lis = "".join(f"<li>{x}</li>" for x in b["items"])
        return ('<section class="sources"><div class="section-head" style="margin-top:0">'
                '<span class="num">Method</span><h2>Sources &amp; how to read this</h2></div>'
                f'<ul class="src-list">{lis}</ul><footer>{b["footer"]}</footer></section>')

    if k == "table":
        _classes = []
        if b.get("cls"):
            _classes.append(b["cls"])
        if _is_long_table(b):
            _classes.append("longtable")
        cls = (" " + " ".join(_classes)) if _classes else ""
        cap = f'<caption>{b["caption"]}</caption>' if b.get("caption") else ""
        head = "".join(f"<th>{h}</th>" for h in b["headers"])
        rows = ""
        for r in b["rows"]:
            tds = "".join((f'<td class="claim">{cell}</td>' if i == 0 else f"<td>{cell}</td>")
                          for i, cell in enumerate(r))
            rows += f"<tr>{tds}</tr>"
        foot = f'<p class="tbl-foot">{b["foot"]}</p>' if b.get("foot") else ""
        return (f'<div class="tbl-wrap{cls}"><table>{cap}'
                f'<thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>{foot}')

    if k == "country":
        cards = ""
        for name, stat, body in b["items"]:
            cards += (f'<div class="cty"><div class="cty-h"><span class="cty-name">{name}</span>'
                      f'<span class="cty-stat">{stat}</span></div>'
                      f'<p class="cty-body">{body}</p></div>')
        return f'<div class="country">{cards}</div>'

    if k == "colophon":
        intro = f'<p class="colo-intro">{b["intro"]}</p>' if b.get("intro") else ""
        rows = "".join(f'<div class="colo-row"><span class="colo-k">{kk}</span>'
                       f'<div class="colo-v">{vv}</div></div>' for kk, vv in b["rows"])
        return (f'<section class="colophon"><span class="tag">{b.get("tag","Colophon")}</span>'
                f'<h3>{b["title"]}</h3>{intro}<div class="colo-rows">{rows}</div></section>')

    return ""

def body_html(fig_inner):
    """Render blocks, grouping a sub-head or caption-lead with the figure OR table it
    introduces so print pagination never strands a heading on the page before its
    block (keep-with-next). Long tables are deliberately excluded — they are meant to
    break across pages, and binding one would re-create the very orphan this avoids;
    an h3 immediately before a long table relies on h3{break-after:avoid} instead.
    The wrapper is inert on screen; in print it carries break-inside:avoid."""
    S = __import__("content").SECTIONS
    n = len(S)
    out = []
    i = 0
    def short_intro(b):
        return b.get("k") in ("p", "lede") and len(b.get("t") or "") < 360
    def caption_lead(b):
        # a heading/caption paragraph that introduces a figure or a (non-long) table
        return b.get("k") in ("p", "lede") and len(b.get("t") or "") < 420
    def bindable(b):
        # the kinds a heading/caption may keep-with: a figure, a NON-long table, or scenarios
        k = b.get("k")
        if k in ("fig", "table_marker", "table_audit", "scenarios"):
            return True
        if k == "table":
            return not _is_long_table(b)
        return False
    while i < n:
        b = S[i]
        k = b.get("k")
        # group starting at an h3 sub-head: h3 [+ up to 2 short intros] [+ the fig/table it introduces]
        if k == "h3":
            grp = [b]; j = i + 1
            while j < n and short_intro(S[j]) and (j - i) <= 2:
                grp.append(S[j]); j += 1
            if j < n and bindable(S[j]):
                grp.append(S[j]); j += 1
            elif len(grp) == 1 and j < n and not (S[j].get("k") == "table" and _is_long_table(S[j])):
                grp.append(S[j]); j += 1        # heading keeps at least its first following block
            inner = "".join(block_html(x, fig_inner) for x in grp)
            out.append(f'<div class="keepwith">{inner}</div>')
            i = j; continue
        # group a caption-lead paragraph that sits immediately before a figure or table
        if caption_lead(b) and i + 1 < n and bindable(S[i + 1]):
            inner = block_html(b, fig_inner) + block_html(S[i + 1], fig_inner)
            out.append(f'<div class="keepwith">{inner}</div>')
            i += 2; continue
        out.append(block_html(b, fig_inner))
        i += 1
    return "\n".join(out)
