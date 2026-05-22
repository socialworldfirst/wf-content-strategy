#!/usr/bin/env python3
"""
Project Canopy — Audience Research.
Evidence brief: what value-driven content Malaysian China-importers actually
want. Built from three parallel research streams. Encrypts inner with 'wf'.
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

def dots(n):
    return '<span class="dots">' + "".join(
        f'<span class="dot {"dot-on" if i < n else ""}"></span>' for i in range(3)) + '</span>'

def rank(n, title, sig, evidence):
    return f"""<div class="rank">
  <div class="rank-head"><span class="rank-n">{n}</span><span class="rank-ttl">{title}</span>{dots(sig)}</div>
  <p class="rank-ev">{evidence}</p>
</div>"""

# ----------------------------------------------------------------------------
# Content
# ----------------------------------------------------------------------------
HERO = """
<header class="page-header">
  <p class="eyebrow">Project Canopy · Audience Research</p>
  <h1 class="page-title">What the audience actually wants.</h1>
  <p class="page-byline">Three research streams into Malaysian China-importers and the wider source-from-China-and-sell audience. The evidence, not the guess.</p>
  <p class="addendum-link"><a href="angles.html">&larr; Angle exploration</a> · The evidence base under the angle decision</p>
</header>
"""

METHOD = """
<section id="method" class="section">
  <p class="kicker">How this was researched</p>
  <h2 class="section-title">Three streams, looking for evidence, not for what we hoped to find.</h2>
  <p class="lede">The earlier angles were guesses. This is not. Three parallel research efforts went looking for proof of what this audience genuinely seeks out, watches, asks, and rewards.</p>
  <ul class="pts">
    <li><strong>Stream 1 — YouTube and the creator landscape.</strong> Which channels and videos actually pull views, and which topics and formats win.</li>
    <li><strong>Stream 2 — Reddit and the global English seller forums.</strong> The questions asked over and over, and the kind of post the communities reward.</li>
    <li><strong>Stream 3 — Malaysia, specifically.</strong> Lowyat.NET, Malaysian creators, Malay and English search signals, and Facebook seller groups.</li>
  </ul>
  <p class="method-note"><strong>What the research could and could not reach.</strong> Reddit blocked direct access, so subreddit sizes are not cited and thread vote counts were not pulled. The thematic findings are corroborated across three or more independent sources each. Creator view and subscriber counts are used only where verifiable and labelled as approximate. Google Trends volumes were inferred from the density of ranking content, not pulled as exact figures. Nothing here is invented. Where the evidence is thin, the brief says so.</p>
</section>
"""

DEMAND = f"""
<section id="demand" class="section">
  <p class="kicker">What they want most</p>
  <h2 class="section-title">The same five demands surfaced across every stream.</h2>
  <p class="lede">Ranked by how strong and how consistent the signal was. Signal: {dots(3)} strongest and most consistent &nbsp; {dots(2)} strong &nbsp; {dots(1)} present.</p>
  {rank("1","Paying suppliers safely, and not getting scammed",3,
    "The strongest and most consistent signal in the whole research. On the global seller forums it is the single most repeated theme: the canonical story, told again and again on r/Alibaba, of a supplier quoting a good price, asking for a roughly 30% deposit by wire to a personal account, then disappearing. Sellers openly distrust the &ldquo;Gold Supplier&rdquo;, &ldquo;Verified&rdquo; and &ldquo;Trade Assurance&rdquo; badges as not enough. On Malaysia's Lowyat.NET, the dominant unmet need is trust and risk, not how to find products: one thread, &ldquo;Wa.... do business with China so scary&rdquo;, drew about 50 posts in a single day on supplier fraud, trademark theft and the sample-versus-bulk quality gap. This is the audience's deepest anxiety. It is also exactly what WorldFirst does.")}
  {rank("2","What to sell",2,
    "A strong and universal demand. Beginner-question FAQs built from real seller questions lead with &ldquo;where do I find products&rdquo;. On r/Flipping the defining recurring questions are literally &ldquo;what should I flip&rdquo; and &ldquo;how do I know what sells&rdquo;. But it is also the most saturated lane in the niche: the recurring complaint is that &ldquo;everyone's selling the same TikTok trending products with the same ad angles&rdquo;. And in the Malaysia stream specifically, it surfaced behind supplier trust. It is genuinely wanted. It is also the most crowded ground there is.")}
  {rank("3","The real profit math",2,
    "Sellers consistently hit the gap between simple math and reality. The line quoted across multiple sources: &ldquo;I'm doing $10K in monthly revenue but only keeping $800 after all expenses.&rdquo; What blindsides them is the stack of costs nobody put on the invoice: ad spend, payment-processing fees, returns, chargebacks, lost packages, and currency conversion. They do not want a theory of costs. They want the true number on a real product.")}
  {rank("4","Getting it here: shipping, logistics, forwarders",2,
    "&ldquo;Reddit hates slow shipping&rdquo; turns up almost word for word across guides. In Malaysia the need is sharper and more concrete: Lowyat threads trade forwarder mechanics and name specific services, and &ldquo;how to find a shipping agent&rdquo; is one of the three things Malaysian sellers most search for.")}
  {rank("5","Where do I even start",1,
    "Beginner overwhelm is real, but lower-frequency than the four above. New sellers want one clear first-step sequence rather than a pile of tactics. It is a present demand, not a defining one.")}
