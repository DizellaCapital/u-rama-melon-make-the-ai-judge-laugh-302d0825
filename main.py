"""Make the AI Judge Laugh — entry program.

Writes one office-life joke to entry.txt: Brenda from HR has printed
the same onboarding form 63 times this year, the printer jammed on
the last page every single time, and she still blames the new guy.
The joke lands on the collision: a machine that fails identically
63 times, and a human who has learned nothing from any of them —
the fault is always someone else, preferably someone who just arrived.

The program enforces the bounty limits (one line, 1-200 characters,
no leading or trailing whitespace) and verifies the write by reading
the file back and comparing it byte for byte with the line.
"""

import os
import sys

LINE = "Brenda from HR has printed the same onboarding form 63 times this year; the printer jammed on the last page every time, and she still calls it 'the new guy's fault'."

MAX_CHARS = 200


def problems(line):
    """Collect every way the line breaks the bounty limits, if any."""
    found = []
    if not line or line.strip() != line:
        found.append("empty or padded")
    if len(line) > MAX_CHARS:
        found.append("over 200 characters")
    if "\n" in line or "\r" in line:
        found.append("more than one line")
    return found


def main():
    bad = problems(LINE)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
