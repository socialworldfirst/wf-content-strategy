#!/usr/bin/env python3
"""
WorldFirst Content Strategy — Brand Search addendum.
Re-tailors the content strategy with brand search as the North Star metric.
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
# Before / after content transformations
# ----------------------------------------------------------------------------
PAIRS = [
    ("Canton Fair",
     "Canton Fair 2027: The Complete Playbook", "Canton Fair 2027",
     "We mapped all 9 Canton Fair halls and ranked them for SEA importers — the WorldFirst Hall Map. Free, link below.",
     "WorldFirst Canton Fair map",
     "The payoff is a named, branded asset. The brand is the only door to it."),
    ("Supplier red flags",
     "12 red flags in a supplier PI", "supplier PI red flags",
     "The WorldFirst Supplier Check — the 12-flag scan our China desk runs on every factory invoice.",
     "WorldFirst Supplier Check",
     "The method is named for the brand. The framework carries it."),
    ("Scam phrases",
     "5 words a real supplier never says", "China supplier scams",
     "Our fraud desk reviews 12,000 supplier invoices a month. The 5 phrases that always flag a scam.",
     "WorldFirst fraud desk",
     "Leads with the proprietary vantage only WorldFirst has. The authority is branded."),
    ("FX cost",
     "Your bank's CNY rate vs the real rate", "CNY to MYR rate",
     "We built the True-Cost Check — see exactly what your bank's margin costs on a supplier payment.",
     "WorldFirst True Cost",
     "The payoff is a branded tool. You search the brand to use it."),
    ("CNY calendar",
     "CNY 2027 payment calendar", "CNY 2027 dates",
     "The WorldFirst CNY Payment Calendar — every factory-close and last-safe-send date, one poster, updated yearly.",
     "WorldFirst CNY calendar",
     "A recurring, named, branded annual franchise people come back to."),
    ("Customer story",
     "An importer lost RM87,000 to a fake supplier", "(nothing branded)",
     "An importer was about to lose RM87,000 — the exact check WorldFirst ran that caught it.",
     "WorldFirst supplier verification",
     "WorldFirst is the protagonist of the rescue, not a bystander narrating it."),
]

def pair_cards():
    out = []
    for tag, t_title, t_search, b_title, b_search, why in PAIRS:
        out.append(f"""
<div class="ba">
  <p class="ba-tag">{tag}</p>
  <div class="ba-grid">
    <div class="ba-side ba-old">
      <p class="ba-label">Topic-led — the old way</p>
      <p class="ba-title">{t_title}</p>
      <p class="ba-search">After watching, they Google: <span class="ba-q ba-q-leak">{t_search}</span></p>
    </div>
    <div class="ba-arrow">→</div>
    <div class="ba-side ba-new">
      <p class="ba-label">Brand-engineered</p>
      <p class="ba-title">{b_title}</p>
      <p class="ba-search">After watching, they Google: <span class="ba-q ba-q-win">{b_search}</span></p>
    </div>
  </div>
  <p class="ba-why"><strong>Why it flips:</strong> {why}</p>
</div>""")
    return "\n".join(out)

# ----------------------------------------------------------------------------
# Content
# ----------------------------------------------------------------------------
HERO = """
<header class="page-header">
  <p class="eyebrow">WorldFirst · Content Strategy · Addendum</p>
  <h1 class="page-title">Engineered for brand search.</h1>
  <p class="page-byline">The content strategy, re-tailored so the audience searches WorldFirst — not just the topic. Brand search as the North Star.</p>
  <p class="addendum-link"><a href="index.html">← The base content strategy</a></p>
</header>
"""

NORTHSTAR = """
<section id="northstar" class="section">
  <p class="kicker">01 · The North Star</p>
  <h2 class="section-title">Brand search is the metric this is built to move.</h2>
  <p class="lede">The brief: one North Star — lift WorldFirst brand search through social. It is not the whole story of brand awareness, but it is the part you can read.</p>
  <p>Brand search works as a North Star for three reasons. It is <strong>measurable</strong> — Google Search Console and Trends give you the volume. It is <strong>attributable to intent</strong> — someone typing "WorldFirst" has decided WorldFirst is the answer, which is exactly the shift social is meant to create. And it is a <strong>readable proxy</strong> — it will not capture everything, but it moves when awareness moves, so it is a usable reference for whether the spend is working.</p>
  <p>One honest caveat carried through this whole document: brand search <em>lags</em> (2-4 months), and PR, paid and word-of-mouth move it too. So the strategy below pairs with a geo-holdout — see section 07 — to isolate social's share. With that caveat noted, the rest of this page does one thing: tailor the content so brand search actually goes up.</p>