</section>
"""

FORM = """
<section id="form" class="section">
  <p class="kicker">What form the value takes</p>
  <h2 class="section-title">How the value is delivered matters as much as the topic.</h2>
  <p class="lede">This is the direct answer to the question. The value that drives this audience is risk removed or uncertainty resolved, proven with real numbers and real steps.</p>
  <p class="block-lbl">What wins</p>
  <ul class="pts">
    <li><strong>Concrete and proof-based.</strong> The posts that earn a &ldquo;this is gold&rdquo; reaction on the forums are specific and numbers-backed: real supplier-vetting checklists, real profit breakdowns, scam case studies that show the exact mechanics of the fraud.</li>
    <li><strong>&ldquo;I tried it&rdquo; proof.</strong> On YouTube the biggest-pulling format is the realistic challenge. One large ecommerce channel's two most-viewed videos, at roughly 2.7 million and 1.5 million views, are both &ldquo;I tried this with this budget, here is what really happened&rdquo;.</li>
    <li><strong>The definitive walkthrough.</strong> The highest and most durable floor belongs to complete step-by-step tutorials. One channel's top four videos, roughly 1 million down to 600,000 views, are all variations of a single full beginner course. Evergreen.</li>
    <li><strong>Income proof and case studies.</strong> Audiences want to watch a normal person actually do it, with the figures shown on screen.</li>
  </ul>
  <p class="block-lbl">What gets punished</p>
  <ul class="pts">
    <li><strong>Hype, promotion, get-rich-quick.</strong> The communities actively downvote anything vague, anything that smells like an ad, and anything that promises an easy win. The moment content tips into a pitch, the audience leaves.</li>
  </ul>
</section>
"""

GAP = """
<section id="gap" class="section">
  <p class="kicker">The open lane</p>
  <h2 class="section-title">Nobody large owns sourcing as the subject.</h2>
  <p class="lede">One finding is a straight strategic opening.</p>
  <p>Dedicated China-sourcing education is an underserved niche, not a saturated one. The channels purely about sourcing are tiny, a few hundred to a couple of thousand subscribers. The large audiences sit inside generalist make-money-online channels, roughly 600,000 to 1.3 million subscribers, where sourcing from China is one chapter of a much bigger story and never the focus.</p>
  <p>For a company whose entire business is the China-to-elsewhere supply line, that is open ground. WorldFirst would not be entering a crowded room. It would be the first to treat sourcing as the whole subject rather than a side note.</p>
