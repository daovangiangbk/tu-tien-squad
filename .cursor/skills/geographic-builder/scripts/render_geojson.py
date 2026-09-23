#!/usr/bin/env python3
"""
Render tien-hiep-novel world GeoJSON (story grid, not WGS84) to PNG or SVG.

Usage:
  python render_geojson.py path/to/file.geojson -o map.png
  python render_geojson.py projects/tap-linh-dieu-lo/logic/world/geo/00-tinh-ha.geojson
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Iterable

os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Polygon as MplPolygon

KIND_STYLE: dict[str, dict[str, Any]] = {
    "continent": {"facecolor": "#c4b59a", "edgecolor": "#5c4a32", "linewidth": 1.2, "alpha": 0.55, "zorder": 1},
    "polity": {"facecolor": "#a8c4e6", "edgecolor": "#3d6a9e", "linewidth": 1.0, "alpha": 0.45, "zorder": 2},
    "wilderness": {"facecolor": "#d8e4c8", "edgecolor": "#6b8f5e", "linewidth": 0.9, "alpha": 0.4, "zorder": 2},
    "hub": {"marker": "s", "color": "#c0392b", "size": 42, "zorder": 5},
    "settlement": {"marker": "o", "color": "#2980b9", "size": 28, "zorder": 4},
    "dungeon": {"marker": "^", "color": "#8e44ad", "size": 32, "zorder": 4},
    "resource": {"marker": "D", "color": "#d35400", "size": 26, "zorder": 4},
    "barrier": {"marker": "x", "color": "#2c3e50", "size": 30, "zorder": 4},
    "route": {"color": "#7f8c8d", "linewidth": 1.5, "zorder": 3},
    "default": {"marker": ".", "color": "#34495e", "size": 20, "zorder": 3},
}


def iter_coords(geometry: dict[str, Any]) -> Iterable[tuple[float, float]]:
    gtype = geometry["type"]
    coords = geometry["coordinates"]
    if gtype == "Point":
        yield tuple(coords)
    elif gtype == "LineString":
        for c in coords:
            yield tuple(c)
    elif gtype == "Polygon":
        for ring in coords:
            for c in ring:
                yield tuple(c)
    elif gtype == "MultiPolygon":
        for poly in coords:
            for ring in poly:
                for c in ring:
                    yield tuple(c)
    else:
        raise ValueError(f"Unsupported geometry type: {gtype}")


def load_fc(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if data.get("type") != "FeatureCollection":
        raise ValueError(f"{path}: expected FeatureCollection")
    return data


def bbox_from_fc(fc: dict[str, Any]) -> tuple[float, float, float, float]:
    xs: list[float] = []
    ys: list[float] = []
    for feat in fc.get("features", []):
        geom = feat.get("geometry")
        if not geom:
            continue
        for x, y in iter_coords(geom):
            xs.append(x)
            ys.append(y)
    if not xs:
        return (-1, -1, 1, 1)
    pad_x = max((max(xs) - min(xs)) * 0.08, 8)
    pad_y = max((max(ys) - min(ys)) * 0.08, 8)
    return (min(xs) - pad_x, min(ys) - pad_y, max(xs) + pad_x, max(ys) + pad_y)


def _ring_points(ring: list[list[float]]) -> list[tuple[float, float]]:
    pts = [tuple(p) for p in ring]
    if len(pts) > 1 and pts[0] == pts[-1]:
        pts = pts[:-1]
    return pts


def label_anchor(geometry: dict[str, Any]) -> tuple[float, float] | None:
    """Center of shape for label placement (polygon centroid, line midpoint, point)."""
    gtype = geometry["type"]
    coords = geometry["coordinates"]

    if gtype == "Point":
        return tuple(coords)

    if gtype == "LineString":
        pts = [tuple(c) for c in coords]
        if not pts:
            return None
        if len(pts) == 1:
            return pts[0]
        mx = sum(p[0] for p in pts) / len(pts)
        my = sum(p[1] for p in pts) / len(pts)
        return (mx, my)

    if gtype == "Polygon":
        pts = _ring_points(coords[0])
        if not pts:
            return None
        area = 0.0
        cx = 0.0
        cy = 0.0
        n = len(pts)
        for i in range(n):
            x0, y0 = pts[i]
            x1, y1 = pts[(i + 1) % n]
            cross = x0 * y1 - x1 * y0
            area += cross
            cx += (x0 + x1) * cross
            cy += (y0 + y1) * cross
        area *= 0.5
        if abs(area) < 1e-12:
            return (sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n)
        cx /= 6.0 * area
        cy /= 6.0 * area
        return (cx, cy)

    if gtype == "MultiPolygon":
        best: tuple[float, float] | None = None
        best_area = 0.0
        for poly in coords:
            sub = {"type": "Polygon", "coordinates": poly}
            c = label_anchor(sub)
            if not c:
                continue
            pts = _ring_points(poly[0])
            a = 0.0
            for i in range(len(pts)):
                x0, y0 = pts[i]
                x1, y1 = pts[(i + 1) % len(pts)]
                a += x0 * y1 - x1 * y0
            a = abs(a * 0.5)
            if a >= best_area:
                best_area = a
                best = c
        return best

    return None


def label_for(props: dict[str, Any], mode: str) -> str:
    if mode == "id":
        return props.get("id", "")
    if mode == "vi":
        return props.get("name_vi") or props.get("id", "")
    if mode == "both":
        vi = props.get("name_vi", "")
        fid = props.get("id", "")
        return f"{vi}\n({fid})" if vi and fid else (vi or fid)
    return ""


def render(
    fc: dict[str, Any],
    *,
    title: str,
    label_mode: str,
    dpi: int,
    figsize: tuple[float, float],
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=figsize)
    xmin, ymin, xmax, ymax = bbox_from_fc(fc)

    route_segments: list[list[tuple[float, float]]] = []

    for feat in fc.get("features", []):
        props = feat.get("properties") or {}
        geom = feat.get("geometry")
        if not geom:
            continue
        kind = props.get("kind", "default")
        gtype = geom["type"]

        if gtype == "Polygon":
            style = KIND_STYLE.get(kind, KIND_STYLE["wilderness"])
            if kind == "barrier":
                style = {
                    **style,
                    "facecolor": "#5d6d7e",
                    "edgecolor": "#2c3e50",
                    "alpha": 0.65,
                    "linewidth": 1.2,
                    "zorder": 3,
                }
            ring = geom["coordinates"][0]
            patch = MplPolygon(
                ring,
                closed=True,
                facecolor=style.get("facecolor", "#cccccc"),
                edgecolor=style.get("edgecolor", "#666666"),
                linewidth=style.get("linewidth", 1),
                alpha=style.get("alpha", 0.5),
                zorder=style.get("zorder", 1),
            )
            ax.add_patch(patch)
        elif gtype == "LineString":
            if kind == "route":
                route_segments.append([tuple(c) for c in geom["coordinates"]])
            else:
                xs, ys = zip(*geom["coordinates"])
                ax.plot(xs, ys, color="#555555", linewidth=1.2, zorder=3)
        elif gtype == "Point":
            style = KIND_STYLE.get(kind, KIND_STYLE["default"])
            x, y = geom["coordinates"]
            ax.scatter(
                [x],
                [y],
                marker=style.get("marker", "o"),
                c=style.get("color", "#333333"),
                s=style.get("size", 24),
                zorder=style.get("zorder", 4),
                edgecolors="white",
                linewidths=0.6,
            )

    if route_segments:
        style = KIND_STYLE["route"]
        lc = LineCollection(
            route_segments,
            colors=style["color"],
            linewidths=style["linewidth"],
            zorder=style["zorder"],
            linestyles="--",
        )
        ax.add_collection(lc)

    for feat in fc.get("features", []):
        props = feat.get("properties") or {}
        geom = feat.get("geometry")
        if not geom:
            continue
        text = label_for(props, label_mode)
        if not text:
            continue
        anchor = label_anchor(geom)
        if anchor is None:
            continue
        x, y = anchor
        ax.text(
            x,
            y,
            text,
            ha="center",
            va="center",
            fontsize=7,
            color="#1a1a1a",
            zorder=6,
            clip_on=True,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor="none", alpha=0.75),
        )

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linestyle=":", alpha=0.35)
    ax.set_xlabel("Đông (+x)")
    ax.set_ylabel("Bắc (+y)")

    scope = fc.get("world:scope", "")
    note = fc.get("world:coordinateNote", "")
    subtitle = " · ".join(p for p in [scope, note[:80] + ("…" if len(note) > 80 else "") if note else ""] if p)
    ax.set_title(f"{title}\n{subtitle}" if subtitle else title, fontsize=11)

    parent = fc.get("world:parent_coordinates")
    if parent and len(parent) == 2:
        ax.scatter(
            [parent[0]],
            [parent[1]],
            marker="+",
            c="#e67e22",
            s=120,
            linewidths=2,
            zorder=7,
            label="parent origin",
        )
        ax.legend(loc="upper right", fontsize=8)

    fig.tight_layout()
    return fig


def default_output_path(input_path: Path, fmt: str) -> Path:
    return input_path.with_suffix(f".{fmt}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Render world GeoJSON to PNG/SVG")
    parser.add_argument("geojson", type=Path, help="Path to .geojson file")
    parser.add_argument("-o", "--output", type=Path, help="Output image path (.png or .svg)")
    parser.add_argument(
        "--format",
        choices=("png", "svg"),
        default="png",
        help="Output format if -o omitted (default: png)",
    )
    parser.add_argument(
        "--labels",
        choices=("id", "vi", "both", "none"),
        default="vi",
        help="Feature labels at shape center (default: name_vi)",
    )
    parser.add_argument("--dpi", type=int, default=150, help="PNG dpi (default: 150)")
    parser.add_argument("--width", type=float, default=10, help="Figure width inches")
    parser.add_argument("--height", type=float, default=10, help="Figure height inches")
    args = parser.parse_args()

    if not args.geojson.is_file():
        print(f"File not found: {args.geojson}", file=sys.stderr)
        return 1

    fc = load_fc(args.geojson)
    out = args.output or default_output_path(args.geojson, args.format)
    if args.output and args.output.suffix.lower() == ".svg":
        fmt = "svg"
    elif args.output and args.output.suffix.lower() == ".png":
        fmt = "png"
    else:
        fmt = args.format if not args.output else out.suffix.lstrip(".").lower()

    title = args.geojson.name
    fig = render(
        fc,
        title=title,
        label_mode=args.labels,
        dpi=args.dpi,
        figsize=(args.width, args.height),
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=args.dpi if fmt == "png" else None, bbox_inches="tight")
    plt.close(fig)
    print(out.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
