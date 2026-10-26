# Tiểu cục index — Arc 1 · Tây Mạch

| Trường | Giá trị |
| --- | --- |
| **work_slug** | `kho-hai-tien-lo` |
| **Arc** | 1 — Tạp Dịch Khu Mỏ (ch. 1–18, `complete`) · **2 — Ngoại Môn & Mạch Ngầm Tông Môn (ch. 19–45, `active`)** |
| **Region** | `REG-TL-TAY-MACH` · [`01-region-active.md`](01-region-active.md) |
| **Geo micro** | [`geo/micro/arc-01-kho-hai-tien-lo.geojson`](geo/micro/arc-01-kho-hai-tien-lo.geojson) *(dùng chung khung tọa độ Tây Mạch)* |
| **ID tiểu cục** | `MICRO-ARC01-TAY-MACH` (`TC-KHTL-A1`) · **`MICRO-ARC02-TAY-MACH` (`TC-KHTL-A2`)** |
| **Governance** | `T-world-arc-1` (`approved`) · **`T-world-arc-2` (delta Arc 2)** · 2026-10-23 |

**Convention:** Feature ID trùng registry khi có; site con dùng suffix `-GATE`, `-N` theo registry.

---

## Bảng site Arc 1

| ID | Loại | Tên | Arc 1 vai trò | Link logic |
| --- | --- | --- | --- | --- |
| `LOC-VIL-001` | site · thôn | **Thạch Khê Thôn** | Mở màn ch.1–2; huyết dẫn; hố khoai; nhặt ấn | §1 dưới |
| `LOC-VIL-002` | site · thôn | **Bạch Thổ Thôn** `[giả định]` | Chu Thiết quê; cùng lô khổ dịch; payoff D-03 sau | §2 |
| `LOC-MINE-001` | site · mỏ | **Hắc Nham Khoáng Động** | Cửa mỏ + toàn khu hầm tạp dịch | §3 |
| `LOC-MINE-001-N` | site · tuyến | **Bắc Tuyến** `[giả định]` | Lương Khôn · định mức · đáy hầm Arc 1 | §3 |
| `SECT-001` | site · tông | **Thái Nhạc Tông** (sơn môn / ngoại vi) | Lệnh dời dân; lễ cuối arc; Nghiêm trên cao | §4 |
| `LOC-MINE-002` | site · deferred | **Cựu Mạch Hầm** | Không geometry Arc 1; echo hao hụt | index only |
| `LOC-VIL-003` | site · deferred | **Lão Mạch Thôn** | CHAR-010; ngoài cụm geo Arc 1 | index only |

---

## §1 — `LOC-VIL-001` Thạch Khê Thôn

- **Geo:** tây nam micro hub; **dưới chân nhánh mạch Tây** (sườn đá vỡ sau khai mạch).
- **Social:** ~vài chục hộ phàm; nghề đẽo đá; **không** linh mạch nuôi tu.
- **Plot anchor:** FS-TBD-VILLAGE-TRUTH · domino 1 · ấn tại **rìa mạch mở**.

---

## §2 — `LOC-VIL-002` Bạch Thổ Thôn

- **Xác nhận world-builder (2026-10-23):** **đông bắc** Thạch Khê, **cùng thung lũng phụ**, cách **~nửa ngày đi bộ**; đất **bạch phèn** (khớp tên); **mẹ + hai em Chu** *(plot D-03)*.
- **Registry:** vẫn `[giả định]` Open #1 — cấu trúc **LOCKED**, tên có thể đổi.
- **Arc 1:** Chu cùng lô với MC; **không** cảnh sống tại thôn trước mỏ (trừ nhắc quê).

---

## §3 — `LOC-MINE-001` · `LOC-MINE-001-N`

- **Cửa mỏ (`LOC-MINE-001`):** vách **hắc nham**, khói địa nhiệt; tu gác LK; xe quặng **đông** về sơn môn.
- **Bắc Tuyến:** **bắc** và **sâu** trong núi; lán quản sự · kho phế · tầng tạp dịch; **trận nhãn** *(deferred sâu, không Point Arc 1)*.
- **Power / economy:** sát khí · phế khoáng · định mức; **Cố lão** kho phế · **Đinh lão** tầng đá.

