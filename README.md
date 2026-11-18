# The World Today — 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Kyamii21/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Kyamii21/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A one-page newspaper front page summing up Tuesday 17 November 2026 in a
single 1024×1024 image. Designed to stay readable when shrunk to ~300px:
one big lead story with a simple map graphic, three secondary stories, and
a bottom news strip — no text smaller than 26px (except the 24px source
credit line).

## The five stories

1. **US and Iran trade fire** — U.S. jets hit IRGC missile sites on
   Qeshm Island; Iran fires drones at a U.S. radar base in Bahrain
   (the third strike there in five days). Iran claims it downed a U.S.
   MQ-9 drone; a third U.S. carrier, USS Theodore Roosevelt, is now in
   the Gulf.
2. **Kerch Bridge hit again** — Ukrainian drones strike the Crimea
   bridge for a second day; a road span falls into the strait, two
   killed.
3. **Trump heads to Shenzhen** — After ASEAN/Quad in Manila, Trump
   flies to the APEC summit; the first Trump–Xi–Putin summit is set
   for Thursday.
4. **NVIDIA's record quarter** — Record sales; the board rejects
   Jensen Huang's return and opens a probe.
5. **Also:** Houthi drones target a Saudi oil pipeline; five EU states
   plan a Rwanda returns hub; Zelensky hails a big prisoner swap;
   Brent crude ~$93.

Sources: Reuters, AP, BBC, CBS, Al Jazeera.

## Run

```sh
python3 main.py
```

This validates `entry.png` (PNG magic bytes, 1024×1024) and copies it to
`/output/entry.png`, printing its size and sha256. Standard library only —
no dependencies.

## License

MIT — see [LICENSE](LICENSE).
