#!/usr/bin/env python3
"""
Project Canopy — WorldFirst content system operating plan.
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
# Content
# ----------------------------------------------------------------------------
HERO = """
<header class="page-header">
  <p class="eyebrow">WorldFirst · Project Canopy · Operating Plan</p>
  <h1 class="page-title">Project Canopy.</h1>
  <p class="page-byline">The content system, and how we move forward — one core, a canopy of content, localised market by market.</p>
  <p class="addendum-link"><a href="insider.html">The Insider direction</a> · <a href="landscape.html">Content landscape</a> · <a href="importer-index.html">The Importer Index</a></p>
</header>
"""

SYSTEM = """
<section id="system" class="section">
  <p class="kicker">01 · The system</p>
  <h2 class="section-title">Canopy is a content system, not a content calendar.</h2>
  <p class="lede">One rule underneath everything: build content as a tree, not as standalone posts.</p>
  <p>A <strong>trunk</strong> — one piece of real research, done rarely. <strong>Branches</strong> — a bounded set of derivative formats cut from that trunk. <strong>Leaves</strong> — each branch localised per market. One research effort feeds roughly twenty derivative pieces across every format, then localises into each market.</p>
  <p>The flagship is <strong>capped</strong> — a ~15-page mini-report, never a 100-page monument. That is the China Sourcing Map lesson: a flagship is the top of a ladder, not a tomb nobody reads. Canopy is the discipline that makes the content diversified, localisable and feasible at the same time — and feasible is the word that matters, because production capacity is the real constraint.</p>
</section>
"""

TREES = """
<section id="trees" class="section">
  <p class="kicker">02 · Two trees</p>
  <h2 class="section-title">Three markets, but two trees.</h2>
  <p class="lede">The three target markets are not three versions of one tree. They split into two — because they are two genuinely different audiences.</p>
  <div class="two-trees">
    <article class="tt">
      <p class="tt-tag">Tree 01 · Sourcing</p>
      <h3>The Sourcing Tree</h3>
      <p class="tt-markets">Malaysia + Thailand</p>
      <p><strong>Audience:</strong> importers paying Chinese suppliers — outbound. They lose money on FX and agent fees.</p>
      <p><strong>Trunk:</strong> The Importer Index — what importers told us about sourcing, trust and the cost gap.</p>
    </article>
    <article class="tt">
      <p class="tt-tag">Tree 02 · Freelancer</p>
      <h3>The Freelancer Tree</h3>
      <p class="tt-markets">Vietnam</p>
      <p><strong>Audience:</strong> freelancers collecting international income — inbound. They lose money to PayPal, Payoneer and PingPong fees.</p>
      <p><strong>Trunk:</strong> a freelancer fee-comparison index — what VN freelancers actually lose, and to whom.</p>
    </article>
  </div>
  <p>Same Canopy system, different trunks. The mistake to avoid is forcing Vietnam onto the importer trunk — the freelancer is not an importer, and the content would ring false.</p>
