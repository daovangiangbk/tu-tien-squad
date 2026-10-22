# Atlas thế giới — Thần Khí (神器)

> **work_slug:** `than-khi` · **Cõi:** **Linh Giới** (灵界) · Brief v1 (2026-10-08) · **Naming:** stub ID — **chưa** canon Hán Việt (chờ `xianxia-naming-specialist`).

**GeoJSON:** [`geo/00-tinh-ha.geojson`](geo/00-tinh-ha.geojson) · [`geo/chau-luc/chl-tk-phu-lam.geojson`](geo/chau-luc/chl-tk-phu-lam.geojson) · [`geo/region/reg-tk-lien-tran.geojson`](geo/region/reg-tk-lien-tran.geojson)

**Foundation (read-only):** [`foundation/core/02-world-laws-lore-core.md`](../../../../foundation/core/02-world-laws-lore-core.md) · [`foundation/core/03-power-system-economy-core.md`](../../../../foundation/core/03-power-system-economy-core.md) · [`foundation/logic/world/realms/linh-gioi/00-world-atlas.md`](../../../../foundation/logic/world/realms/linh-gioi/00-world-atlas.md) (Tinh hà Càn Nguyên)

**Micro tóm:** [`00-micro-region-setting.md`](00-micro-region-setting.md) · **Bàn cờ MC:** [`01-region-active.md`](01-region-active.md)

---

## §0. Quyết định stack thế giới (bắt buộc)

| Lựa chọn | Chốt |
| --- | --- |
| **Foundation Core** | **Reuse** — Luật 1–7, Luật 6b (phàm + tu chung cư trú), Nhân–Quả, bảng cảnh giới §1.2; **không** patch `foundation/core/`. |
| **Geo & lore địa danh** | **Project-only instantiate** — file GeoJSON dưới `projects/than-khi/logic/world/geo/`; **không** copy 6 lục Foundation vào repo work. |
| **Neo logic (không geo file)** | Vùng truyện = **một lát biên** trên đại lục trong cụm **`TH-LINH-CAN-NGUYEN`** (Foundation) — đủ gần **thương mạch · linh thạch nội sinh**, đủ xa **tam tông Trung Linh** để quy mô **2–3 thành · 4–5 trấn** hợp lý. |
| **Work tinh hà file** | **`00-tinh-ha.geojson`** = **view work** (1 lục MC + 2 lục expansion `hidden_logic`); **không** thay thế Foundation `foundation/logic/world/realms/linh-gioi/planets/can-nguyen-tinh/geo/00-tinh-ha.geojson`. |

### Logic overrides (project — không sửa Core)

| Override | Giá trị Thần Khí | Ghi chú |
| --- | --- | --- |
| **Mật độ không gian** | Chỉ **REG-TK-LIEN-TRAN** populated (3 thành · 5 trấn); hoang / hải / lục khác = slot | Brief §4 · out of scope đại lục full |
| **Trần chiến lực công khai** | **Kim Đan** toạ trấn mỗi thành/trấn | Brief §9 |
| **Trần đe doạ** | **Nguyên Anh** ẩn sau mỗi toà trấn — **hiếm ra tay**, chủ yếu răn đe & điều phối | Không Hóa Thần+ trong work |
| **MC band** | **Trúc Cơ hậu kỳ** (Lôi–Hỏa); có thể tiến **Kim Đan** nếu có giá (D6 deferred) | Không power creep |
| **Kinh tế MC** | **Ổn định**; **mua** viện ngang hàng (linh thạch · ân tình có giá) | Brief §5 |
| **Cơ chế work** | **Tiên lộ đoạn** · **nghiệp sát** mỗi ám sát — đề xuất CP, chưa Foundation resource | D4 deferred |
| **Thời gian** | Nuôi trẻ → kết liệu **15–25 năm** in-world `[giả định]` | D2 deferred |

---

## 1. Tinh hà (work view)

| ID | Tên (stub) | Vai trò | Geo |
| --- | --- | --- | --- |
| `TINH-HA-REF` | Hub tham chiếu work | Gốc lưới story | Point `00-tinh-ha` |
| **`CHL-TK-PHU-LAM`** | **[pending] đại lục biên · Liên Trần** | **Lục MC** — micro-region | [`chl-tk-phu-lam.geojson`](geo/chau-luc/chl-tk-phu-lam.geojson) |
| `CHL-TK-EXP-EAST` | [pending] lục đông | Thương mạch · arc xa | `hidden_logic` — chưa chau_luc |
| `CHL-TK-EXP-NORTH` | [pending] lục bắc | Neo **tầm phù** endgame (D5) | `hidden_logic` — chưa chau_luc |

**Neo Foundation:** `world:foundation_anchor` = `TH-LINH-CAN-NGUYEN` trên collection tinh hà work.

---

## 2. Đại lục `CHL-TK-PHU-LAM` (tóm)