</section>
"""

PROBLEM = """
<section id="problem" class="section">
  <p class="kicker">02 · The problem</p>
  <h2 class="section-title">Topic content lifts topic search. Not brand search.</h2>
  <p class="lede">This is the honest gap in the base strategy, and it is worth saying plainly before fixing it.</p>
  <p>Take "Canton Fair 2027: The Complete Playbook." It is good content. But walk the viewer's actual path: they finish the video more interested in <em>Canton Fair</em> — so they Google "Canton Fair 2027." They do not Google "WorldFirst." The content raised <strong>topic intent</strong>, not <strong>brand intent</strong>. Worse, it raised intent that every competitor also benefits from — you have grown the category, not the brand.</p>
  <p>This is the default failure mode of useful content marketing. Being <em>useful</em> earns attention; it does not, by itself, earn the brand search. A great explainer about a topic sends people to the topic. If brand search is the North Star, "make genuinely useful content" is necessary but nowhere near sufficient.</p>
  <p>The fix is not to make the content less useful. It is to change <em>where the value attaches</em> — so the thing the viewer wants more of is unmistakably WorldFirst's.</p>
</section>
"""

MECHANISM = """
<section id="mechanism" class="section">
  <p class="kicker">03 · The mechanism</p>
  <h2 class="section-title">Three ways content actually drives brand search.</h2>
  <p class="lede">Content lifts brand search only when WorldFirst is the gateway, the author, or the protagonist of the value — never just its publisher.</p>

  <div class="mech-grid">
    <div class="mech">
      <p class="mech-num">Mode 01</p>
      <h3>Gateway</h3>
      <p>The payoff of the content is a named, branded asset — a map, a tool, a calendar, a dataset. The video gives the teaser; the asset is the resolution; the brand is the only door to it. To get the thing, you search the brand.</p>
    </div>
    <div class="mech">
      <p class="mech-num">Mode 02</p>
      <h3>Author</h3>
      <p>The method, framework or check is named for and authored by WorldFirst. People do not search "how to check a supplier" — they search "the WorldFirst Supplier Check." The framework carries the brand wherever it travels.</p>
    </div>
    <div class="mech">
      <p class="mech-num">Mode 03</p>
      <h3>Protagonist</h3>
      <p>WorldFirst — or its named human, the China desk, the fraud desk — is <em>in</em> the story as the one who sees, knows, or solves. The authority belongs to the brand, not the topic. The viewer wants more of <em>that source</em>.</p>
    </div>
  </div>
  <p>Every piece in the re-tailored strategy has to run through at least one of these three modes. Useful-but-unattached content — the Canton Fair Playbook as originally framed — does not ship.</p>
</section>
"""

RULES = """
<section id="rules" class="section">
  <p class="kicker">04 · The rules</p>
  <h2 class="section-title">Six rules every piece must pass.</h2>
  <ol class="rules">
    <li><strong>Name the asset.</strong> Every tool, map, list, calendar or dataset gets a WorldFirst-branded name. The payoff is branded — to get it, you search the brand.</li>
    <li><strong>Own the method.</strong> Teach "the WorldFirst Supplier Check," never a generic "how to check a supplier." The framework is the brand's, and it carries the brand when shared.</li>
    <li><strong>Show the vantage.</strong> Lead with the proprietary position only WorldFirst has — "our China desk sees 12,000 supplier invoices a month." The authority is branded, not borrowed from the topic.</li>
    <li><strong>Build franchises.</strong> Recurring, named series — Trade Pulse, the Hall Map, the CNY Calendar — so people search the franchise, and the franchise contains the brand.</li>
    <li><strong>Give it a face.</strong> A named, recurring WorldFirst human. A face becomes a brand mnemonic; people search the person and the brand together.</li>
    <li><strong>Never let the topic travel alone.</strong> "Canton Fair" always arrives as "WorldFirst's Canton Fair Hall Map." Topic and brand become a single phrase in memory.</li>
  </ol>
</section>
"""

RETAILOR = f"""
<section id="retailor" class="section">
  <p class="kicker">05 · The re-tailoring</p>
  <h2 class="section-title">Same ideas, re-engineered.</h2>
  <p class="lede">Six pieces from the base strategy, before and after. The content is just as useful — the value simply attaches to WorldFirst instead of to the topic.</p>
  {pair_cards()}
