# Progress map — Tạp Linh Diêu Lộ

> **Mục đích:** Một file theo dõi **Phase → Arc → Chapter** qua nhiều session.  
> **Cập nhật khi:** xong chương, đổi phase, mở block arc mới, hoặc cuối session.  
> **Chi tiết spine (slug, FS, beat):** [`logic/chapters/00-chapter-spine-phase1.md`](logic/chapters/00-chapter-spine-phase1.md)  
> **Task queue agent:** [`status.md`](status.md)

**Lần cập nhật:** 2026-09-10  
**Session focus:** **REWRITE-66-112 complete** — ch.66–112 rewrite approved · Phase 1 khép · Phase 2 stub
**Tác phẩm:** Tạp Linh Diêu Lộ (杂灵遥路) · **Brief:** v3 · **Trần phase 1:** Trúc Cơ đỉnh phong

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
| **1** — Trúc Cơ đỉnh phong | `complete` | 4 khối (1+T+2+3) | **112 / 112** approved draft | Arc 3 **prose_complete** · ch.112 Trúc Cơ ĐVM + đèn |
| **2** — Kim Đan+ | `planned` | — | 0 | Stub sau phase 1 |

---

## Phase 1 — Trúc Cơ đỉnh phong `[complete]`

**Logic:** [`logic/00-story-spine.md`](logic/00-story-spine.md) · [`logic/arcs/00-arc-master-outline.md`](logic/arcs/00-arc-master-outline.md)

### Arc 1 — Phế Địa Tán Tu · ch. 1–48 · LK 1→12 `[prose_complete]`

| Metric | Giá trị |
| --- | --- |
| Spine | ✅ 48/48 dòng |
| Prose | **48** approved draft · Arc 1 **prose_complete** |
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
| 45 | Ép Công | **approved draft** · Beat 9 mở | [chapter-45-ep-cong.md](interface/chapters/chapter-45-ep-cong.md) · [review r2](interface/chapter-view/review-chapter-45-ep-cong-r2.md) |
| 46 | Trận Tàn Một Nhịp | **approved draft** | [chapter-46-tran-tan-mot-nhip.md](interface/chapters/chapter-46-tran-tan-mot-nhip.md) · [review r2](interface/chapter-view/review-chapter-46-tran-tan-mot-nhip-r2.md) |
| 47 | LK Viên Mãn | **approved draft** · Beat 9 đóng | [chapter-47-lk-vien-man.md](interface/chapters/chapter-47-lk-vien-man.md) · [review r2](interface/chapter-view/review-chapter-47-lk-vien-man-r2.md) |
| 48 | Thạch Lam Ẩn | **approved draft** · Beat 10 đóng · **Arc 1 đóng** | [chapter-48-thach-lam-an.md](interface/chapters/chapter-48-thach-lam-an.md) · [review r2](interface/chapter-view/review-chapter-48-thach-lam-an-r2.md) |

---

### Transition — Thành Trì Khế · ch. 49–54 · LK VM `[prose_complete approved draft]`

| Metric | Giá trị |
| --- | --- |
| Beat sheet | ✅ [`logic/arcs/02-transition-beats.md`](logic/arcs/02-transition-beats.md) — 6 beat |
| Spine | ✅ 6/6 dòng outline |
| Prose | **6 / 6** draft |

| Ch | Tiêu đề | Status | File |
| --- | --- | --- | --- |
| 49 | Cửa Thạch Lam | `approved draft` | [chapter-49-cua-thach-lam.md](interface/chapters/chapter-49-cua-thach-lam.md) |
| 50 | Danh Trên Khế | `approved draft` | [chapter-50-dan-tren-khe.md](interface/chapters/chapter-50-dan-tren-khe.md) |
| 51 | Bách Hóa Đổi | `approved draft` | [chapter-51-bach-hoa-doi.md](interface/chapters/chapter-51-bach-hoa-doi.md) |
| 52 | Độc Quyền Đột Phá | `approved draft` | [chapter-52-monopoly-dot-pha.md](interface/chapters/chapter-52-monopoly-dot-pha.md) |
| 53 | Hắc Thị Sát Thủ | `approved draft` | [chapter-53-hac-thi-sat-thu.md](interface/chapters/chapter-53-hac-thi-sat-thu.md) |
| 54 | Ký Khế Mạch | `approved draft` | [chapter-54-ky-khe-mach.md](interface/chapters/chapter-54-ky-khe-mach.md) |

---

### Arc 2 — Tranh Mạch Phụ · ch. 55–88 · Trúc Cơ Sơ–Trung `[spine + beats]`

