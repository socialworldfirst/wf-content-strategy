#!/usr/bin/env python3
"""
WorldFirst Content Strategy — Brand Search addendum (evidence-based rebuild).
Rebuilt on researched best practice: built-in vs bolt-on branding, proven B2B plays.
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
# Data
# ----------------------------------------------------------------------------
PLAYS = [
    ("Proprietary-data research franchise", "Gong Labs",
     "Turn data only WorldFirst has into a named, recurring research series. Un-copyable, inherently quotable — it earns citations, and the brand name rides inside every one."),
    ("Own a sub-language", "HubSpot · Drift",
     "Coin and seed a phrase until the phrase and the brand are inseparable, and the category search becomes a brand search. Realistic for WF: not a grand new category — a sub-language like \"1688 supplier payments\" or \"same-day CNY.\""),
    ("A consistent human face", "Ahrefs",
     "A recurring presenter is a distinctive asset that carries a point of view. Trust forms faster around a person than a logo — personal accounts outperform brand accounts roughly 2×."),
    ("A named recurring franchise", "Global Sourcing Guide",
     "A named show accrues brand equity every episode, and the franchise name is itself the searchable asset. WorldFirst already has one — the discipline is to lock the name and never let it drift."),
    ("Distinctive brand assets", "Gong · Ramp",
     "Consistent visual and verbal codes let the audience attribute content in the 1.5 seconds a feed gives it. Campaigns with a recurring \"fluent device\" are 73% more likely to report large profit gains."),
    ("Community and creators", "Notion · Clay",
     "Give your most passionate users status, tools and amplification. Their content multiplies branded mentions outside your own channels, where they read as credible."),
]

CASES = [
    ("Gong", "Proprietary-data research franchise",
     "\"Gong Labs\" — a named, recurring research series built on data only Gong has: millions of recorded sales calls. The findings are un-copyable and inherently quotable, so they get cited, screenshotted and re-shared everywhere — and the brand name rides inside every citation. That is how \"Gong\" became inseparable from \"revenue intelligence.\" The single most transferable case for WorldFirst."),
    ("Ahrefs", "Product-led content + a human face",
     "Product-led educational content at scale, fronted by a visible CMO — Tim Soulo. Internal testing found ads run through Soulo's personal account performed 2× better than the same ads from the @Ahrefs brand account. $100M+ ARR, zero outside funding — built on content, not outbound."),
    ("HubSpot &amp; Drift", "Category creation — own a phrase",
     "HubSpot coined \"inbound marketing\"; Drift coined \"conversational marketing.\" Both deliberately refused to trademark the term — they wanted every agency and blogger using it, betting they could be the brand most associated with it. The category phrase itself became the brand search."),
    ("Clay", "Category creation via a role",
     "Clay invented a job title — \"GTM Engineer\" — a new identity for technical go-to-market operators. People put it on their LinkedIn profiles and in job postings. The identity spreads the brand: category creation through a role, carried by the people who adopt it."),
    ("Mailchimp", "Engineer the search, then capture it",
     "The purest case of manufacturing brand search on purpose: Mailchimp turned memorable mispronunciations of its name — MailShrimp, KaleLimp, FailChips — into real content, then bought paid search on all of them so the curiosity landed back on the brand. Worth knowing as a mechanic; too gimmicky to be WorldFirst's model."),
]

def plays_html():
    out = []
    for i, (name, case, desc) in enumerate(PLAYS, 1):
        out.append(f"""<li class="play">
          <p class="play-head"><span class="play-name">{name}</span><span class="play-case">{case}</span></p>
          <p class="play-desc">{desc}</p>
        </li>""")
    return "\n".join(out)

def cases_html():
    out = []
    for brand, mech, desc in CASES:
        out.append(f"""<article class="case">
          <div class="case-head"><h3>{brand}</h3><span class="case-mech">{mech}</span></div>
          <p>{desc}</p>
        </article>""")
    return "\n".join(out)

# ----------------------------------------------------------------------------
# Content
# ----------------------------------------------------------------------------
HERO = """
<header class="page-header">
  <p class="eyebrow">WorldFirst · Content Strategy · Addendum · Rebuilt on evidence</p>
  <h1 class="page-title">Engineered for brand search.</h1>
  <p class="page-byline">How brands actually lift brand search through social — and the corrected play for WorldFirst, rebuilt on researched best practice.</p>
  <p class="addendum-link"><a href="index.html">← The base content strategy</a></p>