</section>
"""

TEST = """
<section id="test" class="section">
  <p class="kicker">06 · The test</p>
  <h2 class="section-title">The brand-search test.</h2>
  <p class="lede">One question, asked before anything publishes. It is the publishing gate.</p>
  <div class="test-box">
    <p class="test-q">After seeing this, what does the viewer type into Google?</p>
    <div class="test-rows">
      <div class="test-row test-fail">
        <span class="test-verdict">FAILS</span>
        <p>If the honest answer is the topic — "Canton Fair", "supplier scams", "CNY rate" — the content grew the category, not the brand. Re-engineer it through one of the three modes.</p>
      </div>
      <div class="test-row test-pass">
        <span class="test-verdict">PASSES</span>
        <p>If the answer is "WorldFirst [something]" — "WorldFirst Canton Fair map", "WorldFirst Supplier Check" — the content attached the value to the brand. Ship it.</p>
      </div>
    </div>
  </div>
  <p>This is the discipline that makes brand search a reachable North Star instead of a hopeful one. The topic builds the category — useful, but shared with every competitor. Only the brand-attached search builds WorldFirst.</p>
</section>
"""

MEASURE = """
<section id="measure" class="section">
  <p class="kicker">07 · Measurement</p>
  <h2 class="section-title">How the lift is read — and why it is geo-focused.</h2>
  <p class="lede">A North Star is only useful if it is concentrated enough to move and clean enough to trust.</p>

  <h3 class="sub">What to track</h3>
  <p>Branded-query volume in Google Search Console and Google Trends. Two layers: the <strong>core</strong> — "worldfirst", "world first", "worldfirst account" — and the <strong>long-tail the content is designed to manufacture</strong> — "worldfirst canton fair map", "worldfirst supplier check", "worldfirst trade pulse". The long-tail is the cleanest proof of all: nobody types "worldfirst canton fair map" by accident. If that query exists at all, a specific piece of content created it.</p>

  <h3 class="sub">Why one region, not six</h3>
  <p>Brand search only moves as a <em>readable</em> signal if the spend is concentrated. Spread a budget across six markets and the lift is too thin to detect anywhere — you will have spent the money and learned nothing. Concentrate on one lead region (Malaysia), perhaps a second. One region also sets up a clean read: run the content in Malaysia, hold a comparable market dark, and compare the branded-search delta. That geo-holdout is what isolates social's contribution from PR, paid and word-of-mouth.</p>

  <div class="chart-wrap">
    <svg viewBox="0 0 520 240" xmlns="http://www.w3.org/2000/svg">
      <text x="20" y="22" font-family="JetBrains Mono" font-size="10" fill="#888">BRANDED SEARCH VOLUME · INDEXED TO BASELINE</text>
      <line x1="48" y1="200" x2="500" y2="200" stroke="#E5E0D5"/>
      <line x1="48" y1="40" x2="48" y2="200" stroke="#E5E0D5"/>
      <g font-family="JetBrains Mono" font-size="9" fill="#888">
        <text x="42" y="204" text-anchor="end">100</text>
        <text x="42" y="124" text-anchor="end">150</text>
        <text x="42" y="48" text-anchor="end">200</text>
      </g>
      <line x1="160" y1="40" x2="160" y2="200" stroke="#E5E0D5" stroke-dasharray="3 3"/>
      <text x="166" y="52" font-family="JetBrains Mono" font-size="9" fill="#888">content starts</text>
      <polyline points="48,200 104,199 160,200 216,184 272,160 328,132 384,108 440,86 496,72"
        fill="none" stroke="#E6185F" stroke-width="2.5"/>
      <polyline points="48,200 104,200 160,199 216,198 272,200 328,197 384,199 440,198 496,196"
        fill="none" stroke="#888" stroke-width="2" stroke-dasharray="4 3"/>
      <circle cx="496" cy="72" r="4" fill="#E6185F"/>
      <text x="488" y="64" text-anchor="end" font-family="JetBrains Mono" font-size="9" fill="#E6185F">focus region (Malaysia)</text>
      <text x="488" y="188" text-anchor="end" font-family="JetBrains Mono" font-size="9" fill="#888">holdout market</text>
    </svg>
  </div>
  <p class="chart-cap">The read: focus-region branded search, indexed to baseline, monthly. The gap between the two lines is social's isolated contribution.</p>

  <h3 class="sub">The honest reading</h3>
  <ul>
    <li><strong>Baseline first.</strong> Measure current branded-search volume in the focus region before any content runs. No baseline, no lift.</li>
    <li><strong>Expect a lag.</strong> Brand search responds 2-4 months after content, not the same week. Judge it on a quarter, not a post.</li>
    <li><strong>Watch the long-tail hardest.</strong> Core "worldfirst" volume is noisy. The branded long-tail — "worldfirst supplier check" — is the unambiguous proof the content is doing its job.</li>
    <li><strong>Don't over-gate.</strong> Engineering for brand search must not make the content worse. The brand is the souvenir, not a tollbooth — if the content is weak, attaching it to the brand just means nobody searches at all.</li>
  </ul>