</section>
"""

ANATOMY = """
<section id="anatomy" class="section">
  <p class="kicker">03 · Anatomy of a tree</p>
  <h2 class="section-title">Trunk, branches, leaves.</h2>

  <div class="tree">
    <div class="tree-tier">
      <p class="tier-lbl">Trunk</p>
      <div class="tier-row"><div class="tree-box tree-box-trunk">One research effort · capped ~15pp · e.g. the Importer Index</div></div>
    </div>
    <p class="tree-down">↓ &nbsp; cut into, not re-researched</p>
    <div class="tree-tier">
      <p class="tier-lbl">Branches — the bounded kit (~20 pieces)</p>
      <div class="tier-row">
        <div class="tree-box">Mini-report ~15pp</div>
        <div class="tree-box">Carousel</div>
        <div class="tree-box">6× stat cards</div>
        <div class="tree-box">4× short videos</div>
        <div class="tree-box">8× text posts</div>
      </div>
    </div>
    <p class="tree-down">↓ &nbsp; localised — the cheap end, per market</p>
    <div class="tree-tier">
      <p class="tier-lbl">Leaves — per-market editions</p>
      <div class="tier-row">
        <div class="tree-box">Malaysia edition</div>
        <div class="tree-box">Thailand edition</div>
        <div class="tree-box tree-box-mute">(Vietnam = its own tree)</div>
      </div>
    </div>
  </div>

  <h3 class="sub">The trunk</h3>
  <p>One research effort, done a few times a year. Built from three real-input mechanisms — a <strong>community survey</strong>, <strong>borrowed insiders</strong> (real agents, forwarders and freelancers on camera), and <strong>synthesis</strong> of the scattered landscape (1688, the forums, platform changes). Capped at ~15 pages. All the rigorous sourcing happens here, once — and every branch and leaf inherits its credibility.</p>

  <h3 class="sub">The branches — the depth ladder</h3>
  <p>A bounded kit cut from the trunk. Not new research — re-format. The ladder runs from authority at the top to reach at the bottom:</p>
  <div class="ladder">
    <div class="rung"><span class="rung-fmt">Mini-report (~15pp)</span><span class="rung-role">Authority — few readers, deepest trust, gets cited</span></div>
    <div class="rung"><span class="rung-fmt">Carousel</span><span class="rung-role">Considered — saved and forwarded importer-to-importer</span></div>
    <div class="rung"><span class="rung-fmt">Stat cards ×6</span><span class="rung-role">Screenshot-bait — the single most travelled format</span></div>
    <div class="rung"><span class="rung-fmt">Short videos ×4</span><span class="rung-role">Discovery — algorithmic reach to new audiences</span></div>
    <div class="rung"><span class="rung-fmt">Text posts ×8</span><span class="rung-role">Reach — highest volume, lowest cost</span></div>
  </div>

  <h3 class="sub">The leaves</h3>
  <p>Each branch localised per market — local tone, local examples, local language. The discipline: <strong>localise the cheap end, not the expensive trunk.</strong> Localising twenty light pieces is cheap and high-leverage; localising a 15-page report four ways is expensive and low-leverage. The research is done once, pan-market; every output is market-targeted.</p>
</section>
"""

TRUST = """
<section id="trust" class="section">
  <p class="kicker">04 · The trust model</p>
  <h2 class="section-title">AI is the processor — never the source.</h2>
  <p class="lede">Canopy's content cannot read as AI slop or carry a hallucination. Trust is the entire strategy — the content itself has to be trustworthy.</p>
  <p>Hallucination is a sourcing problem, not an AI problem. AI invents facts when it is asked to <em>be</em> the source; it is reliable when it <em>processes</em> facts that come from somewhere real. So the ground truth always comes from a real input:</p>
  <ul class="trust-list">
    <li><strong>Survey data</strong> — collected, not generated. If 500 importers answer, the aggregate is a fact. The trust-safest format.</li>
    <li><strong>Borrowed insiders</strong> — a real person on camera. You cannot hallucinate a primary witness.</li>
    <li><strong>Synthesis</strong> — the riskiest; needs tight source-citation and the most human checking.</li>
  </ul>
  <p>AI structures, drafts, charts and localises. A human verifies the synthesis against the source — a fast check, not an authoring job. And the armour against "this is just AI": proprietary inputs plus visible sourcing. Generic and unsourced reads as slop; proprietary and sourced reads as authority — whatever tool drafted it.</p>
</section>
"""

ROLLOUT = """
<section id="rollout" class="section">
  <p class="kicker">05 · The rollout</p>
  <h2 class="section-title">Region by region.</h2>
  <p class="lede">Each market is sequenced to its own real timeline — not a uniform launch.</p>

  <article class="region">
    <div class="region-head"><h3>Malaysia</h3><span class="region-when">The proving ground · now → July</span></div>
    <p>Cleanest fit: clear product-market fit (the hidden importers), the deep-dive research is done, and Joan's July onshore launch is a hard deadline. Build the first full tree here.</p>
    <ul>
      <li><strong>Trunk:</strong> the Importer Index, Malaysia edition — the hidden-importer FX-bleed and agent-fee cost gap.</li>
      <li><strong>Branches:</strong> the full ~20-piece kit.</li>
      <li><strong>Leaves:</strong> localise by language, not channel — English + Mandarin routed through existing global and Chinese channels; the Malay community via Malay KOLs.</li>
      <li><strong>Lead:</strong> Joan Poon. <strong>Why first:</strong> prove the whole system on MY before replicating.</li>
    </ul>
  </article>

  <article class="region">
    <div class="region-head"><h3>Vietnam</h3><span class="region-when">Lean parallel trunk · now</span></div>
    <p>Thao launches the freelancer segment end of May — too soon to wait for Malaysia. Vietnam gets its own small, fast trunk.</p>
    <ul>
      <li><strong>Trunk:</strong> a freelancer fee-comparison piece — what VN freelancers lose to PayPal / Payoneer / PingPong. Not a 15-page report; lean and fast.</li>
      <li><strong>Branches:</strong> the freelancers themselves are the branches — the "freelancer as micro-influencer" playbook is the distribution.</li>
      <li><strong>Lead:</strong> Thao. <strong>Why now:</strong> the launch is imminent; the content has to feed it, not follow it.</li>
    </ul>
  </article>

  <article class="region">
    <div class="region-head"><h3>Thailand</h3><span class="region-when">Built on the runway · fired at the July unlock</span></div>
    <p>Iris is deliberately holding heavy spend until the pay-to-Chinese-bank product lands (~July). Use the runway to build, so it is ready to fire at the unlock.</p>
    <ul>
      <li><strong>Trunk:</strong> the Importer Index, Thailand edition — Thai-language, supplier-payment focused (1688 + B2B sourcing, not collection), on a dedicated Thai Facebook page.</li>
      <li><strong>The bonus:</strong> Canopy directly solves Iris's real blocker — content cadence. One trunk → the branch kit = the content volume she is stuck on, from low production.</li>
      <li><strong>Lead:</strong> Iris Teo. <strong>Timing:</strong> build June, fire at the product unlock.</li>
    </ul>
  </article>
