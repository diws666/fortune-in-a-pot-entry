#!/usr/bin/env python3
"""Write one fortune for the houseplant on the windowsill to /output/entry.txt."""

import os

OUTPUT_PATH = "/output/entry.txt"

# The fixed fortune line: 111 characters.
FORTUNE = "Good news, little plant: you will be watered on time this week, and the sun has big plans for your newest leaf."


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
