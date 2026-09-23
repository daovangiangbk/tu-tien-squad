# World GeoJSON visualizer

> **Canonical:** `.cursor/skills/geographic-builder/scripts/render_geojson.py`, `render_stack.sh`. File trong thư mục này là shim.

Render bản đồ kiến thế (`world/geo/*.geojson`, lưới story grid — **không** WGS84) thành **PNG** hoặc **SVG**.

Quy ước GeoJSON: [`foundation/logic/00-geojson-world-map-convention.md`](../../foundation/logic/00-geojson-world-map-convention.md).

## Cài đặt

```bash
pip install -r .cursor/skills/geographic-builder/requirements.txt
```

## Dùng

```bash
# Một file → cùng thư mục, tên .png
python render_geojson.py ../../../projects/tap-linh-dieu-lo/logic/world/geo/00-tinh-ha.geojson

# Chỉ định output
python render_geojson.py path/to/region/reg-thach-lam.geojson -o /tmp/region-thach-lam.png

# SVG, nhãn id + tên
python render_geojson.py path/to/micro/arc-01-phi-van-tap.geojson -o map.svg --labels both --dpi 200
```

### Tuỳ chọn

| Flag | Ý nghĩa |
| --- | --- |
| `-o` | File ảnh đích |
| `--format png\|svg` | Khi không có `-o` |
| `--labels id\|vi\|both\|none` | Nhãn điểm (mặc định: `name_vi`) |
| `--dpi` | PNG (mặc định 150) |
| `--width` / `--height` | Inch (mặc định 10×10) |

### Render cả stack (gợi ý)

```bash
./render_stack.sh ../../../projects/tap-linh-dieu-lo
python render_geojson.py "$GEO/micro/arc-01-phi-van-tap.geojson" -o "$GEO/out/phi-van.png"
```

Thư mục `geo/out/` có thể thêm vào `.gitignore` nếu chỉ là artifact local.

## Ký hiệu

- **Polygon:** màu theo `kind` (continent, polity, wilderness…)
- **Point:** hình theo `kind` (hub vuông, dungeon tam giác…)
- **LineString** `route`: nét đứt xám
- **Nhãn:** `name_vi` / `id` đặt **giữa** shape (centroid polygon, midpoint line, tại point)
- **+** cam: `world:parent_coordinates` (neo tầng cha)
