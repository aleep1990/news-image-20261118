#!/usr/bin/env python3
"""news-image-20261118 entry: place the bundled front page in the output dir.

The bundled image is a 1024x1024 newspaper front page summing up the
world news of Wednesday 18 November 2026 — Kerch Bridge hit again, the
Iran drone strike on the US radar base in Bahrain, the Quad summit in
Manila, Nvidia ruling out Jensen Huang's return, the Siberian plane
crash, and Mongolia's president resigning. Copying only: no network,
no clock, no randomness, so repeated runs produce identical bytes.
"""

import hashlib
import os
import sys
from pathlib import Path

ENTRY_NAME = "entry.png"


def file_digest(path):
    """SHA-256 of a file, streamed in 1 MiB blocks."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    source = Path(__file__).resolve().parent / ENTRY_NAME
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / ENTRY_NAME
    destination.write_bytes(source.read_bytes())
    # The graded runs must agree byte for byte, so prove the copy here
    # instead of trusting the filesystem to have done it right.
    if file_digest(source) != file_digest(destination):
        print("entry.png did not copy cleanly", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
