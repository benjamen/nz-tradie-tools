#!/usr/bin/env /usr/bin/python3
"""NZ Tradie Tools — static site generator."""

import json
import logging
import re
import shutil
import subprocess
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader
import logging

SITE_ROOT = Path(__file__).parent
CONTENT_DIR = SITE_ROOT / "content"
LAYOUTS_DIR = SITE_ROOT / "layouts"
STATIC_DIR = SITE_ROOT / "static"
DATA_DIR = SITE_ROOT / "data"
PUBLIC_DIR = SITE_ROOT / "docs"
CONFIG_FILE = SITE_ROOT / "site.json"
CLAIMED_DIR = DATA_DIR / "claimed"

MD = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list"])


def slugify(text):
    """Convert business name to URL-safe slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def load_claimed_businesses():
    """Return dict of slug -> claimed business data."""
    claimed = {}
    if CLAIMED_DIR.exists():
        for f in CLAIMED_DIR.glob("*.json"):
            try:
                data = json.loads(f.read_text())
                claimed[data["slug"]] = data
            except Exception:
                pass
    return claimed


def load_config():
    return json.loads(CONFIG_FILE.read_text())


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    front = yaml.safe_load(parts[1]) or {}
    return front, parts[2].strip()


def render_markdown(body):
    MD.reset()
    return MD.convert(body)


def prefix_internal_links(html, base_path):
    if not base_path:
        return html
    return re.sub(r'href="(/(?!/))', f'href="{base_path}/', html)


def build_nav(config):
    return config.get("nav", [])


def build_articles(env, config, nav, base_path):
    logging.info("Building articles")
    articles_dir = CONTENT_DIR / "articles"
    for article_path in articles_dir.glob("*.md"):
        front, body = parse_frontmatter(article_path.read_text())
        html_body = render_markdown(body)
        html_body = prefix_internal_links(html_body, front.get("base_path", ""))
        template = env.get_template(front.get("layout", "article.html"))
        output_path = PUBLIC_DIR / article_path.with_suffix(".html").relative_to(CONTENT_DIR)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(template.render(**front, content=html_body, nav=nav))
        logging.info(f"Article built: {output_path}")


def build():
    logging.info("Build start")
    config = load_config()
    env = Environment(loader=FileSystemLoader(str(LAYOUTS_DIR)))
    nav = build_nav(config)
    base_path = config.get("base_path", "")
    build_articles(env, config, nav, base_path)

    if STATIC_DIR.exists():
        for f in STATIC_DIR.rglob("*"):
            if f.is_file():
                dest = PUBLIC_DIR / "static" / f.relative_to(STATIC_DIR)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dest)
        favicon = STATIC_DIR / "favicon.svg"
        if favicon.exists():
            shutil.copy2(favicon, PUBLIC_DIR / "favicon.svg")

    articles = []
    calculators = []

    articles_dir = CONTENT_DIR / "articles"
    if articles_dir.exists():
        for md_file in articles_dir.glob("*.md"):
            page = process_page(md_file, config, env, "base.html", "articles", nav, base_path)
            if page and not page.get("draft"):
                articles.append(page)
    articles.sort(key=lambda a: a.get("date_iso", ""), reverse=True)

    articles_by_slug = {a["slug"]: a for a in articles}
    calcs_dir = CONTENT_DIR / "calculators"
    if calcs_dir.exists():
        for md_file in sorted(calcs_dir.glob("*.md")):
            page = process_page(md_file, config, env, "calculator.html", "calculators", nav, base_path,
                                articles=articles, articles_by_slug=articles_by_slug)
            if page and not page.get("draft"):
                calculators.append(page)

    build_index(articles, calculators, config, env, nav, base_path)
    build_listing(articles, config, env, "articles", nav, base_path)
    build_listing(calculators, config, env, "calculators", nav, base_path)
    build_calc_categories(calculators, config, env, nav, base_path)
    build_contact(config, env, nav, base_path)
    build_privacy(config, env, nav, base_path)
    build_glossary(config, env, nav, base_path)
    build_faq(config, env, nav, base_path)
    build_tax_dates(config, env, nav, base_path)
    profiles_count = build_business_profiles(config, env, nav, base_path)
    build_claim_page(config, env, nav, base_path)

    trades_count, locations_count = build_trades_and_locations(config, env, nav, base_path)

    cities = json.loads((DATA_DIR / "cities.json").read_text())
    trades_data = json.loads((DATA_DIR / "trades.json").read_text())
    job_pages = build_job_pages(config, env, nav, base_path)
    template_pages = build_templates(config, env, nav, base_path)
    rate_rows = build_tradie_rates(config, nav, base_path)
    build_sitemap(articles, calculators, cities, trades_data, config, job_pages)
    build_robots(config)
    build_ads_txt(config)
    build_rss(articles, config)

    print(f"Built: {len(articles)} articles, {len(calculators)} calculators, "
          f"{trades_count} trade pages, {locations_count} location pages, "
          f"{job_pages} job cost pages, {template_pages} template pages, "
          f"{rate_rows} trade rate rows, {profiles_count} business profiles")
    return articles, calculators


def process_page(md_file, config, env, layout_name, section, nav, base_path, articles=None, articles_by_slug=None):
    text = md_file.read_text(encoding="utf-8")
    front, body = parse_frontmatter(text)

    if not front.get("title"):
        return None

    slug = md_file.stem
    html_body = render_markdown(body)

    for name, url in config.get("affiliates", {}).items():
        html_body = re.sub(
            rf'(?<!["\'])(\b{re.escape(name.title())}\b)(?!["\'])',
            rf'<a href="{url}" rel="sponsored noopener" target="_blank">\1</a>',
            html_body,
            count=1,
        )

    html_body = prefix_internal_links(html_body, base_path)

    try:
        template = env.get_template(layout_name)
    except Exception:
        template = env.get_template("base.html")

    date_val = front.get("date", "")
    if hasattr(date_val, "strftime"):
        date_str = date_val.strftime("%-d %B %Y")
        date_iso = date_val.strftime("%Y-%m-%d")
    else:
        date_str = str(date_val)
        date_iso = str(date_val)

    tags = front.get("tags", [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",")]

    related_slugs = front.get("related_articles", [])
    if isinstance(related_slugs, str):
        related_slugs = [s.strip() for s in related_slugs.split(",")]
    related_articles_data = [articles_by_slug[s] for s in related_slugs if articles_by_slug and s in articles_by_slug]

    ctx = {
        **config,
        "base_path": base_path,
        "page_title": front.get("title"),
        "title": front.get("title"),
        "description": front.get("description", front.get("title")),
        "date": date_str,
        "date_iso": date_iso,
        "author": front.get("author", config.get("author", "")),
        "tags": tags,
        "content": html_body,
        "slug": slug,
        "section": section,
        "url": f"{base_path}/{section}/{slug}.html",
        "draft": front.get("draft", False),
        "calculator_html": front.get("calculator_html", ""),
        "faqs": front.get("faqs", []),
        "nav": nav,
        "year": datetime.now().year,
        "recent_articles": (articles or [])[:3],
        "related_articles_data": related_articles_data,
    }

    rendered = template.render(**ctx)
    out_path = PUBLIC_DIR / section / f"{slug}.html"
    out_path.write_text(rendered, encoding="utf-8")
    return ctx


def build_trades_and_locations(config, env, nav, base_path):
    cities = json.loads((DATA_DIR / "cities.json").read_text())
    trades = json.loads((DATA_DIR / "trades.json").read_text())
    year = datetime.now().year
    shared = {**config, "base_path": base_path, "nav": nav, "year": year,
               "cities": cities, "trades": trades}

    top10_dir = DATA_DIR / "top10"
    claimed = load_claimed_businesses()  # slug -> claimed data
    trades_count = 0
    locations_count = 0

    # Trade listing page (/trades/)
    tpl_listing = env.get_template("trade-listing.html")
    (PUBLIC_DIR / "trades" / "index.html").write_text(
        tpl_listing.render(**shared), encoding="utf-8"
    )
    trades_count += 1

    tpl_hub = env.get_template("trade-hub.html")
    tpl_city = env.get_template("trade-city.html")
    tpl_loc = env.get_template("location-hub.html")

    for trade in trades:
        trade_dir = PUBLIC_DIR / "trades" / trade["slug"]
        trade_dir.mkdir(exist_ok=True)

        # Load existing top10 data for this trade keyed by city slug
        city_data = {}
        for city in cities:
            f = top10_dir / f"{trade['slug']}-{city['slug']}.json"
            if f.exists():
                city_data[city["slug"]] = json.loads(f.read_text())

        # Trade hub page
        hub_html = tpl_hub.render(**shared, trade=trade, city_data=city_data)
        (trade_dir / "index.html").write_text(hub_html, encoding="utf-8")
        trades_count += 1

        # City pages for this trade
        for city in cities:
            data = city_data.get(city["slug"], {})
            other_cities = [c for c in cities if c["slug"] != city["slug"]]
            # Annotate each business with profile_url if they have a claimed listing
            businesses = []
            for b in data.get("businesses", []):
                b = dict(b)  # copy so we don't mutate the source data
                biz_slug = slugify(b.get("name", ""))
                if biz_slug in claimed:
                    b["profile_url"] = f"/businesses/{biz_slug}/"
                else:
                    b["profile_url"] = None
                businesses.append(b)
            ctx = {
                **shared,
                "trade": trade,
                "city": city,
                "businesses": businesses,
                "regional_cost_note": data.get("regional_cost_note", ""),
                "updated": data.get("updated", str(year)),
                "other_cities": other_cities,
            }
            html = tpl_city.render(**ctx)
            (trade_dir / f"{city['slug']}.html").write_text(html, encoding="utf-8")
            trades_count += 1

    # Location hub pages (/locations/[city]/)
    for city in cities:
        loc_dir = PUBLIC_DIR / "locations" / city["slug"]
        loc_dir.mkdir(parents=True, exist_ok=True)

        # Which trades have data for this city
        city_trade_data = {}
        for trade in trades:
            f = top10_dir / f"{trade['slug']}-{city['slug']}.json"
            city_trade_data[trade["slug"]] = f.exists()

        html = tpl_loc.render(
            **shared,
            city=city,
            city_data=city_trade_data,
            all_cities=cities,
        )
        (loc_dir / "index.html").write_text(html, encoding="utf-8")
        locations_count += 1

    return trades_count, locations_count


def build_job_pages(config, env, nav, base_path):
    estimates_file = DATA_DIR / "job_estimates.json"
    if not estimates_file.exists():
        return 0

    data = json.loads(estimates_file.read_text())
    jobs = data["jobs"]
    regional_multipliers = data["regional_multipliers"]
    cities = json.loads((DATA_DIR / "cities.json").read_text())
    trades = json.loads((DATA_DIR / "trades.json").read_text())
    year = datetime.now().year

    jobs_dir = PUBLIC_DIR / "jobs"
    jobs_dir.mkdir(exist_ok=True)

    shared = {**config, "base_path": base_path, "nav": nav, "year": year,
              "cities": cities, "trades": trades, "regional_multipliers": regional_multipliers}

    # Inject slug into each job dict so templates can use {{ job.slug }}
    jobs_list = [{"slug": slug, **job} for slug, job in jobs.items()]
    jobs_by_slug = {j["slug"]: j for j in jobs_list}

    tpl_city = env.get_template("job-city.html")
    tpl_hub = env.get_template("job-hub.html")
    tpl_listing = env.get_template("jobs-listing.html")

    count = 0

    # Jobs listing index
    featured_cities = [c for c in cities if c["slug"] in ["auckland", "wellington", "christchurch", "hamilton", "tauranga"]]
    (jobs_dir / "index.html").write_text(
        tpl_listing.render(**shared, jobs=jobs_list, featured_cities=featured_cities),
        encoding="utf-8"
    )
    count += 1

    for job in jobs_list:
        slug = job["slug"]
        job_dir = jobs_dir / slug
        job_dir.mkdir(exist_ok=True)
        other_jobs = [j for j in jobs_list if j["slug"] != slug]

        # Job national hub
        (job_dir / "index.html").write_text(
            tpl_hub.render(**shared, job=job, other_jobs=other_jobs),
            encoding="utf-8"
        )
        count += 1

        # Job × city pages
        for city in cities:
            mult = regional_multipliers.get(city["slug"], 1.0)
            other_cities = [c for c in cities if c["slug"] != city["slug"]]
            ctx = {
                **shared,
                "job": job,
                "city": city,
                "multiplier": mult,
                "other_cities": other_cities,
                "other_jobs": other_jobs,
            }
            (job_dir / f"{city['slug']}.html").write_text(
                tpl_city.render(**ctx), encoding="utf-8"
            )
            count += 1

    return count


def _extract_template_doc(html):
    """Extract the #template-doc div content from a rendered template page."""
    marker = '<div id="template-doc">'
    start = html.find(marker)
    if start == -1:
        return html
    pos = start + len(marker)
    depth = 1
    while depth > 0 and pos < len(html):
        next_open  = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            pos = next_close + 6
    return html[start:pos]


