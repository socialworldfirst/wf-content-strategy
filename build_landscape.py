#!/usr/bin/env python3
"""
WorldFirst Content Landscape — what the social content looks like under the
sourcing / cross-border-ecom insider positioning (newsroom model).
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
# Mockup builders
# ----------------------------------------------------------------------------
def tk_tiles():
    t = [
        ("On the Ground", "Walking Yiwu Market at 6am — what RM2 actually buys", "1.4M"),
        ("Sourcing Insiders", "A Yiwu agent: what I'd never buy from a trading company", "720K"),
        ("Importer Index", "We asked 500 importers their worst supplier story", "2.1M"),
        ("What Changed", "1688 just changed this — most importers haven't noticed", "380K"),
        ("On the Ground", "Inside the factory that makes your phone case", "910K"),
        ("Sourcing Insiders", "A forwarder: what really happens to your container", "540K"),
        ("Importer Index", "60% of you have hit this exact scam. Here it is.", "1.1M"),
        ("What Changed", "Canton Fair Phase 2 opened — the 3 halls that matter", "260K"),
        ("Community", "Drop your worst supplier red flag 👇 we're building the list", "430K"),
    ]
    return "\n".join(f"""<div class="tk-tile"><span class="tk-fr">{fr}</span>
      <p class="tk-tt">{title}</p><span class="tk-v">▶ {v}</span></div>""" for fr, title, v in t)

def ig_tiles():
    t = [
        ("Importer Index", "carousel", "We asked 500 importers where they source — the map"),
        ("On the Ground", "reel", "Walking Yiwu Market at 6am"),
        ("Importer Index", "carousel", "5 supplier scams, told by importers"),
        ("Sourcing Insiders", "reel", "A Shenzhen agent's 3 rules for first orders"),
        ("Everyday", "carousel", "How to read a Chinese quotation, line by line"),
        ("What Changed", "reel", "1688 just changed this"),
        ("Importer Index", "carousel", "Where 1,000 importers actually got burned"),
        ("Sourcing Insiders", "reel", "A QC inspector's fake-factory tells"),
        ("Everyday", "carousel", "The 12-point check before you pay a factory"),
    ]
    gl = {"carousel": "▤", "reel": "▶"}
    return "\n".join(f"""<div class="ig-tile"><span class="ig-k">{gl[k]}</span>
      <span class="ig-fr">{fr}</span><p class="ig-tt">{title}</p></div>""" for fr, k, title in t)

def yt_cards():
    v = [
        ("Sourcing Insiders", "A Yiwu Agent Answers Every Question You're Afraid to Ask", "340K views · 2 weeks ago", "28:14"),
        ("On the Ground", "48 Hours Inside Canton Fair", "510K views · 1 month ago", "19:02"),
        ("The Importer Index", "We Surveyed 1,000 SEA Importers: The State of Sourcing 2027", "220K views · 3 weeks ago", "15:47"),
        ("Global Sourcing Guide", "1688 vs Alibaba: The Real Difference", "680K views · 2 months ago", "13:30"),
        ("What Changed", "Everything That Changed in China Sourcing This Month", "95K views · 4 days ago", "11:08"),
    ]
    return "\n".join(f"""<div class="yt-card"><div class="yt-thumb"><span class="yt-fr">{fr}</span>
      <span class="yt-play">▶</span><span class="yt-dur">{dur}</span></div>
      <p class="yt-tt">{title}</p><p class="yt-m">{meta}</p></div>""" for fr, title, meta, dur in v)

TIKTOK_MOCK = f"""
<div class="phone-mock">
  <div class="phone"><div class="phone-notch"></div>
    <div class="phone-screen tk-screen">
      <div class="tk-status"><span>9:41</span><span>● ● ● ● 5G</span></div>
      <div class="tk-profile">
        <div class="tk-avatar">W</div>
        <p class="tk-handle">@worldfirst</p>
        <p class="tk-name">WorldFirst · Sourcing Insider</p>
        <div class="tk-stats"><span><strong>196</strong> Following</span><span><strong>284K</strong> Followers</span><span><strong>4.1M</strong> Likes</span></div>
        <p class="tk-bio">What's really happening in China sourcing. New to importing? Start here →</p>
        <div class="tk-follow">Follow</div>
      </div>
      <div class="tk-tabs"><span class="tk-tab-on">▦</span><span>↻</span><span>♡</span></div>
      <div class="tk-grid">{tk_tiles()}</div>
    </div>
  </div>
  <p class="mock-cap">TikTok — the discovery engine. Algorithmic reach pulls in importers who have never heard of WorldFirst.</p>
