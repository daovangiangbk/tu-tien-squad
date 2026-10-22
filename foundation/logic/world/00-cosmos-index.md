# Cosmos Index — Foundation Canon (`foundation-canon`)

> **Luật nền đọc trước:** [`laws/00-index.md`](laws/00-index.md) · **Cấu trúc không gian:** [`history/tier-00/00a-phu-luc-cau-truc-khong-gian-ban-co.md`](history/tier-00/00a-phu-luc-cau-truc-khong-gian-ban-co.md).
>
> **Mô hình:** Bốn **giới diện vật chất song song trong Nhân Giới thuộc Không gian Bàn Cổ**: Phàm · Linh · Tiên · Thần. Giới bích nội tầng tách từng giới diện; **Vực Ngoại** là vùng rìa nội giới, còn ngoài **Giới Tường** mới là Hỗn Độn.

**work_slug GeoJSON:** `foundation-canon` · Convention: [`../00-geojson-world-map-convention.md`](../00-geojson-world-map-convention.md) · **Kiến trúc object:** [`01-world-object-architecture.md`](01-world-object-architecture.md) · **Mẫu:** [`_templates/object/`](_templates/object/README.md)

**Tracker:** [`status.md`](status.md)

**Chính sách hồ sơ:** Phàm Giới chỉ có **Bích Lạc Tinh**, Linh Giới chỉ có **Càn Nguyên Tinh** là planet active được mô tả sâu. Tiên Giới và Thần Giới dùng system-first; planet và châu lục chỉ sinh khi arc kích hoạt. Toàn bộ atlas, GeoJSON, PNG và canvas hiện hữu được giữ nguyên làm lớp tương thích.

---

## 1. Bốn giới diện vật chất chính

| Giới | Hán Việt | Năng lượng đặc trưng | Tinh hà (kế hoạch) | Atlas |
| --- | --- | --- | --- | --- |
| **Phàm Giới** | 凡界 | Linh khí cực mỏng / vô linh | **1 planet active:** [Bích Lạc Tinh](realms/pham-gioi/planets/bich-lac-tinh/00-overview.md); `TH-PHAM-BICH-LAC` là parent map legacy | [`realms/pham-gioi/00-world-atlas.md`](realms/pham-gioi/00-world-atlas.md) |
| **Linh Giới** | 灵界 | Thiên Địa Linh Khí | **1 planet active:** [Càn Nguyên Tinh](realms/linh-gioi/planets/can-nguyen-tinh/00-overview.md); quần vực láng giềng deferred | [`realms/linh-gioi/00-world-atlas.md`](realms/linh-gioi/00-world-atlas.md) |
| **Tiên Giới** | 仙界 | Tiên Khí / Tiên Nguyên Lực | **System-first:** [`TH-TIEN-*`](realms/tien-gioi/systems/00-system-index.md); planet theo nhu cầu | [`realms/tien-gioi/00-world-atlas.md`](realms/tien-gioi/00-world-atlas.md) |
| **Thần Giới** | 神界 | Thần Khí | **System-first:** [`TH-THAN-*`](realms/than-gioi/systems/00-system-index.md); planet theo nhu cầu | [`realms/than-gioi/00-world-atlas.md`](realms/than-gioi/00-world-atlas.md) |

### 1.1. Giới bích (tóm)

| Cặp | Cơ chế `(invariant)` |
| --- | --- |
| Phàm ↔ Linh | Xuyên giới (khai mạch, truyền tống, đại năng…) |
| Linh ↔ Tiên | Phi thăng — **Cửu Cửu** tại Độ Kiếp |
| Tiên ↔ Thần | Đại kiếp / tài nguyên Thần giai — hiếm |

---

## 2. Phàm Giới — tinh hà (Phase 1a ✓)

**Quy mô user:** Chỉ **một tinh hà chủ** — sự kiện / đại lục chính; tinh hà lân cận (nếu nhắc) = **bất khả đạt** trừ crack / truyền thuyết (tối thiểu).