---

## §4 — `SECT-001` Thái Nhạc Tông

- **Geo micro:** **sơn môn** đông bắc cửa mỏ — **Thái Nhạc** peak motif; ngoại môn sườn núi (~+400m so thung lũng).
- **Cấu trúc (Logic delta, không beat):** sơn môn → ngoại môn → **phòng khảo mạch / chấp pháp** (cao) · **khu mỏ** (tách sườn, không trong điện chính).
- **Quan hệ Tam Tông:** xem [`01-region-active.md`](01-region-active.md) §3.

---

## Arc 2 — Ngoại Môn & Mạch Ngầm (`MICRO-ARC02-TAY-MACH` / `TC-KHTL-A2`)

### Bảng site mở rộng Arc 2 (ch. 19–45)

| ID | Loại | Tên canon | Arc 2 vai trò | Link logic |
| --- | --- | --- | --- | --- |
| `SECT-001-OUTER` | site · phân khu tông | **Ngoại môn Thái Nhạc Tông** *(Ngoại viện, Đan các ngoại viện, Phòng khảo mạch)* | Lâm Hàn nhập viện (thẻ LK3), gánh khế ngoại môn; tranh ngạch Trúc Cơ Đan với Khương Minh Thư (`CHAR-011`); vẽ bản đồ khảo mạch cùng Tần Thanh Mặc (`CHAR-004`) | §5 dưới |
| `SECT-001-LAW` | site · phân khu tông | **Chấp pháp đường** | Nghiêm Hoằng Độ (`CHAR-007`) lưu bản chép hồ sơ *Thạch Khê*; tĩnh thất thờ bài vị không tên (`FS-014`); nơi nhận bản đồ khảo mạch và gạch tên Lương Khôn (`D-08`) | §6 dưới |
| `CLAN-VE-001` | site · thế gia nội vi | **Vệ Thủy Ngân phủ** | Phủ đệ thế gia của Vệ Hoài Trà (`CHAR-012`) & Vệ Cảnh Hành (`CHAR-005`); nắm khế nợ nhà Tần (`FS-010`) và khóa nguồn Kim hệ (`D-06`, `FS-005`) | §7 dưới |
| `LOC-CITY-001` | site · thành phụ | **Cạn Mạch Thành** | Thành phụ chân núi Thái Nhạc; quê chi họ Khương Minh Thư (`CHAR-011`), linh điền thế chấp Tần gia, chợ ngầm biên Tây Mạch | §8 dưới |
| `LOC-MINE-002` | site · hầm phế tích | **Cựu Mạch Hầm** *(kèm phế tích **Lão Mạch Thôn** `LOC-VIL-003`)* | Đổi từ `deferred` sang `active` ở nửa sau Arc 2: địa bàn lò đan lậu của **Tro Lão / Giữ Lò (`CHAR-010` Đỗ Viễn)**, nơi Chu Thiết (`CHAR-002`) mua đan độc tăng tốc (`FS-012`, `FS-019`) | §9 dưới |
| `LOC-MINE-001` | site · mỏ | **Hắc Nham Khoáng Động** *(Bắc Tuyến & Kho phế)* | Mở lại sau 3 tháng đóng đáy; định mức chồng thêm; nơi Cố lão (`CHAR-006`) trao Thủy hệ và Lương Khôn (`CHAR-003`) bị sổ sách gạch tên (`D-08`) | §3 trên |
| `LOC-VIL-002` | site · thôn | **Bạch Thổ Thôn** `[giả định]` | Quê mẹ và hai em Chu Thiết; bị bản đồ khảo mạch của Hàn & Thanh Mặc vô tình chỉ làm điểm khai mạch kế tiếp (`FS-016`, `D-03`) | §2 trên |

---

## §5 — `SECT-001-OUTER` Ngoại môn Thái Nhạc Tông (`TC-KHTL-A2-OUTER`)

