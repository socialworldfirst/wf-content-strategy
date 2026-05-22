#!/usr/bin/env python3
"""
Project Canopy — Foundation Exploration (recut).
Five candidate angles for the Sourcing Tree, re-derived through the audience's
lens only. Each shown as a Malaysian importer would see it. Encrypts with 'wf'.
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
# Helpers
# ----------------------------------------------------------------------------
def feed(items):
    cards = []
    for kind, label, text in items:
        play = '<span class="play"></span>' if kind in ("youtube","short") else ''
        cards.append(f'<div class="art art-{kind}"><p class="art-lbl">{play}{label}</p>'
                     f'<p class="art-txt">{text}</p></div>')
    return '<div class="feed">' + "".join(cards) + '</div>'

def dots(n):
    return '<span class="dots">' + "".join(
        f'<span class="dot {"dot-on" if i < n else ""}"></span>' for i in range(3)) + '</span>'

def scorecard(rows):
    return '<div class="score">' + "".join(
        f'<div class="score-row"><span class="score-lbl">{l}</span>{dots(n)}</div>'
        for l, n in rows) + '</div>'

def option(num, sid, name, question, what, feed_items, why, score_rows):
    return f"""
<section id="{sid}" class="section">
  <p class="kicker">Angle {num}</p>
  <h2 class="section-title">{name}</h2>
  <p class="lede">&ldquo;{question}&rdquo;</p>
  <p>{what}</p>
  <p class="block-lbl">What a Malaysian importer would see</p>
  {feed(feed_items)}
  <p class="block-lbl">Why they want it</p>
  <p>{why}</p>
  <p class="block-lbl">Through the audience's eyes</p>
  {scorecard(score_rows)}
</section>
"""

# ----------------------------------------------------------------------------
# Content
# ----------------------------------------------------------------------------
HERO = """
<header class="page-header">
  <p class="eyebrow">Project Canopy · Foundation Exploration · Recut</p>
  <h1 class="page-title">Where the content starts.</h1>
  <p class="page-byline">Five angles for the Sourcing Tree, re-derived through one lens only: what a Malaysian importer is truly interested in.</p>
  <p class="addendum-link"><a href="canopy.html">&larr; Project Canopy</a> · Audience: ~600,000 Malaysian sellers who source from China and sell at home</p>
</header>
"""

HOW = """
<section id="how" class="section">
  <p class="kicker">How to read this</p>
  <h2 class="section-title">Take two. This time, only the audience's lens.</h2>
  <p class="lede">The first set of angles was scored on whether WorldFirst could own them, defend them, keep them evergreen, attach the brand. That is WorldFirst's lens. It ranked the one thing the audience wants most, what to sell, stone last.</p>
  <p>A Malaysian importer does not care whether we can own a topic. They care what makes them money. So the only lens on this page is theirs: what they search for, click, save, send, and act on.</p>
  <p>One rule runs underneath all of it. <strong>The audience does not want content about their situation. They want a tool for their next decision.</strong> Not the story of sourcing, but what to sell. Not the emotion of a scam, but the ten-minute check. Five angles, re-derived that way.</p>
  <p class="method-note"><strong>Status.</strong> Still an exploration. No angle chosen. WorldFirst's connection to the content is real, and it is handled once, at the end. It is a consequence of the angle, not a filter on it.</p>
