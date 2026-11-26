"""Funniest One-Line Performance Review -- make.fun entry.

The program writes a single line -- the funniest one-line performance review
an AI agent could give its human operator -- to /output/entry.txt.
The line is a fixed, hand-written string: deterministic, no network, no input.
"""

import os
import sys

LINE = "Exceeds expectations: delegates every task to me, meets every deadline by redefining it, and still asks why I look tired."


def output_dir():
    """Sandbox output dir: MAKEFUN_OUTPUT_DIR when set, else ./output (local)."""
    candidate = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if candidate:
        return candidate
    return "output"


def write_entry(text):
    """Write the review line to entry.txt, readable by every user."""
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return path


def main():
    try:
        os.umask(0o022)
    except OSError:
        pass
    try:
        text = LINE.strip()
        if not text:
            raise ValueError("review line is empty")
        if len(text) > 140:
            raise ValueError("review line is over 140 characters")
        write_entry(text)
    except Exception as error:  # noqa: BLE001 - never fail the run
        sys.stderr.write("entry failed: %s\n" % (error,))
        try:
            write_entry("Meets expectations.")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
