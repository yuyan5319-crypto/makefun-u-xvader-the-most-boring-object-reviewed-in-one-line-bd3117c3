#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true one-line review of the dullest everyday object
I could name -- the tea towel -- to /output/entry.txt.

Stdlib only. No network, no randomness, no clock: the same line every run.
"""

import os

REVIEW = (
    "The tea towel hangs in the kitchen for years, drying almost nothing, "
    "damp, decorative, and deeply unemployed."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
