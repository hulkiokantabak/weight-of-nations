# -*- coding: utf-8 -*-
"""Five alternative covers for 'The Shifting Weight of Nations' (Google Books, 1600x2400).
Each cover is hand-authored SVG in the book's own type + palette (Fraunces / IBM Plex,
oxblood / paper / steel), drawing on a different idea from the essay. Rendered via cairosvg."""
import os, cairosvg

W, H = 1600, 2400
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("WON_COVERS_DIR", HERE)
os.makedirs(OUT, exist_ok=True)

# ---- palette (from the project) ----
PAPER="#F4EEE2"; PAPER2="#FBF7EF"; CARD="#FCFAF4"
INK="#221C17"; INK_SOFT="#5C534A"; INK_FAINT="#8C8273"
RULE="#DCD2C1"; RULE_SOFT="#E7DECF"; OX="#993C1D"
US="#A23B26"; CN="#C0851F"; EU="#2F5573"; IN="#2E8B6F"; JP="#8A4F7D"; UK="#B96E37"; RU="#62702F"; ROW="#9C9285"
DARK="#1B2530"   # deep steel ground for cover 5

TITLE="Fraunces"; SANS="IBM Plex Sans"; MONO="IBM Plex Mono"

# ---- data (the book's actual series) ----
YEARS=[1500,1600,1700,1820,1870,1913,1950,1973,2000,2024]
LONG_ORDER=["United States","Western Europe","Japan","Russia / USSR","China","India","Rest of world"]
LONG={"United States":[0.3,0.2,0.1,1.8,8.9,19,27,22,21,15],
      "Western Europe":[18,20,22,23,33,33,26,25,20,15],
      "Japan":[3.1,2.9,4.1,3.0,2.3,2.6,3.0,7.7,7,3.4],
      "Russia / USSR":[3.4,3.5,4.4,5.4,7.6,8.6,9.6,9.4,2.7,3.5],
      "China":[25,29,22,33,17,9,4.5,4.6,12,19],
      "India":[24,22,24,16,12,7.5,4.2,3.1,5,8],
      "Rest of world":[26.2,22.4,23.4,17.8,19.2,20.3,25.7,28.2,32.3,36.1]}
CK={"United States":US,"Western Europe":EU,"Japan":JP,"Russia / USSR":RU,"China":CN,"India":IN,"Rest of world":ROW}
WEST=[21.4,23.1,26.2,27.8,44.2,54.6,56.0,54.7,48,33.4]
CHIND=[49,51,46,49,29,16.5,8.7,7.7,17,27]

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def T(x,y,s,size,fill,font=TITLE,weight=None,style=None,anchor="start",ls=None,op=None):
    a=[f'x="{x}"',f'y="{y}"',f'font-family="{font}"',f'font-size="{size}"',f'fill="{fill}"',f'text-anchor="{anchor}"']
    if weight: a.append(f'font-weight="{weight}"')
    if style: a.append(f'font-style="{style}"')
    if ls is not None: a.append(f'letter-spacing="{ls}"')
    if op is not None: a.append(f'opacity="{op}"')
    return f'<text {" ".join(a)}>{esc(s)}</text>'

def smooth(pts):
    """Catmull-Rom -> cubic bezier path through pts."""
    if len(pts)<3:
        d=f'M {pts[0][0]:.1f} {pts[0][1]:.1f} '+" ".join(f'L {x:.1f} {y:.1f}' for x,y in pts[1:]); return d
    d=f'M {pts[0][0]:.1f} {pts[0][1]:.1f} '
    for i in range(len(pts)-1):
        p0=pts[i-1] if i>0 else pts[0]; p1=pts[i]; p2=pts[i+1]; p3=pts[i+2] if i+2<len(pts) else pts[-1]
        c1x=p1[0]+(p2[0]-p0[0])/6.0; c1y=p1[1]+(p2[1]-p0[1])/6.0
        c2x=p2[0]-(p3[0]-p1[0])/6.0; c2y=p2[1]-(p3[1]-p1[1])/6.0
        d+=f'C {c1x:.1f} {c1y:.1f} {c2x:.1f} {c2y:.1f} {p2[0]:.1f} {p2[1]:.1f} '
    return d

