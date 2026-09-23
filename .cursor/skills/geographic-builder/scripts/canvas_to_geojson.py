#!/usr/bin/env python3
"""Convert canvas region layout + entities JSON to GeoJSON FeatureCollection."""
from __future__ import annotations

import argparse
import json
import math
import random
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from shapely.geometry import LineString, Polygon, mapping, shape
from shapely.geometry import box as shapely_box

try:
    from shapely.validation import make_valid
except ImportError:
    make_valid = None  # type: ignore


def snap(v: float, grid: int) -> int:
    if grid <= 0:
        return int(round(v))
    return int(round(v / grid) * grid)


def resolve_anchor(
    reg: dict,
    computed: dict[str, tuple[int, int, int, int]],
    y_axis: str,
) -> tuple[int, int]:
    anchor = reg["anchor"]
    w = int(reg["dimensions"]["width"])
    length = int(reg["dimensions"]["length"])

    if anchor["type"] == "absolute":
        return int(anchor["x"]), int(anchor["y"])

    ref_id = anchor["ref_id"]
    ref_x, ref_y, ref_w, ref_l = computed[ref_id]
    edge = anchor["edge"]
    align = anchor.get("align", "start")

    if y_axis == "layout_down":
        if edge == "right":
            x_min = ref_x + ref_w
            y_min = ref_y if align == "top" else ref_y + (ref_l - length)
        elif edge == "left":
            x_min = ref_x - w
            y_min = ref_y if align == "top" else ref_y + (ref_l - length)
        elif edge == "top":
            x_min = ref_x if align == "start" else ref_x + (ref_w - w)
            y_min = ref_y - length
        elif edge == "bottom":
            x_min = ref_x if align == "start" else ref_x + (ref_w - w)
            y_min = ref_y + ref_l
        else:
            raise ValueError(f"unknown edge {edge}")
        return x_min, y_min

    # y = North (+)
    if edge == "right":
        x_min = ref_x + ref_w
        y_min = ref_y + ref_l - length if align == "top" else ref_y
    elif edge == "left":
        x_min = ref_x - w
        y_min = ref_y + ref_l - length if align == "top" else ref_y
    elif edge == "top":
        x_min = ref_x if align == "start" else ref_x + (ref_w - w)
        y_min = ref_y + ref_l
    elif edge == "bottom":
        x_min = ref_x if align == "start" else ref_x + (ref_w - w)
        y_min = ref_y - length
    else:
        raise ValueError(f"unknown edge {edge}")
    return x_min, y_min


def border_settings(canvas: dict) -> tuple[int, float, float, int, random.Random]:
    """segments, amp_internal, amp_external, seed, rng."""
    rough = (canvas.get("border_roughness") or canvas.get("internal_border_roughness") or "medium").lower()
    presets = {
        "none": (4, 0.0, 0.0),
        "low": (8, 4.0, 1.5),
        "medium": (16, 10.0, 3.0),
        "high": (28, 16.0, 5.0),
    }
    seg, amp_in, amp_out = presets.get(rough, presets["medium"])
    seg = int(canvas.get("border_segments", seg))
    amp_in = float(canvas.get("border_amp_internal", canvas.get("border_amp", amp_in)))
    amp_out = float(canvas.get("border_amp_external", amp_out))
    seed = int(canvas.get("border_seed", canvas.get("seed", 20260916)))
    return seg, amp_in, amp_out, seed, random.Random(seed)


def _round_key(x: float, y: float, prec: int = 1) -> tuple[float, float]:
    return (round(float(x), prec), round(float(y), prec))


def wobble_segment(
    p0: tuple[float, float],
    p1: tuple[float, float],
    *,
    segments: int,
    amp: float,
    rng: random.Random,
) -> list[tuple[float, float]]:
    """Polyline p0→p1 with perpendicular noise; includes endpoints."""
    if amp <= 0 or segments < 2:
        return [p0, p1]
    ax, ay = p0
    bx, by = p1
    length = math.hypot(bx - ax, by - ay)
    if length < 1e-6:
        return [p0, p1]
    nx, ny = -(by - ay) / length, (bx - ax) / length
    waves = rng.randint(2, 5)
    phase = rng.random() * (2 * math.pi)
    out: list[tuple[float, float]] = [p0]
    for i in range(1, segments):
        t = i / segments
        x = ax + (bx - ax) * t
        y = ay + (by - ay) * t
        wobble = amp * (
            0.55 * math.sin(phase + t * math.pi * waves)
            + 0.35 * math.sin(phase * 1.7 + t * math.pi * (waves + 1))
            + 0.25 * (rng.random() - 0.5)
        )
        x += nx * wobble
        y += ny * wobble
        out.append((x, y))
    out.append(p1)
    return out


