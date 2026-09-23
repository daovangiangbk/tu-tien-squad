# Story spine — Phase 1 (Logic stub)

> **Tác phẩm:** **Thần Phù** (神符) · **Slug:** `than-phu` · **Brief:** v1.1 · **Trần phase 1:** **Trúc Cơ kỳ đỉnh phong**  
> **Neo Foundation:** `foundation/core/01–03` · `foundation/resources/06-phu-luc.md` · `10-phu-nghe-tu-tien` · `foundation/logic/01-event-scale-system.md`

---

## 1. Cốt truyện một câu

**Thẩm Vô Ngọc**, công tử **phế danh** **Thẩm thị · Phù Lĩnh**, sống sót **cửu địch tàn sát** nhờ **hi sinh người thân**, vô tình giữ **Thần Phù Cổ Phổ** — đi **phù sư + tu vi** song hành (`03` §3.5) — từ **Luyện Khí yếu** leo tới **Trúc Cơ đỉnh phong**, trả giá **thần thức · vật liệu · Nghiệp** (Ma phù), điều tra **Hàn Diệp Liên** và tuyến **U Huyết Các** tại **Thanh Phù Thành**, trước khi phase 2 mở **Kim Đan+** (deferred).

---

## 2. Trục phase 1 (không prose)

| Trục | Nội dung |
| --- | --- |
| **Ngoại** | **Phù Lĩnh Lệnh** → **Tây Lam** thoát → **Thanh Phù Thành** (luyện huyết / bắt cóc) → **Phù Viên** giang hồ (Nam hoang) |
| **Nội** | Wound §3.5 *mạng ta mua bằng máu họ* → báo thù vs *chỉ mạnh mới xứng sống* → Hữu tình (cứu trẻ / giữ lời) vs Vô tình (tu nhanh, bỏ điều tra) |
| **Cảnh giới** | LK sơ/yếu → LK trung–hậu → Trúc Cơ sơ → Trúc Cơ trung–**đỉnh phong** |
| **Kinh tế** | Linh điền tộc · phù hộ thân hạ · cống hiến Phù các; thành: hắc thị tin **~20+ hạt**; phù cao = **mực/da hiếm** + hao thần |
| **Theme** | Nghịch Thiên qua phù vs thiên phú kém; Chính–Tà theo **ứng xụ**; **không** heal wound sớm; cửu địch / đầu não **deferred** arc 2+ |

---

## 3. Dòng arc (xương sống đại cục)

```mermaid
flowchart LR
  A1[Arc1_PhuLinhHuyetDa_LK]
  A2[Arc2_ThanhPhuUHuyet_TruCơSo]
  A3[Arc3_PhuGiangBao_TruCơPeak]
  A1 --> A2 --> A3
  STUB[Phase2_KimDan_stub]
  A3 --> STUB
```

| Khối | ID | Tên | Chương ước | Cảnh giới | Cliffhanger ra |
| --- | --- | --- | --- | --- | --- |
| **Arc 1** | `arc-1` | **Phù Lĩnh Huyết Dạ** | **1–35** *(band)* | LK sơ → LK trung | Manh cửu địch + hướng **Thanh Phù**; tin **U Huyết** mầm |
| **Arc 2** | `arc-2` | **Thanh Phù U Huyết** | **36–75** | LK hậu → **Trúc Cơ sơ** | **Thiên Phù/ quan im**; manh thuê ma; rời thành **Nam hoang** (ch.75) → Arc 3 |
| **Arc 3** | `arc-3` | **Phù Giang Báo** | **76–110** *(band)* | Trúc Cơ trung → **đỉnh phong** | Payoff manh **Hàn Diệp** (chưa đầu não); phase 2 stub |

**Tổng phase 1:** ~**96–110** chương (brief **80–120**).

Chi tiết arc: [`arcs/00-arc-master-outline.md`](./arcs/00-arc-master-outline.md).

---

## 4. Chapter spine (điểm neo trước prose)

| Artifact | Path | Mức chi tiết |
| --- | --- | --- |
| **Beat Arc 1** | [`arcs/01-arc1-beats.md`](./arcs/01-arc1-beats.md) | Beat ↔ dải ch *(band)* |
| **Beat Arc 2–3** | [`arcs/02-arc2-beats.md`](./arcs/02-arc2-beats.md) · [`arcs/03-arc3-beats.md`](./arcs/03-arc3-beats.md) · [`chapters/00-chapter-spine-phase1.md`](./chapters/00-chapter-spine-phase1.md) | Arc 2 **36–75 approved** · Arc 3 ch.103–110 **approved** (finale P1) |
| **Mục lục Interface** | [`../interface/chapters/00-index.md`](../interface/chapters/00-index.md) | Arc 1 ch.1–35 · Arc 2 ch.36–75 **approved** |

**Trạng thái chương (spine):**

| Status | Nghĩa |
| --- | --- |
| `outline` | Có dòng spine; chưa prose |
| `draft` | Có file `.md` trong `interface/chapters/` |
| `review` | User/orchestrator duyệt |
| `canon` | Khóa; đổi Logic cần ticket |

---

## 5. Thứ tự công việc (orchestrator)

1. Chốt story spine + arc master (artifact này + `00-arc-master-outline.md`).
2. **`foreshadowing-architect`** — ledger FS khớp beat Arc 1.
3. Beat Arc 2–3 khi Arc 1 prose tiến.
4. **`world-builder`** — cập nhật placeholder địa danh trong `01-region-active.md` nếu cần.
5. Prose sau beat + naming registry.

---

## 6. Phase 2+ (stub)

Kim Đan → phi thăng → đại kết báo thù / Nhân-Quả — **không** outline chương tới brief phase 2.

---

*Logic — arc-planner — 2026-09-17.*
