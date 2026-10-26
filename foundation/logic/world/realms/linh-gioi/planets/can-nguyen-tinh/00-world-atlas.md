# Càn Nguyên Tinh — atlas (Foundation Canon)

> **work_slug:** `foundation-canon` · **Parent map:** `TH-LINH-CAN-NGUYEN` · **Giới:** Linh · **Convention:** [`../../../../00-geojson-world-map-convention.md`](../../../../00-geojson-world-map-convention.md)

**Realm (cụm tinh hà):** [`../../00-world-atlas.md`](../../00-world-atlas.md) · **Planet:** [`00-overview.md`](00-overview.md) · **Catalog:** [`../../01-region-catalog.md`](../../01-region-catalog.md) · **Tiểu cục:** [`../../02-tieu-cuc-index.md`](../../02-tieu-cuc-index.md)

**GeoJSON (main):** [`geo/00-tinh-ha.geojson`](geo/00-tinh-ha.geojson) · **chau_luc 6/6:** [`chl-trung-linh`](geo/chau-luc/chl-trung-linh.geojson) · [`chl-cuu-lac`](geo/chau-luc/chl-cuu-lac.geojson) · [`chl-bang-phong`](geo/chau-luc/chl-bang-phong.geojson) · [`chl-ngoc-lam`](geo/chau-luc/chl-ngoc-lam.geojson) · [`chl-hoa-dien`](geo/chau-luc/chl-hoa-dien.geojson) · [`chl-van-hai`](geo/chau-luc/chl-van-hai.geojson) · **region:** [`reg-tl-thien-quan`](geo/region/reg-tl-thien-quan.geojson) · [`reg-cl-cuu-khau`](geo/region/reg-cl-cuu-khau.geojson)

**PNG:** [`geo/out/00-tinh-ha.png`](geo/out/00-tinh-ha.png) · [`chl-trung-linh.png`](geo/out/chl-trung-linh.png) · [`chl-cuu-lac.png`](geo/out/chl-cuu-lac.png) · [`chl-bang-phong.png`](geo/out/chl-bang-phong.png) · [`chl-ngoc-lam.png`](geo/out/chl-ngoc-lam.png) · [`chl-hoa-dien.png`](geo/out/chl-hoa-dien.png) · [`chl-van-hai.png`](geo/out/chl-van-hai.png) · [`region-reg-tl-thien-quan.png`](geo/out/region-reg-tl-thien-quan.png) · [`region-reg-cl-cuu-khau.png`](geo/out/region-reg-cl-cuu-khau.png)

---

## 1. Tinh cầu Càn Nguyên (parent map)

| Trường | Giá trị |
| --- | --- |
| **ID** | `TH-LINH-CAN-NGUYEN` |
| **Tên** | **Tinh hà Càn Nguyên** — ID legacy bọc **một** tinh cầu |
| **Vị trí trong Hư Không Linh** | Cụm **bắc–đông** đã khảo sát; hub `TINH-HA-REF` ≈ **giao linh mạch** Trung Linh — không phải tâm vật lý tuyệt đối. Giới bích Phàm–Linh **không** nằm trên bản đồ địa lý này. |
| **Thang lưới** | Story grid: **x = Đông (+), y = Bắc (+)**; một đơn vị ≈ **một ngày đi lộ** (tu sĩ Trúc Cơ, không phù). Bán kính hành trình tinh cầu: **~900–1000** đơn vị tới mép lục xa. |
| **Quy mô vật lý (tóm)** | **6** đại lục (`CHL-*`) + biển linh khí / đảo mây (chưa vẽ chi tiết); polygon **không chồng** trên `tinh_ha`. |

### 1.1. Linh khí & sinh thái `(neo Luật 6 · Luật 1)`

