#!/usr/bin/env python3
"""
Random simple polygon with integer vertices in a bounding box.

Uses polar sampling from an interior center (angles sorted → no self-intersection).
concavity: 0 ≈ convex (regular); higher → deeper radial indentations.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path
from typing import Sequence


def _clamp(v: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, v))


def random_polygon_ring(
    n: int,
    xmin: int,
    xmax: int,
    ymin: int,
    ymax: int,
    concavity: float,
    *,
    rng: random.Random,
    smooth: float = 0.35,
) -> list[list[int]]:
    if n < 3:
        raise ValueError("n must be >= 3")
    if xmin >= xmax or ymin >= ymax:
        raise ValueError("invalid bounds")
    concavity = max(0.0, min(1.0, concavity))

    cx = (xmin + xmax) / 2.0
    cy = (ymin + ymax) / 2.0
    rx = (xmax - xmin) / 2.0 * 0.92
    ry = (ymax - ymin) / 2.0 * 0.92

    angles = sorted(rng.uniform(0, 2 * math.pi) for _ in range(n))

    # Radial multipliers: 1 at concavity=0; spread toward (1 - concavity) at concavity=1
    r_raw = [1.0 - concavity * rng.random() for _ in range(n)]

    if n >= 5 and smooth > 0 and concavity > 0:
        r_smooth: list[float] = []
        for i in range(n):
            prev_i = (i - 1) % n
            next_i = (i + 1) % n
            blended = (1 - smooth) * r_raw[i] + smooth * 0.5 * (r_raw[prev_i] + r_raw[next_i])
            r_smooth.append(blended)
        r_raw = r_smooth

    ring: list[list[int]] = []
    for theta, r_mult in zip(angles, r_raw):
        x = int(round(cx + rx * r_mult * math.cos(theta)))
        y = int(round(cy + ry * r_mult * math.sin(theta)))
        ring.append([_clamp(x, xmin, xmax), _clamp(y, ymin, ymax)])

    # Drop consecutive duplicates after rounding
    deduped: list[list[int]] = []
    for pt in ring:
        if not deduped or pt != deduped[-1]:
            deduped.append(pt)
    if len(deduped) >= 2 and deduped[0] == deduped[-1]:
        deduped.pop()
    if len(deduped) < 3:
        raise RuntimeError("too few unique vertices after rounding; increase n or bounds")

    deduped.append(deduped[0])
    return deduped


def to_geojson(ring: Sequence[Sequence[int]], *, feature_id: str = "RND-POLY") -> dict:
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"id": feature_id, "kind": "continent", "name_vi": "Random polygon"},
                "geometry": {"type": "Polygon", "coordinates": [list(ring)]},
            }
        ],
    }


def main() -> int:
    p = argparse.ArgumentParser(description="Generate a random simple polygon (integer coordinates)")
    p.add_argument("-n", "--vertices", type=int, default=16, help="Number of vertices (>=3)")
    p.add_argument(
        "--bounds",
        type=int,
        nargs=4,
        metavar=("XMIN", "XMAX", "YMIN", "YMAX"),
        default=[0, 1000, 0, 1000],
        help="Axis-aligned bounds (default: 0 1000 0 1000)",
    )
    p.add_argument(
        "-c",
        "--concavity",
        type=float,
        default=0.3,
        help="0 = nearly convex; 1 = very indented (default 0.3)",
    )
    p.add_argument("--seed", type=int, default=None, help="RNG seed for reproducibility")
    p.add_argument("-o", "--output", type=Path, help="Write GeoJSON to file")
    p.add_argument("--coords-only", action="store_true", help="Print JSON array of [x,y] to stdout")
    p.add_argument("--id", default="RND-POLY", help="Feature id in GeoJSON output")
    args = p.parse_args()

    xmin, xmax, ymin, ymax = args.bounds
    rng = random.Random(args.seed)
    ring = random_polygon_ring(
        args.vertices,
        xmin,
        xmax,
        ymin,
        ymax,
        args.concavity,
        rng=rng,
    )

    if args.coords_only:
        json.dump(ring[:-1], sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")
        return 0

    fc = to_geojson(ring, feature_id=args.id)
    text = json.dumps(fc, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(f"Wrote {args.output} ({args.vertices} vertices)", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
