#!/usr/bin/env python3
"""The One-Line Exit — make.fun entry.

Writes the one-line resignation letter (accountant, 135 chars) to
/output/entry.txt. Deterministic: the same line every run.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-140 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 140:
        print(f"ERROR: entry is {len(line)} chars, over the 140-char limit",
              file=sys.stderr)
        sys.exit(1)


# Winner of an 8-variant pairwise selection (see leaderboard-top10.md):
# 2-beat structure — setup (214 spreadsheets, deadpan accountant voice)
# + reveal in the last clause ("become a rounding error"), a double turn
# ("not one balanced me back" personifies the sheets first). Reads like a
# real letter, no fantasy premise, quotable final clause.
LINE = (
    "I resign from Accounts: I balanced 214 spreadsheets this year and "
    "not one balanced me back, so I am leaving to become a rounding error."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
