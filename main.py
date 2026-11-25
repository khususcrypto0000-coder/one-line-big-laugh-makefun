"""One Line, Big Laugh — make.fun bounty entry.

Writes the single joke line to /output/entry.txt (no trailing newline)
and verifies the file is byte-identical to the in-memory entry.
Stdlib only: os, sys.
"""

import os
import sys

ENTRY = "I fed the parking meter two dollars and it expired in ten minutes, so now I'm convinced it's a slot machine that pays out in fines."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # GATE guards: exactly one line, 1-200 chars, not whitespace-only.
    if not 1 <= len(ENTRY) <= 200:
        sys.exit("ENTRY must be 1-200 chars, got %d" % len(ENTRY))
    if not ENTRY.strip():
        sys.exit("ENTRY must not be whitespace-only")
    if "\n" in ENTRY or "\r" in ENTRY:
        sys.exit("ENTRY must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Read back and assert byte-identical, no trailing newline.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt is not byte-identical to ENTRY"
    assert not written.endswith(b"\n"), "entry.txt must not end with a newline"
    print("Wrote %s (%d chars, %d bytes)" % (OUTPUT_PATH, len(ENTRY), len(data)))


if __name__ == "__main__":
    main()