</div>
"""

IG_MOCK = f"""
<div class="phone-mock">
  <div class="phone"><div class="phone-notch"></div>
    <div class="phone-screen ig-screen">
      <div class="ig-top"><span class="ig-h">worldfirst ▾</span><span>＋  ☰</span></div>
      <div class="ig-prof"><div class="ig-avatar">W</div>
        <div class="ig-stats"><span><strong>361</strong><br>posts</span><span><strong>118K</strong><br>followers</span><span><strong>92</strong><br>following</span></div>
      </div>
      <p class="ig-name">WorldFirst · Sourcing Insider</p>
      <p class="ig-bio">The insider's read on China sourcing &amp; cross-border ecom.<br>We ask importers. We go to the factories. We tell you what changed.</p>
      <div class="ig-hl"><span>Yiwu</span><span>Insiders</span><span>The Index</span><span>Scams</span><span>Canton</span></div>
      <div class="ig-tabs"><span class="ig-tab-on">▦</span><span>▶</span><span>👤</span></div>
      <div class="ig-grid">{ig_tiles()}</div>
    </div>
  </div>
  <p class="mock-cap">Instagram — the Importer Index carousels get saved and forwarded; Reels cross-post from TikTok.</p>
</div>
"""

YOUTUBE_MOCK = f"""
<div class="yt-mock">
  <div class="yt-frame">
    <div class="yt-banner"><span class="yt-banner-t">THE SOURCING INSIDER</span></div>
    <div class="yt-head">
      <div class="yt-avatar">W</div>
      <div class="yt-cmeta">
        <p class="yt-cname">WorldFirst</p>
        <p class="yt-csub">@worldfirst · 284K subscribers</p>
        <p class="yt-cdesc">The insider's channel on sourcing from China and selling cross-border. Interviews, field trips, the Importer Index.</p>
      </div>
      <div class="yt-sub">Subscribe</div>
    </div>
    <p class="yt-row-l">Latest</p>
    <div class="yt-row">{yt_cards()}</div>
  </div>
  <p class="mock-cap">YouTube — depth and authority. The long-form insider interviews and the annual Importer Index.</p>
</div>
"""

LINKEDIN_MOCK = """
<div class="li-mock">
  <div class="li-post">
    <div class="li-head"><div class="li-logo">W</div>
      <div><p class="li-name">WorldFirst</p><p class="li-meta">31,402 followers · 2d · The Importer Index</p></div>
    </div>
    <p class="li-body">We asked 800 SEA importers what scared them most about sourcing in 2027.<br><br>It wasn't tariffs. It wasn't freight costs. <strong>62% said the same thing: supplier trust.</strong> They've each been burned at least once — and it shapes every decision after.<br><br>Full Importer Index breakdown ↓</p>
    <div class="li-chart">
      <svg viewBox="0 0 360 150" xmlns="http://www.w3.org/2000/svg">
        <text x="14" y="18" font-family="JetBrains Mono" font-size="9" fill="#888">"BIGGEST SOURCING WORRY, 2027" · 800 SEA IMPORTERS</text>
        <line x1="40" y1="124" x2="346" y2="124" stroke="#E5E0D5"/>
        <rect x="56"  y="34"  width="44" height="90" fill="#E6185F"/>
        <rect x="124" y="78"  width="44" height="46" fill="#E6185F" opacity="0.5"/>
        <rect x="192" y="90"  width="44" height="34" fill="#E6185F" opacity="0.4"/>
        <rect x="260" y="100" width="44" height="24" fill="#E6185F" opacity="0.3"/>
        <g font-family="Inter" font-size="9.5" fill="#1A1A1A" font-weight="500">
          <text x="78"  y="138" text-anchor="middle">Supplier trust</text>
          <text x="146" y="138" text-anchor="middle">Quality</text>
          <text x="214" y="138" text-anchor="middle">Freight</text>
          <text x="282" y="138" text-anchor="middle">Tariffs</text>
        </g>
        <g font-family="JetBrains Mono" font-size="9" fill="#1A1A1A">
          <text x="78"  y="28" text-anchor="middle">62%</text>
          <text x="146" y="72" text-anchor="middle">18%</text>
          <text x="214" y="84" text-anchor="middle">12%</text>
          <text x="282" y="94" text-anchor="middle">8%</text>
        </g>
      </svg>
    </div>
    <div class="li-eng"><span>👍 1,940</span><span>💬 212 comments</span><span>↻ 388 reposts</span></div>
  </div>
  <div class="li-post">
    <div class="li-head"><div class="li-logo">W</div>
      <div><p class="li-name">WorldFirst</p><p class="li-meta">31,402 followers · 5d</p></div>
    </div>
    <p class="li-body">We're running the 2027 Importer Index — the largest independent survey of Southeast Asian importers.<br><br>If you source from China: 2 minutes, link below. We publish everything, free. The more importers answer, the sharper the picture for all of us.</p>
    <div class="li-cta"><span class="li-cta-tag">COMMUNITY CALL</span><p class="li-cta-t">The 2027 Importer Index — take part</p></div>
    <div class="li-eng"><span>👍 624</span><span>💬 71 comments</span><span>↻ 154 reposts</span></div>
  </div>
  <p class="mock-cap">LinkedIn — the Importer Index data drops, and the community calls that source the next one.</p>
