# Phàm Giới — Region catalog

> **Mục đích:** Liệt kê `REG-*` theo đại lục — đối chiếu stub vs **`chau_luc`** (Phase 1b) vs **`region/*`** (Phase 1c).

**Atlas:** [`00-world-atlas.md`](00-world-atlas.md) · **Tinh hà:** [`planets/bich-lac-tinh/geo/00-tinh-ha.geojson`](planets/bich-lac-tinh/geo/00-tinh-ha.geojson) · **Châu lục:** [`planets/bich-lac-tinh/continents/00-continent-index.md`](planets/bich-lac-tinh/continents/00-continent-index.md)

**Chú thích cột Geo:** `chau_luc` = polygon trong file lục; `region` = file `planets/bich-lac-tinh/geo/region/reg-*.geojson` (1c); `—` = stub catalog / chưa vẽ.

---

## [CHL-XICH-HA (Xích Hạ)](planets/bich-lac-tinh/continents/xich-ha/00-overview.md) — chau_luc **done**

File: [`planets/bich-lac-tinh/geo/chau-luc/chl-xich-ha.geojson`](planets/bich-lac-tinh/geo/chau-luc/chl-xich-ha.geojson) · Hub: `LOC-XH-LAC-DUONG`

| REG ID | Tên (geo) | Vai trò (tóm) | Geo |
| --- | --- | --- | --- |
| `REG-XH-NAM-HAI` | Nam Hải Quan | Thuế nhập, cửa biển nam | chau_luc |
| `REG-XH-NAM-CAN` | Nam Cạn | Nội địa khô, mỏ cạn | chau_luc |
| `REG-XH-XICH-NGUYEN` | Xích Nguyên Bình | Bình địa trung | chau_luc |
| `REG-XH-DE-DO` | Đế Đô Lạc Dương | Trung ương phàm | chau_luc · **region geo: done** → [`reg-xh-de-do.geojson`](planets/bich-lac-tinh/geo/region/reg-xh-de-do.geojson) |
| `REG-XH-BAC-HAN` | Bắc Hạn | Sa mạc bắc | chau_luc |
| `REG-XH-HOANG-TAY` | Hoang Tây | Biên quan tây | chau_luc |
| `REG-XH-TAY-SON` | Tây Sơn Tự | Sơn môn | chau_luc |
| `REG-XH-DONG-NOI` | Đông Nội | Đồi phù sa | chau_luc |
| `REG-XH-DONG-HAI` | Đông Hải An | Ven biển đông | chau_luc |
| `BRR-XH-HONG-LIEN` | Dãy Hồng Liên | Barrier (polygon) | chau_luc |

*Stub cũ (catalog 1a) `REG-XH-XICH-CO`, `REG-XH-HA-QUAN`, `REG-XH-LIEU-THANH` — **không** dùng trong geo 1b; gộp logic vào cụm Nam/Trung trên khi cần region deep.*

---

## [CHL-TAM-NGUYEN (Tam Nguyên)](planets/bich-lac-tinh/continents/tam-nguyen/00-overview.md) — chau_luc **done**

File: [`planets/bich-lac-tinh/geo/chau-luc/chl-tam-nguyen.geojson`](planets/bich-lac-tinh/geo/chau-luc/chl-tam-nguyen.geojson) · Hub: `LOC-TN-DONG-HAI`

| REG ID | Tên (geo) | Vai trò (tóm) | Geo |
| --- | --- | --- | --- |
| `REG-TN-NAM-HAI` | Nam Hải | Cửa biển nam | chau_luc |
| `REG-TN-NAM-BINH` | Nam Bình Thôn | Ven đồng nam | chau_luc |
| `REG-TN-TRUNG-NGUYEN` | Trung Nguyên Tam Quốc | Chính trị trung tâm | chau_luc · **region geo: done** → [`reg-tn-trung-nguyen.geojson`](planets/bich-lac-tinh/geo/region/reg-tn-trung-nguyen.geojson) |
| `REG-TN-BAC-HA` | Bắc Hạ | Vực bắc | chau_luc |
| `REG-TN-TAY-CAN` | Tây Cạn | Biên tây | chau_luc |
| `REG-TN-TAY-HA` | Tây Hạ | Đồi tây nam | chau_luc |
| `REG-TN-DONG-LAM` | Đông Lâm | Rừng đông | chau_luc |
| `REG-TN-DONG-HAI` | Đông Hải Cảng | Thương cảng (hub) | chau_luc |
| `REG-TN-TAM-GIAO` | Tam Giáo Sơn | Phế địa / dungeon hook | chau_luc |
| `BRR-TN-NGUU-SON` | Dãy Ngưu Sơn | Barrier (polygon) | chau_luc |

