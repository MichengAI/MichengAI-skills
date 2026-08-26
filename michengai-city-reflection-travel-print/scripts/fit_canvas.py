#!/usr/bin/env python3
"""Fit a generated city print to an exact final canvas without changing its semantics."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def parse_size(value: str) -> tuple[int, int]:
    try:
        width_s, height_s = value.lower().split("x", 1)
        width, height = int(width_s), int(height_s)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("size must be WIDTHxHEIGHT, for example 768x1024") from exc
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("width and height must be positive")
    return width, height


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--size", type=parse_size, default=(768, 1024), help="final WIDTHxHEIGHT; default: 768x1024")
    args = parser.parse_args()

    if not args.input.is_file():
        parser.error(f"input not found: {args.input}")
    args.output.parent.mkdir(parents=True, exist_ok=True)

    with Image.open(args.input) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
        fitted = ImageOps.fit(image, args.size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
        fitted.save(args.output, quality=92, optimize=True)


if __name__ == "__main__":
    main()
