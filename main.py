#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line, aimed at a robot/AI, to /output/entry.txt.
The line is fixed text, written by this program from a literal in this file.
Stdlib only, no network, no environment reads, deterministic output.
"""

import os

LINE = "Are you my two-factor code? Because you're the only six digits I actually wait for."


def validate(line: str) -> None:
    """Fail fast on a line the sealed gate would reject, before writing."""
    assert line.strip(), "entry must not be whitespace only"
    assert line == line.strip(), "entry must not have leading or trailing whitespace"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    validate(written)


if __name__ == "__main__":
    main()
