#!/usr/bin/env python3
"""
ChemWiki static site builder.

Turns Markdown articles (with LaTeX maths and \\ce{} chemical equations)
into a Wikipedia-style static website in the ./site folder.

Usage:
    python build.py            # build the site into ./site
    python build.py --serve    # build, then preview at http://localhost:8000
"""

import datetime as dt
import html
import json
import os
import re
import shutil
import urllib.parse
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
ARTICLES = CONTENT / "articles"
STATIC = ROOT / "static"
MEDIA = ROOT / "media"
TEMPLATES = ROOT / "templates"
OUT = ROOT / "site"

CONFIG = yaml.safe_load((ROOT / "config.yml").read_text(encoding="utf-8"))
BASE = CONFIG.get("base_path", "").rstrip("/")          # "" or "/repo-name"
SITE_URL = CONFIG.get("site_url", "").rstrip("/")         # https://yourdomain.com


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_]+", "-", text).strip("-")


def url(path: str) -> str:
    """Site-relative URL that respects base_path."""
    return f"{BASE}/{path.lstrip('/')}"


def read_front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    else:
        meta, body = {}, text
    return meta, body.lstrip("\n")


# --------------------------------------------------------------------------
# Maths protection: keep LaTeX away from the Markdown parser
# --------------------------------------------------------------------------

CODE_RE = re.compile(r"(```.*?```|~~~.*?~~~|`[^`\n]+`)", re.S)
MATH_PATTERNS = [
    # $$ ... $$  and  \[ ... \]  -> display maths
    (re.compile(r"\$\$(.+?)\$\$", re.S), True),
    (re.compile(r"\\\[(.+?)\\\]", re.S), True),
    # \( ... \)  and  $ ... $   -> inline maths
    (re.compile(r"\\\((.+?)\\\)", re.S), False),
    (re.compile(r"(?<![\\$])\$(?=\S)((?:\\.|[^$\\\n])+?)(?<=\S)\$(?!\d)"), False),
]


class MathStash:
    def __init__(self):
        self.items = []

    def protect(self, text: str, wikilink_sub=None) -> str:
        # 1. hide code so "$" inside code is left alone
        code = []

        def hide_code(m):
            code.append(m.group(0))
            return f"CODEPH{len(code) - 1}X"

        text = CODE_RE.sub(hide_code, text)

        # 2. pull maths out and replace with placeholders
        for pattern, display in MATH_PATTERNS:
            def stash(m, display=display):
                self.items.append((m.group(1).strip(), display))
                return f"MATHPH{len(self.items) - 1}X"
            text = pattern.sub(stash, text)

        # 3. a literal dollar sign is written \$
        text = text.replace(r"\$", "&#36;")

        # 4. wiki links (not inside code)
        if wikilink_sub:
            text = WIKILINK_RE.sub(wikilink_sub, text)

        # 5. put code back
        return re.sub(r"CODEPH(\d+)X", lambda m: code[int(m.group(1))], text)

    def restore(self, html_text: str) -> str:
        def render(i):
            tex, display = self.items[i]
            tex = html.escape(tex, quote=False)
            if display:
                return f'<div class="math display">{tex}</div>'
            return f'<span class="math inline">{tex}</span>'

        html_text = re.sub(r"<p>\s*MATHPH(\d+)X\s*</p>",
                           lambda m: render(int(m.group(1))), html_text)
        return re.sub(r"MATHPH(\d+)X", lambda m: render(int(m.group(1))), html_text)


# --------------------------------------------------------------------------
# Wiki links:  [[Benzene]]  or  [[Ideal gas law|the gas law]]
# --------------------------------------------------------------------------

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(#[^\]|]+)?(?:\|([^\]]+))?\]\]")


def make_wikilink_sub(lookup):
    def sub(m):
        target, anchor, label = m.group(1).strip(), m.group(2) or "", m.group(3)
        label = (label or target).strip()
        key = target.lower()
        if key in lookup:
            slug = lookup[key]
            return f'<a href="{url("wiki/" + slug + "/")}{anchor}">{label}</a>'
        # page doesn't exist yet -> red link, like Wikipedia
        return (f'<a class="new" href="{url("special/missing/")}?title='
                f'{urllib.parse.quote(target)}" title="{html.escape(target)} '
                f'(page does not exist)">{label}</a>')
    return sub


# --------------------------------------------------------------------------
# Markdown rendering
# --------------------------------------------------------------------------

MD_EXTENSIONS = ["abbr", "attr_list", "def_list", "fenced_code", "footnotes",
                 "md_in_html", "tables", "toc", "sane_lists", "smarty", "admonition"]
MD_CONFIG = {
    "toc": {"permalink": False, "toc_depth": "2-4"},
    "footnotes": {"BACKLINK_TEXT": "↑"},
}


def render_markdown(text: str, wikilink_sub):
    stash = MathStash()
    text = stash.protect(text, wikilink_sub)
    md = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG)
    body = md.convert(text)
    body = stash.restore(body)
    return body, md.toc_tokens


