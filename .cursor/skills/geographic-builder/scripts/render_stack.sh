#!/usr/bin/env bash
# Render default geo stack for a project work_root (logic/world/geo).
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORK_ROOT="${1:?Usage: render_stack.sh projects/<slug>}"
GEO="$WORK_ROOT/logic/world/geo"
OUT="$GEO/out"
PY="${PYTHON:-python3}"
if [[ -x "$SCRIPT_DIR/.venv/bin/python" ]]; then
  PY="$SCRIPT_DIR/.venv/bin/python"
fi
mkdir -p "$OUT"
if [[ -f "$GEO/00-tinh-ha.geojson" ]]; then
  "$PY" "$SCRIPT_DIR/render_geojson.py" "$GEO/00-tinh-ha.geojson" -o "$OUT/00-tinh-ha.png" --labels both
fi
for cl in "$GEO"/chau-luc/*.geojson; do
  [[ -f "$cl" ]] || continue
  base="$(basename "$cl" .geojson)"
  "$PY" "$SCRIPT_DIR/render_geojson.py" "$cl" -o "$OUT/chau-luc-$base.png" --labels both
done
for reg in "$GEO"/region/*.geojson; do
  [[ -f "$reg" ]] || continue
  base="$(basename "$reg" .geojson)"
  "$PY" "$SCRIPT_DIR/render_geojson.py" "$reg" -o "$OUT/region-$base.png" --labels both
done
for micro in "$GEO"/micro/*.geojson; do
  [[ -f "$micro" ]] || continue
  base="$(basename "$micro" .geojson)"
  "$PY" "$SCRIPT_DIR/render_geojson.py" "$micro" -o "$OUT/micro-$base.png" --labels both
done
echo "Wrote PNGs under $OUT"
