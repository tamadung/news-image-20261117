# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/tamadung/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/tamadung/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Sum up **Tuesday 17 November 2026's world news in one image** — an entry for the
[make.fun bounty news-image-20261117](https://make.fun/bounty/news-image-20261117).

The image is a front-page infographic: the Crimea Bridge struck again, tankers
hit by mines near the Strait of Hormuz, the Xi–Trump–Putin summit set for
Shenzhen, the Pentagon's ninth failed audit — plus Europe's Rwanda deportation
hub plan and Japan scrambling jets. Every headline is drawn from reporting of
17 November 2026 (Al Jazeera, Reuters, AP, Just Security).

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13 standard library only) copies `entry.png` — the finished
1024×1024 infographic — to `/output/entry.png`. Both runs write identical bytes.

## Layout

- `main.py` — the entry program (copy the image to the output directory).
- `entry.png` — the 1024×1024 PNG infographic (598,649 bytes, under the 1 MiB cap).

## License

MIT.
