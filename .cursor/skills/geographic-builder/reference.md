# Geographic Builder — repo mapping (tien-hiep-novel)

## Scripts (canonical)

Tất cả nằm trong `.cursor/skills/geographic-builder/scripts/`:

| Script | Vai trò |
| --- | --- |
| `random_polygon.py` | Polygon ngẫu nhiên (lục tinh hà) |
| `build_world_tinh_ha.py` | Gom 4 lục → `00-tinh-ha.geojson` |
| `canvas_to_geojson.py` | Canvas layout + entities → chau_luc |
| `normalize_chau_luc.py` | Tùy chọn — sửa tay chau_luc (canvas pipeline gọi nội bộ) |
| `render_geojson.py` | PNG/SVG |
| `render_stack.sh` | Render tinh hà + chau-luc + region + micro |

`pip install -r .cursor/skills/geographic-builder/requirements.txt`

Shim cũ (vẫn chạy được): `tools/geo-shape-random/`, `tools/world-geo-normalizer/`, `tools/world-geo-visualizer/` → delegate sang skill.

## Geo files (tap-linh-dieu-lo)

| Tầng | File |
| --- | --- |
| Tinh hà | `projects/tap-linh-dieu-lo/logic/world/geo/00-tinh-ha.geojson` |
| Châu lục | `projects/tap-linh-dieu-lo/logic/world/geo/chau-luc/<slug>.geojson` |
| Region MC | `projects/tap-linh-dieu-lo/logic/world/geo/region/*.geojson` |

Convention: `foundation/logic/00-geojson-world-map-convention.md`.

## Neo tinh hà → châu lục

1. Lấy polygon `CHL-*` từ `00-tinh-ha`.
2. Chọn `world:parent_coordinates` = điểm neo trên tinh hà (vd. đông nam lục).
3. Scale local: `(tinh_xy - parent) * k` + offset để vừa `world:grid_extent` `[0,1000]`.
4. Cập nhật `region/*.geojson` `parent_coordinates` = hub trên chau_luc (vd. `LOC-THACH-LAM`).

## Canvas `y_axis`

- **`layout_down`** (mặc định trong `canvas_to_geojson.py`): khớp mẫu anchor `edge: top` → `y_min = ref_y - length`.
- **`north`**: y=Bắc (+) như GeoJSON repo — set `"canvas": { "y_axis": "north", ... }`.

## ID gợi ý

- `CHL-*`, `REG-*`, `CHAU-*`, `BRR-*`, `RIVER-*`, `LOC-*`