</header>
"""

CORRECTION = """
<section id="correction" class="section">
  <p class="kicker">01 · The correction</p>
  <h2 class="section-title">The metric was right. The tactic was wrong.</h2>
  <p class="lede">This page got it wrong the first time. It said: attach the WorldFirst name to every asset — "the WorldFirst Canton Fair Map," "the WorldFirst Supplier Check." This is the corrected version, rebuilt on how brands actually do this.</p>
  <p>Keep the North Star. Brand search is a legitimate one — Les Binet's Share of Search work (branded search divided by category search) correlates around <strong>83% with market share</strong> and <em>leads</em> it by 6-24 months. As a measurable proxy for brand awareness, it holds up.</p>
  <p>But researching how brands actually engineer brand-search lift, the verdict on "attach the name" is blunt: it is the <strong>single weakest technique on the board</strong>. The B2B brands that have genuinely done this — Gong, Ahrefs, HubSpot — did something structurally different. This page replaces the naming exercise with what the evidence supports.</p>
</section>
"""

FAILS = """
<section id="fails" class="section">
  <p class="kicker">02 · Why it fails</p>
  <h2 class="section-title">Attaching the name fails twice.</h2>
  <p class="lede">It is not a small effect that needs scaling up. It is structurally wrong, and it loses on two fronts at once.</p>
  <div class="fail-grid">
    <div class="fail">
      <p class="fail-num">Failure 01</p>
      <h3>It loses reach</h3>
      <p>Platforms throttle promotional framing. Explicit brand stamps and sales layers cut LinkedIn organic reach by up to <strong>40%</strong>, and branded content underperforms organic on engagement even setting algorithms aside. Putting the name on it shrinks the audience that could ever form a memory.</p>
    </div>
    <div class="fail">
      <p class="fail-num">Failure 02</p>
      <h3>It loses attribution</h3>
      <p>A feed gives a post around <strong>1.5 seconds</strong> of attention. Only branding <em>structurally tied</em> to the content gets attributed in that window. A bolt-on logo or a "WorldFirst" prefix sits outside it — the viewer encodes the topic, not the brand. VCCP and Karen Nelson-Field: weak branding wastes <strong>66p of every £1</strong>.</p>
    </div>
  </div>
  <p>The Canton Fair symptom still holds — a topic video sends people to Google "Canton Fair." But the fix is not a better label. Renaming the asset "WorldFirst Canton Fair Map" is still a label; it still loses reach and still loses attribution. The fix is structural.</p>
</section>
"""

DISTINCTION = """
<section id="distinction" class="section">
  <p class="kicker">03 · The distinction</p>
  <h2 class="section-title">Brand built-in, not brand bolted-on.</h2>
  <p class="lede">This is the one distinction that the whole rebuild turns on. The goal is not less brand. It is not more brand. It is structural brand.</p>
  <div class="cmp-grid">
    <div class="cmp cmp-bad">
      <p class="cmp-label">Bolt-on</p>
      <p class="cmp-def">Branding is a separable layer — an end-card logo, a watermark, a "WorldFirst-" prefix on a title. Strip it away and the content is unchanged.</p>
      <ul class="cmp-list">
        <li>Platforms read the layer as promotional and throttle it.</li>
        <li>Viewers skip the layer; they encode the topic, not the brand.</li>
        <li>The appearance of branding without the mechanism of branding.</li>
      </ul>
      <p class="cmp-verdict">Loses reach <em>and</em> attribution.</p>
    </div>
    <div class="cmp cmp-good">
      <p class="cmp-label">Built-in</p>
      <p class="cmp-def">The brand is inseparable from the value. The recurring presenter <em>is</em> the format. The proprietary data carries the brand name in its title. The owned phrase <em>is</em> the subject.</p>
      <ul class="cmp-list">
        <li>You cannot strip the brand out without destroying the content.</li>
        <li>Nothing for the algorithm to flag — no promotional penalty.</li>
        <li>Attribution is total: the brand is the value, not a sticker on it.</li>
      </ul>
      <p class="cmp-verdict">Wins reach <em>and</em> attribution.</p>
    </div>
  </div>
  <p>Every play that follows is a way of making the brand built-in. None of them attach a name.</p>
</section>
"""

PLAYS_SEC = f"""
<section id="plays" class="section">
  <p class="kicker">04 · The plays</p>
  <h2 class="section-title">Six plays that actually move brand search.</h2>
  <p class="lede">Each one is proven by a B2B brand, and each one makes the brand structural rather than decorative.</p>
  <ol class="plays">
    {plays_html()}
  </ol>
</section>
"""

CASES_SEC = f"""
<section id="cases" class="section">
  <p class="kicker">05 · The evidence</p>
  <h2 class="section-title">Five brands that did it — without slapping the name on.</h2>
  <p class="lede">The B2B cases worth being convinced by. Each used a real mechanic; none relied on labelling content with the brand.</p>
  {cases_html()}