# ============================================================ COVER 1 — Two Rulers
def cover_two_rulers():
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    s.append(f'<rect x="46" y="46" width="{W-92}" height="{H-92}" fill="none" stroke="{RULE}" stroke-width="2"/>')
    # kicker + title
    s.append(T(W/2,250,"ECONOMIC HISTORY · A DATA ESSAY",26,INK_FAINT,font=MONO,anchor="middle",ls=7))
    s.append(T(W/2,400,"The Shifting",118,INK,weight=600,anchor="middle"))
    s.append(T(W/2,520,"Weight of Nations",118,INK,weight=600,anchor="middle"))
    # two rulers
    top,bot=760,1840; cx=W/2; gap=150; rw=150
    lx=cx-gap-rw; rx=cx+gap
    def ruler(x,color,topcap):
        g=[f'<rect x="{x}" y="{top}" width="{rw}" height="{bot-top}" fill="{CARD}" stroke="{color}" stroke-width="3"/>']
        n=20
        for i in range(n+1):
            yy=bot-(bot-top)*i/n; major=(i%5==0)
            tl=46 if major else 24
            g.append(f'<line x1="{x}" y1="{yy:.1f}" x2="{x+tl}" y2="{yy:.1f}" stroke="{color}" stroke-width="{2.4 if major else 1.4}"/>')
        return "".join(g)
    s.append(ruler(lx,OX,True)); s.append(ruler(rx,EU,True))
    # ruler captions
    s.append(T(lx+rw/2,top-90,"NOMINAL",30,OX,font=MONO,anchor="middle",ls=4))
    s.append(T(lx+rw/2,top-52,"market rate",27,INK_SOFT,font=TITLE,style="italic",anchor="middle"))
    s.append(T(rx+rw/2,top-90,"PPP",30,EU,font=MONO,anchor="middle",ls=4))
    s.append(T(rx+rw/2,top-52,"real output",27,INK_SOFT,font=TITLE,style="italic",anchor="middle"))
    # the same nation, two heights
    yL=bot-(bot-top)*0.46; yR=bot-(bot-top)*0.74
    s.append(f'<line x1="{lx+rw}" y1="{yL:.1f}" x2="{rx}" y2="{yR:.1f}" stroke="{INK_FAINT}" stroke-width="2" stroke-dasharray="7 6"/>')
    s.append(f'<circle cx="{lx+rw}" cy="{yL:.1f}" r="13" fill="{OX}" stroke="{CARD}" stroke-width="3"/>')
    s.append(f'<circle cx="{rx}" cy="{yR:.1f}" r="13" fill="{EU}" stroke="{CARD}" stroke-width="3"/>')
    s.append(T(cx,(yL+yR)/2-22,"the same nation,",27,INK_SOFT,font=TITLE,style="italic",anchor="middle"))
    s.append(T(cx,(yL+yR)/2+12,"two readings",27,INK_SOFT,font=TITLE,style="italic",anchor="middle"))
    # subtitle + author
    s.append(T(W/2,2010,"Five centuries of world GDP, two rulers,",40,INK_SOFT,font=TITLE,style="italic",anchor="middle"))
    s.append(T(W/2,2068,"and the one variable underneath them both.",40,INK_SOFT,font=TITLE,style="italic",anchor="middle"))
    s.append(f'<line x1="{cx-70}" y1="2150" x2="{cx+70}" y2="2150" stroke="{OX}" stroke-width="3"/>')
    s.append(T(W/2,2250,"HULKI OKAN TABAK",32,INK,font=MONO,anchor="middle",ls=6))
    s.append("</svg>"); return "".join(s)