def shared_boundary_keys(
    boxes: dict[str, tuple[int, int, int, int]],
    *,
    eps: float = 1.0,
) -> set[tuple[Any, ...]]:
    """Keys for internal edges (vertical / horizontal) shared by two regions."""
    by_x: dict[float, list[tuple[str, float, float]]] = defaultdict(list)
    by_y: dict[float, list[tuple[str, float, float]]] = defaultdict(list)

    for _rid, (x, y, w, length) in boxes.items():
        x1, y1 = x + w, y + length
        by_x[float(x)].append(("L", float(y), float(y1)))
        by_x[float(x1)].append(("R", float(y), float(y1)))
        by_y[float(y)].append(("S", float(x), float(x1)))
        by_y[float(y1)].append(("N", float(x), float(x1)))

    shared: set[tuple[Any, ...]] = set()

    for x, items in by_x.items():
        lefts = [(a, b) for side, a, b in items if side == "L"]
        rights = [(a, b) for side, a, b in items if side == "R"]
        for y0, y1 in lefts:
            for y0r, y1r in rights:
                ya, yb = max(y0, y0r), min(y1, y1r)
                if yb - ya > eps:
                    shared.add(("V", round(x, 1), round(ya, 1), round(yb, 1)))

    for y, items in by_y.items():
        souths = [(a, b) for side, a, b in items if side == "S"]
        norths = [(a, b) for side, a, b in items if side == "N"]
        for x0, x1 in souths:
            for x0n, x1n in norths:
                xa, xb = max(x0, x0n), min(x1, x1n)
                if xb - xa > eps:
                    shared.add(("H", round(y, 1), round(xa, 1), round(xb, 1)))

    return shared


def edge_cache_key(
    p0: tuple[float, float],
    p1: tuple[float, float],
    shared_keys: set[tuple[Any, ...]],
) -> tuple[Any, ...]:
    x0, y0 = p0
    x1, y1 = p1
    if abs(x0 - x1) < 0.5:
        x = round((x0 + x1) / 2, 1)
        ya, yb = sorted((y0, y1))
        k = ("V", x, round(ya, 1), round(yb, 1))
        if k in shared_keys:
            return k
    if abs(y0 - y1) < 0.5:
        y = round((y0 + y1) / 2, 1)
        xa, xb = sorted((x0, x1))
        k = ("H", y, round(xa, 1), round(xb, 1))
        if k in shared_keys:
            return k
    return ("E", _round_key(p0[0], p0[1]), _round_key(p1[0], p1[1]))