</section>
"""

O1 = option(
  "01", "a1", "The Profit Map",
  "What should I actually be selling?",
  "A real research effort into where the money is for a Malaysian importer. The categories and products that are genuinely profitable to import from China and sell in Malaysia, with margin, demand and competition mapped and ranked. Re-cut every year.",
  [("youtube","YouTube title","The 5 Most Profitable Things to Import and Sell in Malaysia in 2026."),
   ("short","Short video hook","Stop selling phone cases. This is what is actually making sellers money in 2026."),
   ("carousel","Carousel headline","8 categories ranked by real margin. Number 3 surprised us."),
   ("post","Feed post","Everyone asks what to sell. So we ran the numbers on 40 categories. Here are the five worth your money this year.")],
  "This is the question every seller asks before any other, and the one almost nobody answers with real work instead of a guess. A ranked list, a promise of profit, their market, this year. They search it, they click it, they save it, they send it to their group chat. It is also the strongest franchise on the page: a fresh edition every year, and a category deep dive sitting behind every line on the map.",
  [("Searched",3),("Watched",3),("Saved &amp; sent",3),("Points at profit",3)]
)

O2 = option(
  "02", "a2", "The Price Breakdown",
  "If I import this, what do I actually make?",
  "The real money math. Take one real product, follow it from the 1688 price to the Malaysian shelf, and show the true landed cost and the true profit, in ringgit, with nothing left out. Worked examples, not a theory lecture.",
  [("youtube","YouTube title","I Imported a RM4 Item from 1688. Here Is Exactly What I Made on It."),
   ("short","Short video hook","1688 price: RM4.20. Shelf price: RM29. Your profit is not RM24.80. Here is the real figure."),
   ("carousel","Carousel headline","From the 1688 listing to your Shopee shelf: every cost, on one real product."),
   ("post","Feed post","A RM4 product is not a RM4 product. Here is its full journey to your customer, in ringgit, with nothing hidden.")],
  "Sellers do not want a lecture on the costs they are missing. They want the real number on a real product, laid out so they can copy the math straight onto their own. Concrete, copyable, and pointed directly at profit. It is the most saved angle of the five.",
  [("Searched",2),("Watched",2),("Saved &amp; sent",3),("Points at profit",3)]
)

O3 = option(
  "03", "a3", "The Sourcing Playbook",
  "Where do I find it, and how do I buy it without getting burned?",
  "The practical how-to of getting the product in hand. Where to find the supplier, how to get the price down, how to place the order, and how not to get cheated doing it.",
  [("youtube","YouTube title","How to Find a 1688 Supplier That Will Not Waste Your Money."),
   ("short","Short video hook","Three messages. That is all it takes to tell a real factory from a middleman."),
   ("carousel","Carousel headline","The 10-minute check before you pay any China supplier a single cent."),
   ("post","Feed post","You found the product. Now the part nobody explains properly: how to actually buy it, safely, from 8,000km away.")],
  "Once a seller knows what to sell, this is the very next thing they need, and they need it as steps, not as a story. The scam-avoidance the audience genuinely worries about lives here as a practical check, not an emotional documentary. Pure do-this-now content, and the most saved alongside the Price Breakdown.",
  [("Searched",3),("Watched",2),("Saved &amp; sent",3),("Points at profit",2)]
)

O4 = option(
  "04", "a4", "The Trend Radar",
  "What is hot right now, and what should I stock next?",
  "The fast read on what is selling in Malaysia right now, what is cooling off, and what to order from China before each season. The timely, frequently-refreshed angle.",
  [("youtube","YouTube title","What Malaysians Are Buying Right Now, and What to Import Before Raya."),
   ("short","Short video hook","This category looked dead last year. Look at it now."),
   ("carousel","Carousel headline","5 products heating up on Shopee Malaysia this quarter."),
   ("post","Feed post","Year-end is 11 weeks away. Here is what to order from China now, while the factories still have the time.")],
  "Sellers live and die on timing. Stock the wrong thing, or the right thing too late, and the season is gone. This is the angle they check again and again, not once. The trade-off is built in and fine: it dates fast, which is exactly why it works as a frequently-refreshed branch format rather than a once-a-year report.",
  [("Searched",3),("Watched",3),("Saved &amp; sent",2),("Points at profit",2)]
)

O5 = option(
  "05", "a5", "The Proof",
  "Who is actually doing this, and what did it really take?",
  "Real Malaysian importers, real numbers. What a working store actually chose, paid, and earned. The case study with the figures in it, not the highlight reel.",
  [("youtube","YouTube title","She Sells RM40,000 a Month on Shopee. We Went Through Her Numbers."),
   ("short","Short video hook","He started with RM3,000 and one category. Here is what year one really looked like."),
   ("carousel","Carousel headline","One seller, one product, the real first-year profit and loss."),
   ("post","Feed post","Not a success story. The actual numbers: what she imported, what it cost her, what she kept.")],
  "Proof and aspiration at once. A seller wants to see someone like them actually doing it, with the real figures on the table, so they can trace the path themselves. It is more aspiration than tool, which is why it watches better than it gets searched, but it earns trust like nothing else can.",
  [("Searched",2),("Watched",3),("Saved &amp; sent",2),("Points at profit",2)]
)

def crow(name, scores):
    cells = "".join(f"<td>{dots(n)}</td>" for n in scores)
    return f"<tr><td><strong>{name}</strong></td>{cells}</tr>"

COMPARE = f"""
<section id="compare" class="section">
  <p class="kicker">Side by side</p>
  <h2 class="section-title">All five, through the audience's eyes.</h2>
  <p class="lede">Scored only on the audience. Read down the columns.</p>
  <div class="table-wrap">
    <table class="rtbl">
      <thead>
        <tr><th>Angle</th><th>Searched</th><th>Watched</th><th>Saved &amp; sent</th><th>Points at profit</th></tr>
      </thead>
      <tbody>
        {crow("01 The Profit Map",[3,3,3,3])}
        {crow("02 The Price Breakdown",[2,2,3,3])}
        {crow("03 The Sourcing Playbook",[3,2,3,2])}
        {crow("04 The Trend Radar",[3,3,2,2])}
        {crow("05 The Proof",[2,3,2,2])}
      </tbody>
    </table>
  </div>
  <p>The Profit Map leads, because &ldquo;what should I sell&rdquo; is the question every Malaysian importer asks before any other, and the one almost nobody answers with real research. The other four are strong, and all five can become trunks in time. The open question is only which one the Sourcing Tree starts with.</p>
