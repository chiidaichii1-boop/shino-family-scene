#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene -- two lines, well under 280 characters --
to $MAKEFUN_OUTPUT_DIR/entry.txt. Python 3 standard library only.

The scene is a fixed literal, so every run produces byte-identical output.
"""

import os
import sys

SCENE = (
    "Dad taught me to shave on a balloon with a butter knife.\n"
    "Twenty years later he still inspects my chin every Sunday, "
    "then steals the last pancake and calls it a tax.\n"
)


def main() -> int:
    text = SCENE
    if not 1 <= len(text) <= 280:
        print(f"scene is {len(text)} characters, must be 1-280",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("scene is blank", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
