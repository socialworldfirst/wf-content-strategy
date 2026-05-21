#!/usr/bin/env python3
"""
WorldFirst Content Strategy — single-page HTML with platform mockups.
Encrypts inner content with 'wf' (PBKDF2 + AES-GCM).
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
    salt = os.urandom(16)
    iv = os.urandom(12)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITERATIONS)
    key = kdf.derive(password.encode("utf-8"))
    ct = AESGCM(key).encrypt(iv, plaintext.encode("utf-8"), None)
    return {"v": 1,
            "salt": base64.b64encode(salt).decode("ascii"),
            "iv": base64.b64encode(iv).decode("ascii"),
            "iterations": ITERATIONS,
            "ciphertext": base64.b64encode(ct).decode("ascii")}

# ============================================================================
# MOCKUPS
# ============================================================================

def tiktok_tiles():
    tiles = [
        ("5 words a real supplier never says", "220K", "P3"),
        ("Walking Canton Fair at 8am — what RM2 buys", "1.2M", "P1"),
        ("Your bank's CNY rate vs the real one", "89K", "P2"),
        ("Sample perfect. Bulk trash. RM17K gone.", "640K", "P3"),
        ("Why suppliers want you OFF Alibaba", "312K", "P1"),
        ("The 30-second check before you pay a factory", "156K", "P3"),
        ("1688 vs Alibaba — the real difference", "410K", "P1"),
        ("CNY closes Friday. Your last safe pay date.", "78K", "P2"),
        ("Found a Shopee bestseller on 1688 for ¼", "880K", "P1"),
    ]
    out = []
    for title, views, pillar in tiles:
        out.append(f"""<div class="tk-tile">
          <span class="tk-pillar">{pillar}</span>
          <p class="tk-tile-title">{title}</p>
          <span class="tk-views">▶ {views}</span>
        </div>""")
    return "\n".join(out)

TIKTOK_MOCK = f"""
<div class="phone-mock">
  <div class="phone">
    <div class="phone-notch"></div>
    <div class="phone-screen tk-screen">
      <div class="tk-statusbar"><span>9:41</span><span>● ● ● ● 5G</span></div>
      <div class="tk-profile">
        <div class="tk-avatar">W</div>
        <p class="tk-handle">@worldfirst</p>
        <p class="tk-name">WorldFirst</p>
        <div class="tk-stats">
          <span><strong>142</strong> Following</span>
          <span><strong>38.4K</strong> Followers</span>
          <span><strong>510K</strong> Likes</span>
        </div>
        <p class="tk-bio">Cross-border sourcing + payments for SEA importers. Pay China suppliers safe →</p>
        <div class="tk-followbtn">Follow</div>
      </div>
      <div class="tk-tabs"><span class="tk-tab-active">▦</span><span>↻</span><span>♡</span></div>
      <div class="tk-grid">
        {tiktok_tiles()}
      </div>
    </div>
  </div>
  <p class="mock-cap">The WorldFirst TikTok profile — a scrolling importer meets the brand here first.</p>
</div>
"""

def ig_tiles():
    tiles = [
        ("12 red flags in a supplier PI", "carousel", "P3"),
        ("Walking Yiwu Market", "reel", "P1"),
        ("How to read a Chinese quotation", "carousel", "P1"),
        ("73% of CNY payments landed same-day", "card", "P4"),
        ("5 words a supplier never says", "reel", "P3"),
        ("CNY 2027 — every payment date you need", "carousel", "P2"),
        ("Sample-to-bulk QC checklist", "carousel", "P1"),
        ("“I lost RM87,000” — a customer story", "reel", "P3"),
        ("What your bank's rate really costs", "card", "P2"),
    ]
    glyph = {"carousel": "▤", "reel": "▶", "card": "▣"}
    out = []
    for title, kind, pillar in tiles:
        out.append(f"""<div class="ig-tile">
          <span class="ig-kind">{glyph[kind]}</span>
          <span class="ig-pillar">{pillar}</span>
          <p class="ig-tile-title">{title}</p>
        </div>""")
    return "\n".join(out)

IG_MOCK = f"""
<div class="phone-mock">
  <div class="phone">
    <div class="phone-notch"></div>
    <div class="phone-screen ig-screen">
      <div class="ig-topbar"><span class="ig-handle-top">worldfirst ▾</span><span>＋  ☰</span></div>
      <div class="ig-profile">
        <div class="ig-avatar">W</div>
        <div class="ig-stats">
          <span><strong>312</strong><br>posts</span>
          <span><strong>47.1K</strong><br>followers</span>
          <span><strong>88</strong><br>following</span>
        </div>
      </div>
      <p class="ig-name">WorldFirst · Sourcing &amp; Payments</p>
      <p class="ig-bio">Source smarter. Pay China safe. Don't get burned.<br>SEA importers + ecommerce sellers.</p>
      <div class="ig-highlights">
        <span>Sourcing</span><span>Scams</span><span>CNY</span><span>Rates</span><span>Stories</span>
      </div>
      <div class="ig-tabs"><span class="ig-tab-active">▦</span><span>▶</span><span>👤</span></div>
      <div class="ig-grid">
        {ig_tiles()}
      </div>
    </div>
  </div>
  <p class="mock-cap">The Instagram grid — carousels get saved and forwarded; Reels cross-post from TikTok.</p>