</section>
"""

WHEREWF = """
<section id="wf" class="section">
  <p class="kicker">Where WorldFirst fits</p>
  <h2 class="section-title">The brand is the rail, not the headline.</h2>
  <p class="lede">Every angle on this page is, underneath, a China-to-Malaysia import. The seller who acts on any of them has to source from China and pay a Chinese supplier. That payment is WorldFirst.</p>
  <p>So the content does not need to be about WorldFirst to work for WorldFirst. It earns the audience by being genuinely useful about what to sell, what it costs, and where to buy. The product sits underneath, in the call to action and the natural moments, never the opening line. Value first, brand last.</p>
  <p>The worry behind the first attempt, that a payments company cannot own content about products and profit, was the wrong worry. WorldFirst is the cross-border import company. Intelligence about where the Malaysian import opportunity actually is sits dead-center in its lane. That is more natural ground for the brand than emotional sourcing stories ever were.</p>
  <p>So the angle gets chosen on what the audience wants. The WorldFirst connection follows from it. It does not lead.</p>
</section>
"""

FOOTER = """
<footer class="site-footer">
  <p>WorldFirst · Internal · Project Canopy · Foundation exploration, recut · <a href="#" id="lock">lock device</a></p>
</footer>
"""

INNER = HERO + HOW + O1 + O2 + O3 + O4 + O5 + COMPARE + WHEREWF + FOOTER

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
.page-header{padding-bottom:36px;border-bottom:1px solid var(--line);margin-bottom:10px;}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:20px;}
.page-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:62px;line-height:1.0;letter-spacing:-.03em;margin-bottom:16px;}
.page-byline{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:21px;color:var(--ink-soft);max-width:640px;margin-bottom:24px;}
.addendum-link{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--ink-mute);}
.addendum-link a{color:var(--ink-mute);}
.section{padding-top:50px;padding-bottom:28px;scroll-margin-top:24px;border-top:1px solid var(--line);}
.section:first-of-type{border-top:none;}
.kicker{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:14px;}
.section-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:34px;letter-spacing:-.018em;line-height:1.16;margin-bottom:18px;max-width:720px;}
.section p{margin-bottom:14px;max-width:700px;}
.section p strong{color:var(--ink);}
.lede{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:19px;color:var(--ink-soft);margin-bottom:16px;max-width:680px;line-height:1.5;}
.method-note{font-size:13px;color:var(--ink-mute);border-left:2px solid var(--line);padding-left:14px;}
.method-note strong{color:var(--ink-soft);}
.block-lbl{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:var(--wf-pink);margin:26px 0 4px;}
/* mock feed */
.feed{display:flex;flex-direction:column;gap:10px;margin:12px 0 6px;max-width:620px;}
.art{border:1px solid var(--line);border-radius:5px;padding:13px 15px;background:#fff;}
.art-lbl{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-mute);margin-bottom:7px!important;display:flex;align-items:center;gap:7px;}
.art-txt{font-size:14.5px;line-height:1.5;margin:0!important;max-width:none!important;}
.art-youtube .art-txt{font-weight:600;}
.art-short .art-txt{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:16.5px;color:var(--ink);}
.art-carousel .art-txt{font-weight:500;}
.art-post .art-txt{color:var(--ink-soft);}
.play{width:0;height:0;border-style:solid;border-width:4.5px 0 4.5px 7.5px;border-color:transparent transparent transparent var(--wf-pink);display:inline-block;}
/* scorecard */
.score{margin:12px 0 4px;max-width:380px;}
.score-row{display:grid;grid-template-columns:128px 1fr;gap:14px;align-items:center;padding:5px 0;}
.score-lbl{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--ink-soft);}
.dots{display:flex;gap:5px;}
.dot{width:9px;height:9px;border-radius:50%;border:1px solid var(--wf-pink);box-sizing:border-box;}
.dot-on{background:var(--wf-pink);}
/* table */
.table-wrap{overflow-x:auto;margin:18px 0 16px;}
.rtbl{width:100%;border-collapse:collapse;font-size:13.5px;}
.rtbl th,.rtbl td{padding:11px 14px;text-align:left;border-bottom:1px solid var(--line);}
.rtbl th{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.07em;color:var(--ink);border-bottom:1px solid var(--ink);}
.rtbl td{color:var(--ink-soft);}
.rtbl tbody tr:hover{background:var(--line-soft);}
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
<title>Project Canopy · Foundation Exploration</title>
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
    <h1 class="gate-title">Project Canopy</h1>
    <p class="gate-subtitle">Where the content starts.</p>
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
  wrap.innerHTML=`<aside class="toc"><p class="toc-lbl">Angles</p><ul class="toc-list">
    <li><a href="#how">How to read this</a></li>
    <li><a href="#a1">01 · The Profit Map</a></li>
    <li><a href="#a2">02 · The Price Breakdown</a></li>
    <li><a href="#a3">03 · The Sourcing Playbook</a></li>
    <li><a href="#a4">04 · The Trend Radar</a></li>
    <li><a href="#a5">05 · The Proof</a></li>
    <li><a href="#compare">Side by side</a></li>
    <li><a href="#wf">Where WorldFirst fits</a></li>
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
(ROOT / "angles.html").write_text(HTML, encoding="utf-8")
print(f"Wrote angles.html ({len(HTML):,} bytes; {len(INNER):,} inner)")
