# Foundation Canon World — campaign tracker

| Trường | Giá trị |
| --- | --- |
| **work_slug** | `foundation-canon` |
| **logic_root** | `foundation/logic/world/` |
| **Pipeline** | Foundation Logic (geo + atlas) — **không** thuộc `projects/` |
| **lifecycle** | `active` |
| **Cập nhật** | 2026-09-18 |

## Mục tiêu

Instantiate **bốn giới song song** (Luật 6 — `foundation/core/02-world-laws-lore-core.md`) + giới phụ (markdown). Mỗi giới chính: cây `realms/<slug>/` theo convention GeoJSON v2 (`foundation/logic/00-geojson-world-map-convention.md`).

**Cấm:** Sao chép tên/địa danh từ `projects/archive/`; vi phạm `(invariant)` Core 02/03.

---

## Phases

| Phase | Phạm vi | Trạng thái |
| --- | --- | --- |
| **0** | Scaffold + `00-cosmos-index.md` + `status.md` + layout `realms/*` | `done` (orchestrator) |
| **1** | **Phàm Giới** — 1 tinh hà chủ; tinh_ha geo ≥5 CHL; atlas; PNG | `done` |
| **1b** | Phàm — 2 châu lục `chau_luc` deep (8–12 REG/file) | **`done`** |
| **1c** | Phàm — exemplar `region/*` (1–2 REG chính) | **`done`** |
| **1d** | Phàm — region deep **Tàn Mộ** (`REG-TM-KHE-GIOI` · `REG-TM-CO-TU`) | **`done`** |
| **1e** | Phàm — **toàn bộ** region trên `chl-tan-mo` (7 REG còn lại) | **`done`** |
| **2** | **Linh Giới** — 3–5 tinh hà (1 main); tinh_ha + atlas | **`done`** |
| **2b** | Linh — chau_luc deep (2 lục ưu tiên) | **`done`** |
| **2b-ext** | Linh — **6/6** chau_luc (4 lục còn: Băng Phong · Ngọc Lâm · Hỏa Diễm · Vân Hải) | **`done`** |
| **2c** | Linh — exemplar `region/*` | **`done`** |
| **3** | **Tiên Giới** — 5–8 tinh hà | **`done`** (3a) |
| **3b** | Tiên — chau_luc deep (2 lục ưu tiên) | **`done`** |
| **3b-ext** | Tiên — **6/6** chau_luc (4 lục còn: Ngự Long · Kim Hoa · Trần Lạc · Huyên Băng) | **`done`** |
| **3c** | Tiên — exemplar `region/*` | **`done`** |
| **4** | **Thần Giới** — 8–12 tinh hà; Thánh-tier liên tinh hà (lore) | **`done`** (4a) |
| **4b** | Thần — chau_luc deep (2 lục ưu tiên) | **`done`** |
| **4b-ext** | Thần — **7/7** chau_luc (4 lục còn: Kiếm Lôi · Hồn Vực · Sinh Tiêu · Cửu Phong; **Huyền Băng** đã có) | **`done`** |
| **4c** | Thần — exemplar `region/*` | **`done`** |
| **5** | Giới phụ: Minh · Ma/Yêu · Vực Ngoại · Tiểu Thiên Thế Giới · stub Bí cảnh / Chư Thiên | **`done`** |
| **6** | Exemplar region/micro cross-realm (stub → geo) | `backlog` |
| **7** | **Region deep** — mọi CHL chưa có `geo/region/reg-*.geojson` (neo hub lục) | **`in_progress`** |
| **7-P / 1f** | Phàm — Hàn Phương · Phù Tảo · Lô Hàng (3 lục, 32 REG+BRR) | **`done`** |
| **7-L / 2d** | Linh — Băng Phong · Ngọc Lâm · Hỏa Diễm · Vân Hải | `planned` |
| **7-T / 3d** | Tiên — Ngự Long · Kim Hoa · Trần Lạc · Huyên Băng | `planned` |
| **7-H / 4d** | Thần — Kiếm Lôi · Hồn Vực · Sinh Tiêu · Cửu Phong | `planned` |

### Phase 7 — backlog CHL (region geo chưa có)

**Skip (exemplar only hoặc full):** Phàm `chl-xich-ha`, `chl-tam-nguyen`, `chl-tan-mo` (9/9), `chl-han-phuong` · `chl-phu-tao` · `chl-lo-hang` (32/32); Linh `chl-trung-linh`, `chl-cuu-lac`; Tiên `chl-trung-tien`, `chl-thanh-van`; Thần `chl-trung-than`, `chl-van-phap`.

