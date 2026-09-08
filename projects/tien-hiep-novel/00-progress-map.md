# Progress map — Tiên Hiệp Novel

> **Mục đích:** Một file theo dõi **Phase → Arc → Chapter** qua nhiều session.  
> **Cập nhật khi:** xong chương, đổi phase, mở block arc mới, hoặc cuối session.  
> **Chi tiết spine (slug, FS, beat):** [`logic/chapters/00-chapter-spine-phase1.md`](logic/chapters/00-chapter-spine-phase1.md)  
> **Task queue agent:** [`status.md`](status.md)

**Lần cập nhật:** 2026-09-08  
**Session focus:** Transition beat sheet (ch.49–54) · naming Arc 2 · foreshadow ch band · Arc 2 beats synced  
**Brief:** v2 · **Trần phase 1:** Trúc Cơ đỉnh phong

---

## Chú giải trạng thái

| Mức | Giá trị | Nghĩa |
| --- | --- | --- |
| **Phase** | `planned` | Chưa bắt đầu outline chương |
| | `in_progress` | Đang viết / spine active |
| | `complete` | Prose + logic khóa milestone |
| **Arc** | `spine` | Có arc outline + chapter spine (hoặc block) |
| | `prose_partial` | Một phần chương đã có file |
| | `prose_complete` | Toàn bộ dải ch arc đã canon/review |
| | `planned` | Chỉ có tên trên story spine |
| **Chapter** | `block` | Chưa mở từng ch — chỉ block arc |
| | `outline` | Có dòng spine, chưa prose |
| | `draft` | Có file `interface/chapters/` |
| | `review` | Chờ user duyệt |
| | `canon` | Khóa; sửa cần ticket |

---

## Tổng quan (rollup)

| Phase | Trạng thái | Arc | Chương (prose) | Ghi chú |
| --- | --- | --- | --- | --- |
| **1** — Trúc Cơ đỉnh phong | `in_progress` | 4 khối (1+T+2+3) | **44 / 112** prose (**44** approved) | Spine Arc 1 đủ 48 ch |
| **2** — Kim Đan+ | `planned` | — | 0 | Stub sau phase 1 |

---

## Phase 1 — Trúc Cơ đỉnh phong `[in_progress]`

**Logic:** [`logic/00-story-spine.md`](logic/00-story-spine.md) · [`logic/arcs/00-arc-master-outline.md`](logic/arcs/00-arc-master-outline.md)

### Arc 1 — Phế Địa Tán Tu · ch. 1–48 · LK 1→12 `[prose_partial]`

| Metric | Giá trị |
| --- | --- |
| Spine | ✅ 48/48 dòng |
| Prose | **44** approved draft · **4** outline |
| Beat sheet | [`logic/arcs/01-arc1-beats.md`](logic/arcs/01-arc1-beats.md) |

