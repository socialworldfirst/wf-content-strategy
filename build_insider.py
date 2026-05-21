#!/usr/bin/env python3
"""
WorldFirst Content Strategy — The Insider direction.
Content strategy with a spine: WorldFirst as the sourcing & ecom insider.
The build-out of the proprietary-data research-franchise play (the Gong model).
Encrypts inner content with 'wf'. Same LS key as index.html (one unlock).
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
# Snippet mockups — bylined intelligence, Gong-Labs style
# ----------------------------------------------------------------------------
SNIPPETS = [
    ("WorldFirst China Desk", "with Lin Wei · Sourcing Intelligence",
     "From 1,400 SEA importer onboardings last quarter:",
     "The #1 reason a first order goes wrong isn't price. It's paying the full deposit before a live factory tour — 7 in 10 of the importers who got burned had skipped it.",
     "WorldFirst China Desk — weekly"),
    ("WorldFirst Fraud Desk", "with Adam Roslan · Risk Intelligence",
     "We blocked 3 supplier-impersonation attempts this week.",
     "All three used the identical move — a mid-deal request to “update” the supplier's bank account to a personal one. If payment details change mid-order, stop and verify.",
     "WorldFirst Fraud Desk — as it happens"),
    ("WorldFirst Ecom Desk", "with Mei Tan · Marketplace Intelligence",
     "TikTok Shop quietly changed its SEA seller payout cycle this month.",
     "Most sellers won't notice until a cash-flow gap hits around week six. Here is exactly what changed — and the two ways to bridge it.",
     "WorldFirst Ecom Desk — weekly"),
]

def snippets_html():
    out = []
    for desk, person, headline, body, foot in SNIPPETS:
        out.append(f"""<div class="snip">
      <div class="snip-byline">
        <div class="snip-avatar">W</div>
        <div><p class="snip-desk">{desk}</p><p class="snip-person">{person}</p></div>
      </div>
      <p class="snip-headline">{headline}</p>
      <p class="snip-body">{body}</p>
      <p class="snip-foot">{foot}</p>
    </div>""")
    return "\n".join(out)

# ----------------------------------------------------------------------------
# Content
# ----------------------------------------------------------------------------
HERO = """
<header class="page-header">
  <p class="eyebrow">WorldFirst · Content Strategy · The Insider Direction</p>
  <h1 class="page-title">WorldFirst, the insider.</h1>
  <p class="page-byline">The content strategy with a spine — WorldFirst as the sourcing and ecom insider. The Gong model, built for cross-border trade.</p>
  <p class="addendum-link"><a href="index.html">← Base content strategy</a> &nbsp;·&nbsp; <a href="brand-search.html">Brand-search evidence →</a></p>
</header>
"""

DIRECTION = """
<section id="direction" class="section">
  <p class="kicker">01 · The direction</p>
  <h2 class="section-title">The strategy gets a spine.</h2>
  <p class="lede">The base strategy stood four content pillars side by side. This is the evolution: WorldFirst becomes The Insider — the brand that knows what is really happening inside China sourcing and cross-border ecom, and says it first.</p>
  <p>The model is Gong. Gong didn't sell sales software by describing software. It published intelligence — "data from 100,000 sales calls shows these 3 words kill deals" — under a named, recurring research franchise, fronted by its own people. It became the brand sales leaders thought of first. When they had a problem, they searched "Gong." The companion brand-search analysis rates this — a <strong>proprietary-data research franchise</strong> — as the single most transferable play for WorldFirst. This page builds it out.</p>
  <p>One thing it is <em>not</em>: stamping "WorldFirst" onto every asset title. That is the weakest technique on the board — it reads promotional, and it loses both reach and attribution. The Insider direction does the opposite. It builds a genuine named intelligence franchise with a human face and a real vantage. The brand rides in the byline and the consistency, never in a stamped PDF name.</p>
  <p>Why this direction holds: WorldFirst sits in the middle of the SEA-to-China trade flow. That position <em>is</em> a vantage. The Insider direction turns the vantage into the content engine — not "content about sourcing," but intelligence from inside it. It is defensible (a competitor can copy a how-to video; they cannot copy your vantage), and it is the only engine that reliably ends in brand search.</p>
