# Mẫu mô tả thế giới tu tiên / huyền huyễn

Khung **5 tầng tư duy** (Logic Layer) ánh xạ sang **sáu miền hồ sơ** bắt buộc cho đối tượng active — xem [`01-world-object-architecture.md`](../01-world-object-architecture.md).

| Tầng mẫu | Nội dung cốt lõi | Miền hồ sơ (`object/`) |
| --- | --- | --- |
| **1** Thiên đạo & quy tắc | Năng lượng, cảnh giới, bách nghệ | [`power-system/`](object/power-system/00-overview.md) |
| **2** Bản đồ & cấu trúc | Đa giới, địa lý, cấm địa | [`geo/`](object/geo/00-overview.md) |
| **3** Thế lực & kinh tế | Tổ chức, tranh tài nguyên, tiền tệ | [`social/`](object/social/00-overview.md) + [`economy/`](object/economy/00-overview.md) |
| **4** Thực thể & chủng tộc | Nhân / yêu / ma / thần thú | [`bio/`](object/bio/00-overview.md) |
| **5** Văn hóa, triết lý & lịch sử | Tâm lý tu sĩ, thần thoại, vết thương lịch sử | [`social/`](object/social/00-overview.md) (§ triết lý) + [`history/`](object/history/00-overview.md) |

## Cách dùng

1. Sao chép [`object/`](object/README.md) sang hồ sơ đối tượng active (realm → planet → …).
2. Điền từng miền theo **gợi ý trong mẫu**; mỗi miền giữ **5–10 ý cấp cao** khi chốt canon (không nhét bách khoa vào overview).
3. Neo **Foundation** trước: `foundation/core/00-glossary.md`, `02-world-laws-lore-core.md`, `03-power-system-economy-core.md`.
4. Kiểm tra **logic xuyên tầng**: thay đổi ở Tầng 1 (vd. linh khí cạn) phải lộ ra Tầng 3 (kinh tế) và Tầng 2 (cấm địa mở).

## Ví dụ logic xuyên tầng

- **Thiên đạo khuyết thiếu** → linh khí cạn (Tầng 1) → linh thạch đắt, linh thảo hiếm (Tầng 3) → tông lớn hút phàm / ma đan (Tầng 3 & 5).
- **Kết giới suy yếu** → cấm địa cổ mở (Tầng 2) → đệ tử liều mạng tìm cơ duyên (Tầng 2 & 1).

**Mẫu chi tiết:** [`object/README.md`](object/README.md)
