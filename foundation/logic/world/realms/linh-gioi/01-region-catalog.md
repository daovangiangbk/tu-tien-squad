# Linh Giới — Region catalog

> **Mục đích:** Liệt kê `REG-*` theo đại lục **tinh hà Càn Nguyên** — đối chiếu `chau_luc` (2b) / `region` (2c).

**Atlas (tinh cầu):** [`planets/can-nguyen-tinh/00-world-atlas.md`](planets/can-nguyen-tinh/00-world-atlas.md) · **Giới (cụm TH):** [`00-world-atlas.md`](00-world-atlas.md) · **Tinh hà:** [`planets/can-nguyen-tinh/geo/00-tinh-ha.geojson`](planets/can-nguyen-tinh/geo/00-tinh-ha.geojson) · **Tiểu cục:** [`02-tieu-cuc-index.md`](02-tieu-cuc-index.md)

**Chú thích cột Geo:** `✓` = có polygon trong `chau_luc`; **region** = có `geo/region/*.geojson` (2c); `—` = stub / chưa vẽ.

---

## CHL-TRUNG-LINH (Trung Linh) — chau_luc done

Hub: `LOC-TL-THIEN-QUAN` · File: [`geo/chau-luc/chl-trung-linh.geojson`](planets/can-nguyen-tinh/geo/chau-luc/chl-trung-linh.geojson)

| REG ID | Tên gợi ý | Vai trò | Geo |
| --- | --- | --- | --- |
| `REG-TL-NAM-VAN` | Nam Vân · cửa mây | Thương lộ Vân Hải | ✓ |
| `REG-TL-LINH-HA` | Linh Hà bình | Mạch công cộng | ✓ |
| `REG-TL-THIEN-QUAN` | Thiên Quan thành | Trung ương tông · hub | ✓ · **region** → [`reg-tl-thien-quan.geojson`](planets/can-nguyen-tinh/geo/region/reg-tl-thien-quan.geojson) |
| `REG-TL-TAM-TONG` | Tam Tông đài | Chính trị tu giới | ✓ |
| `REG-TL-BAC-LINH` | Bắc Linh | Biên Băng Phong | ✓ |
| `REG-TL-BAC-DONG` | Bắc Đông uyên | Hoang đông bắc | ✓ |
| `REG-TL-TAY-MACH` | Tây Mạch | Biên Hỏa Diễm | ✓ |
| `BRR-TL-THIEN-LAM` | Dãy Thiên Lam | Barrier (polygon) | ✓ |
| `REG-TL-PHUC-DIA` | Phúc Địa cốc | Động phủ T2–T3 | ✓ |
| `REG-TL-DONG-LAM` | Đông Lam | Rừng linh · mạch vệt | ✓ |
| `REG-TL-DONG-HAI` | Đông Hải linh cảng | Phi thuyền · thuế | ✓ |

**Sông (chau_luc):** `RIVER-TL-LINH-HA`, `RIVER-TL-DONG-LUU`

---

## CHL-CUU-LAC (Cửu Lạc) — chau_luc done

Hub: `LOC-CL-CUU-KHAU` · File: [`geo/chau-luc/chl-cuu-lac.geojson`](planets/can-nguyen-tinh/geo/chau-luc/chl-cuu-lac.geojson)

| REG ID | Tên gợi ý | Vai trò | Geo |
| --- | --- | --- | --- |
| `REG-CL-NAM-HAI` | Nam Hải đài | Cửa biển | ✓ |
| `REG-CL-PHAM-KHE` | Phàm Khe | Crack Phàm–Linh `(slot E-LINH-PHAM-CRACK)` | ✓ |
| `REG-CL-LAC-HE` | Lạc Hà hội | Cửu sông hội | ✓ |
| `REG-CL-LAC-TAM` | Lạc Tam trì | Trì linh trung tâm | ✓ |
| `REG-CL-CUU-KHAU` | Cửu Khẩu đài | Phi thăng `(slot E-LINH-ASCENSION-GATE)` · hub | ✓ · **region** → [`reg-cl-cuu-khau.geojson`](planets/can-nguyen-tinh/geo/region/reg-cl-cuu-khau.geojson) |
| `REG-CL-TAN-TIEN` | Tàn Tiên đài | Tản Tiên di tích | ✓ |
| `REG-CL-DONG-LAC` | Đông Lạc | Đảo phía đông | ✓ |
| `REG-CL-TAY-DAO` | Tây Đảo | Liên đảo tây | ✓ |
| `BRR-CL-CUU-SON` | Dãy Cửu Sơn | Barrier | ✓ |
| `REG-CL-BAC-PHONG` | Bắc Phong | Hướng Ngọc Lâm | ✓ |

