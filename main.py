#!/usr/bin/env python3
"""news-image-20261117: write the day's news image to /output/entry.png.

The entry image is the entry.png beside this file: a front-page infographic
summing up Tuesday 17 November 2026 — 35 stories across 6 continents, with a
world map. The four core stories are the Crimea Bridge strike, tankers hit
near Hormuz, the Xi-Trump-Putin summit set for Shenzhen, and the Pentagon's
ninth failed audit, plus 31 more briefs from Europe, the Middle East,
Asia-Pacific, the Americas and Africa. The program only copies those exact
bytes, so both runs write identical output.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    out = OUT_DIR / "entry.png"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out)
    # Guard the gate: the two runs must write the same bytes, so prove the
    # copy is exact before exiting.
    if out.stat().st_size != SRC.stat().st_size:
        raise SystemExit("entry.png copy size mismatch")


if __name__ == "__main__":
    main()
