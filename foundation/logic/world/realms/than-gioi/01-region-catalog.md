# Thần Giới — Region catalog

> **Mục đích:** Liệt kê `REG-*` theo đại lục **tinh hà Huyền Cự** — đối chiếu `chau_luc` (**7/7** ✓) / `region` (4c ✓).

**Atlas:** [`00-world-atlas.md`](00-world-atlas.md) · **Tinh hà:** [`geo/00-tinh-ha.geojson`](geo/00-tinh-ha.geojson)

**Chú thích cột Geo:** `✓` = có polygon trên `chau_luc`; **region** = có `geo/region/*.geojson` (4c); `—` = stub tinh_ha only.

---

## CHL-TRUNG-THAN (Trung Thần) — chau_luc ✓

**Geo:** [`geo/chau-luc/chl-trung-than.geojson`](geo/chau-luc/chl-trung-than.geojson) · **Hub:** `LOC-RT-THAN-QUAN` · **parent:** `[-60.0, -34.0]`

| REG ID | Tên gợi ý | Vai trò | Geo | `than_khi_tier` |
| --- | --- | --- | --- | --- |
| `REG-RT-THAN-QUAN` | Thần Quan thành | Trung ương thần triều · hub | chau_luc · **region geo: done** → [`reg-rt-than-quan.geojson`](geo/region/reg-rt-than-quan.geojson) | `mach_chủ` |
| `REG-RT-TAM-DE` | Tam Đế đài | Chính trị thần giới | ✓ | `rất_nặng` |
| `REG-RT-TRUNG-NGUYEN` | Trung Nguyên đài | Chợ Thần nguyên · hội thương | ✓ | `rất_nặng` |
| `REG-RT-NAM-VAN` | Nam Vân cửa | Thương lộ mây thần | ✓ | `nặng_ổn_định` |
| `REG-RT-NAM-HAI` | Nam Hải thần cảng | Thần thuyền Độ Du | ✓ | `rất_nặng` |
| `REG-RT-BAC-LINH` | Bắc Linh uyên | Biên Kiếm Lôi | ✓ | `nặng_ổn_định` |
| `REG-RT-TAY-QUAN` | Tây Quan | Biên Hồn Vực | ✓ | `nặng_ổn_định` |
| `REG-RT-DONG-THAN` | Đông Thần đài | Liên Vạn Pháp | ✓ | `rất_nặng` |
| `REG-RT-DONG-HAI` | Đông Hải thần cảng | Thuế thần triều | ✓ | `rất_nặng` |
| `REG-RT-PHUC-DIA` | Phúc Địa cốc | Thần phủ T2–T3 | ✓ | `mach_T2_T3` |
| `BRR-RT-THIEN-LAM` | Dãy Thiên Lam | Barrier (polygon) | ✓ | `mach_rải_cao` |

**Sông:** `RIVER-RT-THAN-HA` ✓ · `RIVER-RT-DONG-LUU` ✓

---

## CHL-HUYEN-BANG (Huyền Băng) — chau_luc ✓

**Geo:** [`geo/chau-luc/chl-huyen-bang.geojson`](geo/chau-luc/chl-huyen-bang.geojson) · **Hub:** `LOC-HC-CUC-PHONG` · **parent:** `[-248.0, 177.0]`

