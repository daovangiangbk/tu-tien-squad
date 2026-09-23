# Project status — Hầm mỏ — cập nhật 2026-09-22 (redraft v3)

**Work slug:** `ham-mo`  
**Work root:** `projects/ham-mo/`  

## Project lifecycle

| Trường | Giá trị |
| --- | --- |
| **lifecycle** | `active` |
| **pipeline** | **A** — sáng tác **truyện ngắn** — **`in_progress`** (campaign **`T-story-redraft-v3`**) |
| **foundation_root** | `foundation/` (shared) |

**Note:** Brief **v2.1** — 4 chương, vô danh, vô căn thuần → khai sau sập; kết **tia sáng** miệng hầm. **Prior pipeline A** (prose revamp 4/4) **superseded** bởi redraft v3 — prose cũ giữ file, **stale** cho plot/agency.

## User feedback (2026-09-22) — verbatim

**Điểm mạnh (giữ):**

- Lột tả khắc nghiệt phàm nhân sống gần tu sĩ; mặt tối giới tu — coi mạng người như cỏ rác.

**Điểm yếu (phải sửa trong draft mới):**

1. **MC thiếu khát vọng sinh tồn** — bình thường lẫn biến cố: gần như chỉ than thở, chịu đựng; không thể hiện **ý chí làm điều gì cụ thể** (mục tiêu hành động, kế hoạch nhỏ, lựa chọn có stakes).
2. **Biến cố (đặc biệt sập hầm / thoát khe) thiếu kịch tính** — MC "chỉ bò"; mô tả cơ thể/địa hình **không thay đổi tình thế** hay hành động MC (ví dụ máu trơn đá chỉ làm bò dễ hơn — cảm giác vô hại, không leo stakes).

**User request:** «Draft lại toàn bộ câu chuyện» — 4 chương ngắn, scope brief v2.1.

**Logic map:** [`logic/00-redraft-v3-user-feedback-map.md`](logic/00-redraft-v3-user-feedback-map.md)

## Snapshot

- **Format:** 1 arc · **4 chương** — prose **v3 draft 4/4** (chờ batch review)
- **MC:** vô danh · wound giữ · **cần agency beats** mỗi ch
- **Geo:** `T-world-geo-stack` **waived**
- **Prose (baseline cũ):** ~**12.244** từ — **không** coi là approved cho redraft v3

## Campaign gate

| Cờ | Giá trị |
| --- | --- |
| **Campaign** | **`T-story-redraft-v3`** |
| **Campaign gate** | **`standard`** *(redraft)* — review → **`awaiting_human_confirm`** trước revise/approved; **không** auto APPROVE ALL cho pass mới |
| **Prior gate** | `APPROVE ALL` (revamp) — **closed** |

## Human gate

- **Bật lại** cho chuỗi redraft v3 (confirm review ID trước revise) — trừ user đổi cờ trong status.

## Chapter gates (Pipeline A) — redraft v3

| Ch | Trạng thái v3 | Ghi chú |
| --- | --- | --- |
| 1 Ca đá | **approved_v3** | review pass — không revise bắt buộc |
| 2 Hạ hầm | **approved_v3** | review pass — không revise bắt buộc |
| 3 Khe tối | **approved_v3** | Revise must-fix done (2026-09-23) |
| 4 Miệng hầm | **approved_v3** | Revise must-fix done (2026-09-23) |

## Task queue — campaign `T-story-redraft-v3`

| Task ID | State | Owner | Output |
| --- | --- | --- | --- |
| **`T-redraft-v3-spine`** | **done** | arc-planner | `logic/00-story-spine.md` · `logic/chapters/00-chapter-spine-ham-mo.md` · `logic/characters/00-mc-profile.md` §13 |
| `T-redraft-v3-mc-agency` | **waived** | — | Gộp vào spine + profile §13 |
| **`T-prose-v3-1`** | **done** | xianxia-prose-writer | `chapter-01-ca-da.md` · `notes-revamp-prose-v3-ch01.md` · ~**2.904** từ prose |
| **`T-prose-v3-2`** | **done** | xianxia-prose-writer | `chapter-02-ha-ham.md` · `notes-revamp-prose-v3-ch02.md` · ~**2.899** từ prose |
| **`T-prose-v3-3`** | **done** | xianxia-prose-writer | `chapter-03-khe-toi.md` · `notes-revamp-prose-v3-ch03.md` · ~**2.809** từ prose |
| **`T-prose-v3-4`** | **done** | xianxia-prose-writer | `chapter-04-mieng-ham.md` · `notes-revamp-prose-v3-ch04.md` · ~**2.750** từ prose |
| **`T-review-v3-1..4`** | **done** | xianxia-chapter-reviewer | `review-chapter-0N-*-v3.md` (2026-09-22) |
| **`T-revise-v3-3..4`** | **done** | agent (human confirm revise) | C-01–C-04 ch.3 · C-01–C-03 ch.4 (2026-09-23) |
| **`T-revise-v3-1..2`** | **waived** | — | pass — không revise bắt buộc |

