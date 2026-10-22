# Mẫu hồ sơ đối tượng thế giới

Sao chép toàn bộ thư mục này sang đối tượng active, thay metadata mẫu, rồi giữ mỗi miền ở mức 5–10 gạch đầu dòng. Đối tượng deferred chỉ cần `00-overview.md` và liên kết con.

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

## Hoàn tất khi

- [ ] Metadata đủ và ID ổn định.
- [ ] Có liên kết `parent` và danh mục `children`.
- [ ] Đối tượng active phủ đủ sáu miền.
- [ ] Mỗi miền có 5–10 ý cấp cao, ghi nguồn và trạng thái.
- [ ] Cha chỉ tóm tắt 1–2 dòng, không chép nội dung con.
- [ ] Liên kết tương đối mở đúng hồ sơ hoặc atlas hiện hữu.
