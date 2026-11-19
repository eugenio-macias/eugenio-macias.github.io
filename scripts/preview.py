#!/usr/bin/env python3
"""Local preview: expand the default layout and serve the site without Ruby/Jekyll."""
from __future__ import annotations

import re
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAYOUT = (ROOT / "_layouts" / "default.html").read_text()

try:
    import markdown as mdlib
except ImportError:
    mdlib = None

LIQUID_REL = re.compile(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}")
LIQUID_BASE = re.compile(r"\{\{\s*site\.baseurl\s*\}\}")
LIQUID_TITLE = re.compile(r"\{\{\s*page\.title\s*\}\}")
LIQUID_SITE_TITLE = re.compile(r"\{\{\s*site\.title\s*\}\}")
LIQUID_TAG = re.compile(r"\{%.*?%\}", re.S)
IF_HOME = re.compile(
    r"\{%\s*if\s+page\.title\s*==\s*\"Home\"\s*%\}(.*?)\{%\s*endif\s*%\}",
    re.S,
)


def split_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta = {}
    for line in parts[1].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, parts[2]


def expand(html: str, title: str, is_home: bool) -> str:
    def keep_home(m):
        return m.group(1) if is_home else ""

    html = IF_HOME.sub(keep_home, html)
    html = LIQUID_REL.sub(lambda m: m.group(1), html)
    html = LIQUID_BASE.sub("", html)
    html = LIQUID_TITLE.sub(title, html)
    html = LIQUID_SITE_TITLE.sub("Eugenio Macías", html)
    html = LIQUID_TAG.sub("", html)
    return html


def render_page(path: Path) -> bytes:
    meta, body = split_front_matter(path.read_text())
    title = meta.get("title", "")
    is_home = title == "Home"
    if path.suffix == ".md" and mdlib is not None:
        body_html = mdlib.markdown(body, extensions=["extra", "nl2br"])
    else:
        body_html = body
    page = LAYOUT.replace("{{ content }}", body_html)
    return expand(page, title, is_home).encode()


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        raw = self.path.split("?", 1)[0]
        if raw.endswith("/") and raw != "/":
            raw = raw[:-1]
        mapping = {
            "/": ROOT / "index.md",
            "/index.html": ROOT / "index.md",
            "/projects": ROOT / "projects.md",
            "/notes": ROOT / "notes.md",
            "/classes-i-have-taken": ROOT / "classes-i-have-taken.md",
            "/music-repertoire": ROOT / "music-repertoire.md",
            "/skills-interests": ROOT / "skills-interests.md",
            "/education": ROOT / "education.md",
            "/experience": ROOT / "experience.md",
            "/awards": ROOT / "awards.md",
        }
        src = mapping.get(raw)
        if src is None and raw.endswith(".html"):
            cand = ROOT / (raw[1:].replace(".html", "") + ".md")
            if cand.exists():
                src = cand
        if src and src.exists():
            data = render_page(src)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        return super().do_GET()


if __name__ == "__main__":
    port = 4173
    httpd = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"preview http://127.0.0.1:{port}/")
    httpd.serve_forever()