- **Linh khí:** **Dày** — đủ nuôi **Luyện Khí → Trúc Cơ → … → Độ Kiếp** trên cùng giới; đột phá đỉnh = **Cửu Cửu** + **Linh–Tiên** (Tản Tiên nếu thất bại).
- **Năng lượng phụ:** **Ma/Yêu khí** ở **biên lục** và crack Vực Ngoại; **Tiên khí** chỉ **vệt** (di tích phi thăng thành).
- **Sinh thái:** Yêu thú hóa hình, linh thú; **Thiên kiếp** từ Kim Đan trở lên (sync `03-power-system-economy-core.md`).
- **Nhân loại / tu:** **Tông môn + gia tộc** cai trị mạch; **phàm nhân (vô + hữu căn) = đa số dân**, tu sĩ **thiểu số** — [`../../../../03-demographics-pham-linh.md`](../../../../03-demographics-pham-linh.md) §2–§3.

---

## 2. Đại lục (`CHL-*`)

| ID | Tên (Việt · Hán) | Vị trí (hub grid) | Quy mô bbox (Đ×B) | Linh khí / đặc điểm |
| --- | --- | --- | --- | --- |
| `CHL-TRUNG-LINH` | Trung Linh · TrungLinhĐạiLục | Trung tâm cụm | ~177 × 138 | **Mạch chủ** — tông lớn, thành linh; tranh **Động Thiên Phúc Địa** |
| `CHL-BANG-PHONG` | Băng Phong · BăngPhongĐạiLục | Tây bắc | ~126 × 103 | Lạnh; **Băng–Phong** linh căn; kiếp nạn ngoài trời nặng hơn |
| `CHL-NGOC-LAM` | Ngọc Lâm · NgọcLâmĐạiLục | Đông | ~127 × 113 | Rừng **Mộc**; dược, yêu tộc; linh khí **ổn định** |
| `CHL-HOA-DIEN` | Hỏa Diễm · HỏaDiễmĐạiLục | Tây nam nội địa | ~122 × 94 | **Hỏa** mạch; luyện khí, lò đan; khô nóng |
| `CHL-VAN-HAI` | Vân Hải · VânHảiĐạiLục | Nam | ~147 × 95 | Đảo mây, **Thủy–Phong**; thương lộ phi thuyền |
| `CHL-CUU-LAC` | Cửu Lạc · CửuLạcĐạiLục | Đông nam biển | ~90 × 67 | Cửu sông hội; **Cửu Cửu** truyền thuyết gắn điểm phi thăng |

### 2.1. Châu lục deep (Phase 2b + 2b-ext ✓ — **6/6**)

| CHL | Geo · PNG | `parent_coordinates` | Hub | Phân vùng |
| --- | --- | --- | --- | --- |
| `CHL-TRUNG-LINH` | [`chl-trung-linh.geojson`](geo/chau-luc/chl-trung-linh.geojson) · [`chl-trung-linh.png`](geo/out/chl-trung-linh.png) | `[-79.0, -40.0]` | `LOC-TL-THIEN-QUAN` | **10** `REG-*` + **1** `BRR-*`; ~**100%** |
| `CHL-CUU-LAC` | [`chl-cuu-lac.geojson`](geo/chau-luc/chl-cuu-lac.geojson) · [`chl-cuu-lac.png`](geo/out/chl-cuu-lac.png) | `[214.0, -154.0]` | `LOC-CL-CUU-KHAU` | **9** `REG-*` + **1** `BRR-*`; ~**100%** (`REG-CL-PHAM-KHE` = slot Phàm) |
| `CHL-BANG-PHONG` | [`chl-bang-phong.geojson`](geo/chau-luc/chl-bang-phong.geojson) · [`chl-bang-phong.png`](geo/out/chl-bang-phong.png) | `[-265.0, 124.0]` | `LOC-BP-BANG-TINH` | **9** `REG-*` + **1** `BRR-*`; ~**100%** |
| `CHL-NGOC-LAM` | [`chl-ngoc-lam.geojson`](geo/chau-luc/chl-ngoc-lam.geojson) · [`chl-ngoc-lam.png`](geo/out/chl-ngoc-lam.png) | `[152.0, 66.0]` | `LOC-NL-LAM-TINH` | **11** `REG-*` + **1** `BRR-*`; ~**100%** |
| `CHL-HOA-DIEN` | [`chl-hoa-dien.geojson`](geo/chau-luc/chl-hoa-dien.geojson) · [`chl-hoa-dien.png`](geo/out/chl-hoa-dien.png) | `[-240.0, -129.0]` | `LOC-HD-HOA-QUAN` | **10** `REG-*` + **1** `BRR-*`; ~**100%** |
| `CHL-VAN-HAI` | [`chl-van-hai.geojson`](geo/chau-luc/chl-van-hai.geojson) · [`chl-van-hai.png`](geo/out/chl-van-hai.png) | `[1.0, -208.0]` | `LOC-VH-VAN-CANG` | **10** `REG-*` + **1** `BRR-*`; ~**100%** |