| ID | Tên | Vị trí trong void Phàm | Quy mô (story) | Linh khí / sinh thái |
| --- | --- | --- | --- | --- |
| `TH-PHAM-BICH-LAC` | **Tinh hà Bích Lạc** (碧落星河) | Cụm **nam–tây** mặt phẳng Hư Không Phàm; giới bích Phàm–Linh ~9 vạn đơn vị hư không *(lore, không đo phàm)* | **6** đại lục (`CHL-*`); bbox grid ~ x∈[−360,+330], y∈[−250,+220] | **Mạt pháp** — cực mỏng / vô linh; **võ tu / Luyện Thể**; manh mạch **rò khí** ( không chân tu cư trú — Luật 6a ) |

**Atlas · catalog:** [`realms/pham-gioi/00-world-atlas.md`](realms/pham-gioi/00-world-atlas.md) · [`realms/pham-gioi/01-region-catalog.md`](realms/pham-gioi/01-region-catalog.md)

**GeoJSON · PNG:** [`realms/pham-gioi/planets/bich-lac-tinh/geo/00-tinh-ha.geojson`](realms/pham-gioi/planets/bich-lac-tinh/geo/00-tinh-ha.geojson) · [`realms/pham-gioi/planets/bich-lac-tinh/geo/out/00-tinh-ha.png`](realms/pham-gioi/planets/bich-lac-tinh/geo/out/00-tinh-ha.png) · **Tàn Mộ:** 9/9 REG `planets/bich-lac-tinh/geo/region/reg-tm-*.geojson` (Phase **1e** ✓)

**Châu lục deep (Phase 1b + ext ✓ — 6/6):** atlas §2.1 · `geo/chau-luc/chl-{xich-ha,tam-nguyen,han-phuong,phu-tao,lo-hang,tan-mo}.geojson`

**Region exemplars (Phase 1c–1d ✓):** `reg-xh-de-do` · `reg-tn-trung-nguyen` · `reg-tm-khe-gioi` · `reg-tm-co-tu` · [`02-tieu-cuc-index.md`](realms/pham-gioi/02-tieu-cuc-index.md)

---

## 3. Linh Giới — tinh hà (Phase 2a ✓)

**Quy mô user:** **1** tinh hà chủ (geo) + **2–3** láng giềng (atlas only). Main **khác** Phàm `TH-PHAM-BICH-LAC` (tên · void · bbox).

| ID | Tên | Vị trí trong void Linh | Quy mô (story) | Linh khí / sinh thái |
| --- | --- | --- | --- | --- |
| **`TH-LINH-CAN-NGUYEN`** | **Tinh hà Càn Nguyên** (苍元灵域) | Cụm **bắc–đông** Hư Không Linh | **6** đại lục (`CHL-*`); bbox ~ x∈[−265,+304], y∈[−208,+227] | **Dày**; Luyện Khí→Độ Kiếp; giới bích Linh–Tiên = Cửu Cửu |
| `TH-LINH-HUYEN-AM` | Tinh hà Huyền Âm (玄阴灵域) | **Tây** main (~3–5 vạn hư không lore) | 4–5 lục (chưa geo) | Âm thịnh — tu âm, Minh mạch |
| `TH-LINH-MOC-DUONG` | Tinh hà Mộc Dương (木阳灵域) | **Nam** main | 5–7 lục (chưa geo) | Mộc–dương — dược, yêu biên |
| `TH-LINH-KIM-HA` | Tinh hà Kim Hà (金河灵域) | **Đông bắc xa** main | 6+ lục (chưa geo) | Kim–Thủy — linh thạch thượng, liên tinh thương |

**Atlas · catalog:** [`realms/linh-gioi/00-world-atlas.md`](realms/linh-gioi/00-world-atlas.md) (cụm tinh hà) · [`realms/linh-gioi/planets/can-nguyen-tinh/00-world-atlas.md`](realms/linh-gioi/planets/can-nguyen-tinh/00-world-atlas.md) (Càn Nguyên chi tiết) · [`realms/linh-gioi/01-region-catalog.md`](realms/linh-gioi/01-region-catalog.md)

**GeoJSON · PNG (main):** [`realms/linh-gioi/planets/can-nguyen-tinh/geo/00-tinh-ha.geojson`](realms/linh-gioi/planets/can-nguyen-tinh/geo/00-tinh-ha.geojson) · [`realms/linh-gioi/planets/can-nguyen-tinh/geo/out/00-tinh-ha.png`](realms/linh-gioi/planets/can-nguyen-tinh/geo/out/00-tinh-ha.png)

