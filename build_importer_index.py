#!/usr/bin/env python3
"""
The WorldFirst Importer Index — flagship survey report (illustrative edition).
The Importer Index franchise, built as a real report artifact.
Encrypts inner content with 'wf'. Same LS key as the other strategy pages.
"""
import os, base64, json, pathlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes

ROOT = pathlib.Path(__file__).resolve().parent
PASSWORD = "wf"
ITERATIONS = 100_000
LS_KEY = "wf_content_pw"

def encrypt_payload(plaintext: str, password: str = PASSWORD) -> dict:
    salt = os.urandom(16); iv = os.urandom(12)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITERATIONS)
    key = kdf.derive(password.encode("utf-8"))
    ct = AESGCM(key).encrypt(iv, plaintext.encode("utf-8"), None)
    return {"v":1,"salt":base64.b64encode(salt).decode(),"iv":base64.b64encode(iv).decode(),
            "iterations":ITERATIONS,"ciphertext":base64.b64encode(ct).decode()}

# ----------------------------------------------------------------------------
# Chart helper — horizontal bars
# ----------------------------------------------------------------------------
def chart(items, unit="%"):
    rows = []
    for label, pct, hi in items:
        cls = "chart-fill chart-fill-hi" if hi else "chart-fill"
        rows.append(f"""<div class="chart-row">
      <span class="chart-label">{label}</span>
      <span class="chart-track"><span class="{cls}" style="width:{pct}%"></span></span>
      <span class="chart-val">{pct}{unit}</span>
    </div>""")
    return '<div class="chart">' + "".join(rows) + '</div>'

def bigstat(num, text):
    return f'<div class="bigstat"><p class="bigstat-n">{num}</p><p class="bigstat-t">{text}</p></div>'

# ----------------------------------------------------------------------------
# Content
# ----------------------------------------------------------------------------
HERO = """
<header class="page-header">
  <p class="eyebrow">The WorldFirst Importer Index · 2027</p>
  <h1 class="page-title">The State of Sourcing.</h1>
  <p class="page-byline">What 1,200 Southeast Asian importers told us about sourcing from China — the trust, the scams, the money, and the year ahead.</p>
  <div class="hero-stat">
    <p class="hero-stat-n">73%</p>
    <p class="hero-stat-t">of Southeast Asian importers have lost money to a supplier. This is the full picture.</p>
  </div>
  <p class="addendum-link"><a href="landscape.html">← Content landscape</a> · The Importer Index franchise, built as a real report</p>
</header>
"""

METHOD = """
<section id="method" class="section">
  <p class="kicker">Method</p>
  <h2 class="section-title">What the Index is.</h2>
  <p class="lede">The WorldFirst Importer Index is an independent survey of Southeast Asian importers — the people sourcing goods from China and selling across the region. One purpose: to give importers an honest picture of the trade they are in.</p>
  <p>The 2027 edition draws on <strong>1,200 responses</strong> across <strong>Malaysia, Singapore, Thailand and Vietnam</strong>, from importers running businesses of every size — first-order side hustles through to teams shipping containers monthly. Every finding is published free, in full.</p>
  <p class="method-note"><strong>About this edition.</strong> This is an illustrative edition. It shows the format, the structure and the kind of findings the Index produces — the figures are realistic, research-grounded examples, not yet-collected data. It is the template the first live edition will follow.</p>
</section>
"""

F1 = f"""
<section id="f1" class="section">
  <p class="kicker">Finding 01</p>
  <h2 class="section-title">The number one worry is trust — not tariffs.</h2>
  <p class="lede">We asked importers to name their single biggest sourcing worry for 2027. Trade media spends its year on tariffs. Importers don't.</p>
  {chart([("Supplier trust", 62, True), ("Product quality", 18, False), ("Freight &amp; logistics", 12, False), ("Tariffs &amp; policy", 8, False)])}
  <p>62% named <strong>supplier trust</strong> — whether the factory on the other end will actually deliver what was agreed. Tariffs, the headline of nearly every trade-news story, came last at 8%. The dominant anxiety in this trade is quiet, and it is badly under-served by the content importers are offered.</p>
</section>
"""

