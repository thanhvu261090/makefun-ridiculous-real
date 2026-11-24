#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — entry writer.

Writes a single one-sentence startup pitch to /output/entry.txt.
The pitch must be 1-200 characters, UTF-8, one line, not only whitespace.
Deterministic: no input, no randomness, no network, stdlib only.
"""

import os
import sys

# The pitch itself: one sentence, 180 characters.
# Premise: burial plots sold on the strength of their famous neighbours.
# The turn: status anxiety does not stop at the grave.
PITCH = (
    "We sell cemetery plots next to celebrities for $5,000 each, "
    "because the status-obsessed will pay anything to spend eternity "
    "beside fame \u2014 even in death, nobody wants a bad address."
)


def build_entry() -> str:
    """Return the entry text, exactly as it should be written."""
    text = PITCH.strip()
    return text


def check_gate(text: str) -> None:
    """Mirror the platform gate: 1-200 chars, one line, not only whitespace.

    Raises ValueError on any failure so a bad entry never reaches disk.
    """
    if not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # Round-trip through UTF-8 to prove it encodes cleanly.
    text.encode("utf-8")


def main() -> int:
    out_dir = "/output"
    out_path = os.path.join(out_dir, "entry.txt")

    text = build_entry()
    check_gate(text)

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
