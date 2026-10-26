#!/usr/bin/env python3
"""One-off: 00-tinh-ha for work than-phu (distinct CHL IDs from tap-linh-dieu-lo)."""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[5] / ".cursor/skills/geographic-builder/scripts"
sys.path.insert(0, str(_SCRIPTS))
from build_world_tinh_ha import bbox, overlaps, translate_ring  # noqa: E402
from random_polygon import random_polygon_ring  # noqa: E402


def main() -> int:
    out = Path(__file__).resolve().parents[1] / "geo" / "00-tinh-ha.geojson"
    seed = 20260917
    specs = [
        ("CHL-TAY-DUOC", "Tây Dược đại lục", "TâyDượcĐạiLục", (-235, 25), 175, 185, 26, 0.41),
        ("CHL-PHU-VIEN", "Phù Viên đại lục · Hạ Giới", "PhùNguyênĐạiLục", (48, -118), 215, 138, 28, 0.37),
        ("CHL-BAC-LINH", "Bắc Linh đại lục", "BắcLinhĐạiLục", (15, 175), 205, 128, 26, 0.39),
        ("CHL-DONG-HAI-YUAN", "Đông Hải Nguyên lục", "ĐôngHảiNguyênLục", (228, -15), 182, 148, 28, 0.34),
        ("CHL-NAM-MO", "Nam Mộ hoang lục", "NamMạcHoangLục", (72, -275), 195, 95, 24, 0.43),
    ]
    rng = random.Random(seed)
    placed: list[tuple[int, int, int, int]] = []
    features = [
        {
            "type": "Feature",
            "properties": {
                "id": "TINH-HA-REF",
                "name_vi": "Phù Vi Tinh Hà (tham chiếu)",
                "name_hv": "Phù Vi Tinh Hà",
                "kind": "hub",
            },
            "geometry": {"type": "Point", "coordinates": [0, 0]},
        }
    ]
    for fid, nvi, nhv, (cx, cy), bw, bh, n, conc in specs:
        for _ in range(50):
            local = random_polygon_ring(n, 0, bw, 0, bh, conc, rng=rng)
            ring = translate_ring(local, cx - bw // 2, cy - bh // 2)
            bb = bbox(ring)
            if not any(overlaps(bb, o) for o in placed):
                placed.append(bb)
                features.append(
                    {
                        "type": "Feature",
                        "properties": {
                            "id": fid,
                            "name_vi": nvi,
                            "name_hv": nhv,
                            "kind": "continent",
                            "notes": f"geo-shape-random seed {seed}; work than-phu",
                        },
                        "geometry": {"type": "Polygon", "coordinates": [ring]},
                    }
                )
                break
        else:
            print(f"WARN: placement failed for {fid}", file=sys.stderr)

    fc = {
        "type": "FeatureCollection",
        "world:schema": "tien-hiep-novel/geo/v2",
        "world:scope": "tinh_ha",
        "world:work_slug": "than-phu",
        "world:hub_id": "TINH-HA-REF",
        "world:coordinateNote": "Phù Vi Tinh Hà — geo-shape-random; x=Đông, y=Bắc; tách biệt tap-linh-dieu-lo.",
        "features": features,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(fc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({len(features)-1} continents)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
