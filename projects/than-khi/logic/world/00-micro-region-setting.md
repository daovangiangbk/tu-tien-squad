# Micro-region — Liên Trần (3 thành · 5 trấn)

| Trường | Giá trị |
| --- | --- |
| **work_slug** | `than-khi` |
| **Owner** | world-builder (T-world-project) |
| **Neo** | `00-master-brief.md` §4 · §8–§9 · D8 |
| **Geo** | [`geo/region/reg-tk-lien-tran.geojson`](geo/region/reg-tk-lien-tran.geojson) |

**Naming:** Stub ID trong bảng dưới — **pending** `interface/naming/registry.md`.

---

## 1. Quy mô đã khóa (geo = source of truth)

| Loại | Số lượng | ID |
| --- | --- | --- |
| **Thành lớn** | **3** | `LOC-TK-CTY-01` (bắc) · `LOC-TK-CTY-02` (đông) · `LOC-TK-CTY-03` (tây) |
| **Thị trấn nhỏ** | **5** | `LOC-TK-TWN-HOME` · `02` · `03` · `04` · `05` |
| **MC anchor (D8)** | **1** | **`LOC-TK-TWN-HOME`** — lò rèn ban ngày |

Mỗi settlement: **`guardian_public: Kim Đan`** · **`backing_hidden: Nguyên Anh`** (properties GeoJSON).

---

## 2. Vai trò narrative (không beat)

| ID | Chức năng logic |
| --- | --- |
| `LOC-TK-TWN-HOME` | Cover phàm · kinh tế ổn · **điểm giao đêm** gần `LOC-TK-NET-SAFE` |
| `LOC-TK-CTY-02` | Mạng đêm nối (`ROUTE-TK-NIGHT-LOOP`); thuế · chính trị |
| `LOC-TK-CTY-01` | Luật chặt · đấu giá · khế với trấn bắc |
| `LOC-TK-CTY-03` | Gia tu vỏ · thương hội |
| `LOC-TK-TWN-03` | Cửa **REG-TK-NAM-DU** → `LOC-TK-WLD-BEAST` |
| `LOC-TK-TWN-02` | Bến `RIVER-TK-LINH-HE` |
| `LOC-TK-TWN-04` | Mỏ · phàm lao · linh thạch hạ |
| `LOC-TK-TWN-05` | Lâm · nguyên liệu rèn / dược thấp |

---

## 3. Điểm ngầm (không prose)

| ID | visibility | Ghi |
| --- | --- | --- |
| `LOC-TK-NET-SAFE` | `mc_phase1` | Giao nhiệm vụ mạng |
| `LOC-TK-CLAN-SHELL-A` | `hidden_logic` | MC gốc gia tu |
| `LOC-TK-CLAN-SHELL-B` | `hidden_logic` | Khế bắc |
| `LOC-TK-WLD-BEAST` | `public` | Yêu thú · mốc giữ trẻ |

---

## 4. Liên thành (MC phase 1)

- **Nhà cố định:** chỉ `LOC-TK-TWN-HOME`.
- **Liên kết:** đại lộ + linh hà tới **3 thành** (1–4 ngày đi bộ tùy hướng — xem region geo `travel_days_walk`).
- **Luân chuyển thành** (nếệm vụ dài): plot-architect quyết — **geo không đổi**.

---

*Stub settlement map · naming-specialist tiếp theo.*
