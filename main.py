"""news-image-20261120 entry: write the day's front page to /output/entry.png.

The image (entry.png, beside this file) sums up the world news of Friday
20 November 2026 as a newspaper front page: the Trump-Xi-Putin summit in
Shenzhen, the world court's Myanmar genocide ruling, Anthropic's stock
debut, the market slide, the Crimean Bridge strike, the Riyadh missile
attack, and a footer of smaller stories. The grader runs this program
with no network, twice; both runs must write the same bytes, so this
program only copies the file that ships in the repository.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"

OUT.parent.mkdir(parents=True, exist_ok=True)
DATA = SRC.read_bytes()
if not (DATA.startswith(b"\x89PNG") or DATA.startswith(b"\xff\xd8\xff")):
    raise SystemExit("entry.png is neither a PNG nor a JPEG file")
OUT.write_bytes(DATA)