| REG ID | Tên gợi ý | Vai trò | Geo | `than_khi_tier` |
| --- | --- | --- | --- | --- |
| `REG-HC-CUC-PHONG` | Cự Phong | Mép **Tiên–Thần** `(bí mật)` · hub | ✓ | `mach_chủ` |
| `REG-HC-BANG-NGUYEN` | Băng Nguyên | Huyền băng cấm | ✓ | `mach_T2_T3` |
| `REG-HC-BAC-MACH` | Bắc Mạch cực | E-THAN-TIEN-GATE treo | ✓ | `mach_rải_cao` |
| `REG-HC-NAM-HAI` | Nam Hải băng đài | Biển băng thần khí | ✓ | `nặng_lạnh` |
| `REG-HC-TAY-HUYEN` | Tây Huyền quan | Biên Hư Vi void | ✓ | `nặng_lạnh` |
| `REG-HC-DONG-LAM` | Đông Lam uyên | Rìa Kiếm Lôi | ✓ | `nặng_ổn_định` |
| `REG-HC-CUU-HAN` | Cửu Hàn cốc | Thần nguyên băng | ✓ | `mach_T2_T3` |
| `REG-HC-TRUNG-BANG` | Trung Băng đài | Trung chuyển Thần nguyên | ✓ | `rất_nặng` |
| `REG-HC-LINH-DONG` | Linh Đông đài | Nhập khí từ Trung Thần | — (clip vỏ) | `rất_nặng` |
| `BRR-HC-HUYEN-SON` | Dãy Huyền Sơn | Barrier | ✓ | `mach_rải_cao` |

**Sông:** `RIVER-HC-BANG-HE` ✓ · `RIVER-HC-TAY-LUU` ✓

---

## CHL-VAN-PHAP (Vạn Pháp) — chau_luc ✓

**Geo:** [`geo/chau-luc/chl-van-phap.geojson`](geo/chau-luc/chl-van-phap.geojson) · **Hub:** `LOC-VP-PHAP-DIEN` · **parent:** `[121.0, 8.0]`

| REG ID | Tên gợi ý | Vai trò | Geo | `than_khi_tier` |
| --- | --- | --- | --- | --- |
| `REG-VP-PHAP-DIEN` | Pháp Điện thành | Luật thần · hub | chau_luc · **region geo: done** → [`reg-vp-phap-dien.geojson`](geo/region/reg-vp-phap-dien.geojson) | `mach_chủ` |
| `REG-VP-VAN-KY` | Vạn Ký các | Khế **Vạn Tự** treo | ✓ | `luật_pháp` |
| `REG-VP-TRUNG-LUAT` | Trung Luật đài | Hội thương pháp | ✓ | `rất_nặng` |
| `REG-VP-TAY-LUAT` | Tây Luật uyên | Trận pháp thần | ✓ | `nặng_ổn_định` |
| `REG-VP-DONG-HAI` | Đông Hải bình | Liên Kiếm Lôi | ✓ | `rất_nặng` |
| `BRR-VP-PHAP-SON` | Dãy Pháp Sơn | Barrier | ✓ | `mach_rải_cao` |

**Sông:** `RIVER-VP-VAN-HE` ✓

---

## CHL-KIEM-LOI (Kiếm Lôi) — chau_luc ✓

**Geo:** [`geo/chau-luc/chl-kiem-loi.geojson`](geo/chau-luc/chl-kiem-loi.geojson) · **Hub:** `LOC-KL-LOI-DINH` · **parent:** `[114.0, 158.0]`

| REG ID | Tên gợi ý | Vai trò | Geo | `than_khi_tier` |
| --- | --- | --- | --- | --- |
| `REG-KL-LOI-DINH` | Lôi Đình | Thử **Thần kiếp** · hub | ✓ | `mach_chủ` |
| `REG-KL-KIEM-TAN` | Kiếm Tán | Kiếm mạch công cộng | ✓ | `mach_chủ` |
| `REG-KL-TRUNG-LOI` | Trung Lôi đài | Hội thương lôi tinh | ✓ | `rất_nặng` |
| `REG-KL-NAM-VAN` | Nam Vân cửa | Thương lộ lôi mây | ✓ | `nặng_ổn_định` |
| `REG-KL-BAC-HAN` | Bắc Hàn uyên | Biên REG-HC-DONG-LAM | ✓ | `mach_rải` |
| `REG-KL-TAY-KIEM` | Tây Kiếm quan | Biên REG-RT-BAC-LINH | ✓ | `nặng_ổn_định` |
| `REG-KL-LOI-VUC` | Lôi Vực | Thần phủ kiếm–lôi | ✓ | `mach_T2_T3` |
| `REG-KL-DONG-HAI` | Đông Hải bình | Liên Vạn Pháp / Cửu Phong | — (mép vỏ hẹp; lore `ROUTE-CP-BAC-KIEM-LOI`) | `rất_nặng` |
| `REG-KL-NAM-LOI` | Nam Lôi đảo | Lôi tinh thần hạ phẩm | — (clip vỏ nam) | `lôi_tinh` |
| `BRR-KL-LOI-SON` | Dãy Lôi Sơn | Barrier | ✓ | `mach_rải_cao` |

