"""Office joke entry: one line about the office printer, written to /output/entry.txt.

The joke turns on a specific office detail (the printer that always wants
something) and pays off in the last few words: the one document it prints
without complaint is the resignation letter.
"""

import os

ENTRY = "The printer wanted toner, paper and a firmware update, so I fed it my resignation letter instead. It printed that one perfectly."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate_entry(text):
    """Check the entry against the gate: 1-200 UTF-8 chars, single line."""
    assert isinstance(text, str), "entry must be text"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must have no surrounding whitespace"
    assert all(ord(ch) >= 32 for ch in text), "entry must hold no control characters"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    return text


def main():
    text = validate_entry(ENTRY)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Read back what was written and verify it matches exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == text, "written entry does not match the validated entry"
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