| Lane | CHL slug | REG (catalog) | Hub | Task ID | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| **P** | `chl-han-phuong` | 10 REG + `BRR-HP-HAN-SON` | `LOC-HP-HAN-TINH` | **T-foundation-pham-1f** | **`done`** |
| **P** | `chl-phu-tao` | 10 REG + `BRR-PT-LOI-DI` | `LOC-PT-PHU-TRAN` | **T-foundation-pham-1f** | **`done`** |
| **P** | `chl-lo-hang` | 9 REG + `BRR-LH-LONG-QUY` | `LOC-LH-CANG-TIEN` | **T-foundation-pham-1f** | **`done`** |
| L | `chl-bang-phong` | `REG-BP-*` | (catalog) | T-foundation-linh-2d | `planned` |
| L | `chl-ngoc-lam` | `REG-NL-*` | (catalog) | T-foundation-linh-2d | `planned` |
| L | `chl-hoa-dien` | `REG-HD-*` | (catalog) | T-foundation-linh-2d | `planned` |
| L | `chl-van-hai` | `REG-VH-*` | (catalog) | T-foundation-linh-2d | `planned` |
| T | `chl-ngu-long` | `REG-NL-*` (Tiên) | (catalog) | T-foundation-tien-3d | `planned` |
| T | `chl-kim-hoa` | `REG-KH-*` | (catalog) | T-foundation-tien-3d | `planned` |
| T | `chl-tran-lac` | `REG-TL-*` | (catalog) | T-foundation-tien-3d | `planned` |
| T | `chl-huyen-bang` | `REG-HB-*` (Tiên) | (catalog) | T-foundation-tien-3d | `planned` |
| H | `chl-kiem-loi` | `REG-KL-*` | (catalog) | T-foundation-than-4d | `planned` |
| H | `chl-hon-vuc` | `REG-HV-*` | (catalog) | T-foundation-than-4d | `planned` |
| H | `chl-sinh-tieu` | `REG-ST-*` | (catalog) | T-foundation-than-4d | `planned` |
| H | `chl-huyen-bang` | `REG-HC-*` (Thần — file khác Tiên) | (catalog) | T-foundation-than-4d | `planned` |
| H | `chl-cuu-phong` | `REG-CP-*` | (catalog) | T-foundation-than-4d | `planned` |

*Sau batch 1f (Lane P): còn **13 CHL** (4L + 4T + 5H) — Phàm region deep **6/6** chau_luc.*

---

## Task queue

| ID | Agent | Trạng thái | Artifact kỳ vọng |
| --- | --- | --- | --- |
| **T-foundation-world-0** | orchestrator | `done` | `status.md`, `00-cosmos-index.md`, `realms/*/` layout |
| **T-foundation-pham-1a** | `world-builder` | **`done`** | `realms/pham-gioi/00-world-atlas.md`, `01-region-catalog.md`, `geo/00-tinh-ha.geojson`, `geo/out/00-tinh-ha.png` |
| **T-foundation-pham-1b** | `world-builder` | **`done`** | `chl-xich-ha` + `chl-tam-nguyen` geo/canvas/PNG; atlas + catalog |
| **T-foundation-pham-1c** | `world-builder` | **`done`** | `reg-xh-de-do` + `reg-tn-trung-nguyen` geo/PNG; atlas §2.2; `02-tieu-cuc-index.md` |
| **T-foundation-pham-1b-ext-A** | `world-builder` | **`done`** | `chl-han-phuong` + `chl-phu-tao` chau_luc/canvas/PNG; atlas §2.1; catalog |
| **T-foundation-pham-1b-ext-B** | `world-builder` | **`done`** | `chl-lo-hang` + `chl-tan-mo` chau_luc/canvas/PNG; atlas §2.1; catalog |
| **T-foundation-pham-1d** | `world-builder` | **`done`** | `reg-tm-khe-gioi` + `reg-tm-co-tu` geo/PNG; atlas §2.2; catalog; `02-tieu-cuc-index.md` |
| **T-foundation-pham-1e** | `world-builder` | **`done`** | 7× `reg-tm-*.geojson` + PNG; full CHL-TAN-MO region coverage (9/9 REG) |
| **T-foundation-linh-2a** | `world-builder` | **`done`** | `realms/linh-gioi/` atlas + 4 TH doc + main `00-tinh-ha.geojson` (6 CHL) + PNG |
| **T-foundation-linh-2b** | `world-builder` | **`done`** | `chl-trung-linh` + `chl-cuu-lac` chau_luc/canvas/PNG; atlas §2.1; catalog |
| **T-foundation-linh-2b-ext** | `world-builder` | **`done`** | 4× `chl-bang-phong` · `chl-ngoc-lam` · `chl-hoa-dien` · `chl-van-hai` (geo/canvas/PNG); atlas §2.1; catalog stub→✓; **6/6** chau_luc parity Phàm |
| **T-foundation-linh-2c** | `world-builder` | **`done`** | `reg-tl-thien-quan` + `reg-cl-cuu-khau` geo/PNG; atlas §2.2; `02-tieu-cuc-index.md` |
| **T-foundation-tien-3a** | `world-builder` | **`done`** | `realms/tien-gioi/00-world-atlas.md`, `01-region-catalog.md`, `geo/00-tinh-ha.geojson` (6 CHL), `geo/out/00-tinh-ha.png` |
| **T-foundation-tien-3b** | `world-builder` | **`done`** | `chl-trung-tien` + `chl-thanh-van` chau_luc/canvas/PNG; atlas §2.1; catalog |
| **T-foundation-tien-3c** | `world-builder` | **`done`** | `reg-tt-tien-quan` + `reg-tv-van-cung` + PNG; bàn cờ catalog |
| **T-foundation-tien-3b-ext** | `world-builder` | **`done`** | 4× `chl-ngu-long` · `chl-kim-hoa` · `chl-tran-lac` · `chl-huyen-bang` (geo/canvas/PNG); atlas §2.1; catalog stub→✓; **6/6** parity Phàm/Linh |
| **T-foundation-than-4a** | `world-builder` | **`done`** | `than-gioi/` 10 TH doc + main `00-tinh-ha` (7 CHL) + PNG |
| **T-foundation-than-4b** | `world-builder` | **`done`** | `chl-trung-than` + `chl-van-phap` chau_luc/canvas/PNG; atlas §2.1; catalog |
| **T-foundation-than-4c** | `world-builder` | **`done`** | `reg-rt-than-quan` + `reg-vp-phap-dien` + PNG; atlas §2.1 exemplar; `02-tieu-cuc-index.md`; catalog bàn cờ |
| **T-foundation-than-4b-ext** | `world-builder` | **`done`** | 4× `chl-kiem-loi` · `chl-hon-vuc` · `chl-sinh-tieu` · `chl-cuu-phong` (geo/canvas/PNG); atlas §2.1 **7/7**; catalog stub→✓; fix `CHL-KIEM-LOI` tinh_ha shell |
| **T-foundation-subsidiary-5** | `world-builder` | **`done`** | [`06-subsidiary-realms.md`](06-subsidiary-realms.md) · `00-cosmos-index.md` §6 ✓ |
| **T-foundation-pham-1f** | `world-builder` | **`done`** | 32× `reg-{hp,pt,lh}-*.geojson` + PNG; atlas §2.2; catalog **region geo: done**; `02-tieu-cuc-index.md` stub hub/hook; [`scripts/build_pham_regions_1f.py`](../realms/pham-gioi/scripts/build_pham_regions_1f.py) |