F2 = f"""
<section id="f2" class="section">
  <p class="kicker">Finding 02</p>
  <h2 class="section-title">Almost everyone has been burned.</h2>
  <p class="lede">Trust tops the worry list for a simple reason: the damage is near-universal.</p>
  {bigstat("73%", "have lost money to a supplier at least once — a deposit gone, goods that never matched the sample, an order that never shipped.")}
  <p>And it is worst for the newest importers, the ones least able to absorb it. Among importers in their first three years, the figure climbs to 81%. Experience reduces the risk; it never removes it.</p>
  {chart([("First 3 years", 81, True), ("3–7 years", 72, False), ("7+ years", 64, False)])}
</section>
"""

F3 = f"""
<section id="f3" class="section">
  <p class="kicker">Finding 03</p>
  <h2 class="section-title">The anatomy of a burn.</h2>
  <p class="lede">We asked importers who had lost money what actually went wrong. Four patterns covered nine in ten cases.</p>
  {chart([("Bait-and-switch", 41, True), ("Deposit redirect", 27, False), ("Fake / no factory", 19, False), ("Weight &amp; freight overcharge", 13, False)])}
  <ul class="anat">
    <li><strong>Bait-and-switch (41%)</strong> — the sample was perfect, the bulk order was not. The single most common failure, and the hardest to catch before the money has moved.</li>
    <li><strong>Deposit redirect (27%)</strong> — mid-deal, the supplier asked for the deposit to go to a different account, often a personal one. More than one in four importers has seen this.</li>
    <li><strong>Fake or no factory (19%)</strong> — the "factory" was a trading company, or did not exist as described.</li>
    <li><strong>Weight &amp; freight overcharge (13%)</strong> — the shipment was billed at a weight the importer could not verify.</li>
  </ul>
</section>
"""

F4 = f"""
<section id="f4" class="section">
  <p class="kicker">Finding 04</p>
  <h2 class="section-title">Importers pay before they check.</h2>
  <p class="lede">The gap that creates the loss is a behavioural one — and importers know it.</p>
  {bigstat("68%", "had paid a supplier deposit before doing any verification of the factory — no video tour, no third-party check, no reference call.")}
  <p>The verification step is widely known and widely skipped — almost always under time pressure from the supplier ("another buyer is waiting", "the price holds until Friday"). Among the importers who <em>did</em> verify before paying, the reported loss rate on that order fell by more than half. The check works. The problem is that it loses to the clock.</p>
</section>
"""

F5 = f"""
<section id="f5" class="section">
  <p class="kicker">Finding 05</p>
  <h2 class="section-title">Off-platform, and exposed.</h2>
  <p class="lede">One risk in the data is specific, common, and almost entirely avoidable.</p>
  {bigstat("1 in 4", "importers has been asked by a supplier to pay outside the platform — a direct bank transfer, a personal account.")}
  <p>24% were asked; <strong>61% of those asked, did it.</strong> And paying off-platform quietly removes the dispute protection that platforms such as Alibaba provide — the recourse an importer is counting on if the order goes wrong. Most importers we surveyed did not know that connection until after a loss. It is the clearest example in the whole Index of a risk that is pure information gap: importers are not reckless, they are uninformed at the exact moment it matters.</p>
</section>
"""