**Sông (chau_luc):** `RIVER-CL-CUU-LAC`, `RIVER-CL-LAC-CHI`

---

## Exemplar region (Phase 2c ✓)

**Geo:** [`geo/region/reg-tl-thien-quan.geojson`](planets/can-nguyen-tinh/geo/region/reg-tl-thien-quan.geojson) · [`geo/region/reg-cl-cuu-khau.geojson`](planets/can-nguyen-tinh/geo/region/reg-cl-cuu-khau.geojson)
**PNG:** [`geo/out/region-reg-tl-thien-quan.png`](planets/can-nguyen-tinh/geo/out/region-reg-tl-thien-quan.png) · [`geo/out/region-reg-cl-cuu-khau.png`](planets/can-nguyen-tinh/geo/out/region-reg-cl-cuu-khau.png)

### Bàn cờ — Thiên Quan thành (`REG-TL-THIEN-QUAN`)

**Khan hiếm:** Linh thạch **hạ–trung** qua `LOC-TL-LINH-MACH-NO` — monopoly **Thiên Quan Tông** + Tam Tông; thuế mạch **25–30%** trên `RIVER-TL-LINH-HA-URBAN`; động phủ **T1** (`LOC-TL-GIA-TTOC-PHU`, gia tộc) · **T2** (`LOC-TL-TONG-LINH-HA`); tranh **T2–T3** tại `LOC-TL-PHUC-DIA-MEN` (Phúc Địa).

**Cửa thoát:** Bắc `ROUTE-TL-THIEN-TAM` → `REG-TL-TAM-TONG`; đông `ROUTE-TL-THIEN-DONG` → `REG-TL-DONG-LAM`; nam sông → `REG-TL-LINH-HA`; tây `BRR-TL-THIEN-LAM-FOOT` → Thiên Lam (mạch rải, kiếp nặng hơn).

**Phản ứng tông / chính trị tu:** Lộ diện tranh mạch = **truy nã liên tông**; phe một tông trong Tam Tông = **đóng thành** với đối thủ; đụng mạch gốc nội thành = **Nhân quả** + can thiệp trung ương. **Phần thưởng:** an toàn tương đối quanh hub, tiếp cận công pháp hạng trung–cao, đan dược nhập từ Ngọc Lâm/Vân Hải. **Giá:** thuế linh thạch cao; chính trị Tam Tông — **không trung lập** lâu dài.

### Bàn cờ — Cửu Khẩu đài (`REG-CL-CUU-KHAU`)

**Khan hiếm:** Linh thạch **thượng / linh nguyên** đốt tại `LOC-CL-HOI-THANH` (chờ chu kỳ); trì `LOC-CL-LAC-TAM-NE` — thuế **35–45%** + quota tông; động phủ **T3** tại `LOC-CL-CUU-MEN` `(slot E-LINH-ASCENSION-GATE)` — **không** mua bằng thạch thuần.

**Cửa thoát:** Nam `RIVER-CL-CUU-LAC-URBAN` → Nam Hải / Lạc Hà hội; bắc `ROUTE-CL-KHAU-BAC-PHONG` → Ngọc Lâm (gió linh); đông bắc `ROUTE-CL-KHAU-TAN-TIEN` → Tàn Tiên (vệt Tiên khí); tây `LOC-CL-CUU-SON-FOOT` → Cửu Sơn.

**Phản ứng tông / chính trị tu:** Chen lấn **chu kỳ phi thăng** = **diệt sát** hoặc khế **mang nợ Nhân quả**; lộ vệt Tàn Tiên = phe tranh **di cổ**; hội thành — **hội thương liên tông** giám sát, không chiến công khai trong vòng đài. **Phần thưởng:** cơ hội **Cửu Cửu** / Linh–Tiên (logic slot); đan dược từ Lạc Tam trì. **Giá:** đan dược + linh thạch **đốt**; thất bại phi thăng = **Tản Tiên** (Luật 5–6).

---

## CHL-BANG-PHONG (Băng Phong) — chau_luc done

