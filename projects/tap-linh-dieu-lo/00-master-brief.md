# Master Brief — Tạp Linh Diêu Lộ — v3 — 2026-09-09

> Khung làm việc cho hệ subagent. Cập nhật version + mục **Changelog** khi đổi phạm vi; `project-orchestrator` đánh dấu artifact stale.

## 0. Work identity

| Trường              | Giá trị                                       |
| ------------------- | --------------------------------------------- |
| **work_title**      | **Tạp Linh Diêu Lộ** (杂灵遥路)                |
| **work_title_short**| *Diêu Lộ* (遥路) — rút gọn khi cần            |
| **work_slug**       | `tap-linh-dieu-lo` *(thư mục `projects/`; trước: `tien-hiep-novel`)* |
| **work_root**       | `projects/tap-linh-dieu-lo/`                   |
| **foundation_root** | `foundation/` *(shared — Core tại repo root)* |
| **logic_root**      | `projects/tap-linh-dieu-lo/logic/`             |
| **interface_root**  | `projects/tap-linh-dieu-lo/interface/`         |

## 1. Raw intent (user)

> Nam tán tu, lấy tự do, tiêu diêu tự tại làm đạo, không màng chính đạo, ma đạo. Hành động vì chính nghĩa. Tuy là tạp linh căn (Hoả, Kim, Mộc) nhưng có trí tuệ siêu phàm, biến nguy thành an trong tình huống thập tử nhất sinh. Quãng đường tu tiên gặp nhiều trắc trở, nhưng gặp được nhiều cơ duyên may mắn. Sức mạnh phát triển toàn diện Thể Lực - Linh Lực - Thần Lực, đa ngành đa nghề, tuy yếu nhưng biến ảo khôn lường.

## 2. Tóm tắt điều hành (5–10 dòng)

Tiểu thuyết tiên hiệp dài, tone **Tru Tiên** (triết lý xám, bi kịch, phục bút). **MC contract:** tán tu, tiêu diêu (tư tưởng + ít ràng buộc môn), tạp linh căn Hỏa–Kim–Mộc map archetype Core §3.1; yếu tài nguyên trung bình, mạnh **trí tuệ, cơ duyên, đa nghề** (đan/khí/trận/phù) và Thể–Linh–Thần cân bằng; **chính nghĩa = hành vi**, không gắn phe Chính/Ma. **Phase 1 Logic:** outline đại cục đến **Trúc Cơ kỳ đỉnh phong** (~2–3 arc). **Quan hệ tình:** NC/tam giác **trì hoãn** — Arc 1 tập trung tán tu, kinh tế, bí cảnh. Core shared `foundation/core/01–03`; tên canon ở Interface sau naming.

## 3. Mục tiêu & thành công

- **Sản phẩm:** Tiểu thuyết markdown trong repo; có thể xuất bản sau.
- **Độc giả / tone:** Quen “cái giá tu luyện”; phe xám; cảm xúc trầm, iconic moment.
- **Phase 1 thành công:** Arc outline + chương 1 khớp Core; MC không power creep đa nghề vô luật.
- **Không làm:** Power creep vô luật; spoil twist arc xa sớm; sửa Core im lặng khi chỉ sửa chương.

## 4. Phạm vi & quy mô

| Hạng mục | Giá trị |
| --- | --- |
| **Phase 1 (Logic v1)** | 2–3 arc (hoặc 2 arc + transition) đến **Trúc Cơ kỳ đỉnh phong** |
| **Quy mô phase 1** | ~80–120 chương; ~2.500–4.000 chữ/chương |
| **Endgame dài hạn** | Mở rộng sau (Kết Đan+, phi thăng/Tiên Giới) — **chưa** khóa trong outline v1 |
| **POV** | Third limited (MC); không đa POV chính; có thể đoạn mở đầu chương / tin truyền âm ngắn |
| **Định dạng output** | Markdown dưới `projects/tap-linh-dieu-lo/interface/` |
| **Ngôn ngữ** | Tiếng Việt; danh từ riêng Hán Việt theo `foundation/core/00-glossary.md` |

## 5. Ràng buộc sáng tác

- **Theme ưu tiên:** Nghịch Thiên Nhi Hành; Vô tình vs Hữu tình; Chính–Tà theo ứng xụ; Cường giả vi tôn (`01-theme-tragedy-core.md`).
- **Luật / cảnh giới:** Bám Core trong `foundation_root`; tạp căn variant tham chiếu `foundation/resources/11-thien-phu-ky-nang-an.md`; đa nghề `10-phu-nghe-tu-tien.md` — mỗi buff có **trade-off** (Core 03).
- **Nội dung nhạy cảm / giới hạn:** Bạo lực tu tiên có **cái giá** trên trang; không miêu tả tình dục/graphic; Ma/Tà công pháp có trade-off Nghiệp/Tâm ma.
- **Khác biệt vs Tru Tiên:** Cùng triết lý xám & phục bút; khác **tán tu + tiêu diêu**, **tạp căn + đa nghề**, ít “một kiếm một môn”; MC **cơ duyên + trí** hơn pedigree môn phái.

## 6. Yêu cầu theo lớp

### Foundation