</div>
"""

def yt_cards():
    vids = [
        ("The Real Cost of Paying Chinese Suppliers Wrong", "142K views · 3 weeks ago", "14:02"),
        ("Canton Fair 2027: The Complete Playbook", "308K views · 1 month ago", "17:38"),
        ("1688 Ultimate Guide for Southeast Asian Importers", "521K views · 2 months ago", "21:10"),
        ("How to Spot a Fake Supplier in 10 Minutes", "197K views · 1 month ago", "11:46"),
        ("Paying Suppliers Safely: Every Method Compared", "88K views · 5 days ago", "13:21"),
    ]
    out = []
    for title, meta, dur in vids:
        out.append(f"""<div class="yt-card">
          <div class="yt-thumb"><span class="yt-play">▶</span><span class="yt-dur">{dur}</span></div>
          <p class="yt-title">{title}</p>
          <p class="yt-meta">{meta}</p>
        </div>""")
    return "\n".join(out)

YOUTUBE_MOCK = f"""
<div class="yt-mock">
  <div class="yt-frame">
    <div class="yt-banner"><span class="yt-banner-txt">GLOBAL SOURCING GUIDE</span></div>
    <div class="yt-header">
      <div class="yt-avatar">W</div>
      <div class="yt-channel-meta">
        <p class="yt-channel-name">WorldFirst</p>
        <p class="yt-channel-sub">@worldfirst · 38.4K subscribers · 312 videos</p>
        <p class="yt-channel-desc">The Global Sourcing Guide — how to source from China and pay suppliers safely.</p>
      </div>
      <div class="yt-subbtn">Subscribe</div>
    </div>
    <p class="yt-row-label">Global Sourcing Guide — latest</p>
    <div class="yt-row">
      {yt_cards()}
    </div>
  </div>
  <p class="mock-cap">The YouTube channel — long-form depth, and where WorldFirst proves it is an authority.</p>
</div>
"""

LINKEDIN_MOCK = """
<div class="li-mock">
  <div class="li-post">
    <div class="li-head">
      <div class="li-logo">W</div>
      <div>
        <p class="li-name">WorldFirst</p>
        <p class="li-meta">24,108 followers · 2d</p>
      </div>
    </div>
    <p class="li-body"><strong>73% of CNY supplier payments via WorldFirst landed same-day in May</strong> — a 12-point jump on the same month last year. The China corridor is getting materially faster for SEA importers. Full Trade Pulse breakdown in comments.</p>
    <div class="li-chart">
      <svg viewBox="0 0 360 150" xmlns="http://www.w3.org/2000/svg">
        <text x="14" y="18" font-family="JetBrains Mono" font-size="9" fill="#888">% SAME-DAY LANDING · MAY 2026</text>
        <line x1="40" y1="124" x2="346" y2="124" stroke="#E5E0D5"/>
        <rect x="58"  y="40"  width="46" height="84" fill="#E6185F"/>
        <rect x="128" y="30"  width="46" height="94" fill="#E6185F"/>
        <rect x="198" y="66"  width="46" height="58" fill="#E6185F" opacity="0.55"/>
        <rect x="268" y="86"  width="46" height="38" fill="#E6185F" opacity="0.35"/>
        <g font-family="Inter" font-size="10" fill="#1A1A1A" font-weight="500">
          <text x="81"  y="138" text-anchor="middle">MY</text>
          <text x="151" y="138" text-anchor="middle">SG</text>
          <text x="221" y="138" text-anchor="middle">TH</text>
          <text x="291" y="138" text-anchor="middle">VN</text>
        </g>
        <g font-family="JetBrains Mono" font-size="9" fill="#1A1A1A">
          <text x="81"  y="34" text-anchor="middle">73%</text>
          <text x="151" y="24" text-anchor="middle">81%</text>
          <text x="221" y="60" text-anchor="middle">49%</text>
          <text x="291" y="80" text-anchor="middle">33%</text>
        </g>
      </svg>
    </div>
    <div class="li-engage"><span>👍 412</span><span>💬 38 comments</span><span>↻ 64 reposts</span></div>
  </div>

  <div class="li-post">
    <div class="li-head">
      <div class="li-logo">W</div>
      <div>
        <p class="li-name">WorldFirst</p>
        <p class="li-meta">24,108 followers · 5d</p>
      </div>
    </div>
    <p class="li-body">An importer messaged us last week. She'd paid a 30% deposit to a factory she'd worked with twice before. Then the supplier "updated" their bank details — to a personal account.<br><br>Here's the 4-step check that would have caught it 👇</p>
    <div class="li-carousel">
      <span class="li-car-tag">CAROUSEL · 6 slides</span>
      <p class="li-car-title">The deposit-redirect scam — and the 4 checks that stop it</p>
    </div>
    <div class="li-engage"><span>👍 1,204</span><span>💬 91 comments</span><span>↻ 233 reposts</span></div>
  </div>
  <p class="mock-cap">LinkedIn — the Trade Desk pillar and customer proof, framed for the importer as a business owner.</p>
