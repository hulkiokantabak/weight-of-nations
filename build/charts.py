# -*- coding: utf-8 -*-
"""charts.py — render all 16 figures as styled PNGs for the PDF, from data.py."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import data as D

P = D.PALETTE
HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets"); os.makedirs(ASSETS, exist_ok=True)
TTF = os.path.join(HERE, "ttf")

# ---- fonts ----
for fn in ["Fraunces-600.ttf","Fraunces-400i.ttf","PlexSans-400.ttf","PlexSans-500.ttf","PlexMono-400.ttf"]:
    p=os.path.join(TTF,fn)
    if os.path.exists(p): fm.fontManager.addfont(p)
def _fp(path, **kw):
    p=os.path.join(TTF,path)
    return fm.FontProperties(fname=p, **kw) if os.path.exists(p) else fm.FontProperties(**kw)
F_TITLE=_fp("Fraunces-600.ttf", size=15)
F_SANS =_fp("PlexSans-400.ttf", size=10.5)
F_SANS5=_fp("PlexSans-500.ttf", size=10.5)
F_MONO =_fp("PlexMono-400.ttf", size=9.5)
try:
    matplotlib.rcParams["font.family"]=fm.FontProperties(fname=os.path.join(TTF,"PlexSans-400.ttf")).get_name()
except Exception:
    pass
matplotlib.rcParams["axes.unicode_minus"]=False

INK=P["ink"]; SOFT=P["ink_soft"]; FAINT=P["ink_faint"]; RULE=P["rule"]; CARD=P["card"]
GRID=(0.13,0.11,0.09,0.10)

def _new(w=7.2,h=4.3):
    fig,ax=plt.subplots(figsize=(w,h),dpi=200)
    fig.patch.set_facecolor(CARD); ax.set_facecolor(CARD)
    return fig,ax

def _style(ax,ymax=None,ypct=True,ystep=None,xlabels=None,xpos=None,ylab=None,xmult=False):
    for s in ["top","right"]: ax.spines[s].set_visible(False)
    for s in ["left","bottom"]: ax.spines[s].set_color(RULE); ax.spines[s].set_linewidth(1.0)
    ax.tick_params(length=0, colors=SOFT)
    ax.yaxis.grid(True,color=GRID,linewidth=1.0); ax.set_axisbelow(True)
    if ymax is not None: ax.set_ylim(0,ymax)
    if ystep is not None and ymax is not None:
        ax.set_yticks(np.arange(0,ymax+0.001,ystep))
    for t in ax.get_yticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    if ypct: ax.yaxis.set_major_formatter(lambda v,_: f"{v:g}%")
    elif xmult: ax.yaxis.set_major_formatter(lambda v,_: f"{v:g}\u00d7")
    if xpos is not None and xlabels is not None:
        ax.set_xticks(xpos); ax.set_xticklabels(xlabels)
    for t in ax.get_xticklabels(): t.set_fontproperties(F_MONO); t.set_color(SOFT)
    if ylab: ax.set_ylabel(ylab,fontproperties=F_SANS,color=SOFT)

def _title(ax,txt): ax.set_title(txt,fontproperties=F_TITLE,color=INK,loc="left",pad=12)
def _legend(ax,ncol,y=-0.16):
    leg=ax.legend(loc="upper center",bbox_to_anchor=(0.5,y),ncol=ncol,frameon=False,
                  prop=F_SANS,handlelength=1.4,columnspacing=1.6,handletextpad=0.5)
    for t in leg.get_texts(): t.set_color(SOFT)
    return leg
def _save(fig,name):
    fig.tight_layout()
    out=os.path.join(ASSETS,name+".png")
    fig.savefig(out,facecolor=CARD,bbox_inches="tight",pad_inches=0.12)
    plt.close(fig); return out

def c(k): return P[k]

# ---------------- Fig 01 stacked bars ----------------
def long_bar():
    fig,ax=_new(7.4,4.6); x=np.arange(len(D.YEARS_LONG)); bottom=np.zeros(len(x))
    for k in D.LONG_ORDER:
        v=np.array(D.LONG[k],float)
        ax.bar(x,v,bottom=bottom,width=0.86,label=k,color=c(D.LONG_COLORKEY[k]),
               edgecolor=CARD,linewidth=0.7)
        bottom+=v
    _style(ax,ymax=100,ystep=20,xlabels=D.YEARS_LONG,xpos=x)
    _title(ax,"World GDP share by region, PPP basis (%)"); _legend(ax,4)
    return _save(fig,"long_bar")

# ---------------- Fig 02 stacked area ----------------
def long_area():
    fig,ax=_new(7.4,4.6); x=np.arange(len(D.YEARS_LONG))
    ys=[np.array(D.LONG[k],float) for k in D.LONG_ORDER]
    cols=[c(D.LONG_COLORKEY[k]) for k in D.LONG_ORDER]
    ax.stackplot(x,ys,labels=D.LONG_ORDER,colors=cols,edgecolor=CARD,linewidth=0.5,alpha=0.92)
    ax.set_xlim(0,len(x)-1)
    _style(ax,ymax=100,ystep=20,xlabels=D.YEARS_LONG,xpos=x)
    _title(ax,"The same five centuries as a re-sliced pie (%)"); _legend(ax,4)
    return _save(fig,"long_area")

# ---------------- Fig 03 manufacturing lines ----------------
def mfg():
    fig,ax=_new(7.4,4.4); x=np.arange(len(D.YEARS_MFG))
    for k in D.MFG_ORDER:
        ax.plot(x,D.MFG[k],marker="o",ms=4.5,lw=2.4,color=c(D.MFG_COLORKEY[k]),
                label=k,mec=CARD,mew=1.0)
    _style(ax,ymax=70,ystep=10,xlabels=D.YEARS_MFG,xpos=x)
    _title(ax,"Share of world manufacturing output, 1750\u20131900 (Bairoch)"); _legend(ax,5)
    return _save(fig,"mfg")

# ---------------- Fig 04 nominal canvas ----------------
def nom():
    fig,ax=_new(7.4,4.5); x=np.arange(len(D.YEARS_NOM))
    for k in D.NOM_ORDER:
        ax.plot(x,D.NOM[k],marker="o",ms=3.4,lw=2.3,color=c(D.NOM_COLORKEY[k]),label=k,mec=CARD,mew=0.8)
    ax.plot(x,D.WEST_BLOC_NOM,lw=2.4,ls=(0,(6,3)),color=c("accent"),label='"West" bloc (US+EU+UK+Japan)')
    _style(ax,ymax=84,ystep=20,xlabels=D.YEARS_NOM,xpos=x)
    _title(ax,"World GDP share, nominal market exchange rates (%)"); _legend(ax,4)
    return _save(fig,"nom")

# ---------------- Fig 05 US nominal 1913 ----------------
def us():
    fig,ax=_new(7.4,4.2); x=np.arange(len(D.YEARS_US))
    ax.plot(x,D.US_NOM,marker="o",ms=5,lw=2.6,color=c("us"),mec=CARD,mew=1.0)
    ax.fill_between(x,D.US_NOM,color=c("us"),alpha=0.07)
    i45=D.YEARS_US.index("1945")
    ax.annotate("~50% \u2014 the rubble peak",xy=(i45,50),xytext=(i45+0.4,52.5),
                fontproperties=F_SANS,color=c("us"),
                arrowprops=dict(arrowstyle="-",color=c("us"),lw=1))
    _style(ax,ymax=58,ystep=10,xlabels=D.YEARS_US,xpos=x)
    _title(ax,"US share of world GDP, nominal, 1913\u20132024 (benchmark estimates)")
    return _save(fig,"us")

# ---------------- Fig 06 bloc both rulers ----------------
def bloc():
    fig,ax=_new(7.4,4.5); x=np.arange(len(D.YEARS_BLOC))
    spec=[("West bloc \u2014 nominal",c("us"),"-"),
          ("West bloc \u2014 PPP",c("us"),(0,(5,3))),
          ("China + India \u2014 nominal",c("in"),"-"),
          ("China + India \u2014 PPP",c("in"),(0,(5,3)))]
    for k,col,ls in spec:
        ax.plot(x,D.BLOC[k],lw=2.6,ls=ls,color=col,label=k)
    _style(ax,ymax=82,ystep=20,xlabels=D.YEARS_BLOC,xpos=x)
    _title(ax,"US-plus-allies vs China-plus-India \u2014 both rulers (%)"); _legend(ax,2)
    return _save(fig,"bloc")

# ---------------- Fig 07 who gained/lost (diverging hbar) ----------------
def delta():
    fig,ax=_new(7.4,4.4)
    ents=D.DELTA_ENT[::-1]; y=np.arange(len(ents)); h=0.36
    nom=[D.DELTA_NOM[e] for e in ents]; ppp=[D.DELTA_PPP[e] for e in ents]
    ax.barh(y+h/2,nom,height=h,color=c("us"),label="Nominal change")
    ax.barh(y-h/2,ppp,height=h,color=c("eu"),label="PPP change")
    ax.axvline(0,color=RULE,lw=1.2)
    for s in ["top","right","left"]: ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(RULE)
    ax.tick_params(length=0,colors=SOFT)
    ax.set_yticks(y); ax.set_yticklabels(ents,fontproperties=F_SANS5,color=INK)
    ax.xaxis.grid(True,color=GRID,lw=1.0); ax.set_axisbelow(True)
    ax.set_xlim(-16,18)
    ax.xaxis.set_major_formatter(lambda v,_: f"{v:+g}")
    for t in ax.get_xticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    for e,yy in zip(ents,y):
        ax.text(D.DELTA_NOM[e]+(0.3 if D.DELTA_NOM[e]>=0 else -0.3),yy+h/2,f"{D.DELTA_NOM[e]:+.1f}",
                va="center",ha="left" if D.DELTA_NOM[e]>=0 else "right",fontproperties=F_MONO,color=SOFT,fontsize=8)
        ax.text(D.DELTA_PPP[e]+(0.3 if D.DELTA_PPP[e]>=0 else -0.3),yy-h/2,f"{D.DELTA_PPP[e]:+.1f}",
                va="center",ha="left" if D.DELTA_PPP[e]>=0 else "right",fontproperties=F_MONO,color=SOFT,fontsize=8)
    ax.set_xlabel("change in share of world GDP, percentage points 1990\u20132024",fontproperties=F_SANS,color=SOFT)
    _title(ax,"Who gained and lost world-GDP share, 1990\u20132024"); _legend(ax,2,y=-0.20)
    return _save(fig,"delta")

# ---------------- Fig 08 multiplier over time ----------------
def mult():
    fig,ax=_new(7.4,4.5); x=np.arange(len(D.YEARS_MULT))
    for k in D.MULT_ORDER:
        ax.plot(x,D.MULT[k],marker="o",ms=4,lw=2.4,color=c(D.MULT_COLORKEY[k]),label=k,mec=CARD,mew=0.9)
    ax.axhline(1.0,color=FAINT,lw=1.3,ls=(0,(5,4)))
    ax.text(len(x)-1,1.04,"world average 1.0\u00d7",ha="right",fontproperties=F_MONO,color=FAINT,fontsize=8.5)
    _style(ax,ymax=5,ystep=1,xlabels=D.YEARS_MULT,xpos=x,ypct=False,xmult=True)
    _title(ax,"Income relative to the world average, PPP (\u00d7)"); _legend(ax,3)
    return _save(fig,"mult")

# ---------------- Fig 09 2024 shares two rulers (grouped hbar) ----------------
def share24():
    fig,ax=_new(7.4,4.5)
    ents=D.SHARE24_ENT[::-1]; y=np.arange(len(ents)); h=0.36
    nom=[D.SHARE24_NOM[D.SHARE24_ENT.index(e)] for e in ents]
    ppp=[D.SHARE24_PPP[D.SHARE24_ENT.index(e)] for e in ents]
    ax.barh(y+h/2,nom,height=h,color=c("us"),label="Market exchange rates (nominal)")
    ax.barh(y-h/2,ppp,height=h,color=c("cn"),label="Purchasing power parity (PPP)")
    for s in ["top","right","left"]: ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(RULE); ax.tick_params(length=0,colors=SOFT)
    ax.set_yticks(y); ax.set_yticklabels(ents,fontproperties=F_SANS5,color=INK)
    ax.xaxis.grid(True,color=GRID,lw=1.0); ax.set_axisbelow(True); ax.set_xlim(0,30)
    ax.xaxis.set_major_formatter(lambda v,_: f"{v:g}%")
    for t in ax.get_xticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    for e,yy in zip(ents,y):
        n=D.SHARE24_NOM[D.SHARE24_ENT.index(e)]; p=D.SHARE24_PPP[D.SHARE24_ENT.index(e)]
        ax.text(n+0.3,yy+h/2,f"{n:.1f}",va="center",fontproperties=F_MONO,color=SOFT,fontsize=8)
        ax.text(p+0.3,yy-h/2,f"{p:.1f}",va="center",fontproperties=F_MONO,color=SOFT,fontsize=8)
    _title(ax,"Nominal vs PPP share of world GDP, 2024 (%)"); _legend(ax,2,y=-0.18)
    return _save(fig,"share24")

# ---------------- Fig 10 2024 multiplier two rulers (grouped vbar) ----------------
def mult24():
    fig,ax=_new(7.4,4.5); x=np.arange(len(D.MULT24_ENT)); w=0.38
    ax.bar(x-w/2,D.MULT24_NOM,width=w,color=c("us"),label="Nominal (market rates)")
    ax.bar(x+w/2,D.MULT24_PPP,width=w,color=c("cn"),label="PPP")
    ax.axhline(1.0,color=FAINT,lw=1.3,ls=(0,(5,4)))
    ax.text(len(x)-0.5,1.08,"parity 1.0\u00d7",ha="right",fontproperties=F_MONO,color=FAINT,fontsize=8.5)
    _style(ax,ymax=7,ystep=1,xlabels=D.MULT24_ENT,xpos=x,ypct=False,xmult=True)
    for t in ax.get_xticklabels(): t.set_fontproperties(F_SANS); t.set_rotation(18); t.set_ha("right")
    _title(ax,"Income vs world average, 2024 \u2014 nominal vs PPP (\u00d7)"); _legend(ax,2)
    return _save(fig,"mult24")

# ---------------- Fig 10 the 2024 ruler gap (diverging hbar) ----------------
def gap24():
    fig,ax=_new(7.4,4.2)
    ents=sorted(D.GAP24_ENT, key=lambda e: D.GAP24[e])  # ascending -> largest gap at top
    y=np.arange(len(ents)); vals=[D.GAP24[e] for e in ents]
    cols=[c("us") if v>=0 else c("eu") for v in vals]
    ax.barh(y,vals,height=0.62,color=cols)
    ax.axvline(0,color=RULE,lw=1.2)
    for s in ["top","right","left"]: ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(RULE); ax.tick_params(length=0,colors=SOFT)
    ax.set_yticks(y); ax.set_yticklabels(ents,fontproperties=F_SANS5,color=INK)
    ax.xaxis.grid(True,color=GRID,lw=1.0); ax.set_axisbelow(True); ax.set_xlim(-6,13)
    ax.xaxis.set_major_formatter(lambda v,_: f"{v:+g}")
    for t in ax.get_xticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    for e,yy in zip(ents,y):
        v=D.GAP24[e]
        ax.text(v+(0.2 if v>=0 else -0.2),yy,f"{v:+.1f}",va="center",
                ha="left" if v>=0 else "right",fontproperties=F_MONO,color=SOFT,fontsize=8)
    ax.set_xlabel("nominal share minus PPP share, percentage points (2024)",fontproperties=F_SANS,color=SOFT)
    _title(ax,"The 2024 ruler gap \u2014 bigger in dollars, or bigger on PPP")
    return _save(fig,"gap24")

# ---------------- Fig 12 population vs real-output scatter ----------------
def scatter24():
    fig,ax=_new(7.4,4.7); lim=21.5
    ax.plot([0,lim],[0,lim],ls=(0,(5,4)),color=FAINT,lw=1.3,zorder=1)
    ax.text(lim*0.60,lim*0.635,"parity \u2014 multiplier 1.0\u00d7",rotation=29,
            fontproperties=F_MONO,color=FAINT,fontsize=8,rotation_mode="anchor",zorder=2)
    offs={"United States":(7,5),"China":(8,-2),"EU (27)":(7,5),"India":(-8,8),
          "Japan":(7,3),"United Kingdom":(-10,-12),"Russia":(7,-4)}
    for e in D.POP24_ENT:
        i=D.POP24_ENT.index(e); x=D.POP24[i]; yv=D.POP24_PPP[i]
        ax.scatter([x],[yv],s=165,color=c(D.POP24_COLORKEY[e]),edgecolor=CARD,linewidth=1.3,zorder=4)
        dx,dy=offs.get(e,(6,5))
        ax.annotate(e,(x,yv),xytext=(dx,dy),textcoords="offset points",
                    fontproperties=F_SANS5,color=INK,fontsize=8.6,zorder=5,
                    ha="right" if dx<0 else "left")
    for s in ["top","right"]: ax.spines[s].set_visible(False)
    for s in ["left","bottom"]: ax.spines[s].set_color(RULE)
    ax.tick_params(length=0,colors=SOFT)
    ax.grid(True,color=GRID,lw=1.0); ax.set_axisbelow(True)
    ax.set_xlim(0,lim); ax.set_ylim(0,lim)
    ax.xaxis.set_major_formatter(lambda v,_: f"{v:g}%")
    ax.yaxis.set_major_formatter(lambda v,_: f"{v:g}%")
    for t in list(ax.get_xticklabels())+list(ax.get_yticklabels()):
        t.set_fontproperties(F_MONO); t.set_color(FAINT)
    ax.set_xlabel("share of world population (%)",fontproperties=F_SANS,color=SOFT)
    ax.set_ylabel("share of world GDP, PPP (%)",fontproperties=F_SANS,color=SOFT)
    _title(ax,"Population weight vs real-output weight, 2024")
    return _save(fig,"scatter24")

# ---------------- Fig 13 Japan, the warning label (two rulers over time) ----------------
def jp():
    fig,ax=_new(7.4,4.4); x=np.arange(len(D.JP_YEARS))
    ax.plot(x,D.JP_NOM,marker="o",ms=4.5,lw=2.6,color=c("jp"),label="Japan — nominal (market rates)",mec=CARD,mew=1.0)
    ax.plot(x,D.JP_PPP,marker="o",ms=4.0,lw=2.4,ls=(0,(5,3)),color=c("ru"),label="Japan — PPP (real output)",mec=CARD,mew=0.9)
    ipk=D.JP_YEARS.index("1994")
    ax.annotate("1994 nominal peak ~18.2%",xy=(ipk,18.2),xytext=(ipk+0.5,18.4),
                fontproperties=F_SANS,color=c("jp"),
                arrowprops=dict(arrowstyle="-",color=c("jp"),lw=1))
    _style(ax,ymax=20,ystep=5,xlabels=D.JP_YEARS,xpos=x)
    _title(ax,"Japan, the warning label — one country, two rulers (%)"); _legend(ax,2)
    return _save(fig,"jp")

# ---------------- Fig 14 multiplier arithmetic — why India is the swing variable ----------------
def swing24():
    fig,ax=_new(7.4,4.6); xmax=D.SWING_XMAX; ymax=35
    xs=np.linspace(0,xmax,100)
    for e in D.SWING_ENT:
        pop=D.SWING_POP[e]; col=c(D.SWING_COLORKEY[e])
        ax.plot(xs,pop*xs,lw=2.6,color=col,label=e)
        mx=D.SWING_MULT24[e]; my=pop*mx
        ax.scatter([mx],[my],s=120,color=col,edgecolor=CARD,linewidth=1.3,zorder=5)
        ax.annotate("2024",(mx,my),xytext=(5,5),textcoords="offset points",
                    fontproperties=F_MONO,color=SOFT,fontsize=7.5,zorder=6)
    ax.axhline(0,color=RULE,lw=1.0)
    for s in ["top","right"]: ax.spines[s].set_visible(False)
    for s in ["left","bottom"]: ax.spines[s].set_color(RULE); ax.spines[s].set_linewidth(1.0)
    ax.tick_params(length=0,colors=SOFT)
    ax.yaxis.grid(True,color=GRID,lw=1.0); ax.xaxis.grid(True,color=GRID,lw=1.0); ax.set_axisbelow(True)
    ax.set_xlim(0,xmax); ax.set_ylim(0,ymax)
    ax.set_xticks(np.arange(0,xmax+0.001,1))
    ax.xaxis.set_major_formatter(lambda v,_: f"{v:g}\u00d7")
    ax.yaxis.set_major_formatter(lambda v,_: f"{v:g}%")
    for t in list(ax.get_xticklabels())+list(ax.get_yticklabels()):
        t.set_fontproperties(F_MONO); t.set_color(FAINT)
    ax.set_xlabel("assumed PPP multiplier (output per person vs world)",fontproperties=F_SANS,color=SOFT)
    ax.set_ylabel("implied share of world GDP (%)",fontproperties=F_SANS,color=SOFT)
    _title(ax,"Why India is the swing variable — multiplier \u00d7 a huge population base"); _legend(ax,4)
    return _save(fig,"swing24")

def _twin_spines(ax,ax2):
    ax.spines["top"].set_visible(False); ax2.spines["top"].set_visible(False)
    for a in (ax,ax2):
        a.spines["left"].set_color(RULE); a.spines["left"].set_linewidth(1.0)
        a.spines["right"].set_color(RULE); a.spines["right"].set_linewidth(1.0)
        a.spines["bottom"].set_color(RULE); a.spines["bottom"].set_linewidth(1.0)
        a.tick_params(length=0,colors=SOFT)

# ---------------- Fig 15 : five centuries of the whole ----------------
def world_long():
    fig,ax=_new(7.4,4.6); x=np.arange(len(D.AGG_L_YEARS))
    bars=ax.bar(x,D.AGG_L_POP,width=0.60,color=c("eu"),alpha=0.85,
                edgecolor=CARD,linewidth=0.7,label="World population (billions)",zorder=2)
    ax.set_ylim(0,7); ax.set_yticks(np.arange(0,7.01,1))
    ax.yaxis.grid(True,color=GRID,linewidth=1.0); ax.set_axisbelow(True)
    ax.set_ylabel("world population (billions)",fontproperties=F_SANS,color=SOFT)
    ax2=ax.twinx()
    ln,=ax2.plot(x,D.AGG_L_GDP,marker="o",ms=5,lw=2.8,color=c("us"),
                 mec=CARD,mew=1.1,label="World real GDP (tn, 2011 int'l-$, PPP)",zorder=3)
    ax2.set_ylim(0,80); ax2.set_yticks(np.arange(0,80.01,20))
    ax2.set_ylabel("world real GDP (trillions, 2011 int'l-$)",fontproperties=F_SANS,color=SOFT)
    _twin_spines(ax,ax2)
    ax.set_xticks(x); ax.set_xticklabels(D.AGG_L_YEARS)
    for t in ax.get_xticklabels(): t.set_fontproperties(F_MONO); t.set_color(SOFT)
    for t in ax.get_yticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    for t in ax2.get_yticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    ax2.yaxis.set_major_formatter(lambda v,_: f"${v:g}T")
    _title(ax,"Five centuries of the whole — headcount and real output")
    leg=ax.legend(handles=[bars,ln],loc="upper center",bbox_to_anchor=(0.5,-0.14),
                  ncol=2,frameon=False,prop=F_SANS,handlelength=1.5,columnspacing=1.8,handletextpad=0.6)
    for t in leg.get_texts(): t.set_color(SOFT)
    return _save(fig,"world_long")

# ---------------- Fig 16 : the modern totals and the road to 2050 ----------------
def world_modern():
    fig,ax=_new(7.4,4.6)
    x0,x1=1900,2050
    # population (left axis): solid actual + dashed projection
    pl,=ax.plot(D.AGG_M_POP_X,D.AGG_M_POP,marker="o",ms=4.5,lw=2.8,color=INK,
                mec=CARD,mew=1.0,label="World population (billions)",zorder=4)
    ax.plot(D.AGG_M_POP_PX,D.AGG_M_POP_PROJ,lw=2.4,ls=(0,(5,3)),color=INK,alpha=0.55,zorder=4)
    ax.scatter([D.AGG_M_POP_PX[-1]],[D.AGG_M_POP_PROJ[-1]],s=46,color=INK,alpha=0.55,
               edgecolor=CARD,linewidth=1.0,zorder=5)
    ax.set_ylim(0,11); ax.set_yticks(np.arange(0,11.01,2))
    ax.set_xlim(x0,x1)
    ax.yaxis.grid(True,color=GRID,linewidth=1.0); ax.set_axisbelow(True)
    ax.set_ylabel("world population (billions)",fontproperties=F_SANS,color=SOFT)
    # GDP (right axis): nominal + PPP, current dollars
    ax2=ax.twinx()
    pp,=ax2.plot(D.AGG_M_PPP_X,D.AGG_M_PPP,marker="o",ms=4.5,lw=2.6,color=c("eu"),
                 mec=CARD,mew=1.0,label="World GDP — PPP (current int'l-$)",zorder=3)
    nm,=ax2.plot(D.AGG_M_NOM_X,D.AGG_M_NOM,marker="o",ms=4.5,lw=2.6,color=c("us"),
                 mec=CARD,mew=1.0,label="World GDP — nominal (current US$)",zorder=3)
    ax2.set_ylim(0,210); ax2.set_yticks(np.arange(0,210.01,50))
    ax2.set_ylabel("world GDP (trillions, current $)",fontproperties=F_SANS,color=SOFT)
    ax2.yaxis.set_major_formatter(lambda v,_: f"${v:g}T")
    # "now" marker + endpoint annotations
    ax.axvline(2024,color=RULE,lw=1.0,ls=(0,(2,3)),zorder=1)
    ax.annotate("8.2bn",(2024,8.2),xytext=(-4,6),textcoords="offset points",
                fontproperties=F_MONO,color=INK,fontsize=8,ha="right",zorder=6)
    ax.annotate("9.7bn (2050,\nUN median)",(2050,9.7),xytext=(-2,-2),textcoords="offset points",
                fontproperties=F_MONO,color=SOFT,fontsize=7.5,ha="right",va="top",zorder=6)
    _twin_spines(ax,ax2)
    xt=[1900,1950,2000,2024,2050]
    ax.set_xticks(xt); ax.set_xticklabels([str(y) for y in xt])
    for t in ax.get_xticklabels(): t.set_fontproperties(F_MONO); t.set_color(SOFT)
    for t in ax.get_yticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    for t in ax2.get_yticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    _title(ax,"The modern totals, and the road to 2050")
    leg=ax.legend(handles=[pl,nm,pp],loc="upper center",bbox_to_anchor=(0.5,-0.14),
                  ncol=3,frameon=False,prop=F_SANS,handlelength=1.5,columnspacing=1.4,handletextpad=0.5)
    for t in leg.get_texts(): t.set_color(SOFT)
    return _save(fig,"world_modern")

def _tag(ax, text, projection=False):
    """Small uppercase flag marking a figure as illustrative scenario / projection."""
    col = c("eu") if projection else c("us")
    ax.text(0.995, 1.045, text, transform=ax.transAxes, ha="right", va="bottom",
            fontproperties=F_MONO, fontsize=7.6, color=col, alpha=0.95)

# ---------------- Fig 17 : the scenario space (2x2 conceptual) ----------------
def scenario_space():
    fig, ax = _new(7.4, 5.8)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    quad = [((0,5,5,5), c("us"), "Frontier Pull-Away", "integrated order,\nconcentrated frontier", (2.5,8.6)),
            ((5,5,5,5), c("in"), "The Great Catch-Up", "integrated order,\ndiffused frontier", (7.5,8.6)),
            ((0,0,5,5), c("jp"), "Two Suns", "fragmented order,\nconcentrated frontier", (2.5,3.6)),
            ((5,0,5,5), c("eu"), "Archipelago", "fragmented order,\ndiffused frontier", (7.5,3.6))]
    for (x,y,w,h), col, name, desc, (tx,ty) in quad:
        ax.add_patch(plt.Rectangle((x,y), w, h, facecolor=col, alpha=0.10, edgecolor=col, linewidth=1.0))
        ax.text(tx, ty, name, ha="center", va="center", fontproperties=F_TITLE, fontsize=13, color=INK)
        ax.text(tx, ty-0.95, desc, ha="center", va="center", fontproperties=F_MONO, fontsize=7.6, color=SOFT)
    # axes crosshair + labels
    ax.plot([5,5],[0,10], color=RULE, lw=1.0, zorder=1); ax.plot([0,10],[5,5], color=RULE, lw=1.0, zorder=1)
    ax.annotate("", xy=(10,-0.55), xytext=(0,-0.55), annotation_clip=False,
                arrowprops=dict(arrowstyle="->", color=SOFT, lw=1.2))
    ax.text(0,-1.05,"frontier concentrates", ha="left", va="top", fontproperties=F_MONO, fontsize=8, color=SOFT)
    ax.text(10,-1.05,"frontier diffuses", ha="right", va="top", fontproperties=F_MONO, fontsize=8, color=SOFT)
    ax.annotate("", xy=(-0.55,10), xytext=(-0.55,0), annotation_clip=False,
                arrowprops=dict(arrowstyle="->", color=SOFT, lw=1.2))
    ax.text(-1.0,0,"order fragments", ha="left", va="bottom", rotation=90, fontproperties=F_MONO, fontsize=8, color=SOFT)
    ax.text(-1.0,10,"order integrates", ha="right", va="bottom", rotation=90, fontproperties=F_MONO, fontsize=8, color=SOFT)
    # the Long Plateau band across the centre
    ax.add_patch(plt.Rectangle((0.6,4.2), 8.8, 1.6, facecolor=CARD, alpha=0.82, edgecolor=c("us"),
                               linewidth=1.1, linestyle=(0,(5,3)), zorder=4))
    ax.text(5, 5.0, "The Long Plateau", ha="center", va="center", fontproperties=F_TITLE, fontsize=12, color=c("us"), zorder=5)
    ax.text(5, 4.5, "the low-productivity version of all four", ha="center", va="center",
            fontproperties=F_MONO, fontsize=7.4, color=SOFT, zorder=5)
    _title(ax, "The scenario space")
    ax.text(0.995, 1.02, "CONCEPTUAL MAP \u00b7 NOT A DATA PLOT", transform=ax.transAxes, ha="right",
            va="bottom", fontproperties=F_MONO, fontsize=7.6, color=c("us"))
    return _save(fig, "scenario_space")

# ---------------- Fig 18 : the cone of outcomes (fan chart) ----------------
def cone():
    fig, ax = _new(7.4, 4.4); X = D.CONE_X
    for name, series in D.CONE.items():
        col = c(D.CONE_CK[name])
        lo = [s[0] for s in series]; mid = [s[1] for s in series]; hi = [s[2] for s in series]
        ax.fill_between(X, lo, hi, color=col, alpha=0.15, linewidth=0)
        ax.plot(X, hi, color=col, lw=1.0, ls=(0,(4,3)), alpha=0.55)
        ax.plot(X, lo, color=col, lw=1.0, ls=(0,(4,3)), alpha=0.55)
        ax.plot(X, mid, color=col, lw=2.6, label=name)
        ax.scatter([X[0]], [mid[0]], color=col, s=28, zorder=5, edgecolor=CARD, linewidth=1.1)
        ax.annotate(f"{hi[-1]:.0f}", (X[-1], hi[-1]), xytext=(6,0), textcoords="offset points",
                    fontproperties=F_MONO, fontsize=8, color=col, va="center")
    ax.set_xlim(2024, 2050); ax.set_ylim(8, 28)
    ax.set_xticks([2024, 2035, 2050]); ax.set_yticks([10,15,20,25])
    ax.yaxis.grid(True, color=GRID, linewidth=1.0); ax.set_axisbelow(True)
    for sp in ("top","right"): ax.spines[sp].set_visible(False)
    for sp in ("left","bottom"): ax.spines[sp].set_color(RULE)
    ax.tick_params(length=0, colors=SOFT)
    for t in ax.get_xticklabels(): t.set_fontproperties(F_MONO); t.set_color(SOFT)
    for t in ax.get_yticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    ax.yaxis.set_major_formatter(lambda v,_: f"{v:g}%")
    ax.set_ylabel("share of world GDP at PPP", fontproperties=F_SANS, color=SOFT)
    _title(ax, "The cone of outcomes")
    _legend(ax, 3); _tag(ax, "ILLUSTRATIVE \u00b7 NOT FORECASTS")
    return _save(fig, "cone")

# ---------------- Fig 19 : 2050 PPP shares under each scenario (grouped bars) ----------------
def scenario_bars():
    fig, ax = _new(7.9, 4.7); actors = D.SCEN_BARS_ACTORS; scen = D.SCEN
    cols = [c("us"), c("in"), c("jp"), c("eu"), FAINT]
    x = np.arange(len(actors)); nb = len(scen); w = 0.16
    for i, s in enumerate(scen):
        vals = [D.SCEN_BARS[a][i] for a in actors]
        ax.bar(x + (i-(nb-1)/2)*w, vals, width=w, color=cols[i], label=s,
               edgecolor=CARD, linewidth=0.5)
    ax.set_xticks(x); ax.set_xticklabels(["United States","China","India","Sub-Saharan\nAfrica","EU + UK","Rest of\nWorld"])
    for t in ax.get_xticklabels(): t.set_fontproperties(F_SANS); t.set_color(INK); t.set_fontsize(8.4)
    ax.set_ylim(0, 42); ax.set_yticks([0,10,20,30,40])
    ax.yaxis.grid(True, color=GRID, linewidth=1.0); ax.set_axisbelow(True)
    for sp in ("top","right"): ax.spines[sp].set_visible(False)
    for sp in ("left","bottom"): ax.spines[sp].set_color(RULE)
    ax.tick_params(length=0, colors=SOFT)
    for t in ax.get_yticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    ax.yaxis.set_major_formatter(lambda v,_: f"{v:g}%")
    ax.set_ylabel("share of world GDP at PPP, 2050", fontproperties=F_SANS, color=SOFT)
    _title(ax, "2050 PPP shares by scenario")
    _legend(ax, 5); _tag(ax, "ILLUSTRATIVE \u00b7 NOT FORECASTS")
    return _save(fig, "scenario_bars")

# ---------------- Fig 20 : demographic destiny (lines; UN WPP 2024 projection) ----------------
def demography():
    fig, ax = _new(7.4, 4.5); X = D.DEMO_X
    for name, series in D.DEMO.items():
        col = c(D.DEMO_CK[name])
        ax.plot(X, series, color=col, lw=2.6, label=name, marker="o", ms=3.2, mec=CARD, mew=0.8)
        ax.annotate(f"{series[-1]:.0f}", (X[-1], series[-1]), xytext=(6,0), textcoords="offset points",
                    fontproperties=F_MONO, fontsize=8, color=col, va="center")
    ax.axhline(100, color=RULE, lw=1.0, ls=(0,(2,3)))
    ax.set_xlim(2024, 2050); ax.set_ylim(70, 200)
    ax.set_xticks([2024,2030,2035,2040,2045,2050]); ax.set_yticks([80,100,120,140,160,180,200])
    ax.yaxis.grid(True, color=GRID, linewidth=1.0); ax.set_axisbelow(True)
    for sp in ("top","right"): ax.spines[sp].set_visible(False)
    for sp in ("left","bottom"): ax.spines[sp].set_color(RULE)
    ax.tick_params(length=0, colors=SOFT)
    for t in ax.get_xticklabels(): t.set_fontproperties(F_MONO); t.set_color(SOFT)
    for t in ax.get_yticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    ax.set_ylabel("working-age (15\u201364) population, 2024 = 100", fontproperties=F_SANS, color=SOFT)
    _title(ax, "Demographic destiny")
    _legend(ax, 3); _tag(ax, "PROJECTION \u00b7 UN WPP 2024", projection=True)
    return _save(fig, "demography")

# ---------------- Fig 21 : the dollar's reserve share to 2050 (lines; scenarios) ----------------
def dollar():
    fig, ax = _new(7.4, 4.4); X = D.DOLLAR_X
    style = {"status-quo-plus": (c("in"), "-"), "base drift": (c("us"), "-"),
             "fragmentation": (c("jp"), "-"), "rupture": (c("ru"), (0,(5,2)))}
    for name in ["status-quo-plus","base drift","fragmentation","rupture"]:
        col, ls = style[name]
        lw = 2.8 if name == "rupture" else 2.4
        ax.plot(X, D.DOLLAR[name], color=col, lw=lw, ls=ls, label=name)
        ax.annotate(f"{D.DOLLAR[name][-1]:.0f}%", (X[-1], D.DOLLAR[name][-1]), xytext=(6,0),
                    textcoords="offset points", fontproperties=F_MONO, fontsize=8, color=col, va="center")
    ax.scatter([2024],[58], color=INK, s=30, zorder=6, edgecolor=CARD, linewidth=1.1)
    ax.annotate("~58% (2024)", (2024,58), xytext=(8,8), textcoords="offset points",
                fontproperties=F_MONO, fontsize=8, color=INK)
    ax.set_xlim(2024, 2050); ax.set_ylim(25, 62)
    ax.set_xticks([2024,2030,2035,2040,2045,2050]); ax.set_yticks([30,40,50,60])
    ax.yaxis.grid(True, color=GRID, linewidth=1.0); ax.set_axisbelow(True)
    for sp in ("top","right"): ax.spines[sp].set_visible(False)
    for sp in ("left","bottom"): ax.spines[sp].set_color(RULE)
    ax.tick_params(length=0, colors=SOFT)
    for t in ax.get_xticklabels(): t.set_fontproperties(F_MONO); t.set_color(SOFT)
    for t in ax.get_yticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    ax.yaxis.set_major_formatter(lambda v,_: f"{v:g}%")
    ax.set_ylabel("USD share of global FX reserves", fontproperties=F_SANS, color=SOFT)
    _title(ax, "The dollar's reserve share to 2050")
    _legend(ax, 4); _tag(ax, "ILLUSTRATIVE \u00b7 RUPTURE IS A TAIL")
    return _save(fig, "dollar")

# ---------------- Fig 22 : diffuse vs concentrate, on the multiplier (paired bars) ----------------
def multiplier_shift():
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 4.0), sharey=True)
    fig.patch.set_facecolor(CARD)
    actors = D.MULT_SHIFT_ACTORS
    short = ["US", "EU+UK", "India", "Sub-Sah.\nAfrica"]
    cols = [c(D.MULT_SHIFT_CK[a]) for a in actors]
    x = np.arange(len(actors))
    for ax, case in zip(axes, ["Concentrate", "Diffuse"]):
        ax.set_facecolor(CARD)
        ax.bar(x, D.MULT_SHIFT[case], width=0.62, color=cols, edgecolor=CARD, linewidth=0.6)
        ax.axhline(0, color=SOFT, lw=1.1)
        ax.set_xticks(x); ax.set_xticklabels(short)
        for t in ax.get_xticklabels(): t.set_fontproperties(F_SANS); t.set_color(INK); t.set_fontsize(8.2)
        ax.set_ylim(-0.25, 0.7)
        for sp in ("top","right"): ax.spines[sp].set_visible(False)
        for sp in ("left","bottom"): ax.spines[sp].set_color(RULE)
        ax.tick_params(length=0, colors=SOFT)
        ax.set_title(case, fontproperties=F_TITLE, color=INK, fontsize=12, pad=8)
        for t in ax.get_yticklabels(): t.set_fontproperties(F_MONO); t.set_color(FAINT)
    axes[0].set_yticks([-0.2,0,0.2,0.4,0.6])
    axes[0].set_ylabel("change in PPP multiplier, 2024\u20132050", fontproperties=F_SANS, color=SOFT)
    axes[1].text(0.995, 1.08, "ILLUSTRATIVE \u00b7 NOT FORECASTS", transform=axes[1].transAxes,
                 ha="right", va="bottom", fontproperties=F_MONO, fontsize=7.6, color=c("us"))
    fig.subplots_adjust(wspace=0.12)
    return _save(fig, "multiplier_shift")

RENDERERS={"long_bar":long_bar,"long_area":long_area,"mfg":mfg,"nom":nom,"us":us,
           "bloc":bloc,"delta":delta,"mult":mult,"share24":share24,"gap24":gap24,
           "mult24":mult24,"scatter24":scatter24,"jp":jp,"swing24":swing24,
           "world_long":world_long,"world_modern":world_modern,
           "scenario_space":scenario_space,"cone":cone,"scenario_bars":scenario_bars,
           "demography":demography,"dollar":dollar,"multiplier_shift":multiplier_shift}

def render_all():
    out={}
    for k,fn in RENDERERS.items():
        out[k]=fn()
    return out

if __name__=="__main__":
    paths=render_all()
    for k,p in paths.items(): print(k, os.path.basename(p), os.path.getsize(p))