**Route / sông:** `ROUTE-KL-TAY-TRUNG-THAN` ✓ → `REG-RT-BAC-LINH` · `RIVER-KL-LOI-HE` ✓

---

## CHL-HON-VUC (Hồn Vực) — chau_luc ✓

**Geo:** [`geo/chau-luc/chl-hon-vuc.geojson`](geo/chau-luc/chl-hon-vuc.geojson) · **Hub:** `LOC-HV-HON-DIEN` · **parent:** `[-250.0, -13.0]`

| REG ID | Tên gợi ý | Vai trò | Geo | `than_khi_tier` |
| --- | --- | --- | --- | --- |
| `REG-HV-HON-DIEN` | Hồn Điện | Mệnh lực thần · hub | ✓ | `mach_chủ` |
| `REG-HV-TRUNG-MENH` | Trung Mệnh đài | Khế mệnh thần | ✓ | `rất_nặng` |
| `REG-HV-VONG-HA` | Vong Hà cửa | Luân hồi treo `(Phase 5)` | ✓ | `mach_T2_T3` |
| `REG-HV-NAM-HON` | Nam Hồn cửa | Thương lộ hồn phế | ✓ | `nặng_ổn_định` |
| `REG-HV-NAM-VUC` | Nam Vực đài | Biên REG-ST-BAC-SINH | ✓ | `rất_nặng` |
| `REG-HV-BAC-U` | Bắc U uyên | Mép void Hư Vi (lore) | ✓ | `mach_rải` |
| `REG-HV-TAY-U` | Tây U vực | Âm–dương hồn | ✓ | `nặng_ổn_định` |
| `REG-HV-TAY-VI` | Tây Vi mép | E-THAN-VOID-HV | ✓ | `loãng_lạnh` |
| `REG-HV-DONG-QUAN` | Đông Hồn quan | Biên REG-RT-TAY-QUAN | ✓ | `nặng_ổn_định` |
| `BRR-HV-HON-SON` | Dãy Hồn Sơn | Barrier | ✓ | `mach_rải_cao` |

**Route / sông:** `ROUTE-HV-DONG-TRUNG-THAN` ✓ → `REG-RT-TAY-QUAN` · `RIVER-HV-VONG-HE` ✓

---

## CHL-SINH-TIEU (Sinh Tiêu) — chau_luc ✓

**Geo:** [`geo/chau-luc/chl-sinh-tieu.geojson`](geo/chau-luc/chl-sinh-tieu.geojson) · **Hub:** `LOC-ST-SINH-QUAN` · **parent:** `[-105.0, -217.0]`