</div>
"""

WHATSAPP_MOCK = """
<div class="wac-mock">
  <div class="wac-frame">
    <div class="wac-header">
      <div class="wac-avatar">W</div>
      <div class="wac-meta">
        <p class="wac-name">WorldFirst <span class="wac-verified">✓</span></p>
        <p class="wac-sub">2,418 followers</p>
      </div>
      <button class="wac-follow">Following</button>
    </div>
    <p class="wac-desc">Rate moves and supplier-payment deadlines that actually matter. No daily noise — only when it counts.</p>
    <div class="wac-posts">
      <div class="wac-post">
        <p class="wac-post-meta">Today · 09:10</p>
        <p class="wac-post-text">⚠️ <strong>CNY → MYR moved +1.8% this week.</strong> If you have a supplier payment pending, today's a better-than-usual window. <span class="wac-link">check your rate →</span></p>
        <p class="wac-react">👍 64   🔥 22</p>
      </div>
      <div class="wac-post">
        <p class="wac-post-meta">Mon · 14:30</p>
        <p class="wac-post-text"><strong>Heads up — Chinese factories close for CNY on Fri 5 Feb.</strong> Last safe day to send a supplier payment via WorldFirst for pre-holiday landing: <strong>Tue 2 Feb.</strong> Save this.</p>
        <p class="wac-react">👍 118   🔥 41   💡 27</p>
      </div>
      <div class="wac-post">
        <p class="wac-post-meta">Fri · 10:05</p>
        <p class="wac-post-text">Voice note from Lin, China desk — the supplier scam doing the rounds this week and the one line that gives it away.</p>
        <div class="wac-voice">▶ 0:00 ▬▬▬▬▬▬▬▬▬ 1:12</div>
        <p class="wac-react">👍 156   ❤️ 38</p>
      </div>
    </div>
  </div>
  <p class="mock-cap">WhatsApp Channel — secondary, and an alert surface, not a daily feed. Sparse by design.</p>
</div>
"""

# ============================================================================
# CONTENT
# ============================================================================

HERO = """
<header class="page-header">
  <p class="eyebrow">WorldFirst · Content Strategy · May 2026</p>
  <h1 class="page-title">The content, by platform.</h1>
  <p class="page-byline">A social-first content strategy for WorldFirst — the pillars, the formats, and what each channel actually looks like to the importer scrolling it.</p>
  <div class="meta-row">
    <span class="meta-pill"><span class="meta-label">Scope</span><span class="meta-val">Social-first · SEO excluded</span></span>
    <span class="meta-pill"><span class="meta-label">Audience</span><span class="meta-val">SEA cross-border importers + ecom sellers</span></span>
    <span class="meta-pill"><span class="meta-label">Job</span><span class="meta-val">Discovery · authority · FX-intent capture</span></span>
  </div>
</header>
"""

BRIEF = """
<section id="brief" class="section">
  <p class="kicker">01 · The brief</p>
  <h2 class="section-title">What content marketing's job actually is now.</h2>
  <p class="lede">The strategy work this builds on reached one hard conclusion: a daily content channel — the thing people go to and depend on — is the squeezed middle. It loses to personalised, real-time, embedded answers. So content marketing is not the product.</p>
  <p>That doesn't kill content marketing. It sharpens its job. WorldFirst content marketing has three jobs, and only three:</p>
  <ul class="brief-jobs">
    <li><strong>Discovery.</strong> Be the thing a SEA importer scrolls past on TikTok at lunch and stops for.</li>
    <li><strong>Authority.</strong> Be the brand that obviously understands cross-border sourcing and payments better than anyone else in the feed.</li>
    <li><strong>Intent capture.</strong> Catch the importer at the moment sourcing or FX is on their mind, and route that intent to WorldFirst.</li>
  </ul>
  <p>It does <em>not</em> try to be the daily habit or the utility people rely on — that belongs embedded in the product. Content earns attention and trust, then hands off. Content earns; product keeps.</p>
  <p><strong>Scope.</strong> Social-first. SEO content is deliberately excluded here. Primary platforms: TikTok, Instagram, YouTube, LinkedIn. Secondary: WhatsApp Channel and email. Every piece is framed importer-side — "what this means for your next supplier payment" — never as market commentary for speculators.</p>
</section>
"""

PILLARS = """
<section id="pillars" class="section">
  <p class="kicker">02 · The pillars</p>
  <h2 class="section-title">Four content pillars.</h2>
  <p class="lede">Everything WorldFirst publishes sits in one of four pillars. Three earn the audience; one earns the brand its authority.</p>

  <div class="pillars">
    <article class="pillar">
      <p class="pillar-num">Pillar 01</p>
      <h3>Source Smarter</h3>
      <p class="pillar-what">The how-to-import engine.</p>
      <p>Finding real factories, reading a PI, MOQ negotiation, QC before you pay, 1688 vs Alibaba, navigating Canton Fair and Yiwu. The highest-volume pillar — the genuinely useful content that earns the audience the right to be marketed to. The social-first extension of the Global Sourcing Guide.</p>
      <p class="pillar-leans">Leans on: TikTok · YouTube · Instagram</p>
    </article>
    <article class="pillar">
      <p class="pillar-num">Pillar 02</p>
      <h3>Move Money Right</h3>
      <p class="pillar-what">Cross-border payments and FX — importer-framed.</p>
      <p>What your bank's rate actually costs you. CNY payment timing and holiday windows. Same-day payments. FX margin in plain numbers. Forwards without the jargon. This is the pillar that captures FX intent at the top of the funnel and routes it to the WorldFirst product — never market commentary.</p>
      <p class="pillar-leans">Leans on: TikTok · Instagram · LinkedIn</p>
    </article>
    <article class="pillar">
      <p class="pillar-num">Pillar 03</p>
      <h3>Don't Get Burned</h3>
      <p class="pillar-what">Trust, scams, and safety.</p>
      <p>Supplier scams, payment fraud, WhatsApp impersonation, fake forwarders, the "pay my personal Alipay" red flag, deposit-and-disappear stories. The highest-anxiety, highest-shared territory in the SEA importer world — and brand-positive for a payments company to own.</p>
      <p class="pillar-leans">Leans on: TikTok · Instagram · YouTube</p>
    </article>
    <article class="pillar">
      <p class="pillar-num">Pillar 04</p>
      <h3>The Trade Desk</h3>
      <p class="pillar-what">Data and authority.</p>
      <p>WorldFirst sits on cross-border payment data nobody else has — corridor volumes, what SEA is importing, FX volatility, scam patterns blocked. Published as clean single-chart posts and a periodic Trade Pulse. Lowest volume, highest credibility — the pillar that makes serious operators and journalists take WorldFirst seriously.</p>
      <p class="pillar-leans">Leans on: LinkedIn · then everything as derivatives</p>
    </article>
  </div>
  <p class="pillar-note">Customer proof — anonymised, real, numbers-led stories — is not a fifth pillar. It is a treatment that runs through all four, strongest in Pillar 03.</p>