*Stub cũ `REG-TN-TAM-HE`, `REG-TN-THIEN-TRU`, `REG-TN-VUONG-THANH`, `REG-TN-LINH-VIEN` — thay bằng id geo trên; payoff Thiên Trụ/Linh Viên gắn `REG-TN-TAM-GIAO` / Trung Nguyên khi 1c.*

---

## [CHL-HAN-PHUONG (Hàn Phương)](planets/bich-lac-tinh/continents/han-phuong/00-overview.md) — chau_luc **done**

File: [`planets/bich-lac-tinh/geo/chau-luc/chl-han-phuong.geojson`](planets/bich-lac-tinh/geo/chau-luc/chl-han-phuong.geojson) · Hub: `LOC-HP-HAN-TINH` · Parent SW: `[-356, -32]`

| REG ID | Tên (geo) | Vai trò (tóm) | Geo |
| --- | --- | --- | --- |
| `REG-HP-NAM-CAN` | Nam Cạn · rìa ấm | Biên nam · giao thương hiếm | chau_luc · **region geo: done** → [`reg-hp-nam-can.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-nam-can.geojson) |
| `REG-HP-BANG-HA` | Băng Hà | Sông đóng · lộ ven băng | chau_luc · **region geo: done** → [`reg-hp-bang-ha.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-bang-ha.geojson) |
| `REG-HP-NOI-DIA` | Nội Địa | Đồng băng nam | chau_luc · **region geo: done** → [`reg-hp-noi-dia.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-noi-dia.geojson) |
| `REG-HP-TUYET-LAM` | Tuyết Lâm | Rừng băng | chau_luc · **region geo: done** → [`reg-hp-tuyet-lam.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-tuyet-lam.geojson) |
| `REG-HP-PHONG-MO` | Phong Mộ Cốc | Di tích phong ấn `(hook)` | chau_luc · **region geo: done** → [`reg-hp-phong-mo.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-phong-mo.geojson) |
| `REG-HP-BANG-YUAN` | Băng Nguyên | Mạch băng **kiệt** · Luyện Thể | chau_luc · **region geo: done** → [`reg-hp-bang-yuan.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-bang-yuan.geojson) |
| `REG-HP-HAN-TINH` | Hàn Tinh Quan | Thành cực bắc · phàm quốc | chau_luc · **region geo: done** → [`reg-hp-han-tinh.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-han-tinh.geojson) |
| `REG-HP-BAC-HUYEN` | Bắc Huyền | Đại vực băng | chau_luc · **region geo: done** → [`reg-hp-bac-huyen.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-bac-huyen.geojson) |
| `REG-HP-TAY-PHONG` | Tây Phong | Biên tây | chau_luc · **region geo: done** → [`reg-hp-tay-phong.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-tay-phong.geojson) |
| `REG-HP-DONG-HUYEN` | Đông Huyền | Địa đông · `(mc_phase1)` | chau_luc · **region geo: done** → [`reg-hp-dong-huyen.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-dong-huyen.geojson) |
| `BRR-HP-HAN-SON` | Dãy Hàn Sơn | Barrier (polygon) | chau_luc · **region geo: done** → [`reg-hp-han-son.geojson`](planets/bich-lac-tinh/geo/region/reg-hp-han-son.geojson) |

*Point phụ:* `LOC-HP-PHONG-MO` · Sông: `RIVER-HP-BANG-HA`, `RIVER-HP-HAN-MACH`.*

---

## [CHL-PHU-TAO (Phù Tảo)](planets/bich-lac-tinh/continents/phu-tao/00-overview.md) — chau_luc **done**

File: [`planets/bich-lac-tinh/geo/chau-luc/chl-phu-tao.geojson`](planets/bich-lac-tinh/geo/chau-luc/chl-phu-tao.geojson) · Hub: `LOC-PT-PHU-TRAN` · Parent SW: `[-160, 104]`