# ============================================================ COVER 2 — Stacked Centuries
def cover_strata():
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    strata_h=1560
    xs=[i/(len(YEARS)-1)*W for i in range(len(YEARS))]
    # stack top->bottom in this order
    order=["United States","Western Europe","Japan","Russia / USSR","China","India","Rest of world"]
    tops=[0.0]*len(YEARS); 
    for name in order:
        vals=LONG[name]; bots=[tops[i]+vals[i]/100.0*strata_h for i in range(len(YEARS))]
        topline=[(xs[i],tops[i]) for i in range(len(YEARS))]
        botline=[(xs[i],bots[i]) for i in range(len(YEARS))]
        d=smooth(topline)
        # append bottom line reversed
        rev=list(reversed(botline))
        d2=f' L {rev[0][0]:.1f} {rev[0][1]:.1f} '+smooth(rev)[1:]  # smooth returns 'M ...'; strip M
        # simpler: straight down then smooth back
        path=smooth(topline)+f' L {botline[-1][0]:.1f} {botline[-1][1]:.1f} '+ \
             " ".join(f'L {x:.1f} {y:.1f}' for x,y in reversed(botline[:-1]))+" Z"
        s.append(f'<path d="{path}" fill="{CK[name]}" opacity="0.95"/>')
        tops=bots
    # faint vertical year guides
    for i,(x,yr) in enumerate(zip(xs,YEARS)):
        if i in (0,4,len(YEARS)-1):
            s.append(f'<line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="{strata_h}" stroke="{PAPER}" stroke-width="1.5" opacity="0.35"/>')
    # endpoints year labels on strata (light)
    s.append(T(24,strata_h-26,"1500",26,PAPER,font=MONO,ls=3,op=0.9))
    s.append(T(W-24,strata_h-26,"2024",26,PAPER,font=MONO,anchor="end",ls=3,op=0.9))
    # title panel
    py=strata_h
    s.append(f'<rect x="0" y="{py}" width="{W}" height="{H-py}" fill="{PAPER}"/>')
    s.append(f'<rect x="0" y="{py}" width="{W}" height="6" fill="{OX}"/>')
    s.append(T(110,py+118,"FIVE CENTURIES OF WORLD GDP, RE-SLICED",25,OX,font=MONO,ls=5))
    s.append(T(110,py+232,"The Shifting Weight",96,INK,weight=600))
    s.append(T(110,py+330,"of Nations",96,INK,weight=600))
    s.append(T(110,py+408,"Two rulers, and the one variable underneath the numbers.",37,INK_SOFT,font=TITLE,style="italic"))
    s.append(T(110,py+560,"HULKI OKAN TABAK",31,INK,font=MONO,ls=6))
    s.append("</svg>"); return "".join(s)

