# -*- coding: utf-8 -*-
"""build_html.py — emit the interactive (Chart.js) edition into outputs/ (override with WON_OUTPUT_DIR)."""
import json, os
import data as D
import common

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.environ.get("WON_OUTPUT_DIR", os.path.join(HERE, "..", "outputs"))
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "the-shifting-weight-of-nations.html")

DATA_JS = json.dumps({
    "PAL": D.PALETTE,
    "YEARS_LONG": D.YEARS_LONG, "LONG": D.LONG, "LONG_ORDER": D.LONG_ORDER, "LONG_CK": D.LONG_COLORKEY,
    "YEARS_MFG": D.YEARS_MFG, "MFG": D.MFG, "MFG_ORDER": D.MFG_ORDER, "MFG_CK": D.MFG_COLORKEY,
    "YEARS_NOM": D.YEARS_NOM, "NOM": D.NOM, "NOM_ORDER": D.NOM_ORDER, "NOM_CK": D.NOM_COLORKEY, "WEST": D.WEST_BLOC_NOM,
    "YEARS_US": D.YEARS_US, "US_NOM": D.US_NOM,
    "YEARS_BLOC": D.YEARS_BLOC, "BLOC": D.BLOC, "BLOC_ORDER": D.BLOC_ORDER,
    "DELTA_ENT": D.DELTA_ENT, "DELTA_NOM": D.DELTA_NOM, "DELTA_PPP": D.DELTA_PPP,
    "YEARS_MULT": D.YEARS_MULT, "MULT": D.MULT, "MULT_ORDER": D.MULT_ORDER, "MULT_CK": D.MULT_COLORKEY,
    "S24_ENT": D.SHARE24_ENT, "S24_NOM": D.SHARE24_NOM, "S24_PPP": D.SHARE24_PPP,
    "M24_ENT": D.MULT24_ENT, "M24_NOM": D.MULT24_NOM, "M24_PPP": D.MULT24_PPP,
    "GAP_ENT": D.GAP24_ENT, "GAP": D.GAP24,
    "POP_ENT": D.POP24_ENT, "POP": D.POP24, "POP_PPP": D.POP24_PPP, "POP_CK": D.POP24_COLORKEY,
    "JP_YEARS": D.JP_YEARS, "JP_NOM": D.JP_NOM, "JP_PPP": D.JP_PPP,
    "SWING_ENT": D.SWING_ENT, "SWING_POP": D.SWING_POP, "SWING_MULT24": D.SWING_MULT24,
    "SWING_CK": D.SWING_COLORKEY, "SWING_XMAX": D.SWING_XMAX,
    "AGG_L_YEARS": D.AGG_L_YEARS, "AGG_L_POP": D.AGG_L_POP, "AGG_L_GDP": D.AGG_L_GDP,
    "AGG_M_POP_X": D.AGG_M_POP_X, "AGG_M_POP": D.AGG_M_POP,
    "AGG_M_POP_PX": D.AGG_M_POP_PX, "AGG_M_POP_PROJ": D.AGG_M_POP_PROJ,
    "AGG_M_NOM_X": D.AGG_M_NOM_X, "AGG_M_NOM": D.AGG_M_NOM,
    "AGG_M_PPP_X": D.AGG_M_PPP_X, "AGG_M_PPP": D.AGG_M_PPP,
}, ensure_ascii=False)

