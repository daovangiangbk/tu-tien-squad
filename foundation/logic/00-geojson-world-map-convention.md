# Quy ước GeoJSON — bản đồ kiến thế (Logic)

**Mục đích:** Mô tả **địa lý thiết kế** bằng GeoJSON tách khỏi prose — **bản đồ nhỏ neo trong bản đồ lớn**, tra cứu nhất quán cho writer/reviewer (read-only).

**Agent sở hữu:** `world-builder` tạo/cập nhật; arc-planner / prose **không** sửa `.geojson`.

---

## 1. Thứ tự bốn tầng (bắt buộc)

Luồng **từ lớn → nhỏ**; mỗi tầng là **một phần** của tầng trên, không tách rời:

```text
Tinh Hà (00)  →  Châu lục (chau-luc/*)  →  Region (region/*)  →  Micro (micro/*)
  toàn tinh hà      một file / CHL-*           một file / vùng MC        tiểu cục arc
```

| # | Scope | File / thư mục | Nội dung | Markdown |
| --- | --- | --- | --- | --- |
| **1** | `tinh_ha` | `<geo-root>/00-tinh-ha.geojson` | **Toàn Tinh Hà:** châu lục nào tồn tại, **vị trí tương đối**; phe/thế lực cấp giới (deferred); **không** phố, không beat | `00-world-atlas.md` (tóm lược + mục lục châu lục) |
| **2** | `chau_luc` | `<geo-root>/chau-luc/<slug>.geojson` | **Một châu lục / đại lục** (`CHL-*`): châu , mạch, thành cấp lục; neo trong tinh hà | `00-world-atlas.md` (link từng file) |
| **3** | `region` | `<geo-root>/region/<slug>.geojson` | **Một phần** của châu lục — vùng làm việc (vd. Thạch Lam · Lan Sa); tuyến, bàn cờ | `01-region-active.md` (hoặc md theo vùng MC) |
| **4** | `micro` | `<geo-root>/micro/*.geojson` | **Một phần** của region — tiểu cục / địa điểm chi tiết | `02-tieu-cuc-index.md` |

### 1.1. Layer logic và scope GeoJSON

Kiến trúc đối tượng chính thức nằm tại [`world/01-world-object-architecture.md`](world/01-world-object-architecture.md):

```text
realm → planet/system → continent → region → site → micro
```

Chuỗi trên là layer logic; bốn scope GeoJSON trong bảng là lớp không gian tương thích và **không đổi schema v2**. `tinh_ha` là tên scope legacy cho bản đồ quần vực: với Phàm/Linh, nó bọc không gian quanh một tinh cầu chính; với Tiên/Thần, nó có thể bọc tinh hệ hoặc quần tinh. Scope này không thay tầng `planet/system`, và các `CHL-*` trong atlas Phàm/Linh là châu lục của cùng một tinh cầu, không phải các tinh cầu riêng.

`site` nằm giữa region và micro trong hồ sơ logic nhưng không cần scope GeoJSON mới. Thành, trấn, tông môn, giáo phái có lãnh thổ có thể dùng Point hoặc feature trong region/micro; phe không có lãnh thổ chỉ cần hồ sơ logic.

### 1.2. Quyền sở hữu thư mục `geo`

- Planet active của Phàm/Linh sở hữu bản đồ tại `realms/<realm>/planets/<planet>/geo/...`; realm chỉ giữ atlas, catalog và chỉ mục domain, không chứa geometry thuộc planet.
- Tiên/Thần giữ bản đồ ở realm/system theo scope hiện hành trong giai đoạn system-first. Khi một planet được instantiate theo nhu cầu arc, geometry riêng của planet mới chuyển vào `planets/<planet>/geo/...`.
- Trong phần còn lại của quy ước này, `<geo-root>` là thư mục `geo/` của object đang sở hữu bản đồ.

### 1.3. Quy tắc đặt tên file (tầng 2–3)

- **Slug** = `id` canon **chữ thường**, dấu `-` (vd. `CHL-HA-GIOI-NAM` → `chl-ha-gioi-nam.geojson`).
- **Một châu lục = một file** trong `chau-luc/` — thêm lục mới **không** đổi tên file cũ.
- **Một vùng region = một file** trong `region/` — slug gợi ý `reg-<tên-vùng>` (vd. `reg-thach-lam.geojson`, `reg-lan-sa-chau.geojson`), kèm `world:region_id` trong collection.
- **`world:parent_file`:** đường dẫn **tương đối từ `<geo-root>/`** (vd. `chau-luc/chl-ha-gioi-nam.geojson`, `region/reg-lan-sa-chau.geojson`).

