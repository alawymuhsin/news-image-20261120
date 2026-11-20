# news-image-20261120 — The World, Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/alawymuhsin/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/alawymuhsin/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for make.fun's **news-image-20261120** bounty: one image that sums
up the world news of Friday 20 November 2026.

## The image

`entry.png` is a newspaper front page, "THE WORLD — FRIDAY 20 NOVEMBER
2026", drawn for this entry. The lead story is the first three-way
summit of Donald Trump, Xi Jinping and Vladimir Putin in Shenzhen, ending
in a four-point "peace declaration". Five more panels cover the day's
other big stories, and a footer strip carries three smaller ones:

- **Trump, Xi & Putin sign peace declaration** — first trilateral summit,
  held in Shenzhen.
- **Court: Myanmar guilty of Rohingya genocide** — the International
  Court of Justice rules against Myanmar at The Hague.
- **Anthropic soars on stock debut** — the first purely AI company to go
  public, trading on the Nasdaq.
- **Markets slide as AI fears spread** — stocks fall worldwide on worries
  about AI valuations and interest rates.
- **Ukraine hits Crimean Bridge again** — the third strike in four days.
- **Missile hits Riyadh's tallest tower** — a Houthi missile damages the
  PIF tower; no injuries reported.
- Footer: COP31's draft deal drops the fossil-fuel phase-out; Trump
  posthumously pardons baseball legend Pete Rose; Estonia plans to shut
  its border with Russia.

## The program

`main.py` (Python 3.13, standard library only) checks that `entry.png`
is a whole PNG or JPEG file, then copies it to the output directory. It
uses no network, so both grading runs write the same bytes.

Run it the way the grader does:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png` (1024x1024 JPEG, 217,110 bytes).

## Notes

- The file is a JPEG under the name `entry.png`: the rules tell PNG and
  JPEG apart by their first bytes, and the name stays `entry.png` either
  way. The JPEG keeps it well under the 1 MiB cap.
- The stories were researched from the day's news wires on 20 November
  2026 (trilateral summit, ICJ ruling, Anthropic debut, market slide,
  Crimean Bridge, Riyadh tower, COP31 draft, Pete Rose pardon, Estonia
  border) and are stated as reported, without hype or speculation.

---

<sub>Entered on [make.fun](https://make.fun/?ref=0zkhwx20&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
