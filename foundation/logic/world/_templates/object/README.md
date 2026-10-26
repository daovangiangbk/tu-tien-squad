# Mẫu hồ sơ đối tượng thế giới

Sao chép toàn bộ thư mục này sang đối tượng active, thay metadata mẫu, rồi điền **sáu miền** theo khung 5 tầng trong [`../README.md`](../README.md). Đối tượng deferred chỉ cần `00-overview.md` và liên kết con.

```yaml
---
id: OBJ-ON-DINH
type: realm | planet | system | continent | region | site | micro
parent_id: ID-CHA
parent_path: ../00-overview.md
scope: active
status: draft
visibility: public
canon_source: []
child_index: []
---
```

## Sáu miền (bắt buộc khi `scope: active`)

| Thư mục | Tầng mẫu | File mẫu |
| --- | --- | --- |
| `power-system/` | 1 — Thiên đạo & quy tắc | [00-overview.md](power-system/00-overview.md) |
| `geo/` | 2 — Bản đồ & cấu trúc | [00-overview.md](geo/00-overview.md) |
| `social/` | 3.1 + 5.1 — Thế lực & triết lý tu sĩ | [00-overview.md](social/00-overview.md) |
| `economy/` | 3.2 — Kinh tế tu tiên | [00-overview.md](economy/00-overview.md) |
| `bio/` | 4 — Thực thể & chủng tộc | [00-overview.md](bio/00-overview.md) |
| `history/` | 5.2 — Lịch sử & thần thoại | [00-overview.md](history/00-overview.md) |

## Hoàn tất khi

- [ ] Metadata đủ và ID ổn định.
- [ ] Có liên kết `parent` và danh mục `children`.
- [ ] Đối tượng active phủ đủ sáu miền.
- [ ] Mỗi miền có 5–10 ý cấp cao (sau khi rút từ các mục gợi ý trong mẫu), ghi nguồn và trạng thái.
- [ ] Cha chỉ tóm tắt 1–2 dòng, không chép nội dung con.
- [ ] Liên kết tương đối mở đúng hồ sơ hoặc atlas hiện hữu.
- [ ] Ít nhất một chuỗi **logic xuyên tầng** (Tầng 1 → 2 → 3 hoặc 5) được ghi rõ ở planet/realm tương ứng.