| REG ID | Tên (geo) | Vai trò (tóm) | Geo |
| --- | --- | --- | --- |
| `REG-PT-NAM-HA` | Nam Hải | Ven đầm phía nam | chau_luc · **region geo: done** → [`reg-pt-nam-ha.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-nam-ha.geojson) |
| `REG-PT-DAO-LAM` | Đảo Lam | Quần đảo nổi · linh thảo sơ | chau_luc · **region geo: done** → [`reg-pt-dao-lam.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-dao-lam.geojson) |
| `REG-PT-NAM-BINH` | Nam Bình | Đê ven nam | chau_luc · **region geo: done** → [`reg-pt-nam-binh.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-nam-binh.geojson) |
| `REG-PT-TRUNG-DAM` | Trung Đầm | Đại trũng | chau_luc · **region geo: done** → [`reg-pt-trung-dam.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-trung-dam.geojson) |
| `REG-PT-PHU-TRAN` | Phù Trấn | Chợ dược phàm (hub) | chau_luc · **region geo: done** → [`reg-pt-phu-tran.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-phu-tran.geojson) |
| `REG-PT-NGOAI-DAO` | Ngoại Đảo | Đảo ngoài | chau_luc · **region geo: done** → [`reg-pt-ngoai-dao.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-ngoai-dao.geojson) |
| `REG-PT-BAC-MANG` | Bắc Mang | Biển sậy bắc | chau_luc · **region geo: done** → [`reg-pt-bac-mang.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-bac-mang.geojson) |
| `REG-PT-TAY-LAM` | Tây Lâm | Rừng đầm tây | chau_luc · **region geo: done** → [`reg-pt-tay-lam.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-tay-lam.geojson) |
| `REG-PT-KHE-U` | Khe U | Sương độc · dược quý `(hook)` | chau_luc · **region geo: done** → [`reg-pt-khe-u.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-khe-u.geojson) |
| `REG-PT-DONG-U` | Đông U | Sương đông | chau_luc · **region geo: done** → [`reg-pt-dong-u.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-dong-u.geojson) |
| `BRR-PT-LOI-DI` | Dãy Lôi Đê | Đê khô xuyên đầm | chau_luc · **region geo: done** → [`reg-pt-loi-di.geojson`](planets/bich-lac-tinh/geo/region/reg-pt-loi-di.geojson) |

*Point phụ:* `LOC-PT-KHE-U` · Sông: `RIVER-PT-DAM-LUU`, `RIVER-PT-KHE-U`.*

---

## [CHL-LO-HANG (Lô Hàng)](planets/bich-lac-tinh/continents/lo-hang/00-overview.md) — chau_luc **done**

File: [`planets/bich-lac-tinh/geo/chau-luc/chl-lo-hang.geojson`](planets/bich-lac-tinh/geo/chau-luc/chl-lo-hang.geojson) · Hub: `LOC-LH-CANG-TIEN` · Parent SW: `[188, -37]`

| REG ID | Tên (geo) | Vai trò (tóm) | Geo |
| --- | --- | --- | --- |
| `REG-LH-NAM-HAI` | Nam Hải | Hư không hải · cửa nam | chau_luc · **region geo: done** → [`reg-lh-nam-hai.geojson`](planets/bich-lac-tinh/geo/region/reg-lh-nam-hai.geojson) |
| `REG-LH-CANG-TIEN` | Cảng Tiên Sa | Hải thương · thuế quan (hub) | chau_luc · **region geo: done** → [`reg-lh-cang-tien.geojson`](planets/bich-lac-tinh/geo/region/reg-lh-cang-tien.geojson) |
| `REG-LH-TRUNG-DAO` | Trung Đảo | Đảo chính | chau_luc · **region geo: done** → [`reg-lh-trung-dao.geojson`](planets/bich-lac-tinh/geo/region/reg-lh-trung-dao.geojson) |
| `REG-LH-QUAN-DAO` | Quần Đảo Lô | Đảo nhỏ · hải tặc | chau_luc · **region geo: done** → [`reg-lh-quan-dao.geojson`](planets/bich-lac-tinh/geo/region/reg-lh-quan-dao.geojson) |
| `REG-LH-HAI-PHONG` | Hải Phong | Phong ấn tu Linh `(hook)` | chau_luc · **region geo: done** → [`reg-lh-hai-phong.geojson`](planets/bich-lac-tinh/geo/region/reg-lh-hai-phong.geojson) |
| `REG-LH-TAY-AN` | Tây An | Hải vực yên | chau_luc · **region geo: done** → [`reg-lh-tay-an.geojson`](planets/bich-lac-tinh/geo/region/reg-lh-tay-an.geojson) |
| `REG-LH-BAC-HAI` | Bắc Hải | Cửa bắc · nối Xích Hạ | chau_luc · **region geo: done** → [`reg-lh-bac-hai.geojson`](planets/bich-lac-tinh/geo/region/reg-lh-bac-hai.geojson) |
| `REG-LH-DONG-LUU` | Đông Lưu | Hành lang thương · trạm neo | chau_luc · **region geo: done** → [`reg-lh-dong-luu.geojson`](planets/bich-lac-tinh/geo/region/reg-lh-dong-luu.geojson) |
| `REG-LH-LO-QUAN` | Lô Quan | Nội cảng · hộ thương | chau_luc · **region geo: done** → [`reg-lh-lo-quan.geojson`](planets/bich-lac-tinh/geo/region/reg-lh-lo-quan.geojson) |
| `BRR-LH-LONG-QUY` | Dãy Long Quy | Barrier (polygon) | chau_luc · **region geo: done** → [`reg-lh-long-quy.geojson`](planets/bich-lac-tinh/geo/region/reg-lh-long-quy.geojson) |

