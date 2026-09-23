# Projects — nhiều tác phẩm

Mỗi tiểu thuyết (tác phẩm) **active** là **một thư mục con** `projects/<work-slug>/`. Tác phẩm **archive** nằm tại `projects/archive/<work-slug>/` — xem [`archive/README.md`](archive/README.md).

| File / thư mục | Vai trò |
| --- | --- |
| `projects/active-work.md` | Slug tác phẩm đang làm việc (một dòng); **chỉ** slug **active**, không trỏ `archive/` |
| `projects/archive/` | Work đóng gói — read-only pipeline mặc định; bảng + thủ tục trong `archive/README.md` |
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

**Quy ước slug:** chữ thường, số, gạch ngang (`tap-linh-dieu-lo`, `vo-dong-ky`).

## Tác phẩm active

| Slug | Tên hiển thị | Ghi chú |
| --- | --- | --- |
| [`ham-mo`](ham-mo/00-master-brief.md) | **Hầm mỏ** | Pipeline A — **truyện ngắn** 4 chương; shared `foundation/`; geo stack waived |

**Archived:** [`archive/README.md`](archive/README.md) (bảng + `git mv` / restore).

## Lifecycle (tóm tắt)

| Trạng thái | Path | Orchestrator |
| --- | --- | --- |
| **active** | `projects/<slug>/` | Delegate pipeline A/B/C bình thường |
| **archived** | `projects/archive/<slug>/` | **Không** `T-prose-*` / geo mới / CP mặc định; read-only hoặc **restore** khi user yêu cầu |

`T-archive-project` · `T-restore-project` — **thủ tục repo tùy chọn**, không thuộc pipeline A/B/C; chỉ khi user yêu cầu — `.cursor/agents/project-orchestrator.md` §1.10.