---

## Parallel lanes (tùy chọn sau Phase 1a)

Khi scaffold ổn, có thể chạy **một task / giới** song song (4 agent), mỗi lane độc lập dưới `realms/<giới>/`:

- Lane **P** — Phàm (`pham-gioi`)
- Lane **L** — Linh (`linh-gioi`)
- Lane **T** — Tiên (`tien-gioi`)
- Lane **H** — Thần (`than-gioi`)

Orchestrator: **một delegate / lượt** trừ khi user bật parallel — ghi lane trong bảng trên.

---

## Cursor

- **Foundation world MVP (Phase 0–5):** **complete** — bốn giới geo/atlas + giới phụ markdown [`06-subsidiary-realms.md`](06-subsidiary-realms.md).
- **Phàm mở rộng:** **6/6** lục `chau_luc/*` **`done`**. **Tàn Mộ regions:** **9/9 REG** **`done`** (1d Khe Giới · Cổ Tu; 1e bảy vùng còn lại — [world-builder](0bc448ba-95ac-4d2f-a66f-d1af52273f66)). Tái sinh TM: `realms/pham-gioi/scripts/build_tm_regions_1e.py`.
- **Phase 7 — Lane P (2026-09-18):** **T-foundation-pham-1f** ✓ — [world-builder](c7c9b518-084e-4c7a-93a2-e9ff731303f0) · **32** `reg-{hp,pt,lh}-*` + PNG (HP·PT·LH); tái sinh [`build_pham_regions_1f.py`](../realms/pham-gioi/scripts/build_pham_regions_1f.py). Backlog region-deep: **13 CHL** (L/T/H) · cursor **T-foundation-linh-2d**.
- **Tiếp theo (sau 1f):** **T-foundation-linh-2d** → **3d** → **4d**; **micro geo**; Phase **6** cross-realm.
- **Lane H (2026-09-18):** **T-foundation-than-4b-ext** ✓ — **7/7** chau_luc `TH-THAN-HUYEN-CUC` — [world-builder](818a3ecc-7493-4240-99b8-2934c960f054) (Huyền Băng Thần ≠ Tiên `chl-huyen-bang`).
- **Orchestrator (2026-09-18):** đồng bộ `00-cosmos-index.md` §5 link 4b/4c sau [Thần region exemplars](078dc075-2cd0-4d15-9ec4-8e0f923a46b9).
- **Lane P / L / T / H:** Phase **1a–4c complete**; Phase **5** ✓ (subsidiary logic).
- **Lane L:** **T-foundation-linh-2b-ext** ✓ — **6/6** chau_luc `TH-LINH-CAN-NGUYEN`.
- **Lane T (2026-09-18):** **T-foundation-tien-3b-ext** ✓ — **6/6** chau_luc `TH-TIEN-HUONG-NGUYEN` — [world-builder](ce0be0b1-2950-4e3a-833b-bf7ad4e7addb).

---

## CP / RP

Không có — world generic Foundation; không promote vào Core trừ human yêu cầu.