</section>
"""

FORMATS = """
<section id="formats" class="section">
  <p class="kicker">03 · The format system</p>
  <h2 class="section-title">One idea, every format.</h2>
  <p class="lede">Every piece starts as one idea — one supplier red flag, one data point, one story. It is then cut into platform-native formats. One idea, one production effort, every platform.</p>

  <div class="fmt-cols">
    <div class="fmt-col">
      <h3>Video</h3>
      <ul>
        <li><strong>Talking-head explainer</strong> — 45-90s, one insight to camera. Backbone of Pillars 1 + 2.</li>
        <li><strong>On-location POV</strong> — 45-90s, walking Canton Fair, Yiwu, a factory floor. The discovery magnet.</li>
        <li><strong>Annotated reveal</strong> — 30-60s, a real anonymised PI or scam screenshot, marked up. The engine of Pillar 3.</li>
        <li><strong>China-desk voice</strong> — a named WorldFirst expert, recurring face, builds trust across pillars.</li>
        <li><strong>Long-form</strong> — 10-15min YouTube, the Global Sourcing Guide deep dives.</li>
      </ul>
    </div>
    <div class="fmt-col">
      <h3>Image / static</h3>
      <ul>
        <li><strong>Carousel</strong> — numbered, swipeable, "save this." The workhorse for IG + LinkedIn.</li>
        <li><strong>Insight card</strong> — one stat or one rule, single image. Screenshot-bait.</li>
        <li><strong>Annotated screenshot</strong> — the visual signature of Pillar 3.</li>
        <li><strong>Data chart card</strong> — Trade Pulse. LinkedIn-led.</li>
        <li><strong>Calendar / window poster</strong> — CNY and holiday payment dates. Cyclical, Pillar 2.</li>
      </ul>
    </div>
    <div class="fmt-col">
      <h3>Post / text</h3>
      <ul>
        <li><strong>Customer story</strong> — anonymised, real, numbers-led. Proof across all pillars.</li>
        <li><strong>POV / hot take</strong> — LinkedIn thought-leadership, a senior or founder voice.</li>
        <li><strong>Quick tip</strong> — one-line utility, high frequency, low cost.</li>
      </ul>
    </div>
  </div>
</section>
"""

def platform_section(num, sid, kicker, title, role_lead, role_points, mock):
    points = "".join(f"<li>{p}</li>" for p in role_points)
    return f"""
<section id="{sid}" class="section">
  <p class="kicker">{num} · {kicker}</p>
  <h2 class="section-title">{title}</h2>
  <p class="lede">{role_lead}</p>
  <ul class="role-points">{points}</ul>
  {mock}
