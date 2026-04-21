#!/usr/bin/env /usr/bin/python3
"""NZ Tradie Tools — static site generator."""

import json
import re
import shutil
from datetime import datetime
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

SITE_ROOT = Path(__file__).parent
CONTENT_DIR = SITE_ROOT / "content"
LAYOUTS_DIR = SITE_ROOT / "layouts"
STATIC_DIR = SITE_ROOT / "static"
DATA_DIR = SITE_ROOT / "data"
PUBLIC_DIR = SITE_ROOT / "docs"
CONFIG_FILE = SITE_ROOT / "site.json"

MD = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list"])


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


def build():
    config = load_config()
    base_path = config.get("base_path", "")

    nav = [
        {"label": item["label"], "url": base_path + item["url"]}
        for item in config.get("nav", [])
    ]

    env = Environment(loader=FileSystemLoader(str(LAYOUTS_DIR)))

    PUBLIC_DIR.mkdir(exist_ok=True)
    (PUBLIC_DIR / "articles").mkdir(exist_ok=True)
    (PUBLIC_DIR / "calculators").mkdir(exist_ok=True)
    (PUBLIC_DIR / "trades").mkdir(exist_ok=True)
    (PUBLIC_DIR / "locations").mkdir(exist_ok=True)
    (PUBLIC_DIR / ".nojekyll").touch()

    if STATIC_DIR.exists():
        for f in STATIC_DIR.rglob("*"):
            if f.is_file():
                dest = PUBLIC_DIR / "static" / f.relative_to(STATIC_DIR)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dest)

    articles = []
    calculators = []

    articles_dir = CONTENT_DIR / "articles"
    if articles_dir.exists():
        for md_file in sorted(articles_dir.glob("*.md"), reverse=True):
            page = process_page(md_file, config, env, "base.html", "articles", nav, base_path)
            if page and not page.get("draft"):
                articles.append(page)

    calcs_dir = CONTENT_DIR / "calculators"
    if calcs_dir.exists():
        for md_file in sorted(calcs_dir.glob("*.md")):
            page = process_page(md_file, config, env, "calculator.html", "calculators", nav, base_path)
            if page and not page.get("draft"):
                calculators.append(page)

    build_index(articles, calculators, config, env, nav, base_path)
    build_listing(articles, config, env, "articles", nav, base_path)
    build_listing(calculators, config, env, "calculators", nav, base_path)
    build_contact(config, env, nav, base_path)

    trades_count, locations_count = build_trades_and_locations(config, env, nav, base_path)

    cities = json.loads((DATA_DIR / "cities.json").read_text())
    trades_data = json.loads((DATA_DIR / "trades.json").read_text())
    build_sitemap(articles, calculators, cities, trades_data, config)
    build_robots(config)

    print(f"Built: {len(articles)} articles, {len(calculators)} calculators, "
          f"{trades_count} trade pages, {locations_count} location pages")
    return articles, calculators


def process_page(md_file, config, env, layout_name, section, nav, base_path):
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
        "nav": nav,
        "year": datetime.now().year,
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
            ctx = {
                **shared,
                "trade": trade,
                "city": city,
                "businesses": data.get("businesses", []),
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


def build_sitemap(articles, calculators, cities, trades, config):
    base_url = config.get("base_url", "").rstrip("/")
    today = datetime.now().strftime("%Y-%m-%d")
    urls = []

    urls.append({"loc": f"{base_url}/", "priority": "1.0", "changefreq": "daily", "lastmod": today})
    for section, pri in [("articles", "0.6"), ("calculators", "0.8"), ("trades", "0.9")]:
        urls.append({"loc": f"{base_url}/{section}/", "priority": pri, "changefreq": "weekly", "lastmod": today})

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
                         "priority": "0.8", "changefreq": "weekly", "lastmod": today})
    for city in cities:
        urls.append({"loc": f"{base_url}/locations/{city['slug']}/", "priority": "0.7",
                     "changefreq": "weekly", "lastmod": today})

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines += ["  <url>", f"    <loc>{u['loc']}</loc>",
                  f"    <lastmod>{u['lastmod']}</lastmod>",
                  f"    <changefreq>{u['changefreq']}</changefreq>",
                  f"    <priority>{u['priority']}</priority>", "  </url>"]
    lines.append("</urlset>")
    (PUBLIC_DIR / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def build_robots(config):
    base_url = config.get("base_url", "").rstrip("/")
    (PUBLIC_DIR / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {base_url}/sitemap.xml\n", encoding="utf-8"
    )


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


def build_listing(pages, config, env, section, nav, base_path):
    template = env.get_template("listing.html")
    label = section.title()
    ctx = {
        **config,
        "base_path": base_path,
        "page_title": f"{label} — {config['title']}",
        "pages": pages,
        "section": section,
        "section_label": label,
        "nav": nav,
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / section / "index.html").write_text(template.render(**ctx), encoding="utf-8")


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


if __name__ == "__main__":
    build()