CSS = """
:root{
  --paper:#F4EEE2;--paper-2:#FBF7EF;--card:#FCFAF4;--ink:#221C17;--ink-soft:#5C534A;--ink-faint:#6E6456;
  --rule:#DCD2C1;--rule-soft:#E7DECF;--accent:#993C1D;--accent-2:#B9743A;
  --us:#A23B26;--cn:#D29329;--eu:#2F5573;--in:#2E8B6F;--jp:#8A4F7D;--uk:#C77B43;--ru:#6E7B3E;--row:#A79D90;
  --shadow:0 1px 0 rgba(34,28,23,.04),0 18px 40px -28px rgba(34,28,23,.35);
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font-family:"IBM Plex Sans",system-ui,sans-serif;
  font-size:17px;line-height:1.62;letter-spacing:.005em;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;position:relative;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.5;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='0.035'/></svg>")}
.wrap{position:relative;z-index:1;max-width:920px;margin:0 auto;padding:0 22px 120px}
.prose-w{max-width:66ch}
p{margin:0 0 1.05em;max-width:66ch}
a{color:var(--accent);text-decoration:none;border-bottom:1px solid rgba(153,60,29,.32)}

.masthead{padding:74px 0 30px}
.kicker{font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);margin:0 0 22px}
h1{font-family:"Fraunces",Georgia,serif;font-weight:600;font-optical-sizing:auto;font-size:clamp(2.5rem,6.4vw,4.5rem);
  line-height:1.02;letter-spacing:-.018em;margin:0 0 .35em;max-width:16ch}
h1 em{font-style:italic;font-weight:500;color:var(--accent)}
.standfirst{font-family:"Fraunces",Georgia,serif;font-weight:400;font-style:italic;font-size:clamp(1.15rem,2.5vw,1.5rem);
  line-height:1.46;color:var(--ink-soft);max-width:42ch;margin:0 0 30px}
.dateline{font-family:"IBM Plex Mono",monospace;font-size:12.5px;color:var(--ink-faint);letter-spacing:.02em;line-height:1.7;
  border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:14px 0;display:flex;gap:26px;flex-wrap:wrap}
.dateline b{color:var(--ink-soft);font-weight:500}

.argument{margin:30px 0 8px;border:1px solid var(--rule);border-radius:6px;background:linear-gradient(180deg,var(--card),var(--paper-2));
  box-shadow:var(--shadow);overflow:hidden}
.arg-row{display:grid;grid-template-columns:130px 1fr;gap:20px;padding:20px 26px;border-bottom:1px solid var(--rule-soft)}
.arg-row:last-child{border-bottom:none}
.arg-tag{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);padding-top:4px}
.arg-row p{margin:0;font-size:1.02rem;max-width:none}
.arg-row:last-child p{font-family:"Fraunces",serif;font-style:italic;font-size:1.1rem;color:var(--ink)}
@media(max-width:620px){.arg-row{grid-template-columns:1fr;gap:6px}}

.section-head{margin:72px 0 8px}
.section-head .num{font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.2em;color:var(--accent);text-transform:uppercase}
h2{font-family:"Fraunces",Georgia,serif;font-weight:600;font-size:clamp(1.7rem,4vw,2.5rem);line-height:1.08;letter-spacing:-.01em;margin:.18em 0 .5em;max-width:20ch}
h3{font-family:"Fraunces",serif;font-weight:600;font-size:1.28rem;margin:1.7em 0 .4em;letter-spacing:-.005em}
.lede{font-size:1.06rem;color:var(--ink-soft);max-width:60ch;margin:0 0 1.4em}

.identity{margin:26px 0;padding:30px 26px;background:var(--card);border:1px solid var(--rule);border-radius:6px;box-shadow:var(--shadow);text-align:center}
.idt{display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap}
.idt-lhs{font-family:"Fraunces",serif;font-size:1rem;color:var(--ink);line-height:1.2}
.idt-eq,.idt-x{font-family:"Fraunces",serif;font-size:1.5rem;color:var(--ink-faint)}
.idt-box{font-size:.82rem;line-height:1.25;color:var(--ink-soft);padding:12px 16px;border-radius:6px;border:1px solid var(--rule)}
.idt-box b{font-family:"IBM Plex Sans";font-weight:600;color:var(--ink);font-size:.92rem}
.idt-sub{font-size:.72rem;color:var(--ink-faint)}
.b-pop{background:rgba(110,123,62,.10)}.b-price{background:rgba(47,85,115,.10)}.b-prod{background:rgba(153,60,29,.10);border-color:rgba(153,60,29,.3)}
.idt-note{font-size:.84rem;color:var(--ink-faint);margin:18px auto 0;max-width:62ch}

.callout{background:linear-gradient(180deg,var(--card),var(--paper-2));border:1px solid var(--rule);border-left:3px solid var(--accent);
  border-radius:4px;padding:26px 30px;margin:34px 0;box-shadow:var(--shadow)}
.callout h3{margin-top:0}
.callout .tag{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:10px}
.callout-intro{max-width:none}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:6px}
.two-col h4{font-family:"Fraunces",serif;font-size:1.05rem;margin:0 0 .3em;font-weight:600}
.two-col p{font-size:.95rem;color:var(--ink-soft);margin:0;max-width:none}
@media(max-width:620px){.two-col{grid-template-columns:1fr;gap:16px}}

.figure{margin:40px 0 30px;background:var(--card);border:1px solid var(--rule);border-radius:6px;padding:26px 26px 22px;box-shadow:var(--shadow);opacity:0;transform:translateY(18px)}
.figure.in{animation:rise .8s cubic-bezier(.2,.7,.2,1) forwards}
@keyframes rise{to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.figure{opacity:1;transform:none;animation:none}}
.fig-head{display:flex;justify-content:space-between;align-items:baseline;gap:16px;flex-wrap:wrap;margin-bottom:4px}
.fig-num{font-family:"IBM Plex Mono",monospace;font-size:11.5px;letter-spacing:.18em;color:var(--accent);text-transform:uppercase}
.fig-title{font-family:"Fraunces",serif;font-weight:600;font-size:1.35rem;line-height:1.15;margin:.15em 0 .1em}
.fig-sub{font-size:.92rem;color:var(--ink-faint);margin:0 0 16px}
.chart-box{position:relative;width:100%;height:480px}
.chart-box.chart-static{height:auto}
.chart-box canvas{max-width:100%}
.chart-img{width:100%;height:auto;display:block;border-radius:6px}
@media(max-width:600px){.chart-box{height:400px}}
@media(max-width:380px){.chart-box{height:340px}}
.fig-caption{font-size:.86rem;color:var(--ink-soft);line-height:1.55;margin:16px 2px 0;max-width:none}
.fig-caption b{color:var(--ink)}
.hint{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--ink-faint);letter-spacing:.02em}
.controls{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}
.btn{font-family:"IBM Plex Sans",sans-serif;font-size:12.5px;font-weight:500;color:var(--ink-soft);background:var(--paper-2);border:1px solid var(--rule);padding:6px 13px;border-radius:999px;cursor:pointer;transition:all .18s ease}
.btn:hover{border-color:var(--ink-faint);color:var(--ink)}
.btn[aria-pressed="true"]{background:var(--accent);color:#fff;border-color:var(--accent)}

.scenarios{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:30px 0}
@media(max-width:720px){.scenarios{grid-template-columns:1fr}}
.scn{background:var(--card);border:1px solid var(--rule);border-top:3px solid var(--accent);border-radius:5px;padding:18px 18px 16px;box-shadow:var(--shadow)}
.scn-h{display:flex;flex-direction:column;margin-bottom:8px}
.scn-name{font-family:"Fraunces",serif;font-weight:600;font-size:1.12rem;color:var(--ink)}
.scn-lab{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.scn-body{font-size:.9rem;color:var(--ink-soft);margin:0 0 10px;max-width:none}
.scn-watch{font-size:.82rem;color:var(--ink-faint);margin:0;max-width:none;border-top:1px solid var(--rule-soft);padding-top:8px}
.scn-watch span{font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:2px}

.tbl-wrap{margin:30px 0 8px;overflow-x:auto;border:1px solid var(--rule);border-radius:6px;box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;background:var(--card);font-size:.92rem}
caption{caption-side:top;text-align:left;font-family:"Fraunces",serif;font-weight:600;font-size:1.15rem;padding:18px 18px 10px}
th,td{padding:11px 16px;text-align:left;border-bottom:1px solid var(--rule-soft);vertical-align:top}
thead th{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-faint);font-weight:500;background:var(--paper-2)}
tbody tr:last-child td{border-bottom:none}
td.claim{font-weight:500;color:var(--ink)}
td .measure{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;padding:2px 7px;border-radius:4px;background:rgba(47,85,115,.1);color:var(--eu)}
td .measure.nom{background:rgba(162,59,38,.1);color:var(--us)}
td .measure.mix{background:rgba(138,79,125,.12);color:var(--jp)}
.tbl-foot{font-size:.8rem;color:var(--ink-faint);margin:0 2px 1.05em;max-width:none}
/* Mobile: compact cells so most tables fit a phone; momentum-scroll the genuinely wide ones. */
@media(max-width:600px){
  table{font-size:.84rem}
  th,td{padding:8px 11px}
  caption{font-size:1.06rem;padding:14px 14px 8px}
  .tbl-wrap{-webkit-overflow-scrolling:touch}
}
@media(max-width:400px){
  table{font-size:.76rem}
  th,td{padding:6px 8px}
}

.pull{font-family:"Fraunces",serif;font-style:italic;font-weight:500;font-size:clamp(1.35rem,3.2vw,1.85rem);line-height:1.32;color:var(--ink);
  border-top:2px solid var(--accent);border-bottom:1px solid var(--rule);padding:30px 0;margin:46px 0;max-width:24ch}
.pull span{color:var(--accent)}

.concl-list{list-style:none;counter-reset:c;padding:0;margin:24px 0}
.concl-list li{display:grid;grid-template-columns:46px 1fr;gap:16px;padding:16px 0;border-bottom:1px solid var(--rule-soft);max-width:none}
.concl-list li:last-child{border-bottom:none}
.cn-n{font-family:"IBM Plex Mono",monospace;font-size:13px;color:var(--accent);padding-top:3px}
.concl-list b{font-family:"Fraunces",serif;font-weight:600;font-size:1.05rem;color:var(--ink)}
.concl-list div{font-size:.96rem;color:var(--ink-soft)}

.sources{margin-top:60px;border-top:1px solid var(--rule);padding-top:30px}
.sources h2{font-size:1.5rem}
.src-list{font-size:.9rem;color:var(--ink-soft);line-height:1.7}
.src-list li{margin-bottom:.5em;max-width:72ch}
footer{margin-top:50px;padding-top:24px;border-top:1px solid var(--rule);font-family:"IBM Plex Mono",monospace;font-size:11.5px;color:var(--ink-faint);letter-spacing:.02em;line-height:1.7;max-width:80ch}

.sw{display:inline-block;width:.7em;height:.7em;border-radius:2px;margin-right:.35em;vertical-align:baseline;position:relative;top:.02em}
.byline{font-family:"Fraunces",serif;font-style:italic;font-size:1.02rem;color:var(--ink);margin:0 0 22px}
.country{margin:26px 0 10px}
.cty{padding:16px 0;border-bottom:1px solid var(--rule-soft)}
.cty:first-child{border-top:1px solid var(--rule-soft)}
.cty-h{display:flex;justify-content:space-between;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:4px}
.cty-name{font-family:"Fraunces",serif;font-weight:600;font-size:1.2rem;color:var(--ink)}
.cty-stat{font-family:"IBM Plex Mono",monospace;font-size:11.5px;letter-spacing:.02em;color:var(--accent)}
.cty-body{font-size:.97rem;color:var(--ink-soft);margin:0;max-width:none}
.colophon{margin:48px 0 10px;background:linear-gradient(180deg,var(--card),var(--paper-2));border:1px solid var(--rule);border-left:3px solid var(--accent);border-radius:4px;padding:26px 30px;box-shadow:var(--shadow)}
.colophon .tag{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:8px}
.colophon h3{margin-top:0}
.colo-intro{max-width:none;color:var(--ink-soft)}
.colo-rows{margin-top:6px}
.colo-row{display:grid;grid-template-columns:158px 1fr;gap:18px;padding:11px 0;border-top:1px solid var(--rule-soft)}
.colo-k{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-faint);padding-top:3px}
.colo-v{font-size:.95rem;color:var(--ink-soft);max-width:none}
@media(max-width:620px){.colo-row{grid-template-columns:1fr;gap:4px}}
::selection{background:rgba(153,60,29,.18)}
"""