F6 = f"""
<section id="f6" class="section">
  <p class="kicker">Finding 06</p>
  <h2 class="section-title">The FX blind spot.</h2>
  <p class="lede">Importers watch the product price to the cent. Far fewer watch the currency.</p>
  {bigstat("7 in 10", "could not say what FX margin their bank or provider charged on their most recent supplier payment.")}
  <p>On a typical order, that margin is often larger than the price difference the importer negotiated so hard for. It is invisible because of how payments are made — the rate is shown once, at the moment of transfer, and never compared.</p>
  {chart([("Bank wire / TT", 48, True), ("Third-party agent", 31, False), ("Payment fintech", 16, False), ("Other", 5, False)])}
  <p>Bank wire is still how nearly half of importers pay their suppliers — the channel where the FX margin is widest and least visible.</p>
</section>
"""

F7 = f"""
<section id="f7" class="section">
  <p class="kicker">Finding 07</p>
  <h2 class="section-title">The 2027 outlook.</h2>
  <p class="lede">Despite all of it, the Southeast Asian importer is not retreating.</p>
  {chart([("Increase volume", 64, True), ("Hold steady", 28, False), ("Reduce volume", 8, False)])}
  <p>64% plan to increase their China sourcing volume in 2027; only 8% to reduce. The appetite is not in question. What importers told us they want is not <em>less</em> sourcing — it is a <strong>safer way to do the sourcing they are already committed to.</strong> That is the gap the trade still has not closed for them.</p>
</section>
"""

REGIONAL = """
<section id="regional" class="section">
  <p class="kicker">Regional snapshot</p>
  <h2 class="section-title">Four markets, four pictures.</h2>
  <p class="lede">The Index is regional, and the four markets do not behave alike.</p>
  <div class="table-wrap">
    <table class="rtbl">
      <thead>
        <tr><th>Market</th><th>Burned at least once</th><th>Most common burn</th><th>Plan to increase in 2027</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Malaysia</strong></td><td>76%</td><td>Bait-and-switch</td><td>67%</td></tr>
        <tr><td><strong>Singapore</strong></td><td>64%</td><td>Deposit redirect</td><td>58%</td></tr>
        <tr><td><strong>Thailand</strong></td><td>71%</td><td>Bait-and-switch</td><td>62%</td></tr>
        <tr><td><strong>Vietnam</strong></td><td>79%</td><td>Fake / no factory</td><td>71%</td></tr>
      </tbody>
    </table>
  </div>
  <p>Vietnam and Malaysia carry the highest burn rates — both have the youngest, fastest-growing importer bases, and inexperience shows in the data. Singapore importers report the lowest burn rate and are the most likely to verify a factory before paying — discipline that the numbers reward. Across all four, the appetite to source more in 2027 holds.</p>
</section>
"""

ABOUT = """
<section id="about" class="section">
  <p class="kicker">About the Index</p>
  <h2 class="section-title">Built by importers, for importers.</h2>
  <p class="lede">Every finding here came from an importer who took two minutes to answer. That is the whole method — and the whole point.</p>
  <p>The WorldFirst Importer Index has no proprietary dataset behind it and needs none. It is the Southeast Asian importer community, asked a clear question and answered honestly, then aggregated and published in full. The more importers take part, the sharper the picture becomes — for everyone in the trade.</p>
  <div class="cta-box">
    <p class="cta-eyebrow">The next edition is open</p>
    <p class="cta-title">If you source from China, take part in the next Importer Index.</p>
    <p class="cta-body">Two minutes. We publish everything, free — and contributors get the full results first. The Index runs every year, and it only gets better the more of the trade is in it.</p>
  </div>
  <p class="about-foot">The WorldFirst Importer Index · published annually · free, in full. This 2027 edition is illustrative — sample findings shown in the live format.</p>
</section>
"""

FOOTER = """
<footer class="site-footer">
  <p>WorldFirst · Internal · The Importer Index 2027 (illustrative edition) · <a href="#" id="lock">lock device</a></p>
</footer>
"""

INNER = HERO + METHOD + F1 + F2 + F3 + F4 + F5 + F6 + F7 + REGIONAL + ABOUT + FOOTER

