#!/usr/bin/env python3
"""Check required course navigation and lesson-learning elements."""

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSONS = (
    "lab_o1",
    "lab_02",
    "lab_03",
    "lab_04",
    "lab_05",
    "lab_06",
    "lab_07",
    "lab_08",
    "lab_09",
    "lab_10",
)


class CurriculumParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.classes = set()
        self.ids = set()
        self.tags = set()
        self.text = []
        self.lesson_cards = []
        self.search_input = False
        self.level_select = False
        self.live_status = False
        self.navigation_link_count = 0
        self.in_lesson_navigation = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.tags.add(tag)
        self.ids.update([attributes["id"]] if "id" in attributes else [])
        classes = set(attributes.get("class", "").split())
        self.classes.update(classes)

        if "lesson-card" in classes:
            self.lesson_cards.append(attributes)
        if tag == "input" and attributes.get("type") == "search":
            self.search_input = True
        if tag == "select":
            self.level_select = True
        if attributes.get("id") == "filter-status" and attributes.get("aria-live") == "polite":
            self.live_status = True
        if tag == "nav" and "lesson-navigation" in classes:
            self.in_lesson_navigation = True
        if tag == "a" and self.in_lesson_navigation:
            self.navigation_link_count += 1

    def handle_endtag(self, tag):
        if tag == "nav" and self.in_lesson_navigation:
            self.in_lesson_navigation = False

    def handle_data(self, data):
        self.text.append(data.strip())

    @property
    def plain_text(self):
        return " ".join(part for part in self.text if part)


def parse(path):
    parser = CurriculumParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def main():
    errors = []
    home = parse(ROOT / "index.html")
    if "Start here: Lab 01" not in home.plain_text:
        errors.append("index.html: missing beginner start route")
    if "Where does hosting fit?" not in home.plain_text:
        errors.append("index.html: missing guidance for optional hosting lesson")
    if len(home.lesson_cards) != 11:
        errors.append(f"index.html: expected 11 lesson cards, found {len(home.lesson_cards)}")
    if not home.search_input or not home.level_select or not home.live_status:
        errors.append("index.html: search, level filter, or accessible live status is missing")
    for card in home.lesson_cards:
        if not card.get("data-search") or not card.get("data-level"):
            errors.append("index.html: a lesson card is missing search or difficulty metadata")
            break

    required_classes = {"lesson-overview", "knowledge-check", "lesson-navigation"}
    required_ids = {"lesson-guide", "knowledge-check-title"}
    required_text = (
        "Learning outcomes",
        "Prerequisites:",
        "Key concepts:",
        "Steps:",
        "Expected result:",
        "Hint and solution",
    )
    for lesson in LESSONS:
        page = ROOT / lesson / "index.html"
        parser = parse(page)
        missing_classes = required_classes - parser.classes
        missing_ids = required_ids - parser.ids
        missing_text = [phrase for phrase in required_text if phrase not in parser.plain_text]
        if missing_classes:
            errors.append(f"{lesson}/index.html: missing lesson sections {', '.join(sorted(missing_classes))}")
        if missing_ids:
            errors.append(f"{lesson}/index.html: missing accessible section IDs {', '.join(sorted(missing_ids))}")
        if missing_text:
            errors.append(f"{lesson}/index.html: missing required guidance: {', '.join(missing_text)}")
        if "details" not in parser.tags or "summary" not in parser.tags:
            errors.append(f"{lesson}/index.html: checkpoint needs a disclosure with a solution hint")
        if parser.navigation_link_count < 2:
            errors.append(f"{lesson}/index.html: previous/next lesson navigation is incomplete")
        if not (ROOT / lesson / "README.md").is_file():
            errors.append(f"{lesson}: missing companion README.md")

    challenge = parse(ROOT / "30-day-git-challenge" / "index.html")
    for phrase in ("Final challenge", "conflict", "pull request", "v1.0.0"):
        if phrase.lower() not in challenge.plain_text.lower():
            errors.append(f"30-day-git-challenge/index.html: capstone is missing {phrase!r}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "canonical published lessons" not in readme:
        errors.append("README.md: document the canonical published lesson source")
    if "hands-on exercises are coming soon" in readme.lower():
        errors.append("README.md: remove the stale challenge description")

    if errors:
        print("\n".join(errors))
        return 1

    print(f"Checked course overview, {len(LESSONS)} lessons, and the challenge capstone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
