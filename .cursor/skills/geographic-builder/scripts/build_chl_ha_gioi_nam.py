#!/usr/bin/env python3
"""Build chau_luc GeoJSON: scaled shell from 00-tinh-ha + canvas layout."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from shapely.geometry import mapping, shape

_SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPTS))
from canvas_to_geojson import entities_to_features, finalize_chau_luc, regions_to_features  # noqa: E402


def scale_shell_from_tinh_ha(
    tinh_path: Path,
    continent_id: str,
    *,
    grid_max: int = 1000,
    pad: int = 20,
) -> tuple[dict, list[float], float]:
    fc = json.loads(tinh_path.read_text(encoding="utf-8"))
    src = None
    for f in fc.get("features", []):
        if (f.get("properties") or {}).get("id") == continent_id:
            src = f
            break
    if src is None:
        raise ValueError(f"{continent_id} not in {tinh_path}")

    poly = shape(src["geometry"])
    minx, miny, maxx, maxy = poly.bounds
    parent = [float(minx), float(miny)]
    span = max(maxx - minx, maxy - miny) or 1.0
    k = (grid_max - 2 * pad) / span

    def map_ring(ring: list) -> list:
        out = []
        for x, y in ring:
            lx = round((float(x) - minx) * k + pad, 1)
            ly = round((float(y) - miny) * k + pad, 1)
            out.append([lx, ly])
        if out and out[0] != out[-1]:
            out.append(out[0])
        return out

    geom = src["geometry"]
    if geom["type"] == "Polygon":
        coords = [map_ring(ring) for ring in geom["coordinates"]]
    else:
        raise ValueError("continent must be Polygon")

    props = dict(src.get("properties") or {})
    props.setdefault("kind", "continent")
    shell = {
        "type": "Feature",
        "properties": props,
        "geometry": {"type": "Polygon", "coordinates": coords},
    }
    return shell, parent, k


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--tinh-ha", type=Path, required=True)
    p.add_argument("--canvas", type=Path, required=True)
    p.add_argument("-o", "--output", type=Path, required=True)
    p.add_argument("--continent-id", default="CHL-HA-GIOI-NAM")
    p.add_argument("--work-slug", default="tap-linh-dieu-lo")
    args = p.parse_args()

    shell, parent, k = scale_shell_from_tinh_ha(args.tinh_ha, args.continent_id)
    data = json.loads(args.canvas.read_text(encoding="utf-8"))
    reg_feats, _ = regions_to_features(data)
    ent_feats = entities_to_features(data.get("entities") or [])

    fc = {
        "type": "FeatureCollection",
        "world:schema": "tien-hiep-novel/geo/v2",
        "world:scope": "chau_luc",
        "world:work_slug": args.work_slug,
        "world:hub_id": "LOC-THACH-LAM",
        "world:continent_id": args.continent_id,
        "world:parent_scope": "tinh_ha",
        "world:parent_feature_id": args.continent_id,
        "world:parent_file": "00-tinh-ha.geojson",
        "world:parent_coordinates": parent,
        "world:grid_extent": [0, grid_max := 1000],
        "world:coordinateNote": (
            f"Vỏ lục scale từ tinh hà; parent SW bbox; k≈{k:.2f}; canvas {args.canvas.name}"
        ),
        "features": [shell, *reg_feats, *ent_feats],
    }
    props = shell["properties"]
    props["notes"] = (
        f"Vỏ lục = silhouette CHL-HA-GIOI-NAM từ 00-tinh-ha; parent SW {parent}; k≈{k:.2f}; "
        f"hub LOC-THACH-LAM (620,380)"
    )

    fc = finalize_chau_luc(fc)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(fc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output} ({len(fc['features'])} features)", file=sys.stderr)
    print(f"parent_coordinates={parent} k={k:.4f}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