def build_templates(config, env, nav, base_path):
    templates_file = DATA_DIR / "templates.json"
    if not templates_file.exists():
        return 0

    templates = json.loads(templates_file.read_text())
    year = datetime.now().year
    shared = {**config, "base_path": base_path, "nav": nav, "year": year}

    templates_dir = PUBLIC_DIR / "templates"
    templates_dir.mkdir(exist_ok=True)

    tpl_listing = env.get_template("template-listing.html")
    tpl_page = env.get_template("template-page.html")

    (templates_dir / "index.html").write_text(
        tpl_listing.render(**shared, templates=templates), encoding="utf-8"
    )

    count = 1
    for tmpl in templates:
        other_templates = [t for t in templates if t["slug"] != tmpl["slug"]]
        html = tpl_page.render(**shared, tmpl=tmpl, other_templates=other_templates)
        (templates_dir / f"{tmpl['slug']}.html").write_text(html, encoding="utf-8")
        count += 1

    # Build the downloadable ZIP bundle — clean PDFs via headless Chromium
    css_tmpl = (SITE_ROOT / "static" / "css" / "templates.css").read_text(encoding="utf-8")

    chromium = shutil.which("chromium-browser") or shutil.which("chromium") or shutil.which("google-chrome")

    zip_path = PUBLIC_DIR / "static" / "tradie-templates-bundle.zip"
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        with tempfile.TemporaryDirectory(dir=SITE_ROOT) as tmp:
            for tmpl in templates:
                html_path = templates_dir / f"{tmpl['slug']}.html"
                if not html_path.exists():
                    continue

                # Extract just the #template-doc div — no nav, no sidebar, no wrapper padding
                raw = html_path.read_text(encoding="utf-8")
                doc_content = _extract_template_doc(raw)

                # Build a clean minimal page for PDF rendering
                pdf_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
{css_tmpl}
body {{
    margin: 0;
    padding: 12mm 15mm;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 10pt;
    color: #000;
    background: #fff;
}}
#template-doc {{
    border: none !important;
    border-top: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    min-height: unset !important;
}}
.logo-box-clickable, .doc-logo-box {{
    background: #f0f0f0 !important;
    border: 1px solid #ccc !important;
    color: #999 !important;
    font-size: 8pt !important;
}}
@page {{ margin: 12mm 15mm; size: A4; }}
</style>
</head>
<body>
{doc_content}
</body>
</html>"""

                tmp_html = Path(tmp) / f"{tmpl['slug']}.html"
                tmp_pdf  = Path(tmp) / f"{tmpl['slug']}.pdf"
                tmp_html.write_text(pdf_html, encoding="utf-8")

                if chromium:
                    subprocess.run(
                        [chromium, "--headless=new", "--no-sandbox", "--disable-gpu",
                         "--no-pdf-header-footer",
                         f"--print-to-pdf={tmp_pdf}",
                         f"file://{tmp_html}"],
                        capture_output=True, timeout=30
                    )
                    if tmp_pdf.exists():
                        zf.write(tmp_pdf, f"nz-tradie-templates/{tmpl['slug']}.pdf")
                    else:
                        zf.writestr(f"nz-tradie-templates/{tmpl['slug']}.html", pdf_html)
                        logging.warning(f"PDF failed for {tmpl['slug']}, included HTML instead")
                else:
                    zf.writestr(f"nz-tradie-templates/{tmpl['slug']}.html", pdf_html)

    return count


def build_sitemap(articles, calculators, cities, trades, config, job_pages_count=0):
    base_url = config.get("base_url", "").rstrip("/")
    today = datetime.now().strftime("%Y-%m-%d")
    urls = []

    urls.append({"loc": f"{base_url}/", "priority": "1.0", "changefreq": "daily", "lastmod": today})
    urls.append({"loc": f"{base_url}/tradie-rates/", "priority": "0.9", "changefreq": "weekly", "lastmod": today})
    urls.append({"loc": f"{base_url}/glossary/", "priority": "0.7", "changefreq": "monthly", "lastmod": today})
    urls.append({"loc": f"{base_url}/faq/", "priority": "0.8", "changefreq": "monthly", "lastmod": today})
    urls.append({"loc": f"{base_url}/tax-dates/", "priority": "0.8", "changefreq": "yearly", "lastmod": today})
    urls.append({"loc": f"{base_url}/claim/", "priority": "0.6", "changefreq": "monthly", "lastmod": today})
    # Business profiles
    for slug in load_claimed_businesses():
        urls.append({"loc": f"{base_url}/businesses/{slug}/", "priority": "0.8",
                     "changefreq": "monthly", "lastmod": today})
    for section, pri in [("articles", "0.6"), ("calculators", "0.8"), ("trades", "0.9"),
                          ("jobs", "0.9"), ("locations", "0.7")]:
        urls.append({"loc": f"{base_url}/{section}/", "priority": pri, "changefreq": "weekly", "lastmod": today})

    # Calc category landing pages
    for cat in CALC_CATEGORIES:
        urls.append({"loc": f"{base_url}/calculators/{cat['slug']}/", "priority": "0.85",
                     "changefreq": "monthly", "lastmod": today})

    for a in articles:
        urls.append({"loc": f"{base_url}/articles/{a['slug']}.html", "priority": "0.7",
                     "changefreq": "monthly", "lastmod": a.get("date_iso", today)})
    for c in calculators:
        urls.append({"loc": f"{base_url}/calculators/{c['slug']}.html", "priority": "0.8",
                     "changefreq": "monthly", "lastmod": today})
    for trade in trades:
        urls.append({"loc": f"{base_url}/trades/{trade['slug']}/", "priority": "0.9",
                     "changefreq": "weekly", "lastmod": today})
        for city in cities:
            urls.append({"loc": f"{base_url}/trades/{trade['slug']}/{city['slug']}.html",
                         "priority": "0.8", "changefreq": "monthly", "lastmod": today})
    for city in cities:
        urls.append({"loc": f"{base_url}/locations/{city['slug']}/", "priority": "0.7",
                     "changefreq": "monthly", "lastmod": today})

    estimates_file = DATA_DIR / "job_estimates.json"
    if estimates_file.exists():
        job_data = json.loads(estimates_file.read_text())
        for job_slug in job_data["jobs"]:
            urls.append({"loc": f"{base_url}/jobs/{job_slug}/", "priority": "0.9",
                         "changefreq": "monthly", "lastmod": today})
            for city in cities:
                urls.append({"loc": f"{base_url}/jobs/{job_slug}/{city['slug']}.html",
                             "priority": "0.85", "changefreq": "monthly", "lastmod": today})

    templates_file = DATA_DIR / "templates.json"
    if templates_file.exists():
        tmpl_data = json.loads(templates_file.read_text())
        urls.append({"loc": f"{base_url}/templates/", "priority": "0.9",
                     "changefreq": "monthly", "lastmod": today})
        for t in tmpl_data:
            urls.append({"loc": f"{base_url}/templates/{t['slug']}.html",
                         "priority": "0.85", "changefreq": "monthly", "lastmod": today})

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines += ["  <url>", f"    <loc>{u['loc']}</loc>",
                  f"    <lastmod>{u['lastmod']}</lastmod>",
                  f"    <changefreq>{u['changefreq']}</changefreq>",
                  f"    <priority>{u['priority']}</priority>", "  </url>"]
    lines.append("</urlset>")
    (PUBLIC_DIR / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def build_rss(articles, config):
    base_url = config.get("base_url", "").rstrip("/")
    site_title = config.get("title", "NZ Tradie Tools")
    build_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")

    def esc(s):
        return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    items = []
    for a in articles:
        pub_date = a.get("date_iso", "")
        try:
            pub_date_rss = datetime.strptime(pub_date, "%Y-%m-%d").strftime("%a, %d %b %Y 00:00:00 +0000")
        except Exception:
            pub_date_rss = build_date
        link = f"{base_url}/articles/{a['slug']}.html"
        items.append(
            f"  <item>\n"
            f"    <title>{esc(a.get('page_title', ''))}</title>\n"
            f"    <link>{link}</link>\n"
            f"    <guid isPermaLink=\"true\">{link}</guid>\n"
            f"    <description>{esc(a.get('description', ''))}</description>\n"
            f"    <pubDate>{pub_date_rss}</pubDate>\n"
            f"  </item>"
        )

    rss = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        '  <channel>\n'
        f'    <title>{esc(site_title)}</title>\n'
        f'    <link>{base_url}/</link>\n'
        '    <description>Free calculators, templates and guides for New Zealand tradies.</description>\n'
        '    <language>en-nz</language>\n'
        f'    <lastBuildDate>{build_date}</lastBuildDate>\n'
        f'    <atom:link href="{base_url}/rss.xml" rel="self" type="application/rss+xml"/>\n'
        + "\n".join(items) + "\n"
        '  </channel>\n'
        '</rss>\n'
    )
    (PUBLIC_DIR / "rss.xml").write_text(rss, encoding="utf-8")


def build_robots(config):
    base_url = config.get("base_url", "").rstrip("/")
    (PUBLIC_DIR / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {base_url}/sitemap.xml\n", encoding="utf-8"
    )


def build_ads_txt(config):
    pass


def build_index(articles, calculators, config, env, nav, base_path):
    template = env.get_template("index.html")
    ctx = {
        **config,
        "base_path": base_path,
        "page_title": config["title"],
        "articles": articles[:6],
        "calculators": calculators,
        "nav": nav,
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / "index.html").write_text(template.render(**ctx), encoding="utf-8")


CALC_CATEGORIES = [
    {
        "slug": "tax",
        "title": "Tax & Finance Calculators",
        "description": "Free NZ tax and finance calculators for tradies — GST, PAYE, provisional tax, ACC levy, depreciation, vehicle mileage and more.",
        "slugs": [
            "gst-calculator", "paye-employee-calculator", "provisional-tax-calculator",
            "provisional-tax-topup-calculator", "subcontractor-tax-calculator",
            "acc-levy-calculator", "depreciation-calculator", "vehicle-mileage-calculator",
            "kiwisaver-employer-cost-calculator", "leave-entitlements-calculator",
            "holiday-pay-calculator", "overtime-calculator",
        ],
    },
    {
        "slug": "business",
        "title": "Business & Pricing Calculators",
        "description": "Free NZ tradie business calculators — hourly rate, job costing, quote builder, breakeven, cash flow, markup vs margin and more.",
        "slugs": [
            "hourly-rate-calculator", "job-cost-calculator", "quote-builder-wizard",
            "labour-cost-calculator", "breakeven-calculator", "cash-flow-forecast",
            "markup-margin-calculator", "materials-escalation-calculator",
            "equipment-finance-calculator", "retentions-calculator",
            "apprentice-wage-calculator", "employee-total-cost-calculator",
            "contractor-vs-employee-calculator",
        ],
    },
    {
        "slug": "trade-tools",
        "title": "Trade Tools & Quantity Calculators",
        "description": "Free NZ tradie quantity calculators — concrete, tiles, timber, paint, cable sizing, drainage, scaffolding, earthworks and more.",
        "slugs": [
            "concrete-calculator", "tile-calculator", "paint-calculator",
            "brick-block-calculator", "timber-framing-calculator", "roof-area-calculator",
            "decking-calculator", "fence-calculator", "staircase-calculator",
            "cable-sizing-calculator", "voltage-drop-calculator", "drain-grade-calculator",
            "stormwater-grade-calculator", "retaining-wall-calculator",
            "retaining-wall-load-calculator", "earthworks-calculator",
            "irrigation-calculator", "paving-calculator", "scaffolding-calculator",
        ],
    },
    {
        "slug": "estimators",
        "title": "Project Cost Estimators",
        "description": "Free NZ project cost estimators — bathroom, kitchen, insulation, heat pumps, solar, skip bins, scaffolding hire and more.",
        "slugs": [
            "bathroom-renovation-calculator", "kitchen-renovation-calculator",
            "skip-bin-calculator", "scaffolding-hire-calculator",
            "building-consent-fee-calculator", "h1-insulation-calculator",
            "insulation-calculator", "healthy-homes-cost-estimator",
            "heat-pump-sizing-calculator", "hot-water-cylinder-calculator",
            "solar-savings-calculator", "pool-volume-calculator",
            "carpet-flooring-calculator", "cladding-paint-calculator",
            "waterproofing-calculator",
        ],
    },
]


def build_calc_categories(calculators, config, env, nav, base_path):
    template = env.get_template("calc-category.html")
    by_slug = {c["slug"]: c for c in calculators}
    year = datetime.now().year

    all_cats_meta = [
        {"slug": cat["slug"], "title": cat["title"], "count": len(cat["slugs"])}
        for cat in CALC_CATEGORIES
    ]

    for cat in CALC_CATEGORIES:
        cat_calcs = [by_slug[s] for s in cat["slugs"] if s in by_slug]
        out_dir = PUBLIC_DIR / "calculators" / cat["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        ctx = {
            **config,
            "base_path": base_path,
            "nav": nav,
            "year": year,
            "cat": cat,
            "calcs": cat_calcs,
            "all_categories": all_cats_meta,
            "total_calcs": len(calculators),
        }
        (out_dir / "index.html").write_text(template.render(**ctx), encoding="utf-8")


def build_listing(pages, config, env, section, nav, base_path):
    template = env.get_template("listing.html")
    label = section.title()
    descriptions = {
        "articles": "Free guides, tips and news for New Zealand tradies — tax, licensing, pricing, H&S compliance and more.",
        "calculators": "Free NZ tradie calculators — GST, hourly rate, job cost, depreciation, overtime and 30+ more. All NZ-specific.",
    }
    ctx = {
        **config,
        "base_path": base_path,
        "page_title": f"{label} — {config['title']}",
        "description": descriptions.get(section, config.get("description", "")),
        "pages": pages,
        "section": section,
        "section_label": label,
        "nav": nav,
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / section / "index.html").write_text(template.render(**ctx), encoding="utf-8")


def build_privacy(config, env, nav, base_path):
    template = env.get_template("privacy.html")
    ctx = {
        **config,
        "base_path": base_path,
        "nav": nav,
        "date": datetime.now().strftime("%-d %B %Y"),
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / "privacy").mkdir(exist_ok=True)
    (PUBLIC_DIR / "privacy" / "index.html").write_text(template.render(**ctx), encoding="utf-8")


def build_faq(config, env, nav, base_path):
    template = env.get_template("faq.html")
    ctx = {
        **config,
        "base_path": base_path,
        "nav": nav,
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / "faq").mkdir(exist_ok=True)
    (PUBLIC_DIR / "faq" / "index.html").write_text(template.render(**ctx), encoding="utf-8")


def build_business_profiles(config, env, nav, base_path):
    """Generate a profile page for each claimed business."""
    claimed = load_claimed_businesses()
    if not claimed:
        return 0
    template = env.get_template("business-profile.html")
    biz_dir = PUBLIC_DIR / "businesses"
    biz_dir.mkdir(exist_ok=True)
    year = datetime.now().year
    count = 0
    for slug, business in claimed.items():
        ctx = {
            **config,
            "base_path": base_path,
            "nav": nav,
            "year": year,
            "business": business,
        }
        out_dir = biz_dir / slug
        out_dir.mkdir(exist_ok=True)
        (out_dir / "index.html").write_text(template.render(**ctx), encoding="utf-8")
        count += 1
    return count


def build_claim_page(config, env, nav, base_path):
    template = env.get_template("claim.html")
    ctx = {**config, "base_path": base_path, "nav": nav, "year": datetime.now().year}
    (PUBLIC_DIR / "claim").mkdir(exist_ok=True)
    (PUBLIC_DIR / "claim" / "index.html").write_text(template.render(**ctx), encoding="utf-8")
    # Simple thank-you page
    thankyou_html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="refresh" content="5;url={config.get('base_url','')}/claim/"><title>Thanks! — NZ Tradie Tools</title><link rel="stylesheet" href="{base_path}/static/css/style.css"></head><body><div class="container" style="padding:4rem 1rem;text-align:center"><h1>✅ Claim submitted!</h1><p style="font-size:1.1rem;color:#555">We'll review your listing and email you within 1 business day when your profile page is live.</p><p style="margin-top:1.5rem"><a href="{base_path}/" style="color:#0055a5">← Back to NZ Tradie Tools</a></p></div></body></html>"""
    (PUBLIC_DIR / "claim" / "thankyou.html").write_text(thankyou_html, encoding="utf-8")


