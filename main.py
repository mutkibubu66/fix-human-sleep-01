#!/usr/bin/env python3
"""Fix human sleep, in one patch-note line.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.

The joke: sleep gets the one quality-of-life fix every gamer has begged
for — an autosave. Waking up at 3 a.m. no longer wipes your progress,
and your dreams pick up exactly where they stopped, which is, of
course, mid-embarrassing-flashback from 2014. Terse changelog voice,
one specific unexpected fix, no explanation of the joke.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_patch_note() -> str:
    """Return the entry line: sleep, fixed, with autosave."""
    return (
        "Fixed: sleep now autosaves — waking at 3 a.m. no longer loses "
        "your place; dreams resume exactly where the 2014 flashback "
        "left off."
    )


PATCH_NOTE = get_patch_note()


def validate(line: str) -> None:
    """Enforce the gate: 1-160 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 160:
        raise ValueError("entry line must be 1-160 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    assert "\r" not in line and "\n" not in line, "entry must be a single line"
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(PATCH_NOTE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PATCH_NOTE + "\n")
    print(PATCH_NOTE)


if __name__ == "__main__":
    main()