- **Geo:** Sườn nam – đông nam núi Thái Nhạc (~+400m), gồm ba cụm: **Khu tạp dịch ngoại viện** (lán đá thấp sát rìa sườn núi cho đệ tử mới thăng từ khu mỏ), **Đan các ngoại viện / Sảnh phát đan** (nơi phát đan định kỳ và niêm yết bảng công tích chờ ngạch Trúc Cơ Đan), và **Phòng khảo mạch – Linh dược viện** (nơi lưu trữ phiếu đo mạch Tây Mạch).
- **Social & Economy:** Quy tắc vận hành bằng **sổ công tích** và **khế bảo lãnh**. Đệ tử từ mỏ lên như Lâm Hàn mang thân phận *ngoại môn hạ đẳng*, mỗi tháng phải nộp đủ công tích khảo mạch hoặc tạp dịch mới được lãnh đan hạ phẩm. Bảng chờ ngạch Trúc Cơ Đan là chiếc thang hẹp khiến các đệ tử hàn môn như **Khương Minh Thư (`CHAR-011`)** tự biến mình thành người giữ sổ khắc nghiệt nhất.
- **Power:** Linh khí dày hơn khu mỏ nhưng bị trận pháp nội môn hút lên cao; đệ tử ngoại môn phổ biến Luyện Khí tầng 3–9, đỉnh là Luyện Khí tầng 10–12 chờ Trúc Cơ.

---

## §6 — `SECT-001-LAW` Chấp pháp đường (`TC-KHTL-A2-LAW`)

- **Geo:** Sườn bắc cao Thái Nhạc (~+650m), bậc đá xám lạnh, tách biệt khỏi khu sinh hoạt ngoại môn; bên trong có đại sảnh án thư gỗ mun, kho văn thư lưu trữ toàn bộ sổ *dời dân / sự cố / định mức*, và một gian tĩnh thất nhỏ phía sau không treo biển.
- **Social & History:** Do **Nghiêm Hoằng Độ (`CHAR-007`, Kim Đan trung kỳ)** chấp chưởng. Gian tĩnh thất phía sau đặt **chiếc bài vị gỗ không khắc tên** (`FS-014`), nơi mỗi năm vào ngày khai mạch cũ ông đều đốt một nén hương cho mọi «hao hụt hợp pháp».
- **Plot anchor:** Nơi lưu bản chép tờ công trạng số 12 mang chữ *Thạch Khê* (`FS-018`); nơi tiếp nhận bản đồ khảo mạch để chọn thôn khai mạch tiếp theo (`FS-016`); nơi hạ bút gạch tên Lương Khôn (`D-08`) để dập tiếng xấu định mức.

---

## §7 — `CLAN-VE-001` Vệ Thủy Ngân phủ (`TC-KHTL-A2-VE`)

- **Geo:** Đỉnh phụ đông bắc Thái Nhạc (~+700m), tọa lạc ngay trên nhánh linh mạch Kim–Thủy tinh thuần nhất của tông môn; kiến trúc hiên ngói xám bạc, rèm trúc, hồ nước bạc lạnh quanh năm.
- **Social & Economy:** Thế gia nội môn do **Vệ Hoài Trà (`CHAR-012`, Trúc Cơ Đại Viên Mãn)** đứng đầu, nuôi dưỡng đệ tử chân truyền **Vệ Cảnh Hành (`CHAR-005`)** và nhận bảo lãnh môn khách hàn môn (**Khương Minh Thư `CHAR-011`**). Nắm giữ **khế nợ linh thạch của Tần gia** (cộng thêm 3 tháng phạt từ sổ sự cố Arc 1) làm dây trói hôn ước với **Tần Thanh Mặc (`CHAR-004`)** (`D-02`, `FS-010`).
- **Power:** Độc quyền nguồn vật liệu **Kim hệ thượng hạng** (Canh Kim tinh / Thủy Ngân sa) trong phạm vi Thái Nhạc Tông — cổng chặn trực tiếp khiến Lâm Hàn không thể gom đủ hệ Kim khi xung kích Trúc Cơ cuối Arc 2 (`D-06`, `FS-005`).

---

