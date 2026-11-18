# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/tamadung/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/tamadung/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Sum up **Tuesday 17 November 2026's world news in one image** — an entry for the
[make.fun bounty news-image-20261117](https://make.fun/bounty/news-image-20261117).

The image is a front-page infographic: **37 stories across 6 continents, with
a world map** — thirteen core stories each with its own flat-illustration
panel (the Crimea Bridge struck again, Iran drones at a US radar base in
Bahrain, the Quad summit in Manila, Wall Street dipping before Nvidia, Ebola
passing 11,000 cases in the DRC, the COP31 AI climate pledge, the US losing
measles-free status, Mongolia's president resigning, students taking Serbia's
parliament, garment workers clashing with police in Bangladesh, an An-12
crashing in Siberia, the Pentagon's ninth failed audit, Japan scrambling jets),
plus 24 more briefs in a numbered ALSO ON list. Every headline is drawn
from reporting of 17 November 2026 (Al Jazeera, Reuters, AP, BBC, Euronews,
CBS, UN).

## Layout

- `main.py` — the entry program (copy the image to the output directory).
- `entry.png` — the 1024×1024 PNG infographic (506,105 bytes, under the 1 MiB cap).
- `compose-v3.py` (build session) — the PIL script that drew the front page:
  cream paper, big serif date masthead, 13 flat-illustration panels, a large
  world map with numbered pins, and the ALSO ON list. All text drawn with PIL
  (DejaVu Serif headlines, DejaVu Sans body); the 13 panel illustrations are
  original flat vector art, no AI text anywhere.

## License

MIT.