</div>
"""

# ----------------------------------------------------------------------------
# Franchise cards
# ----------------------------------------------------------------------------
FRANCHISES = [
    ("The Importer Index", "Community sensor network",
     "\"We asked [N] SEA importers…\" — recurring surveys of the audience itself, aggregated and published free. WorldFirst has no proprietary China desk; it doesn't need one. The moment you aggregate 500 importer answers, that aggregate is proprietary — built with a question, not a data operation. This is the brand-search engine: a named, citable, un-copyable franchise.",
     "Importer Index"),
    ("Sourcing Insiders", "Borrowed insiders",
     "Real China-side agents, forwarders, factory QC inspectors and veteran importers, on camera. WorldFirst doesn't claim to be the insider — it gives the real insiders a platform. Their credibility, WorldFirst's distribution and brand. Recurring named guests become recurring faces.",
     "Sourcing Insiders"),
    ("On the Ground", "Lightweight field capture",
     "POV field content — Yiwu Market at dawn, inside real factories, the Canton Fair floor. No standing operation: a creator and a trip, a few times a year. \"Insider\" here just means we were physically there, and the audience wasn't.",
     "On the Ground"),
    ("What Changed", "Synthesis of the scattered landscape",
     "Sourcing intelligence is fragmented across 1688, the forums, forwarder groups and the Chinese internet. Nobody consolidates it for the SEA importer. WorldFirst watches all of it and packages \"what changed this week and what it means for you.\" The vantage is coverage, not secret data.",
     "What Changed"),
]

def franchise_cards():
    out = []
    for i, (name, mech, desc, _) in enumerate(FRANCHISES, 1):
        out.append(f"""<article class="fr-card">
      <p class="fr-num">Franchise 0{i}</p>
      <h3>{name}</h3>
      <p class="fr-mech">Fed by: {mech}</p>
      <p>{desc}</p>
    </article>""")
    return "\n".join(out)

# ----------------------------------------------------------------------------
# Content
# ----------------------------------------------------------------------------
HERO = """
<header class="page-header">
  <p class="eyebrow">WorldFirst · Content Strategy · The Content Landscape</p>
  <h1 class="page-title">What it looks like.</h1>
  <p class="page-byline">WorldFirst as the sourcing and cross-border ecom insider — the social content landscape, platform by platform, built to reach new importers and lift brand search.</p>
  <p class="addendum-link"><a href="index.html">← Base strategy</a> &nbsp;·&nbsp; <a href="insider.html">The Insider direction</a> &nbsp;·&nbsp; <a href="brand-search.html">Brand-search evidence</a></p>
