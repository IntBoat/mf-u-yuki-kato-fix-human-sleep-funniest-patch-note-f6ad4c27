#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note (make.fun).

Writes the one-line entry to /output/entry.txt, where the sealed
scorer reads it.
"""

import os

ENTRY = 'Fixed: humans no longer wake at 3am to replay every embarrassing thing they have ever said.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
