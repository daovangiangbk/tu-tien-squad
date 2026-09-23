# chapter-view

Review **chỉ liệt kê mục cần sửa** (bảng ngắn + lý do 1 câu), không dump pass checklist.

## Đặt tên

- Prefix bắt buộc: **`review-`**
- Một chương: `review-chapter-NN-<slug>.md`
- Re-review: `review-chapter-NN-<slug>-r2.md`

## Workflow

1. `xianxia-prose-writer` → `../chapters/chapter-NN-*.md`
2. `xianxia-chapter-reviewer` → file `review-...` tại đây
3. **Human** tick ID trong bảng *Human confirm*
4. `project-orchestrator` → `xianxia-prose-writer` **revise**
5. Human **approved** → chương tiếp theo

## Experimental reader

- Prefix: **`reader-`**
- Thư mục: `reader-comment/` (beta read độc giả mới; không trộn với `review-`)