Hub: `LOC-BP-BANG-TINH` · File: [`geo/chau-luc/chl-bang-phong.geojson`](planets/can-nguyen-tinh/geo/chau-luc/chl-bang-phong.geojson) · PNG: [`chl-bang-phong.png`](planets/can-nguyen-tinh/geo/out/chl-bang-phong.png)

| REG ID | Tên gợi ý | Vai trò | Geo |
| --- | --- | --- | --- |
| [`REG-BP-NAM-DONG`](planets/can-nguyen-tinh/continents/bang-phong/regions/reg-bp-nam-dong/00-overview.md) | Nam Đông | Biên Trung Linh (`REG-TL-BAC-LINH`) | ✓ |
| [`REG-BP-NAM-PHONG`](planets/can-nguyen-tinh/continents/bang-phong/regions/reg-bp-nam-phong/00-overview.md) | Nam Phong | Cửa gió · thương lộ | ✓ |
| [`REG-BP-TAY-BANG`](planets/can-nguyen-tinh/continents/bang-phong/regions/reg-bp-tay-bang/00-overview.md) | Tây Băng | Biên tây · Huyền Âm (lore) | ✓ |
| `BRR-BP-VAN-PHONG` | Dãy Vân Phong | Barrier Băng–Phong | ✓ |
| [`REG-BP-PHONG-COC`](planets/can-nguyen-tinh/continents/bang-phong/regions/reg-bp-phong-coc/00-overview.md) | Phong Cốc | Tu Băng–Phong | ✓ |
| [`REG-BP-HAN-UYEN`](planets/can-nguyen-tinh/continents/bang-phong/regions/reg-bp-han-uyen/00-overview.md) | Hàn Uyên | Hoang địa | ✓ |
| [`REG-BP-LINH-BANG`](planets/can-nguyen-tinh/continents/bang-phong/regions/reg-bp-linh-bang/00-overview.md) | Linh Băng hồ | Linh thạch đóng băng | ✓ |
| [`REG-BP-DONG-HAN`](planets/can-nguyen-tinh/continents/bang-phong/regions/reg-bp-dong-han/00-overview.md) | Đông Hàn | Uyên đông | ✓ |
| [`REG-BP-BANG-TINH`](planets/can-nguyen-tinh/continents/bang-phong/regions/reg-bp-bang-tinh/00-overview.md) | Băng Tinh quan | Thành cực bắc · hub | ✓ |
| [`REG-BP-BAC-HUYEN`](planets/can-nguyen-tinh/continents/bang-phong/regions/reg-bp-bac-huyen/00-overview.md) | Bắc Huyền | Cực bắc · kiếp nặng | ✓ |

**Sông / tuyến (chau_luc):** `RIVER-BP-LINH-BANG`, `ROUTE-BP-DONG-TRUNG-LINH`

---

## CHL-NGOC-LAM (Ngọc Lâm) — chau_luc done

Hub: `LOC-NL-LAM-TINH` · File: [`geo/chau-luc/chl-ngoc-lam.geojson`](planets/can-nguyen-tinh/geo/chau-luc/chl-ngoc-lam.geojson) · PNG: [`chl-ngoc-lam.png`](planets/can-nguyen-tinh/geo/out/chl-ngoc-lam.png)

| REG ID | Tên gợi ý | Vai trò | Geo |
| --- | --- | --- | --- |
| `REG-NL-NAM-HAI` | Nam Hải linh cảng | Phi thuyền · thuế | ✓ |
| `REG-NL-LAM-TINH` | Lam Tinh trấn | Dược thương · hub | ✓ |
| `REG-NL-BICH-HO` | Bích Hồ | Linh thảo | ✓ |
| `REG-NL-THAO-COC` | Thảo Cốc | Thung lũng dược | ✓ |
| `REG-NL-TAY-LAM` | Tây Lâm | Rìa tây | ✓ |
| `BRR-NL-THAN-SON` | Dãy Thần Sơn | Barrier Mộc | ✓ |
| `REG-NL-THAN-MOC` | Thần Mộc lâm | Yêu tộc biên | ✓ |
| `REG-NL-CUU-VIEN` | Cửu Viên | Bí cảnh Mộc | ✓ |
| `REG-NL-TRUNG-DU` | Trung Du | Đồng bằng linh mộc | ✓ |
| `REG-NL-BAC-PHONG` | Bắc Phong | Hướng Cửu Lạc (`REG-CL-BAC-PHONG`) | ✓ |
| `REG-NL-DONG-LINH` | Đông Linh | Biên Trung Linh (`REG-TL-DONG-HAI`) | ✓ |
| `REG-NL-NGOAI-VI` | Ngoại Vi | Đảo phía đông | ✓ |

