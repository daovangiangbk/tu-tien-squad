# Đại cục thế giới — Thần Phù

> Tóm lược tinh hà **Phù Vi Tinh Hà** (符微星河) — **tách biệt** `tap-linh-dieu-lo`. Tên canon: `interface/naming/registry.md` · brief §8 v1.1 (2026-09-17).

**GeoJSON (4 tầng):** [`geo/00-tinh-ha.geojson`](geo/00-tinh-ha.geojson) · châu lục MC [`geo/chau-luc/chl-phu-vien.geojson`](geo/chau-luc/chl-phu-vien.geojson) · region [`geo/region/reg-gia-toc-phu-vuc.geojson`](geo/region/reg-gia-toc-phu-vuc.geojson). Quy ước: [`foundation/logic/00-geojson-world-map-convention.md`](../../../foundation/logic/00-geojson-world-map-convention.md) (v2).

---

## 1. Luật & tone (tóm tắt)

- **Theme (work):** Nghịch Thiên Nhi Hành; **Hữu tình** báo thù; vết *nợ máu* sau hi sinh người thân; phù đạo **có giá** (`06-phu-luc`).
- **MC bối cảnh:** Công tử **Thẩm thị · Phù Lĩnh** — phù gia phú, thiên tư kém, thực lực thấp; **cửu địch** tàn sát; arc 2 **Thanh Phù Thành** — ma tu luyện huyết đô thị.
- **Cõi làm việc phase 1:** **Hạ Giới** trên **Phù Viên đại lục** (`CHL-PHU-VIEN`); tinh hà còn bốn lục khác = expansion slot.
- **Quy mô sự kiện mục tiêu:** Arc 1 **III** (tộc diệt); arc 2 **II–III** (thành · điều tra); arc 3 mở **III** giang hồ — bám `foundation/logic/01-event-scale-system.md`.

---

## 2. Lịch sử (mốc logic — chưa chốt tên phe)

| Thứ tự | Mốc | Hệ quả hiện tại |
| --- | --- | --- |
| 1 | **Phù gia Thẩm thị · Phù Lĩnh độc quyền công thức** (đại khung) | Linh khí **trung–cao** vùng tộc; Phù các; cống hiến Phù các tông *(logic)* |
| 2 | **Cửu địch** kìm **biên bắc** (`REG-BIEN-CUU-DICH`) | Áp lực quân sự · thương mại; tiền đề tàn sát — **danh tính deferred** |
| 3 | **Thảm sát gia tộc** (Arc 1) | Phế địa tộc · MC sống sót · manh công thức |
| 4 | **Dịch chuyển sinh tồn → Thanh Phù Thành** (Arc 2) | Luật thành · hắc thị · **ma tu bắt cóc** — quan phủ xám |
| 5 | **Nam hoang đạo** mở giang hồ (Arc 3) | Tranh slot phù vật · báo thù dài |

---

## 3. Địa lý đại cục

### 3.1. Phù Vi Tinh Hà

**File:** [`geo/00-tinh-ha.geojson`](geo/00-tinh-ha.geojson) · **PNG:** [`geo/out/00-tinh-ha.png`](geo/out/00-tinh-ha.png).

| Hướng (tương đối) | ID | Tên | GeoJSON chau_luc | Ghi chú |
| --- | --- | --- | --- | --- |
| **Trung–đông (MC)** | `CHL-PHU-VIEN` | Phù Viên đại lục · Hạ Giới | [`chl-phu-vien.geojson`](geo/chau-luc/chl-phu-vien.geojson) | Arc 1–3 phase 1 |
| Tây | `CHL-TAY-DUOC` | Tây Dược đại lục | *(chưa mở file)* | Dược · đan — expansion |
| Bắc | `CHL-BAC-LINH` | Bắc Linh đại lục | *(chưa mở file)* | Linh hàn · cửu địch xa? |
| Đông | `CHL-DONG-HAI-YUAN` | Đông Hải Nguyên lục | *(chưa mở file)* | Hải ngoại deferred |
| Nam | `CHL-NAM-MO` | Nam Mộ hoang lục | *(chưa mở file)* | `hidden_logic` |

- **Neo tinh hà → lục:** `parent_coordinates` **`[-25, -172]`**, scale k≈**5.89** (SW bbox `CHL-PHU-VIEN`).