| Lớp | ID | Vai trò |
| --- | --- | --- |
| **Vùng làm truyện** | `REG-TK-LIEN-TRAN` | 3 thành · 5 trấn · mạng ngầm |
| **Nam** | `REG-TK-NAM-DU` | Yêu thú · nhiệm vụ mở · bỏ trẻ |
| **Bắc** | `REG-TK-BAC-LAM` + `BRR-TK-BAC-SON` | Rào · lối thoát hiếm |
| **Tây / Đông** | `REG-TK-TAY-HOANG` · `REG-TK-DONG-HAI` | Hoang · hải khẩu (phase sau) |
| **Thủy** | `RIVER-TK-LINH-HE` | Liên thành tây–đông |

**Hub lục (shared id):** `LOC-TK-TWN-HOME` tại `(500,400)` trên lưới lục = thị trấn MC.

### 2.1. Thành · trấn (stub — naming pending)

| ID | Loại | Kim Đan công khai | Nguyên Anh ẩn | Ghi |
| --- | --- | --- | --- | --- |
| `LOC-TK-CTY-01` | Thành lớn · **bắc** | Toà trấn A | Viên A | Luật thành · đấu giá |
| `LOC-TK-CTY-02` | Thành lớn · **đông** | Toà trấn B | Viên B | Hải cửa nội địa · thuế |
| `LOC-TK-CTY-03` | Thành lớn · **tây** | Toà trấn C | Viên C | Gia tu · thương hội vỏ |
| **`LOC-TK-TWN-HOME`** | **Thị trấn MC** | Toà trấn D | Viên D | **Lò rèn ban ngày** · **D8 nhà cố định** |
| `LOC-TK-TWN-02` | Trấn · bến sông | Toà trấn E | Viên E | Thu phí linh hà |
| `LOC-TK-TWN-03` | Trấn · ải nam | Toà trấn F | Viên F | Cửa dã |
| `LOC-TK-TWN-04` | Trấn · mỏ phụ | Toà trấn G | Viên G | Linh thạch hạ · phàm lao |
| `LOC-TK-TWN-05` | Trấn · lâm tiền | Toà trấn H | Viên H | Gỗ · dược thấp |

*Viên A–H có thể trùng phe hoặc khác phe — plot-architect gán; **mặc định logic:** 3 viên cho 3 thành, 1 viên **chung** giám sát 5 trấn qua khế lợi ích.*

---

## 3. Lớp quyền lực (sketch)

### 3.1. Kim Đan toạ trấn / Nguyên Anh ẩn

- **Công khai:** Mỗi thành/trấn có **một Kim Đan** (hoặc đại diện) **tọa trấn** — cấm tàn sát công khai trong luật thành (Luật 3 · Luật 7 Foundation).
- **Ẩn:** **Nguyên Anh** không xuất diện trừ khi **vi phạm khế vùng** hoặc **đe doạ cân bằng** — hành vi = răn đe, không flex.
- **MC:** Trúc Cơ hậu kỳ — sống **dưới** tầng này; thắng nhờ **kỹ năng · phù · binh khí · mua viện**, không vượt cảnh.

### 3.2. Mạng sát thủ (`FAC-TK-ASSN-NET` — stub)

| Khía cạnh | Logic |
| --- | --- |
| **Lợi ích** | Hoàn thành nhiệm vụ **không để lại dấu chính trị** trên bàn Kim Đan; thu phí **linh thạch + khế im lặng** |
| **Constraint** | **Không lạm sát** ngoài mục tiêu (uy tín nghề MC); **lộ mặt** → săn giết (brief §1) |
| **Blind spot** | Toà trấn **cần** mạng để xử lý việc **bẩn** nhưng **không được** công nhận — đổ lỗi cho “tu sĩ lẻ” |
| **Neo địa lý** | `LOC-TK-NET-SAFE` (region) — giao nhận gần MC town; tuyến đêm `ROUTE-TK-NIGHT-LOOP` |

**Kim Đan đứng sau mạng:** `[giả định]` một **Nguyên Anh** (cùng phe với viên thành đông) giữ **khế** — không lộ danh; CP D4/D5 có thể refine.

### 3.3. Gia tu ẩn (`FAC-TK-CLAN-HIDE-*` — stub)

| ID logic | Vai trò |
| --- | --- |
| `LOC-TK-CLAN-SHELL-A` | Vỏ thương hội tây — **MC gốc gia tu** (flashback / thù phụ) |
| `LOC-TK-CLAN-SHELL-B` | Trang viện phía bắc — **khế** với toà trấn thành 01 |
| **Blind spot** | Gia tu **cần** danh tiếng phàm để thu **đệ tử hữu căn**; che **ám sát** = đổi lấy **im lặng** từ mạng |

### 3.4. Ràng buộc lợi ích chéo (tóm)

```text
Nguyên Anh (ẩn) ── khế ── Kim Đan toà trấn (3 thành)
        │                    │
        │                    ├── thuế · luật · đấu giá
        │                    │
        └── mạng sát thủ ────┴── gia tu vỏ (A/B)
                    │
              MC: thợ rèn / sát thủ (đoạn tiên lộ)
```

---

## 4. Lịch sử vùng (nhân–quả ngắn)