| Ch | Tiêu đề | Status | File |
| --- | --- | --- | --- |
| 01 | Kiến Sa | `approved draft` | [`interface/chapters/chapter-01-kien-sa.md`](interface/chapters/chapter-01-kien-sa.md) |
| 02 | Thuận Thiên Tàn | `approved draft` | [chapter-02-thuan-thien-tan.md](interface/chapters/chapter-02-thuan-thien-tan.md) |
| 03 | Tam Hệ Huyết | `approved draft` | [`interface/chapters/chapter-03-tam-he-huyet.md`](interface/chapters/chapter-03-tam-he-huyet.md) |
| 04 | Phi Vân Tập | `approved draft` | [`interface/chapters/chapter-04-phi-van-tap.md`](interface/chapters/chapter-04-phi-van-tap.md) |
| 05 | Sa Điêu Đổ | `approved draft` | [`interface/chapters/chapter-05-sa-dieu-do.md`](interface/chapters/chapter-05-sa-dieu-do.md) |
| 06 | Bảo Hộ Phí | `approved draft` | [`interface/chapters/chapter-06-bao-ho-phi.md`](interface/chapters/chapter-06-bao-ho-phi.md) |
| 07 | Săn Yêu Hạ | `approved draft` | [`interface/chapters/chapter-07-san-yeu-ha.md`](interface/chapters/chapter-07-san-yeu-ha.md) |
| 08 | Linh Thạch Đếm | `approved draft` | [`interface/chapters/chapter-08-linh-thach-dem.md`](interface/chapters/chapter-08-linh-thach-dem.md) |
| 09 | Ấn Pháp Sơ | `approved draft` | [`interface/chapters/chapter-09-an-phap-so.md`](interface/chapters/chapter-09-an-phap-so.md) |
| 10 | Yêu Đan Đổi | `approved draft` | [`interface/chapters/chapter-10-yeu-dan-doi.md`](interface/chapters/chapter-10-yeu-dan-doi.md) |
| 11 | Hộ Thân Phù | `approved draft` | [`interface/chapters/chapter-11-ho-than-phu.md`](interface/chapters/chapter-11-ho-than-phu.md) |
| 12 | Đa Hành Lệch | `approved draft` | [`interface/chapters/chapter-12-da-hanh-lech.md`](interface/chapters/chapter-12-da-hanh-lech.md) |
| 13 | Thần Thức Mỏi | `approved draft` | [`interface/chapters/chapter-13-than-thuc-moi.md`](interface/chapters/chapter-13-than-thuc-moi.md) |
| 14 | Mảnh Cửu Huyền Trận | `approved draft` | [`interface/chapters/chapter-14-manh-cuu-huyen-tran.md`](interface/chapters/chapter-14-manh-cuu-huyen-tran.md) |
| 15 | Linh Sa Uyên Tin | **approved draft** | [review-chapter-15](interface/chapter-view/review-chapter-15-linh-sa-uyen-tin.md) · suggest_pass |
| 16 | Thanh Sa Giá | **approved draft** | [review-chapter-16](interface/chapter-view/review-chapter-16-thanh-sa-gia.md) · suggest_pass |
| 17 | Hợp Đội Lệnh | **approved draft** | [review-chapter-17](interface/chapter-view/review-chapter-17-hop-doi-lenh.md) · suggest_pass |
| 18 | Phương Ngự Hàn | **approved draft** | [review-chapter-18](interface/chapter-view/review-chapter-18-phuong-ngu-han.md) · suggest_pass |
| 19 | Tọa Độ Mua | **approved draft** | [review-chapter-19](interface/chapter-view/review-chapter-19-toa-do-mua.md) · suggest_pass |
| 20 | Vào Uyên | **approved draft** | [review-chapter-20](interface/chapter-view/review-chapter-20-vao-uyen.md) · suggest_pass |
| 21 | Tranh Suất | **approved draft** | [chapter-21-tran-slot.md](interface/chapters/chapter-21-tran-slot.md) · [review](interface/chapter-view/review-chapter-21-tran-slot.md) |
| 22 | Phong Bộc | **approved draft** | [chapter-22-phong-buoc.md](interface/chapters/chapter-22-phong-buoc.md) · [review](interface/chapter-view/review-chapter-22-phong-buoc.md) |
| 23 | Thanh Phong Liên | **approved draft** | [chapter-23-thanh-phong-lien.md](interface/chapters/chapter-23-thanh-phong-lien.md) · [review](interface/chapter-view/review-chapter-23-thanh-phong-lien.md) |
| 24 | Vòng Vây | **approved draft** | [chapter-24-vong-vay.md](interface/chapters/chapter-24-vong-vay.md) · [review-r2](interface/chapter-view/review-chapter-24-vong-vay-r2.md) |
| 25 | Đảo Kèo | **approved draft** | [chapter-25-dao-keo.md](interface/chapters/chapter-25-dao-keo.md) · [review](interface/chapter-view/review-chapter-25-dao-keo.md) |
| 26 | Mất Tin | **approved draft** | [chapter-26-mat-tin.md](interface/chapters/chapter-26-mat-tin.md) · [review](interface/chapter-view/review-chapter-26-mat-tin.md) |
| 27 | Lượt Chia | **approved draft** | [chapter-27-loot-chia.md](interface/chapters/chapter-27-loot-chia.md) · [review](interface/chapter-view/review-chapter-27-loot-chia.md) |
| 28 | Ra Uyên | **approved draft** | [chapter-28-ra-uyen.md](interface/chapters/chapter-28-ra-uyen.md) · [review](interface/chapter-view/review-chapter-28-ra-uyen.md) |
| 29 | Mồi Yêu | **approved draft** | [chapter-29-moi-yeu.md](interface/chapters/chapter-29-moi-yeu.md) |
| 30 | Cứu Hay Không | **approved draft** | [chapter-30-cuu-hay-khong.md](interface/chapters/chapter-30-cuu-hay-khong.md) · [review](interface/chapter-view/review-chapter-30-cuu-hay-khong.md) |
| 31 | Hữu Tình Giá | **approved draft** | [chapter-31-huu-tinh-gia.md](interface/chapters/chapter-31-huu-tinh-gia.md) · [review](interface/chapter-view/review-chapter-31-huu-tinh-gia.md) |
| 32 | Mất Lối | **approved draft** | [chapter-32-mat-loi.md](interface/chapters/chapter-32-mat-loi.md) · [review](interface/chapter-view/review-chapter-32-mat-loi.md) |
| 33 | Tâm Ma Mầm | **approved draft** | [chapter-33-tam-ma-mam.md](interface/chapters/chapter-33-tam-ma-mam.md) · [review](interface/chapter-view/review-chapter-33-tam-ma-mam.md) |
| 34 | Về Phế Địa | **approved draft** | [chapter-34-ve-phe-dia.md](interface/chapters/chapter-34-ve-phe-dia.md) · [review-r2](interface/chapter-view/review-chapter-34-ve-phe-dia-r2.md) |
| 35 | Tụ Linh Vi Trận | **approved draft** | [chapter-35-tu-linh-vi-tran.md](interface/chapters/chapter-35-tu-linh-vi-tran.md) · [review](interface/chapter-view/review-chapter-35-tu-linh-vi-tran.md) |
| 36 | LK Thất Cửu | **approved draft** | [chapter-36-lk-that-cuu.md](interface/chapters/chapter-36-lk-that-cuu.md) · [review](interface/chapter-view/review-chapter-36-lk-that-cuu.md) |
| 37 | Mạc Lão Mắt | **approved draft** | [chapter-37-mac-lao-mat.md](interface/chapters/chapter-37-mac-lao-mat.md) · [review](interface/chapter-view/review-chapter-37-mac-lao-mat.md) |
| 38 | Nghịch Thiên Mi | **approved draft** | [chapter-38-nghich-thien-mi.md](interface/chapters/chapter-38-nghich-thien-mi.md) · [review-r2](interface/chapter-view/review-chapter-38-nghich-thien-mi-r2.md) |
| 39 | Giá Trị Khai Thác | **approved draft** | [chapter-39-gia-tri-khai-thac.md](interface/chapters/chapter-39-gia-tri-khai-thac.md) · [review](interface/chapter-view/review-chapter-39-gia-tri-khai-thac.md) |
| 40 | Trận Rung | **approved draft** | [chapter-40-tran-rung.md](interface/chapters/chapter-40-tran-rung.md) · [review r2](interface/chapter-view/review-chapter-40-tran-rung-r2.md) |
| 41 | Lớp Dưới | **approved draft** | [chapter-41-lop-duoi.md](interface/chapters/chapter-41-lop-duoi.md) · [review r2](interface/chapter-view/review-chapter-41-lop-duoi-r2.md) |
| 42 | Lệch Khí Ngọc | **approved draft** | [chapter-42-lech-khi-ngoc.md](interface/chapters/chapter-42-lech-khi-ngoc.md) · [review r2](interface/chapter-view/review-chapter-42-lech-khi-ngoc-r2.md) |
| 43 | Khế Chưa Ký | **approved draft** | [chapter-43-khe-chua-ky.md](interface/chapters/chapter-43-khe-chua-ky.md) · [review r2](interface/chapter-view/review-chapter-43-khe-chua-ky-r2.md) |
| 44 | Bán Tin | **approved draft** · Beat 8 đóng | [chapter-44-ban-tin.md](interface/chapters/chapter-44-ban-tin.md) · [review r2](interface/chapter-view/review-chapter-44-ban-tin-r2.md) |
| 45 | Ép Công | `outline` | — |
| 46 | Trận Tàn Một Nhịp | `outline` | — |
| 47 | LK Viên Mãn | `outline` | — |
| 48 | Thạch Lam Ẩn | `outline` | — |