**Sông / tuyến (chau_luc):** `RIVER-NL-BICH-HO`, `ROUTE-NL-BAC-CUU-LAC`

---

## CHL-HOA-DIEN (Hỏa Diễm) — chau_luc done

Hub: `LOC-HD-HOA-QUAN` · File: [`geo/chau-luc/chl-hoa-dien.geojson`](planets/can-nguyen-tinh/geo/chau-luc/chl-hoa-dien.geojson) · PNG: [`chl-hoa-dien.png`](planets/can-nguyen-tinh/geo/out/chl-hoa-dien.png)

| REG ID | Tên gợi ý | Vai trò | Geo |
| --- | --- | --- | --- |
| `REG-HD-NAM-VIEM` | Nam Viêm | Sa nóng nam | ✓ |
| `REG-HD-HOA-QUAN` | Hỏa Quan thành | Lò đan / luyện khí · hub | ✓ |
| `REG-HD-VIEM-QUAN` | Viêm Quan | Mỏ Hỏa mạch | ✓ |
| `REG-HD-TAN-DIA` | Tàn Địa | Chiến trường Hỏa–Băng cổ | ✓ |
| `REG-HD-TAY-HOANG` | Tây Hoang | Biên tây | ✓ |
| `BRR-HD-LIET-DUONG` | Dãy Liệt Dương | Barrier · biên Tây Mạch | ✓ |
| `REG-HD-DONG-MACH` | Đông Mạch | Biên Trung Linh (`REG-TL-TAY-MACH`) | ✓ |
| `REG-HD-VIEM-TAM` | Viêm Tam | Hỏa trì luyện đan | ✓ |
| `REG-HD-BAC-LO` | Bắc Lô | Luyện khí liên minh | ✓ |
| `REG-HD-NGOAI-HOA` | Ngoại Hỏa | Sa hỏa đông | ✓ |
| `REG-HD-BAC-HAN` | Bắc Hàn | Biên Băng Phong (lore) | ✓ |

**Sông / tuyến (chau_luc):** `RIVER-HD-VIEM-HE`, `ROUTE-HD-TAY-TRUNG-LINH`

---

## CHL-VAN-HAI (Vân Hải) — chau_luc done

Hub: `LOC-VH-VAN-CANG` · File: [`geo/chau-luc/chl-van-hai.geojson`](planets/can-nguyen-tinh/geo/chau-luc/chl-van-hai.geojson) · PNG: [`chl-van-hai.png`](planets/can-nguyen-tinh/geo/out/chl-van-hai.png)

| REG ID | Tên gợi ý | Vai trò | Geo |
| --- | --- | --- | --- |
| `REG-VH-BAC-VAN` | Bắc Vân | Cửa Trung Linh (`REG-TL-NAM-VAN`) | ✓ |
| `REG-VH-VAN-CANG` | Vân Cảng | Phi thuyền · hub | ✓ |
| `REG-VH-DAO-MOC` | Đảo Mộc | Đảo trung tâm | ✓ |
| `REG-VH-TAY-DAO` | Tây Đảo | Liên đảo tây | ✓ |
| `BRR-VH-HAI-SON` | Dãy Hải Sơn | Barrier Thủy–Phong | ✓ |
| `REG-VH-VAN-HAI` | Vân Hải | Hải vực mây | ✓ |
| `REG-VH-HAI-MA` | Hải Mạch | Ma patch `(slot E-LINH-MA-PATCH-VH)` | ✓ |
| `REG-VH-PHONG-BAO` | Phong Bão hải | Hải vực nguy hiểm | ✓ |
| `REG-VH-DONG-DAO` | Đông Đảo | Hướng Ngọc Lâm / Cửu Lạc | ✓ |
| `REG-VH-LINH-DAM` | Linh Đám mây | Thu linh khí mây | ✓ |
| `REG-VH-NAN-DAO` | Nam Đảo | Quần đảo nam · hậu cần hải lộ | ✓ |

**Sông / tuyến (chau_luc):** `RIVER-VH-VAN-LUU`, `ROUTE-VH-BAC-NAM-VAN`

---

*World-builder · T-foundation-linh-2b-ext · 6/6 chau_luc Càn Nguyên*