</section>
"""

WFPLAY = """
<section id="wfplay" class="section">
  <p class="kicker">06 · The WorldFirst play</p>
  <h2 class="section-title">Lead with the Gong model.</h2>
  <p class="lede">The headline recommendation, drawn straight from the evidence: a named, recurring research franchise built on WorldFirst's proprietary data.</p>
  <p>WorldFirst sits on data nobody else has — cross-border payment flows, FX corridors, supplier-verification patterns, the scam attempts it blocks. Give that data a fixed-name franchise. Publish it on a fixed cadence. The brand name then rides inside every citation, every screenshot, every share — because the data is uncopyable and the brand is in the title. It is <strong>built-in by construction</strong>: there is nothing to strip out and nothing for an algorithm to flag.</p>
  <p>Then stack the supporting plays: a consistent Global Sourcing Guide presenter (the human face), an owned sub-language seeded across everything ("1688 supplier payments"), and locked distinctive visual codes.</p>
  <div class="callout">
    <p class="callout-label">What this replaces</p>
    <p>Version one's instinct — make WorldFirst the source and author — was right. Its execution — rename every asset "WorldFirst-X" — was the bolt-on version of that instinct. The research franchise is the <em>built-in</em> version of the same idea. Same goal, structural delivery.</p>
  </div>
</section>
"""

MEASURE = """
<section id="measure" class="section">
  <p class="kicker">07 · Realism &amp; measurement</p>
  <h2 class="section-title">What brand search will, and won't, do.</h2>
  <p class="lede">An honest North Star comes with honest limits. Three, and then how to read the lift.</p>
  <ul class="real">
    <li><strong>It is slow.</strong> Branded search is a leading indicator — it moves on a 6-24 month horizon, bounded by share of voice. No spike holds. Judge it on quarters, not posts.</li>
    <li><strong>The navigational trap.</strong> WorldFirst is a fintech with daily-login account-holders. A large share of "WorldFirst" searches is existing customers reaching the login page — raw branded search measures your installed base, not new awareness. Track <em>net-new, non-navigational</em> branded search and the branded long-tail.</li>
    <li><strong>Don't let the metric corrupt the creative.</strong> Flat, direct, "left-brain" creative drives short-term search and clicks faster — but kills the long-term brand effect. If the literal KPI becomes a near-term brand-search bump, the team will drift to direct-response creative that hits the number and hollows the brand. Brand search is the scoreboard, not the playbook.</li>
  </ul>

  <h3 class="sub">Prove it with a geo-holdout</h3>
  <p>Run the content in one focus region (Malaysia), hold a comparable market dark, and compare the branded-search delta. It is the only way to isolate social's contribution from PR, paid and word-of-mouth. Concentrate the spend — brand search only moves as a readable signal when it is not spread thin.</p>
  <div class="chart-wrap">
    <svg viewBox="0 0 520 240" xmlns="http://www.w3.org/2000/svg">
      <text x="20" y="22" font-family="JetBrains Mono" font-size="10" fill="#888">NON-NAVIGATIONAL BRANDED SEARCH · INDEXED TO BASELINE</text>
      <line x1="48" y1="200" x2="500" y2="200" stroke="#E5E0D5"/>
      <line x1="48" y1="40" x2="48" y2="200" stroke="#E5E0D5"/>
      <g font-family="JetBrains Mono" font-size="9" fill="#888">
        <text x="42" y="204" text-anchor="end">100</text>
        <text x="42" y="124" text-anchor="end">150</text>
        <text x="42" y="48" text-anchor="end">200</text>
      </g>
      <line x1="160" y1="40" x2="160" y2="200" stroke="#E5E0D5" stroke-dasharray="3 3"/>
      <text x="166" y="52" font-family="JetBrains Mono" font-size="9" fill="#888">franchise launches</text>
      <polyline points="48,200 104,199 160,200 216,186 272,164 328,138 384,114 440,92 496,76"
        fill="none" stroke="#E6185F" stroke-width="2.5"/>
      <polyline points="48,200 104,200 160,199 216,198 272,200 328,197 384,199 440,198 496,196"
        fill="none" stroke="#888" stroke-width="2" stroke-dasharray="4 3"/>
      <circle cx="496" cy="76" r="4" fill="#E6185F"/>
      <text x="488" y="68" text-anchor="end" font-family="JetBrains Mono" font-size="9" fill="#E6185F">focus region (Malaysia)</text>
      <text x="488" y="188" text-anchor="end" font-family="JetBrains Mono" font-size="9" fill="#888">holdout market</text>
    </svg>
  </div>
  <p class="chart-cap">The read: focus-region non-navigational branded search, indexed to baseline, monthly. The gap between the lines is social's isolated contribution — visible on a 6-24 month horizon, not in weeks.</p>
