#!/usr/bin/env python3
"""Build the single-file Typora STEM guide from its multifile sources."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "multifile"
INDEX_PATH = SOURCE_DIR / "index.md"
OUTPUT_PATH = ROOT / "singlefile" / "typora-stem-guide.md"

CHAPTER_LINK_RE = re.compile(
    r"(?P<prefix>\]\()(?:\./)?(?P<filename>chapter-[^()#\s]+\.md)"
    r"(?P<fragment>#[^()\s]*)?(?P<suffix>\))"
)
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def heading_slug(heading: str) -> str:
    """Approximate the stable GFM/Typora fragment for a plain-text heading."""
    result: list[str] = []
    for character in heading.strip().lower():
        category = unicodedata.category(character)
        if character.isspace() or character == "-":
            result.append("-")
        elif category[0] in {"L", "N"} or character == "_":
            result.append(character)
    return re.sub(r"-+", "-", "".join(result)).strip("-")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def chapter_anchor(path: Path) -> str:
    match = HEADING_RE.search(read_text(path))
    if match is None:
        raise ValueError(f"chapter has no level-1 heading: {path}")
    return heading_slug(match.group(1))


def rewrite_chapter_links(text: str, anchors: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        filename = match.group("filename")
        if filename not in anchors:
            raise ValueError(f"link targets an unknown chapter: {filename}")
        fragment = match.group("fragment")
        target = fragment if fragment is not None else f"#{anchors[filename]}"
        return f"{match.group('prefix')}{target}{match.group('suffix')}"

    return CHAPTER_LINK_RE.sub(replace, text)


def build() -> str:
    chapter_paths = sorted(SOURCE_DIR.glob("chapter-*.md"))
    if not chapter_paths:
        raise ValueError(f"no chapter files found in {SOURCE_DIR}")

    anchors = {path.name: chapter_anchor(path) for path in chapter_paths}
    sections = [read_text(INDEX_PATH), *(read_text(path) for path in chapter_paths)]
    merged = "\n\n---\n\n".join(sections) + "\n"
    return rewrite_chapter_links(merged, anchors)


def main() -> int:
    try:
        output = build()
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_text(output, encoding="utf-8")
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    relative_output = OUTPUT_PATH.relative_to(ROOT)
    print(f"Wrote {relative_output} ({len(output.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
