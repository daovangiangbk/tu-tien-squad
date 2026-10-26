# Tiểu cục — index

> **Cập nhật:** 2026-10-08 · **`T-world-arc-2`** *(mở rộng TC-TK-001 · sửa nhãn Mòn Thám Lộ)*

| Arc | TC-ID | File micro | Hub local | Neo region |
| --- | --- | --- | --- | --- |
| **1** | **TC-TK-001** | [`geo/micro/arc-01-tran-ren-mc.geojson`](geo/micro/arc-01-tran-ren-mc.geojson) | `LOC-TWN-MC-FORGE` `[0,0]` | `reg-cuoc-an-sat` · parent `[0,0]` |
| **1** | **TC-TK-002** | [`geo/micro/arc-01-rung-nhiem-vu.geojson`](geo/micro/arc-01-rung-nhiem-vu.geojson) | `LOC-FOREST-MISSION` `[0,0]` | `reg-cuoc-an-sat` · parent `[-48,-8]` |
| **2** | **TC-TK-001** *(mở rộng)* | **Cùng file** [`arc-01-tran-ren-mc.geojson`](geo/micro/arc-01-tran-ren-mc.geojson) — *không* tách `arc-02-*.geojson` | `LOC-TWN-MC-FORGE` | `reg-cuoc-an-sat` · parent `[0,0]` |

**Beat map Arc 1:** [`../arcs/01-arc1-beats.md`](../arcs/01-arc1-beats.md) § Ràng buộc tiểu cục · **Arc 2:** [`../arcs/02-arc2-beats.md`](../arcs/02-arc2-beats.md) § Ràng buộc tiểu cục · tóm [`00-arc-master-outline.md`](../arcs/00-arc-master-outline.md) § Arc 2.

**Quy ước mở rộng:** Cùng **`world:tieu_cuc_id`** + hub → bổ sung feature trong file micro hiện có; ghi `world:arc_coverage` trên collection. Arc 3+ thành / di chuyển → region mới hoặc micro mới (plot-architect).

---

## Arc 1 — tóm không gian

### TC-TK-001 — Trấn rèn MC

| ID | Vai trò Arc 1 |
| --- | --- |
| `LOC-TWN-MC-FORGE` | Cửa lò · hub |
| `LOC-FORGE-FURNACE-HALL` | Lò công khai |
| `LOC-FORGE-WORKSHOP-HIDDEN` | Xưởng ngầm · binh khí |
| `LOC-FORGE-CHILD-NICHE` | Ẩn CHAR-002 |
| `LOC-TRANN-ELDER-YARD` | Trấn lão · phí im lặng |
| `LOC-NET-MEET-INN` | CHAR-003 · hợp đồng / đối chất |
| `ROUTE-FORGE-TO-FOREST-HEAD` | Đầu **U Lâm Đạo** · đêm |

### TC-TK-002 — Rừng nhiệm vụ

| ID | Vai trò Arc 1 |
| --- | --- |
| `LOC-FOREST-MISSION` | **U Lâm Khẩu** · hub |
| `LOC-FOREST-TRAIL-IN` | **Mòn Thám Lộ** · vào trại |
| `LOC-FOREST-TARGET-CAMP` | Trại tháo chạy |
| `LOC-FOREST-KILL-GROUND` | Giết vợ chồng |
| `LOC-FOREST-CHILD-SPOT` | Giữ trẻ · FS-002 |
| `LOC-FOREST-BEAST-PATH` | Yêu thú áp sát |
| `LOC-FOREST-EXIT-NORTH` | Mòn rút về trấn |

---

## Arc 2 — Lò rèn & nuôi ẩn *(ch 19–35)*

**Macro:** Nuôi ẩn tại **Thiết Ngọc Trấn** · CHAR-002 tại **`LOC-FORGE-CHILD-NICHE`** (continuity ch.18) · tension trấn / mạng / nghiệp.

**File:** Mở rộng **TC-TK-001** trong [`arc-01-tran-ren-mc.geojson`](geo/micro/arc-01-tran-ren-mc.geojson) — **không** file micro Arc 2 riêng.

| ID | Vai trò Arc 2 |
| --- | --- |
| `LOC-FORGE-CHILD-NICHE` | Nuôi · kỷ luật im · SUB-MAIN-NURTURE |
| `LOC-FORGE-WORKSHOP-HIDDEN` | Che trẻ · phù / búa · không đưa lên sân lò |
| `LOC-FORGE-PHU-VAULT` | **Mật Phù Khố** · **FS-003** plant · kho phù *(ch ~25–30)* |
| `LOC-TRANN-ELDER-YARD` | Trấn hỏi · **mua im lặng** · phí ~30 hạt/tháng |
| `LOC-TWN-MARKET-HEAD` | **Thiết Hành Khẩu** · đầu chợ · lương · mắt dân · **RF-001** nếu lộ trẻ |
| `LOC-TWN-GRAIN-DEPOT` | **Trấn Lương Khố** · cung bánh · nối **Nhật Cung Đạo** |
| `LOC-TWN-HERB-STALL` | **Thảo Đầu Đàn** · thuốc phàm trẻ · chi phí ẩn |
| `LOC-TWN-WELL-CROSS` | **Giao Kính Đinh** · giếng giao phố · đồn đoán hàng xóm |
| `LOC-NET-MEET-INN` | **Giới Liên Trạm** · mạng **hạ uy tín** · cảnh báo sai quy cách |
| `ROUTE-TWN-SUPPLY-FORGE` | **Nhật Cung Đạo** · ban ngày: kho → **Thiết Hành Khẩu** → **Giao Kính Đinh** → cửa lò |
| `ROUTE-TWN-PATROL-EAST` | **Đông Huan Tuần** · trấn vệ · rủi ro tiếng / khách lạ |
| `ROUTE-FORGE-TO-FOREST-HEAD` | Nhiệm vụ đêm khác · nghiệp tăng *(arc 2 xen)* |

**Naming:** Tên canon Arc 2 trấn — [`interface/naming/registry.md`](../../interface/naming/registry.md) § Micro Arc 2 *(2026-10-08 · `T-naming-places-arc-2`)*.

**TC-TK-002:** Read-only flashback / nhắc **U Lâm** — không mở rộng geo Arc 2 trừ sửa nhãn **`LOC-FOREST-TRAIL-IN`** (Mòn Thám Lộ).

---

## Arc 3+ *(pending)*

| Arc | Micro (dự kiến) |
| --- | --- |
| 3 | Thành · `reg-tk-lien-tran` hub · micro mới |
| 4+ | Trốn đa trấn · plot-architect |

**Ghi chú:** `00-micro-region-setting.md` (Liên Trần / `reg-tk-lien-tran`) là **lớp vùng** tổng; Arc 1–2 prose **neo** `reg-cuoc-an-sat` + **TC-TK-001** cho khớp beats / ch.18.
