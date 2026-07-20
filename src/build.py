# -*- coding: utf-8 -*-
"""
Static-site generator for the Greek-market version of aggelosmouzakitis.com.
Reuses the original site's design system (colours, typography, components) and
adapts the copy for the Greek audience. Emits plain HTML so it can be hosted on
GitHub Pages with no build step at serve time.

Links are relative and depth-aware, so the site works both under a GitHub Pages
project sub-path (preview) and later at a root domain (production).
Images reference the already-hosted production assets on aggelosmouzakitis.com.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "site")

# ── Config (change BASE_URL once the final Greek domain is decided) ───────────
BASE_URL   = "https://aggelosmouzakitis.gr"   # placeholder for canonical/sitemap
IMG        = "https://aggelosmouzakitis.com/img"
EMAIL      = "aggelos.mouzakitis@gmail.com"
LINKEDIN   = "https://www.linkedin.com/in/growth-product-manager/"
YOUTUBE    = "https://www.youtube.com/channel/UCfeHgYhNWwIRgWyRW9J0YCA"
INSTAGRAM  = "https://www.instagram.com/"      # TODO: replace with real handle
GA_ID      = "G-KV83RRF6ZM"

# ── Design tokens (from the original site) ───────────────────────────────────
ACCENT   = "#1a7f37"
ACCENT_D = "#146b2e"
TEXT     = "#282726"
MUTED    = "#666"
BG       = "#F5F5F5"

# ── Navigation model ─────────────────────────────────────────────────────────
SERVICES = [
    ("executive-coaching", "Executive Coaching"),
    ("burnout",            "Burnout"),
    ("career-coaching",    "Career Coaching"),
    ("imposter-syndrome",  "Imposter Syndrome"),
]
SERVICE_SLUGS = [s for s, _ in SERVICES]


def rel(depth, slug):
    """Depth-aware relative href. depth 0 = homepage, depth 1 = /slug/ pages."""
    prefix = "../" * depth
    if slug == "":
        return prefix if depth > 0 else "./"
    return (prefix if depth > 0 else "") + slug + "/"


# ── SVG icons ────────────────────────────────────────────────────────────────
IC_HOME = '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9.5L12 3l9 6.5V20a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9.5z"/><polyline points="9 21 9 12 15 12 15 21"/></svg>'
IC_COMPASS = '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>'
IC_LAYERS = '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>'
IC_USER = '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
IC_CLIP = '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/></svg>'
IC_CHEV = '<svg class="svc-chev" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>'
IC_LI = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>'
IC_YT = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46a2.78 2.78 0 0 0-1.95 1.96A29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58A2.78 2.78 0 0 0 3.41 19.6C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 0 0 1.95-1.96A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" fill="#F5F5F5"/></svg>'
IC_IG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><line x1="17.5" y1="6.5" x2="17.5" y2="6.5"/></svg>'


# ── Shared CSS (mirrors the original inline styles + responsive nav) ──────────
CSS = f"""
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
html,body{{height:100%}}
body{{background:{BG};font-family:'Libre Franklin',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:16px;line-height:1.7;-webkit-font-smoothing:antialiased;color:{TEXT}}}
::selection{{background:{TEXT};color:#fff}}
#root{{display:flex;overflow:hidden;height:100%}}
#main-scroll{{flex:1;overflow-y:auto;overflow-x:hidden;background:#fff;color:{TEXT}}}
#main-scroll a{{color:{ACCENT};text-underline-offset:3px;text-decoration-thickness:1px}}
#main-scroll a:hover{{color:{ACCENT_D};text-decoration-thickness:2px}}
#main-scroll strong{{font-weight:400;color:{TEXT};border-bottom:1px solid rgba(40,39,38,.3);padding-bottom:1px}}
#main-scroll::-webkit-scrollbar{{width:4px}}
#main-scroll::-webkit-scrollbar-thumb{{background:rgba(40,39,38,.15)}}

/* sidebar */
#sidebar{{width:300px;min-width:300px;background:{BG};border-right:1px solid rgba(40,39,38,.1);height:100vh;flex-shrink:0;display:flex;flex-direction:column;overflow:visible}}
.sb-scroll{{flex:1;overflow-y:auto;overflow-x:hidden;display:flex;flex-direction:column}}
.sb-profile{{display:flex;align-items:center;gap:12px;padding:22px 18px 20px;border-bottom:1px solid rgba(40,39,38,.1)}}
.sb-profile img{{width:38px;height:38px;border-radius:50%;object-fit:cover;flex-shrink:0;display:block}}
.sb-name{{font-size:15px;font-weight:700;letter-spacing:.02em;text-transform:uppercase;color:{TEXT};white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.sb-role{{font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:{MUTED};margin-top:3px}}
.sb-cta-wrap{{padding:16px 16px 8px}}
.sb-cta{{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;padding:13px 0;font-family:inherit;font-weight:700;font-size:12px;letter-spacing:.06em;text-transform:uppercase;background:{ACCENT};border:1.5px solid {ACCENT};color:#fff;cursor:pointer;text-decoration:none;transition:background .15s,border-color .15s}}
.sb-cta:hover{{background:{ACCENT_D};border-color:{ACCENT_D}}}
.sb-cta-note{{font-size:11px;letter-spacing:.03em;color:{MUTED};text-align:center;margin-top:8px;text-transform:uppercase}}
.sb-nav{{padding:8px 0 0}}
.nav-item{{display:flex;align-items:center;gap:12px;width:100%;padding:11px 18px;background:transparent;border-left:2px solid transparent;cursor:pointer;font-family:inherit;text-decoration:none;font-size:14px;font-weight:500;letter-spacing:.03em;text-transform:uppercase;color:rgba(40,39,38,.65);transition:background .12s,color .12s}}
.nav-item:hover{{background:rgba(40,39,38,.04);color:rgba(40,39,38,.85)}}
.nav-item.active{{background:rgba(40,39,38,.08);border-left:2px solid {ACCENT};color:{TEXT}}}
.svc-toggle{{display:flex;align-items:center;justify-content:space-between;width:100%;padding:11px 18px;background:transparent;border:none;border-left:2px solid transparent;cursor:pointer;font-family:inherit;font-size:14px;font-weight:500;letter-spacing:.03em;text-transform:uppercase;color:rgba(40,39,38,.65);transition:background .12s,color .12s}}
.svc-toggle:hover{{background:rgba(40,39,38,.04);color:rgba(40,39,38,.85)}}
.svc-toggle.active{{color:{TEXT}}}
.svc-toggle .svc-left{{display:flex;align-items:center;gap:12px}}
.svc-chev{{transition:transform .2s ease}}
.svc-group.collapsed .svc-chev{{transform:rotate(-90deg)}}
.svc-sub{{overflow:hidden}}
.svc-group.collapsed .svc-sub{{display:none}}
.svc-sub a{{display:block;padding:9px 18px 9px 50px;font-family:inherit;text-decoration:none;font-size:13px;font-weight:500;letter-spacing:.02em;color:rgba(40,39,38,.6);border-left:2px solid transparent;transition:background .12s,color .12s}}
.svc-sub a:hover{{background:rgba(40,39,38,.04);color:rgba(40,39,38,.85)}}
.svc-sub a.active{{color:{ACCENT};border-left:2px solid {ACCENT};background:rgba(26,127,55,.06)}}
.sb-spacer{{flex:1}}
.sb-socials{{display:flex;gap:6px;padding:14px 18px 20px;border-top:1px solid rgba(40,39,38,.1)}}
.sb-socials a{{display:flex;align-items:center;justify-content:center;width:34px;height:34px;color:rgba(40,39,38,.55);transition:color .12s,background .12s;border-radius:6px}}
.sb-socials a:hover{{color:{ACCENT};background:rgba(40,39,38,.05)}}

/* mobile header */
#mtop,#mmenu{{display:none}}
@media (max-width:860px){{
  #root{{display:block;height:auto;overflow:visible}}
  #sidebar{{display:none}}
  #main-scroll{{height:auto;overflow:visible}}
  #mtop{{display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:200;background:{BG};border-bottom:1px solid rgba(40,39,38,.1);padding:12px 16px}}
  #mtop .mbrand{{display:flex;align-items:center;gap:10px;text-decoration:none}}
  #mtop .mbrand img{{width:32px;height:32px;border-radius:50%;display:block}}
  #mtop .mbrand span{{font-size:13px;font-weight:700;letter-spacing:.02em;text-transform:uppercase;color:{TEXT}}}
  #mtop .mright{{display:flex;align-items:center;gap:10px}}
  .mdiag{{font-size:11px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;background:{ACCENT};color:#fff;text-decoration:none;padding:8px 12px}}
  #mburger{{background:none;border:none;cursor:pointer;color:{TEXT};padding:6px;display:flex}}
  #mmenu{{display:none;position:sticky;top:57px;z-index:190;background:{BG};border-bottom:1px solid rgba(40,39,38,.1);padding:6px 0 12px}}
  #mmenu.open{{display:block}}
  #mmenu a,#mmenu .mlabel{{display:block;padding:11px 18px;text-decoration:none;font-size:14px;font-weight:500;letter-spacing:.03em;text-transform:uppercase;color:rgba(40,39,38,.75)}}
  #mmenu a.active{{color:{ACCENT}}}
  #mmenu .mlabel{{color:{MUTED};font-size:11px;letter-spacing:.12em;padding-bottom:4px}}
  #mmenu .msub a{{padding-left:32px;font-size:13px}}
}}

/* content typography */
.wrap{{max-width:940px;margin:0 auto;padding:4rem 2rem 7rem}}
.wrap-home{{max-width:1100px;margin:0 auto;padding:4rem 2.5rem 7rem}}
h1{{font-size:32px;font-weight:400;line-height:1.4;letter-spacing:-.02em;margin-bottom:2.5rem}}
.lead{{font-size:23px;font-weight:500;letter-spacing:-.01em;line-height:1.6;margin-bottom:1.4rem}}
.sec{{display:grid;grid-template-columns:184px 1fr;gap:0 2.25rem;margin-bottom:3rem}}
.sec h2{{font-size:17px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:{MUTED};padding-top:.25rem;line-height:1.5;text-wrap:balance}}
.sec p{{margin-bottom:1.2rem;line-height:1.75;font-size:18px}}
.sec p:last-child{{margin-bottom:0}}
.kick{{font-size:17px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:{MUTED};margin:0 0 1.2rem;line-height:1.5}}
.block{{margin-bottom:3.5rem}}
hr.sep{{border:none;border-top:1px solid rgba(40,39,38,.2);margin:2.5rem 0}}
.cta-btn{{font-family:inherit;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:{ACCENT};border:1px solid {ACCENT};text-decoration:none;padding:.85rem 1.6rem;display:inline-block;cursor:pointer;transition:background .15s,border-color .15s}}
.cta-btn:hover{{background:{ACCENT_D};border-color:{ACCENT_D};color:#fff}}
.cta-ghost{{font-family:inherit;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:{TEXT};background:transparent;border:1px solid rgba(40,39,38,.3);text-decoration:none;padding:.85rem 1.6rem;display:inline-block;cursor:pointer;transition:border-color .15s,color .15s}}
.cta-ghost:hover{{border-color:{ACCENT};color:{ACCENT}}}
.card{{border:1px solid rgba(40,39,38,.12);border-radius:12px;background:#fff;padding:1.35rem}}
.card h3{{font-size:17px;font-weight:700;color:{TEXT};margin:0 0 .5rem}}
.card p{{font-size:15px;line-height:1.65;margin:0}}
.grid2{{display:flex;gap:1rem;align-items:stretch}}
.grid2>*{{flex:1}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}}
.plist{{border:1px solid rgba(40,39,38,.12);border-radius:12px;background:#fff;overflow:hidden;margin:.4rem 0 1.4rem}}
.plist .row{{display:grid;grid-template-columns:246px 26px 1fr;align-items:baseline;padding:.95rem 1.3rem;font-size:15px;line-height:1.55}}
.plist .row+.row{{border-top:1px solid rgba(40,39,38,.12)}}
.plist .cause{{font-weight:700}}
.plist .arw{{color:{ACCENT};font-weight:700;text-align:center}}
.faq h3{{font-size:18px;font-weight:400;line-height:1.7;margin-bottom:.6rem;border-bottom:1px solid rgba(40,39,38,.12);padding-bottom:.4rem}}
.faq .qa{{margin-bottom:2rem}}
.faq p{{font-size:18px;line-height:1.75}}
.topics{{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem;margin-top:1rem}}
.topic{{display:block;border:1px solid rgba(40,39,38,.12);border-radius:12px;background:#fff;padding:1.4rem 1.5rem;text-decoration:none;color:{TEXT};transition:border-color .18s,box-shadow .18s,transform .18s}}
.topic:hover{{border-color:rgba(26,127,55,.5);box-shadow:0 8px 26px rgba(26,127,55,.10);transform:translateY(-3px)}}
.topic .t-name{{font-size:19px;font-weight:700;color:{TEXT};margin-bottom:.35rem}}
.topic .t-desc{{font-size:15px;color:{MUTED};line-height:1.6}}
.callout{{border:1px solid rgba(40,39,38,.12);border-left:3px solid {ACCENT};border-radius:10px;background:rgba(26,127,55,.04);padding:1.35rem 1.5rem;font-size:16px;line-height:1.7}}
.sectitle{{font-size:22px;font-weight:700;letter-spacing:-.01em;color:{ACCENT};margin-bottom:1.2rem;line-height:1.3}}
.hero{{display:flex;gap:4rem;align-items:center}}
.hero-txt{{flex:1.15 1 0;min-width:0;max-width:520px}}
.hero-txt p{{font-size:18px;line-height:1.75;margin-bottom:1.2rem}}
.hero-txt p:last-child{{margin-bottom:0}}
.hero-img{{flex:1 1 0;min-width:0}}
.hero-img img{{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:14px;display:block}}
.hero-cta{{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:1.8rem}}
@media (max-width:860px){{.hero{{flex-direction:column;gap:1.5rem}}.hero-txt{{max-width:none}}.hero-img img{{aspect-ratio:16/10}}}}

/* footer */
.site-ft{{margin-top:5rem;padding-top:3.25rem;border-top:1px solid rgba(40,39,38,.2)}}
.site-ft-cols{{display:grid;grid-template-columns:repeat(3,1fr);gap:2.5rem}}
.site-ft-h{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{ACCENT};margin-bottom:1.1rem}}
.site-ft-row{{margin-bottom:.75rem}}
.site-ft a{{display:inline-flex;align-items:baseline;gap:.35rem;font-size:15px;color:{TEXT};text-decoration:none;line-height:1.4;transition:color .12s}}
.site-ft a:hover{{color:{ACCENT}}}
.site-ft-social{{display:flex;gap:10px;margin-top:.2rem}}
.site-ft-social a{{display:flex;align-items:center;justify-content:center;width:38px;height:38px;border:1px solid rgba(40,39,38,.15);border-radius:8px;color:rgba(40,39,38,.6);transition:color .12s,border-color .12s}}
.site-ft-social a:hover{{color:{ACCENT};border-color:rgba(26,127,55,.5)}}
.site-ft-copy{{margin-top:2.5rem;padding-top:1.5rem;border-top:1px solid rgba(40,39,38,.12);font-size:13px;color:{MUTED}}}

@media (max-width:860px){{
  .wrap,.wrap-home{{padding:1.75rem 1.15rem 4rem}}
  h1{{font-size:22px;margin-bottom:1.5rem}}
  .lead{{font-size:19px}}
  .sec{{display:block;margin-bottom:2rem}}
  .sec h2{{padding-bottom:.4rem;margin-bottom:.6rem}}
  .grid2,.grid3,.topics{{grid-template-columns:1fr;display:grid}}
  .grid2{{gap:.9rem}}
  .plist .row{{grid-template-columns:1fr;gap:.15rem}}
  .plist .arw{{display:none}}
  .site-ft-cols{{display:block}}
  .site-ft-col{{margin-bottom:2rem}}
}}
"""

# ── JSON-LD ──────────────────────────────────────────────────────────────────
PERSON_LD = ('{"@context":"https://schema.org","@type":"Person","name":"Aggelos Mouzakitis",'
    '"alternateName":"Άγγελος Μουζακίτης","url":"' + BASE_URL + '/","image":"' + IMG + '/aggelos.jpg",'
    '"jobTitle":["Σύμβουλος Ψυχικής Υγείας","Mental Health Counsellor"],'
    '"description":"Σύμβουλος Ψυχικής Υγείας με υπόβαθρο founder και ηγετικό ρόλο στην τεχνολογία. Δουλεύει με έμπειρους επαγγελματίες, στελέχη, founders και ελεύθερους επαγγελματίες σε burnout, μεταβάσεις καριέρας, πίεση ηγεσίας και imposter syndrome.",'
    '"knowsAbout":["Executive Coaching","Burnout","Career Coaching","Imposter Syndrome","Επαγγελματική εξουθένωση","Σύνδρομο του απατεώνα","Συμβουλευτική στελεχών","Αλλαγή καριέρας"],'
    '"sameAs":["' + LINKEDIN + '","' + YOUTUBE + '"],"@id":"' + BASE_URL + '/#person"}')


def head(title, desc, slug, depth, extra_ld=""):
    canonical = BASE_URL + "/" + (slug + "/" if slug else "")
    og_img = IMG + "/og/home.png"
    ld = '<script type="application/ld+json">' + PERSON_LD + '</script>'
    if extra_ld:
        ld += '<script type="application/ld+json">' + extra_ld + '</script>'
    return f"""<!DOCTYPE html>
<html lang="el-GR">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@400;500;600;700&display=swap">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="icon" href="{IMG}/../favicon.svg" type="image/svg+xml">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="el_GR">
<meta property="og:site_name" content="Aggelos Mouzakitis">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_img}">
<meta name="author" content="Aggelos Mouzakitis">
<meta name="theme-color" content="{BG}">
<link rel="alternate" hreflang="el-GR" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
{ld}
<style>{CSS}</style>
</head>
<body>"""


# ── Sidebar + mobile nav ─────────────────────────────────────────────────────
def sidebar(active, depth):
    def cls(slug):
        return " active" if active == slug else ""
    svc_open = active in SERVICE_SLUGS
    svc_group_cls = "svc-group" if svc_open else "svc-group collapsed"
    svc_links = "".join(
        f'<a href="{rel(depth, s)}" class="{ "active" if active==s else "" }">{label}</a>'
        for s, label in SERVICES
    )
    return f"""
<div id="sidebar">
  <div class="sb-scroll">
    <a class="sb-profile" href="{rel(depth,'')}" style="text-decoration:none">
      <img src="{IMG}/aggelos-96.webp" alt="Άγγελος Μουζακίτης" width="38" height="38">
      <div style="overflow:hidden">
        <div class="sb-name">Aggelos Mouzakitis</div>
        <div class="sb-role">Σύμβουλος Ψυχικής Υγείας</div>
      </div>
    </a>
    <div class="sb-cta-wrap">
      <a class="sb-cta" href="{rel(depth,'burnout-diagnostic')}">{IC_CLIP}<span>Burnout Diagnostic</span></a>
      <div class="sb-cta-note">Δωρεάν τεστ αυτοαξιολόγησης · ~8'</div>
    </div>
    <nav class="sb-nav">
      <a class="nav-item{cls('')}" href="{rel(depth,'')}">{IC_HOME}<span>Αρχική</span></a>
      <a class="nav-item{cls('how-i-work')}" href="{rel(depth,'how-i-work')}">{IC_COMPASS}<span>Πώς δουλεύω</span></a>
      <div class="{svc_group_cls}" id="svcGroup">
        <button class="svc-toggle{' active' if svc_open else ''}" id="svcToggle" aria-expanded="{'true' if svc_open else 'false'}">
          <span class="svc-left">{IC_LAYERS}<span>Υπηρεσίες</span></span>{IC_CHEV}
        </button>
        <div class="svc-sub">{svc_links}</div>
      </div>
      <a class="nav-item{cls('about')}" href="{rel(depth,'about')}">{IC_USER}<span>Σχετικά</span></a>
    </nav>
    <div class="sb-spacer"></div>
    <div class="sb-socials">
      <a href="{LINKEDIN}" target="_blank" rel="noopener" title="LinkedIn">{IC_LI}</a>
      <a href="{YOUTUBE}" target="_blank" rel="noopener" title="YouTube">{IC_YT}</a>
      <a href="{INSTAGRAM}" target="_blank" rel="noopener" title="Instagram">{IC_IG}</a>
    </div>
  </div>
</div>"""


def mobile_nav(active, depth):
    def a(slug, label):
        c = " active" if active == slug else ""
        return f'<a class="{c.strip()}" href="{rel(depth, slug)}">{label}</a>'
    svc = "".join(
        f'<a class="{ "active" if active==s else "" }" href="{rel(depth,s)}">{label}</a>'
        for s, label in SERVICES
    )
    return f"""
<header id="mtop">
  <a class="mbrand" href="{rel(depth,'')}"><img src="{IMG}/aggelos-96.webp" alt="Άγγελος Μουζακίτης"><span>Aggelos Mouzakitis</span></a>
  <div class="mright">
    <a class="mdiag" href="{rel(depth,'burnout-diagnostic')}">Diagnostic</a>
    <button id="mburger" aria-label="Μενού"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg></button>
  </div>
</header>
<nav id="mmenu">
  {a('', 'Αρχική')}
  {a('how-i-work', 'Πώς δουλεύω')}
  <div class="mlabel">Υπηρεσίες</div>
  <div class="msub">{svc}</div>
  {a('about', 'Σχετικά')}
</nav>"""


JS = """
<script>
(function(){
  var t=document.getElementById('svcToggle'),g=document.getElementById('svcGroup');
  if(t&&g)t.addEventListener('click',function(){
    var open=!g.classList.contains('collapsed');
    g.classList.toggle('collapsed');t.setAttribute('aria-expanded',String(!open));
  });
  var b=document.getElementById('mburger'),m=document.getElementById('mmenu');
  if(b&&m)b.addEventListener('click',function(){m.classList.toggle('open');});
})();
</script>
"""


# ── Footer ───────────────────────────────────────────────────────────────────
def footer(depth):
    svc_links = "".join(
        f'<div class="site-ft-row"><a href="{rel(depth,s)}">{label}</a></div>'
        for s, label in SERVICES
    )
    return f"""
<footer class="site-ft">
  <div class="site-ft-cols">
    <div class="site-ft-col">
      <div class="site-ft-h">Υπηρεσίες</div>
      {svc_links}
    </div>
    <div class="site-ft-col">
      <div class="site-ft-h">Ιστότοπος</div>
      <div class="site-ft-row"><a href="{rel(depth,'')}">Αρχική</a></div>
      <div class="site-ft-row"><a href="{rel(depth,'how-i-work')}">Πώς δουλεύω</a></div>
      <div class="site-ft-row"><a href="{rel(depth,'about')}">Σχετικά</a></div>
      <div class="site-ft-row"><a href="{rel(depth,'burnout-diagnostic')}">Burnout Diagnostic</a></div>
      <div class="site-ft-row"><a href="{rel(depth,'confidentiality')}">Εμπιστευτικότητα</a></div>
    </div>
    <div class="site-ft-col">
      <div class="site-ft-h">Επικοινωνία</div>
      <div class="site-ft-social">
        <a href="{LINKEDIN}" target="_blank" rel="noopener" title="LinkedIn">{IC_LI}</a>
        <a href="{YOUTUBE}" target="_blank" rel="noopener" title="YouTube">{IC_YT}</a>
        <a href="{INSTAGRAM}" target="_blank" rel="noopener" title="Instagram">{IC_IG}</a>
      </div>
    </div>
  </div>
  <div class="site-ft-copy">© Aggelos Mouzakitis · Σύμβουλος Ψυχικής Υγείας</div>
</footer>"""


def page(slug, depth, title, desc, main_html, extra_ld="", wrap="wrap"):
    return (head(title, desc, slug, depth, extra_ld)
            + mobile_nav(slug, depth)
            + '<div id="root">'
            + sidebar(slug, depth)
            + f'<div id="main-scroll"><main class="{wrap}">'
            + main_html
            + footer(depth)
            + '</main></div></div>'
            + JS
            + '\n</body>\n</html>\n')


# ── Content helpers ──────────────────────────────────────────────────────────
def sec(label, *paras):
    inner = "".join(f"<p>{p}</p>" for p in paras)
    return f'<section class="sec"><h2>{label}</h2><div>{inner}</div></section>'


def sec_html(label, inner):
    return f'<section class="sec"><h2>{label}</h2><div>{inner}</div></section>'


def diag_cta(depth, label="Ξεκινήστε το Burnout Diagnostic →"):
    return f'<div style="margin-top:1.4rem"><a class="cta-btn" href="{rel(depth,"burnout-diagnostic")}">{label}</a></div>'


def faq(items):
    qa = "".join(f'<div class="qa"><h3>{q}</h3><p>{a}</p></div>' for q, a in items)
    return f'<section class="sec"><h2>Συχνές ερωτήσεις</h2><div class="faq">{qa}</div></section>'


def il(depth, slug, text):
    return f'<a href="{rel(depth, slug)}">{text}</a>'


# ═══════════════════════════════════════════════════════════════════════════
#  PAGES
# ═══════════════════════════════════════════════════════════════════════════
PAGES_OUT = {}  # slug -> (filepath, html)


def emit(slug, html):
    path = "index.html" if slug == "" else f"{slug}/index.html"
    PAGES_OUT[slug] = path
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


# ---- content modules imported from pages_content.py -------------------------
import pages_content as PC

for spec in PC.build(rel, sec, sec_html, faq, diag_cta, il, footer):
    emit(spec["slug"], page(spec["slug"], spec["depth"], spec["title"],
                            spec["desc"], spec["main"],
                            spec.get("extra_ld", ""), spec.get("wrap", "wrap")))

# ---- diagnostic page (self-contained) ---------------------------------------
import diagnostic_page as DP
emit("burnout-diagnostic", DP.render(head, mobile_nav, sidebar, footer, JS, rel))

# ---- 404 --------------------------------------------------------------------
_404 = page("", 0, "Η σελίδα δεν βρέθηκε | Aggelos Mouzakitis",
            "Η σελίδα που ζητήσατε δεν υπάρχει.",
            '<h1>Η σελίδα δεν βρέθηκε</h1><p class="lead">Η σελίδα που ζητήσατε δεν υπάρχει ή έχει μετακινηθεί.</p>'
            '<p><a class="cta-btn" href="./">Επιστροφή στην αρχική →</a></p>')
with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
    f.write(_404)

# ---- sitemap + robots -------------------------------------------------------
urls = [""] + [s for s in PAGES_OUT if s != ""]
order = ["", "how-i-work", "executive-coaching", "burnout", "career-coaching",
         "imposter-syndrome", "burnout-diagnostic", "about", "confidentiality"]
urls = [u for u in order if u in PAGES_OUT]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    loc = BASE_URL + "/" + (u + "/" if u else "")
    pr = "1.0" if u == "" else ("0.9" if u in ("burnout","career-coaching","burnout-diagnostic") else "0.8")
    sm.append(f"  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>{pr}</priority></url>")
sm.append("</urlset>")
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(sm) + "\n")

with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: " + BASE_URL + "/sitemap.xml\n")

# .nojekyll so GitHub Pages serves files as-is
open(os.path.join(OUT, ".nojekyll"), "w").close()

print("Built", len(PAGES_OUT), "pages +", "sitemap/robots/404 into", OUT)