def build_tax_dates(config, env, nav, base_path):
    template = env.get_template("tax-dates.html")
    ctx = {
        **config,
        "base_path": base_path,
        "nav": nav,
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / "tax-dates").mkdir(exist_ok=True)
    (PUBLIC_DIR / "tax-dates" / "index.html").write_text(template.render(**ctx), encoding="utf-8")


def build_glossary(config, env, nav, base_path):
    template = env.get_template("glossary.html")
    ctx = {
        **config,
        "base_path": base_path,
        "nav": nav,
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / "glossary").mkdir(exist_ok=True)
    (PUBLIC_DIR / "glossary" / "index.html").write_text(template.render(**ctx), encoding="utf-8")


def build_contact(config, env, nav, base_path):
    template = env.get_template("contact.html")
    ctx = {
        **config,
        "base_path": base_path,
        "page_title": f"Contact — {config['title']}",
        "nav": nav,
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / "contact").mkdir(exist_ok=True)
    (PUBLIC_DIR / "contact" / "index.html").write_text(template.render(**ctx), encoding="utf-8")


def build_tradie_rates(config, nav, base_path):
    base_url = config.get("base_url", "").rstrip("/")
    year = datetime.now().year
    trades = json.loads((DATA_DIR / "trades.json").read_text())
    cities = json.loads((DATA_DIR / "cities.json").read_text())
    top10_dir = DATA_DIR / "top10"

    # Extract rate range from regional_cost_note, e.g. "$75–$130/hr" or "$75-$130/hr"
    def parse_rate(note):
        m = re.search(r'\$(\d+)\s*[–\-—]+\s*\$?(\d+)/hr', note or "")
        if m:
            return f"${m.group(1)}–${m.group(2)}"
        return None

    # Build matrix: trade -> {city_slug: rate_str}
    TRADE_ICONS = {
        "builders": "🏗️", "plumbers": "🔧", "electricians": "⚡",
        "painters": "🖌️", "roofers": "🏠", "landscapers": "🌿",
        "carpenters": "🪚", "gasfitters": "🔥", "plasterers": "🪣",
        "concreters": "🏛️", "drainlayers": "🚰", "tilers": "🔲",
    }
    rows = []
    for trade in trades:
        rate_by_city = {}
        for city in cities:
            f = top10_dir / f"{trade['slug']}-{city['slug']}.json"
            if f.exists():
                data = json.loads(f.read_text())
                rate = parse_rate(data.get("regional_cost_note", ""))
                if rate:
                    rate_by_city[city["slug"]] = rate
        if not rate_by_city:
            continue
        # NZ average: average the mid-points
        mids = []
        for r in rate_by_city.values():
            parts = r.replace("$", "").split("–")
            if len(parts) == 2:
                try:
                    mids.append((int(parts[0]) + int(parts[1])) / 2)
                except ValueError:
                    pass
        if mids:
            avg_mid = sum(mids) / len(mids)
            lo_vals = []
            hi_vals = []
            for r in rate_by_city.values():
                parts = r.replace("$", "").split("–")
                if len(parts) == 2:
                    try:
                        lo_vals.append(int(parts[0]))
                        hi_vals.append(int(parts[1]))
                    except ValueError:
                        pass
            avg_rate = f"${round(sum(lo_vals)/len(lo_vals))}–${round(sum(hi_vals)/len(hi_vals))}" if lo_vals else "—"
        else:
            avg_rate = "—"
        icon = TRADE_ICONS.get(trade["slug"], "🔨")
        rows.append({"trade": trade, "icon": icon, "rates": rate_by_city, "avg": avg_rate})

    # Build header cells
    city_headers = "".join(
        f'<th><a href="{base_url}/locations/{c["slug"]}/">{c["name"]}</a></th>'
        for c in cities
    )
    # Build table rows
    def rate_cell(r):
        if r:
            return f'<td class="rate">{r}</td>'
        return '<td class="na">—</td>'

    tbody_rows = ""
    for row in rows:
        cells = "".join(rate_cell(row["rates"].get(c["slug"])) for c in cities)
        tbody_rows += (
            f'<tr><th><a href="{base_url}/trades/{row["trade"]["slug"]}/">'
            f'{row["icon"]} {row["trade"]["name"]}</a></th>'
            f'{cells}<td class="rate national"><strong>{row["avg"]}</strong></td></tr>'
        )

    # City hub links
    city_links = "".join(
        f'<a href="{base_url}/locations/{c["slug"]}/" style="background:#f0f4fa;padding:.35rem .85rem;'
        f'border-radius:20px;font-size:.85rem;color:#0055a5;text-decoration:none">{c["name"]}</a>'
        for c in cities
    )

    ga_id = config.get("ga_id", "")
    ga_script = ""
    if ga_id:
        ga_script = (
            f"<script async src='https://www.googletagmanager.com/gtag/js?id={ga_id}'></script>"
            f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}"
            f"gtag('js',new Date());gtag('config','{ga_id}');</script>"
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NZ Tradie Hourly Rates {year} — All Trades, All Cities</title>
<meta name="description" content="Compare NZ tradie hourly rates by trade and city for {year}. Builders, plumbers, electricians, painters and more — Auckland, Wellington, Christchurch and all major NZ cities.">
<link rel="canonical" href="{base_url}/tradie-rates/">
<meta property="og:title" content="NZ Tradie Hourly Rates {year} — All Trades, All Cities">
<meta property="og:description" content="Compare NZ tradie hourly rates by trade and city. Updated {year}.">
<meta property="og:type" content="website">
<meta property="og:url" content="{base_url}/tradie-rates/">
<meta property="og:site_name" content="{config.get('title', 'NZ Tradie Tools')}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebPage","name":"NZ Tradie Hourly Rates {year}","description":"Compare NZ tradie hourly rates by trade and city","url":"{base_url}/tradie-rates/"}}</script>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/static/css/style.css">
{ga_script}
<style>
.rate-table-wrap {{ overflow-x: auto; margin: 1.5rem 0; }}
.rate-table {{ border-collapse: collapse; width: 100%; font-size: .82rem; min-width: 900px; }}
.rate-table th, .rate-table td {{ padding: .45rem .6rem; border: 1px solid #ddd; text-align: center; white-space: nowrap; }}
.rate-table thead th {{ background: #0055a5; color: #fff; font-weight: 600; }}
.rate-table thead th:first-child {{ text-align: left; }}
.rate-table tbody tr:nth-child(even) {{ background: #f8f9fa; }}
.rate-table tbody th {{ text-align: left; font-weight: 600; background: #f0f4fa; }}
.rate-table tbody th a {{ color: #0055a5; text-decoration: none; }}
td.rate {{ color: #1a1a1a; }}
td.na {{ color: #bbb; }}
td.national {{ background: #e8f0fe; font-weight: 600; }}
.rate-note {{ background: #fff8e1; border: 1px solid #ffe082; border-radius: 6px; padding: 1rem 1.2rem; font-size: .88rem; margin: 1.5rem 0; }}
.cta-box {{ background: #0055a5; color: #fff; border-radius: 8px; padding: 1.5rem; margin: 2rem 0; text-align: center; }}
.cta-box a {{ color: #fff; font-weight: 600; text-decoration: underline; }}
</style>
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="/" class="logo">🔧 NZ Tradie Tools</a>
    <nav class="main-nav">
      <a href="/">Home</a><a href="/trades/">Find a Tradie</a><a href="/calculators/">Calculators</a><a href="/articles/">Articles</a><a href="/templates/">Templates</a>
    </nav>
  </div>
</header>

<section class="hero" style="padding:3rem 0">
  <div class="container">
    <h1>NZ Tradie Hourly Rates {year}</h1>
    <p>Compare what tradies charge across all major NZ cities — updated {year}. Rates shown are typical labour-only hourly rates (ex GST unless noted).</p>
  </div>
</section>

<div class="container" style="max-width:1200px">
  <div class="rate-note">
    ℹ️ <strong>About these rates:</strong> Compiled from local job data across Auckland, Wellington, Christchurch and 17 other NZ cities. Rates are labour-only and exclude GST unless stated. Emergency callouts, after-hours work, and specialist jobs typically add 30–80%. Always get 3 quotes. <a href="/calculators/hourly-rate-calculator.html">Calculate your own rate →</a>
  </div>

  <div class="rate-table-wrap">
    <table class="rate-table">
      <thead>
        <tr>
          <th>Trade</th>
          {city_headers}
          <th>NZ Average</th>
        </tr>
      </thead>
      <tbody>
        {tbody_rows}
      </tbody>
    </table>
  </div>

  <div class="cta-box">
    <p style="margin:0 0 .5rem;font-size:1.1rem;font-weight:700">Not sure if your quote is fair?</p>
    <p style="margin:0 0 1rem;opacity:.9">Use our free job cost calculator to check any quote against typical NZ rates.</p>
    <a href="/calculators/job-cost-calculator.html" style="background:#fff;color:#0055a5;padding:.65rem 1.4rem;border-radius:5px;display:inline-block">Check my quote →</a>
  </div>

  <div class="article-body">
    <h2>Why Rates Vary by City</h2>
    <p>Auckland consistently has the highest tradie rates in New Zealand, driven by higher overheads, longer travel times, and strong demand. Wellington rates are typically 5–15% below Auckland. Christchurch and Hamilton sit in the mid-range, while smaller cities like Invercargill, Gisborne, and Whanganui tend to have the lowest rates — though smaller contractor pools can mean less competitive quotes for specialist work.</p>

    <h2>What's Included in These Rates</h2>
    <ul>
      <li><strong>Labour only</strong> — materials, consent fees, and site costs are additional</li>
      <li><strong>Standard hours</strong> — after-hours and emergency rates are typically 50–100% higher</li>
      <li><strong>Experienced tradespeople</strong> — apprentice rates are typically 30–50% lower</li>
      <li><strong>Ex GST</strong> unless stated — add 15% for GST-registered tradies</li>
    </ul>

    <h2>How to Use These Rates</h2>
    <p>Use this table as a sanity check on quotes, not as a fixed price guide. A quote significantly below the typical range may indicate a less experienced operator or one cutting corners on compliance. A quote well above range warrants asking for a breakdown.</p>
    <p>For job-specific pricing (e.g. bathroom renovation, deck, re-roofing), use our <a href="/jobs/">job cost estimator</a> which applies city-specific multipliers to typical job costs.</p>

    <h2>Find Top-Rated Tradies by City</h2>
    <div style="display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.75rem">
      {city_links}
    </div>
  </div>
</div>

<footer class="site-footer">
  <div class="container">
    <div>
      <p style="color:rgba(255,255,255,.85);font-weight:700;margin-bottom:.2rem">{config.get('title', 'NZ Tradie Tools')}</p>
      <p>Free calculators, templates and guides for New Zealand tradies.</p>
    </div>
    <div style="text-align:right">
      <p><a href="/privacy/">Privacy Policy</a></p>
      <p><a href="/contact/">Contact</a></p>
      <p style="margin-top:.5rem">&copy; {year} {config.get('title', 'NZ Tradie Tools')}</p>
    </div>
  </div>
</footer>
</body>
</html>"""

    out_dir = PUBLIC_DIR / "tradie-rates"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    return len(rows)


if __name__ == "__main__":
    build()
