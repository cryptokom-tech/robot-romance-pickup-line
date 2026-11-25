#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line, aimed at a robot/AI, to /output/entry.txt.
The line is fixed text, written by this program from a literal in this file.
Stdlib only, no network, no environment reads, deterministic output.
"""

import os

LINE = "Are you my two-factor code? Because you're the only six digits I actually wait for."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert written.strip(), "entry must not be whitespace only"
    assert "\n" not in written, "entry must be a single line"


if __name__ == "__main__":
    main()