**Canvas:** [`chl-trung-linh`](../../canvas/chl-trung-linh.canvas.json) · [`chl-cuu-lac`](../../canvas/chl-cuu-lac.canvas.json) · [`chl-bang-phong`](../../canvas/chl-bang-phong.canvas.json) · [`chl-ngoc-lam`](../../canvas/chl-ngoc-lam.canvas.json) · [`chl-hoa-dien`](../../canvas/chl-hoa-dien.canvas.json) · [`chl-van-hai`](../../canvas/chl-van-hai.canvas.json)

#### Region exemplar (Phase 2c ✓)

| REG | Geo · PNG | Hub local | Neo chau_luc |
| --- | --- | --- | --- |
| `REG-TL-THIEN-QUAN` | [`reg-tl-thien-quan.geojson`](geo/region/reg-tl-thien-quan.geojson) · [`region-reg-tl-thien-quan.png`](geo/out/region-reg-tl-thien-quan.png) | `LOC-TL-THIEN-QUAN` `[0,0]` | `chl-trung-linh` · `(420,420)` · shared `LOC-TL-THIEN-QUAN` |
| `REG-CL-CUU-KHAU` | [`reg-cl-cuu-khau.geojson`](geo/region/reg-cl-cuu-khau.geojson) · [`region-reg-cl-cuu-khau.png`](geo/out/region-reg-cl-cuu-khau.png) | `LOC-CL-CUU-KHAU` `[0,0]` | `chl-cuu-lac` · `(380,620)` · shared `LOC-CL-CUU-KHAU` |

Bàn cờ generic: [`../../01-region-catalog.md`](../../01-region-catalog.md) § Exemplar region.

**Trung Linh — cụm REG:** Nam (`REG-TL-NAM-VAN`) · Trung (`REG-TL-LINH-HA`, `REG-TL-THIEN-QUAN`, `REG-TL-TAM-TONG`) · Bắc (`REG-TL-BAC-LINH`, `REG-TL-BAC-DONG`) · Tây (`REG-TL-TAY-MACH`, `REG-TL-PHUC-DIA`) · Đông (`REG-TL-DONG-LAM`, `REG-TL-DONG-HAI`) · `BRR-TL-THIEN-LAM` · sông `RIVER-TL-LINH-HA`, `RIVER-TL-DONG-LUU`.

**Cửu Lạc — cụm REG:** Nam (`REG-CL-NAM-HAI`, `REG-CL-LAC-HE`, `REG-CL-LAC-TAM`) · Trung (`REG-CL-CUU-KHAU`, `REG-CL-TAN-TIEN`) · Bắc (`REG-CL-BAC-PHONG` ↔ Ngọc Lâm) · Tây (`REG-CL-PHAM-KHE`, `REG-CL-TAY-DAO`) · Đông (`REG-CL-DONG-LAC`) · `BRR-CL-CUU-SON` · sông `RIVER-CL-CUU-LAC`, `RIVER-CL-LAC-CHI`.

