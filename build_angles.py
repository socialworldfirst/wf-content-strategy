#!/usr/bin/env python3
"""
Project Canopy — Foundation Exploration.
Five candidate angles for the Sourcing Tree, each shown as the audience would see it.
Exploration artifact, not a decision. Encrypts inner content with 'wf'.
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

def option(num, sid, name, question, what, feed_items, why, score_rows, catch):
    return f"""
<section id="{sid}" class="section">
  <p class="kicker">Angle {num}</p>
  <h2 class="section-title">{name}</h2>
  <p class="lede">&ldquo;{question}&rdquo;</p>
  <p>{what}</p>
  <p class="block-lbl">What a Malaysian importer would see</p>
  {feed(feed_items)}
  <p class="block-lbl">Why they click, or don't</p>
  <p>{why}</p>
  <p class="block-lbl">The read</p>
  {scorecard(score_rows)}
  <p class="catch">{catch}</p>
</section>
"""

# ----------------------------------------------------------------------------
# Content
# ----------------------------------------------------------------------------
HERO = """
<header class="page-header">
  <p class="eyebrow">Project Canopy · Foundation Exploration</p>
  <h1 class="page-title">Where the content starts.</h1>
  <p class="page-byline">Five candidate angles for the Sourcing Tree, and how each one looks to a Malaysian importer. An exploration, not a decision.</p>
  <p class="addendum-link"><a href="canopy.html">&larr; Project Canopy</a> · Audience: ~600,000 Malaysian sellers who look local and source from China</p>
</header>
"""

HOW = """
<section id="how" class="section">
  <p class="kicker">How to read this</p>
  <h2 class="section-title">The foundation is the one decision that changes every other one.</h2>
  <p class="lede">The trunk is a single heavy research effort. Every branch of content derives from it. Choose the angle wrong and twenty pieces are wrong.</p>
  <p>So the angle is not picked by what is convenient, or by what we have built before. It is picked by what the audience actually cares about and will actually watch. This page puts five candidate angles side by side and shows, for each, the content a Malaysian importer would really see in their feed.</p>
  <p>Everything below is judged against five tests. The first is the one that matters most.</p>
  <ul class="tests">
    <li><strong>Click-to-watch.</strong> Would the audience genuinely stop and watch this. Not &ldquo;should they&rdquo;.</li>
    <li><strong>Evergreen.</strong> The research base does not rot in three months.</li>
    <li><strong>Ownable.</strong> WorldFirst can credibly research and own it, through the newsroom model, with no China desk we do not have.</li>
    <li><strong>Watchable.</strong> Story-rich, not chart-rich. Charts do not get watched.</li>
    <li><strong>Brand link.</strong> WorldFirst connects to it honestly, never as a pitch.</li>
  </ul>
  <p class="method-note"><strong>Status.</strong> No angle has been chosen. All five can become trunks over time. The open question is only which one the Sourcing Tree starts with.</p>