| Mốc | Sự kiện | Hệ quả hiện tại |
| --- | --- | --- |
| **Cận cổ** | Ba thành ký **Hiệp ước Liên Trần** — chia linh hà · thuế ải | Kim Đan không giao chiến công khai; tranh qua **khế & ngầm** |
| **~80 năm trước** | Gia tu A **bị lộ** huyết mạch → kẻ thù (manh thù MC phụ) | Vỏ thương hội thay tên; `LOC-TK-CLAN-SHELL-A` |
| **Hiện tại** | Mạng sát thủ **professional hóa** dưới Nguyên Anh thành đông | MC có **tiếng** trong nghề; **đoạn tiên lộ** |
| **Mở truyện** | Nhiệm vụ tại `LOC-TK-WLD-BEAST` | Nhân–Quả · giữ trẻ |

---

## 5. Tài nguyên & kinh tế (≥3 số liệu)

| Hạng mục | Số liệu gợi ý | Ai thu |
| --- | --- | --- |
| **Thu phí ải thành–trấn** | **8–25 hạt linh thạch**/lượt (tu sĩ); phàm **bạc phàm** | Kim Đan toà trấn + quan phàm |
| **Nhiệm vụ sát thủ (tầng MC)** | **150–600 hạt**/vụ (độ khó Trúc Cơ) | Mạng trích **~15–25%**; phần còn MC |
| **Rèn binh khí phàm (MC ban ngày)** | **2–8 hạt**/món phàm; **30–120 hạt**/ pháp khí hạ | MC giữ margin; thuê **linh hỏa** tốn thêm |
| **Mua viện ngang hàng** | **50–300 hạt**/ lần (Trúc Cơ) | Broker · lữ khách · ân tình có giá |
| **Lò rèn · linh thạch hạ mỏ TWN-04** | **~400–900 hạt**/tháng kho (tổng trấn) | Trấn quản · tông gia thuê mỏ |

**Hai tầng tiền (Luật 6b):** Phàm nhân đông ở trấn — **bạc phàm**; tu sĩ & MC — **linh thạch**.

---

## 6. Invariant dự án (phase epic)

1. **Không** phi thăng Tiên Giới · **không** Hóa Thần+ combat trong vùng.
2. **Kim Đan** = trần công khai; **Nguyên Anh** = ẩn / đe doạ — vi phạm = có **giá chính trị**, không retcon.
3. **MC lộ diện sát thủ** → phản ứng săn giết (brief) — không gỡ bằng “may mắn”.
4. **Thù cha mẹ** = manh **phụ** — không đổi cốt chính nuôi trẻ / nghiệp / đại kết.
5. **Đại kết locked** — phù xa **ở nơi khác** (`CHL-TK-EXP-NORTH` slot logic).

---

## 7. Expansion slots

| Slot | Tầng bí mật | Logic sẵn |
| --- | --- | --- |
| `CHL-TK-EXP-EAST` | `(chưa lộ)` | Thương nhân · linh thạch hạng cao · săn đầu người |
| `CHL-TK-EXP-NORTH` | `(chưa lộ)` | **Tầm phù** · thần hồn MC (D5) |
| `REG-TK-DONG-HAI` | `(MC phase 1 biết sơ)` | Tẩu tượng · không arc đầu |
| **Danh tính Viên A–H** | `(hidden_logic)` | Plot twist khế Liên Trần |
| **CP: tiên lộ đoạn** | `(công khai sau CP)` | Nghiệp sát gắn mỗi ám sát |

---

## 8. Manh mối → arc xa

| Manh mối | Câu hỏi | Ràng buộc payoff |
| --- | --- | --- |
| Gia tu A · MC gốc | Ai diệt cha mẹ? | **Phụ** — không lái arc chính |
| Khế Liên Trần | Ai ký với mạng? | Phải có **lợi ích Kim Đan/Nguyên Anh** |
| Đứa trẻ nhiệm vụ | Huyết mạch / thù? | Gắn **Nhân–Quả** · trả nghiệp |
| Tầm phù xa | Cơ chế hồi hồn? | **Locked** endgame; D5 CP |
| `LOC-TK-NET-SAFE` | Ai là chủ mạng? | Không lộ trước plot-architect beat |

---

## 9. Naming pending (orchestrator → naming-specialist)

| Stub ID | Loại | Ghi chú |
| --- | --- | --- |
| `CHL-TK-PHU-LAM` | Đại lục | Tên Hán Việt + Việt |
| `REG-TK-LIEN-TRAN` | Vùng | Hiệp ước ba thành |
| `LOC-TK-TWN-HOME` | **Trấn MC** | Lò rèn · nhà cố định D8 |
| `LOC-TK-CTY-01` · `02` · `03` | Thành | Bắc · Đông · Tây |
| `LOC-TK-TWN-02` … `05` | Trấn | Bến · ải · mỏ · lâm |
| `FAC-TK-ASSN-NET` | Phe | Mạng sát thủ |
| `FAC-TK-CLAN-HIDE-*` | Phe | Gia tu ẩn |
| `RIVER-TK-LINH-HE` | Địa mạo | Linh hà |
| MC · đứa trẻ · tên mạng | Nhân vật | D3 · D7 |

---

*Thần Khí — world atlas A1 · world-builder · 2026-10-08*