</section>
"""

TIKTOK_SEC = platform_section(
    "04", "tiktok", "Primary platform", "TikTok &amp; Reels — the front door.",
    "TikTok is the top of the funnel: where a SEA importer scrolling at lunch meets WorldFirst for the first time. Fast, genuinely useful, a little dramatic.",
    ["Lead pillars: Source Smarter and Don't Get Burned — the content that stops a scroll.",
     "Format: on-location POV and annotated reveals. Designed with one screenshot-able frame that travels into WhatsApp.",
     "Goal: the stop-scroll and the follow. Not the sale — that comes later.",
     "Cadence: 3-4 per week."],
    TIKTOK_MOCK)

IG_SEC = platform_section(
    "05", "instagram", "Primary platform", "Instagram — the considered middle.",
    "Instagram is where the importer who is now paying attention goes deeper. Carousels that get saved and forwarded; Reels cross-posted from TikTok.",
    ["Lead pillars: Source Smarter, Don't Get Burned, and Move Money Right.",
     "Format: the carousel is the workhorse — numbered, save-worthy, screenshot-friendly.",
     "Goal: saves and forwards — the quiet signal that content is being passed importer to importer.",
     "Cadence: mirrors TikTok plus 2-3 carousels per week."],
    IG_MOCK)

YT_SEC = platform_section(
    "06", "youtube", "Primary platform", "YouTube — depth and authority.",
    "YouTube is where a serious importer goes to actually learn — and where WorldFirst proves it is an authority, not a brand chasing trends. The Global Sourcing Guide is the anchor.",
    ["Lead pillars: Source Smarter and Don't Get Burned, in long form.",
     "Format: 10-15min deep dives, plus Shorts cut down from the long-form and from TikTok.",
     "Goal: credibility and depth — the proof that the short-form brand has substance behind it.",
     "Cadence: 2 long-form per month, Shorts continuous."],
    YOUTUBE_MOCK)

LI_SEC = platform_section(
    "07", "linkedin", "Primary platform", "LinkedIn — credibility and the business owner.",
    "LinkedIn reaches the importer as a business owner, plus the wider cross-border industry. This is where the Trade Desk pillar lives.",
    ["Lead pillar: The Trade Desk — proprietary data nobody else can publish.",
     "Format: single-chart data posts, customer-story posts, and POV / hot takes.",
     "Goal: authority and lead quality — the serious operators and the press.",
     "Cadence: 3 per week."],
    LINKEDIN_MOCK)

WA_SEC = platform_section(
    "08", "whatsapp", "Secondary platform", "WhatsApp Channel — the alert surface.",
    "WhatsApp Channel is secondary, and deliberately not a daily feed — the research killed that idea. It is a sparse, triggered alert surface for the already-warm audience.",
    ["Content: only when it counts — a real rate move, a holiday payment deadline, a live scam warning.",
     "Format: short alert posts and the occasional named China-desk voice note.",
     "Goal: stay top-of-mind with people who already know WorldFirst, without noise.",
     "Cadence: on trigger only — never on the clock."],
    WHATSAPP_MOCK)

RUNS = """
<section id="runs" class="section">
  <p class="kicker">09 · How it runs</p>
  <h2 class="section-title">The landscape, working together.</h2>
  <p class="lede">The five channels are not five strategies. They are one idea moving through a system, each platform doing the job it is best at.</p>

  <div class="flow">
    <div class="flow-step"><span class="flow-plat">TikTok</span><p>A scrolling importer is stopped by a useful, slightly dramatic clip. First contact.</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><span class="flow-plat">Instagram</span><p>They follow, they save the carousels, they forward one into a supplier WhatsApp group.</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><span class="flow-plat">YouTube</span><p>When they are serious, they go deep — and WorldFirst proves it has real substance.</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><span class="flow-plat">LinkedIn</span><p>The data and the customer proof close the credibility gap for the business owner.</p></div>
    <div class="flow-arrow">→</div>
    <div class="flow-step flow-step-end"><span class="flow-plat">WorldFirst</span><p>Intent is captured. The product — and its embedded, personalised FX layer — takes over.</p></div>
  </div>

  <h3 class="sub">The handoff</h3>
  <p>This is the line that keeps the strategy honest. Content marketing's job ends at the WorldFirst doorstep. It captures attention, builds trust, and catches sourcing and FX intent — then hands the person to the product, where the personalised, embedded intelligence layer does the keeping. Content is the front of the funnel, not the whole of it.</p>

  <h3 class="sub">The weekly shape</h3>
  <ul class="cadence">
    <li><strong>TikTok</strong> — 3-4 short videos / week</li>
    <li><strong>Instagram</strong> — TikTok mirror + 2-3 carousels / week</li>
    <li><strong>YouTube</strong> — 2 long-form / month, Shorts continuous</li>
    <li><strong>LinkedIn</strong> — 3 posts / week (1 data, 1 story, 1 POV)</li>
    <li><strong>WhatsApp Channel</strong> — on trigger only</li>
  </ul>
  <p>One idea, produced once, becomes a TikTok video, an Instagram carousel, a LinkedIn post, a YouTube Short and a WhatsApp alert. The team plans content atoms, not platform posts — and the landscape above is what the audience sees as the result.</p>
</section>
"""

FOOTER = """
<footer class="site-footer">
  <p>WorldFirst · Internal · Content Strategy · May 2026 · <a href="#" id="lock">lock device</a></p>
</footer>
"""

INNER = HERO + BRIEF + PILLARS + FORMATS + TIKTOK_SEC + IG_SEC + YT_SEC + LI_SEC + WA_SEC + RUNS + FOOTER

# ============================================================================
# CSS
# ============================================================================

CSS = """
:root{--wf-pink:#E6185F;--wf-pink-soft:#FFE6EE;--ant-navy:#001E5C;--cream:#FFFAF2;--ink:#1A1A1A;--ink-soft:#555;--ink-mute:#888;--line:#E5E0D5;--line-soft:#F0EBE0;--paper:#fff;}
*{box-sizing:border-box;margin:0;padding:0;}
[hidden]{display:none!important;}
html{scroll-behavior:smooth;}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--cream);color:var(--ink);line-height:1.65;font-size:15.5px;-webkit-font-smoothing:antialiased;}
body.locked .wrap{filter:blur(20px);pointer-events:none;user-select:none;}
a{color:var(--ink);text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:3px;}
a:hover{text-decoration-color:var(--wf-pink);}
code{font-family:'JetBrains Mono',monospace;font-size:.86em;background:var(--line-soft);padding:1px 5px;border-radius:2px;}

.progress{position:fixed;top:0;left:0;height:2px;background:var(--wf-pink);z-index:100;width:0;transition:width .05s linear;}

