"""The Absurd Clause Contest entry.

Writes a single absurd terms-of-service clause (<= 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt as a fallback).
Python 3.13 standard library only.
"""

import os

ENTRY = (
    "Clause 12.4: We reserve the right to borrow your soul on bank holidays "
    "and return it within 3-5 business days, slightly used, plus a $4.99 "
    "restocking fee."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only whitespace, as a single line.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