**Legacy (deprecated):** `00-world-macro.geojson`, `01-region-active.geojson` (tầng region cũ), `01-chau-luc-active.geojson`, `02-region-active.geojson` — migrate sang cấu trúc thư mục trên.

---

## 2. Neo tọa độ (bắt buộc)

### 2.1. Lưới story grid

- **Không** WGS84. Trục **x** = **Đông** (+), **y** = **Bắc** (+).
- Mỗi file GeoJSON có **gốc local** (hub — ghi trong `world:hub_id` và `world:coordinateNote`); **region/micro** thường hub `[0,0]`, **châu lục** có thể dùng toàn lục `0…1000`.
- **Đơn vị** = hành trình tương đối (ngày đi / dặm / canh). **Tinh hà** giữ thang thô; **châu lục** dùng lưới chi tiết (khuyến nghị **`world:grid_extent`: `[0, 1000]`** trên mỗi trục). **Region/micro** giữ thang riêng; neo lên châu lục qua `world:parent_coordinates` (vd. tọa độ `LOC-THACH-LAM` trên file châu lục).

### 2.1.1. Quy tắc vẽ `chau_luc` (bắt buộc)

1. **Lưới:** vẽ chi tiết trong **`0…1000`** (có thể lọt mép; biên ngoài = polygon `CHL-*` / `kind: continent`).
2. **Phân vùng khép kín:** mọi ô đất liền **phủ kín** lục (không gap có chủ đích): `REG-*`, `CHAU-*`, **`BRR-*` (dãy núi)**, v.v.; **cạnh ngoài** trùng biên lục; **cạnh trong** giữa hai ô **dùng cùng tọa độ** (không hai biên song song / overlap).
3. **Dãy núi = một vùng:** mỗi dãy (`id` **`BRR-*`**) là **một ô phân vùng riêng** — `Polygon` có bề rộng; **không** vẽ núi chồng lên hoang/rừng/châu; hoang · rừng · nội địa **kéo biên tới mép núi** và dùng chung polyline với polygon núi. `kind: barrier` (mặc định) hoặc `wilderness` nếu ghi chú địa mạo. **Cấm** `LineString` cho dãy núi chính.
4. **Sông (`kind: route`, id `RIVER-*`):** `LineString` **uốn khúc** (nhiều đỉnh); không đoạn thẳng dài một nét.
5. **Chi tiết nhỏ** (phố, phế địa, tuyến arc): **không** trên `chau_luc` — để `region/*` và `micro/*`.

### 2.2. Foreign members (FeatureCollection)

| Khóa | Bắt buộc | Ý nghĩa |
| --- | --- | --- |
| `world:schema` | có | `"tien-hiep-novel/geo/v2"` |
| `world:scope` | có | `tinh_ha` \| `chau_luc` \| `region` \| `micro` |
| `world:work_slug` | có | slug tác phẩm |
| `world:hub_id` | có | `id` feature hub local `[0,0]` (trừ tinh hà có thể dùng `TINH-HA-REF`) |
| `world:continent_id` | khuyến nghị (tầng 2) | `CHL-*` — trùng đại lục chính của file |
| `world:region_id` | khuyến nghị (tầng 3) | `REG-*` — id vùng region của file |
| `world:parent_scope` | tầng 2–4 | `tinh_ha` \| `chau_luc` \| `region` |
| `world:parent_feature_id` | tầng 2–4 | `id` vùng cha **trên file cha** (vd. `CHL-HA-GIOI-NAM`) |
| `world:parent_coordinates` | tầng 2–4 | `[x, y]` — vị trí **gốc local** của file con trên **lưới file cha** |
| `world:parent_file` | khuyến nghị | Từ `<geo-root>/`, vd. `chau-luc/chl-ha-gioi-nam.geojson` |
| `world:coordinateNote` | có | Một dòng tiếng Việt |

**Quy đổi lên tầng cha (mặt phẳng ngang — mặt đất, bản đồ châu):**

```text
parent_xy = world:parent_coordinates + local_xy
```

Lặp lại theo chuỗi `micro → region → chau_luc → tinh_ha`.