</header>
"""

POSITIONING = """
<section id="positioning" class="section">
  <p class="kicker">01 · The positioning</p>
  <h2 class="section-title">WorldFirst is the insider — and a newsroom, not a desk.</h2>
  <p class="lede">Long-term, WorldFirst owns one position: the insider on China sourcing and cross-border ecom. Not the company that sells payments — the one that knows the trade and says what's really going on.</p>
  <p>The earlier version of this assumed a proprietary "China desk" producing original intelligence. WorldFirst doesn't have one, and the payment data that could feed it is compliance-locked. So the model is corrected: <strong>WorldFirst runs a newsroom, not a desk.</strong> The intelligence already exists in the ecosystem — WorldFirst aggregates, edits and broadcasts it. Three sourcing mechanisms, none of which need data WorldFirst doesn't have:</p>
  <ul class="pos-mechs">
    <li><strong>The community as the sensor network.</strong> The audience is the desk. Ask 500 importers, aggregate, publish — and the aggregate is proprietary.</li>
    <li><strong>Borrowed insiders.</strong> Real China-side agents, forwarders and factory people, given a platform. Their credibility, WorldFirst's reach.</li>
    <li><strong>Synthesis of the scattered landscape.</strong> Watch the Chinese internet, 1688, the forums; package what changed for the SEA importer.</li>
  </ul>
  <p>And every piece in the landscape below is built to do four things at once: <strong>resonate</strong> with the core importer audience, be <strong>genuinely shareable</strong>, <strong>lift brand search</strong>, and <strong>reach new importers</strong> — not just serve existing customers.</p>
</section>
"""

FRANCHISES_SEC = f"""
<section id="franchises" class="section">
  <p class="kicker">02 · The franchises</p>
  <h2 class="section-title">Four named franchises carry the landscape.</h2>
  <p class="lede">The landscape isn't loose posts — it runs on four named, recurring franchises. Named, because the franchise name is itself the searchable asset, and a named show accrues brand equity every episode. Each franchise is fed by one of the three sourcing mechanisms.</p>
  <div class="fr-grid">
    {franchise_cards()}
  </div>
  <p class="fr-note">Each franchise is fronted by a face — a recurring WorldFirst host plus the borrowed insiders. Trust forms faster around a person than a logo, and a personal account outreaches a brand account roughly 2×.</p>
</section>
"""

def platform_sec(num, sid, kick, title, lead, points, mock):
    pts = "".join(f"<li>{p}</li>" for p in points)
    return f"""
<section id="{sid}" class="section">
  <p class="kicker">{num} · {kick}</p>
  <h2 class="section-title">{title}</h2>
  <p class="lede">{lead}</p>
  <ul class="role-points">{pts}</ul>
  {mock}
</section>
"""

TIKTOK_SEC = platform_sec("03", "tiktok", "The discovery engine", "TikTok — where new importers find WorldFirst.",
  "TikTok is the one platform built to reach people who have never heard of WorldFirst. The algorithm does the introducing — which is exactly the brief: reach new importers, not just serve existing customers.",
  ["Leads with On the Ground and Sourcing Insiders — POV field clips and real insider faces stop the scroll.",
   "Community prompts (\"drop your worst supplier red flag\") turn viewers into the sensor network.",
   "Every clip is framed as the importer's world, not WorldFirst's product — you don't need to be a customer to care.",
   "Cadence: 4-5 short videos a week."], TIKTOK_MOCK)

IG_SEC = platform_sec("04", "instagram", "The save-and-forward layer", "Instagram — where the Index gets shared.",
  "Instagram is where the considered importer goes deeper. The Importer Index carousels are built to be saved and forwarded importer-to-importer — the quiet shareability signal.",
  ["Leads with Importer Index carousels — numbered, data-led, screenshot-friendly.",
   "Reels cross-post from TikTok at near-zero extra cost.",
   "Highlights organise the franchises so a new follower sees the whole landscape at once.",
   "Cadence: TikTok mirror + 2-3 carousels a week."], IG_MOCK)

YT_SEC = platform_sec("05", "youtube", "Depth and authority", "YouTube — where the insider proves it.",
  "YouTube is where a serious importer goes to actually learn — and where WorldFirst proves the short-form brand has real substance. Long-form interviews and the annual Importer Index live here.",
  ["Leads with full Sourcing Insiders interviews and On the Ground deep dives.",
   "The annual Importer Index report becomes a flagship long-form film — the most citable asset of the year.",
   "Shorts cut down from the long-form and from TikTok keep the channel active daily.",
   "Cadence: 2 long-form a month, Shorts continuous."], YOUTUBE_MOCK)

LI_SEC = platform_sec("06", "linkedin", "Authority and the community call", "LinkedIn — where the Index is published and refilled.",
  "LinkedIn reaches the importer as a business owner, plus the wider trade industry. It is the home of the Importer Index data drops — and the community calls that source the next one.",
  ["Leads with The Importer Index — data posts that get cited, screenshotted and reposted.",
   "Community-call posts recruit importers into the next survey: the sensor network refilling itself.",
   "Sourcing Insiders quote-clips position WorldFirst alongside credible voices.",
   "Cadence: 3 posts a week."], LINKEDIN_MOCK)

WHY = """
<section id="why" class="section">
  <p class="kicker">07 · Why it works</p>
  <h2 class="section-title">Resonance, shareability, brand search, new reach.</h2>
  <p class="lede">The four things every piece had to do — and how the landscape delivers each.</p>

  <div class="why-grid">
    <div class="why">
      <p class="why-n">01</p>
      <h3>It resonates with the core audience</h3>
      <p>The content is the importer's world — Yiwu, suppliers, scams, what changed on 1688 — not WorldFirst's product. An importer cares about this whether or not they're a customer. That is the only way content earns a stranger's attention.</p>
    </div>
    <div class="why">
      <p class="why-n">02</p>
      <h3>It's genuinely shareable</h3>
      <p>Community participation, scam reveals, counterintuitive Index data, POV field clips — every shareability trigger from the SEA research. Importers forward this into their supplier WhatsApp groups because it's useful to the person they send it to.</p>
    </div>
    <div class="why">
      <p class="why-n">03</p>
      <h3>It lifts brand search</h3>
      <p>Named, recurring franchises are searchable assets. The Importer Index is a citable, un-copyable, proprietary-data franchise. Consistent faces and distinctive formats make WorldFirst recognisable in 1.5 seconds — no name-stamping needed.</p>
    </div>
    <div class="why">
      <p class="why-n">04</p>
      <h3>It reaches new audiences</h3>
      <p>Discovery-first. TikTok and Reels are algorithmic — they put WorldFirst in front of importers who have never heard of it. The content needs no prior relationship with WorldFirst to be worth watching. It grows the audience, it doesn't just service it.</p>
    </div>
  </div>

  <h3 class="sub">And the secondary layer</h3>
  <p>WhatsApp sits underneath the landscape as the alert surface for the already-warm — triggered scam warnings and holiday payment deadlines, never a daily feed. It is where the audience the four franchises built gets kept. Discovery happens on TikTok; the relationship is kept on WhatsApp; the product converts it.</p>