**Review v3 summary (2026-09-22):** pass ch.1–2 · suggest_revise ch.3–4 (tiếng Anh meta trong prose + typo ch.3). **Must-fix tổng: 7** (ch.3: 4 · ch.4: 3).

**Campaign prose v3:** **4/4 complete** · review **4/4 complete**

**Current task:** *(none)* — redraft v3 **4/4 approved** (prose + review + revise must-fix)

**Pipeline A:** campaign `T-story-redraft-v3` có thể đánh **`complete`** khi user chốt publish.

### CP / Foundation

- **Không CP** — feedback thuộc Logic/instantiate brief §5 wound + sinh tồn; Core giữ nguyên.

## Task queue (archive — revamp pass · đã đóng)

| Task ID | State | Owner | Output |
| --- | --- | --- | --- |
| `T-brief-init` · `T-brief-decisions` | **done** | briefer / user | `00-master-brief.md` v2.1 |
| `T-theme-mc` | **done** | character-architect | `logic/characters/` |
| `T-micro-world` | **done** | world-builder | `logic/world/00-micro-mo-setting.md` |
| `T-spine-short` | **done** | arc-planner | spine 4 ch |
| `T-naming` | **done** | naming | `interface/naming/registry.md` |
| `T-prose-1..4` | **approved** | prose-writer | `interface/chapters/chapter-0N-*.md` |
| `T-review-1..4` | **done** | chapter-reviewer | `interface/chapter-view/review-chapter-0N-*.md` |
| `T-revise-1..4` | **done** | prose-writer | (ch.1 có `notes-chapter-01-ca-da.md`) |

### Prose revamp pass (2026-09-22)

**Intent:** Holistic **văn phong** (rule mới `xianxia-prose-style.mdc`) — không chỉ patch r3; **giữ** plot beats, FS, cliffhanger, metadata, ~3k/ch (±10%).

**Deliverable:** rewrite-in-place `interface/chapters/chapter-0N-*.md` (cùng title/slug); optional `interface/chapter-view/notes-revamp-prose-chNN.md`.

**Thứ tự:** tuần tự ch.1→4 — **một** chương / lượt delegate.

| Task ID | State | Owner | Output |
| --- | --- | --- | --- |
| `T-revamp-prose-1` | **done** | prose-writer | `chapter-01-ca-da.md` · `notes-revamp-prose-ch01.md` · ~**3.150** từ prose |
| `T-revamp-prose-2` | **done** | prose-writer | `chapter-02-ha-ham.md` · `notes-revamp-prose-ch02.md` · ~**3.108** từ prose |
| `T-revamp-prose-3` | **done** | prose-writer | `chapter-03-khe-toi.md` · `notes-revamp-prose-ch03.md` · ~**2.949** từ prose |
| `T-revamp-prose-4` | **done** | prose-writer | `chapter-04-mieng-ham.md` · `notes-revamp-prose-ch04.md` · ~**3.037** từ prose |
| `T-review-r4-1..4` | **backlog** | chapter-reviewer | *(optional — không auto)* |

**Campaign:** **Prose revamp pass — complete** (2026-09-22) · 4/4 chương

**Current task:** *(none)*

**Prior:** **T-revise-r3-1..4** done · notes: `interface/chapter-view/notes-revise-r3-summary.md`

**Human gate r2:** confirm ID must-fix → `T-revise-r2-*` (writer) — **giữ backlog** trong lúc r3 chạy; **cổng ngôn ngữ/văn phong** ưu tiên kết luận **r3** (rule mới `.cursor/rules/xianxia-prose-style.mdc` + alias `xianxia-prose-language.mdc`). Revise thực thi sau r3: queue `T-revise-r3-*` (human/orchestrator), **không** auto-revise từ r3 dù campaign `APPROVE ALL`.