*Point phụ:* `LOC-LH-THUONG-HOI` · Hải lưu: `RIVER-LH-THUONG-LUU`, `RIVER-LH-NAM-LUU`.*

---

## [CHL-TAN-MO (Tàn Mộ)](planets/bich-lac-tinh/continents/tan-mo/00-overview.md) — chau_luc **done**

File: [`planets/bich-lac-tinh/geo/chau-luc/chl-tan-mo.geojson`](planets/bich-lac-tinh/geo/chau-luc/chl-tan-mo.geojson) · Hub: `LOC-TM-CO-TU` · Parent SW: `[-205, -248]`

| REG ID | Tên (geo) | Vai trò (tóm) | Geo |
| --- | --- | --- | --- |
| `REG-TM-NAM-QUAN` | Nam Quan | Ải nam · thu phí lữ khách | chau_luc · **region geo: done** → [`reg-tm-nam-quan.geojson`](planets/bich-lac-tinh/geo/region/reg-tm-nam-quan.geojson) |
| `REG-TM-SA-HAI` | Sa Hải | Đại sa mạc · Cổ khí vụn | chau_luc · **region geo: done** → [`reg-tm-sa-hai.geojson`](planets/bich-lac-tinh/geo/region/reg-tm-sa-hai.geojson) |
| `REG-TM-CO-TU` | Cổ Tu | Phi thăng thất bại (hub) | chau_luc · **region geo: done** → [`reg-tm-co-tu.geojson`](planets/bich-lac-tinh/geo/region/reg-tm-co-tu.geojson) |
| `REG-TM-KHE-GIOI` | Khe Giới | Crack Phàm–Linh · barrier `(E-PHAM-CRACK-LINH)` | chau_luc · **region geo: done** → [`reg-tm-khe-gioi.geojson`](planets/bich-lac-tinh/geo/region/reg-tm-khe-gioi.geojson) |
| `REG-TM-TAY-MA` | Tây Ma | Vệt Ma khí `(E-PHAM-MA-PATCH)` | chau_luc · **region geo: done** → [`reg-tm-tay-ma.geojson`](planets/bich-lac-tinh/geo/region/reg-tm-tay-ma.geojson) |
| `REG-TM-BAC-HAN` | Bắc Hạn | Rìa bắc | chau_luc · **region geo: done** → [`reg-tm-bac-han.geojson`](planets/bich-lac-tinh/geo/region/reg-tm-bac-han.geojson) |
| `REG-TM-DONG-OA` | Đông Oa | Ốc đảo · phe thu gom | chau_luc · **region geo: done** → [`reg-tm-dong-oa.geojson`](planets/bich-lac-tinh/geo/region/reg-tm-dong-oa.geojson) |
| `REG-TM-CO-TA` | Cổ Ta | Phế tháp lang thang | chau_luc · **region geo: done** → [`reg-tm-co-ta.geojson`](planets/bich-lac-tinh/geo/region/reg-tm-co-ta.geojson) |
| `REG-TM-HAN-COC` | Hạn Cốc | Cốc khô | chau_luc · **region geo: done** → [`reg-tm-han-coc.geojson`](planets/bich-lac-tinh/geo/region/reg-tm-han-coc.geojson) |
| `BRR-TM-TIET-LO` | Dãy Tiết Lộ | Barrier (polygon) | chau_luc |

*Point phụ:* `LOC-TM-KHE-GIOI`, `LOC-TM-OA-TUYEN` · Cố đô: `RIVER-TM-CUU-HA`, `RIVER-TM-OA-LUU`.*

---

## Phase tiếp

- **1c:** **`done`** — exemplar `REG-XH-DE-DO`, `REG-TN-TRUNG-NGUYEN` + [`02-tieu-cuc-index.md`](02-tieu-cuc-index.md).
- **1d:** **`done`** — Tàn Mộ deep `REG-TM-KHE-GIOI`, `REG-TM-CO-TU` + micro stub trong `02-tieu-cuc-index.md`.
- **1e:** **`done`** — toàn bộ 9 REG `CHL-TAN-MO` có `planets/bich-lac-tinh/geo/region/reg-tm-*.geojson` + PNG.
- **1b-ext:** **`done`** — 6/6 lục `chau_luc/*` (ext-A: Hàn Phương · Phù Tảo; ext-B: Lô Hàng · Tàn Mộ).
- **Micro:** theo slot trong `02-tieu-cuc-index.md` khi arc lock.

- **1f:** **`done`** — Hàn Phương · Phù Tảo · Lô Hàng: 32× `planets/bich-lac-tinh/geo/region/reg-{hp,pt,lh}-*.geojson` + PNG; script [`scripts/build_pham_regions_1f.py`](scripts/build_pham_regions_1f.py).

*Cập nhật · T-foundation-pham-1f · 2026-09-18*