</section>
"""

TIMELINE = """
<section id="timeline" class="section">
  <p class="kicker">06 · The timeline</p>
  <h2 class="section-title">The phased roadmap.</h2>
  <div class="table-wrap">
    <table class="tl">
      <thead>
        <tr><th>Market</th><th>Now · late May</th><th>June</th><th>July</th><th>Aug+</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Malaysia</strong></td>
          <td>Trunk drafted — Importer Index MY edition</td>
          <td>Branch kit + localisation built</td>
          <td>Onshore launch — full tree live</td>
          <td>Recurring cadence</td>
        </tr>
        <tr>
          <td><strong>Vietnam</strong></td>
          <td>Lean freelancer trunk drafted, into Thao's launch</td>
          <td>Launch live · iterate on what travels</td>
          <td>Second freelancer trunk if July scales</td>
          <td>Recurring cadence</td>
        </tr>
        <tr>
          <td><strong>Thailand</strong></td>
          <td>Brief Iris</td>
          <td>Trunk built on the runway (Thai-language)</td>
          <td>Fire at the pay-to-Chinese-bank unlock</td>
          <td>Recurring cadence</td>
        </tr>
        <tr>
          <td><strong>The system</strong></td>
          <td>Survey-collection mechanism stood up</td>
          <td>Branch kit templated — so every future trunk slots in</td>
          <td>System proven on MY</td>
          <td>Scale to further markets</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
"""

ROLES = """
<section id="roles" class="section">
  <p class="kicker">07 · Automation &amp; delegation</p>
  <h2 class="section-title">Who does what.</h2>
  <p class="lede">The heavy production is rare. Most of the work is derivation and localisation — and most of that is automatable.</p>
  <div class="roles">
    <div class="role">
      <p class="role-who">Automated</p>
      <ul>
        <li>Survey collection — a standing, always-open form</li>
        <li>Landscape monitoring — 1688, forums, platform changes</li>
        <li>First-pass drafting, charting and localisation</li>
      </ul>
    </div>
    <div class="role">
      <p class="role-who">Claude</p>
      <ul>
        <li>Draft and build the trunks</li>
        <li>Cut the branch kits — all ~20 pieces per trunk</li>
        <li>Run the localisation passes</li>
        <li>Build the HTML artifacts</li>
      </ul>
    </div>
    <div class="role">
      <p class="role-who">Steven · supervises</p>
      <ul>
        <li>Approve each trunk — angle and outline</li>
        <li>Sign off local tone per market</li>
        <li>Hold the verification gate</li>
      </ul>
    </div>
    <div class="role">
      <p class="role-who">Regional leads</p>
      <ul>
        <li>Joan (MY) · Iris (TH) · Thao (VN)</li>
        <li>Local ground-truth and validation</li>
        <li>Operator / KOL relationships</li>
        <li>On-market distribution</li>
      </ul>
    </div>
  </div>
