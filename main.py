#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note -- a make.fun one-line entry.

This small program writes the entry below to /output/entry.txt,
where the sealed scorer reads it. The entry is a single line of
plain ASCII text, written as a patch note: after this fix, humans no
longer wake at 3am to replay every embarrassing thing they have
ever said.
"""

import os

ENTRY = 'Fixed: humans no longer wake at 3am to replay every embarrassing thing they have ever said.'

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    """Write the one-line entry to the scorer's output file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
