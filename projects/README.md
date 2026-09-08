# Projects — nhiều tác phẩm

Mỗi tiểu thuyết (tác phẩm) là **một thư mục con** `projects/<work-slug>/`.

| File / thư mục | Vai trò |
| --- | --- |
| `projects/active-work.md` | Slug tác phẩm đang làm việc (một dòng) |
| `projects/<slug>/00-master-brief.md` | Master Brief — `requirements-briefer` |
| `projects/<slug>/00-progress-map.md` | **Bản đồ tiến độ Phase → Arc → Chapter** (multi-session) |
| `projects/<slug>/status.md` | Trạng thái & task queue — `project-orchestrator` |
| `projects/<slug>/logic/` | Arc, foreshadow, **story/chapter spine** (Logic Layer) |
| `projects/<slug>/logic/00-story-spine.md` | Cốt truyện + dòng arc (xương sống) |
| `projects/<slug>/logic/chapters/00-chapter-spine-*.md` | Bảng chương trước prose |
| `projects/<slug>/interface/chapters/00-index.md` | Mục lục chương đã/chưa viết |
| `projects/<slug>/core-proposals/` | Core enrichment **propose** (CP-*.md) — human approve trước khi chạy Foundation |
| `projects/<slug>/interface/chapter-view/` | Review comment only — file **`review-*.md`** |
| `projects/<slug>/interface/` | Prose chương, registry tên (Interface Layer) |
| `projects/<slug>/foundation/` | *(tùy chọn)* Core riêng tác phẩm |

**Foundation dùng chung:** tác phẩm có thể trỏ `foundation_root: foundation/` ở root repo (xem brief §0). Tác phẩm mới hoàn toàn độc lập → đặt Core trong `projects/<slug>/foundation/core/`.

**Quy ước slug:** chữ thường, số, gạch ngang (`tien-hiep-novel`, `vo-dong-ky`).

## Tác phẩm trong repo

| Slug | Tên hiển thị | Ghi chú |
| --- | --- | --- |
| `tien-hiep-novel` | Tiên Hiệp Novel | Core dùng chung `foundation/` root |
