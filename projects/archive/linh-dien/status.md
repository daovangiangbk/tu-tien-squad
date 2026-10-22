# Project status — Linh điền — cập nhật 2026-10-02

**Work slug:** `linh-dien`  
**Work root:** `projects/archive/linh-dien/` *(sau archive)*  

## Project lifecycle

| Trường | Giá trị |
| --- | --- |
| **lifecycle** | `archived` |
| **archived_at** | 2026-10-02 |
| **archived_reason** | Chuyển focus sang tác phẩm mới; arc 1 prose 8/8 draft v2, human gate v5 thoại chưa tick |
| **restore_note** | Restore nếu muốn tick review / approve arc 1 hoặc viết tiếp |
| **pipeline** | **A** — 1 arc · 8 ch · slice — **paused** (prose draft xong, review chờ human) |
| **foundation_root** | `foundation/` (shared) |

## Snapshot

- **Prose:** **8/8** **draft v2 expanded** (~2.500–2.836 từ/ch, `wc -w`) — [xianxia-prose-writer](dfeeb91b-d9b1-4493-8ede-42aaf6b709cf)
- **Index:** [`interface/chapters/00-index.md`](interface/chapters/00-index.md)
- **Review v1:** [`interface/chapter-view/review-chapter-*.md`](interface/chapter-view/) (trước expand)
- **Review v2:** [`interface/chapter-view/review-chapter-*-v2.md`](interface/chapter-view/) — [xianxia-chapter-reviewer](edd86086-90e4-43e7-94b3-4b24ca1b46dd)
- **Review v5 thoại:** [`interface/chapter-view/review-chapter-*-v5-thoai.md`](interface/chapter-view/) — ch 1–7 suggest_revise · ch 8 suggest_pass

## Task queue — Pipeline A

| Task ID | State | Owner | Output |
| --- | --- | --- | --- |
| **`T-prose-expand`** | **done** | xianxia-prose-writer | 8 ch · draft v2 expanded |
| **`T-prose-expand-cleanup`** | **done** | orchestrator | gỡ lại `Ghi chú sáng tác` · sửa meta/EN ch.8 |
| **`T-review-2`** | **done** | xianxia-chapter-reviewer | 8× `review-*-v2.md` |
| **`T-prose-revise-v2`** | **done** | orchestrator | tick review C-01… theo ch.1–8 |
| **`T-review-v3-van-van`** | **done** | xianxia-chapter-reviewer | 8× `review-*-v3-van-van.md` |
| **`T-prose-van-van`** | **done** | orchestrator | ván/ván tre · ch.4 tre giới · ch.1 mương tưới |
| **`T-review-v4-linh-thua`** | **done** | xianxia-chapter-reviewer | 8× `review-*-v4-linh-thua.md` · quy ước `logic/README.md` |
| **`T-review-v5-thoai`** | **done** | xianxia-chapter-reviewer | 8× `review-*-v5-thoai.md` |
| **`T-prose-revise-v5-thoai`** | **done** | orchestrator | thoại ấm/đủ · ch 1–7 theo bảng v5 |
| **`T-prose-herb-name-cleanup`** | **done** | orchestrator | tên đủ registry · gỡ lặp `Thanh Linh Thảo` · đổi *Thanh niên* → *người trẻ trong ca làm việc* (ch 1–6) |

**Current task:** *(none — archived)* · Human gate v5 thoại defer đến khi restore.

## Milestone

Arc 1 **đủ độ dài brief** · beat spine giữ — chờ review / approve.