| REG ID | Tên gợi ý | Vai trò | Geo | `than_khi_tier` |
| --- | --- | --- | --- | --- |
| `REG-ST-SINH-QUAN` | Sinh Quan | Sinh–diệt thần lệ · hub | ✓ | `mach_chủ` |
| `REG-ST-TRUNG-DIET` | Trung Diệt đài | Thần lệ công khai | ✓ | `rất_nặng` |
| `REG-ST-TIEU-DIA` | Tiêu Địa | Mạch suy / tái sinh | ✓ | `mach_T2_T3` |
| `REG-ST-NAM-HAI` | Nam Hải đảo | Đảo hư thần khí | ✓ | `rất_nặng` |
| `REG-ST-DONG-NAM` | Đông Nam uyên | Ven biển sinh–diệt | ✓ | `mach_rải` |
| `REG-ST-BAC-SINH` | Bắc Sinh uyên | Biên Trung Thần / Hồn Vực | ✓ | `nặng_ổn_định` |
| `REG-ST-TAY-TIEU` | Tây Tiêu quan | E-THAN-TIEN-VESTIGE | ✓ | `nặng_ổn_định` |
| `REG-ST-VONG-DIEN` | Vong Điện cốc | Diệt mệnh thần phủ | ✓ | `mach_T2_T3` |
| `REG-ST-DONG-PHUC` | Đông Phục đài | Mạch Phục Mệnh (lore) | ✓ | `dao_động` |
| `BRR-ST-SINH-SON` | Dãy Sinh Sơn | Barrier | ✓ | `mach_rải_cao` |

**Route / sông:** `ROUTE-ST-BAC-TRUNG-THAN` ✓ → `REG-RT-NAM-VAN` · `RIVER-ST-SINH-HE` ✓

---

## CHL-CUU-PHONG (Cửu Phong) — chau_luc ✓

**Geo:** [`geo/chau-luc/chl-cuu-phong.geojson`](geo/chau-luc/chl-cuu-phong.geojson) · **Hub:** `LOC-CP-CUU-MEN` · **parent:** `[50.0, -188.0]`

| REG ID | Tên gợi ý | Vai trò | Geo | `than_khi_tier` |
| --- | --- | --- | --- | --- |
| `REG-CP-CUU-MEN` | Cửu Môn | Cửu phong thần · hub | ✓ | `mach_chủ` |
| `REG-CP-TRUNG-DAN` | Trung Đan đài | Thần đan các | ✓ | `rất_nặng` |
| `REG-CP-PHONG-COC` | Phong Cốc | Đan thần · phong ấn | ✓ | `mach_T2_T3` |
| `REG-CP-NAM-HAI` | Nam Hải cửa | Thương lộ đan thần | ✓ | `rất_nặng` |
| `REG-CP-BAC-PHONG` | Bắc Phong uyên | Biên Kiếm Lôi | ✓ | `nặng_ổn_định` |
| `REG-CP-TAY-CUU` | Tây Cửu quan | Biên Sinh Tiêu | ✓ | `nặng_ổn_định` |
| `REG-CP-DONG-LAM` | Đông Lam | Thần thảo cổ | ✓ | `rất_nặng` |
| `REG-CP-DONG-HAI` | Đông Hải bình | Liên REG-VP-DONG-HAI | ✓ | `rất_nặng` |
| `REG-CP-NAM-DAO` | Nam Đảo phụ | Đan hạ phẩm | — (clip vỏ nam) | `mach_rải` |
| `BRR-CP-CUU-SON` | Dãy Cửu Sơn | Barrier | ✓ | `mach_rải_cao` |

**Route / sông:** `ROUTE-CP-BAC-KIEM-LOI` ✓ · `RIVER-CP-CUU-HE` ✓

---

## Exemplar region (Phase 4c ✓)

**Geo:** [`geo/region/reg-rt-than-quan.geojson`](geo/region/reg-rt-than-quan.geojson) · [`geo/region/reg-vp-phap-dien.geojson`](geo/region/reg-vp-phap-dien.geojson)  
**PNG:** [`geo/out/reg-rt-than-quan.png`](geo/out/reg-rt-than-quan.png) · [`geo/out/reg-vp-phap-dien.png`](geo/out/reg-vp-phap-dien.png)  
**Micro stub:** [`02-tieu-cuc-index.md`](02-tieu-cuc-index.md)

### Bàn cờ — Thần Quan thành (`REG-RT-THAN-QUAN`) · **thần triều**

