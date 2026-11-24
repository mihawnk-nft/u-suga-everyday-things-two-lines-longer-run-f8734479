#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run - make.fun entry.

Writes two lines to /output/entry.txt: line 1 explains a traffic jam to a
10-year-old in one vivid sentence built on a zipper analogy; line 2 says in
one sentence why the analogy works - what it maps and what it leaves out.
Pure Python standard library; no network, no secrets, no dependencies.
"""

import os

ENTRY = (
    "A traffic jam is a zipper stuck halfway, with every car a tooth "
    "waiting for the one in front to move.\n"
    "The zipper fits because cars can only move in order, one after "
    "another, but it leaves out that zipper teeth never get impatient, "
    "honk, or try to cut in line."
)


def validate(text: str) -> None:
    """Check the gate the competition states: UTF-8 text, 1-400 chars,
    exactly two lines, each a single sentence."""
    assert 1 <= len(text) <= 400, f"{len(text)} characters, must be 1-400"
    assert text.strip() == text, "leading/trailing whitespace"
    lines = text.split("\n")
    assert len(lines) == 2, f"expected 2 lines, got {len(lines)}"
    for line in lines:
        assert line.strip() == line, f"line has surrounding whitespace: {line!r}"
        assert line.endswith("."), f"line is not one sentence: {line!r}"
        assert line.count(".") == 1, f"line has more than one sentence: {line!r}"
        assert "?" not in line and "!" not in line, f"unexpected punctuation: {line!r}"


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