def get_wobble_chain(
    p0: tuple[float, float],
    p1: tuple[float, float],
    *,
    shared_keys: set[tuple[Any, ...]],
    cache: dict[tuple[Any, ...], list[tuple[float, float]]],
    segments: int,
    amp_internal: float,
    amp_external: float,
    rng: random.Random,
) -> list[tuple[float, float]]:
    k = edge_cache_key(p0, p1, shared_keys)
    if k not in cache:
        is_internal = k[0] in ("V", "H")
        amp = amp_internal if is_internal else amp_external
        seg = segments if is_internal else max(6, segments // 2)
        sub_rng = random.Random(rng.randint(0, 2**31 - 1) ^ hash(k))
        cache[k] = wobble_segment(p0, p1, segments=seg, amp=amp, rng=sub_rng)
    chain = cache[k]
    if _round_key(chain[0][0], chain[0][1]) != _round_key(p0[0], p0[1]):
        chain = list(reversed(chain))
    return chain


def box_to_wobble_polygon(
    x: float,
    y: float,
    w: float,
    length: float,
    *,
    shared_keys: set[tuple[Any, ...]],
    cache: dict[tuple[Any, ...], list[tuple[float, float]]],
    segments: int,
    amp_internal: float,
    amp_external: float,
    rng: random.Random,
) -> Polygon:
    """y = North (+): south → east → north → west."""
    x1, y1 = x + w, y + length
    corners = [
        ((x, y), (x1, y)),
        ((x1, y), (x1, y1)),
        ((x1, y1), (x, y1)),
        ((x, y1), (x, y)),
    ]
    ring: list[tuple[float, float]] = []
    for p0, p1 in corners:
        chain = get_wobble_chain(
            p0,
            p1,
            shared_keys=shared_keys,
            cache=cache,
            segments=segments,
            amp_internal=amp_internal,
            amp_external=amp_external,
            rng=rng,
        )
        if ring:
            ring.extend(chain[1:])
        else:
            ring.extend(chain)
    if ring and ring[0] != ring[-1]:
        ring.append(ring[0])
    poly = Polygon(ring)
    if make_valid and not poly.is_valid:
        poly = make_valid(poly)
        if poly.geom_type == "MultiPolygon":
            poly = max(poly.geoms, key=lambda g: g.area)
    return poly


def compute_region_boxes(data: dict) -> dict[str, tuple[int, int, int, int]]:
    canvas = data.get("canvas") or {}
    grid = int(canvas.get("grid_snap", 1))
    y_axis = canvas.get("y_axis", "layout_down")
    computed: dict[str, tuple[int, int, int, int]] = {}
    for reg in data["regions"]:
        reg_id = reg["id"]
        w = int(reg["dimensions"]["width"])
        length = int(reg["dimensions"]["length"])
        x_min, y_min = resolve_anchor(reg, computed, y_axis)
        x_min, y_min = snap(x_min, grid), snap(y_min, grid)
        w, length = snap(w, grid), snap(length, grid)
        computed[reg_id] = (x_min, y_min, w, length)
    return computed


def regions_to_features(data: dict) -> tuple[list[dict], dict[str, tuple[int, int, int, int]]]:
    canvas = data.get("canvas") or {}
    regions = data["regions"]
    computed = compute_region_boxes(data)
    seg, amp_in, amp_out, _seed, rng = border_settings(canvas)
    shared_keys = shared_boundary_keys(computed)
    cache: dict[tuple[Any, ...], list[tuple[float, float]]] = {}
    features: list[dict] = []

    for reg in regions:
        reg_id = reg["id"]
        x_min, y_min, w, length = computed[reg_id]
        props = reg.get("properties") or {}
        straight = props.get("border_style") == "straight" or props.get("wobble") is False
        if straight:
            geom = shapely_box(x_min, y_min, x_min + w, y_min + length)
        else:
            geom = box_to_wobble_polygon(
                float(x_min),
                float(y_min),
                float(w),
                float(length),
                shared_keys=shared_keys,
                cache=cache,
                segments=seg,
                amp_internal=amp_in,
                amp_external=amp_out,
                rng=rng,
            )
        features.append(
            {
                "type": "Feature",
                "geometry": mapping(geom),
                "properties": {
                    "id": reg_id,
                    "name_vi": reg.get("name", reg_id),
                    "kind": reg.get("properties", {}).get("kind", reg.get("kind", "wilderness")),
                    **{k: v for k, v in reg.get("properties", {}).items() if k != "kind"},
                },
            }
        )
    return features, computed


def wobble_line(points: list[tuple[float, float]], roughness: str) -> LineString:
    if len(points) < 2 or roughness in ("none", "low", ""):
        return LineString(points)
    amp = {"low": 3, "medium": 8, "high": 15}.get(roughness, 8)
    seg = {"low": 6, "medium": 12, "high": 20}.get(roughness, 12)
    rng = random.Random(hash(tuple(points)) % 10_000)
    out: list[tuple[float, float]] = []
    for i in range(len(points) - 1):
        chain = wobble_segment(points[i], points[i + 1], segments=seg, amp=amp, rng=rng)
        if out:
            out.extend(chain[1:])
        else:
            out.extend(chain)
    return LineString(out)


def mountain_polygon(entity: dict, rng_seed: int = 0) -> Any:
    b = entity["bounds"]
    cx, cy = b["center"]["x"], b["center"]["y"]
    rx, ry = b["radius_x"], b["radius_y"]
    rng = random.Random(rng_seed)
    n = 24
    ring = []
    for i in range(n):
        t = 2 * math.pi * i / n
        rj = 0.75 + 0.25 * rng.random()
        ring.append((cx + rx * rj * math.cos(t), cy + ry * rj * math.sin(t)))
    ring.append(ring[0])
    return Polygon(ring)


def entities_to_features(entities: list[dict]) -> list[dict]:
    features = []
    for ent in entities:
        et = ent["type"]
        props = {"id": ent["id"], "name_vi": ent.get("name", ent["id"]), **ent.get("properties", {})}
        if et == "river":
            pts = [(p["x"], p["y"]) for p in ent["control_points"]]
            ls = wobble_line(pts, ent.get("roughness", "medium"))
            props["kind"] = "route"
            features.append({"type": "Feature", "geometry": mapping(ls), "properties": props})
        elif et == "point":
            c = ent["coordinates"]
            features.append(
                {
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [c["x"], c["y"]]},
                    "properties": props,
                }
            )
        elif et == "mountain_range":
            poly = mountain_polygon(ent, rng_seed=hash(ent["id"]) % 10_000)
            props["kind"] = "barrier"
            if make_valid:
                poly = make_valid(poly)
            features.append({"type": "Feature", "geometry": mapping(poly), "properties": props})
            b = ent.get("bounds") or {}
            center = b.get("center") or {}
            for peak in ent.get("peaks", []):
                px = center.get("x", 0) + peak["offset_x"]
                py = center.get("y", 0) + peak["offset_y"]
                features.append(
                    {
                        "type": "Feature",
                        "geometry": {"type": "Point", "coordinates": [px, py]},
                        "properties": {
                            "id": f"PEAK-{peak['name']}",
                            "name_vi": peak["name"],
                            "kind": "hub",
                            "elevation_m": peak.get("elevation_m"),
                        },
                    }
                )
        else:
            print(f"skip entity type {et}", file=sys.stderr)
    return features