**Khan hiếm:** Thần nguyên **hạ–trung** qua `LOC-RT-THAN-MACH-NO` — monopoly **Thần Quốc Tông** + Tam Đế; thuế mạch **12–25%** trên `RIVER-RT-THAN-HA-URBAN`; thần phủ **T1** (`LOC-RT-GIA-THAN-PHU`) · **T2** (`LOC-RT-TRUNG-NGUYEN-KE`); tranh **T2–T3** tại `LOC-RT-THAN-PHU-MEN` (Phúc Địa).

**Cửa thoát:** Bắc `ROUTE-RT-THAN-TAM` → `REG-RT-TAM-DE`; đông `ROUTE-RT-THAN-DONG` → `REG-RT-DONG-HAI`; nam sông → `REG-RT-TRUNG-NGUYEN`; tây `BRR-RT-THIEN-LAM-FOOT` → Thiên Lam (mạch rải, **Thần kiếp** nặng hơn).

**Phản ứng thần triều / chính trị tu:** Lộ diện tranh mạch = **truy nã liên tông**; phe một tông trong Tam Đế = **đóng thành** với đối thủ; đụng mạch gốc nội thành = **Nhân quả** + can thiệp trung ương. **Phần thưởng:** an toàn tương đối quanh hub, tiếp cận **Thần lệ** hạng trung–cao, Thần nguyên nhập từ Nam Vân/Đông Hải. **Giá:** thuế Thần nguyên cao; chính trị Tam thần triều — **không trung lập** lâu dài; **Tiên mới Thần** chưa mạch `(E-THAN-TIEN-THAN)`.

### Bàn cờ — Pháp Điện thành (`REG-VP-PHAP-DIEN`) · **luật thần**

**Khan hiếm:** Thần nguyên **luật pháp** đốt tại `LOC-VP-PHAP-MACH-NO`; khế **Vạn Tự** treo tại `LOC-VP-VAN-KY-CAC` — thuế **15–28%** + vi phạm khế = **Thần lệ** tự kích; thần phủ **T1** (`LOC-VP-PHAP-TONG`) · **T2** (`LOC-VP-TRUNG-LUAT-KE`); mỏ **T2** tại `LOC-VP-THAN-NGUYEN-MO` — tranh tinh luật, **không** mua bằng thuế thuần.

**Cửa thoát:** Bắc `ROUTE-VP-PHAP-VAN-KY` → `REG-VP-VAN-KY`; đông `ROUTE-VP-PHAP-DONG` → `REG-VP-DONG-HAI` (Kiếm Lôi); nam `RIVER-VP-VAN-HE-URBAN` → `REG-VP-TRUNG-LUAT`; tây `BRR-VP-PHAP-SON-FOOT` → Pháp Sơn (trận pháp thần).

**Phản ứng pháp tông / luật thần:** Chen lấn **khế công khai** = **phản khế** hoặc **mang nợ Nhân quả**; lộ thần công pháp cấm = **Vạn Ký** đóng mạch; hội thành — **Trung Luật các** giám sát, chiến công khai trong vòng đài = vi phạm **luật thần**. **Phần thưởng:** thần công pháp hạng cao, an toàn **theo khế** nếu tuân luật. **Giá:** tự do hành vi **bị ràng**; đối đầu thần triều = tranh **mạch + lệ**, không chỉ võ lực.

---

## Phase tiếp

- **4c:** **`done`** — exemplar `REG-RT-THAN-QUAN`, `REG-VP-PHAP-DIEN` + [`02-tieu-cuc-index.md`](02-tieu-cuc-index.md).
- **Micro:** theo slot trong `02-tieu-cuc-index.md` khi arc lock.
- **5:** giới phụ cosmos — orchestrator **T-foundation-subsidiary-5**.

*World-builder · T-foundation-than-4c · 4b-ext · 2026-09-18*
