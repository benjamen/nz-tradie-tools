#!/usr/bin/env python3
"""Replace old text-logo header with correct logo+nav in standalone HTML pages."""
import re
from pathlib import Path

CORRECT_HEADER = '''    <header class="site-header">
        <div class="container">
            <a href="/" class="logo"><img src="/static/img/logo-dark.png" alt="TradieTools NZ" class="logo-img"></a>
            <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="main-nav">
                <span></span><span></span><span></span>
            </button>
            <nav class="main-nav" id="main-nav">
                <a href="/trades/">Find a Tradie</a>
                <a href="/post-job/">Post a Job</a>
                <a href="/jobs/">Cost Guides</a>
                <div class="nav-dropdown">
                    <button class="nav-dropdown-btn" aria-expanded="false" aria-haspopup="true">For Tradies &#9662;</button>
                    <div class="nav-dropdown-menu" role="menu">
                        <a href="/for-tradies/" role="menuitem">For Tradies Hub</a>
                        <a href="/calculators/" role="menuitem">Calculators</a>
                        <a href="/templates/" role="menuitem">Free Templates</a>
                        <a href="/articles/" role="menuitem">Articles &amp; Guides</a>
                        <a href="/contact/" role="menuitem">Contact</a>
                    </div>
                </div>
                <a id="nav-my-listing" href="/find/" class="nav-my-listing" style="display:none">My Listing</a>
                <a href="/signup/" class="nav-cta">Free Listing &#8594;</a>
            </nav>
            <script>
            (function(){
                var t=document.querySelector('.nav-toggle'),n=document.getElementById('main-nav');
                if(!t||!n)return;
                t.addEventListener('click',function(){var o=n.classList.toggle('is-open');t.setAttribute('aria-expanded',o);});
                var db=n.querySelector('.nav-dropdown-btn'),dm=n.querySelector('.nav-dropdown-menu');
                if(db&&dm){
                    db.addEventListener('click',function(e){
                        if(window.innerWidth<=768){e.stopPropagation();var open=dm.classList.toggle('is-open');db.setAttribute('aria-expanded',open);}
                    });
                }
                document.addEventListener('click',function(e){
                    if(!t.contains(e.target)&&!n.contains(e.target)){
                        n.classList.remove('is-open');t.setAttribute('aria-expanded','false');
                        if(dm){dm.classList.remove('is-open');if(db)db.setAttribute('aria-expanded','false');}
                    }
                });
                var id=localStorage.getItem('tradieId');
                if(id){var ml=document.getElementById('nav-my-listing');if(ml){ml.style.display='';ml.href='/find/?highlight='+encodeURIComponent(id);}}
            })();
            </script>
        </div>
    </header>'''

# Match everything from <header to </header>
HEADER_RE = re.compile(r'<header\b[^>]*>.*?</header>', re.DOTALL)

FILES = [
    "docs/post-job/index.html",
    "docs/planning/index.html",
    "docs/tier-compare/index.html",
    "docs/unsubscribe/index.html",
    "docs/quote-generator/index.html",
    "docs/diy/index.html",
    "docs/browse-jobs/index.html",
    "docs/404.html",
]

ROOT = Path(__file__).parent

for rel in FILES:
    p = ROOT / rel
    if not p.exists():
        print(f"  SKIP (not found): {rel}")
        continue
    text = p.read_text(encoding="utf-8")
    if 'logo-dark.png' in text:
        print(f"  OK (already fixed): {rel}")
        continue
    updated = HEADER_RE.sub(CORRECT_HEADER, text, count=1)
    if updated == text:
        print(f"  WARN (no match): {rel}")
    else:
        p.write_text(updated, encoding="utf-8")
        print(f"  FIXED: {rel}")