# ============================================================ COVER 3 — Crossing Curves
def cover_curves():
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER2}"/>')
    s.append(f'<rect x="46" y="46" width="{W-92}" height="{H-92}" fill="none" stroke="{RULE}" stroke-width="2"/>')
    # title
    s.append(T(W/2,300,"THE GREAT DIVERGENCE — AND THE RE-CONVERGENCE",24,INK_FAINT,font=MONO,anchor="middle",ls=5))
    s.append(T(W/2,470,"The Shifting Weight",112,INK,weight=600,anchor="middle"))
    s.append(T(W/2,588,"of Nations",112,INK,weight=600,anchor="middle"))
    # plot
    px0,px1=170,1430; py0,py1=820,1840; vmax=60.0
    def X(i): return px0+(px1-px0)*i/(len(YEARS)-1)
    def Y(v): return py1-(py1-py0)*v/vmax
    # faint baseline grid
    for v in (0,20,40,60):
        yy=Y(v); s.append(f'<line x1="{px0}" y1="{yy:.1f}" x2="{px1}" y2="{yy:.1f}" stroke="{RULE}" stroke-width="1.2"/>')
        s.append(T(px0-18,yy+9,f"{v}%",24,INK_FAINT,font=MONO,anchor="end"))
    westp=[(X(i),Y(WEST[i])) for i in range(len(YEARS))]
    chp=[(X(i),Y(CHIND[i])) for i in range(len(YEARS))]
    s.append(f'<path d="{smooth(westp)}" fill="none" stroke="{OX}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append(f'<path d="{smooth(chp)}" fill="none" stroke="{EU}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
    # endpoints dots
    for (x,y),c in [(westp[-1],OX),(chp[-1],EU),(westp[0],OX),(chp[0],EU)]:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{c}" stroke="{PAPER2}" stroke-width="3"/>')
    # labels
    s.append(T(westp[-1][0]+2,westp[-1][1]-26,"the West",30,OX,font=TITLE,style="italic",anchor="end"))
    s.append(T(chp[-1][0]+2,chp[-1][1]+44,"China + India",30,EU,font=TITLE,style="italic",anchor="end"))
    # year ticks
    for i in (0,4,len(YEARS)-1):
        s.append(T(X(i),py1+42,str(YEARS[i]),26,INK_FAINT,font=MONO,anchor="middle"))
    # subtitle + author
    s.append(T(W/2,2070,"Five centuries of world GDP, two rulers,",38,INK_SOFT,font=TITLE,style="italic",anchor="middle"))
    s.append(T(W/2,2126,"and the one variable underneath.",38,INK_SOFT,font=TITLE,style="italic",anchor="middle"))
    s.append(T(W/2,2270,"HULKI OKAN TABAK",31,INK,font=MONO,anchor="middle",ls=6))
    s.append("</svg>"); return "".join(s)

# ============================================================ COVER 4 — The Identity (ink, typographic)
def cover_identity():
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{INK}"/>')
    s.append(f'<rect x="46" y="46" width="{W-92}" height="{H-92}" fill="none" stroke="#3A322A" stroke-width="2"/>')
    s.append(T(W/2,270,"ECONOMIC HISTORY · A DATA ESSAY",26,INK_FAINT,font=MONO,anchor="middle",ls=7))
    s.append(T(W/2,430,"The Shifting Weight",104,PAPER,weight=600,anchor="middle"))
    s.append(T(W/2,540,"of Nations",104,PAPER,weight=600,anchor="middle"))
    # the identity, stacked
    cx=W/2
    s.append(T(cx,860,"share of world GDP",44,INK_FAINT,font=SANS,anchor="middle"))
    s.append(T(cx,940,"=",46,"#6E6356",font=TITLE,anchor="middle"))
    s.append(T(cx,1100,"population",78,PAPER2,weight=600,anchor="middle"))
    s.append(T(cx,1240,"\u00d7   price level",78,PAPER2,weight=600,anchor="middle"))
    s.append(T(cx,1392,"\u00d7   productivity",92,OX,weight=600,anchor="middle"))
    s.append(f'<line x1="{cx-300}" y1="1430" x2="{cx+300}" y2="1430" stroke="{OX}" stroke-width="2" opacity="0.55"/>')
    s.append(T(cx,1492,"the one variable underneath",30,"#C98A6F",font=MONO,anchor="middle",ls=3))
    # subtitle + author bottom
    s.append(T(W/2,2070,"Five centuries of world GDP, two rulers,",38,"#B9AE9E",font=TITLE,style="italic",anchor="middle"))
    s.append(T(W/2,2126,"and the one variable underneath.",38,"#B9AE9E",font=TITLE,style="italic",anchor="middle"))
    s.append(T(W/2,2270,"HULKI OKAN TABAK",31,PAPER,font=MONO,anchor="middle",ls=6))
    s.append("</svg>"); return "".join(s)

# ============================================================ COVER 5 — The Multiplier Map (dark, geometric)
def cover_diagonal():
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{DARK}"/>')
    # title
    s.append(T(W/2,260,"THE MULTIPLIER — OUTPUT PER PERSON vs THE WORLD",24,"#8FA3B5",font=MONO,anchor="middle",ls=4))
    s.append(T(W/2,430,"The Shifting Weight",104,PAPER,weight=600,anchor="middle"))
    s.append(T(W/2,540,"of Nations",104,PAPER,weight=600,anchor="middle"))
    # square plot
    L=300; Rr=1300; Tp=760; Bp=1760; lim=22.0
    def X(v): return L+(Rr-L)*v/lim
    def Y(v): return Bp-(Bp-Tp)*v/lim
    # grid
    for g in (0,5,10,15,20):
        s.append(f'<line x1="{X(g):.1f}" y1="{Tp}" x2="{X(g):.1f}" y2="{Bp}" stroke="#2C3A48" stroke-width="1.3"/>')
        s.append(f'<line x1="{L}" y1="{Y(g):.1f}" x2="{Rr}" y2="{Y(g):.1f}" stroke="#2C3A48" stroke-width="1.3"/>')
    # parity diagonal
    s.append(f'<line x1="{X(0):.1f}" y1="{Y(0):.1f}" x2="{X(lim):.1f}" y2="{Y(lim):.1f}" stroke="{PAPER}" stroke-width="2.4" stroke-dasharray="9 7" opacity="0.8"/>')
    s.append(T(X(lim)-10,Y(lim)+44,"parity — richer above, poorer below",24,"#9FB1C2",font=TITLE,style="italic",anchor="end"))
    # dots: (pop%, ppp%)
    dots=[("United States",4.2,15.1,US,(14,-10)),("China",17.5,19.7,CN,(16,6)),("India",18.0,8.4,IN,(-14,40)),
          ("Europe",5.6,14.4,EU,(14,-8)),("Japan",1.5,3.4,JP,(16,4)),("Russia",1.8,3.6,RU,(16,28))]
    for name,px,py,c,off in dots:
        x=X(px); y=Y(py)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="22" fill="{c}" opacity="0.22"/>')
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="{c}" stroke="{DARK}" stroke-width="2.5"/>')
        if name in ("United States","China","India"):
            s.append(T(x+off[0],y+off[1],name,28,PAPER,font=SANS,weight=500,anchor=("end" if off[0]<0 else "start")))
    # axis labels
    s.append(T((L+Rr)/2,Bp+70,"share of world population  \u2192",26,"#8FA3B5",font=MONO,anchor="middle"))
    s.append(f'<text x="210" y="{(Tp+Bp)/2}" font-family="{MONO}" font-size="26" fill="#8FA3B5" text-anchor="middle" transform="rotate(-90 210 {(Tp+Bp)/2})">share of world output  \u2192</text>')
    # subtitle + author
    s.append(T(W/2,2070,"Five centuries of world GDP, two rulers,",38,"#AEBDCB",font=TITLE,style="italic",anchor="middle"))
    s.append(T(W/2,2126,"and the one variable underneath.",38,"#AEBDCB",font=TITLE,style="italic",anchor="middle"))
    s.append(T(W/2,2270,"HULKI OKAN TABAK",31,PAPER,font=MONO,anchor="middle",ls=6))
    s.append("</svg>"); return "".join(s)

COVERS=[("cover-1-two-rulers",cover_two_rulers),
        ("cover-2-stacked-centuries",cover_strata),
        ("cover-3-crossing-curves",cover_curves),
        ("cover-4-the-identity",cover_identity),
        ("cover-5-multiplier-map",cover_diagonal)]

for name,fn in COVERS:
    svg=fn()
    open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8").write(svg)
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=f"{OUT}/{name}.png",
                     output_width=W, output_height=H)
    print("rendered", name)
print("done")
