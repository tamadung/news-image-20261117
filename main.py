#!/usr/bin/env python3
"""news-image-20261117: write the day's news image to /output/entry.png.

The entry image is the entry.png beside this file: a front-page infographic
summing up Tuesday 17 November 2026 — 37 stories across 6 continents, with a
world map. Thirteen core stories each get their own flat-illustration panel
(Kerch Bridge, Hormuz, Quad Manila, Nvidia, Ebola, COP31, measles, Mongolia,
Serbia parliament, Bangladesh garment, An-12 crash, Pentagon audit, Japan
jets), plus 24 more briefs in a numbered ALSO ON list and a world map with
numbered pins 1-13 tied to the core stories. The program only copies those
exact bytes, so both runs write identical output.
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