import base64
NEW_STATIC = {"scenario_space", "cone", "scenario_bars", "demography", "dollar", "multiplier_shift"}
_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

def fig_inner(key):
    if key in NEW_STATIC:
        with open(os.path.join(_ASSETS, key + ".png"), "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode()
        return (f'<div class="chart-box chart-static">'
                f'<img class="chart-img" src="data:image/png;base64,{b64}" alt=""></div>')
    return f'<div class="chart-box"><canvas id="c_{key}"></canvas></div>'

SCRIPT = """
const D = __DATA__;
const css=getComputedStyle(document.documentElement);
const COL={}; for(const k in D.PAL){COL[k]=D.PAL[k];}
function ck(map,name){return COL[map[name]];}
Chart.defaults.font.family="'IBM Plex Sans',sans-serif";
Chart.defaults.font.size=12.5; Chart.defaults.color=COL.ink_soft;
const GRID={color:'rgba(34,28,23,0.07)',drawTicks:false};
const TIP={backgroundColor:'#221C17',titleColor:'#FBF7EF',bodyColor:'#EDE6DA',borderColor:'rgba(255,255,255,0.08)',borderWidth:1,
  padding:11,cornerRadius:6,titleFont:{family:"'Fraunces',serif",weight:'600',size:13.5},bodyFont:{family:"'IBM Plex Mono',monospace",size:12},boxPadding:5,usePointStyle:true};
const LEG={position:'bottom',align:'start',labels:{usePointStyle:true,pointStyle:'rectRounded',boxWidth:9,boxHeight:9,padding:14,color:COL.ink_soft,font:{size:12.5,weight:'500'}}};
const xMono={grid:{display:false},border:{color:COL.rule},ticks:{color:COL.ink_soft,font:{family:"'IBM Plex Mono',monospace",size:11.5}}};
function yPct(max,step){return {min:0,max:max,grid:GRID,border:{display:false},ticks:{callback:v=>v+'%',color:COL.ink_faint,stepSize:step}};}
function yMul(max,step){return {min:0,max:max,grid:GRID,border:{display:false},ticks:{callback:v=>v.toFixed(1)+'\\u00d7',color:COL.ink_faint,stepSize:step}};}
const ANIM={duration:1050,easing:'easeOutQuart'};

function stacked(id,labels,obj,order,cmap,max,step){
  const ds=order.map(k=>({label:k,data:obj[k],backgroundColor:ck(cmap,k),borderColor:'rgba(244,238,226,.55)',borderWidth:1,borderRadius:1.5,barPercentage:.94,categoryPercentage:.9}));
  new Chart(document.getElementById(id),{type:'bar',data:{labels,datasets:ds},options:{responsive:true,maintainAspectRatio:false,animation:ANIM,interaction:{mode:'index',intersect:false},
    scales:{x:{stacked:true,...xMono},y:{stacked:true,...yPct(max,step)}},plugins:{legend:LEG,tooltip:{...TIP,callbacks:{label:c=>'  '+c.dataset.label+': '+c.parsed.y.toFixed(1)+'%'}}}}});
}
function area(id,labels,obj,order,cmap,max,step){
  const ds=order.map(k=>({label:k,data:obj[k],backgroundColor:hexA(ck(cmap,k),.9),borderColor:'rgba(244,238,226,.5)',borderWidth:.8,fill:true,pointRadius:0,tension:.25}));
  new Chart(document.getElementById(id),{type:'line',data:{labels,datasets:ds},options:{responsive:true,maintainAspectRatio:false,animation:ANIM,interaction:{mode:'index',intersect:false},
    scales:{x:{...xMono},y:{stacked:true,...yPct(max,step)}},plugins:{legend:LEG,tooltip:{...TIP,callbacks:{label:c=>'  '+c.dataset.label+': '+c.parsed.y.toFixed(1)+'%'}}},elements:{line:{tension:.25}}}});
}
function hexA(hex,a){const h=hex.replace('#','');const r=parseInt(h.slice(0,2),16),g=parseInt(h.slice(2,4),16),b=parseInt(h.slice(4,6),16);return `rgba(${r},${g},${b},${a})`;}
function lines(id,labels,obj,order,cmap,max,step,fmt){
  const ds=order.map(k=>({label:k,data:obj[k],borderColor:ck(cmap,k),backgroundColor:ck(cmap,k),borderWidth:2.5,tension:.3,pointRadius:2.6,pointHoverRadius:5,pointBackgroundColor:ck(cmap,k),pointBorderColor:COL.card,pointBorderWidth:1.4,spanGaps:true}));
  const ch=new Chart(document.getElementById(id),{type:'line',data:{labels,datasets:ds},options:{responsive:true,maintainAspectRatio:false,animation:ANIM,interaction:{mode:'index',intersect:false},
    scales:{x:{...xMono},y:(fmt==='mul'?yMul(max,step):yPct(max,step))},plugins:{legend:LEG,tooltip:{...TIP,callbacks:{label:c=>'  '+c.dataset.label+': '+c.parsed.y.toFixed(fmt==='mul'?2:1)+(fmt==='mul'?'\\u00d7':'%')}}}}});
  return ch;
}
const PARITY={id:'parity',afterDraw(ch){const o=ch.options.plugins.parityLine; if(!o)return; const{ctx,chartArea:{left,right},scales:{y}}=ch; const yy=y.getPixelForValue(o.v);
  ctx.save();ctx.strokeStyle=COL.ink_faint;ctx.lineWidth=1.3;ctx.setLineDash([5,4]);ctx.beginPath();ctx.moveTo(left,yy);ctx.lineTo(right,yy);ctx.stroke();ctx.setLineDash([]);
  ctx.fillStyle=COL.ink_faint;ctx.font="11px 'IBM Plex Mono',monospace";ctx.textAlign='right';ctx.fillText(o.label,right-4,yy-6);ctx.restore();}};

let nomChart=null;
const BUILD={
 long_bar:()=>stacked('c_long_bar',D.YEARS_LONG,D.LONG,D.LONG_ORDER,D.LONG_CK,100,20),
 long_area:()=>area('c_long_area',D.YEARS_LONG,D.LONG,D.LONG_ORDER,D.LONG_CK,100,20),
 mfg:()=>lines('c_mfg',D.YEARS_MFG,D.MFG,D.MFG_ORDER,D.MFG_CK,70,10,'pct'),
 nom:()=>{nomChart=lines('c_nom',D.YEARS_NOM,D.NOM,D.NOM_ORDER,D.NOM_CK,46,10,'pct');},
 us:()=>{const ch=new Chart(document.getElementById('c_us'),{type:'line',data:{labels:D.YEARS_US,datasets:[{label:'US nominal share',data:D.US_NOM,borderColor:COL.us,backgroundColor:hexA(COL.us,.08),borderWidth:2.6,fill:true,tension:.3,pointRadius:3.4,pointHoverRadius:6,pointBackgroundColor:COL.us,pointBorderColor:COL.card,pointBorderWidth:1.4}]},
   options:{responsive:true,maintainAspectRatio:false,animation:ANIM,plugins:{legend:{display:false},tooltip:{...TIP,callbacks:{label:c=>'  US: '+c.parsed.y+'%'}},
     annotation:false},scales:{x:{...xMono},y:yPct(58,10)}}});},
 bloc:()=>{const spec=[['West bloc \\u2014 nominal','us',false],['West bloc \\u2014 PPP','us',true],['China + India \\u2014 nominal','in',false],['China + India \\u2014 PPP','in',true]];
   const ds=spec.map(([k,col,dash])=>({label:k,data:D.BLOC[k],borderColor:COL[col],backgroundColor:COL[col],borderWidth:2.6,borderDash:dash?[5,4]:[],tension:.3,pointRadius:0,pointHoverRadius:5}));
   new Chart(document.getElementById('c_bloc'),{type:'line',data:{labels:D.YEARS_BLOC,datasets:ds},options:{responsive:true,maintainAspectRatio:false,animation:ANIM,interaction:{mode:'index',intersect:false},
     scales:{x:{...xMono},y:yPct(82,20)},plugins:{legend:LEG,tooltip:{...TIP,callbacks:{label:c=>'  '+c.dataset.label+': '+c.parsed.y.toFixed(1)+'%'}}}}});},
 delta:()=>{const ents=D.DELTA_ENT;const nom=ents.map(e=>D.DELTA_NOM[e]);const ppp=ents.map(e=>D.DELTA_PPP[e]);
   new Chart(document.getElementById('c_delta'),{type:'bar',data:{labels:ents,datasets:[{label:'Nominal change',data:nom,backgroundColor:COL.us,borderRadius:2,barPercentage:.8,categoryPercentage:.78},{label:'PPP change',data:ppp,backgroundColor:COL.eu,borderRadius:2,barPercentage:.8,categoryPercentage:.78}]},
     options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,animation:ANIM,scales:{x:{grid:GRID,border:{display:false},ticks:{callback:v=>(v>0?'+':'')+v,color:COL.ink_faint},min:-16,max:18},y:{grid:{display:false},border:{color:COL.rule},ticks:{color:COL.ink,font:{weight:'500'}}}},
       plugins:{legend:LEG,tooltip:{...TIP,callbacks:{label:c=>'  '+c.dataset.label+': '+(c.parsed.x>0?'+':'')+c.parsed.x.toFixed(1)+' pts'}}}}});},
 mult:()=>{const ch=lines('c_mult',D.YEARS_MULT,D.MULT,D.MULT_ORDER,D.MULT_CK,5,1,'mul');ch.options.plugins.parityLine={v:1,label:'world average 1.0\\u00d7'};ch.config.plugins=[PARITY];ch.update();},
 share24:()=>{new Chart(document.getElementById('c_share24'),{type:'bar',data:{labels:D.S24_ENT,datasets:[{label:'Market exchange rates (nominal)',data:D.S24_NOM,backgroundColor:COL.us,borderRadius:2,barPercentage:.82,categoryPercentage:.74},{label:'Purchasing power parity (PPP)',data:D.S24_PPP,backgroundColor:COL.cn,borderRadius:2,barPercentage:.82,categoryPercentage:.74}]},
   options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,animation:ANIM,scales:{x:{grid:GRID,border:{display:false},ticks:{callback:v=>v+'%',color:COL.ink_faint},min:0,max:30},y:{grid:{display:false},border:{color:COL.rule},ticks:{color:COL.ink,font:{weight:'500'}}}},
     plugins:{legend:LEG,tooltip:{...TIP,callbacks:{label:c=>'  '+c.dataset.label+': '+c.parsed.x.toFixed(1)+'%'}}}}});},
 gap24:()=>{const ents=[...D.GAP_ENT].sort((a,b)=>D.GAP[a]-D.GAP[b]);const vals=ents.map(e=>D.GAP[e]);const cols=vals.map(v=>v>=0?COL.us:COL.eu);
   new Chart(document.getElementById('c_gap24'),{type:'bar',data:{labels:ents,datasets:[{label:'gap',data:vals,backgroundColor:cols,borderRadius:2,barPercentage:.7,categoryPercentage:.8}]},
     options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,animation:ANIM,scales:{x:{grid:GRID,border:{display:false},ticks:{callback:v=>(v>0?'+':'')+v,color:COL.ink_faint},min:-6,max:13},y:{grid:{display:false},border:{color:COL.rule},ticks:{color:COL.ink,font:{weight:'500'}}}},
       plugins:{legend:{display:false},tooltip:{...TIP,callbacks:{title:()=>'',label:c=>'  '+(c.parsed.x>0?'+':'')+c.parsed.x.toFixed(1)+' pts '+(c.parsed.x>=0?'(nominal-heavy)':'(PPP-lifted)')}}}}});},
 mult24:()=>{const ch=new Chart(document.getElementById('c_mult24'),{type:'bar',data:{labels:D.M24_ENT,datasets:[{label:'Nominal (market rates)',data:D.M24_NOM,backgroundColor:COL.us,borderRadius:2,barPercentage:.82,categoryPercentage:.72},{label:'PPP',data:D.M24_PPP,backgroundColor:COL.cn,borderRadius:2,barPercentage:.82,categoryPercentage:.72}]},
   options:{responsive:true,maintainAspectRatio:false,animation:ANIM,scales:{x:{grid:{display:false},border:{color:COL.rule},ticks:{color:COL.ink_soft,font:{size:11},maxRotation:25,minRotation:0}},y:yMul(7,1)},
     plugins:{legend:LEG,parityLine:{v:1,label:'parity 1.0\\u00d7'},tooltip:{...TIP,callbacks:{label:c=>'  '+c.dataset.label+': '+c.parsed.y.toFixed(2)+'\\u00d7'}}}},plugins:[PARITY]});},
 scatter24:()=>{const lim=21.5;
   const pts=D.POP_ENT.map((e,i)=>({x:D.POP[i],y:D.POP_PPP[i],e:e}));
   const cols=D.POP_ENT.map(e=>COL[D.POP_CK[e]]);
   const off={'United States':[8,-2],'China':[9,4],'EU (27)':[8,-3],'India':[-8,-2],'Japan':[8,2],'United Kingdom':[-8,12],'Russia':[8,5]};
   const LBL={id:'sl',afterDatasetsDraw(ch){const ctx=ch.ctx;const m=ch.getDatasetMeta(1);ctx.save();ctx.font="500 11px 'IBM Plex Sans',sans-serif";ctx.fillStyle=COL.ink;
     pts.forEach((p,i)=>{const el=m.data[i];if(!el)return;const o=off[p.e]||[8,0];ctx.textAlign=o[0]<0?'right':'left';ctx.fillText(p.e,el.x+o[0],el.y+o[1]);});ctx.restore();}};
   new Chart(document.getElementById('c_scatter24'),{type:'scatter',data:{datasets:[
     {type:'line',label:'parity',data:[{x:0,y:0},{x:lim,y:lim}],borderColor:COL.ink_faint,borderWidth:1.3,borderDash:[5,4],pointRadius:0,fill:false,order:2},
     {label:'2024',data:pts,backgroundColor:cols,pointRadius:9,pointHoverRadius:11,pointBorderColor:COL.card,pointBorderWidth:1.6,order:1}]},
     options:{responsive:true,maintainAspectRatio:false,animation:ANIM,scales:{
       x:{min:0,max:lim,grid:GRID,border:{color:COL.rule},title:{display:true,text:'share of world population (%)',color:COL.ink_soft,font:{size:12}},ticks:{callback:v=>v+'%',color:COL.ink_faint}},
       y:{min:0,max:lim,grid:GRID,border:{color:COL.rule},title:{display:true,text:'share of world GDP, PPP (%)',color:COL.ink_soft,font:{size:12}},ticks:{callback:v=>v+'%',color:COL.ink_faint}}},
       plugins:{legend:{display:false},tooltip:{...TIP,filter:c=>c.datasetIndex===1,callbacks:{title:c=>c[0].raw.e,label:c=>'  pop '+c.parsed.x+'%  \\u00b7  PPP GDP '+c.parsed.y+'%'}}}},plugins:[LBL]});},
 jp:()=>{const spec=[['Japan \\u2014 nominal (market rates)','jp',false],['Japan \\u2014 PPP (real output)','ru',true]];
   const data={'Japan \\u2014 nominal (market rates)':D.JP_NOM,'Japan \\u2014 PPP (real output)':D.JP_PPP};
   const ds=spec.map(([k,col,dash])=>({label:k,data:data[k],borderColor:COL[col],backgroundColor:COL[col],borderWidth:2.6,borderDash:dash?[5,3]:[],tension:.3,pointRadius:2.6,pointHoverRadius:5,pointBackgroundColor:COL[col],pointBorderColor:COL.card,pointBorderWidth:1.2}));
   new Chart(document.getElementById('c_jp'),{type:'line',data:{labels:D.JP_YEARS,datasets:ds},options:{responsive:true,maintainAspectRatio:false,animation:ANIM,interaction:{mode:'index',intersect:false},
     scales:{x:{...xMono},y:yPct(20,5)},plugins:{legend:LEG,tooltip:{...TIP,callbacks:{label:c=>'  '+c.dataset.label+': '+c.parsed.y.toFixed(1)+'%'}}}}});},
 world_long:()=>{const labels=D.AGG_L_YEARS;
   new Chart(document.getElementById('c_world_long'),{data:{labels,datasets:[
     {type:'bar',label:'World population (billions)',data:D.AGG_L_POP,backgroundColor:hexA(COL.eu,.85),borderColor:COL.card,borderWidth:.7,yAxisID:'yp',order:2,barPercentage:.7,categoryPercentage:.8},
     {type:'line',label:"World real GDP (tn, 2011 int'l-$, PPP)",data:D.AGG_L_GDP,borderColor:COL.us,backgroundColor:COL.us,borderWidth:2.8,tension:.3,pointRadius:3.4,pointHoverRadius:6,pointBackgroundColor:COL.us,pointBorderColor:COL.card,pointBorderWidth:1.3,yAxisID:'yg',order:1}]},
     options:{responsive:true,maintainAspectRatio:false,animation:ANIM,interaction:{mode:'index',intersect:false},
       scales:{x:{...xMono},
         yp:{position:'left',min:0,max:7,grid:GRID,border:{color:COL.rule},title:{display:true,text:'world population (billions)',color:COL.ink_soft,font:{size:12}},ticks:{color:COL.ink_faint,stepSize:1}},
         yg:{position:'right',min:0,max:80,grid:{display:false},border:{color:COL.rule},title:{display:true,text:"world real GDP (tn, 2011 int'l-$)",color:COL.ink_soft,font:{size:12}},ticks:{color:COL.ink_faint,stepSize:20,callback:v=>'$'+v+'T'}}},
       plugins:{legend:LEG,tooltip:{...TIP,callbacks:{label:c=>'  '+c.dataset.label+': '+(c.dataset.yAxisID==='yp'?c.parsed.y.toFixed(2)+'bn':'$'+c.parsed.y.toFixed(1)+'T')}}}}});},
 world_modern:()=>{const PA=(xs,ys)=>xs.map((x,i)=>({x:x,y:ys[i]}));
   new Chart(document.getElementById('c_world_modern'),{data:{datasets:[
     {type:'line',label:'World population (billions)',data:PA(D.AGG_M_POP_X,D.AGG_M_POP),borderColor:COL.ink,backgroundColor:COL.ink,borderWidth:2.8,tension:.25,pointRadius:3.2,pointHoverRadius:6,pointBackgroundColor:COL.ink,pointBorderColor:COL.card,pointBorderWidth:1.2,yAxisID:'yp',order:1},
     {type:'line',label:'population (UN median projection)',data:PA(D.AGG_M_POP_PX,D.AGG_M_POP_PROJ),borderColor:hexA(COL.ink,.5),borderDash:[6,4],borderWidth:2.4,tension:0,pointRadius:0,yAxisID:'yp',order:1},
     {type:'line',label:"World GDP — nominal (current US$)",data:PA(D.AGG_M_NOM_X,D.AGG_M_NOM),borderColor:COL.us,backgroundColor:COL.us,borderWidth:2.6,tension:.25,pointRadius:3.2,pointHoverRadius:6,pointBackgroundColor:COL.us,pointBorderColor:COL.card,pointBorderWidth:1.2,yAxisID:'yg',order:2},
     {type:'line',label:"World GDP — PPP (current int'l-$)",data:PA(D.AGG_M_PPP_X,D.AGG_M_PPP),borderColor:COL.eu,backgroundColor:COL.eu,borderWidth:2.6,tension:.25,pointRadius:3.2,pointHoverRadius:6,pointBackgroundColor:COL.eu,pointBorderColor:COL.card,pointBorderWidth:1.2,yAxisID:'yg',order:2}]},
     options:{responsive:true,maintainAspectRatio:false,animation:ANIM,interaction:{mode:'nearest',axis:'x',intersect:false},
       scales:{x:{type:'linear',min:1900,max:2050,grid:GRID,border:{color:COL.rule},ticks:{stepSize:25,color:COL.ink_faint,callback:v=>''+v}},
         yp:{position:'left',min:0,max:11,grid:GRID,border:{color:COL.rule},title:{display:true,text:'world population (billions)',color:COL.ink_soft,font:{size:12}},ticks:{color:COL.ink_faint,stepSize:2}},
         yg:{position:'right',min:0,max:210,grid:{display:false},border:{color:COL.rule},title:{display:true,text:'world GDP (tn, current $)',color:COL.ink_soft,font:{size:12}},ticks:{color:COL.ink_faint,stepSize:50,callback:v=>'$'+v+'T'}}},
       plugins:{legend:{position:'bottom',align:'start',labels:{usePointStyle:true,pointStyle:'line',boxWidth:18,padding:11,color:COL.ink_soft,font:{size:12},filter:it=>it.text!=='population (UN median projection)'}},
         tooltip:{...TIP,callbacks:{title:c=>''+c[0].parsed.x,label:c=>'  '+c.dataset.label+': '+(c.dataset.yAxisID==='yp'?c.parsed.y.toFixed(2)+'bn':'$'+c.parsed.y.toFixed(0)+'T')}}}}});},
 swing24:()=>{const xmax=D.SWING_XMAX,ymax=35;
   const lineDs=D.SWING_ENT.map(e=>{const pop=D.SWING_POP[e];return{type:'line',label:e,data:[{x:0,y:0},{x:xmax,y:pop*xmax}],borderColor:COL[D.SWING_CK[e]],borderWidth:2.6,pointRadius:0,fill:false,tension:0,order:2};});
   const mk=D.SWING_ENT.map(e=>({x:D.SWING_MULT24[e],y:D.SWING_POP[e]*D.SWING_MULT24[e],e:e}));
   const mcols=D.SWING_ENT.map(e=>COL[D.SWING_CK[e]]);
   const dot={type:'scatter',label:'2024',data:mk,backgroundColor:mcols,pointRadius:7,pointHoverRadius:9,pointBorderColor:COL.card,pointBorderWidth:1.5,order:1};
   new Chart(document.getElementById('c_swing24'),{data:{datasets:[...lineDs,dot]},options:{responsive:true,maintainAspectRatio:false,animation:ANIM,
     scales:{x:{type:'linear',min:0,max:xmax,grid:GRID,border:{color:COL.rule},title:{display:true,text:'assumed PPP multiplier (output per person vs world)',color:COL.ink_soft,font:{size:12}},ticks:{stepSize:1,callback:v=>v+'\\u00d7',color:COL.ink_faint}},
       y:{min:0,max:ymax,grid:GRID,border:{color:COL.rule},title:{display:true,text:'implied share of world GDP (%)',color:COL.ink_soft,font:{size:12}},ticks:{callback:v=>v+'%',color:COL.ink_faint}}},
     plugins:{legend:{position:'bottom',align:'start',labels:{usePointStyle:true,pointStyle:'rectRounded',boxWidth:9,boxHeight:9,padding:14,color:COL.ink_soft,font:{size:12.5,weight:'500'},filter:it=>it.text!=='2024'}},
       tooltip:{...TIP,callbacks:{label:c=>'  '+(c.dataset.label==='2024'?(c.raw.e+' 2024'):c.dataset.label)+': '+c.parsed.y.toFixed(1)+'% at '+c.parsed.x.toFixed(2)+'\\u00d7'}}}}});}
};

const done={};
const io=new IntersectionObserver((ents)=>{ents.forEach(en=>{if(en.isIntersecting){const id=en.target.id.replace('fig_','');en.target.classList.add('in');
  if(BUILD[id]&&!done[id]){done[id]=true;try{BUILD[id]();requestAnimationFrame(()=>{const cc=(window.Chart&&Chart.getChart)?Chart.getChart('c_'+id):null;if(cc)cc.resize();});}catch(e){console.error(id,e);}} if(id==='nom')wireWest(); io.unobserve(en.target);}});},{threshold:.12});
Object.keys(BUILD).forEach(k=>{const el=document.getElementById('fig_'+k);if(el)io.observe(el);});

function wireWest(){const btn=document.getElementById('westBtn');if(!btn||btn._wired)return;btn._wired=true;
  const W={label:'\\u201cWest\\u201d bloc (US+EU+UK+Japan)',data:D.WEST,borderColor:COL.accent,backgroundColor:hexA(COL.accent,.06),borderWidth:3,borderDash:[6,3],tension:.3,fill:true,pointRadius:0,order:-1};
  btn.addEventListener('click',e=>{if(!nomChart)return;const on=btn.getAttribute('aria-pressed')==='true';
    if(on){const i=nomChart.data.datasets.findIndex(d=>d.label===W.label);if(i>-1)nomChart.data.datasets.splice(i,1);btn.setAttribute('aria-pressed','false');btn.textContent='+ Show the \\u201cWest\\u201d bloc (US + EU + UK + Japan)';}
    else{nomChart.data.datasets.push({...W});btn.setAttribute('aria-pressed','true');btn.textContent='\\u2013 Hide the \\u201cWest\\u201d bloc';}
    nomChart.update();});}

window.addEventListener('load',()=>{if(typeof Chart==='undefined'){document.querySelectorAll('.chart-box').forEach(b=>{b.innerHTML='<p style=\\'font-family:monospace;font-size:12px;color:#8C8273;padding:40px 0\\'>[ chart library could not load ]</p>';});}});
"""

def build():
    import charts
    for k in NEW_STATIC:                       # ensure coda PNGs exist for base64 inlining
        if not os.path.exists(os.path.join(_ASSETS, k + ".png")):
            charts.RENDERERS[k]()
    body = common.body_html(fig_inner)
    script = SCRIPT.replace("__DATA__", DATA_JS)
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Shifting Weight of Nations — Five Centuries of World GDP</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
<style>{CSS}</style></head><body><div class="wrap">
{body}
</div><script>{script}</script></body></html>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    return OUT, len(html)

if __name__ == "__main__":
    p, n = build()
    print("wrote", p, n, "bytes")