/* gate */
.gate{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px;background:var(--cream);}
.gate-card{width:100%;max-width:420px;text-align:center;}
.gate-eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:22px;}
.gate-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:50px;letter-spacing:-.02em;margin-bottom:14px;line-height:1.02;}
.gate-subtitle{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:18px;color:var(--ink-soft);margin-bottom:38px;}
#gate-form{display:flex;flex-direction:column;gap:10px;margin-bottom:12px;}
#gate-input{width:100%;padding:13px 16px;font-size:15px;font-family:'JetBrains Mono',monospace;border:1px solid var(--line);border-radius:3px;background:#fff;outline:none;}
#gate-input:focus{border-color:var(--wf-pink);}
#gate-btn{padding:13px 16px;font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.08em;background:var(--ink);color:#fff;border:none;border-radius:3px;cursor:pointer;}
#gate-btn:hover{background:var(--wf-pink);}
#gate-err{font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--wf-pink);margin-top:6px;min-height:18px;}

/* layout */
.wrap{display:grid;grid-template-columns:230px minmax(0,1fr);gap:56px;max-width:1200px;margin:0 auto;padding:56px 44px 120px;}
@media(max-width:980px){.wrap{grid-template-columns:1fr;gap:28px;padding:30px 18px 80px;}.toc{position:relative!important;top:0!important;}}
.toc{position:sticky;top:36px;align-self:start;font-family:'JetBrains Mono',monospace;font-size:12px;}
.toc-lbl{text-transform:uppercase;letter-spacing:.14em;color:var(--ink-mute);margin-bottom:16px;font-size:11px;}
.toc-list{list-style:none;display:flex;flex-direction:column;gap:2px;}
.toc-list a{display:block;padding:7px 10px;text-decoration:none;color:var(--ink-soft);border-left:2px solid transparent;line-height:1.35;transition:.15s;}
.toc-list a:hover{color:var(--ink);}
.toc-list a.active{color:var(--wf-pink);border-left-color:var(--wf-pink);}

/* header */
.page-header{padding-bottom:44px;border-bottom:1px solid var(--line);margin-bottom:56px;}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:20px;}
.page-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:60px;line-height:1.02;letter-spacing:-.025em;margin-bottom:16px;}
.page-byline{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:21px;color:var(--ink-soft);margin-bottom:30px;max-width:620px;}
.meta-row{display:flex;flex-wrap:wrap;gap:8px;}
.meta-pill{font-family:'JetBrains Mono',monospace;font-size:11px;border:1px solid var(--line);border-radius:100px;padding:7px 12px;display:inline-flex;gap:8px;align-items:center;}
.meta-label{color:var(--ink-mute);text-transform:uppercase;letter-spacing:.08em;}

/* sections */
.section{padding-top:60px;padding-bottom:36px;scroll-margin-top:24px;border-top:1px solid var(--line);}
.section:first-of-type{border-top:none;padding-top:0;}
.kicker{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--wf-pink);margin-bottom:14px;}
.section-title{font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:36px;letter-spacing:-.018em;line-height:1.15;margin-bottom:22px;max-width:740px;}
.section p{margin-bottom:14px;max-width:720px;}
.section p strong{color:var(--ink);}
.section em{font-style:italic;}
.lede{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:19px;color:var(--ink-soft);margin-bottom:24px;max-width:700px;line-height:1.5;}
.sub{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:22px;margin:34px 0 14px;letter-spacing:-.01em;}
.section ul{margin:8px 0 16px 22px;max-width:720px;}
.section li{margin-bottom:6px;}
.section li strong{color:var(--ink);}
.brief-jobs li{margin-bottom:8px;}

/* pillars */
.pillars{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:16px;}
@media(max-width:700px){.pillars{grid-template-columns:1fr;}}
.pillar{border:1px solid var(--line);border-radius:4px;padding:24px 26px;background:var(--paper);}
.pillar-num{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--wf-pink);letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px;}
.pillar h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:24px;letter-spacing:-.01em;margin-bottom:4px;}
.pillar-what{font-family:'Fraunces',Georgia,serif;font-style:italic;font-size:15px;color:var(--ink-soft);margin-bottom:10px!important;}
.pillar p{font-size:14px;color:var(--ink-soft);margin-bottom:10px;}
.pillar-leans{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);margin-bottom:0!important;padding-top:8px;border-top:1px solid var(--line-soft);}
.pillar-note{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);line-height:1.6;}

/* formats */
.fmt-cols{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;}
@media(max-width:760px){.fmt-cols{grid-template-columns:1fr;}}
.fmt-col{border:1px solid var(--line);border-radius:4px;padding:20px 22px;background:var(--paper);}
.fmt-col h3{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:19px;margin-bottom:12px;}
.fmt-col ul{margin:0 0 0 16px;}
.fmt-col li{font-size:13.5px;color:var(--ink-soft);margin-bottom:8px;line-height:1.5;}

/* platform sections */
.role-points{margin-bottom:28px!important;}
.role-points li{font-size:14.5px;color:var(--ink-soft);}
.mock-cap{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);text-align:center;margin-top:14px!important;text-transform:uppercase;letter-spacing:.06em;max-width:none!important;}