| Metric | Giá trị |
| --- | --- |
| Beat sheet | ✅ [`logic/arcs/02-arc2-beats.md`](logic/arcs/02-arc2-beats.md) — 10 beat |
| Spine | ✅ 34/34 dòng outline (ch.55–88) |
| Prose | **30** (ch.55–84) |

| Ch | Tiêu đề | Status | File |
| --- | --- | --- | --- |
| 55 | Khế Thuê Mạch | `approved draft` | [chapter-55-khe-thue-mach.md](interface/chapters/chapter-55-khe-thue-mach.md) |
| 56 | Đan Sa Phụ | `approved draft` | [chapter-56-dan-sa-phu.md](interface/chapters/chapter-56-dan-sa-phu.md) |
| 57 | Luật Đại Cục | `approved draft` | [chapter-57-luat-dai-cuc.md](interface/chapters/chapter-57-luat-dai-cuc.md) |
| 58 | Trúc Cơ Đan | `approved draft` | [chapter-58-tru-co-dan.md](interface/chapters/chapter-58-tru-co-dan.md) |
| 59 | Mảnh Ghép | `approved draft` | [chapter-59-manh-ghep.md](interface/chapters/chapter-59-manh-ghep.md) |
| 60 | Tranh Suất Mạch | `approved draft` | [chapter-60-tran-slot-mach.md](interface/chapters/chapter-60-tran-slot-mach.md) |
| 61 | Ép Đột Phá | `approved draft` | [chapter-61-ep-dot-pha.md](interface/chapters/chapter-61-ep-dot-pha.md) |
| 62 | Trúc Cơ Sơ | `approved draft` | [chapter-62-tru-co-so.md](interface/chapters/chapter-62-tru-co-so.md) |
| 63 | Vé Bí Cảnh | `approved draft` | [chapter-63-ve-bi-canh.md](interface/chapters/chapter-63-ve-bi-canh.md) |
| 64 | Phong Ấn Tin | `approved draft` | [chapter-64-phong-an-tin.md](interface/chapters/chapter-64-phong-an-tin.md) |
| 65 | Độc Quyền Vé | `approved draft` | [chapter-65-monopoly-ve.md](interface/chapters/chapter-65-monopoly-ve.md) |
| 66 | Hai Cuộc | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-66-hai-cuoc.md](interface/chapters/chapter-66-hai-cuoc.md) |
| 67 | Sát Thủ Phí | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-67-sat-thu-phi.md](interface/chapters/chapter-67-sat-thu-phi.md) |
| 68 | Khách Thuê | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-68-khach-thue.md](interface/chapters/chapter-68-khach-thue.md) |
| 69 | Hợp Đồng Cắn | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-69-hop-dong-can.md](interface/chapters/chapter-69-hop-dong-can.md) |
| 70 | Giữ Suất | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-70-giu-slot.md](interface/chapters/chapter-70-giu-slot.md) |
| 71 | Vì Đại Cục | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-71-vi-dai-cuc.md](interface/chapters/chapter-71-vi-dai-cuc.md) |
| 72 | Bia Không Tên | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-72-bia-khong-ten.md](interface/chapters/chapter-72-bia-khong-ten.md) |
| 73 | Hỗn Loạn | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-73-hon-loan.md](interface/chapters/chapter-73-hon-loan.md) |
| 74 | Ổn Trung | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-74-on-trung.md](interface/chapters/chapter-74-on-trung.md) |
| 75 | Tạ Hàm Nguyệt | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-75-ta-ham-nguyet.md](interface/chapters/chapter-75-ta-ham-nguyet.md) |
| 76 | Phương Tin | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-76-phuong-tin.md](interface/chapters/chapter-76-phuong-tin.md) |
| 77 | Mạch Đoạn | `rewrite approved` | [chapter-77-mach-doan.md](interface/chapters/chapter-77-mach-doan.md) · [review r2](interface/chapter-view/review-chapter-77-mach-doan-r2.md) · REWRITE-66-112 |
| 78 | Khí Sụt | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-78-khi-sut.md](interface/chapters/chapter-78-khi-sut.md) · [review r2](interface/chapter-view/review-chapter-78-khi-sut-r2.md) |
| 79 | Phế Địa Mới | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-79-phe-dia-moi.md](interface/chapters/chapter-79-phe-dia-moi.md) |
| 80 | Nhân Quả Vùng | **rewrite approved** · Beat 7 đóng | [chapter-80-nhan-qua-vung.md](interface/chapters/chapter-80-nhan-qua-vung.md) · [review r2](interface/chapter-view/review-chapter-80-nhan-qua-vung-r2.md) |
| 81 | Huyết Sa | `rewrite approved` (REWRITE-66-112 · r2 pass · Beat 8 mở) | [chapter-81-huyet-sa.md](interface/chapters/chapter-81-huyet-sa.md) |
| 82 | Hút Linh | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-82-hut-linh.md](interface/chapters/chapter-82-hut-linh.md) · [review r2](interface/chapter-view/review-chapter-82-hut-linh-r2.md) |
| 83 | Đường Tắt Ma | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-83-shortcut-ma.md](interface/chapters/chapter-83-shortcut-ma.md) |
| 84 | Cứu Vùng | `rewrite approved` (REWRITE-66-112 · r2 pass · Beat 8 đóng · ~1.9k từ) | [chapter-84-cuu-vung.md](interface/chapters/chapter-84-cuu-vung.md) |
| 85 | Linh Dịch Lệch | `rewrite approved` (REWRITE-66-112 · r2 pass · Beat 9 mở · ~2.47k từ) | [chapter-85-linh-dich-lech.md](interface/chapters/chapter-85-linh-dich-lech.md) |
| 86 | Tâm Ma Nhẹ | `rewrite approved` (REWRITE-66-112 · r2 pass) | [chapter-86-tam-ma-nhe.md](interface/chapters/chapter-86-tam-ma-nhe.md) |
| 87 | Hao Thần | **rewrite approved** · Beat 9 khép · REWRITE-66-112 | [chapter-87-hao-than.md](interface/chapters/chapter-87-hao-than.md) · [review r2](interface/chapter-view/review-chapter-87-hao-than-r2.md) |
| 88 | Cần Đan Sư | **REWRITE approved** · Beat 10 / Arc 2 prose khép | [chapter-88-can-dan-su.md](interface/chapters/chapter-88-can-dan-su.md) · [review r2](interface/chapter-view/review-chapter-88-can-dan-su-r2.md) |