---

### Transition — Thành Trì Khế · ch. 49–54 · LK VM `[spine + beats]`

| Metric | Giá trị |
| --- | --- |
| Beat sheet | ✅ [`logic/arcs/02-transition-beats.md`](logic/arcs/02-transition-beats.md) — 6 beat |
| Spine | ✅ 6/6 dòng outline |
| Prose | 0 |

| Ch | Tiêu đề | Status |
| --- | --- | --- |
| 49 | Cửa Thạch Lam | `outline` |
| 50 | Danh Trên Khế | `outline` |
| 51 | Bách Hóa Đổi | `outline` |
| 52 | Monopoly Đột Phá | `outline` |
| 53 | Hắc Thị Sát Thủ | `outline` |
| 54 | Ký Khế Mạch | `outline` |

---

### Arc 2 — Tranh Mạch Phụ · ch. 55–88 · Trúc Cơ Sơ–Trung `[spine + beats]`

| Metric | Giá trị |
| --- | --- |
| Beat sheet | ✅ [`logic/arcs/02-arc2-beats.md`](logic/arcs/02-arc2-beats.md) — 10 beat |
| Spine | ✅ 34/34 dòng outline (ch.55–88) |
| Prose | 0 |

| Block | Ch | Status | Cốt lõi |
| --- | --- | --- | --- |
| 2A | 55–62 | `outline` | Thuê tranh mạch phụ · Trúc Cơ Sơ |
| 2B | 63–72 | `outline` | Bí cảnh chung; wound đâm · FS-006 |
| 2C | 73–88 | `outline` | Mạch đoạn; Ma lậu; Linh Dịch lệch |

