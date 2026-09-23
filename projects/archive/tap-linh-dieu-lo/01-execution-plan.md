# Kế hoạch thực thi — Tạp Linh Diêu Lộ (review trước, làm lần lượt)

**Trạng thái:** Đang thực thi theo wave (bản lưu tại work root).  
**Work slug:** [`tap-linh-dieu-lo`](./)  
**Pointer:** [`projects/active-work.md`](../active-work.md)  
**Brief:** [`00-master-brief.md`](./00-master-brief.md)  
**Status queue:** [`status.md`](./status.md)  
**Shared Foundation:** [`foundation/core/`](../../foundation/core/) (01–03 + glossary), [`foundation/logic/01-event-scale-system.md`](../../foundation/logic/01-event-scale-system.md)

---

## Bối cảnh hiện tại

| Lớp | Đã có | Chưa có |
| --- | --- | --- |
| **Foundation (shared)** | Core theme/world/power, glossary, event-scale, resources 01–11 | Work-specific MC canon trong Core (đúng quy ước — tên ở Interface) |
| **Logic (work)** | Tham chiếu event-scale trong brief | `logic/arcs/`, `logic/foreshadowing/` |
| **Interface (work)** | — | `interface/naming/registry.md`, `interface/chapters/` |

**Khớp raw intent với Core:** MC archetype `foundation/core/01-theme-tragedy-core.md` §3.1 + user intent (tán tu, tiêu diêu, tạp Hỏa–Kim–Mộc, Thể–Linh–Thần, đa nghề, hành vi chính nghĩa ≠ phe).

---

## Quyết định đã chốt (phase 1)

1. **Phạm vi arc (giai đoạn 1):** Đại cục **tạm thời đến Trúc Cơ kỳ đỉnh phong** — endgame dài hạn mở rộng sau.
2. **Hữu tình / NC:** **Trì hoãn** — Arc 1 (và ưu tiên đầu Arc 2) tập trung tán tu, kinh tế, bí cảnh, cơ duyên.

---

## Lộ trình theo wave

| Wave | Agent | Output |
| --- | --- | --- |
| **W0** | `requirements-briefer` | `00-master-brief.md` v2 |
| **W0.5** | Foundation architects *(tùy chọn)* | Patch `foundation/core/` — mặc định bỏ qua |
| **W1** | `arc-planner` | `logic/arcs/00-arc-master-outline.md` |
| **W2** | `foreshadowing-architect` ∥ `xianxia-naming-specialist` | ledger + `interface/naming/registry.md` |
| **W2.5** | `project-orchestrator` | `status.md`, conflict tickets |
| **W3** | `xianxia-prose-writer` | `interface/chapters/chapter-01-*.md` |

**Thứ tự cứng:** W0 → (W0.5?) → W1 → (T2 ∥ T3) → W2.5 → W3.

---

## Task queue

| ID | Mô tả | Phụ thuộc |
| --- | --- | --- |
| **T0** | Brief v2 | — |
| **T0.5** | Foundation delta | T0 |
| **T1** | Arc master → Trúc Cơ đỉnh phong | T0 |
| **T1b** | Beat sheet Arc 1 | T1 |
| **T2** | FS ledger | T1 |
| **T3** | Naming registry | T0, T1 |
| **T5** | Consistency | T1–T3 |
| **T4** | Chương 1 | T2, T3, T5 |

---

## Definition of Done — M-Prose-01

| Milestone | Tiêu chí |
| --- | --- |
| **M-Brief** | v2 + changelog; không DECISION NEEDED bắt buộc phase 1 |
| **M-Arc** | Outline tới Trúc Cơ đỉnh phong; Arc 1 beats + hook |
| **M-FS** | Ledger Arc 1 plants |
| **M-Naming** | Registry Arc 1 |
| **M-Consistency** | Không conflict P0 Core 02–03 |
| **M-Chương-1** | POV, tone, FS planted, cliffhanger |

---

## Rủi ro

1. Đa nghề power creep → T5.
2. Tiêu diêu mơ hồ → Arc 1 cần xung đột tài nguyên/ân oán cụ thể.
3. Tạp căn Hỏa–Kim–Mộc → map từ resources, không sửa Core im lặng.
4. Không ghi arc/FS vào shared `foundation/` (trừ event-scale).
5. Sync `status.md` sau mỗi wave.

---

## Tóm tắt điều phối

| Ưu tiên | Hành động |
| --- | --- |
| 1 | W0 — brief v2 |
| 2 | W1 — arc outline |
| 3 | W2 + W2.5 — ledger, naming, consistency |
| 4 | W3 — chương 1 |

Foundation shared **đủ** cho phase 1; **T0.5** chỉ khi brief đòi thay Canon shared.
