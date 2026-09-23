#!/usr/bin/env python3
"""Build 00-tinh-ha FeatureCollection with geo-shape-random continent polygons."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPTS))
from random_polygon import random_polygon_ring  # noqa: E402

import random


def translate_ring(ring: list[list[int]], dx: int, dy: int) -> list[list[int]]:
    out = [[x + dx, y + dy] for x, y in ring[:-1]]
    out.append(out[0])
    return out


def bbox(ring: list[list[int]]) -> tuple[int, int, int, int]:
    xs = [p[0] for p in ring[:-1]]
    ys = [p[1] for p in ring[:-1]]
    return min(xs), min(ys), max(xs), max(ys)


def overlaps(a: tuple[int, int, int, int], b: tuple[int, int, int, int], pad: int = 8) -> bool:
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    return not (ax1 + pad < bx0 or bx1 + pad < ax0 or ay1 + pad < by0 or by1 + pad < ay0)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("-o", "--output", type=Path, required=True)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--work-slug", default="tap-linh-dieu-lo")
    args = p.parse_args()

    specs = [
        ("CHL-TAY-MO", "Tây Mạc đại lục", "西漠大陆", (-240, 0), 180, 200, 26, 0.42),
        ("CHL-HA-GIOI-NAM", "Đại Hoang Lục địa · Hạ Giới (Phàm giới)", "大荒大陆", (40, -145), 200, 130, 28, 0.38),
        ("CHL-TRUNG-THIEN", "Trung Thiên đại lục", "中天大陆", (25, 95), 220, 160, 32, 0.32),
        ("CHL-BAC-HUYEN", "Bắc Huyền đại lục", "北玄大陆", (10, 265), 200, 120, 26, 0.42),
        ("CHL-DONG-HAI", "Đông Hải đại lục", "东海大陆", (235, 55), 175, 145, 28, 0.35),
    ]

    rng = random.Random(args.seed)
    placed_boxes: list[tuple[int, int, int, int]] = []
    features = [
        {
            "type": "Feature",
            "properties": {
                "id": "TINH-HA-REF",
                "name_vi": "Vực Tinh Hà (tham chiếu)",
                "name_hv": "星河",
                "kind": "hub",
            },
            "geometry": {"type": "Point", "coordinates": [0, 0]},
        }
    ]

    for fid, nvi, nhv, (cx, cy), bw, bh, n, conc in specs:
        for attempt in range(40):
            local = random_polygon_ring(n, 0, bw, 0, bh, conc, rng=rng)
            lcx, lcy = bw // 2, bh // 2
            ring = translate_ring(local, cx - lcx, cy - lcy)
            bb = bbox(ring)
            if not any(overlaps(bb, other) for other in placed_boxes):
                placed_boxes.append(bb)
                features.append(
                    {
                        "type": "Feature",
                        "properties": {
                            "id": fid,
                            "name_vi": nvi,
                            "name_hv": nhv,
                            "kind": "continent",
                            "notes": f"geo-shape-random seed {args.seed}",
                        },
                        "geometry": {"type": "Polygon", "coordinates": [ring]},
                    }
                )
                break
        else:
            print(f"WARN: could not place {fid} without overlap", file=sys.stderr)

    fc = {
        "type": "FeatureCollection",
        "world:schema": "tien-hiep-novel/geo/v2",
        "world:scope": "tinh_ha",
        "world:work_slug": args.work_slug,
        "world:hub_id": "TINH-HA-REF",
        "world:coordinateNote": "Tinh Hà — geo-shape-random; x=Đông, y=Bắc.",
        "features": features,
    }
    args.output.write_text(json.dumps(fc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output} ({len(features)-1} continents)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
