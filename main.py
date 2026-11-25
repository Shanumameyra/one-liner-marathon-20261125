#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single original one-line comedy joke to /output/entry.txt,
as required by the bounty rules (UTF-8, 1-280 characters, one line).
"""

import os

JOKE = (
    "I taught my dog to fetch my slippers, my keys, and my will to live "
    "\u2014 he's still working on the last one, and honestly, so am I."
)


def main() -> None:
    line = JOKE.strip()
    assert 1 <= len(line) <= 280, f"joke is {len(line)} chars, must be 1-280"
    assert "\n" not in line, "joke must be a single line"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        # Sandbox without a writable /output: keep a local copy for inspection.
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line)
    print(f"wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
