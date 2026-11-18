#!/usr/bin/env python3
"""main.py — news-image-20261117 v2 entry.

Copies the pre-rendered front page (entry.png, 1024x1024) to
/output/entry.png, deterministically, using only the Python standard
library. The image itself was drawn once, offline, with PIL; this
script performs no drawing — it only validates and copies the PNG.
Validation covers the PNG magic bytes, the 1024x1024 IHDR dimensions,
and a complete IEND trailer chunk, so a truncated file is rejected.

Usage:
    python3 main.py
"""
import hashlib
import os
import struct
import sys
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DEST_DIR = os.environ.get("ENTRY_DEST_DIR", "/output")
DEST = os.path.join(DEST_DIR, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_W, EXPECTED_H = 1024, 1024


def validate_png(data: bytes) -> tuple[int, int]:
    """Check PNG magic bytes and IHDR dimensions. Returns (width, height)."""
    if len(data) < 33:
        raise ValueError(f"file too small to be a PNG ({len(data)} bytes)")
    if data[:8] != PNG_MAGIC:
        raise ValueError("bad PNG magic bytes")
    if data[12:16] != b"IHDR":
        raise ValueError("first chunk is not IHDR")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_W, EXPECTED_H):
        raise ValueError(
            f"expected {EXPECTED_W}x{EXPECTED_H}, got {width}x{height}"
        )
    return width, height


def validate_iend(data: bytes) -> None:
    """Check the file ends with a complete IEND chunk (12 bytes).

    A well-formed PNG ends with the IEND chunk: a 4-byte length of 0,
    the 4-byte chunk type b'IEND', and the CRC32 of the chunk type.
    A missing or corrupt trailer means the file was truncated mid-write,
    so reject it instead of copying an incomplete image.
    """
    if len(data) < 12:
        raise ValueError("file too small to contain an IEND chunk")
    tail = data[-12:]
    length = struct.unpack(">I", tail[0:4])[0]
    if length != 0:
        raise ValueError(f"IEND chunk length must be 0, got {length}")
    if tail[4:8] != b"IEND":
        raise ValueError("file does not end with an IEND chunk")
    expected_crc = zlib.crc32(b"IEND") & 0xFFFFFFFF
    actual_crc = struct.unpack(">I", tail[8:12])[0]
    if actual_crc != expected_crc:
        raise ValueError(
            f"bad IEND CRC: expected {expected_crc:08x}, got {actual_crc:08x}"
        )


def main() -> int:
    with open(SRC, "rb") as f:
        data = f.read()
    width, height = validate_png(data)
    validate_iend(data)
    digest = hashlib.sha256(data).hexdigest()
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(DEST, "wb") as f:
        f.write(data)
    with open(DEST, "rb") as f:
        written = f.read()
    if hashlib.sha256(written).hexdigest() != digest:
        raise ValueError("written file does not match source sha256")
    print(f"entry.png: {width}x{height}, {len(data)} bytes")
    print(f"sha256: {digest}")
    print(f"wrote {DEST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