# ----------------------------------------------------------------------------
# CSS
# ----------------------------------------------------------------------------
CSS = """
:root{--wf-pink:#E6185F;--wf-pink-soft:#FFE6EE;--cream:#FFFAF2;--ink:#1A1A1A;--ink-soft:#555;--ink-mute:#888;--line:#E5E0D5;--line-soft:#F0EBE0;--paper:#fff;}
*{box-sizing:border-box;margin:0;padding:0;}
[hidden]{display:none!important;}
html{scroll-behavior:smooth;}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--cream);color:var(--ink);line-height:1.65;font-size:15.5px;-webkit-font-smoothing:antialiased;}
body.locked .wrap{filter:blur(20px);pointer-events:none;user-select:none;}
a{color:var(--ink);text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:3px;}
a:hover{text-decoration-color:var(--wf-pink);}
.progress{position:fixed;top:0;left:0;height:2px;background:var(--wf-pink);z-index:100;width:0;transition:width .05s linear;}
.gate{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px;}
.gate-card{width:100%;max-width:420px;text-align:center;}
.gate-eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:22px;}
.gate-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:46px;letter-spacing:-.02em;margin-bottom:14px;line-height:1.06;}
.gate-subtitle{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:18px;color:var(--ink-soft);margin-bottom:38px;}
#gate-form{display:flex;flex-direction:column;gap:10px;margin-bottom:12px;}
#gate-input{width:100%;padding:13px 16px;font-size:15px;font-family:'JetBrains Mono',monospace;border:1px solid var(--line);border-radius:3px;background:#fff;outline:none;}
#gate-input:focus{border-color:var(--wf-pink);}
#gate-btn{padding:13px 16px;font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.08em;background:var(--ink);color:#fff;border:none;border-radius:3px;cursor:pointer;}
#gate-btn:hover{background:var(--wf-pink);}
#gate-err{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--wf-pink);margin-top:6px;min-height:18px;}
.wrap{display:grid;grid-template-columns:230px minmax(0,1fr);gap:56px;max-width:1140px;margin:0 auto;padding:56px 44px 120px;}
@media(max-width:980px){.wrap{grid-template-columns:1fr;gap:28px;padding:30px 18px 80px;}.toc{position:relative!important;top:0!important;}}
.toc{position:sticky;top:36px;align-self:start;font-family:'JetBrains Mono',monospace;font-size:12px;}
.toc-lbl{text-transform:uppercase;letter-spacing:.14em;color:var(--ink-mute);margin-bottom:16px;font-size:11px;}
.toc-list{list-style:none;display:flex;flex-direction:column;gap:2px;}
.toc-list a{display:block;padding:6px 10px;text-decoration:none;color:var(--ink-soft);border-left:2px solid transparent;line-height:1.35;transition:.15s;}
.toc-list a:hover{color:var(--ink);}
.toc-list a.active{color:var(--wf-pink);border-left-color:var(--wf-pink);}
.page-header{padding-bottom:40px;border-bottom:1px solid var(--line);margin-bottom:48px;}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:20px;}
.page-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:64px;line-height:1.0;letter-spacing:-.03em;margin-bottom:16px;}
.page-byline{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:21px;color:var(--ink-soft);max-width:640px;margin-bottom:28px;}
.hero-stat{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:24px 0;margin-bottom:24px;display:flex;gap:24px;align-items:baseline;flex-wrap:wrap;}
.hero-stat-n{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:80px;line-height:.9;color:var(--wf-pink);letter-spacing:-.03em;}
.hero-stat-t{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:21px;color:var(--ink);max-width:380px;line-height:1.35;}
.addendum-link{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--ink-mute);}
.addendum-link a{color:var(--ink-mute);}
.section{padding-top:54px;padding-bottom:30px;scroll-margin-top:24px;border-top:1px solid var(--line);}
.section:first-of-type{border-top:none;padding-top:0;}
.kicker{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:14px;}
.section-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:35px;letter-spacing:-.018em;line-height:1.14;margin-bottom:20px;max-width:720px;}
.section p{margin-bottom:14px;max-width:700px;}
.section p strong{color:var(--ink);}
.section em{font-style:italic;}
.lede{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:19px;color:var(--ink-soft);margin-bottom:18px;max-width:680px;line-height:1.5;}
.method-note{font-size:13px;color:var(--ink-mute);border-left:2px solid var(--line);padding-left:14px;}
.method-note strong{color:var(--ink-soft);}
/* chart */
.chart{display:flex;flex-direction:column;gap:9px;margin:20px 0 16px;max-width:600px;}
.chart-row{display:grid;grid-template-columns:148px 1fr 46px;gap:12px;align-items:center;}
.chart-label{font-size:13px;color:var(--ink);}
.chart-track{height:22px;background:var(--line-soft);border-radius:3px;overflow:hidden;}
.chart-fill{display:block;height:100%;background:var(--wf-pink);opacity:.4;}
.chart-fill-hi{opacity:1;}
.chart-val{font-family:'JetBrains Mono',monospace;font-size:13px;color:var(--ink);text-align:right;}
/* bigstat */
.bigstat{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:24px 0;margin:20px 0;}
.bigstat-n{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:68px;line-height:.95;color:var(--wf-pink);letter-spacing:-.025em;}
.bigstat-t{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:19px;color:var(--ink);margin-top:10px;max-width:560px;line-height:1.4;}
/* anatomy list */
.anat{margin:14px 0 0 0;padding:0;list-style:none;max-width:700px;}
.anat li{padding:11px 0;border-bottom:1px solid var(--line-soft);font-size:14px;color:var(--ink-soft);}
.anat li:last-child{border-bottom:none;}
.anat li strong{color:var(--ink);}
/* regional table */
.table-wrap{overflow-x:auto;margin:18px 0 16px;}
.rtbl{width:100%;border-collapse:collapse;font-size:13.5px;}
.rtbl th,.rtbl td{padding:11px 14px;text-align:left;border-bottom:1px solid var(--line);}
.rtbl th{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.07em;color:var(--ink);border-bottom:1px solid var(--ink);}
.rtbl td{color:var(--ink-soft);}
.rtbl tbody tr:hover{background:var(--line-soft);}
/* cta */
.cta-box{border:1px solid var(--wf-pink);border-radius:5px;padding:26px 28px;margin:22px 0;background:#FFF1F5;max-width:660px;}
.cta-eyebrow{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.12em;color:var(--wf-pink);margin-bottom:10px;}
.cta-title{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:22px;line-height:1.25;margin-bottom:10px!important;}
.cta-body{font-size:14px;color:var(--ink-soft);margin:0!important;}
.about-foot{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);line-height:1.6;}
.site-footer{margin-top:46px;padding-top:26px;border-top:1px solid var(--line);font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);text-transform:uppercase;letter-spacing:.08em;}
.site-footer a{color:var(--wf-pink);text-decoration:none;}
"""