</section>
"""

ENGINE = """
<section id="engine" class="section">
  <p class="kicker">02 · The engine</p>
  <h2 class="section-title">The Insider loop is a flywheel.</h2>
  <p class="lede">The engine is a cycle, and it compounds — every turn makes the next one stronger.</p>

  <div class="loop">
    <div class="loop-step"><span class="loop-n">01</span><p class="loop-t">Vantage</p><p class="loop-d">WorldFirst's frontline sees the trade flow — onboardings, fraud patterns, field visits, surveys.</p></div>
    <div class="loop-arrow">→</div>
    <div class="loop-step"><span class="loop-n">02</span><p class="loop-t">Intelligence</p><p class="loop-d">The vantage becomes counterintuitive, specific insight. Not "how to source" — "the real reason first orders fail."</p></div>
    <div class="loop-arrow">→</div>
    <div class="loop-step"><span class="loop-n">03</span><p class="loop-t">Branded distribution</p><p class="loop-d">Published under named WorldFirst desks and faces, led on LinkedIn, cut for every platform.</p></div>
    <div class="loop-arrow">→</div>
    <div class="loop-step"><span class="loop-n">04</span><p class="loop-t">WorldFirst = the source</p><p class="loop-d">Repeated weekly, WorldFirst becomes the name SEA importers associate with knowing sourcing and ecom.</p></div>
    <div class="loop-arrow">→</div>
    <div class="loop-step loop-step-end"><span class="loop-n">05</span><p class="loop-t">Brand search → inbound</p><p class="loop-d">When they have a problem, they search "WorldFirst" — not "supplier check." High-intent inbound.</p></div>
  </div>
  <div class="loop-back">↻ &nbsp;The flywheel — every new customer is more frontline vantage. More vantage → sharper intelligence → more authority → more customers. It compounds.</div>
</section>
"""

VANTAGE = """
<section id="vantage" class="section">
  <p class="kicker">03 · The vantage</p>
  <h2 class="section-title">Where the intelligence comes from.</h2>
  <p class="lede">Gong's credibility was its data vantage. WorldFirst can't publish raw payment data — but the vantage doesn't depend on it. Four real sources, none of which touch sensitive data.</p>

  <div class="vgrid">
    <div class="vcard">
      <p class="vnum">Source 01</p>
      <h3>The frontline</h3>
      <p>The China desk and onboarding team talk to thousands of importers and see thousands of supplier situations a quarter. The team is a sensor. "We onboarded 1,400 importers last quarter — the most common mistake was X." Observational, not transactional.</p>
    </div>
    <div class="vcard">
      <p class="vnum">Source 02</p>
      <h3>The fraud desk</h3>
      <p>The risk team sees scam patterns nobody else sees at that volume. "The 3 impersonation attempts we blocked this week opened with the same line." Pattern-level, not customer data — and scam content travels hardest.</p>
    </div>
    <div class="vcard">
      <p class="vnum">Source 03</p>
      <h3>The field</h3>
      <p>People at Canton Fair, in Yiwu, on factory floors, reporting back. "Insider" can literally mean "we were there this week." First-hand, un-copyable.</p>
    </div>
    <div class="vcard">
      <p class="vnum">Source 04</p>
      <h3>Original surveys</h3>
      <p>The opt-in importer base, asked directly. "We asked 800 SEA importers what worried them most about 2027 — the #1 answer wasn't price." Publishable, owned, no compliance issue.</p>
    </div>
  </div>
  <p class="vnote">A note worth a legal conversation: a compliance-cleared version of real data almost certainly exists — aggregated, anonymised, directional. "X% of importers we onboarded mentioned Y" supercharges the vantage. Worth asking. But the four sources above work even if zero raw data ever clears.</p>