### 3.1.1. Phù Viên đại lục (tóm lược)

**File:** [`geo/chau-luc/chl-phu-vien.geojson`](geo/chau-luc/chl-phu-vien.geojson) · **Canvas:** [`canvas/chl-phu-vien.canvas.json`](canvas/chl-phu-vien.canvas.json) · **PNG:** [`geo/out/chau-luc-chl-phu-vien.png`](geo/out/chau-luc-chl-phu-vien.png).

| Lớp | ID | Vai trò logic |
| --- | --- | --- |
| Vùng MC | `REG-GIA-TOC-PHU-GIAU` | **Thẩm thị · Phù Lĩnh** phù giàu · trước thảm sát |
| Châu | `CHAU-THANH-PHU-VIEN` | **Thanh Phù Thành** · arc 2 ma tu đô thị |
| Biên | `REG-BIEN-CUU-DICH` | Áp **cửu địch** |
| Nam | `REG-NAM-HOANG-DUONG` | Vào giang hồ |
| Núi | `BRR-PHU-LINH` | Rào · ải đông |
| Tây | `REG-TAY-LAM` | Thoát / phế tích |

**Hub cấp lục:** `LOC-GIA-TOC-HUB` `(312,318)` · `LOC-THANH-PLACEHOLDER` `(780,318)`.

**Chi tiết bàn cờ MC:** [`01-region-active.md`](01-region-active.md) · region [`geo/region/reg-gia-toc-phu-vuc.geojson`](geo/region/reg-gia-toc-phu-vuc.geojson).

**Sông:** `RIVER-PHU-JIANG` (uốn khúc).

---

## 4. Tài nguyên & linh khí (gợi ý)

| Vùng | Linh khí | Tài nguyên | Hậu quả xã hội |
| --- | --- | --- | --- |
| **REG-GIA-TOC-PHU-GIAU** | Trung–cao | Linh điền · phù vật · **công thức tộc** | Gia tộc phú · thuê vệ · cống hiến Phù các |
| **CHAU-THANH-PHU-VIEN** | Trung bình | Linh thạch nhập · tin · khế | Quan phủ · hắc thị · **ma tu** che chở lợi ích |
| **REG-BIEN-CUU-DICH** | Thấp–trung (loạn biên) | Chiến lợi phẩm · tù binh | Cửu địch · tộc bị kẹt hai phía |
| **REG-NAM-HOANG-DUONG** | Thấp | Yêu thú · cỏ phù | Tán tu · đoạt bảo |

---

## 5. Invariant dự án (phase 1)

1. **Phù không thay đại cảnh giới** — bù khoảng cách ngắn, tu vi nền dài.
2. **Công thức tộc** không miễn phí kích phát / Nghiệp Ma phù.
3. **Cửu địch** có **lợi ích đo được** (đất · công thức · uy hiếp) — không phe thuần ác vô lý.
4. **Thành** = luật khế + hắc thị; ma tu **logic xám** (che chở · nhu cầu huyết khí).
5. **Không** retcon vị trí lục trên tinh hà đã publish GeoJSON.

---

## 6. Expansion slots

| Slot | Logic sẵn | Payoff deferred |
| --- | --- | --- |
| `CHL-BAC-LINH` | Nguồn gốc áp lực cửu địch? | Arc 4+ |
| `CHL-TAY-DUOC` | Dược · đan cho phù vật | Crafting arc |
| `CHL-DONG-HAI-YUAN` | Thương nhân · phù nguyên liệu hiếm | Kim Đan+ |
| `REG-DONG-HAI-RONG` | Cảng · buôn người? (xám) | Song song ma tuyến |
| Danh tính cửu địch | Manh arc 1 | User §8 |

---

## 7. Manh mối → arc

| Manh mối | Câu hỏi | Ràng buộc payoff |
| --- | --- | --- |
| Biên cửu địch | Ai ký lệnh tàn sát? | Không lộ tên trước user chốt |
| Công thức tàn | Cấp phù tối đa phase 1? | CP-001 / RP-001 |
| Ma tu thành | Ai che bắt cóc? | Phải có lợi ích quan · tông |
| Phù Giang | Ai kiểm soát bến? | Kinh tế arc 2 |

---

*Thần Phù — atlas v1 · placeholder địa danh.*
