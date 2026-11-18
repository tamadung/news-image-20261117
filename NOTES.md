# news-image-20261117 — build log

Entry: one 1024×1024 front-page infographic summing up Tuesday 17 November
2026's world news. `main.py` (Python 3.13 stdlib) copies `entry.png` to
`/output/entry.png`; both runs write identical bytes.

## The day's news (researched 18 Nov 2026, from Al Jazeera / Reuters / AP /
Just Security / Outlook India)

The four stories in the image, plus two in the footer — chosen for breadth
across regions and fields:

1. **Crimea Bridge hit again (Europe / war).** A Ukrainian attack on the Kerch
   Bridge early on Tuesday was the second in less than 24 hours; a road
   section collapsed. President Zelenskyy hailed "an unprecedented operation".
   Russia hit Kyiv's North and South bridges over the Dnipro late on Monday,
   disrupting heating, water and power.
2. **Gulf on edge (Middle East / energy).** Iran's Revolutionary Guard navy
   said two oil tankers struck mines and caught fire on a route south of the
   Strait of Hormuz; further tankers were hit east of the strait. Iran fired
   drones at a US military radar system at the Sheikh Isa base in Bahrain
   (intercepted, no casualties or damage). The USS Theodore Roosevelt arrived,
   the third US carrier in the region — the first three-carrier concentration
   since April.
3. **Xi–Trump–Putin summit set (Asia-Pacific / diplomacy).** China's foreign
   ministry confirmed the first three-way meeting of Presidents Xi, Trump and
   Putin, in Shenzhen on Thursday 19 November, on the sidelines of the APEC
   leaders' meeting China is hosting on 18–19 November.
4. **Pentagon fails audit (US).** Independent auditors again issued a
   disclaimer of opinion on the Pentagon's books for fiscal 2026 — the ninth
   year in a row — unable to verify accounts covering more than $4.8 trillion
   in assets.
5. **Also today.** Five European governments (Germany, Denmark, Austria,
   Greece, Netherlands) announced a partnership for a joint return facility in
   Rwanda for rejected asylum seekers. Japan launched fighter jets and strongly
   protested after two suspected Russian aircraft violated its airspace.

Deliberately NOT used: the unconfirmed US-intelligence allegation that Iran is
planning a "dirty bomb" / chemical attack in Washington — reported as an
allegation, not a confirmed event, so it is not shown as fact.

## Why this image

- The judge's first criterion is naming the day and showing specific,
  recognisable events of that day. The date is the biggest text on the page
  ("TUESDAY, 17 NOVEMBER 2026"), and every story is a dated, reported event.
- Breadth: war in Europe, energy/security in the Gulf, great-power diplomacy
  in Asia, a US domestic story, and migration + airspace incidents — not one
  country or one beat.
- Craft: the three hero photographs (collapsed bridge, burning tanker, three
  flags over a skyline) are generated, but ALL text is drawn crisply with PIL
  (DejaVu) at build time — no AI-garbled text anywhere. Legible at 300 px
  across: big date, bold one-line headlines, short captions.

## Validation

- `entry.png`: 1024×1024, 598,649 bytes (< 1,048,576 cap), valid PNG.
- `main.py` run twice locally with different `MAKEFUN_OUTPUT_DIR` values:
  both outputs byte-identical (sha256 match), exit 0, size check passes.
- `makefun check` (without bundle — transcripts_present fails as expected;
  the main session bundles it).

## Weakest points

1. The Pentagon story has no picture of its own (text row only) — the hero
   triptych covers the top three stories.
2. The generated bridge/tanker scenes are illustrative, not the real
   photographs of the events — the judge may weigh a real photo higher, but no
   real photo was available to use.
3. The "ALSO TODAY" footer is small text; at 300 px across it is a caption,
   not a headline.