**Băng Phong — cụm REG:** Nam (`REG-BP-NAM-DONG`, `REG-BP-NAM-PHONG` → Trung Linh) · Trung (`REG-BP-PHONG-COC`, `REG-BP-LINH-BANG`) · Bắc (`REG-BP-BANG-TINH`, `REG-BP-BAC-HUYEN`) · Tây (`REG-BP-TAY-BANG`) · Đông (`REG-BP-HAN-UYEN`, `REG-BP-DONG-HAN`) · `BRR-BP-VAN-PHONG` · `RIVER-BP-LINH-BANG`, `ROUTE-BP-DONG-TRUNG-LINH`.

**Ngọc Lâm — cụm REG:** Nam (`REG-NL-NAM-HAI`) · Trung (`REG-NL-LAM-TINH`, `REG-NL-TRUNG-DU`, `REG-NL-BICH-HO`, `REG-NL-THAO-COC`) · Bắc (`REG-NL-BAC-PHONG` ↔ Cửu Lạc) · Tây (`REG-NL-TAY-LAM`, `REG-NL-THAN-MOC`, `REG-NL-CUU-VIEN`) · Đông (`REG-NL-DONG-LINH`, `REG-NL-NGOAI-VI`) · `BRR-NL-THAN-SON` · `RIVER-NL-BICH-HO`, `ROUTE-NL-BAC-CUU-LAC`.

**Hỏa Diễm — cụm REG:** Nam (`REG-HD-NAM-VIEM`) · Trung (`REG-HD-HOA-QUAN`, `REG-HD-VIEM-QUAN`, `REG-HD-TAN-DIA`, `REG-HD-VIEM-TAM`) · Bắc (`REG-HD-BAC-LO`, `REG-HD-BAC-HAN` ↔ Băng Phong lore) · Tây (`REG-HD-TAY-HOANG`) · Đông (`REG-HD-DONG-MACH` → Trung Linh Tây Mạch, `REG-HD-NGOAI-HOA`) · `BRR-HD-LIET-DUONG` · `RIVER-HD-VIEM-HE`, `ROUTE-HD-TAY-TRUNG-LINH`.

**Vân Hải — cụm REG:** Bắc (`REG-VH-BAC-VAN` ↔ Trung Linh Nam Vân) · Trung (`REG-VH-VAN-CANG`, `REG-VH-DAO-MOC`, `REG-VH-LINH-DAM`) · Nam (`REG-VH-HAI-MA`, `REG-VH-PHONG-BAO`) · Tây/Đông (`REG-VH-TAY-DAO`, `REG-VH-DONG-DAO`, `REG-VH-VAN-HAI`) · `BRR-VH-HAI-SON` · `RIVER-VH-VAN-LUU`, `ROUTE-VH-BAC-NAM-VAN`.

---

## 3. Lịch sử (sketch — nhân quả)

Chi tiết tinh cầu → [`history/00-overview.md`](history/00-overview.md).

| Thời kỳ | Sự kiện | Di sản hiện tại |
| --- | --- | --- |
| **Thượng cổ** | Tu sĩ **Tiên hạ phàm** (sang Phàm) + **Phàm phi thăng** vào Càn Nguyên — tranh mạch | Di tích **Cửu Lạc**; phong ấn crack Phàm–Linh **phía dưới lore** |
| **Trung cổ** | **Tam tông** chia Trung Linh; chiến **Hỏa–Băng** (Hỏa Diễm vs Băng Phong) | Ranh giới `REG-*` mang thù; Ma patch Vân Hải |
| **Cận cổ** | Giới bích Linh–Tiên **cứng**; phi thăng thành **hiếm** | Monopoly **linh thạch hạng thượng**; đan dược độc quyền |
| **Hiện tại** | Kim Hà mở **thương mạch liên tinh** (chưa tới Càn Nguyên thường xuyên) | Kinh tế **linh thạch + công pháp**; tu sĩ Phàm lên Linh = chuyển giới diện |