</section>
"""

NEXT = """
<section id="next" class="section">
  <p class="kicker">08 · Next moves</p>
  <h2 class="section-title">What happens first.</h2>
  <ol class="next">
    <li><strong>Lock the Malaysia trunk.</strong> Draft the Importer Index MY-edition angle and outline for Steven's sign-off — the first thing through the gate.</li>
    <li><strong>Template the branch kit, once.</strong> Spec the ~20-piece kit so every future trunk slots straight in — built once, reused for every market and every trunk after.</li>
    <li><strong>Draft the Vietnam lean trunk, in parallel.</strong> Fast freelancer fee-comparison piece, to feed Thao's end-May launch — can't wait on Malaysia.</li>
    <li><strong>Stand up survey collection.</strong> An always-open form so the next trunk's data starts flowing now, not when we need it.</li>
    <li><strong>Brief Thailand.</strong> Brief Iris, start the Thai trunk on the runway, time it to the July product unlock.</li>
  </ol>
  <p>Measurement stays as set: brand search is the North Star, geo-focused on one lead market so the lift is readable. The trunk is the authority engine; the branches and leaves are the reach. Steven supervises; Canopy runs.</p>
</section>
"""

FOOTER = """
<footer class="site-footer">
  <p>WorldFirst · Internal · Project Canopy · Operating Plan · May 2026 · <a href="#" id="lock">lock device</a></p>