/* phone frame */
.phone-mock{display:flex;flex-direction:column;align-items:center;}
.phone{width:300px;background:#0d0d0d;border-radius:30px;padding:8px;position:relative;box-shadow:0 16px 44px rgba(0,0,0,.16);}
.phone-notch{position:absolute;top:10px;left:50%;transform:translateX(-50%);width:90px;height:18px;background:#0d0d0d;border-radius:0 0 14px 14px;z-index:3;}
.phone-screen{border-radius:24px;overflow:hidden;height:600px;overflow-y:auto;}

/* tiktok */
.tk-screen{background:#000;color:#fff;}
.tk-statusbar{display:flex;justify-content:space-between;padding:12px 18px 6px;font-family:'JetBrains Mono',monospace;font-size:9px;color:rgba(255,255,255,.5);}
.tk-profile{text-align:center;padding:10px 18px 14px;}
.tk-avatar{width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#E6185F,#001E5C);margin:0 auto 8px;display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:30px;color:#fff;}
.tk-handle{font-size:14px;font-weight:600;}
.tk-name{font-size:11px;color:rgba(255,255,255,.55);margin-bottom:10px;}
.tk-stats{display:flex;justify-content:center;gap:16px;font-size:10px;color:rgba(255,255,255,.55);margin-bottom:10px;}
.tk-stats strong{color:#fff;font-size:13px;}
.tk-bio{font-size:11px;color:rgba(255,255,255,.8);line-height:1.5;margin-bottom:10px;}
.tk-followbtn{background:#E6185F;color:#fff;font-size:12px;font-weight:600;padding:8px 0;border-radius:4px;margin:0 40px;}
.tk-tabs{display:flex;justify-content:space-around;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.12);font-size:13px;color:rgba(255,255,255,.4);}
.tk-tab-active{color:#fff;}
.tk-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px;}
.tk-tile{position:relative;aspect-ratio:9/15;background:linear-gradient(165deg,#241019,#0c0c0c);padding:8px 7px;display:flex;flex-direction:column;justify-content:flex-end;}
.tk-pillar{position:absolute;top:6px;left:6px;font-family:'JetBrains Mono',monospace;font-size:8px;color:rgba(255,255,255,.4);}
.tk-tile-title{font-size:9.5px;line-height:1.3;color:#fff;font-weight:500;margin-bottom:4px;}
.tk-views{font-family:'JetBrains Mono',monospace;font-size:8px;color:rgba(255,255,255,.6);}

/* instagram */
.ig-screen{background:#fff;color:#1a1a1a;}
.ig-topbar{display:flex;justify-content:space-between;padding:14px 16px 8px;font-size:13px;}
.ig-handle-top{font-weight:700;}
.ig-profile{display:flex;align-items:center;gap:20px;padding:8px 16px;}
.ig-avatar{width:62px;height:62px;border-radius:50%;background:linear-gradient(135deg,#E6185F,#001E5C);display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:28px;color:#fff;flex-shrink:0;}
.ig-stats{display:flex;gap:18px;font-size:12px;text-align:center;color:#1a1a1a;}
.ig-stats strong{font-size:14px;}
.ig-name{font-size:12px;font-weight:600;padding:4px 16px 0;}
.ig-bio{font-size:12px;color:#444;padding:2px 16px 8px;line-height:1.5;}
.ig-highlights{display:flex;gap:8px;padding:4px 16px 12px;overflow-x:auto;}
.ig-highlights span{flex-shrink:0;font-size:9px;color:#444;border:1px solid var(--line);border-radius:100px;padding:5px 10px;}
.ig-tabs{display:flex;justify-content:space-around;padding:8px 0;border-top:1px solid #eee;font-size:13px;color:#bbb;}
.ig-tab-active{color:#1a1a1a;}
.ig-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px;}
.ig-tile{position:relative;aspect-ratio:1;background:var(--line-soft);padding:9px 8px;display:flex;align-items:flex-end;}
.ig-kind{position:absolute;top:6px;right:7px;font-size:11px;color:var(--ink-mute);}
.ig-pillar{position:absolute;top:6px;left:7px;font-family:'JetBrains Mono',monospace;font-size:8px;color:var(--ink-mute);}
.ig-tile-title{font-size:10px;line-height:1.32;color:var(--ink);font-weight:500;}

/* youtube */
.yt-mock{display:flex;flex-direction:column;align-items:center;}
.yt-frame{width:100%;max-width:680px;background:var(--paper);border:1px solid var(--line);border-radius:6px;overflow:hidden;}
.yt-banner{height:84px;background:linear-gradient(110deg,#001E5C,#E6185F);display:flex;align-items:center;justify-content:center;}
.yt-banner-txt{font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.3em;color:rgba(255,255,255,.9);}
.yt-header{display:flex;gap:16px;align-items:center;padding:18px 22px;border-bottom:1px solid var(--line);}
.yt-avatar{width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,#E6185F,#001E5C);display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:28px;color:#fff;flex-shrink:0;}
.yt-channel-name{font-family:'Fraunces',serif;font-weight:500;font-size:22px;}
.yt-channel-sub{font-size:12px;color:var(--ink-mute);margin:2px 0;}
.yt-channel-desc{font-size:12.5px;color:var(--ink-soft);}
.yt-subbtn{margin-left:auto;background:var(--ink);color:#fff;font-size:12px;font-weight:600;padding:9px 16px;border-radius:100px;align-self:center;}
.yt-row-label{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:var(--ink);padding:16px 22px 10px;}
.yt-row{display:flex;gap:12px;overflow-x:auto;padding:0 22px 22px;}
.yt-card{width:184px;flex-shrink:0;}
.yt-thumb{aspect-ratio:16/9;background:linear-gradient(150deg,#241019,#0c0c0c);border-radius:4px;position:relative;display:flex;align-items:center;justify-content:center;margin-bottom:7px;}
.yt-play{color:rgba(255,255,255,.55);font-size:20px;}
.yt-dur{position:absolute;bottom:5px;right:6px;background:rgba(0,0,0,.8);color:#fff;font-family:'JetBrains Mono',monospace;font-size:8px;padding:2px 4px;border-radius:2px;}
.yt-title{font-size:12.5px;font-weight:600;line-height:1.32;margin-bottom:3px;}
.yt-meta{font-size:11px;color:var(--ink-mute);}

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
.li-carousel{background:linear-gradient(150deg,#2a0f1d,#0c0c0c);border-radius:4px;padding:26px 22px;margin-bottom:12px;}
.li-car-tag{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.1em;color:rgba(255,255,255,.5);}
.li-car-title{font-family:'Fraunces',serif;font-weight:500;font-size:19px;color:#fff;line-height:1.25;margin-top:8px;}
.li-engage{display:flex;gap:16px;padding-top:10px;border-top:1px solid var(--line-soft);font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);}

/* whatsapp channel */
.wac-mock{display:flex;flex-direction:column;align-items:center;}
.wac-frame{width:100%;max-width:380px;background:#ECE5DD;border-radius:8px;overflow:hidden;box-shadow:0 8px 24px rgba(0,0,0,.08);}
.wac-header{padding:14px 16px 10px;background:#fff;display:flex;gap:12px;align-items:center;}
.wac-avatar{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#E6185F,#001E5C);color:#fff;display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-size:22px;}
.wac-meta{flex:1;}
.wac-name{font-size:15px;font-weight:500;display:flex;align-items:center;gap:4px;}
.wac-verified{display:inline-block;width:14px;height:14px;background:#34B7F1;color:#fff;border-radius:50%;font-size:9px;text-align:center;line-height:14px;}
.wac-sub{font-size:11px;color:var(--ink-mute);}
.wac-follow{background:#25D366;color:#fff;border:none;padding:6px 14px;border-radius:100px;font-family:'Inter',sans-serif;font-size:11px;font-weight:500;}
.wac-desc{padding:0 16px 14px;font-size:12.5px;color:var(--ink-soft);background:#fff;border-bottom:1px solid var(--line);line-height:1.45;}
.wac-posts{padding:10px 12px;display:flex;flex-direction:column;gap:7px;}
.wac-post{background:#fff;border-radius:6px;padding:11px 13px;box-shadow:0 1px 1px rgba(0,0,0,.05);}
.wac-post-meta{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--ink-mute);margin-bottom:5px;}
.wac-post-text{font-size:12.5px;color:var(--ink);line-height:1.45;margin-bottom:6px;}
.wac-link{color:var(--wf-pink);}
.wac-voice{background:#DCF8C6;border-radius:3px;padding:6px 10px;font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--ink);margin-bottom:6px;}
.wac-react{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--ink-mute);}

/* flow */
.flow{display:flex;align-items:stretch;gap:8px;flex-wrap:wrap;margin:8px 0 16px;}
.flow-step{flex:1;min-width:130px;border:1px solid var(--line);border-radius:4px;padding:14px 14px;background:var(--paper);}
.flow-step-end{border-color:var(--wf-pink);}
.flow-plat{font-family:'JetBrains Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--wf-pink);display:block;margin-bottom:6px;}
.flow-step p{font-size:12.5px;color:var(--ink-soft);margin:0;}
.flow-arrow{display:flex;align-items:center;color:var(--ink-mute);font-size:16px;}
@media(max-width:700px){.flow-arrow{display:none;}}
.cadence{margin-left:22px;}
.cadence li{font-size:14px;color:var(--ink-soft);}

/* footer */
.site-footer{margin-top:48px;padding-top:26px;border-top:1px solid var(--line);font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--ink-mute);text-transform:uppercase;letter-spacing:.08em;}
.site-footer a{color:var(--wf-pink);text-decoration:none;}
"""

# ============================================================================
# SHELL
# ============================================================================

blob = encrypt_payload(INNER)
payload_json = json.dumps(blob)

HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>WorldFirst Content Strategy</title>
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
    <h1 class="gate-title">Content Strategy</h1>
    <p class="gate-subtitle">The content, by platform.</p>
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
async function decryptPayload(pw){const b=JSON.parse(document.getElementById('payload').textContent);const salt=b64ToBytes(b.salt),iv=b64ToBytes(b.iv),ct=b64ToBytes(b.ciphertext);const k=await deriveKey(pw,salt,b.iterations);const p=await crypto.subtle.decrypt({name:"AES-GCM",iv},k,ct);return new TextDecoder().decode(p);}
function mountContent(html){
  const wrap=document.createElement('div');wrap.className='wrap';
  wrap.innerHTML=`<aside class="toc"><p class="toc-lbl">Contents</p><ul class="toc-list">
    <li><a href="#brief">01 · The brief</a></li>
    <li><a href="#pillars">02 · The pillars</a></li>
    <li><a href="#formats">03 · Format system</a></li>
    <li><a href="#tiktok">04 · TikTok &amp; Reels</a></li>
    <li><a href="#instagram">05 · Instagram</a></li>
    <li><a href="#youtube">06 · YouTube</a></li>
    <li><a href="#linkedin">07 · LinkedIn</a></li>
    <li><a href="#whatsapp">08 · WhatsApp Channel</a></li>
    <li><a href="#runs">09 · How it runs</a></li>
  </ul></aside><main class="content-main">${html}</main>`;
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
(ROOT / "index.html").write_text(HTML, encoding="utf-8")
print(f"Wrote index.html ({len(HTML):,} bytes; {len(INNER):,} inner)")
