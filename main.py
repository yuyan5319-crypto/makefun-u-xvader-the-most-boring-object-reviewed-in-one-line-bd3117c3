#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true one-line review of the dullest everyday object
I could name -- the tea towel -- to /output/entry.txt.

Why the tea towel: every kitchen has one, and almost nobody uses it for
its actual job. It hangs on its hook for years, slightly damp, purely
decorative -- a towel that retired from drying before it ever started.
The joke is the object's own dullness: employed to dry dishes, in
practice deeply unemployed. The "exactly one dish in six years" detail
is the recognisable truth that makes the last three words land.

Stdlib only. No network, no randomness, no clock: the same line every run.
"""

import os

REVIEW = (
    "The tea towel has dried exactly one dish in six years and spends "
    "the rest of its life hanging there, damp, decorative, and deeply "
    "unemployed."
)

# The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space, on a single line.
MAX_CHARS = 200


def gate(line):
    """Refuse anything the sealed scorer would refuse."""
    if not line:
        raise ValueError("review must not be empty")
    if line.strip() != line:
        raise ValueError("review must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("review must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"review is {len(line)} characters, over the {MAX_CHARS} cap"
        )
    if not line.strip():
        raise ValueError("review must not be only white space")


def main():
    gate(REVIEW)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