</section>
"""

MALAYSIA = """
<section id="malaysia" class="section">
  <p class="kicker">Malaysia, specifically</p>
  <h2 class="section-title">Four local specifics that change how the content is made.</h2>
  <p class="lede">The global evidence sets the topics. The Malaysian evidence sets the execution.</p>
  <ul class="pts">
    <li><strong>The platform is 1688, not Alibaba.</strong> Malaysian sellers name 1688 as the sourcing platform, and &ldquo;1688&rdquo; is a genuine standalone Malaysian search trend. The content should speak 1688, not a generic &ldquo;Alibaba&rdquo;.</li>
    <li><strong>English and Malay, co-primary.</strong> Demand is strong in both, and Malay is arguably the larger and less-served search pool: Malay tutorial content competes hard on terms like &ldquo;cara import barang dari China&rdquo; and &ldquo;cara jual di Shopee&rdquo;. Mandarin is a likely third track given Malaysia's Chinese-Malaysian seller base, but the research could not confirm specific Malaysian Mandarin creators, so treat it as unverified for now.</li>
    <li><strong>The audience is on TikTok and Facebook, not mainly YouTube.</strong> For the Malaysian seller segment, TikTok carries equal or greater weight than YouTube. The community layer is Facebook groups, one &ldquo;borong China&rdquo; page alone has about 85,000 likes, and the Lowyat.NET forums.</li>
    <li><strong>The format already exists, without an owner.</strong> Cikgu Shopee teaches Shopee selling in Malay around four-figure-income framing; Bryan Low's viral &ldquo;9 steps to make RM100k&rdquo; names 1688 directly. The audience and the formats are proven. Nobody is serving them with genuine, trusted authority.</li>
  </ul>
</section>
"""

MEANS = """
<section id="means" class="section">
  <p class="kicker">What this means</p>
  <h2 class="section-title">The research does not pick the angle. It sharpens the question.</h2>
  <p class="lede">It rules things in and out, and it points clearly at one match.</p>
  <ul class="pts">
    <li><strong>It confirms the core instinct.</strong> The audience wants practical, value-driven content and actively punishes hype and brand-talk. Value, proven concretely, is the whole game.</li>
    <li><strong>It refines &ldquo;what to sell&rdquo;.</strong> That demand is real and strong, but it is the most saturated lane in the niche, and in Malaysia it ranked behind supplier trust. Building the whole foundation on it alone would mean starting on the most crowded ground and skipping the audience's deepest anxiety.</li>
    <li><strong>It surfaces the strongest match.</strong> The number one evidenced demand, paying suppliers safely and not getting scammed, is precisely what WorldFirst does: verified supplier payments, safe transfers to China. The audience's deepest need and the company's actual product are the same thing. That alignment is rare and should not be wasted.</li>
    <li><strong>It sets the non-negotiable.</strong> Whatever the angle, the value must arrive as concrete checklists, real numbers and proven steps. The moment it becomes a pitch, the evidence says the audience is gone.</li>
  </ul>
  <p class="method-note"><strong>Next step.</strong> Re-derive the Sourcing Tree angles from this evidence, with the demand ranking and the form rules as the brief. Not done on this page. This page is the evidence that decision now stands on.</p>
</section>
"""

SOURCES = """
<section id="sources" class="section">
  <p class="kicker">Sources</p>
  <h2 class="section-title">Where the evidence came from.</h2>
  <p>Stream 1 drew on YouTube channel pages and vidIQ analytics for verified view and subscriber figures. Streams 2 and 3 drew on the sources below, each finding corroborated across several of them.</p>
  <ul class="src">
    <li><a href="https://painonsocial.com/blog/dropshipping-challenges-reddit">7 Biggest Dropshipping Challenges on Reddit — PainOnSocial</a></li>
    <li><a href="https://appscenic.com/blog/popular-questions-dropshipping-faq/">50 Most Popular Questions About Dropshipping — AppScenic</a></li>
    <li><a href="https://www.dropified.com/blog/uncover-success-with-our-ultimate-dropshipping-reddit-guide/">The Ultimate Reddit Guide for Dropshipping — Dropified</a></li>
    <li><a href="https://yakkyofy.com/is-alibaba-legit/">Is Alibaba Legit? Guide to Avoiding Scams — Yakkyofy</a></li>
    <li><a href="https://doctorecomm.com/selling-or-starting-your-ecommerce-brand-what-reddit-gets-right-and-what-it-gets-dead-wrong/">What Reddit Gets Right and Wrong About Selling — Doctor Ecomm</a></li>
    <li><a href="https://www.bigseller.com/blog/articleDetails/3447/1688-sourcing-guide.htm">1688 Sourcing Guide for E-Commerce Sellers in Malaysia — BigSeller</a></li>
    <li><a href="https://forum.lowyat.net/topic/5542898/all">&ldquo;Wa.... do business with China so scary&rdquo; — Lowyat.NET</a></li>
    <li><a href="https://forum.lowyat.net/topic/4459212/all">e-Marketplace Sellers (Lazada, 11Street, Shopee) — Lowyat.NET</a></li>
    <li><a href="https://forum.lowyat.net/topic/5333686">Buying Item From China — Lowyat.NET</a></li>
    <li><a href="https://cikgushopee.com/belajar-shopee/">Cikgu Shopee — Belajar Shopee</a></li>
    <li><a href="https://www.tiktok.com/@bryanlowwww/video/7242898011217579271">Bryan Low — 9 Steps to make RM100k (TikTok)</a></li>
    <li><a href="https://www.facebook.com/BorongChinaServices/">Borong China Services &amp; Trading — Facebook</a></li>
  </ul>
