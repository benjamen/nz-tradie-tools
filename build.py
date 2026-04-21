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
PUBLIC_DIR = SITE_ROOT / "docs"
CONFIG_FILE = SITE_ROOT / "site.json"

MD = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list"])


def load_config():
    return json.loads(CONFIG_FILE.read_text())


def parse_frontmatter(text):
    """Split YAML frontmatter from markdown body."""
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


def slugify(title):
    s = title.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return s.strip("-")


def build():
    config = load_config()
    env = Environment(loader=FileSystemLoader(str(LAYOUTS_DIR)))

    PUBLIC_DIR.mkdir(exist_ok=True)
    (PUBLIC_DIR / "articles").mkdir(exist_ok=True)
    (PUBLIC_DIR / "calculators").mkdir(exist_ok=True)

    # Copy static assets
    if STATIC_DIR.exists():
        for f in STATIC_DIR.rglob("*"):
            if f.is_file():
                dest = PUBLIC_DIR / "static" / f.relative_to(STATIC_DIR)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dest)

    articles = []
    calculators = []

    # Process articles
    articles_dir = CONTENT_DIR / "articles"
    if articles_dir.exists():
        for md_file in sorted(articles_dir.glob("*.md"), reverse=True):
            page = process_page(md_file, config, env, "base.html", "articles")
            if page and not page.get("draft"):
                articles.append(page)

    # Process calculators
    calcs_dir = CONTENT_DIR / "calculators"
    if calcs_dir.exists():
        for md_file in sorted(calcs_dir.glob("*.md")):
            page = process_page(md_file, config, env, "calculator.html", "calculators")
            if page and not page.get("draft"):
                calculators.append(page)

    # Build index page
    build_index(articles, calculators, config, env)

    # Build articles listing
    build_listing(articles, config, env, "articles")

    # Build calculators listing
    build_listing(calculators, config, env, "calculators")

    # Build contact page
    build_contact(config, env)

    print(f"Built: {len(articles)} articles, {len(calculators)} calculators")
    return articles, calculators


def process_page(md_file, config, env, layout_name, section):
    text = md_file.read_text(encoding="utf-8")
    front, body = parse_frontmatter(text)

    if not front.get("title"):
        return None

    slug = md_file.stem
    html_body = render_markdown(body)

    # Inject affiliate links if configured
    for name, url in config.get("affiliates", {}).items():
        # Only replace plain text references, not existing links
        html_body = re.sub(
            rf'(?<!["\'])(\b{re.escape(name.title())}\b)(?!["\'])',
            rf'<a href="{url}" rel="sponsored noopener" target="_blank">\1</a>',
            html_body,
            count=1,
        )

    try:
        template = env.get_template(layout_name)
    except Exception:
        template = env.get_template("base.html")

    date_val = front.get("date", "")
    if hasattr(date_val, "strftime"):
        date_str = date_val.strftime("%-d %B %Y")
    else:
        date_str = str(date_val)

    tags = front.get("tags", [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",")]

    ctx = {
        **config,
        "page_title": front.get("title"),
        "title": front.get("title"),
        "description": front.get("description", front.get("title")),
        "date": date_str,
        "author": front.get("author", config.get("author", "")),
        "tags": tags,
        "content": html_body,
        "slug": slug,
        "section": section,
        "url": f"/{section}/{slug}.html",
        "draft": front.get("draft", False),
        "calculator_html": front.get("calculator_html", ""),
        "nav": config.get("nav", []),
        "year": datetime.now().year,
    }

    rendered = template.render(**ctx)
    out_path = PUBLIC_DIR / section / f"{slug}.html"
    out_path.write_text(rendered, encoding="utf-8")
    return ctx


def build_index(articles, calculators, config, env):
    template = env.get_template("index.html")
    ctx = {
        **config,
        "page_title": config["title"],
        "articles": articles[:6],
        "calculators": calculators,
        "nav": config.get("nav", []),
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / "index.html").write_text(template.render(**ctx), encoding="utf-8")


def build_listing(pages, config, env, section):
    template = env.get_template("listing.html")
    label = section.title()
    ctx = {
        **config,
        "page_title": f"{label} — {config['title']}",
        "pages": pages,
        "section": section,
        "section_label": label,
        "nav": config.get("nav", []),
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / section / "index.html").write_text(template.render(**ctx), encoding="utf-8")


def build_contact(config, env):
    template = env.get_template("contact.html")
    ctx = {
        **config,
        "page_title": f"Contact — {config['title']}",
        "nav": config.get("nav", []),
        "year": datetime.now().year,
    }
    (PUBLIC_DIR / "contact").mkdir(exist_ok=True)
    (PUBLIC_DIR / "contact" / "index.html").write_text(template.render(**ctx), encoding="utf-8")


if __name__ == "__main__":
    build()