</section>
"""

LANES = """
<section id="lanes" class="section">
  <p class="kicker">04 · Two lanes</p>
  <h2 class="section-title">One engine, two desks.</h2>
  <p class="lede">The Insider speaks to WorldFirst's two primary audiences through two lanes — same mechanic, two desks.</p>

  <div class="lane-grid">
    <article class="lane">
      <p class="lane-tag">Lane 01</p>
      <h3>Sourcing Insider</h3>
      <p class="lane-who">For the Operator Importer.</p>
      <p>What is really happening inside China sourcing — suppliers, factories, Canton Fair, 1688, customs, freight, the scams. The China Desk and the Fraud Desk lead this lane.</p>
    </article>
    <article class="lane">
      <p class="lane-tag">Lane 02</p>
      <h3>Ecom Insider</h3>
      <p class="lane-who">For the Cross-border Ecom Seller.</p>
      <p>What is really happening inside cross-border ecommerce — Amazon, Shopee, Lazada and TikTok Shop policy shifts, payout changes, what is selling, what is breaking. The Ecom Desk leads this lane.</p>
    </article>
  </div>
</section>
"""

SHOWUP = f"""
<section id="showup" class="section">
  <p class="kicker">05 · How the Insider shows up</p>
  <h2 class="section-title">Named desks, named faces, real intelligence.</h2>
  <p class="lede">The Insider is not a tone of voice. It is a set of named, recurring franchises — each with a human face and a distinctive format.</p>

  <h3 class="sub">The desks are the franchises</h3>
  <p>The WorldFirst <strong>China Desk</strong>, <strong>Fraud Desk</strong> and <strong>Ecom Desk</strong>. Each is a named, recurring, distinctively-formatted franchise — WorldFirst's equivalent of "Gong Labs." The franchise name is itself the searchable asset; it accrues brand equity every time it publishes. Lock the names, lock the format, never let them drift.</p>

  <h3 class="sub">Each desk has a face</h3>
  <p>Every desk is fronted by a named, recurring WorldFirst person — not a logo. Trust forms faster around a person, and personal accounts outperform brand accounts by roughly 2×. The desk is the franchise; the person is the face. This is the same move Gong made turning its own people into the messengers — pick 3-5 real WorldFirst insiders and make them the recurring voices.</p>

  <h3 class="sub">Flagship intelligence + everyday content</h3>
  <p><strong>Flagship</strong> — the recurring intelligence drops: a weekly read from each desk on what is shifting, the fraud dispatches, field notes from Canton Fair, the annual importer survey. These are the brand-builders. <strong>Everyday</strong> — the high-volume how-to, scam-warning and payment content from the base strategy, every piece now carrying the insider voice and a named desk. Flagship builds authority; everyday builds reach. Both run on the insider identity.</p>

  <h3 class="sub">What an intelligence drop looks like</h3>
  {snippets_html()}
  <p class="snip-note">Note what carries the brand: the franchise byline — "WorldFirst China Desk" — recurring and consistent, plus the named person. Not a stamped asset title. The byline is the brand vehicle.</p>
</section>
"""

BRANDSEARCH = """
<section id="brandsearch" class="section">
  <p class="kicker">06 · Why this lifts brand search</p>
  <h2 class="section-title">The engine that ends in a brand search.</h2>
  <p class="lede">The companion brand-search page rates the proprietary-data research franchise as the top play. The Insider direction is its build-out — and it wins exactly where stamping the name on everything loses.</p>
  <ul class="bs-list">
    <li><strong>It keeps reach.</strong> Bylined intelligence does not read as promotional, so platforms don't throttle it. A stamped, salesy asset name does — and loses up to 40% of organic reach before anyone sees it.</li>
    <li><strong>It is attributable.</strong> A named franchise, a consistent face and a distinctive format let the audience recognise WorldFirst in the 1.5 seconds a feed gives it — without a logo stamp doing the work.</li>
    <li><strong>It compounds into the name.</strong> Repeated weekly under the same desks and faces, WorldFirst becomes the name associated with knowing the trade. The problem arrives; they search "WorldFirst," the desk, or the person.</li>
    <li><strong>It seeds a sub-language.</strong> A desk that repeatedly uses and defines its own terms — "same-day CNY," "1688 supplier payments" — can come to own the phrase, turning a category search into a brand search.</li>
  </ul>
  <p>Measured the same way: brand search as the North Star, geo-focused on one lead region so the lift is readable. The full measurement model is on the <a href="brand-search.html">brand-search page</a>.</p>