</section>
"""

FOOTER = """
<footer class="site-footer">
  <p>WorldFirst · Internal · Project Canopy · Audience research · <a href="#" id="lock">lock device</a></p>
</footer>
"""

INNER = HERO + METHOD + DEMAND + FORM + GAP + MALAYSIA + MEANS + SOURCES + FOOTER

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
.page-byline{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:21px;color:var(--ink-soft);max-width:660px;margin-bottom:24px;}
.addendum-link{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--ink-mute);}
.addendum-link a{color:var(--ink-mute);}
.section{padding-top:50px;padding-bottom:28px;scroll-margin-top:24px;border-top:1px solid var(--line);}
.section:first-of-type{border-top:none;}
.kicker{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:14px;}
.section-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:34px;letter-spacing:-.018em;line-height:1.16;margin-bottom:18px;max-width:730px;}
.section p{margin-bottom:14px;max-width:710px;}
.section p strong{color:var(--ink);}
.lede{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:19px;color:var(--ink-soft);margin-bottom:16px;max-width:690px;line-height:1.5;}
.method-note{font-size:13px;color:var(--ink-mute);border-left:2px solid var(--line);padding-left:14px;}
.method-note strong{color:var(--ink-soft);}
.block-lbl{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:var(--wf-pink);margin:24px 0 4px;}
.pts{margin:14px 0 0 0;padding:0;list-style:none;max-width:710px;}
.pts li{padding:11px 0;border-bottom:1px solid var(--line-soft);font-size:14px;color:var(--ink-soft);}
.pts li:last-child{border-bottom:none;}
.pts li strong{color:var(--ink);}
/* demand ranks */
.rank{padding:15px 0;border-bottom:1px solid var(--line-soft);}
.rank:last-child{border-bottom:none;}
.rank-head{display:flex;align-items:center;gap:13px;margin-bottom:8px;flex-wrap:wrap;}
.rank-n{font-family:'Fraunces',Georgia,serif;font-size:26px;color:var(--wf-pink);line-height:1;}
.rank-ttl{font-family:'Fraunces',Georgia,serif;font-size:21px;letter-spacing:-.01em;}
.rank-head .dots{margin-left:auto;}
.rank-ev{font-size:14px;color:var(--ink-soft);margin:0!important;max-width:700px;}
.dots{display:flex;gap:5px;}
.dot{width:9px;height:9px;border-radius:50%;border:1px solid var(--wf-pink);box-sizing:border-box;}
.dot-on{background:var(--wf-pink);}
/* sources */
.src{list-style:none;margin:14px 0 0;padding:0;max-width:710px;}
.src li{padding:8px 0;border-bottom:1px solid var(--line-soft);font-size:13.5px;}
.src li:last-child{border-bottom:none;}
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
<title>Project Canopy · Audience Research</title>
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
    <p class="gate-subtitle">What the audience wants.</p>
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
    <li><a href="#method">How this was researched</a></li>
    <li><a href="#demand">What they want most</a></li>
    <li><a href="#form">What form the value takes</a></li>
    <li><a href="#gap">The open lane</a></li>
    <li><a href="#malaysia">Malaysia, specifically</a></li>
    <li><a href="#means">What this means</a></li>
    <li><a href="#sources">Sources</a></li>
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
(ROOT / "audience-research.html").write_text(HTML, encoding="utf-8")
print(f"Wrote audience-research.html ({len(HTML):,} bytes; {len(INNER):,} inner)")
