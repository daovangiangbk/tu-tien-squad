# World GeoJSON normalizer (châu lục)

> **Canonical:** `.cursor/skills/geographic-builder/scripts/normalize_chau_luc.py`. File trong thư mục này là shim.

Hậu xử lý file `chau_luc/*.geojson` theo [`foundation/logic/00-geojson-world-map-convention.md`](../../foundation/logic/00-geojson-world-map-convention.md) §2.1.1:

1. **Feature đầu tiên** = vỏ lục (`Polygon`); mọi polygon / line / point khác **nằm trong** (clip / cảnh báo).
2. **Biên trong:** snap + loại overlap; cạnh mới snap vào union các vùng đã xử lý → **dùng chung biên** trong tolerance.
3. **Khe trống** (gap) trong lục: gộp vào vùng kề có biên chung dài nhất (tắt bằng `--no-fill-gaps`).

## Cài đặt

```bash
pip install -r .cursor/skills/geographic-builder/requirements.txt
# hoặc venv cục bộ:
cd tools/world-geo-normalizer && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

## Dùng

```bash
# Ghi đè file (world-builder sau khi vẽ tay)
python normalize_chau_luc.py \
  ../../projects/tap-linh-dieu-lo/logic/world/geo/chau-luc/chl-ha-gioi-nam.geojson \
  --in-place

# File mới + log cảnh báo trên stderr
python normalize_chau_luc.py input.geojson -o output.geojson
```

| Flag | Mặc định | Ý nghĩa |
| --- | --- | --- |
| `--snap-prec` | 1 | Làm tròn tọa độ (lưới 1000) |
| `--snap-tol` | 2.0 | Snap Shapely giữa các vùng (đơn vị lưới) |
| `--min-area` | 8.0 | Bỏ mảnh polygon quá nhỏ sau clip |
| `--no-fill-gaps` | off | Không gộp gap vào vùng lân cận |
| `--overlap` | `subtract` | `subtract` = phân vùng không chồng; `warn` = chỉ clip+snap, báo overlap |

**Gợi ý:** bản vẽ tay overlap nhiều → chạy `--overlap warn` xem log, chỉnh biên chung tay, rồi `subtract --in-place`.

Sau normalize nên chạy [`world-geo-visualizer`](../world-geo-visualizer/README.md) để kiểm tra PNG.

**Thứ tự feature:** feature[0] = lục; các `Polygon` còn lại = phân vùng (thứ tự ghi file có thể đổi sau normalize — sort theo diện tích khi xử lý).