| Block | Ch | Status | Cốt lõi |
| --- | --- | --- | --- |
| 2A | 55–62 | **approved draft** · Beat 2 khép | Thuê tranh mạch phụ · Trúc Cơ Sơ |
| 2B | 63–72 | ch.66–72 **rewrite approved** · ch.63–65 approved draft · Beat 5 khép | Bí cảnh chung; vé; Sát Thủ; wound đâm — Lục chết |
| 2C | 73–88 | ch.73–88 **rewrite approved** (REWRITE-66-112) · Beat 6–10 khép | Trung lệch; Ma lậu; Linh Dịch; Thạch Lam cliff |

---

### Arc 3 — Đan Điền Viên Mãn · ch. 89–112 · Trúc Cơ Hậu–VM `[prose_complete]`

| Metric | Giá trị |
| --- | --- |
| Beat sheet | ✅ [`logic/arcs/03-arc3-beats.md`](logic/arcs/03-arc3-beats.md) (10 beat) |
| Spine | ✅ 24/24 dòng outline (ch.89–112) — [`00-chapter-spine-phase1.md`](logic/chapters/00-chapter-spine-phase1.md) |
| Prose | **24/24** rewrite approved (ch.89–112) · ch.112 full rewrite r2 pass |

| Block | Ch | Status | Cốt lõi |
| --- | --- | --- | --- |
| 3A | 89–98 | ch.89–98 **rewrite approved** (Beat 1–4 khép) | Cửa hội đan · gian lận điểm · lậu phương · Trúc Cơ Hậu · một tầng ổn |
| 3B | 99–106 | ch.99–106 **rewrite approved** (Beat 7 khép · block 3B khép) | Nội bộ hội · phế địa III · Sa/shortcut echo |
| 3C | 107–112 | ch.107–**112** **rewrite approved** (Beat 10 khép · **REWRITE-66-112** done) | Trúc Cơ ĐVM · **FS-008** đèn plant · Thiên Sa treo · Phase 1 khép → Phase 2 stub |

---

## Phase 2 — Kim Đan+ `[planned]`

| Arc | Status | Ghi chú |
| --- | --- | --- |
| *(chưa đặt tên)* | `planned` | Mở sau brief phase 2 |

---

## Cây tóm tắt (session nhanh)

```
Phase 1 [in_progress]
├── Arc 1 Phế Địa Tán Tu [prose_complete]  ch 1–48 approved draft
├── Transition Thành Trì Khế [approved draft]   ch 49–54 prose
├── Arc 2 Tranh Mạch Phụ [prose_complete] ch 55–88 approved draft · Beat 10 khép · gate ch.89
└── Arc 3 Đan Điền Viên Mãn [prose_complete]  ch 89–112 approved draft
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