**Châu lục deep (Phase 2b + 2b-ext ✓ — 6/6):** `geo/chau-luc/chl-{trung-linh,cuu-lac,bang-phong,ngoc-lam,hoa-dien,van-hai}.geojson` · PNG stem `chl-<slug>.png` (parity Phàm 1b-ext)

**Region exemplars (Phase 2c ✓):** [`reg-tl-thien-quan.geojson`](realms/linh-gioi/planets/can-nguyen-tinh/geo/region/reg-tl-thien-quan.geojson) · [`reg-cl-cuu-khau.geojson`](realms/linh-gioi/planets/can-nguyen-tinh/geo/region/reg-cl-cuu-khau.geojson) · [`02-tieu-cuc-index.md`](realms/linh-gioi/02-tieu-cuc-index.md)

---

## 4. Tiên Giới — tinh hà (Phase 3a ✓)

**Quy mô user:** **1** tinh hà chủ (geo) + **5–7** láng giềng (atlas only). Main **khác** Phàm `TH-PHAM-BICH-LAC` và Linh `TH-LINH-CAN-NGUYEN` (tên · void · bbox).

| ID | Tên | Vị trí trong void Tiên | Quy mô (story) | Tiên khí / sinh thái |
| --- | --- | --- | --- | --- |
| **`TH-TIEN-HUONG-NGUYEN`** | **Tinh hà Hương Nguyên** (香元仙域) | Cụm **nam–tây trung tâm** Hư Không Tiên | **6** đại lục (`CHL-*`); bbox ~ x∈[−282,+217], y∈[−192,+244] | **Ổn định–dồi**; Chân Tiên→Tiên Đế; giới bích Tiên–Thần = đại kiếp |
| `TH-TIEN-CAM-LAC` | Tinh hà Cảm Lạc (淡落仙域) | **Tây** main (~4–6 vạn hư không lore) | 4–5 lục (chưa geo) | **Loãng** — Tản Tiên di tích |
| `TH-TIEN-DUONG-HANH` | Tinh hà Dương Hành (曜行仙域) | **Bắc** main | 5–6 lục (chưa geo) | Dương thịnh — phi thuyền liên tinh |
| `TH-TIEN-NGUOC-MAC` | Tinh hà Ngược Mạc (逆漠仙域) | **Tây nam** main | 3–4 lục (chưa geo) | Hỗn loạn cục bộ — thử kiếp |
| `TH-TIEN-LONG-TAU` | Tinh hà Long Tẩu (龙腾仙域) | **Đông** main | 5–7 lục (chưa geo) | Long khí — Long Linh |
| `TH-TIEN-UY-VOI` | Tinh hà Uy Vi (幽微仙域) | **Đông nam xa** main | 4–6 lục (chưa geo) | U vi — ảo cảnh, bí pháp |
| `TH-TIEN-THAI-CUC` | Tinh hà Thái Cực (太极仙域) | **Tây bắc** main | 6 lục (chưa geo) | Trung hòa Ngũ Hành — đan tiên |

**Liên tinh hà (lore):** **Tiên Vương+** có thể mở mạch hư không ngắn giữa `TH-TIEN-*` — **phí / khế**; không thêm invariant Core.

**Atlas · catalog:** [`realms/tien-gioi/00-world-atlas.md`](realms/tien-gioi/00-world-atlas.md) · [`realms/tien-gioi/01-region-catalog.md`](realms/tien-gioi/01-region-catalog.md)

**GeoJSON · PNG (main):** [`realms/tien-gioi/geo/00-tinh-ha.geojson`](realms/tien-gioi/geo/00-tinh-ha.geojson) · [`realms/tien-gioi/geo/out/00-tinh-ha.png`](realms/tien-gioi/geo/out/00-tinh-ha.png)

**Châu lục deep (Phase 3b-ext ✓ — 6/6):** [`chl-trung-tien.geojson`](realms/tien-gioi/geo/chau-luc/chl-trung-tien.geojson) · [`chl-thanh-van.geojson`](realms/tien-gioi/geo/chau-luc/chl-thanh-van.geojson) · [`chl-ngu-long.geojson`](realms/tien-gioi/geo/chau-luc/chl-ngu-long.geojson) · [`chl-kim-hoa.geojson`](realms/tien-gioi/geo/chau-luc/chl-kim-hoa.geojson) · [`chl-tran-lac.geojson`](realms/tien-gioi/geo/chau-luc/chl-tran-lac.geojson) · [`chl-huyen-bang.geojson`](realms/tien-gioi/geo/chau-luc/chl-huyen-bang.geojson) · atlas §2.1.

