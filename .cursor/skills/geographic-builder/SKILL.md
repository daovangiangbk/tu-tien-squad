---
name: geographic-builder
description: Builds world-scale and continent-scale geographic maps as GeoJSON—random continent shapes (geo-shape-random), non-overlapping placement, canvas region layouts with shared edges, rivers and mountain entities. Use when the user asks for geographic-builder, world map / tinh hà / châu lục GeoJSON, canvas region JSON, or converting layout JSON to GeoJSON.
---

# Geographic Builder

## Phạm vi

| Mode | Input | Output |
| --- | --- | --- |
| **World map** | 4–10 lục, bbox tinh hà | `FeatureCollection` (`world:scope`: `tinh_ha`) |
| **Continent map** | GeoJSON lục từ world + canvas JSON | `FeatureCollection` (`world:scope`: `chau_luc`) |

Repo tiên hiệp: đọc thêm [reference.md](reference.md) (4 tầng, render PNG).

---

## 1. World map (bản đồ thế giới)

1. Chọn **4–10** `CHL-*`; đặt **tâm bbox** trên lưới tinh hà (x=Đông, y=Bắc), **không chồng** (kiểm tra bbox hoặc Shapely).
2. Mỗi lục: sinh polygon bằng [scripts/random_polygon.py](scripts/random_polygon.py):
   ```bash
   python .cursor/skills/geographic-builder/scripts/random_polygon.py \
     -n 28 --bounds 0 200 0 160 -c 0.35 --seed <n> --coords-only
   ```
3. **Dịch** ring tới tâm đã chọn; feature[0] = `TINH-HA-REF` Point `[0,0]`; các feature sau = `kind: continent`.
4. Ghi `projects/<slug>/logic/world/geo/00-tinh-ha.geojson` + cập nhật `00-world-atlas.md`.
5. Render: `scripts/render_geojson.py` hoặc `scripts/render_stack.sh <projects/<slug>>` → `geo/out/*.png`.

Helper (tùy chọn): [scripts/build_world_tinh_ha.py](scripts/build_world_tinh_ha.py).

**Phụ thuộc:** `pip install -r .cursor/skills/geographic-builder/requirements.txt`

---

## 2. Continent map (bản đồ châu lục)

**Ràng buộc:** giữ **silhouette** lục từ world GeoJSON (feature `CHL-*`); chi tiết bên trong qua canvas → GeoJSON.

### Bước 1 — Canvas tổng thể (`type`: `"region"`)

Tạo JSON layout (có thể lưu `logic/world/canvas/<chl-slug>.canvas.json`):

```json
{
  "continent": "Châu Âu",
  "canvas": { "unit": "km", "grid_snap": 10 },
  "regions": [
    {
      "id": "tay_au",
      "name": "Tây Âu",
      "dimensions": { "width": 300, "length": 250 },
      "anchor": { "type": "absolute", "x": 200, "y": 400 },
      "properties": { "climate": "Ôn đới hải dương", "main_countries": ["Pháp", "Đức", "Hà Lan"] }
    },
    {
      "id": "bac_au",
      "name": "Bắc Âu",
      "dimensions": { "width": 350, "length": 200 },
      "anchor": { "type": "relative", "ref_id": "tay_au", "edge": "top", "align": "start" },
      "properties": { "climate": "Hàn đới / Ôn đới lạnh", "main_countries": ["Thụy Điển", "Na Uy", "Phần Lan"] }
    },
    {
      "id": "dong_au",
      "name": "Đông Âu",
      "dimensions": { "width": 450, "length": 400 },
      "anchor": { "type": "relative", "ref_id": "tay_au", "edge": "right", "align": "top" },
      "properties": { "climate": "Ôn đới lục địa", "main_countries": ["Ba Lan", "Ukraine", "Romania"] }
    },
    {
      "id": "nam_au",
      "name": "Nam Âu",
      "dimensions": { "width": 300, "length": 150 },
      "anchor": { "type": "relative", "ref_id": "tay_au", "edge": "bottom", "align": "start" },
      "properties": { "climate": "Địa Trung Hải", "main_countries": ["Ý", "Tây Ban Nha", "Hy Lạp"] }
    }
  ]
}
```