## §8 — `LOC-CITY-001` Cạn Mạch Thành (`TC-KHTL-A2-CITY`)

- **Geo:** Thành phụ nằm ở đồng bằng hẹp phía đông nam chân núi Thái Nhạc (~1,5 ngày đi bộ từ sơn môn), xây trên một nhánh linh mạch phụ đã suy kiệt từ trăm năm trước.
- **Social & Economy:** Nơi cư ngụ của các gia tộc tu tiên hạng bét phụ thuộc Thái Nhạc Tông (như **chi họ Khương** của Khương Minh Thư với người anh phế căn cơ sau lần Trúc Cơ thất bại, và **gia tộc họ Tần** của Tần Thanh Mặc đang canh tác linh điền thế chấp). Phía tây thành có chợ phiên tu sĩ tầng thấp và ngõ tối thông với đường dây chợ ngầm biên Tây Mạch (nơi lưu thông đan độc không dấu của **Tro Lão**).

---

## §9 — `LOC-MINE-002` Cựu Mạch Hầm & `LOC-VIL-003` Lão Mạch Thôn (`TC-KHTL-A2-OLDMINE`)

- **Geo:** Phía tây bắc Hắc Nham Khoáng Động (~1 ngày đường rừng đá hiểm trở hướng về đèo biên Hỏa Diễm). `LOC-VIL-003` (**Lão Mạch Thôn**) chỉ còn nền đá cháy sém dưới khe núi; ngay bên dưới là `LOC-MINE-002` (**Cựu Mạch Hầm**) — hệ thống hầm lò cũ bị đánh sập một nửa, hơi nóng địa nhiệt trộn lẫn mùi tro và dược thảo độc.
- **History & Social:** Mười mấy năm trước, sổ tông ghi nơi đây xảy ra «mạch động tự nhiên» và dân thôn «đã dời», thực chất là một lần mở mạch cũ khiến thị đồng phàm nhân **Đỗ Viễn (`CHAR-010`)** bị bỏ lại dưới đáy (`FS-011`, `FS-019`, `FM-010`). Nay Đỗ Viễn lấy danh **Tro Lão / Giữ Lò**, dựng lò đan lậu dưới đáy hầm cũ để nuôi những kẻ sống sót không còn tên trên sổ tông, đồng thời bán đan tăng tốc rút thọ nguyên cho đám đầu mục và **Chu Thiết (`CHAR-002`)** (`FS-012`).

---

## Naming pending (không ghi registry)

| Gợi ý | Lý do |
| --- | --- |
| **Xích Thạch Lĩnh** | Dãy núi bọc Hắc Nham — prose/world only; [`naming-proposals.md`](../../interface/naming/naming-proposals.md) đã bác làm `LOC-MINE-001` |
| *(Chức danh phụ ngoại môn / chấp sự Đan các)* | Dùng danh xưng chức việc chung (*chấp sự Đan các*, *chấp sự khảo mạch*, *chấp sự Chấp pháp đường*) theo quy ước Arc 1; toàn bộ địa danh chính Arc 2 (`Cạn Mạch Thành`, `Cựu Mạch Hầm`, `Lão Mạch Thôn`, `Vệ Thủy Ngân phủ`) **đã là `canon` trong `registry.md`** |

---

## Handoff

| Agent | Đọc |
| --- | --- |
| `plot-architect` (Arc 1 & Arc 2 beats) | Khoảng cách §7–§8 trong **01**; Bạch Thổ placement **§2**; tiểu cục Ngoại môn / Cạn Mạch / Cựu Mạch **§5–§9** |
| `xianxia-prose-writer` | La bàn micro; **Tây** = Hỏa Diễm / Cựu Mạch; **Đông bắc** = về tông / Thủy Ngân phủ; **Đông nam** = Cạn Mạch Thành |
| `foreshadowing-architect` | Trận đáy mỏ = deferred geometry; Cựu Mạch Hầm = vật chứng mở mạch cũ (`FM-010`, `FS-019`) |

*Cập nhật: 2026-10-23 · world-builder · `T-world-arc-1` (`approved`) & `T-world-arc-2` (delta Arc 2).*
