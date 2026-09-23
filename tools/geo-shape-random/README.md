# Random polygon generator

> **Canonical:** `.cursor/skills/geographic-builder/scripts/random_polygon.py` (skill **geographic-builder**). File trong thư mục này là shim.

Sinh **một polygon đơn giản** (không tự cắt) với **tọa độ nguyên**, dùng thử layout châu lục / vùng.

## Thuật toán

- Chọn `n` góc cực, sort theo góc quanh tâm hộp → polygon sao đơn.
- Bán kính mỗi đỉnh: `r = 1 - concavity × U(0,1)` (làm mượt lân cận nếu `concavity > 0`).
- **`concavity = 0`:** gần hình elip đều (lồi). **`concavity → 1`:** lõm / răng cưa mạnh hơn.

## Dùng

```bash
python random_polygon.py -n 32 --bounds 0 1000 0 1000 -c 0.45 --seed 7 -o /tmp/rnd.geojson

# Chỉ mảng tọa độ (copy vào GeoJSON tay)
python random_polygon.py -n 20 --bounds 0 1000 0 1000 -c 0.2 --coords-only
```

| Tham số | Ý |
| --- | --- |
| `-n` | Số đỉnh (≥ 3) |
| `--bounds` | `XMIN XMAX YMIN YMAX` (mặc định `0 1000 0 1000`) |
| `-c` / `--concavity` | Độ lồi lõm, 0…1 |
| `--seed` | Cố định kết quả |
| `-o` | File GeoJSON (1 Feature `Polygon`) |

Không phụ thuộc ngoài stdlib. Render: `.cursor/skills/geographic-builder/scripts/render_geojson.py`.