def render_inline(text, wikilink_sub) -> str:
    body, _ = render_markdown(str(text), wikilink_sub)
    return re.sub(r"^<p>(.*)</p>$", r"\1", body.strip(), flags=re.S)


def build_toc(tokens) -> str:
    def walk(items):
        out = ["<ul>"]
        for t in items:
            out.append(f'<li><a href="#{t["id"]}"><span class="toctext">'
                       f'{t["name"]}</span></a>')
            if t["children"]:
                out.append(walk(t["children"]))
            out.append("</li>")
        out.append("</ul>")
        return "".join(out)

    # toc_tokens start at the top-level heading present (h2 in our articles)
    flat = []
    for t in tokens:
        flat.extend(t["children"] if t["level"] == 1 else [t])
    if len(flat) < 3:
        return ""
    return ('<nav id="toc" class="toc" aria-labelledby="toc-title">'
            '<div class="toctitle"><h2 id="toc-title">Contents</h2>'
            '<button class="toctoggle" type="button">hide</button></div>'
            f'{walk(flat)}</nav>')


def plain_text(html_text: str) -> str:
    text = re.sub(r'<(span|div) class="math[^"]*">.*?</\1>', " ", html_text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


# --------------------------------------------------------------------------
# Templates
# --------------------------------------------------------------------------

def load_template(name):
    return (TEMPLATES / name).read_text(encoding="utf-8")


def fill(template: str, **values) -> str:
    """Replace {{ name }} placeholders."""
    return re.sub(r"{{\s*(\w+)\s*}}",
                  lambda m: str(values.get(m.group(1), "")), template)


def page(title, content, *, description="", path="", tabs="", extra_head=""):
    canonical = f"{SITE_URL}{url(path)}" if SITE_URL else ""
    return fill(
        load_template("base.html"),
        title=html.escape(title),
        site_name=html.escape(CONFIG["site_name"]),
        tagline=html.escape(CONFIG.get("tagline", "")),
        description=html.escape(description or CONFIG.get("tagline", "")),
        canonical=f'<link rel="canonical" href="{canonical}">' if canonical else "",
        content=content,
        tabs=tabs,
        extra_head=extra_head,
        root=BASE,
        year=dt.date.today().year,
        footer_text=CONFIG.get("footer_text", ""),
    )


def write(path: str, text: str):
    target = OUT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------

def load_articles():
    articles = []
    for f in sorted(ARTICLES.glob("*.md")):
        meta, body = read_front_matter(f)
        slug = meta.get("slug") or f.stem
        updated = meta.get("updated") or dt.date.fromtimestamp(f.stat().st_mtime)
        articles.append({
            "file": f, "slug": slug, "body": body,
            "title": meta.get("title", f.stem.replace("-", " ").capitalize()),
            "summary": meta.get("summary", ""),
            "categories": meta.get("categories", []) or [],
            "aliases": meta.get("aliases", []) or [],
            "infobox": meta.get("infobox"),
            "updated": updated if isinstance(updated, dt.date) else
                       dt.date.fromisoformat(str(updated)),
        })
    return articles


def build_infobox(box, title, wikilink_sub) -> str:
    if not box:
        return ""
    rows = [f'<caption class="infobox-title">{html.escape(box.get("title", title))}</caption>']
    if box.get("image"):
        img = box["image"]
        src = url(img) if img.startswith("/") else img
        rows.append(f'<tr><td colspan="2" class="infobox-image">'
                    f'<img src="{src}" alt="{html.escape(box.get("caption", title))}">'
                    + (f'<div class="infobox-caption">{render_inline(box["caption"], wikilink_sub)}</div>'
                       if box.get("caption") else "")
                    + "</td></tr>")
    for key, value in (box.get("rows") or {}).items():
        if value is None or value == "":
            rows.append(f'<tr><th colspan="2" class="infobox-header">{html.escape(str(key))}</th></tr>')
        else:
            rows.append(f'<tr><th scope="row">{html.escape(str(key))}</th>'
                        f'<td>{render_inline(value, wikilink_sub)}</td></tr>')
    return f'<table class="infobox">{"".join(rows)}</table>'


def category_links(cats):
    if not cats:
        return ""
    links = " | ".join(f'<a href="{url("category/" + slugify(c) + "/")}">{html.escape(c)}</a>'
                       for c in cats)
    return f'<div id="catlinks" class="catlinks"><a href="{url("special/categories/")}">Categories</a>: {links}</div>'


def article_tabs(slug, active="article"):
    def tab(name, label, href):
        cls = ' class="selected"' if name == active else ""
        return f'<li{cls}><a href="{href}">{label}</a></li>'
    return ('<ul class="tabs left">'
            + tab("article", "Article", url(f"wiki/{slug}/"))
            + "</ul><ul class=\"tabs right\">"
            + tab("read", "Read", url(f"wiki/{slug}/"))
            + tab("source", "View source", url(f"source/{slug}.md"))
            + "</ul>")


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(STATIC, OUT / "static")
    if MEDIA.exists():
        shutil.copytree(MEDIA, OUT / "media")

    articles = load_articles()
    lookup = {}
    for a in articles:
        lookup[a["title"].lower()] = a["slug"]
        lookup[a["slug"].lower()] = a["slug"]
        for alias in a["aliases"]:
            lookup[str(alias).lower()] = a["slug"]
    wikilink_sub = make_wikilink_sub(lookup)

    categories = {}
    search_index = []

    # ---- articles ----------------------------------------------------------
    for a in articles:
        body, toc_tokens = render_markdown(a["body"], wikilink_sub)

        # Footnotes become a "References" section
        if 'class="footnote"' in body:
            body = body.replace('<div class="footnote">',
                                '<h2 id="references">References</h2><div class="footnote reflist">', 1)
            toc_tokens = toc_tokens + [{"level": 2, "id": "references",
                                        "name": "References", "children": []}]

        # Contents box goes just before the first section heading
        toc = build_toc(toc_tokens)
        if toc and "<h2" in body:
            i = body.index("<h2")
            body = body[:i] + toc + body[i:]

        infobox = build_infobox(a["infobox"], a["title"], wikilink_sub)
        content = fill(load_template("article.html"),
                       title=html.escape(a["title"]),
                       site_name=html.escape(CONFIG["site_name"]),
                       infobox=infobox, body=body,
                       categories=category_links(a["categories"]),
                       updated=f'{a["updated"].day} {a["updated"]:%B %Y}')
        write(f"wiki/{a['slug']}/index.html",
              page(a["title"], content, description=a["summary"],
                   path=f"wiki/{a['slug']}/", tabs=article_tabs(a["slug"])))

        # raw Markdown, so "View source" works
        src = OUT / "source" / f"{a['slug']}.md"
        src.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(a["file"], src)

        for c in a["categories"]:
            categories.setdefault(c, []).append(a)
        search_index.append({"t": a["title"], "s": a["slug"], "d": a["summary"],
                             "a": [str(x) for x in a["aliases"]],
                             "x": plain_text(body)[:3000]})

    # ---- category pages ----------------------------------------------------
    for cat, items in categories.items():
        lis = "".join(f'<li><a href="{url("wiki/" + i["slug"] + "/")}">{html.escape(i["title"])}</a></li>'
                      for i in sorted(items, key=lambda i: i["title"].lower()))
        content = (f'<h1 class="firstHeading">Category: {html.escape(cat)}</h1>'
                   f'<div class="mw-body-content"><p>The following {len(items)} '
                   f'page{"s are" if len(items) != 1 else " is"} in this category.</p>'
                   f'<ul class="columns">{lis}</ul></div>')
        write(f"category/{slugify(cat)}/index.html", page(f"Category:{cat}", content,
              path=f"category/{slugify(cat)}/"))

    cat_list = "".join(f'<li><a href="{url("category/" + slugify(c) + "/")}">{html.escape(c)}</a> ({len(v)})</li>'
                       for c, v in sorted(categories.items()))
    write("special/categories/index.html", page("Categories",
          f'<h1 class="firstHeading">Categories</h1><div class="mw-body-content"><ul class="columns">{cat_list}</ul></div>',
          path="special/categories/"))

    # ---- all pages ---------------------------------------------------------
    all_list = "".join(f'<li><a href="{url("wiki/" + a["slug"] + "/")}">{html.escape(a["title"])}</a></li>'
                       for a in sorted(articles, key=lambda a: a["title"].lower()))
    write("special/all-pages/index.html", page("All pages",
          f'<h1 class="firstHeading">All pages</h1><div class="mw-body-content"><ul class="columns">{all_list}</ul></div>',
          path="special/all-pages/"))

    # ---- search, random, missing page ---------------------------------------
    write("static/search-index.json", json.dumps(search_index, ensure_ascii=False))
    write("search/index.html", page("Search", load_template("search.html"), path="search/"))
    write("special/random/index.html", page("Random article",
          '<h1 class="firstHeading">Random article</h1><p id="random-msg">Picking an article…</p>'
          '<script>document.addEventListener("DOMContentLoaded",()=>Wiki.random());</script>'))
    write("special/missing/index.html", page("Page not found",
          '<h1 class="firstHeading" id="missing-title">This page does not exist yet</h1>'
          '<div class="mw-body-content"><p>Nobody has written this article yet. To create it, add a '
          'Markdown file to <code>content/articles/</code> and rebuild the site.</p>'
          '<p><a href="' + url("search/") + '">Search the wiki</a> instead.</p></div>'
          '<script>const t=new URLSearchParams(location.search).get("title");'
          'if(t)document.getElementById("missing-title").textContent=t+" — this page does not exist yet";</script>'))
    write("404.html", page("Page not found",
          '<h1 class="firstHeading">Page not found</h1><div class="mw-body-content">'
          f'<p>There is no page at this address. Try the <a href="{url("search/")}">search</a> '
          f'or go to the <a href="{url("")}">Main Page</a>.</p></div>'))

    # ---- main page ---------------------------------------------------------
    home_meta, home_body = read_front_matter(CONTENT / "home.md")
    intro, _ = render_markdown(home_body, wikilink_sub)
    featured = next((a for a in articles if a["slug"] == CONFIG.get("featured_article")), None)
    featured_html = ""
    if featured:
        featured_html = (f'<p>{render_inline(featured["summary"], wikilink_sub)} '
                         f'(<a href="{url("wiki/" + featured["slug"] + "/")}"><b>Full article…</b></a>)</p>')
    recent = sorted(articles, key=lambda a: a["updated"], reverse=True)[:8]
    recent_html = "".join(f'<li><a href="{url("wiki/" + a["slug"] + "/")}">{html.escape(a["title"])}</a></li>'
                          for a in recent)
    home = fill(load_template("home.html"),
                site_name=html.escape(CONFIG["site_name"]),
                tagline=html.escape(CONFIG.get("tagline", "")),
                count=len(articles),
                intro=intro,
                featured_title=html.escape(featured["title"]) if featured else "",
                featured=featured_html,
                recent=recent_html,
                categories=cat_list,
                root=BASE)
    write("index.html", page(home_meta.get("title", "Main Page"), home, path=""))

    # ---- sitemap + robots --------------------------------------------------
    if SITE_URL:
        urls = [("", dt.date.today())] + [(f"wiki/{a['slug']}/", a["updated"]) for a in articles]
        urls += [(f"category/{slugify(c)}/", dt.date.today()) for c in categories]
        entries = "".join(f"<url><loc>{SITE_URL}{url(p)}</loc><lastmod>{d.isoformat()}</lastmod></url>"
                          for p, d in urls)
        write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
              f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{entries}</urlset>\n')
        write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}{url('sitemap.xml')}\n")

    print(f"Built {len(articles)} articles and {len(categories)} categories into {OUT}")


def serve(port=8000):
    import http.server
    import functools
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
    print(f"Previewing at http://localhost:{port}  (Ctrl+C to stop)")
    http.server.ThreadingHTTPServer(("", port), handler).serve_forever()


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        serve()