</section>
"""

FOOTER = """
<footer class="site-footer">
  <p>WorldFirst · Internal · Content Strategy / Brand Search · Rebuilt May 2026 · <a href="#" id="lock">lock device</a></p>
</footer>
"""

INNER = HERO + CORRECTION + FAILS + DISTINCTION + PLAYS_SEC + CASES_SEC + WFPLAY + MEASURE + FOOTER

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
.page-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:58px;line-height:1.03;letter-spacing:-.025em;margin-bottom:16px;}
.page-byline{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:21px;color:var(--ink-soft);max-width:640px;margin-bottom:18px;}
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
/* fail grid */
.fail-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:18px;}
@media(max-width:700px){.fail-grid{grid-template-columns:1fr;}}
.fail{border:1px solid var(--line);border-radius:4px;padding:22px 24px;background:var(--paper);}
.fail-num{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--wf-pink);letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px;}
.fail h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:21px;margin-bottom:8px;}
.fail p{font-size:13.5px;color:var(--ink-soft);margin:0;}
/* compare */
.cmp-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;}
@media(max-width:700px){.cmp-grid{grid-template-columns:1fr;}}
.cmp{border:1px solid var(--line);border-radius:4px;padding:22px 24px;}
.cmp-bad{background:var(--line-soft);}
.cmp-good{background:#FFF1F5;border-color:var(--wf-pink-soft);}
.cmp-label{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.12em;margin-bottom:10px;}
.cmp-bad .cmp-label{color:var(--ink-mute);}
.cmp-good .cmp-label{color:var(--wf-pink);}
.cmp-def{font-size:14px;color:var(--ink-soft);margin-bottom:12px;}
.cmp-list{list-style:none;padding:0;margin:0 0 12px;}
.cmp-list li{font-size:13px;color:var(--ink-soft);padding:5px 0 5px 16px;position:relative;}
.cmp-list li::before{content:"·";position:absolute;left:2px;color:var(--wf-pink);}
.cmp-verdict{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:16px;color:var(--ink);margin:0;}
/* plays */
.plays{list-style:none;counter-reset:p;padding:0;margin:0;}
.play{counter-increment:p;position:relative;padding:16px 0 16px 44px;border-bottom:1px solid var(--line-soft);max-width:760px;}
.play:last-child{border-bottom:none;}
.play::before{content:counter(p,decimal-leading-zero);position:absolute;left:0;top:18px;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--wf-pink);}
.play-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:5px!important;}
.play-name{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:18px;color:var(--ink);}
.play-case{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.06em;color:var(--wf-pink);border:1px solid var(--wf-pink-soft);border-radius:100px;padding:3px 9px;}
.play-desc{font-size:13.5px;color:var(--ink-soft);margin:0!important;}
/* cases */
.case{border:1px solid var(--line);border-radius:4px;padding:20px 24px;background:var(--paper);margin-bottom:14px;}
.case-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:8px;}
.case-head h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:22px;color:var(--ink);}
.case-mech{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-mute);}
.case p{font-size:14px;color:var(--ink-soft);margin:0;}
/* callout */
.callout{border:1px solid var(--ink);border-radius:5px;padding:20px 24px;background:var(--paper);margin-top:6px;}
.callout-label{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--wf-pink);margin-bottom:8px!important;}
.callout p:last-child{font-size:14px;color:var(--ink-soft);margin:0;}
/* realism */
.real{list-style:none;padding:0;margin:0 0 8px;max-width:760px;}
.real li{padding:14px 0;border-bottom:1px solid var(--line-soft);font-size:14.5px;color:var(--ink-soft);}
.real li:last-child{border-bottom:none;}
.real li strong{color:var(--ink);}
/* chart */
.chart-wrap{border:1px solid var(--line);border-radius:4px;padding:18px;background:var(--paper);margin:14px 0 8px;}
.chart-wrap svg{display:block;width:100%;height:auto;}
.chart-cap{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);}
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
<title>WorldFirst Content Strategy — Brand Search</title>
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
    <h1 class="gate-title">Brand Search</h1>
    <p class="gate-subtitle">The content strategy, rebuilt on evidence.</p>
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
    <li><a href="#correction">01 · The correction</a></li>
    <li><a href="#fails">02 · Why it fails</a></li>
    <li><a href="#distinction">03 · Built-in vs bolt-on</a></li>
    <li><a href="#plays">04 · The plays</a></li>
    <li><a href="#cases">05 · The evidence</a></li>
    <li><a href="#wfplay">06 · The WorldFirst play</a></li>
    <li><a href="#measure">07 · Realism &amp; measurement</a></li>
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
(ROOT / "brand-search.html").write_text(HTML, encoding="utf-8")
print(f"Wrote brand-search.html ({len(HTML):,} bytes; {len(INNER):,} inner)")
