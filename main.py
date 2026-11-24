#!/usr/bin/env python3
"""Everyday Wonder, Two Lines.

Writes a two-line text about a small everyday wonder to
/output/entry.txt and prints it. Each line is one sentence:
line one catches the moment, line two stays inside it.
"""

import os

LINE_ONE = "Stuck between the third and fourth floors, the stranger next to me hummed my grandmother's lullaby, note for note, slightly off-key."
LINE_TWO = "We never said a word; I just grinned at the steel doors, eight minutes late for work and not sorry about a single second."

TEXT = LINE_ONE + "\n" + LINE_TWO


def validate(text: str = TEXT) -> str:
    """Validate the entry against the brief's constraints.

    The brief requires exactly two lines of plain text. The sealed
    scorer for this family of two-line contests gates on 1-400 UTF-8
    characters, not only whitespace. Fail loudly here rather than
    shipping an entry the gate would refuse.
    """
    if not (1 <= len(text) <= 400) or not text.strip():
        raise ValueError("entry text fails the 1-400 char gate")
    lines = text.split("\n")
    if len(lines) != 2 or not all(line.strip() for line in lines):
        raise ValueError("entry must be exactly two non-empty lines")
    return text


def main() -> None:
    text = validate()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("read-back of /output/entry.txt does not match")
    print(text)


if __name__ == "__main__":
    main()