</footer>
"""

INNER = HERO + SYSTEM + TREES + ANATOMY + TRUST + ROLLOUT + TIMELINE + ROLES + NEXT + FOOTER

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
.gate-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:50px;letter-spacing:-.02em;margin-bottom:14px;line-height:1.04;}
.gate-subtitle{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:18px;color:var(--ink-soft);margin-bottom:38px;}
#gate-form{display:flex;flex-direction:column;gap:10px;margin-bottom:12px;}
#gate-input{width:100%;padding:13px 16px;font-size:15px;font-family:'JetBrains Mono',monospace;border:1px solid var(--line);border-radius:3px;background:#fff;outline:none;}
#gate-input:focus{border-color:var(--wf-pink);}
#gate-btn{padding:13px 16px;font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.08em;background:var(--ink);color:#fff;border:none;border-radius:3px;cursor:pointer;}
#gate-btn:hover{background:var(--wf-pink);}
#gate-err{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--wf-pink);margin-top:6px;min-height:18px;}
.wrap{display:grid;grid-template-columns:230px minmax(0,1fr);gap:56px;max-width:1180px;margin:0 auto;padding:56px 44px 120px;}
@media(max-width:980px){.wrap{grid-template-columns:1fr;gap:28px;padding:30px 18px 80px;}.toc{position:relative!important;top:0!important;}}
.toc{position:sticky;top:36px;align-self:start;font-family:'JetBrains Mono',monospace;font-size:12px;}
.toc-lbl{text-transform:uppercase;letter-spacing:.14em;color:var(--ink-mute);margin-bottom:16px;font-size:11px;}
.toc-list{list-style:none;display:flex;flex-direction:column;gap:2px;}
.toc-list a{display:block;padding:7px 10px;text-decoration:none;color:var(--ink-soft);border-left:2px solid transparent;line-height:1.35;transition:.15s;}
.toc-list a:hover{color:var(--ink);}
.toc-list a.active{color:var(--wf-pink);border-left-color:var(--wf-pink);}
.page-header{padding-bottom:40px;border-bottom:1px solid var(--line);margin-bottom:52px;}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:20px;}
.page-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:62px;line-height:1.0;letter-spacing:-.03em;margin-bottom:16px;}
.page-byline{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:21px;color:var(--ink-soft);max-width:640px;margin-bottom:18px;}
.addendum-link{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--ink-mute);}
.addendum-link a{color:var(--ink-mute);}
.section{padding-top:58px;padding-bottom:34px;scroll-margin-top:24px;border-top:1px solid var(--line);}
.section:first-of-type{border-top:none;padding-top:0;}
.kicker{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:14px;}
.section-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:35px;letter-spacing:-.018em;line-height:1.15;margin-bottom:22px;max-width:740px;}
.section p{margin-bottom:14px;max-width:720px;}
.section p strong{color:var(--ink);}
.section em{font-style:italic;}
.lede{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:19px;color:var(--ink-soft);margin-bottom:22px;max-width:700px;line-height:1.5;}
.sub{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:21px;margin:30px 0 12px;letter-spacing:-.01em;}
.section ul{margin:8px 0 16px 22px;max-width:720px;}
.section li{margin-bottom:7px;}
.section li strong{color:var(--ink);}
.trust-list li{margin-bottom:9px;}
/* two trees */
.two-trees{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:16px;}
@media(max-width:700px){.two-trees{grid-template-columns:1fr;}}
.tt{border:1px solid var(--line);border-radius:4px;padding:24px 26px;background:var(--paper);}
.tt-tag{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--wf-pink);letter-spacing:.1em;text-transform:uppercase;margin-bottom:8px;}
.tt h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:23px;letter-spacing:-.01em;margin-bottom:4px;}
.tt-markets{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);text-transform:uppercase;letter-spacing:.04em;margin-bottom:12px!important;}
.tt p{font-size:13.5px;color:var(--ink-soft);margin-bottom:8px;}
/* tree diagram */
.tree{border:1px solid var(--line);border-radius:5px;background:var(--paper);padding:22px;margin:6px 0 14px;}
.tree-tier{}
.tier-lbl{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-mute);margin-bottom:8px;}
.tier-row{display:flex;gap:8px;flex-wrap:wrap;}
.tree-box{flex:1;min-width:110px;border:1px solid var(--line);border-radius:3px;padding:11px 12px;font-size:12px;color:var(--ink);text-align:center;background:var(--cream);}
.tree-box-trunk{border-color:var(--wf-pink);background:#FFF1F5;font-weight:500;}
.tree-box-mute{color:var(--ink-mute);font-style:italic;}
.tree-down{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--wf-pink);text-align:center;margin:10px 0!important;}
/* ladder */
.ladder{display:flex;flex-direction:column;gap:6px;margin:12px 0 16px;max-width:680px;}
.rung{display:grid;grid-template-columns:180px 1fr;gap:14px;align-items:center;border:1px solid var(--line);border-radius:3px;padding:11px 14px;background:var(--paper);}
.rung:first-child{border-color:var(--wf-pink);}
.rung-fmt{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--ink);}
.rung-role{font-size:13px;color:var(--ink-soft);}
/* region */
.region{border:1px solid var(--line);border-radius:4px;padding:22px 26px;background:var(--paper);margin-bottom:16px;}
.region-head{display:flex;align-items:baseline;gap:14px;margin-bottom:10px;flex-wrap:wrap;}
.region-head h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:24px;letter-spacing:-.01em;}
.region-when{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--wf-pink);text-transform:uppercase;letter-spacing:.04em;}
.region p{font-size:14px;color:var(--ink-soft);}
.region ul{margin-top:6px;}
.region li{font-size:13.5px;color:var(--ink-soft);}
/* timeline table */
.table-wrap{overflow-x:auto;margin:6px 0;}
.tl{width:100%;border-collapse:collapse;font-size:12.5px;}
.tl th,.tl td{padding:11px 12px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top;}
.tl th{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink);border-bottom:1px solid var(--ink);}
.tl td:first-child{font-weight:500;color:var(--ink);white-space:nowrap;}
.tl td{color:var(--ink-soft);}
.tl tbody tr:last-child{background:var(--line-soft);}
/* roles */
.roles{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px;}
@media(max-width:820px){.roles{grid-template-columns:1fr 1fr;}}
@media(max-width:480px){.roles{grid-template-columns:1fr;}}
.role{border:1px solid var(--line);border-radius:4px;padding:18px 18px;background:var(--paper);}
.role-who{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--wf-pink);margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid var(--line-soft);}
.role ul{margin:0 0 0 16px;}
.role li{font-size:12.5px;color:var(--ink-soft);margin-bottom:6px;}
/* next */
.next{list-style:none;counter-reset:n;padding:0;margin:6px 0 16px;max-width:740px;}
.next li{counter-increment:n;position:relative;padding:13px 0 13px 44px;border-bottom:1px solid var(--line-soft);font-size:14px;color:var(--ink-soft);}
.next li:last-child{border-bottom:none;}
.next li::before{content:counter(n,decimal-leading-zero);position:absolute;left:0;top:13px;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--wf-pink);}
.next li strong{color:var(--ink);}
.site-footer{margin-top:48px;padding-top:26px;border-top:1px solid var(--line);font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);text-transform:uppercase;letter-spacing:.08em;}
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
<title>Project Canopy — WorldFirst</title>
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
    <p class="gate-subtitle">The content system — operating plan.</p>
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
    <li><a href="#system">01 · The system</a></li>
    <li><a href="#trees">02 · Two trees</a></li>
    <li><a href="#anatomy">03 · Anatomy of a tree</a></li>
    <li><a href="#trust">04 · The trust model</a></li>
    <li><a href="#rollout">05 · The rollout</a></li>
    <li><a href="#timeline">06 · The timeline</a></li>
    <li><a href="#roles">07 · Automation &amp; delegation</a></li>
    <li><a href="#next">08 · Next moves</a></li>
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
(ROOT / "canopy.html").write_text(HTML, encoding="utf-8")
print(f"Wrote canopy.html ({len(HTML):,} bytes; {len(INNER):,} inner)")
