#!/usr/bin/env python3
"""Write the Make the Judge Smile entry to /output/entry.txt.

Standard library only. Writes exactly one line, no trailing newline.

The line: a small good thing that happened today. The neighbour's cat
has ignored the writer for two years, then walks in this morning and
falls asleep on the laptop. Warmth comes from the animal choosing the
person at last; surprise from the two-year wait ending without warning;
the concrete detail is the laptop, the exact place a cat picks. No
greeting-card phrasing, just the scene as it happened.
"""

from pathlib import Path

ENTRY = (
    "The neighbour's cat, who has ignored me for two years, walked in "
    "this morning and fell asleep on my laptop."
)

MAX_CHARS = 200


def write_entry(text: str, out_path: Path) -> None:
    """Validate the text, then write it with no trailing newline."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")


def main() -> int:
    out_path = Path("/output/entry.txt")
    write_entry(ENTRY, out_path)
    # Read back what landed: the file must be byte-identical to ENTRY.
    if out_path.read_bytes() != ENTRY.encode("utf-8"):
        raise ValueError("read-back check failed: file differs from ENTRY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