</section>
"""

RUNS = """
<section id="runs" class="section">
  <p class="kicker">07 · How it runs</p>
  <h2 class="section-title">Running the Insider.</h2>

  <h3 class="sub">Platforms</h3>
  <p>LinkedIn is the home of the flagship intelligence — it is where Gong runs the same play, and where the importer-as-business-owner is reachable. TikTok, Instagram and YouTube carry the everyday content and the cut-downs of each intelligence drop. WhatsApp carries the Fraud Desk alerts — triggered, not scheduled.</p>

  <h3 class="sub">The roster</h3>
  <p>The strategy runs on real people. Pick 3-5 named WorldFirst insiders — a China desk lead, a fraud/risk lead, an ecom desk voice — and make them the recurring faces. They are the brand's micro-influencers; their personal reach is an asset the brand account cannot match.</p>

  <h3 class="sub">Cadence</h3>
  <p>Flagship — at least one intelligence drop a week across the desks, the recurring franchises (field notes, the survey) on their own rhythm. Everyday — the platform cadences from the base strategy. One vantage observation, produced once, becomes a LinkedIn intelligence post, a TikTok cut-down, a carousel and a WhatsApp alert.</p>

  <h3 class="sub">The bar</h3>
  <p>Insider intelligence only works if it is genuinely insider. The test: is this something only someone inside the trade flow would know? If it is googleable, it is not intelligence — it is content, and it will read generic. Counterintuitive, specific, vantage-sourced, every time. And the vantage must be real and consistently fed — the desks only stay credible if the frontline keeps feeding them.</p>
</section>
"""

FOOTER = """
<footer class="site-footer">
  <p>WorldFirst · Internal · Content Strategy / The Insider · May 2026 · <a href="#" id="lock">lock device</a></p>
