#!/usr/bin/env python3
"""Write the 17 November 2026 world-news front page to /output/entry.png.

The entry image is stored in this repository as entry.png (a 1024x1024
PNG drawn with PIL). This program deterministically copies those exact
bytes to /output/entry.png, with no network access, no randomness and
no dependence on the clock.
"""

import hashlib
import os
import struct
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SIZE = (1024, 1024)


def _png_dimensions(path):
    """Return (width, height) from the PNG IHDR chunk, or None."""
    with open(path, "rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != PNG_MAGIC:
        return None
    if header[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    dims = _png_dimensions(SOURCE)
    if dims != EXPECTED_SIZE:
        print(f"unexpected image size: {dims}", file=sys.stderr)
        return 1
    os.makedirs(DEST_DIR, exist_ok=True)
    hasher = hashlib.sha256()
    with open(SOURCE, "rb") as src, open(DEST, "wb") as dst:
        while True:
            chunk = src.read(65536)
            if not chunk:
                break
            hasher.update(chunk)
            dst.write(chunk)
    print(f"wrote {DEST} ({os.path.getsize(DEST)} bytes, sha256 "
          f"{hasher.hexdigest()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