</section>
"""

FOOTER = """
<footer class="site-footer">
  <p>WorldFirst · Internal · Content Landscape · May 2026 · <a href="#" id="lock">lock device</a></p>
</footer>
"""

INNER = HERO + POSITIONING + FRANCHISES_SEC + TIKTOK_SEC + IG_SEC + YT_SEC + LI_SEC + WHY + FOOTER

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
.wrap{display:grid;grid-template-columns:230px minmax(0,1fr);gap:56px;max-width:1200px;margin:0 auto;padding:56px 44px 120px;}
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
.page-byline{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:21px;color:var(--ink-soft);max-width:640px;margin-bottom:18px;}
.addendum-link{font-family:'JetBrains Mono',monospace;font-size:12px;}
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
.pos-mechs li{margin-bottom:9px;}
/* franchises */
.fr-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:14px;}
@media(max-width:700px){.fr-grid{grid-template-columns:1fr;}}
.fr-card{border:1px solid var(--line);border-radius:4px;padding:22px 24px;background:var(--paper);}
.fr-num{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--wf-pink);letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px;}
.fr-card h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:23px;letter-spacing:-.01em;margin-bottom:4px;}
.fr-mech{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);text-transform:uppercase;letter-spacing:.04em;margin-bottom:10px!important;}
.fr-card p{font-size:13.5px;color:var(--ink-soft);margin:0;}
.fr-note{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);line-height:1.65;}
/* role points */
.role-points{margin-bottom:28px!important;}
.role-points li{font-size:14.5px;color:var(--ink-soft);}
.mock-cap{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);text-align:center;margin-top:14px!important;text-transform:uppercase;letter-spacing:.06em;max-width:none!important;}
/* phone */
.phone-mock{display:flex;flex-direction:column;align-items:center;}
.phone{width:300px;background:#0d0d0d;border-radius:30px;padding:8px;position:relative;box-shadow:0 16px 44px rgba(0,0,0,.16);}
.phone-notch{position:absolute;top:10px;left:50%;transform:translateX(-50%);width:90px;height:18px;background:#0d0d0d;border-radius:0 0 14px 14px;z-index:3;}
.phone-screen{border-radius:24px;overflow:hidden;height:610px;overflow-y:auto;}
/* tiktok */
.tk-screen{background:#000;color:#fff;}
.tk-status{display:flex;justify-content:space-between;padding:12px 18px 6px;font-family:'JetBrains Mono',monospace;font-size:9px;color:rgba(255,255,255,.5);}
.tk-profile{text-align:center;padding:8px 18px 12px;}
.tk-avatar{width:62px;height:62px;border-radius:50%;background:linear-gradient(135deg,#E6185F,#001E5C);margin:0 auto 8px;display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:28px;}
.tk-handle{font-size:14px;font-weight:600;}
.tk-name{font-size:11px;color:rgba(255,255,255,.55);margin-bottom:9px;}
.tk-stats{display:flex;justify-content:center;gap:15px;font-size:10px;color:rgba(255,255,255,.55);margin-bottom:9px;}
.tk-stats strong{color:#fff;font-size:13px;}
.tk-bio{font-size:11px;color:rgba(255,255,255,.8);line-height:1.5;margin-bottom:9px;}
.tk-follow{background:#E6185F;font-size:12px;font-weight:600;padding:8px 0;border-radius:4px;margin:0 44px;}
.tk-tabs{display:flex;justify-content:space-around;padding:9px 0;border-bottom:1px solid rgba(255,255,255,.12);font-size:13px;color:rgba(255,255,255,.4);}
.tk-tab-on{color:#fff;}
.tk-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px;}
.tk-tile{position:relative;aspect-ratio:9/15;background:linear-gradient(165deg,#241019,#0c0c0c);padding:8px 7px;display:flex;flex-direction:column;justify-content:flex-end;}
.tk-fr{position:absolute;top:6px;left:6px;font-family:'JetBrains Mono',monospace;font-size:7.5px;color:var(--wf-pink);}
.tk-tt{font-size:9.5px;line-height:1.3;color:#fff;font-weight:500;margin-bottom:4px;}
.tk-v{font-family:'JetBrains Mono',monospace;font-size:8px;color:rgba(255,255,255,.6);}
/* instagram */
.ig-screen{background:#fff;color:#1a1a1a;}
.ig-top{display:flex;justify-content:space-between;padding:14px 16px 8px;font-size:13px;}
.ig-h{font-weight:700;}
.ig-prof{display:flex;align-items:center;gap:20px;padding:8px 16px;}
.ig-avatar{width:62px;height:62px;border-radius:50%;background:linear-gradient(135deg,#E6185F,#001E5C);display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:28px;color:#fff;flex-shrink:0;}
.ig-stats{display:flex;gap:18px;font-size:12px;text-align:center;}
.ig-stats strong{font-size:14px;}
.ig-name{font-size:12px;font-weight:600;padding:4px 16px 0;}
.ig-bio{font-size:12px;color:#444;padding:2px 16px 8px;line-height:1.5;}
.ig-hl{display:flex;gap:8px;padding:4px 16px 12px;overflow-x:auto;}
.ig-hl span{flex-shrink:0;font-size:9px;color:#444;border:1px solid var(--line);border-radius:100px;padding:5px 10px;}
.ig-tabs{display:flex;justify-content:space-around;padding:8px 0;border-top:1px solid #eee;font-size:13px;color:#bbb;}
.ig-tab-on{color:#1a1a1a;}
.ig-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px;}
.ig-tile{position:relative;aspect-ratio:1;background:var(--line-soft);padding:9px 8px;display:flex;align-items:flex-end;}
.ig-k{position:absolute;top:6px;right:7px;font-size:11px;color:var(--ink-mute);}
.ig-fr{position:absolute;top:6px;left:7px;font-family:'JetBrains Mono',monospace;font-size:7.5px;color:var(--wf-pink);}
.ig-tt{font-size:10px;line-height:1.32;color:var(--ink);font-weight:500;}
/* youtube */
.yt-mock{display:flex;flex-direction:column;align-items:center;}
.yt-frame{width:100%;max-width:680px;background:var(--paper);border:1px solid var(--line);border-radius:6px;overflow:hidden;}
.yt-banner{height:80px;background:linear-gradient(110deg,#001E5C,#E6185F);display:flex;align-items:center;justify-content:center;}
.yt-banner-t{font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.3em;color:rgba(255,255,255,.9);}
.yt-head{display:flex;gap:16px;align-items:center;padding:18px 22px;border-bottom:1px solid var(--line);}
.yt-avatar{width:58px;height:58px;border-radius:50%;background:linear-gradient(135deg,#E6185F,#001E5C);display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:26px;color:#fff;flex-shrink:0;}
.yt-cname{font-family:'Fraunces',serif;font-weight:500;font-size:21px;}
.yt-csub{font-size:12px;color:var(--ink-mute);margin:2px 0;}
.yt-cdesc{font-size:12.5px;color:var(--ink-soft);}
.yt-sub{margin-left:auto;background:var(--ink);color:#fff;font-size:12px;font-weight:600;padding:9px 16px;border-radius:100px;align-self:center;}
.yt-row-l{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.1em;padding:16px 22px 10px;}
.yt-row{display:flex;gap:12px;overflow-x:auto;padding:0 22px 22px;}
.yt-card{width:188px;flex-shrink:0;}
.yt-thumb{aspect-ratio:16/9;background:linear-gradient(150deg,#241019,#0c0c0c);border-radius:4px;position:relative;display:flex;align-items:center;justify-content:center;margin-bottom:7px;}
.yt-fr{position:absolute;top:6px;left:7px;font-family:'JetBrains Mono',monospace;font-size:8px;color:var(--wf-pink);}
.yt-play{color:rgba(255,255,255,.55);font-size:20px;}
.yt-dur{position:absolute;bottom:5px;right:6px;background:rgba(0,0,0,.8);color:#fff;font-family:'JetBrains Mono',monospace;font-size:8px;padding:2px 4px;border-radius:2px;}
.yt-tt{font-size:12.5px;font-weight:600;line-height:1.32;margin-bottom:3px;}
.yt-m{font-size:11px;color:var(--ink-mute);}
/* linkedin */
.li-mock{display:flex;flex-direction:column;align-items:center;gap:16px;}
.li-post{width:100%;max-width:520px;background:var(--paper);border:1px solid var(--line);border-radius:6px;padding:18px 20px;}
.li-head{display:flex;gap:11px;align-items:center;margin-bottom:12px;}
.li-logo{width:46px;height:46px;border-radius:5px;background:linear-gradient(135deg,#E6185F,#001E5C);display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:22px;color:#fff;}
.li-name{font-size:14px;font-weight:600;}
.li-meta{font-size:11.5px;color:var(--ink-mute);}
.li-body{font-size:14px;color:var(--ink);margin-bottom:12px;line-height:1.55;}
.li-chart{background:var(--line-soft);border-radius:4px;padding:12px;margin-bottom:12px;}
.li-chart svg{display:block;width:100%;height:auto;}
.li-cta{background:linear-gradient(150deg,#2a0f1d,#0c0c0c);border-radius:4px;padding:24px 22px;margin-bottom:12px;}
.li-cta-tag{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.1em;color:rgba(255,255,255,.5);}
.li-cta-t{font-family:'Fraunces',serif;font-weight:500;font-size:19px;color:#fff;margin-top:8px;}
.li-eng{display:flex;gap:16px;padding-top:10px;border-top:1px solid var(--line-soft);font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);}
/* why grid */
.why-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:14px;}
@media(max-width:700px){.why-grid{grid-template-columns:1fr;}}
.why{border:1px solid var(--line);border-radius:4px;padding:20px 22px;background:var(--paper);}
.why-n{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--wf-pink);margin-bottom:8px;}
.why h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:19px;line-height:1.2;margin-bottom:8px;}
.why p{font-size:13.5px;color:var(--ink-soft);margin:0;}
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
<title>WorldFirst Content Landscape</title>
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
    <h1 class="gate-title">Content Landscape</h1>
    <p class="gate-subtitle">The sourcing insider, platform by platform.</p>
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
    <li><a href="#positioning">01 · The positioning</a></li>
    <li><a href="#franchises">02 · The franchises</a></li>
    <li><a href="#tiktok">03 · TikTok</a></li>
    <li><a href="#instagram">04 · Instagram</a></li>
    <li><a href="#youtube">05 · YouTube</a></li>
    <li><a href="#linkedin">06 · LinkedIn</a></li>
    <li><a href="#why">07 · Why it works</a></li>
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
(ROOT / "landscape.html").write_text(HTML, encoding="utf-8")
print(f"Wrote landscape.html ({len(HTML):,} bytes; {len(INNER):,} inner)")
