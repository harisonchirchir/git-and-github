#!/usr/bin/env python3
"""Check local links and fragments in the repository's static HTML pages."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        for key in ("id", "name"):
            if key in attributes:
                self.anchors.add(attributes[key])
        if tag == "a" and "href" in attributes:
            self.links.append(attributes["href"])
        if tag in {"link", "script", "img"}:
            key = "href" if tag == "link" else "src"
            if key in attributes:
                self.links.append(attributes[key])


def load_page(path):
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def resolve_target(source, url_path):
    if url_path.startswith("/"):
        target = ROOT / unquote(url_path.lstrip("/"))
    elif url_path:
        target = source.parent / unquote(url_path)
    else:
        target = source

    target = target.resolve()
    if not target.is_relative_to(ROOT):
        return None
    if target.is_dir():
        target /= "index.html"
    return target


def main():
    pages = {path: load_page(path) for path in ROOT.rglob("*.html")}
    errors = []

    for source, parser in pages.items():
        for link in parser.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue

            target = resolve_target(source, parsed.path)
            if target is None or not target.is_file():
                errors.append(f"{source.relative_to(ROOT)}: missing target {link}")
                continue

            fragment = unquote(parsed.fragment)
            if fragment and target in pages and fragment not in pages[target].anchors:
                errors.append(
                    f"{source.relative_to(ROOT)}: missing fragment #{fragment} in "
                    f"{target.relative_to(ROOT)}"
                )

    if errors:
        print("\n".join(errors))
        return 1

    print(f"Checked {len(pages)} HTML pages; all local links and fragments resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