**Region exemplars (Phase 3c ✓):** [`reg-tt-tien-quan.geojson`](realms/tien-gioi/geo/region/reg-tt-tien-quan.geojson) · [`reg-tv-van-cung.geojson`](realms/tien-gioi/geo/region/reg-tv-van-cung.geojson)

---

## 5. Thần Giới — tinh hà (Phase 4a ✓)

**Quy mô user:** **1** tinh hà chủ (geo) + **7–9** láng giềng (atlas) — canon **10** TH. Main **khác** Phàm `TH-PHAM-BICH-LAC`, Linh `TH-LINH-CAN-NGUYEN`, Tiên `TH-TIEN-HUONG-NGUYEN` (tên · void · bbox).

| ID | Tên | Vị trí trong void Thần | Quy mô (story) | Thần khí / sinh thái |
| --- | --- | --- | --- | --- |
| **`TH-THAN-HUYEN-CUC`** | **Tinh hà Huyền Cự** (玄极神域) | Cụm **bắc–tây trung tâm** Hư Không Thần | **7** đại lục (`CHL-*`); bbox ~ x∈[−250,+228], y∈[−217,+244] | **Nặng ổn định**; Thần giai; giới bích Tiên–Thần = đại kiếp |
| `TH-THAN-TICH-MINH` | Tinh hà Tịch Minh (寂明神域) | **Tây** main | 4–5 lục (chưa geo) | **Tịnh** — thần khí sạch, loãng |
| `TH-THAN-DO-DU` | Tinh hà Độ Du (渡游神域) | **Nam** main | 5–6 lục (chưa geo) | Mạch du hành · thuế liên tinh |
| `TH-THAN-LOI-HANH` | Tinh hà Lôi Hành (雷行神域) | **Đông** main | 5–7 lục (chưa geo) | **Lôi thịnh** — Thần kiếp |
| `TH-THAN-HON-NGUYEN` | Tinh hà Hồn Nguyên (混元神域) | **Bắc** main | 6 lục (chưa geo) | Hỗn nguyên manh — **Thánh** lore |
| `TH-THAN-PHUC-MENH` | Tinh hà Phục Mệnh (复命神域) | **Tây nam** main | 4–5 lục (chưa geo) | Sinh–diệt dao động |
| `TH-THAN-VAN-TU` | Tinh hà Vạn Tự (万序神域) | **Đông bắc** main | 6 lục (chưa geo) | Luật thần · khế Vạn Tự |
| `TH-THAN-DOAN-MACH` | Tinh hà Đoạn Mạch (断脉神域) | **Nam tây** main | 3–4 lục (chưa geo) | Mạch đứt — nhập Thần nguyên |
| `TH-THAN-HU-VI` | Tinh hà Hư Vi (虚无神域) | **Tây bắc xa** main | 2–3 lục (chưa geo) | Mép void · Vực Ngoại |
| `TH-THAN-THAI-SO` | Tinh hà Thái Sơ (太初神域) | **Đông nam xa** main | 5–6 lục (chưa geo) | Cổ khí + di tích thần cổ |

**Liên tinh hà (lore):** **Thần Vương+** (Logic mở bậc) mạch hư không ngắn giữa `TH-THAN-*`; **Thánh-tier** liên tinh hà **không** hub geo — không thêm invariant Core.

**Atlas · catalog:** [`realms/than-gioi/00-world-atlas.md`](realms/than-gioi/00-world-atlas.md) · [`realms/than-gioi/01-region-catalog.md`](realms/than-gioi/01-region-catalog.md)

**GeoJSON · PNG (main):** [`realms/than-gioi/geo/00-tinh-ha.geojson`](realms/than-gioi/geo/00-tinh-ha.geojson) · [`realms/than-gioi/geo/out/00-tinh-ha.png`](realms/than-gioi/geo/out/00-tinh-ha.png)