**Feature trùng `id` giữa tầng:** Point cùng `id` (vd. `LOC-THACH-LAM`) — `local_xy` ở file con **phải** sao cho `parent_xy` trùng Point cùng `id` trên file cha (hoặc hub quy ước).

### 2.3. Trục sâu (bí cảnh)

Trong **micro**, tọa độ **sâu xuống** (vd. `y` âm trong lòng uyên) có thể là **lưới nội bộ** — chỉ bắt buộc neo **hub / lối ra** lên region; không quy mọi điểm sâu ra bbox region.

### 2.4. Deprecated

- `world:meso_coordinates` = alias cũ của `world:parent_coordinates` khi `world:parent_scope` = `region`. File mới **chỉ** dùng `world:parent_*`.

---

## 3. Geometry theo tầng

| Scope | Geometry chính | Tránh |
| --- | --- | --- |
| `tinh_ha` | `Polygon` châu lục; `Point` nhãn | Chi tiết thành phố, arc |
| `chau_luc` | `Polygon` lục + ô khép kín (`REG-*`, `CHAU-*`, **`BRR-*` núi**); `LineString` sông uốn; `Point` hub cấp lục | Núi chồng vùng; LineString núi; beat/micro |
| `region` | `Point`, `LineString`, `Polygon` vùng làm việc | Phòng, hang từng cảnh |
| `micro` | `Point`, `LineString`, `Polygon` cảnh | Đổi vị trí châu lục |

**ID gợi ý:** `CHL-*` (châu lục / đại lục), `CHAU-*` hoặc `REG-*` (châu Châu / vùng trong lục), `LOC-*`, `ROUTE-*`.

---

## 4. Properties (Feature)

| Property | Mô tả |
| --- | --- |
| `id` | Stable ID |
| `name_vi`, `name_hv` | Tên canon |
| `kind` | `hub` \| `settlement` \| `wilderness` \| `dungeon` \| `route` \| `barrier` \| `polity` \| `resource` \| `continent` |
| `visibility` | `public` \| `mc_phase1` \| `hidden_logic` |

Route: `from_id`, `to_id`, `hazard`.

---

## 5. Liên kết markdown

Ví dụ (tap-linh-dieu-lo — bổ sung file khi mở thêm lục/vùng):

```markdown
**GeoJSON:** `planets/<planet>/geo/00-tinh-ha.geojson`
· `planets/<planet>/geo/chau-luc/chl-ha-gioi-nam.geojson`
· `planets/<planet>/geo/region/reg-thach-lam.geojson`
```

Micro: link từ `02-tieu-cuc-index.md`.

**Đồng bộ:** sửa GeoJSON trước → một dòng tóm tắt trong `.md`.

---

## 6. Hậu xử lý & visualize

**Chau_luc từ canvas:** `canvas_to_geojson.py` / `build_chl_ha_gioi_nam.py` — clip vào feature[0], biên nội gợn, gộp khe trong một lần chạy. **Sửa tay** `.geojson`: tùy chọn `normalize_chau_luc.py`.

**PNG / SVG:** cùng skill — `scripts/render_geojson.py` hoặc `scripts/render_stack.sh` (shim: `tools/world-geo-visualizer/`).

---

## 7. Ai đọc / sửa

| Agent | Quyền |
| --- | --- |
| `world-builder` | Tạo/sửa; giữ chuỗi neo 00 → chau-luc → region → micro |
| `project-orchestrator` | Delegate theo thứ tự tầng; không patch geo |
| `arc-planner` | Đọc |
| `xianxia-prose-writer` / `xianxia-chapter-reviewer` | Đọc only |

---

## 8. Checklist world-builder (geo)

- [ ] `00-tinh-ha`: ≥1 châu lục + **vị trí**; expansion slot châu lục khác (có thể `hidden_logic`)
- [ ] `chau-luc/<slug>.geojson`: `world:grid_extent` 0–1000; ô khép kín (kể cả `BRR-*`); biên chung; không núi overlay; sông uốn; `parent_*` neo tinh hà
- [ ] `region/<slug>.geojson`: `parent_*` neo đúng file châu lục; subset nằm bbox hợp lý
- [ ] `micro`: `parent_*` neo region; shared `id` khớp quy đổi
- [ ] Không file tầng con “trôi” không `parent_coordinates`

---

*2026-09-16 · v2.2 (chau_luc lưới 1000; phân vùng khép kín; núi polygon; sông uốn)*