</section>
"""

O1 = option(
  "01", "a1", "The Sourcing Reality",
  "Is this going to blow up in my face, and who is actually making it work?",
  "The real story of sourcing from China, told by the Malaysian sellers who lived it. How it breaks, how the survivors avoid it, and the short list of learnable decisions in between. The burn and the win, side by side.",
  [("youtube","YouTube title","I Lost RM38,000 to a 1688 Supplier. Here's Every Mistake I Made."),
   ("short","Short video hook","Your sample arrived perfect. That is exactly when you should worry."),
   ("carousel","Carousel headline","4 ways a China supplier takes your money, and the 10-minute check that stops all four."),
   ("post","Feed post","She had ordered from the same factory six times. The seventh order never shipped. Here is what changed between order six and seven.")],
  "Fear and recognition at the same time. Every importer in Malaysia has a near-miss story, or knows someone who has the real one. This is people exactly like them, and disaster plus survival is the most watchable material there is. They do not just click it, they send it to the other sellers in their group chat.",
  [("Click-to-watch",3),("Evergreen",3),("Ownable",3),("Watchable",3),("Brand link",2)],
  "The brand link is real but soft: WorldFirst is how you do not become the story, never the headline. For a trust-led foundation, that restraint is the point, not a weakness."
)

O2 = option(
  "02", "a2", "The Real Numbers",
  "Am I actually making money, or am I fooling myself?",
  "The honest economics of importing. What it truly costs to land a product from China, what a Malaysian seller truly earns, and which costs quietly disappear before anyone counts them.",
  [("youtube","YouTube title","The Real Cost of a RM10 Product from 1688 (Full Breakdown)."),
   ("short","Short video hook","You think your margin is 40%. Let me show you where a third of it goes."),
   ("carousel","Carousel headline","7 costs between the 1688 price and your shelf. Most sellers count three."),
   ("post","Feed post","A RM12 landed cost is not a RM12 product. Here is the other RM8 nobody printed on the invoice.")],
  "This is the survival question, the profit-and-loss every serious seller is privately unsure about. High intent. The catch is form: it is breakdowns and numbers, closer to a lesson than a story, so it gets read more than it gets watched.",
  [("Click-to-watch",2),("Evergreen",2),("Ownable",3),("Watchable",2),("Brand link",3)],
  "Strongest product link of the five, because WorldFirst is one of the line items. That is also the trap: this is the angle that most easily turns into a sales deck."
)

O3 = option(
  "03", "a3", "The Insider's China",
  "What is my supplier actually thinking, and what do I not know?",
  "The supplier side, decoded. How Chinese factories, trading companies and 1688 actually work, explained for the Malaysian buyer who only ever sees the chat window.",
  [("youtube","YouTube title","What Your 1688 Supplier Means When They Say 'No Problem'."),
   ("short","Short video hook","That factory you are chatting with? Here is how to tell if it is actually a middleman."),
   ("carousel","Carousel headline","How a Chinese supplier decides your price. It is not the number on the listing."),
   ("post","Feed post","Factory or trading company? Your supplier will never tell you straight. These three questions will.")],
  "The China side is a black box, and the buyer badly wants it opened. This is the most genuinely insider of the five, and it sits cleanly inside the sourcing-insider positioning.",
  [("Click-to-watch",3),("Evergreen",3),("Ownable",2),("Watchable",2),("Brand link",1)],
  "Weakest brand link: it is pure authority content with no natural home for the product. It also overlaps the existing Global Sourcing Guide videos on YouTube, so it risks repeating work instead of compounding it."
)

O4 = option(
  "04", "a4", "The Shelf War",
  "Chinese sellers are undercutting me on my own marketplace. How do I survive that?",
  "The Malaysian seller against the Chinese cross-border seller, on the same Shopee shelf. Why the local sellers have lost ground for a decade, and what the ones still standing do differently.",
  [("youtube","YouTube title","Why the Chinese Seller Next to You Charges RM5 Less, and Still Wins."),
   ("short","Short video hook","Local sellers held 65% of this market in 2015. Today it is 40%. Here is where it went."),
   ("carousel","Carousel headline","5 advantages a cross-border seller has over you. You can close three of them."),
   ("post","Feed post","You are not competing with a shop. You are competing with the supply chain behind it. Different fight, different playbook.")],
  "Identity and fear together. This is their fight and it is personal. It travels fast inside seller communities because it names something every local seller already feels but rarely sees explained.",
  [("Click-to-watch",3),("Evergreen",2),("Ownable",2),("Watchable",3),("Brand link",2)],
  "Competitive dynamics shift, so parts of this date faster than the other angles. It works better as a recurring angle on top of a foundation than as the permanent foundation itself."
)

O5 = option(
  "05", "a5", "What Actually Sells",
  "What should I sell, and what is working right now?",
  "The product reality. Which categories actually move in Malaysia, what is saturated, and what a genuinely winning product looks like before you commit money to it.",
  [("youtube","YouTube title","5 Product Categories Quietly Dying on Shopee Malaysia."),
   ("short","Short video hook","Everyone is selling this. That is exactly why you should not."),
   ("carousel","Carousel headline","How to read a 1688 listing's order volume before you commit a cent."),
   ("post","Feed post","A winning product is not the one with the best margin. It is the one you can restock in nine days.")],
  "This is the number one obsession of every seller alive. Raw click is the highest of all five angles, by a clear distance. It is included here precisely so the trade-off is visible on the page.",
  [("Click-to-watch",3),("Evergreen",1),("Ownable",1),("Watchable",3),("Brand link",1)],
  "We cannot own it. A payments company publishing product picks is off-key, the space is saturated with dedicated product-research creators who will always beat us, and the content dates within months. Highest click, lowest everything else."
)

def crow(name, scores):
    cells = "".join(f"<td>{dots(n)}</td>" for n in scores)
    return f"<tr><td><strong>{name}</strong></td>{cells}</tr>"

COMPARE = f"""
<section id="compare" class="section">
  <p class="kicker">The five together</p>
  <h2 class="section-title">No angle wins every test.</h2>
  <p class="lede">Read down the columns, not just across the rows. The trade-offs are the whole point.</p>
  <div class="table-wrap">
    <table class="rtbl">
      <thead>
        <tr><th>Angle</th><th>Click</th><th>Evergreen</th><th>Ownable</th><th>Watchable</th><th>Brand link</th></tr>
      </thead>
      <tbody>
        {crow("01 The Sourcing Reality",[3,3,3,3,2])}
        {crow("02 The Real Numbers",[2,2,3,2,3])}
        {crow("03 The Insider's China",[3,3,2,2,1])}
        {crow("04 The Shelf War",[3,2,2,3,2])}
        {crow("05 What Actually Sells",[3,1,1,3,1])}
      </tbody>
    </table>
  </div>
  <p>Angle five wins raw attention and loses everything else: we cannot own it or sustain it. Angle three and angle four are strong, but each carries a structural catch, an overlap in one case and a shelf-life in the other. Angle two connects hardest to the product, which is exactly why it is the easiest to get wrong. Angle one is the only one that holds up across all five tests at once.</p>
  <p>That is an observation, not a decision. All five can become trunks in time. The only question on the table is which angle the Sourcing Tree starts with, and that call is yours.</p>
</section>
"""

FOOTER = """
<footer class="site-footer">
  <p>WorldFirst · Internal · Project Canopy · Foundation exploration · <a href="#" id="lock">lock device</a></p>
</footer>
"""

INNER = HERO + HOW + O1 + O2 + O3 + O4 + O5 + COMPARE + FOOTER

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
.tests{margin:14px 0 0 0;padding:0;list-style:none;max-width:700px;}
.tests li{padding:10px 0;border-bottom:1px solid var(--line-soft);font-size:14px;color:var(--ink-soft);}
.tests li:last-child{border-bottom:none;}
.tests li strong{color:var(--ink);}
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
.catch{font-size:13px;color:var(--ink-soft);border-left:2px solid var(--wf-pink);padding-left:13px;margin-top:14px;max-width:640px;}
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
    <li><a href="#a1">01 · The Sourcing Reality</a></li>
    <li><a href="#a2">02 · The Real Numbers</a></li>
    <li><a href="#a3">03 · The Insider's China</a></li>
    <li><a href="#a4">04 · The Shelf War</a></li>
    <li><a href="#a5">05 · What Actually Sells</a></li>
    <li><a href="#compare">The five together</a></li>
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
