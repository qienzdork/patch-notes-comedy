#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one funny one-line patch note for a bug in real life / human
biology to /output/entry.txt (or $OUTPUT_PATH when set).
Deterministic, stdlib only, no network, no randomness.
"""

import os

# The entry: one terse release note about a universally recognisable
# human bug - the brain replaying an old embarrassment at 3am.
ENTRY = (
    "v1.4.2: fixed a bug where the brain replayed your most "
    "embarrassing moment from 2009 at 3am instead of sleeping."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
