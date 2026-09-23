# PNG — Phàm Giới (`foundation-canon`)

**Quy ước tên (canon atlas):** tên file = stem GeoJSON, không prefix `chau-luc-` / `region-`.

| Tầng | Pattern | Ví dụ |
| --- | --- | --- |
| Tinh hà | `00-tinh-ha.png` | `geo/00-tinh-ha.geojson` |
| Châu lục | `<chl-slug>.png` | `chl-xich-ha.png` ← `chau-luc/chl-xich-ha.geojson` |
| Region | `<reg-slug>.png` | `reg-xh-de-do.png` ← `region/reg-xh-de-do.geojson` |

Render (không dùng `render_stack.sh` — script đó ghi `chau-luc-*` / `region-*`):

```bash
PY=python3  # hoặc .cursor/skills/geographic-builder/scripts/.venv/bin/python
R=scripts/render_geojson.py  # từ repo root: .cursor/skills/geographic-builder/scripts/render_geojson.py
GEO=foundation/logic/world/realms/pham-gioi/geo
OUT=$GEO/out

$PY $R $GEO/00-tinh-ha.geojson -o $OUT/00-tinh-ha.png --labels both
for f in $GEO/chau-luc/*.geojson; do
  b=$(basename "$f" .geojson)
  $PY $R "$f" -o "$OUT/$b.png" --labels both
done
for f in $GEO/region/*.geojson; do
  b=$(basename "$f" .geojson)
  $PY $R "$f" -o "$OUT/$b.png" --labels both
done
```

**Tàn Mộ (7 REG Phase 1e):** tái sinh GeoJSON — `python3 scripts/build_tm_regions_1e.py` (cwd `realms/pham-gioi/`), rồi loop region render ở trên.

Liên kết: [`../../00-world-atlas.md`](../../00-world-atlas.md)