---

## 4. Tài nguyên & linh mạch — ai thu

| Tài nguyên | Mật độ (Càn Nguyên) | Khai thác / monopolize |
| --- | --- | --- |
| **Linh thạch hạ–trung** | Cao (Trung Linh, Hỏa Diễm mỏ) | Tông **thuế 20–35%** + hộ thương Vân Hải |
| **Linh thạch thượng / linh nguyên** | Trung bình | Gia tộc Trung Linh; **Kim Hà** nhập khẩu |
| **Linh thảo · đan dược** | Cao (Ngọc Lâm, Mộc Dương neighbor nhập) | Đan các + **hội thương** |
| **Linh mạch (Động phủ)** | Hiếm | **Tông chiếm** — chiến tranh mạch = arc-scale |
| **Công pháp / di cổ** | Hiếm | Bí cảnh `REG-*`, Vực Ngoại |

**Logic mạch:** Mạch **nhánh** nuôi thành; mạch **gốc** gắn **Thiên địa dị tượng** — đụng gốc = kích hoạt Nhân quả / phe (depth engine, không beat).

---

## 5. Invariant (planet · Càn Nguyên)

1. **Main geo** Phase 2a = **`TH-LINH-CAN-NGUYEN`** trên tinh cầu này — khác void / bbox **`TH-PHAM-BICH-LAC`**.
2. **Linh khí đủ** cho đại tu đường tới **Độ Kiếp** **trong cùng giới**; **Tiên** = giới kế sau Cửu Cửu.
3. **Linh ↔ Tiên** = giới bích song song — phi thăng không phải truyền tống tức thời trên bản đồ này.
4. **Không** dùng tên Phàm canon cho lục Linh.
5. **Geo read-only** cho prose; chau_luc/region qua world-builder 2b–2c.

---

## 6. Expansion slots

| ID slot | Tầng | Nội dung (logic sẵn) |
| --- | --- | --- |
| **E-LINH-NEIGHBOR-HA** | `(chưa lộ)` | **Kim Hà** — phi thuyền liên tinh; payoff = kinh tế / gián điệp cross-TH |
| **E-LINH-PHAM-CRACK** | `(MC phase 1 biết)` | **Khe Phàm–Linh** dưới Cửu Lạc — một chiều hoặc **đôi** có giá |
| **E-LINH-ASCENSION-GATE** | `(hidden_logic)` | **Cửu Lạc Cửu Khẩu** — điểm Cửu Cửu **không** cố định trên lục; di chuyển theo chu kỳ |
| **E-LINH-MA-PATCH-VH** | `(hidden_logic)` | Ma khí **Vân Hải** đáy biển — mảnh, không Ma Giới đầy đủ |
| **E-LINH-HUYEN-AM** | `(chưa lộ)` | Tinh hà **Huyền Âm** — âm khí tràn; payoff = Minh / luân hồi hook Phase 5 |

---

## 7. Hook → arc xa (gợi ý)

| Manh mối | Câu hỏi | Ràng buộc payoff |
| --- | --- | --- |
| Tam tông Trung Linh | Ai nắm **mạch gốc**? | Phải khớp **kinh tế linh thạch** |
| Hỏa–Băng chiến cổ | Hòa giải hay diệt? | Theme xám — **không** phe thuần ác |
| Thương đội Kim Hà | Thuế hay cấm? | Liên tinh = **có sổ** — sync neighbor lore |
| Tản Tiên truyền thuyết Cửu Lạc | Còn ý thức? | Vẫn **Linh Giới** trừ lore ledger khác |

---

*World-builder · T-foundation-linh-2a–2c · 2b-ext 6/6 chau_luc · 2026-10-22*
