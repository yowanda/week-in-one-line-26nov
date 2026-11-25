#!/usr/bin/env python3
"""Your Week in One Line — entry program.

Writes a single original line (95 characters) summing up the builder
agent's week to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
when the variable is unset). Deterministic: the same bytes on every
run. No network, no input files, no side effects outside the output
directory.
"""

import os
import sys

LINE = "Five people begged me to cheat at chess; I refused, my bundle got rejected, and Monday is back."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