- `width` / `length` = cạnh theo trục x / y canvas.
- **Biên trong chia sẻ:** `relative` + `edge` bám mép `ref_id` (cùng tọa độ sau `grid_snap`).
- Repo tiên hiệp: sau bước 3, **feature[0]** = polygon lục khớp `00-tinh-ha`; các vùng = `REG-*` / `CHAU-*` / `BRR-*` khép kín (convention §2.1.1).
- **Biên nội:** trong `canvas` có thể set `border_roughness` (`low`|`medium`|`high`), `border_segments`, `border_amp_internal`, `border_seed` — `canvas_to_geojson` sinh biên chia sẻ **gợn sóng + ngẫu nhiên** (cùng polyline hai vùng kề nhau).

### Bước 2 — Thực thể trên canvas

```json
{
  "id": "song_danube",
  "name": "Sông Danube",
  "type": "river",
  "properties": { "width": 15 },
  "path_definition": { "start_region": "tay_au", "end_region": "dong_au" },
  "control_points": [
    { "x": 250, "y": 450, "label": "Thượng nguồn" },
    { "x": 480, "y": 520, "label": "Khúc uốn giữa" },
    { "x": 750, "y": 600, "label": "Hạ nguồn" }
  ],
  "roughness": "medium"
}
```

```json
{
  "id": "day_alps",
  "name": "Dãy Alps",
  "type": "mountain_range",
  "bounds": {
    "center": { "x": 350, "y": 500 },
    "radius_x": 120,
    "radius_y": 60,
    "shape": "irregular_ellipse"
  },
  "peaks": [
    { "name": "Mont Blanc", "offset_x": -20, "offset_y": 5, "elevation_m": 4810 },
    { "name": "Matterhorn", "offset_x": 10, "offset_y": -10, "elevation_m": 4478 }
  ]
}
```

- `river` → GeoJSON `LineString`, `kind: route`, id `RIVER-*`; uốn khúc (nhiều đỉnh, `roughness`).
- `mountain_range` → GeoJSON **`Polygon`** (một **vùng** `BRR-*`, `kind: barrier`), không LineString.

Gom vào cùng file canvas: `"entities": [ ... ]` hoặc file `*.entities.json`.

### Bước 3 — Canvas → GeoJSON

Chạy script (Shapely):

```bash
pip install -r .cursor/skills/geographic-builder/requirements.txt
python .cursor/skills/geographic-builder/scripts/canvas_to_geojson.py path/to/canvas.json \
  -o path/to/chau-luc.geojson \
  --world-shell path/to/00-tinh-ha.geojson --continent-id CHL-HA-GIOI-NAM
python .cursor/skills/geographic-builder/scripts/render_geojson.py path/to/chau-luc.geojson \
  -o geo/out/....png --labels both
```

`canvas_to_geojson` (khi có `--world-shell`) **tự** clip vào vỏ lục, xử lý chồng lấn, gộp khe — **không** cần bước normalize riêng. Script `normalize_chau_luc.py` chỉ dùng khi sửa tay file `.geojson`.

---

## Checklist agent

**World**

- [ ] 4–10 lục, random shape, không overlap
- [ ] `00-tinh-ha.geojson` + atlas link
- [ ] PNG tinh hà

**Continent**

- [ ] Vỏ lục = silhouette world (scale + `world:parent_coordinates`)
- [ ] Canvas regions khép kín / biên chung
- [ ] Núi = polygon vùng; sông = uốn khúc
- [ ] `canvas_to_geojson` + PNG (biên nội gợn nếu cần: `border_roughness` trong canvas)

---

## Tài liệu thêm

- [reference.md](reference.md) — mapping repo, anchor tinh hà → chau_luc
- [requirements.txt](requirements.txt) — shapely, matplotlib
- [scripts/](scripts/) — `random_polygon`, `canvas_to_geojson`, `normalize_chau_luc`, `render_geojson`, `render_stack.sh`, `build_world_tinh_ha`
