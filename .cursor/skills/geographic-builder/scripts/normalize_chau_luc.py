#!/usr/bin/env python3
"""
Post-process chau_luc GeoJSON:
  1. Clip partition polygons, rivers, and validate points inside feature[0] (continent shell).
  2. Snap vertices; remove overlaps; snap new edges to existing union (shared internal boundaries).

Convention: foundation/logic/00-geojson-world-map-convention.md §2.1.1
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

from shapely.geometry import LineString, MultiLineString, Polygon, mapping, shape
from shapely.ops import snap, unary_union
from shapely.validation import make_valid


def _round_pt(x: float, y: float, prec: int) -> tuple[float, float]:
    return (round(float(x), prec), round(float(y), prec))


def snap_coords(obj: Any, prec: int) -> Any:
    """Round all coordinates in GeoJSON geometry dict."""
    t = obj.get("type")
    if t == "Point":
        c = obj["coordinates"]
        obj["coordinates"] = list(_round_pt(c[0], c[1], prec))
    elif t == "LineString":
        obj["coordinates"] = [_round_pt(c[0], c[1], prec) for c in obj["coordinates"]]
    elif t == "Polygon":
        obj["coordinates"] = [[list(_round_pt(c[0], c[1], prec)) for c in ring] for ring in obj["coordinates"]]
    elif t == "MultiPolygon":
        obj["coordinates"] = [
            [[list(_round_pt(c[0], c[1], prec)) for c in ring] for ring in poly] for poly in obj["coordinates"]
        ]
    return obj


def largest_polygon(geom) -> Polygon | None:
    if geom is None or geom.is_empty:
        return None
    if geom.geom_type == "Polygon":
        return geom
    if geom.geom_type == "MultiPolygon":
        return max(geom.geoms, key=lambda g: g.area)
    g = make_valid(geom)
    if g.geom_type == "Polygon":
        return g
    if g.geom_type == "MultiPolygon":
        return max(g.geoms, key=lambda x: x.area)
    return None


def lines_from_intersection(geom) -> list[LineString]:
    if geom is None or geom.is_empty:
        return []
    if geom.geom_type == "LineString":
        return [geom] if geom.length > 0 else []
    if geom.geom_type == "MultiLineString":
        return [g for g in geom.geoms if g.length > 0]
    if geom.geom_type == "GeometryCollection":
        out: list[LineString] = []
        for g in geom.geoms:
            out.extend(lines_from_intersection(g))
        return out
    return []


def polygon_to_feature_geom(poly: Polygon, prec: int) -> dict:
    rounded = snap_coords(mapping(poly), prec)
    valid = largest_polygon(make_valid(shape(rounded)))
    if valid is None:
        valid = largest_polygon(make_valid(poly))
    if valid is None:
        raise ValueError("polygon became empty during normalization")
    return mapping(valid)


def normalize_fc(
    fc: dict,
    *,
    snap_prec: int = 1,
    snap_tolerance: float = 2.0,
    min_area: float = 8.0,
    fill_gaps: bool = True,
    overlap_policy: str = "subtract",
) -> tuple[dict, list[str]]:
    """Return (new_fc, warnings)."""
    warnings: list[str] = []
    features = fc.get("features") or []
    if not features:
        raise ValueError("FeatureCollection has no features")

    out_features: list[dict] = []
    first = copy.deepcopy(features[0])
    if first.get("geometry", {}).get("type") != "Polygon":
        raise ValueError("Feature[0] must be a Polygon (continent shell)")
    snap_coords(first["geometry"], snap_prec)
    shell = shape(first["geometry"])
    shell = make_valid(shell)
    shell_poly = largest_polygon(shell)
    if shell_poly is None or shell_poly.is_empty:
        raise ValueError("Feature[0] is not a valid continent polygon")
    first["geometry"] = polygon_to_feature_geom(shell_poly, snap_prec)
    out_features.append(first)

    continent = shell_poly
    partition_specs: list[tuple[int, dict]] = []
    other_specs: list[tuple[int, dict]] = []

    for idx, feat in enumerate(features[1:], start=1):
        f = copy.deepcopy(feat)
        gtype = f.get("geometry", {}).get("type")
        if gtype == "Polygon":
            partition_specs.append((idx, f))
        else:
            other_specs.append((idx, f))

    processed: list[tuple[dict, Polygon]] = []
    union_acc = Polygon()

    # Small partitions first (mountain strips, châu), large backgrounds last — avoids big polygons swallowing overlaps
    def partition_key(item: tuple[int, dict]) -> tuple[float, str]:
        _i, feat = item
        try:
            p = largest_polygon(make_valid(shape(feat["geometry"])))
            a = p.area if p else 0.0
        except Exception:
            a = 0.0
        fid = (feat.get("properties") or {}).get("id") or ""
        return (a, fid)

    partition_specs.sort(key=partition_key)

    for _idx, feat in partition_specs:
        props = feat.get("properties") or {}
        fid = props.get("id", "?")
        raw = shape(feat["geometry"])
        raw = make_valid(raw)
        poly = largest_polygon(raw)
        if poly is None or poly.is_empty:
            warnings.append(f"SKIP {fid}: empty or invalid polygon")
            continue

        poly = largest_polygon(poly.intersection(continent))
        if poly is None or poly.is_empty:
            warnings.append(f"SKIP {fid}: outside continent after clip")
            continue

        if not union_acc.is_empty:
            poly = largest_polygon(snap(poly, union_acc, snap_tolerance))
            if overlap_policy == "subtract":
                diff = poly.difference(union_acc) if poly else None
                if diff is not None and not diff.is_empty and props.get("fill_remainder"):
                    if diff.geom_type == "Polygon":
                        parts = [diff]
                    elif diff.geom_type == "MultiPolygon":
                        parts = list(diff.geoms)
                    elif diff.geom_type == "GeometryCollection":
                        parts = [g for g in diff.geoms if g.geom_type == "Polygon" and not g.is_empty]
                    else:
                        parts = []
                    if parts:
                        diff = unary_union(parts)
                poly = largest_polygon(diff) if diff is not None and not diff.is_empty else None
            elif overlap_policy == "warn":
                ov = poly.intersection(union_acc) if poly else None
                if ov and not ov.is_empty and ov.area > min_area:
                    warnings.append(f"OVERLAP {fid}: {ov.area:.1f} with prior regions")

        if poly is None or poly.is_empty:
            warnings.append(f"SKIP {fid}: empty after clip/overlap")
            continue
        if poly.area < min_area:
            warnings.append(f"SKIP {fid}: area {poly.area:.2f} < min_area {min_area}")
            continue

        poly = largest_polygon(snap(poly, continent.boundary, snap_tolerance * 0.5))
        if poly is None:
            continue

        feat["geometry"] = polygon_to_feature_geom(poly, snap_prec)
        processed.append((feat, poly))
        union_acc = unary_union([union_acc, poly]) if not union_acc.is_empty else poly

    gap = make_valid(continent.difference(union_acc) if not union_acc.is_empty else continent)
    if not gap.is_empty and gap.area > min_area:
        if gap.geom_type == "Polygon":
            gap_parts = [gap]
        elif gap.geom_type == "MultiPolygon":
            gap_parts = list(gap.geoms)
        else:
            gap_parts = [g for g in getattr(gap, "geoms", []) if g.geom_type == "Polygon"]
        gap_parts = [g for g in gap_parts if g.area > min_area]
        if gap_parts and fill_gaps and processed:
            for gap_poly in sorted(gap_parts, key=lambda g: g.area, reverse=True):
                # Assign each disconnected gap to the partition with the longest shared boundary.
                best_i = 0
                best_len = -1.0
                for i, (_f, p) in enumerate(processed):
                    shared = p.boundary.intersection(gap_poly.boundary)
                    length = shared.length if not shared.is_empty else 0.0
                    if length > best_len:
                        best_len = length
                        best_i = i
                if best_len <= 0:
                    continue
                merged = largest_polygon(make_valid(unary_union([processed[best_i][1], gap_poly])))
                if merged:
                    f, _ = processed[best_i]
                    f["geometry"] = polygon_to_feature_geom(merged, snap_prec)
                    processed[best_i] = (f, merged)
                    warnings.append(
                        f"GAP fill: {gap_poly.area:.1f} units merged into "
                        f"{(f.get('properties') or {}).get('id', '?')}"
                    )
            union_acc = unary_union([p for _, p in processed])
        else:
            warnings.append(f"GAP: {gap.area:.1f} units inside continent not covered by partitions")

    overlap_left = largest_polygon(union_acc.intersection(continent))
    if overlap_left and abs(overlap_left.area - continent.area) > min_area * 2:
        missing = continent.difference(union_acc)
        if not missing.is_empty and missing.area > min_area:
            warnings.append(f"Uncovered area remains: {missing.area:.1f}")

    id_to_feat = {(f.get("properties") or {}).get("id"): f for f, _ in processed}
    union_final = unary_union([p for _, p in processed]) if processed else Polygon()

    for _idx, feat in enumerate(features[1:], start=1):
        gtype = feat.get("geometry", {}).get("type")
        if gtype == "Polygon":
            fid = (feat.get("properties") or {}).get("id")
            if fid in id_to_feat:
                out_features.append(id_to_feat[fid])
            continue

    for _idx, feat in other_specs:
        f = copy.deepcopy(feat)
        props = f.get("properties") or {}
        fid = props.get("id", "?")
        geom = f.get("geometry")
        if not geom:
            out_features.append(f)
            continue
        gtype = geom["type"]
        if gtype == "LineString":
            ls = shape(geom)
            ls = ls.intersection(continent)
            parts = lines_from_intersection(ls)
            if not parts:
                warnings.append(f"SKIP line {fid}: outside continent")
                continue
            # Keep longest connected piece if split
            ls = max(parts, key=lambda x: x.length)
            if not union_final.is_empty:
                ls = snap(ls, union_final.boundary, snap_tolerance)
            g = snap_coords(mapping(ls), snap_prec)
            f["geometry"] = g
            out_features.append(f)
        elif gtype == "Point":
            pt = shape(geom)
            if not continent.covers(pt):
                warnings.append(f"WARN point {fid}: outside continent (kept, may need manual move)")
            snap_coords(f["geometry"], snap_prec)
            out_features.append(f)
        else:
            warnings.append(f"WARN {fid}: geometry type {gtype} not normalized")
            out_features.append(f)

    new_fc = copy.deepcopy(fc)
    new_fc["features"] = out_features
    return new_fc, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize chau_luc GeoJSON (clip + shared boundaries)")
    parser.add_argument("input", type=Path, help="Input .geojson (chau_luc scope)")
    parser.add_argument("-o", "--output", type=Path, help="Output path (default: stdout if -; else overwrite input with --in-place)")
    parser.add_argument("--in-place", action="store_true", help="Overwrite input file")
    parser.add_argument("--snap-prec", type=int, default=1, help="Decimal places for coordinates (default 1)")
    parser.add_argument("--snap-tol", type=float, default=2.0, help="Shapely snap tolerance for shared edges")
    parser.add_argument("--min-area", type=float, default=8.0, help="Drop partition fragments smaller than this")
    parser.add_argument("--no-fill-gaps", action="store_true", help="Do not merge gap polygons into neighbors")
    parser.add_argument(
        "--overlap",
        choices=("subtract", "warn"),
        default="subtract",
        help="subtract: remove overlap (partition); warn: clip+snap only, report overlaps",
    )
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    if data.get("world:scope") not in (None, "chau_luc"):
        print(f"Note: world:scope={data.get('world:scope')!r} (expected chau_luc)", file=sys.stderr)

    normalized, warnings = normalize_fc(
        data,
        snap_prec=args.snap_prec,
        snap_tolerance=args.snap_tol,
        min_area=args.min_area,
        fill_gaps=not args.no_fill_gaps,
        overlap_policy=args.overlap,
    )

    for w in warnings:
        print(w, file=sys.stderr)

    text = json.dumps(normalized, ensure_ascii=False, indent=2) + "\n"
    if args.in_place:
        out_path = args.input
    elif args.output:
        out_path = args.output
    else:
        sys.stdout.write(text)
        return 0

    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