---

### Arc 3 — Đan Điền Viên Mãn · ch. 89–112 · Trúc Cơ Hậu–VM `[spine]`

| Block | Ch | Status | Cốt lõi |
| --- | --- | --- | --- |
| 3A | 89–98 | `block` | Hiệp hội đan |
| 3B | 99–106 | `block` | Ma shortcut vs chậm |
| 3C | 107–112 | `block` | **Kết phase 1** — Viên Mãn |

---

## Phase 2 — Kim Đan+ `[planned]`

| Arc | Status | Ghi chú |
| --- | --- | --- |
| *(chưa đặt tên)* | `planned` | Mở sau brief phase 2 |

---

## Cây tóm tắt (session nhanh)

```
Phase 1 [in_progress]
├── Arc 1 Phế Địa Tán Tu [prose_partial]  ch 1–33 approved draft · 34–48 outline
├── Transition Thành Trì Khế [spine+beats]  ch 49–54 outline
├── Arc 2 Tranh Mạch Phụ [spine+beats]    ch 55–88 outline
└── Arc 3 Đan Điền Viên Mãn [spine]       ch 89–112 block
Phase 2 [planned]
```

---

## Checklist cuối session

- [ ] Cập nhật cột **Status** / **File** cho chương vừa viết
- [ ] Sửa **Session focus** + **Lần cập nhật** ở đầu file
- [ ] Nếu đổi slug/tiêu đề: sync [`logic/chapters/00-chapter-spine-phase1.md`](logic/chapters/00-chapter-spine-phase1.md) + [`interface/chapters/00-index.md`](interface/chapters/00-index.md)
- [ ] (Tùy chọn) một dòng trong [`status.md`](status.md) task queue

---

*Progress map v1 — project-orchestrator — file session chính cho Phase → Arc → Chapter.*