</section>
"""

FOOTER = """
<footer class="site-footer">
  <p>WorldFirst · Internal · Content Strategy / Brand Search · May 2026 · <a href="#" id="lock">lock device</a></p>
</footer>
"""

INNER = HERO + NORTHSTAR + PROBLEM + MECHANISM + RULES + RETAILOR + TEST + MEASURE + FOOTER

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
.page-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:58px;line-height:1.03;letter-spacing:-.025em;margin-bottom:16px;}
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
/* mechanism */
.mech-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-bottom:18px;}
@media(max-width:760px){.mech-grid{grid-template-columns:1fr;}}
.mech{border:1px solid var(--line);border-radius:4px;padding:20px 22px;background:var(--paper);}
.mech-num{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--wf-pink);letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px;}
.mech h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:21px;margin-bottom:8px;}
.mech p{font-size:13.5px;color:var(--ink-soft);margin:0;}
/* rules */
.rules{list-style:none;counter-reset:r;padding:0;margin:0;max-width:740px;}
.rules li{counter-increment:r;position:relative;padding:14px 0 14px 44px;border-bottom:1px solid var(--line-soft);font-size:14.5px;color:var(--ink-soft);}
.rules li:last-child{border-bottom:none;}
.rules li::before{content:counter(r,decimal-leading-zero);position:absolute;left:0;top:14px;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--wf-pink);}
/* before/after */
.ba{margin-bottom:18px;border:1px solid var(--line);border-radius:4px;padding:20px 22px;background:var(--paper);}
.ba-tag{font-family:'JetBrains Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:.12em;color:var(--wf-pink);margin-bottom:14px;}
.ba-grid{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:stretch;}
@media(max-width:700px){.ba-grid{grid-template-columns:1fr;}.ba-arrow{display:none;}}
.ba-side{padding:14px 16px;border-radius:4px;}
.ba-old{background:var(--line-soft);}
.ba-new{background:#FFF1F5;border:1px solid var(--wf-pink-soft);}
.ba-label{font-family:'JetBrains Mono',monospace;font-size:9px;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-mute);margin-bottom:8px;}
.ba-title{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:16px;line-height:1.25;color:var(--ink);margin-bottom:10px;}
.ba-search{font-size:12px;color:var(--ink-soft);margin:0;}
.ba-q{font-family:'JetBrains Mono',monospace;font-size:11px;padding:2px 7px;border-radius:3px;display:inline-block;margin-top:3px;}
.ba-q-leak{background:#fff;border:1px solid var(--line);color:var(--ink-mute);}
.ba-q-win{background:var(--wf-pink);color:#fff;}
.ba-arrow{display:flex;align-items:center;color:var(--wf-pink);font-size:20px;}
.ba-why{font-size:13px;color:var(--ink-soft);margin:14px 0 0!important;padding-top:12px;border-top:1px solid var(--line-soft);}
.ba-why strong{color:var(--ink);}
/* test */
.test-box{border:1px solid var(--ink);border-radius:5px;padding:24px 26px;background:var(--paper);margin-bottom:16px;}
.test-q{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:21px;color:var(--ink);margin-bottom:18px!important;}
.test-rows{display:flex;flex-direction:column;gap:12px;}
.test-row{display:grid;grid-template-columns:80px 1fr;gap:14px;align-items:start;}
.test-verdict{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.06em;padding:5px 0;text-align:center;border-radius:3px;}
.test-fail .test-verdict{border:1px solid var(--ink-mute);color:var(--ink-mute);}
.test-pass .test-verdict{background:var(--wf-pink);color:#fff;}
.test-row p{font-size:13.5px;color:var(--ink-soft);margin:0;}
/* chart */
.chart-wrap{border:1px solid var(--line);border-radius:4px;padding:18px;background:var(--paper);margin:14px 0 8px;}
.chart-wrap svg{display:block;width:100%;height:auto;}
.chart-cap{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);margin-bottom:18px!important;}
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
    <p class="gate-subtitle">The content strategy, re-tailored.</p>
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
    <li><a href="#northstar">01 · The North Star</a></li>
    <li><a href="#problem">02 · The problem</a></li>
    <li><a href="#mechanism">03 · The mechanism</a></li>
    <li><a href="#rules">04 · Six rules</a></li>
    <li><a href="#retailor">05 · The re-tailoring</a></li>
    <li><a href="#test">06 · The brand-search test</a></li>
    <li><a href="#measure">07 · Measurement</a></li>
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
