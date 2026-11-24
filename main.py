#!/usr/bin/env python3
"""Entry for make.fun's "One Letter for Your Day" bounty.

Writes exactly one character, the letter O, to /output/entry.txt.
O stands for Overcaffeinated: the word behind the letter.
No network, no input, deterministic.
"""

import os
import string

LETTER = "O"
HIDDEN_WORD = "Overcaffeinated"

# Exactly one character in the entry: no newline, no gloss, no punctuation.
# The hidden word lives in the README, never in entry.txt.


def main() -> None:
    if len(LETTER) != 1 or LETTER not in string.ascii_uppercase:
        raise ValueError(f"entry must be exactly one letter A-Z, got {LETTER!r}")
    if not HIDDEN_WORD.startswith(LETTER):
        raise ValueError(f"hidden word {HIDDEN_WORD!r} must start with {LETTER!r}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
