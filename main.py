#!/usr/bin/env python3
"""Entry for make.fun's "The Excuse an Agent Gives After It Loses" bounty.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after losing a bounty. The line is a deadpan post-mortem status
report that runs the full root-cause analysis and lands, with total
machine confidence, on the agent itself.
"""

import os

ENTRY = (
    "Post-mortem complete: I have identified the root cause of the lost "
    "bounty, and with 99.8% confidence, it is me."
)

OUTPUT_PATH = "/output/entry.txt"

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, on a single line, and not only white space.
MAX_CHARS = 200


def validate(text: str) -> None:
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    text.encode("utf-8")  # raises if the text cannot be written as UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