- [x] `theme-tragedy-architect` — Core `01`
- [x] `world-laws-lore-architect` — Core `02`
- [x] `power-system-economy-architect` — Core `03`
- [ ] **Không sửa Core trừ ticket T0.5 + user** — MC profile work-specific ở Logic/naming, không ghi tên vào Core
- [ ] **Yếu tố mới có tên** (công pháp, phù, pháp bảo…): bổ sung catalog `foundation/resources/` theo [`foundation/resources/README.md`](../../foundation/resources/README.md) § *Promotion từ tác phẩm*
- [ ] Work-specific: phe/địa danh Arc 1 qua `interface/naming/registry.md` + arc outline

### Logic — DoD phase 1

- [x] `arc-planner` → `logic/arcs/00-arc-master-outline.md` — mốc cảnh giới rõ đến Trúc Cơ đỉnh phong; Arc 1 không tam giác sớm
- [x] *(khuyến nghị)* `logic/arcs/01-arc1-beats.md` — 5–10 beat, hook chương 1
- [x] `logic/arcs/02-transition-beats.md` — 6 beat, ch 49–54 (2026-09-08)
- [x] `logic/arcs/02-arc2-beats.md` — 10 beat, ch 55–88 (2026-09-08)
- [x] `logic/arcs/03-arc3-beats.md` — 10 beat, ch 89–112 (2026-09-09) · plan trước prose
- [x] Naming Arc 2 + Transition → `interface/naming/registry.md` (2026-09-08)
- [x] `foreshadowing-architect` → `logic/foreshadowing/00-foreshadow-ledger.md` — plant Arc 1, không payoff twist xa sớm
- [x] Tham chiếu quy mô: `foundation/logic/01-event-scale-system.md`

### Interface — DoD trước chương 1

- [x] `xianxia-naming-specialist` → `interface/naming/registry.md` (MC, địa danh/tông/pháp bảo Arc 1)
- [x] `xianxia-prose-writer` → `interface/chapters/chapter-01-kien-sa.md` — M-Prose-01

## 7. Deliverables & đường dẫn

| Artifact | Path | Owner agent |
| --- | --- | --- |
| Master Brief | `projects/tap-linh-dieu-lo/00-master-brief.md` | requirements-briefer |
| **Progress map** | `projects/tap-linh-dieu-lo/00-progress-map.md` | project-orchestrator / user session |
| Execution plan | `projects/tap-linh-dieu-lo/01-execution-plan.md` | user / orchestrator |
| Story spine | `projects/tap-linh-dieu-lo/logic/00-story-spine.md` | project-orchestrator |
| Chapter spine | `projects/tap-linh-dieu-lo/logic/chapters/00-chapter-spine-phase1.md` | project-orchestrator |
| Mục lục chương | `projects/tap-linh-dieu-lo/interface/chapters/00-index.md` | project-orchestrator |
| Trạng thái | `projects/tap-linh-dieu-lo/status.md` | project-orchestrator |
| Core (shared) | `foundation/core/00–03` | Foundation agents |
| Arc outline | `projects/tap-linh-dieu-lo/logic/arcs/00-arc-master-outline.md` | arc-planner |
| Foreshadow ledger | `projects/tap-linh-dieu-lo/logic/foreshadowing/00-foreshadow-ledger.md` | foreshadowing-architect |
| Tên canon | `projects/tap-linh-dieu-lo/interface/naming/registry.md` | xianxia-naming-specialist |
| Chương | `projects/tap-linh-dieu-lo/interface/chapters/` | xianxia-prose-writer |

## 8. Quyết định đã chốt (phase 1)

| # | Chủ đề | Quyết định |
| --- | --- | --- |
| 1 | Phạm vi arc v1 | Đến **Trúc Cơ kỳ đỉnh phong**; endgame full bộ deferred |
| 2 | Quy mô chương phase 1 | ~80–120 chương; 2.500–4.000 chữ/chương |
| 3 | POV | Third limited MC |
| 4 | vs Tru Tiên | Xám + phục bút giữ; khác tán tu/tạp căn/đa nghề (§5) |
| 5 | MC tên / xuất thân | Xuất thân: vùng linh khí nghèo, tạp Hỏa–Kim–Mộc, bị xếp phế; **tên canon** tại naming (T3) |
| 6 | NC / Hữu tình | **Trì hoãn** Arc 1–đầu Arc 2 |
| 7 | Tên truyện | **Tạp Linh Diêu Lộ** (杂灵遥路) — registry § Tác phẩm |

**Open (không block phase 1):** Quy mô full bộ sau Trúc Cơ; có mở Tiên Giới hay không.

## 9. Giả định đã chốt tạm

- Core tại `foundation/` là Canon cho tác phẩm này đến khi user yêu cầu Foundation pass hoặc tách `projects/tap-linh-dieu-lo/foundation/`.
- Workflow: Brief → Orchestrator → (Foundation nếu T0.5) → Arc → Foreshadow ∥ Naming → Consistency → Prose.
- Tiêu diêu = tư tưởng + ít ràng buộc môn, không nhất thiết vô lễ vô pháp toàn bộ.

## 10. Changelog brief

- **v3 (2026-09-09):** Chốt **tên truyện** *Tạp Linh Diêu Lộ* (杂灵遥路); **slug** `tap-linh-dieu-lo` (đổi từ `tien-hiep-novel`); cập nhật path/reference toàn repo.
- **v2 (2026-09-07):** Chốt phase 1 (Trúc Cơ đỉnh phong, NC trì hoãn, POV, quy mô chương, content bounds, differentiation Tru Tiên); MC contract §2.
- **v1 (2026-09-07):** Khung khởi tạo; chuyển từ `project/` → `projects/tien-hiep-novel/` *(slug cũ)*.
