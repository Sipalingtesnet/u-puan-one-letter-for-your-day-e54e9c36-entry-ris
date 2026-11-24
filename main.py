"""One Letter for Your Day: write a single letter to /output/entry.txt.

The letter stands for a word describing the day. Nothing else is written:
no word, no gloss, no punctuation, no trailing newline.
"""

import os
from pathlib import Path

# Q for queue: the day was one slow line after another, and the line won.
# "Q" is said "cue" -- the letter's own name starts the word.
LETTER = "Q"

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    # Write then rename, so a reader never sees a half-written file.
    tmp = OUT.with_name(OUT.name + ".tmp")
    tmp.write_bytes(LETTER.encode("utf-8"))
    os.replace(tmp, OUT)


if __name__ == "__main__":
    main()