**Châu lục deep (Phase 4b + 4b-ext ✓ — 7/7):** [`chl-trung-than.geojson`](realms/than-gioi/geo/chau-luc/chl-trung-than.geojson) · [`chl-van-phap.geojson`](realms/than-gioi/geo/chau-luc/chl-van-phap.geojson) · [`chl-kiem-loi.geojson`](realms/than-gioi/geo/chau-luc/chl-kiem-loi.geojson) · [`chl-hon-vuc.geojson`](realms/than-gioi/geo/chau-luc/chl-hon-vuc.geojson) · [`chl-sinh-tieu.geojson`](realms/than-gioi/geo/chau-luc/chl-sinh-tieu.geojson) · [`chl-huyen-bang.geojson`](realms/than-gioi/geo/chau-luc/chl-huyen-bang.geojson) · [`chl-cuu-phong.geojson`](realms/than-gioi/geo/chau-luc/chl-cuu-phong.geojson) · PNG stem `chl-<slug>.png` · atlas §2.1.

**Region exemplars (Phase 4c ✓):** [`reg-rt-than-quan.geojson`](realms/than-gioi/geo/region/reg-rt-than-quan.geojson) · [`reg-vp-phap-dien.geojson`](realms/than-gioi/geo/region/reg-vp-phap-dien.geojson) · [`02-tieu-cuc-index.md`](realms/than-gioi/02-tieu-cuc-index.md) · atlas §2.1 exemplar.

---

## 6. Giới phụ & pocket (Phase 5 ✓)

**Depth doc:** [`06-subsidiary-realms.md`](06-subsidiary-realms.md) — Minh · Ma/Yêu patches · Vực Ngoại nội giới · Tiểu Thiên · stub Bí cảnh / Chư Thiên · bảng neo atlas.

Không thay bộ bốn giới diện vật chất trên lộ trình Phàm→Thần `(invariant)`.

| Khái niệm | Vai trò | Gắn vào 4 giới (tóm) |
| --- | --- | --- |
| **Minh Giới** (冥界) | Luân hồi, vong hồn, âm khí | Mạch **Phàm mỏng** · **Linh Huyền Âm** · **Thần Hồn Vực** = hồn–mệnh, **không** hub Minh |
| **Ma / Yêu patches** | Ma Khí / Yêu Khí **mảnh biên** | `SUB-PATCH-MA-TAN-MO` (Phàm) · `SUB-PATCH-MA-VH-ABYSS` (Linh) · `SUB-PATCH-MA-TL-PIT` (Tiên) · Yêu: Ngọc Lâm / Cửu Lạc / Mộc Dương rim |
| **Vực Ngoại nội giới / hư không nội giới** (域外 · 虚空) | Vùng rìa và các mạch xa trong Giới Tường — **không** giới tu | Mạch Phàm–Linh (`REG-TM-KHE-GIOI`, `REG-CL-PHAM-KHE`) · Linh–Tiên (Cửu Khẩu) · Tiên–Thần (Huyền Băng) · mép `TH-THAN-HU-VI` |
| **Tiểu Thiên Thế Giới** (小千世界) | Pocket host | **`E-PHAM-POCKET`** — Tam Nguyên; **không** thay Cửu Cửu |
| **Bí cảnh / Chư Thiên** | Cắt không gian / đa bộ bốn giới | Stub slots trong `06-subsidiary-realms.md` §5–§6 |

```text
     [ Vực Ngoại nội giới — vùng rìa và graph liên giới ]
    /    |      |      \
[Phàm] [Linh] [Tiên] [Thần]   ← bốn giới diện vật chất song song
  |       |
[Minh]  [Ma/Yêu patches]      ← phụ / mảnh
  ~ pocket Tiểu Thiên treo host ~
```

---

## 7. Cây thư mục chuẩn (mỗi giới chính)

```text
foundation/logic/world/realms/<giới-slug>/
  00-world-atlas.md
  01-region-catalog.md
  canvas/
  geo/
    00-tinh-ha.geojson
    chau-luc/*.geojson
    region/*.geojson
    out/*.png
```

**Slug giới:** `pham-gioi` · `linh-gioi` · `tien-gioi` · `than-gioi`

---

*Orchestrator scaffold — 2026-09-18. Tên địa danh do world-builder sinh; không lấy từ tác phẩm archived.*
