#!/usr/bin/env python3
"""Write the one-line auto-reply entry to /output/entry.txt."""

import os
import sys

ENTRY = "Out of office today. My auto-reply is covering for me. It has already replied to itself four times."


def main() -> int:
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not 1 <= len(text) <= 159:
        print(f"entry must be 1-159 chars, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
