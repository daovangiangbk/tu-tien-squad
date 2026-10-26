# Archive — tác phẩm tạm dừng / đóng gói

Thư mục này chứa **các work đã archive**: vẫn trong git, **read-only** cho pipeline sáng tác mặc định; không còn làm việc active trừ khi **restore**.

```text
projects/
  active-work.md          ← slug **active** (một dòng); không trỏ vào archive
  README.md               ← bảng tác phẩm **active**
  <work-slug>/            ← đang làm việc
  archive/
    README.md             ← file này + bảng archive
    <work-slug>/          ← cùng cấu trúc như projects/<slug>/
```

**Quy ước slug:** giữ nguyên (`tap-linh-dieu-lo`). **Không** đổi tên slug khi archive.

---

## Khi nào archive

| Tình huống | Gợi ý |
| --- | --- |
| Chuyển focus sang tác phẩm khác lâu dài | Archive work cũ |
| Dự án pilot / one-shot xong, không viết tiếp | Archive |
| Giữ repo gọn `projects/` active | Archive các work “ngủ” |

**Không** archive để “xóa” — archive = **tách lifecycle**, không thay thế git history.

---

## Thủ tục archive (human hoặc agent có quyền git mv)

1. **Chốt snapshot:** cập nhật `projects/<slug>/status.md` — queue rỗng hoặc ghi rõ defer; không để `waiting_subagent` treo.
2. **Đánh dấu lifecycle** — thêm (hoặc cập nhật) block đầu `status.md`:

```markdown
## Project lifecycle

| Trường | Giá trị |
| --- | --- |
| **lifecycle** | `archived` |
| **archived_at** | YYYY-MM-DD |
| **archived_reason** | (một dòng, tùy chọn) |
| **restore_note** | (tùy chọn — điều kiện mở lại) |
```

3. **Di chuyển thư mục:**

```bash
git mv projects/<slug> projects/archive/<slug>
```

4. **Cập nhật registry:**
   - Xóa hoặc chuyển dòng tác phẩm khỏi bảng **active** trong `projects/README.md`.
   - Thêm dòng vào bảng **Archived** dưới đây (slug, tên, ngày, ghi chú ngắn).
5. **`projects/active-work.md`:** nếu đang trỏ `<slug>` → đổi sang slug active khác **hoặc** để trống một dòng + comment `# chưa chọn` (một dòng slug vẫn là quy ước chính).
6. **Commit** (khi user yêu cầu): message kiểu `chore: archive project <slug>`.

**Orchestrator / sub-agent:** sau archive, `work_root` = `projects/archive/<slug>/` **chỉ** khi user **chỉ rõ** slug archived hoặc lệnh read-only / restore. **Không** delegate `T-prose-*`, world geo mới, CP mặc định trên archived work.

---

## Restore (unarchive)

1. `git mv projects/archive/<slug> projects/<slug>`
2. Trong `status.md`: `lifecycle` → `active`; ghi `restored_at`.
3. Thêm lại vào bảng active `projects/README.md`; xóa khỏi bảng Archived dưới đây.
4. Set `active-work.md` nếu user muốn focus lại.
5. Orchestrator có thể tiếp tục pipeline A/B/C như bình thường.

---

## Bảng tác phẩm archived

| Slug | Tên hiển thị | archived_at | Ghi chú |
| --- | --- | --- | --- |
| `tap-linh-dieu-lo` | Tạp Linh Diêu Lộ | 2026-09-18 | Phase 1 complete · adaptation EP-01–15 · Core shared |
| `than-phu` | Thần Phù (Thần Phù) | 2026-09-18 | Phase 1 prose ch.1–110 approved · Core shared |
| `linh-dien` | Linh điền | 2026-10-02 | Arc 1 · 8 ch prose draft v2 · human gate v5 thoại defer |
| `ham-mo` | Hầm mỏ | 2026-10-08 | Truyện ngắn 4 ch · redraft v3 approved_v3 · geo waived |
| `than-khi` | Thần Khí (Thần khí) | 2026-10-23 | Ch.1–34 approved · `T-spine-ch-35` defer · Core shared |

---

## Path cho brief §0 (archived)

Khi đọc-only hoặc restore prep, brief §0 vẫn dùng slug; đường dẫn:

| Biến | Path |
| --- | --- |
| `work_root` | `projects/archive/<slug>/` |
| `logic_root` | `{work_root}/logic/` |
| `interface_root` | `{work_root}/interface/` |

`foundation_root` không đổi (thường `foundation/` shared).
