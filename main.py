"""Unsent: The Micro-Confession Sprint — entry writer.

Writes one two-part micro-confession to /output/entry.txt: a To: line naming
who the message was meant for, then the unsent message itself, one line,
exactly as typed, with no explanation after it.
"""

import os

ENTRY = (
    "To: my sister\n"
    "I saw your husband's second phone the night before your wedding "
    "and I have carried it through every anniversary toast since."
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