def finalize_chau_luc(fc: dict) -> dict:
    """Clip partitions to shell, shared edges, gap fill — output-ready chau_luc."""
    from normalize_chau_luc import normalize_fc

    finalized, warnings = normalize_fc(fc)
    for w in warnings:
        print(w, file=sys.stderr)
    return finalized


def load_world_shell(path: Path, continent_id: str) -> dict | None:
    fc = json.loads(path.read_text(encoding="utf-8"))
    for f in fc.get("features", []):
        if (f.get("properties") or {}).get("id") == continent_id:
            return f
    return None


def json_to_geojson(
    data: dict,
    *,
    world_shell: dict | None = None,
    finalize: bool = True,
) -> dict:
    features: list[dict] = []
    if world_shell:
        features.append(world_shell)
    reg_feats, _ = regions_to_features(data)
    features.extend(reg_feats)
    entities = data.get("entities") or []
    features.extend(entities_to_features(entities))
    out: dict[str, Any] = {"type": "FeatureCollection", "features": features}
    if data.get("world"):
        out.update(data["world"])
    if finalize and world_shell is not None:
        out = finalize_chau_luc(out)
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Canvas layout JSON → GeoJSON (final chau_luc map)")
    p.add_argument("input", type=Path)
    p.add_argument("-o", "--output", type=Path, required=True)
    p.add_argument("--world-shell", type=Path, help="00-tinh-ha.geojson for continent polygon as feature[0]")
    p.add_argument("--continent-id", default="CHL-HA-GIOI-NAM")
    p.add_argument(
        "--no-finalize",
        action="store_true",
        help="Skip clip/overlap/gap pass (debug only)",
    )
    args = p.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    shell = None
    if args.world_shell:
        shell = load_world_shell(args.world_shell, args.continent_id)
        if shell is None:
            print(f"continent {args.continent_id} not found", file=sys.stderr)
            return 1

    fc = json_to_geojson(data, world_shell=shell, finalize=not args.no_finalize and shell is not None)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(fc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output} ({len(fc['features'])} features)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