blob = encrypt_payload(INNER)
payload_json = json.dumps(blob)

HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>The WorldFirst Importer Index 2027</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>__CSS__</style>
</head>
<body class="locked">
<div class="progress" id="progress"></div>
<section id="gate" class="gate">
  <div class="gate-card">
    <p class="gate-eyebrow">WorldFirst · Internal</p>
    <h1 class="gate-title">The Importer Index</h1>
    <p class="gate-subtitle">The State of Sourcing 2027.</p>
    <form id="gate-form" onsubmit="return gateSubmit(event)">
      <input id="gate-input" type="password" placeholder="password" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" autofocus>
      <button id="gate-btn" type="submit">enter</button>
    </form>
    <div id="gate-err"></div>
  </div>
</section>
<div id="content" hidden></div>
<script type="application/json" id="payload">__PAYLOAD__</script>
<script>
const LS_KEY="__LS_KEY__";
function b64ToBytes(b){const s=atob(b),a=new Uint8Array(s.length);for(let i=0;i<s.length;i++)a[i]=s.charCodeAt(i);return a;}
async function deriveKey(pw,salt,it){const e=new TextEncoder();const bk=await crypto.subtle.importKey("raw",e.encode(pw),"PBKDF2",false,["deriveKey"]);return crypto.subtle.deriveKey({name:"PBKDF2",salt,iterations:it,hash:"SHA-256"},bk,{name:"AES-GCM",length:256},false,["decrypt"]);}
async function decryptPayload(pw){const b=JSON.parse(document.getElementById('payload').textContent);const k=await deriveKey(pw,b64ToBytes(b.salt),b.iterations);const p=await crypto.subtle.decrypt({name:"AES-GCM",iv:b64ToBytes(b.iv)},k,b64ToBytes(b.ciphertext));return new TextDecoder().decode(p);}
function mountContent(html){
  const wrap=document.createElement('div');wrap.className='wrap';
  wrap.innerHTML=`<aside class="toc"><p class="toc-lbl">Contents</p><ul class="toc-list">
    <li><a href="#method">Method</a></li>
    <li><a href="#f1">01 · The #1 worry</a></li>
    <li><a href="#f2">02 · Everyone's been burned</a></li>
    <li><a href="#f3">03 · Anatomy of a burn</a></li>
    <li><a href="#f4">04 · Pay before they check</a></li>
    <li><a href="#f5">05 · Off-platform</a></li>
    <li><a href="#f6">06 · The FX blind spot</a></li>
    <li><a href="#f7">07 · The 2027 outlook</a></li>
    <li><a href="#regional">Regional snapshot</a></li>
    <li><a href="#about">About the Index</a></li>
  </ul></aside><main>${html}</main>`;
  const t=document.getElementById('content');t.innerHTML='';t.appendChild(wrap);t.hidden=false;
  document.getElementById('gate').style.display='none';document.body.classList.remove('locked');initScroll();
}
function initScroll(){
  const pr=document.getElementById('progress');
  const onS=()=>{const h=document.documentElement;const tot=h.scrollHeight-h.clientHeight;pr.style.width=(tot>0?(h.scrollTop/tot)*100:0)+'%';};
  window.addEventListener('scroll',onS,{passive:true});onS();
  const links=Array.from(document.querySelectorAll('.toc-list a'));
  const secs=links.map(a=>document.querySelector(a.getAttribute('href')));
  const setA=()=>{const y=window.scrollY+100;let idx=0;secs.forEach((s,i)=>{if(s&&s.offsetTop<=y)idx=i;});links.forEach((a,i)=>a.classList.toggle('active',i===idx));};
  window.addEventListener('scroll',setA,{passive:true});setA();
  const lk=document.getElementById('lock');if(lk)lk.addEventListener('click',e=>{e.preventDefault();try{localStorage.removeItem(LS_KEY);}catch(_){}location.reload();});
}
async function gateSubmit(e){
  e.preventDefault();const inp=document.getElementById('gate-input'),err=document.getElementById('gate-err');err.textContent='';
  try{const h=await decryptPayload(inp.value);mountContent(h);try{localStorage.setItem(LS_KEY,inp.value);}catch(_){}}
  catch(ex){err.textContent='wrong password';inp.value='';inp.focus();}
  return false;
}
(async()=>{try{const c=localStorage.getItem(LS_KEY);if(c){mountContent(await decryptPayload(c));}}catch(_){try{localStorage.removeItem(LS_KEY);}catch(_){}}})();
</script>
</body>
</html>
"""
HTML = HTML.replace("__CSS__", CSS).replace("__PAYLOAD__", payload_json).replace("__LS_KEY__", LS_KEY)
(ROOT / "importer-index.html").write_text(HTML, encoding="utf-8")
print(f"Wrote importer-index.html ({len(HTML):,} bytes; {len(INNER):,} inner)")