### Quality pass r2 — prose-language (2026-09-22)

| Ch | Gợi ý | Major | Minor | Review |
| --- | --- | --- | --- | --- |
| 1 Ca đá | suggest_revise | 1 | 0 | `interface/chapter-view/review-chapter-01-ca-da-r2.md` |
| 2 Hạ hầm | **pass** | 0 | 0 | `interface/chapter-view/review-chapter-02-ha-ham-r2.md` |
| 3 Khe tối | suggest_revise | 1 | 0 | `interface/chapter-view/review-chapter-03-khe-toi-r2.md` |
| 4 Miệng hầm | suggest_revise | 2 | 1 | `interface/chapter-view/review-chapter-04-mieng-ham-r2.md` |

**Tổng must-fix:** major **4** · minor **1** · pass thuần: **ch.2**.

| Task ID | State | Owner | Output |
| --- | --- | --- | --- |
| `T-review-r2-1` | **done** | chapter-reviewer | `review-chapter-01-ca-da-r2.md` |
| `T-review-r2-2` | **done** | chapter-reviewer | `review-chapter-02-ha-ham-r2.md` |
| `T-review-r2-3` | **done** | chapter-reviewer | `review-chapter-03-khe-toi-r2.md` |
| `T-review-r2-4` | **done** | chapter-reviewer | `review-chapter-04-mieng-ham-r2.md` |
| `T-revise-r2-*` | **backlog** | prose-writer | *(chờ human tick ID; superseded for style gate bởi r3)* |

### Quality pass r3 — prose-style/language (2026-09-22)

**Neo rule:** `.cursor/rules/xianxia-prose-style.mdc` (canonical) · `.cursor/rules/xianxia-prose-language.mdc` (alias) · `.cursor/rules/xianxia-vietnamese-language.mdc` · agent `.cursor/agents/xianxia-chapter-reviewer.md`

**Output naming:** `interface/chapter-view/review-chapter-0N-<slug>-r3.md` (tuần tự ch.1→4, **không** song song).

**Campaign `APPROVE ALL`:** r3 = **read-only review** only — **không** auto-revise / auto-approved từ file r3; sau khi r3 xong (và human tick ID nếu cần) orchestrator queue `T-revise-r3-1..4` → writer.

| Ch | Gợi ý | Major | Minor | Review |
| --- | --- | --- | --- | --- |
| 1 Ca đá | suggest_revise | 3 | 0 | `interface/chapter-view/review-chapter-01-ca-da-r3.md` |
| 2 Hạ hầm | suggest_revise | 1 | 1 | `interface/chapter-view/review-chapter-02-ha-ham-r3.md` |
| 3 Khe tối | suggest_revise | 2 | 0 | `interface/chapter-view/review-chapter-03-khe-toi-r3.md` |
| 4 Miệng hầm | suggest_revise | 4 | 1 | `interface/chapter-view/review-chapter-04-mieng-ham-r3.md` |

**Tổng must-fix r3:** major **10** · minor **2** · `suggest_pass` thuần: **0/4** · **Review phase: complete**.

| Task ID | State | Owner | Output |
| --- | --- | --- | --- |
| `T-review-r3-1` | **done** | chapter-reviewer | `review-chapter-01-ca-da-r3.md` · suggest_revise · major **3** |
| `T-review-r3-2` | **done** | chapter-reviewer | `review-chapter-02-ha-ham-r3.md` · suggest_revise · major **1** · minor **1** |
| `T-review-r3-3` | **done** | chapter-reviewer | `review-chapter-03-khe-toi-r3.md` · suggest_revise · major **2** |
| `T-review-r3-4` | **done** | chapter-reviewer | `review-chapter-04-mieng-ham-r3.md` · suggest_revise · major **4** · minor **1** |
| `T-revise-r3-1` | **done** | prose-writer | `chapter-01-ca-da.md` · C-01–C-03 |
| `T-revise-r3-2` | **done** | prose-writer | `chapter-02-ha-ham.md` · C-01–C-02 |
| `T-revise-r3-3` | **done** | prose-writer | `chapter-03-khe-toi.md` · C-01–C-02 |
| `T-revise-r3-4` | **done** | prose-writer | `chapter-04-mieng-ham.md` · C-01–C-05 |

**Waived:** full multi-arc foreshadow, `T-world-geo-stack`.