</footer>
"""

INNER = HERO + DIRECTION + ENGINE + VANTAGE + LANES + SHOWUP + BRANDSEARCH + RUNS + FOOTER

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
code{font-family:'JetBrains Mono',monospace;font-size:.86em;background:var(--line-soft);padding:1px 5px;border-radius:2px;}
.progress{position:fixed;top:0;left:0;height:2px;background:var(--wf-pink);z-index:100;width:0;transition:width .05s linear;}
.gate{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px;}
.gate-card{width:100%;max-width:420px;text-align:center;}
.gate-eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:22px;}
.gate-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:48px;letter-spacing:-.02em;margin-bottom:14px;line-height:1.04;}
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
.page-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:60px;line-height:1.02;letter-spacing:-.025em;margin-bottom:16px;}
.page-byline{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:21px;color:var(--ink-soft);max-width:620px;margin-bottom:18px;}
.addendum-link{font-family:'JetBrains Mono',monospace;font-size:12px;}
.addendum-link a{color:var(--ink-mute);}
.section{padding-top:58px;padding-bottom:34px;scroll-margin-top:24px;border-top:1px solid var(--line);}
.section:first-of-type{border-top:none;padding-top:0;}
.kicker{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:14px;}
.section-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:35px;letter-spacing:-.018em;line-height:1.15;margin-bottom:22px;max-width:720px;}
.section p{margin-bottom:14px;max-width:720px;}
.section p strong{color:var(--ink);}
.section em{font-style:italic;}
.lede{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:19px;color:var(--ink-soft);margin-bottom:22px;max-width:700px;line-height:1.5;}
.sub{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:21px;margin:30px 0 12px;letter-spacing:-.01em;}
.section ul{margin:8px 0 16px 22px;max-width:720px;}
.section li{margin-bottom:7px;}
.section li strong{color:var(--ink);}
/* loop */
.loop{display:flex;align-items:stretch;gap:7px;flex-wrap:wrap;margin:6px 0 12px;}
.loop-step{flex:1;min-width:135px;border:1px solid var(--line);border-radius:4px;padding:14px 14px;background:var(--paper);}
.loop-step-end{border-color:var(--wf-pink);}
.loop-n{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--wf-pink);}
.loop-t{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:16px;margin:4px 0 6px;}
.loop-d{font-size:12px;color:var(--ink-soft);margin:0;}
.loop-arrow{display:flex;align-items:center;color:var(--ink-mute);font-size:15px;}
@media(max-width:760px){.loop-arrow{display:none;}}
.loop-back{margin-top:10px;border:1px dashed var(--wf-pink);border-radius:4px;padding:12px 16px;font-size:13.5px;color:var(--ink-soft);background:#FFF1F5;}
/* vantage */
.vgrid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:14px;}
@media(max-width:700px){.vgrid{grid-template-columns:1fr;}}
.vcard{border:1px solid var(--line);border-radius:4px;padding:20px 22px;background:var(--paper);}
.vnum{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--wf-pink);letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px;}
.vcard h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:20px;margin-bottom:6px;}
.vcard p{font-size:13.5px;color:var(--ink-soft);margin:0;}
.vnote{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);line-height:1.65;}
/* lanes */
.lane-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;}
@media(max-width:700px){.lane-grid{grid-template-columns:1fr;}}
.lane{border:1px solid var(--line);border-radius:4px;padding:24px 26px;background:var(--paper);}
.lane-tag{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--wf-pink);letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px;}
.lane h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:24px;letter-spacing:-.01em;margin-bottom:4px;}
.lane-who{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:15px;color:var(--ink-soft);margin-bottom:10px!important;}
.lane p{font-size:14px;color:var(--ink-soft);margin:0;}
/* snippets */
.snip{border:1px solid var(--line);border-radius:6px;padding:18px 20px;background:var(--paper);margin-bottom:12px;max-width:560px;}
.snip-byline{display:flex;gap:11px;align-items:center;margin-bottom:12px;}
.snip-avatar{width:42px;height:42px;border-radius:5px;background:linear-gradient(135deg,#E6185F,#001E5C);display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:20px;color:#fff;flex-shrink:0;}
.snip-desk{font-size:13.5px;font-weight:600;color:var(--ink);}
.snip-person{font-size:11.5px;color:var(--ink-mute);}
.snip-headline{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:18px;line-height:1.3;color:var(--ink);margin-bottom:8px!important;}
.snip-body{font-size:14px;color:var(--ink-soft);margin-bottom:12px!important;}
.snip-foot{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--wf-pink);text-transform:uppercase;letter-spacing:.08em;padding-top:10px;border-top:1px solid var(--line-soft);margin:0!important;}
.snip-note{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);line-height:1.65;margin-top:8px;}
/* brand search list */
.bs-list li{font-size:14.5px;color:var(--ink-soft);margin-bottom:9px;}
/* footer */
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
<title>WorldFirst Content Strategy — The Insider</title>
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
    <h1 class="gate-title">The Insider</h1>
    <p class="gate-subtitle">Content strategy — the Insider direction.</p>
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
    <li><a href="#direction">01 · The direction</a></li>
    <li><a href="#engine">02 · The engine</a></li>
    <li><a href="#vantage">03 · The vantage</a></li>
    <li><a href="#lanes">04 · Two lanes</a></li>
    <li><a href="#showup">05 · How it shows up</a></li>
    <li><a href="#brandsearch">06 · Brand search</a></li>
    <li><a href="#runs">07 · How it runs</a></li>
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
(ROOT / "insider.html").write_text(HTML, encoding="utf-8")
print(f"Wrote insider.html ({len(HTML):,} bytes; {len(INNER):,} inner)")
