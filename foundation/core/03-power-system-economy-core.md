# Foundation / Core — Power System & Economy

**Lớp:** Foundation (Core) — không viết chương, không chốt theme/bi kịch nhân vật.  
**Tham chiếu luật thế giới:** `foundation/core/02-world-laws-lore-core.md` (Linh khí, địa mạch, Thiên đạo, Nhân-Quả).  
**Thần thông & công pháp:** `foundation/resources/09-shentong-va-cong-phap.md` · **Trận pháp (catalog):** `foundation/resources/08-tran-phap.md`.  
**Power ceiling canon:** Chuỗi cảnh giới đầy đủ đến **Thánh Nhân** theo nguồn; arc **Hạ Giới** có thể kết tại **Độ Kiếp / Phi Thăng** — tránh inflation trong phạm vi truyện bằng **khoảng cách đại cảnh giới** và **điểm nghẽn tài nguyên**, không bằng cách cắt bậc.

---

## Biên tập nguồn

| Nguồn | Đường dẫn | Vai trò | Xử lý |
| --- | --- | --- | --- |
| Hệ thống cấp bậc (primary) | `foundation/sources/Hệ Thống Cấp Bậc Sức Mạnh.md` | Số liệu cảnh giới, tuổi thọ, kiếp nạn, Tiên Giới | **Chuẩn** — bảng §1 dùng trực tiếp |
| Thế giới tu tiên V2 | `foundation/sources/Xây dựng thế giới tu tiên V2.md` | §3 progression, §9 công pháp, §10 vật phẩm/tiền tệ | **Chuẩn** — phân cấp tài nguyên & tiền tệ |
| Thế giới tu tiên V1 | `foundation/sources/Xây dựng thế giới tu tiên.md` | Trùng V2 §2–3, §8–9 | **Gộp vào V2**; không giữ mâu thuẫn |
| Skeleton cũ `03-power-system-economy-core` | — | Luyện Khí **13** tầng, trần **Đại Thừa**, tuổi thọ khác nguồn | **Bỏ** |
| World laws Core | `foundation/core/02-world-laws-lore-core.md` | Kiếp nạn, linh khí | Checklist sync; điều chỉnh **Luật 5** theo bảng dưới |

**Quy ước đo lường (áp dụng khi viết Logic/Interface):**

- **Thần thức / Linh lực:** phạm vi cảm tri + quy mô linh lực điều khiển được (nguồn ghi km / quốc gia — dùng tương đối, không đổi số tuổi thọ).
- **Tuổi thọ:** trần theo cảnh giới nguồn; đan/bí pháp/Ma đạo có thể lệch — phải có **trade-off** (§5).
- **Chiến đấu ưu thế:** loại đối kháng đặc trưng tầng (cận chiến / thuật pháp / pháp bảo / quy luật / không gian).

---

## 1. Bảng cảnh giới

### 1.1. Phàm nhân & Dẫn khí (tiền tu sĩ)

| Tên | Đặc trưng | Tuổi thọ (ước) | Năng lực chiến đấu | Điều kiện đột phá | Kiếp nạn / rủi ro |
| --- | --- | --- | --- | --- | --- |
| **Phàm Nhân** (凡人) | Nhược thể tráng niên; chưa cảm quan linh khí | 60–80 năm | Sức 50–100 kg; vũ khí phàm; không chống phù/linh lực | — | Bệnh tật, môi trường |
| **Luyện Thể Kỳ** (炼体) — **9 tầng** | **1–3:** Sức Bì Phu (da thịt). **4–6:** Đ锻 Cốt Tủy (xương tủy). **7–9:** Thay Máu Đổi Khí (huyết mạch) | ~100 năm | Sức đấm đá **100 kg–2.000 kg**; tốc độ ×2–3 phàm nhân; **không** Thần Thức / Linh Lực | Bài tập khắc nghiệt; linh dược ngâm thân; đả thông **ngoại kinh** | Chấn thương kinh mạch; lệ thuộc dược liệu |
| **Luyện Khí Kỳ** (炼气) — **12 tầng** | **1–3 (Sơ):** khai kinh mạch, dẫn khí vào Đan Điền. **4–6 (Trung):** khí hóa lỏng sơ bộ. **7–9 (Hậu):** linh lực tràn mạch, Thần Thức sơ khai. **10–12 (Viên Mãn):** 108 huyệt, chuẩn bị ép khí hóa lỏng | 120–150 năm | **1–3:** bùa thấp, nhẹ như chim. **4–6:** ma pháp tiểu hình, Pháp Khí sơ cấp. **7–12:** ngự kiếm ngón tay; Thần Thức **10–100 m** | **Linh Căn**; thiền định hấp thu linh khí; **Tụ Khí Đan**, **Tẩy Tủy Đan** | Kinh mạch nứt; tẩu hỏa nhập ma nếu cưỡng công |

**Nhánh hội nhập:** Võ tu **Luyện Thể** và tu sĩ **Luyện Khí** đều hướng tới **Trúc Cơ**; Luyện Khí là đường chính thống có Linh Căn; Luyện Thể bổ thân trước khi dẫn khí (hoặc song hành tùy môn phái — Logic layer chốt từng phe).

### 1.2. Hạ Giới — chân tu

| Tên | Tiểu cảnh giới | Tuổi thọ (ước) | Năng lực chiến đấu | Điều kiện đột phá | Kiếp nạn / rủi ro |
| --- | --- | --- | --- | --- | --- |
| **Trúc Cơ Kỳ** (筑基) | Sơ → Trung → Hậu → **Đại Viên Mãn** | 200–300 năm | Ngự kiếm phi hành xa; linh khí trung/cao cấp; Thần Thức **vài km**; phá hoại **đồi núi nhỏ** | Ép linh khí **khí → lỏng** (Linh Dịch) tại Đan Điền; **Trúc Cơ Đan** hoặc **Linh Mạch** dồi dào | Tỷ lệ thất bại cao nếu căn cơ yếu; đan độc / cơ bất toàn |
| **Kim Đan Kỳ** (金丹) | Sơ → Trung → Hậu → Đại Viên Mãn; **phẩm đan:** Hạ / Trung / Thượng / Cực / **Thiên Đan** | 500–800 năm | Linh lực khó cạn; Cổ Bảo, Trận Đĩa trung cấp; **hủy thành trì nhỏ** nhanh | Cô đọng Linh Dịch → **Kim Đan** bất hoại | **Tâm Ma Kiếp** sơ cấp **hoặc** **3 luồng Lôi Kiếp** (nhẹ); vỡ đan |
| **Nguyên Anh Kỳ** (元婴) | Sơ → Trung → Hậu → Đại Viên Mãn | 1.000–2.000 năm | Nguyên Anh xuất xác, **Thuấn Di** ngắn; xé không gian ngắn hạn; **phá hủy đại đô thị** | Đập Kim Đan → Nguyên Anh (linh thai) | **Lục Cửu Thiên Kiếp** (6 đợt sấm) + **Tâm Ma Kiếp** khắc nghiệt; đoạt xá nếu thể diệt |
| **Hóa Thần Kỳ / Thần Du** (化神) | Sơ → Trung → Hậu → **Viên Mãn** | 3.000–5.000 năm | **Đỉnh Phàm Giới**; Thần thức **quốc gia / đại lục**; điều động **Linh Khí Thiên Địa** (không chỉ linh lực cá nhân) | Nguyên Anh + Tinh Thần Lực; cảm **Ý Cảnh / Quy Luật** sơ bộ; bế quan **hàng trăm năm** | Ngộ đạo sai → tâm ma; lộ khí → truy sát |

### 1.3. Trung / Thượng Giới — Độ kiếp thăng tiên

| Tên | Tiểu cảnh giới | Tuổi thọ (ước) | Năng lực chiến đấu | Điều kiện đột phá | Kiếp nạn / rủi ro |
| --- | --- | --- | --- | --- | --- |
| **Luyện Hư / Động Hư** (炼虚) | Sơ → Trung → Hậu | 8.000–10.000 năm | Thao túng **lực lượng không gian**; giam đối thủ trong hư không; Trọng Vực / Động Thiên nhỏ trong thân hoặc thần thức | Luyện hóa hư không, dựng không gian độc lập | **Hư không phản phệ**; tiêu hao cực đại |
| **Hợp Thể / Đại Thừa** (合体/大乘) | Sơ → Trung → Hậu → Viên Mãn | **20.000+** năm | **Đại Thừa:** chưởng vỡ đại lục, chuyển sông dời núi; linh lực → **Tiên Nguyên Lực** sơ cấp | Dung hợp Thần Thức, Thể Xác, Quy Luật Thiên Địa; xóa khuyết điểm phàm thể | Thân phân bất hòa; tâm ma hợp thể |
| **Độ Kiếp Kỳ** (渡劫) | Sơ → Trung → Hậu → **Đột Phá Phi Thăng** | (chuẩn bị Tiên thể) | **Đỉnh Hạ Giới**; sức **chuẩn Tiên Nhân**; có thể **phá ranh giới giới** để phi thăng | Hoàn tất Đại Thừa; đón kiếp | **Cửu Cửu Lôi Kiếp** (**81** đạo lôi — mạnh nhất Hạ Giới); thất bại sống sót → **Tản Tiên** (lôi kiếp định kỳ) |

### 1.4. Tiên Giới & cao cấp (sketch)

| Bậc | Đặc trưng cốt lõi | Tuổi thọ / bất tử | Năng lực (tóm) |
| --- | --- | --- | --- |
| **Chân Tiên** (真仙) | Tiên Thể; linh lực → **Tiên Nguyên Lực** | Ngang **tiểu thế giới** (triệu năm) | Sinh tồn & tu luyện trong Tiên Giới |
| **Kim Tiên** (金仙) | **Kim Tiên Quy Tắc** | Bất hoại trước đòn dưới cảnh giới | Kháng sát thương cấp quy tắc |
| **Thái Ất Kim Tiên** (太乙金仙) | Quy luật **Thời Gian** hoặc **Không Gian** cao cấp | — | Du hành vạn giới |
| **Đại La Kim Tiên** (大罗金仙) | Thoát **Ngũ Hành**, ngoài **Luân Hồi** | Đồng thọ Thiên Địa | — |
| **Tiên Vương / Tiên Đế** | Chủ **Quy Luật Đại Đạo** tối cao (trong phạm vi lore) | — | Sáng tạo / hủy diệt tinh hà bằng ý niệm |
| **Thánh Nhân** (混元圣人) | Tuyệt đối bất diệt | Vũ trụ diệt vẫn tồn tại | Tái tạo **Chư Thiên Vạn Giới** |

**Khoảng cách đại cảnh giới:** Một đại cảnh giới ổn định so với đầu cảnh giới dưới thường **bậc logarit** (10×–100× hiệu quả linh lực / quy tắc) — không linear vô hạn; **Tiên Giới** dùng **Tiên Nguyên / quy tắc**, không quy về “số tầng Luyện Khí”.

---

## 2. Quy tắc chiến lực

### 2.1. Trần & nguyên tắc không vi phạm

1. **Cảnh giới là nền:** Kỹ năng tối ưu trong cùng đại cảnh giới hoặc lấn **một bậc tiểu cảnh giới**; không “ý chí” bù trừ thiếu cảnh giới lớn.
2. **Linh khí thiên địa (Hóa Thần+):** Chiến kéo dài **rút cạn linh mạch** — khớp **Luật 1–2** (`02-world-laws-lore-core.md`).
3. **Thọ mệnh là tài nguyên:** Shortcut (Ma đạo, bạo đan) đổi lấy thọ nguyên hoặc trần đột phá sau (§5).
4. **Kiếp nạn theo nguồn:** Kim Đan — Tâm Ma hoặc Lôi nhẹ; Nguyên Anh — **Lục Cửu**; Độ Kiếp — **Cửu Cửu (81)**; sync **Luật 5** world-laws (sửa ngưỡng “chỉ từ Nguyên Anh” thành **Kim Đan có kiếp tùy đường**, bắt buộc nặng từ **Nguyên Anh**).

### 2.2. Vượt cấp — điều kiện cứng

| Cơ chế | Điều kiện | Giới hạn |
| --- | --- | --- |
| **Pháp bảo cao hơn phẩm** | Nuôi bằng linh thạch; người dùng đủ linh lực (ước: ≥ Luyện Khí tầng 7 cho Pháp Khí mạnh) | Không vượt **một đại cảnh giới** ổn định; hao pháp lực / hồn phách |
| **Đan / bạo pháp** | Phệ huyết, Tục Mệnh, v.v. (§3.2) | Thời gian ngắn; tổn **Thọ Nguyên** hoặc gãy đan đạo |
| **Trận pháp (合阵)** | ≥3 tu sĩ + Trận đĩa + linh thạch | ≈ cảnh giới cao nhất +1 bậc tiểu; phá **阵眼** — chi tiết `08-tran-phap.md`, luật trận §3.7 |
| **Huyết mạch / Cổ trận** | Gia tộc / di tích Thượng cổ | Một lần hoặc hiến tế — `(bí mật)` lore |
| **Địa lợi** | Linh mạch, cấm địa | Không mang theo |

**Cấm tuyệt đối (Hạ Giới arc):** Phàm nhân / Luyện Khí sơ kỳ **không** giết **Kim Đan ổn định** chỉ bằng võ công thường — cần pháp bảo cực phẩm + trận + địa lợi + đối thủ suy yếu trước.

### 2.3. Hao tài nguyên chiến đấu

- **Pháp khí / Linh khí:** tiêu hao theo trận; chiến tranh tông môn = hậu cần linh thạch.
- **Nguyên Anh xuất khiếu:** hao Nguyên Thần lực; hồi bằng đan hồn + linh thạch thượng phẩm.
- **Cổ bảo / Tiên bảo:** hủy phẩm → mất đường đột phá; áp lực kinh tế cực cao.
- **Thần thông / thuật / công pháp chiến đấu:** tiêu hao **linh khí (linh lực), thần thức, thể lực** người thi triển `(invariant)` — xem `09-shentong-va-cong-phap.md` §0; Hóa Thân+ có thể hút **linh khí thiên địa** bổ sung linh lực, không miễn thần thức / thể lực.
- **Trận pháp (duy trì):** linh thạch + mạch + nhân trấn nhãn — xem `08-tran-phap.md` §3.

---

## 3. Phân cấp tài nguyên

**Hub / tổng quan** — chi tiết từng loại nằm trong `foundation/resources/` (catalog có cột **Nguồn / Công dụng / Cảnh giới / Hiếm / Trade-off**). Công pháp §9 (V2): **Hoàng → Huyền → Địa → Thiên → Tiên → Thần**, mỗi cấp **Hạ / Trung / Thượng / Cực phẩm** — dùng tham chiếu cho phù, đan phương độ khó, không thay thang pháp bảo §3.3.

| Catalog | Nội dung |
| --- | --- |
| [`foundation/resources/README.md`](../resources/README.md) | Chỉ mục & cách đọc |
| [`01-linh-thach-tien-te.md`](../resources/01-linh-thach-tien-te.md) | Hạng linh thạch, quy đổi, ví dụ giao dịch |
| [`02-linh-duoc.md`](../resources/02-linh-duoc.md) | Linh dược (≥15 mục) |
| [`03-dan-duoc.md`](../resources/03-dan-duoc.md) | Đan dược theo tầng cảnh giới |
| [`04-dan-phuong.md`](../resources/04-dan-phuong.md) | Đan phương & monopoly |
| [`05-phap-bao.md`](../resources/05-phap-bao.md) | Pháp bảo danh xưng + phẩm |
| [`06-phu-luc.md`](../resources/06-phu-luc.md) | Phù lục |
| [`07-yeu-dan-va-vat-lieu.md`](../resources/07-yeu-dan-va-vat-lieu.md) | Yêu đan & vật liệu phụ |
| [`08-tran-phap.md`](../resources/08-tran-phap.md) | Trận pháp — loại, phẩm, tiêu hao |
| [`09-shentong-va-cong-phap.md`](../resources/09-shentong-va-cong-phap.md) | Thần thông, công pháp, thuật, tiêu hao §0 |
| [`10-phu-nghe-tu-tien.md`](../resources/10-phu-nghe-tu-tien.md) | Phụ nghề — hạng sư, cống hiến, liên catalog |
| [`11-thien-phu-ky-nang-an.md`](../resources/11-thien-phu-ky-nang-an.md) | Pool lore — thiên phú, kỹ năng ẩn, pháp bảo nghịch thiên |

### 3.1. Linh thạch & tiền tệ

→ Chi tiết: [`01-linh-thach-tien-te.md`](../resources/01-linh-thach-tien-te.md)

| Hạng | Hiếm (ước) | Công dụng chính | Gắn cảnh giới |
| --- | --- | --- | --- |
| **Hạ phẩm** | Thấp | Tu Luyện Khí; trận hạ cấp | Luyện Khí, ngoại môn |
| **Trung phẩm** | Trung bình | Trúc Cơ, Kim Đan hàng ngày | Trúc Cơ–Kim Đan |
| **Thượng phẩm** | Cao | Nguyên Anh; nuôi Linh khí / Cổ bảo | Kim Đan–Nguyên Anh |
| **Cực phẩm** | Rất cao | Hóa Thần+; chiến tranh giới hạn | Hóa Thần–Luyện Hư |
| **Tiên thạch** | Tiên Giới / di tích | Tu Tiên Giới; giao dịch cao cấp | Độ Kiếp+ / Phi thăng |

**Monopoly:** Tông môn & gia tộc khống chế **mỏ + linh mạch lõi**; tán tu phụ thuộc nhiệm vụ, thương hội, hắc thị.

### 3.2. Đan dược & linh dược (tóm tắt)

→ Đan: [`03-dan-duoc.md`](../resources/03-dan-duoc.md) · Dược: [`02-linh-duoc.md`](../resources/02-linh-duoc.md)

| Nhóm | Vai trò kinh tế | Nghẽn / trade-off |
| --- | --- | --- |
| **Luyện Khí** (Tụ Khí, Tẩy Tủy…) | Tiêu thụ hàng loạt; ngoại môn | Đan độc nếu phẩm kém |
| **Trúc Cơ** (Trúc Cơ Đan) | **Then chốt** Hạ Giới sớm | Monopoly Đan các; thất bại = tổn căn |
| **Kim Đan–Nguyên Anh** (Ngưng Đan, Hồi Nguyên…) | Đan phương bí truyền | Công thức = chiến lợi phẩm |
| **Hồi phục / thọ** (Hồi Xuân, Tục Mệnh) | Đấu giá; lão tổ | Tục Mệnh **bóp thọ** / Nghiệp (Luật 4) |
| **Ma / Cấm** | Hắc thị | Nhân-Quả; Tâm ma, Thiên oán |

**Linh dược then chốt (V2):** Tuyết Lớp, Cửu Diệp Chi, Nhân Sâm nghìn năm, Thiên Nguyện Hoa — map đan phương tại §3.6 & `04-dan-phuong.md`.

### 3.3. Pháp bảo (thang V2)

→ Ví dụ danh xưng: [`05-phap-bao.md`](../resources/05-phap-bao.md)

| Phẩm | Tương ứng tu vi (ước) | Hiếm | Ghi chú |
| --- | --- | --- | --- |
| **Pháp khí** (法器) | Luyện Khí–Trúc Cơ | Thấp–TB | Luyện Khí tầng 4–6 dùng sơ cấp |
| **Linh khí** (灵器) | Trúc Cơ–Kim Đan | TB | Cần nuôi khí |
| **Cổ bảo** (古宝) | Kim Đan–Nguyên Anh | Cao | Kim Đan dùng “Cổ Bảo, Trận Đĩa trung” |
| **Tiên bảo** (仙宝) | Hóa Thần–Độ Kiếp | Rất cao | Liên quan phi thăng |
| **Thần khí** (神器) | Tiên Giới sơ | Cực hiếm | — |
| **Chí bảo Thiên Địa** (天地至宝) | Thượng cổ / plot | Một | Điều kiện lore cứng |

**Loại thường gặp:** phi kiếm, lò luyện đan, nhẫn/túi không gian, trận đĩa, bùa hộ mệnh.

### 3.4. Yêu đan (妖丹)

→ Chi tiết: [`07-yeu-dan-va-vat-lieu.md`](../resources/07-yeu-dan-va-vat-lieu.md)

| Nguồn | Phẩm | Công dụng | Hệ quả |
| --- | --- | --- | --- |
| Yêu thú hạ giai | Hạ–Trung | Phù, Luyện Khí | Săn yêu cơ bản |
| Yêu thú **≈ Kim Đan–Nguyên Anh** | Trung–Cao | Đan phương, tăng tốc tu luyện | Xung đột nhân–yêu |
| **Yêu Vương** nội đan | Thượng–Cực | Đột phá / luyện bảo | Truy sát tộc; Ma đạo **nuốt đan trực tiếp** → Nhân-Quả nặng |

### 3.5. Phù lục (符箓)

→ Catalog: [`06-phu-luc.md`](../resources/06-phu-luc.md)

**Vai trò kinh tế:** Phù là **hàng tiêu hao tức thời** — bù khoảng cách tiểu cảnh giới trong thời gian ngắn, không thay đan đột phá. **Phù sư** (V2 §8) cạnh tranh với Luyện Đan / Trận pháp về **điểm cống hiến** tông môn; phù cao cấp cần **mực linh / da yêu / linh sa** → liên kết săn yêu & linh dược.

| Khía cạnh | Tóm tắt |
| --- | --- |
| **Phân cấp** | Thường theo **công pháp phù** (Hoàng→Thiên) *hoặc* thang phù riêng (Hạ→Thiên Phù) — xem catalog |
| **Sản xuất** | Vẽ tại chỗ (chiến trường) vs **phù đúc sẵn** (đấu giá); hao **Thần thức / linh lực** người vẽ |
| **Lưu thông** | Ngoại môn dùng phù hạ; trận doanh / hộ tống mua sỉ; **cấm phù** (Huyết, Đoạt Mệnh) hắc thị |
| **Trade-off** | Một lần / vài lần; không nuôi khí như pháp bảo; phù vượt cấp → **nứt hồn phách** nếu lạm dụng |

### 3.6. Đan phương (丹方)

→ Catalog: [`04-dan-phuong.md`](../resources/04-dan-phuong.md)

**Vai trò kinh tế:** Đan phương = **bản quyền công nghệ** — quyết định ai luyện được **Trúc Cơ Đan**, **Ngưng Đan**, đan hồi Nguyên Anh. Giá trị often **> một lô đan** vì tái lập sản xuất. **Luyện Đan Sư Hiệp Hội** (V2 §6) chứng nhận phẩm cấp; tông **monopolize** phương lõi, chỉ bán **đan thành phẩm** hoặc đổi phương bằng **công tích / huyết khế**.

| Khía cạnh | Tóm tắt |
| --- | --- |
| **Thành phần** | Liên kết `02-linh-duoc.md` (Tuyết Lớp, Cửu Diệp Chi, Thiên Nguyện Hoa…) |
| **Rào cản** | Cần **Luyện Đan sư** đủ cấp + **lò đan** phẩm; thất bại luyện = hủy nguyên liệu (áp lực kinh tế) |
| **Tranh đoạt** | Đánh cắp phương, mai rùa, ám sát đan sư; **Ma phương** (huyết luyện) — Nghiệp nặng, vẫn có thị trường ngầm |
| **Plot pressure** | Tán tu **yếu trung bình** ( thiếu đan / mạch ) nhưng **đỉnh hiếm, mạnh** nhờ tích lũy bảo khí & thần thông; phụ thuộc hắc thị / Sát Thủ Các; một **phương lậu** có thể đảo cân tông nhỏ |

### 3.7. Trận pháp (阵法)

→ Catalog: [`08-tran-phap.md`](../resources/08-tran-phap.md) · Chiến lực hợp trận: §2.2 · Thần thông (khác trận): [`09-shentong-va-cong-phap.md`](../resources/09-shentong-va-cong-phap.md)

**Vai trò kinh tế:** Trận = **dự án tiêu hao** (linh thạch, trận kỳ, **linh mạch**, nhân trấn **阵眼**) — không thay đan đột phá. **Trận sư** (V2 §8) tranh cống hiến với Đan / Phù. **Hộ sơn đại trận** = tài sản tông gắn Động Thiên.

| Khía cạnh | Tóm tắt |
| --- | --- |
| **Phẩm trận đồ** | Hoàng→Thần (Hạ/Trung/Thượng/Cực) — độ phức tạp |
| **Quy mô** | Cá nhân → hộ sơn → sát trận giới → truyền tống |
| **Nguồn** | Trận sư, truyền thừa, di tích cổ, Ma/huyết trận (Nghiệp) |
| **Tiêu hao** | Linh thạch liên tục; trận đĩa (`05-phap-bao.md`); rút cạn mạch nếu trận lớn |

---

## 4. Vòng kinh tế

```text
Nguồn → Lưu thông → Điểm nghẽn (đột phá) → Tranh đoạt → Plot pressure
```

| Khâu | Nội dung |
| --- | --- |
| **Nguồn** | Linh mạch, linh điền, mỏ (hạ→cực linh thạch), yêu thú/yêu đan, linh dược (Tuyết Lớp, Cửu Diệp Chi…), bí cảnh cổ tích, chiến lợi phẩm |
| **Lưu thông** | Tông môn (công tích → linh thạch/đan); **Bách Hóa Đường / đấu giá**; **Luyện Đan Sư Hiệp Hội**; hắc thị (Tục Mệnh, đan cấm) |
| **Điểm nghẽn** | **Tẩy Tủy / Tụ Khí** (Luyện Khí 10–12); **Trúc Cơ Đan + linh mạch** (Trúc Cơ); phẩm **Kim Đan** (Thiên Đan vs Hạ); **Lục Cửu** chuẩn bị (linh mạch cấp tông, hộ pháp); **Cửu Cửu** (tài nguyên Đại Thừa + đan Tiên giai) |
| **Tranh đoạt** | Chiến mỏ; ám sát tranh **đan phương**; phong ấn di tích; thuế linh mạch; đoạn mạch đối phương (Luật 2) |
| **Plot pressure** | Tán tu **thiếu Trúc Cơ Đan trung bình** ( không “yếu tuyệt đối” ); đỉnh tán tu vs tông = **bảo khí + kinh nghiệm** vs **mạch + hộ pháp**; nội môn tranh **Đan các**; lão tổ hết thọ → liều Ma đạo; phi thăng = tranh **Tiên thạch** & quyền vào thượng giới |

**Ai kiếm gì / cần gì để đột phá**

| Nhóm | Kiếm | Cần đột phá (then chốt) |
| --- | --- | --- |
| Tán tu / ngoại môn | Nhiệm vụ, săn yêu, hắc thị, **Sát Thủ Các** | Linh thạch, **Tụ Khí/Tẩy Tủy**, **Trúc Cơ Đan**, công pháp; đỉnh: **pháp bảo / thần thông mảnh** |
| Đệ tử nội môn | Công tích, sư phụ | **Trúc Cơ Đan**, linh mạch, công pháp Huyền–Địa |
| Gia tộc | Mỏ + huyết mạch | Linh mạch, đan cao cấp, bí truyền |
| Ma đạo | Hút tu, yêu đan, hiến tế | Nhanh tới Kim Đan; **Tâm Ma / Nghiệp** chặn Hóa Thần+ |

---

## 5. Ma đạo / shortcut

**Lợi ích:** Tốc độ 2–5× ở Luyện Khí–Kim Đan; bỏ qua một phần dược liệu bằng **hút linh / nuốt yêu đan / phệ huyết**; chiến lực tức thời mạnh hơn cùng tầng.

**Cái giá:** **Sát khí & Nghiệp** (Luật 4 world-laws); **Thọ Nguyên** giảm hoặc kẹt Hóa Thần; **Tâm Ma** gắn hành vi; **Thiên Kiếp** nặng hơn (Cửu Cửu không thương); phụ thuộc hắc thị; bị coi là **lò đan sống**.

**Ai dễ sa vào (Logic — sync nhân vật):** Hết thọ trước đủ tài nguyên chính đạo; bị tông **ép hy sinh**; linh căn tổn → vá bằng yêu đan/Ma công; báo thù không đủ thời gian tu thuần.

---

## 6. Checklist đồng bộ Core

### Cần **world-laws-lore-architect** (`02-world-laws-lore-core.md`)

- [ ] **Luật 5:** Cập nhật ngưỡng kiếp — **Kim Đan** (Tâm Ma / 3 lôi), **Nguyên Anh** (Lục Cửu + Tâm Ma), **Độ Kiếp** (Cửu Cửu 81), **Tản Tiên**.
- [ ] Phân bổ **Linh khí** Hạ / Thượng Giới vs mật độ tu luyện bảng trên (Tiên Giới “dào dạt” — V2 §4).
- [ ] **Thiên đạo / lách kiếp** Ma đạo có vi phạm invariant không.
- [ ] **Yêu Giới / Ma Giới** — yêu đan & Ma khí vs Luật 1 (Ma khí ô nhiễm).
- [ ] Di tích Thượng cổ: pháp bảo **Chí bảo** vs trần **Hóa Thần / Độ Kiếp** trong arc.
- [ ] **Phi Thăng:** ranh giới thế giới — kinh tế **Tiên thạch** sau khi lên Tiên Giới.

### Cần **theme-tragedy-architect** (`01-theme-tragedy-core.md`)

- [ ] **Vô tình / Hữu tình đạo** vs **Cường giả vi tôn** (V2 §2) — ai monopolize Trúc Cơ Đan.
- [ ] Gray morality: Chính đạo **Đan các** có từ chối cứu người thiếu đan không.
- [ ] Bi kịch MC ↔ **Tục Mệnh / Ma đạo / hi sinh tài nguyên** cho người khác.

### Đã xử lý trong phiên biên tập này

- [x] Luyện Thể **9** tầng + Luyện Khí **12** tầng từ nguồn primary.
- [x] Tuổi thọ & kiếp nạn theo **Hệ Thống Cấp Bậc Sức Mạnh.md**.
- [x] Tiền tệ, đan tên V2, thang pháp bảo V2.
- [x] Bỏ skeleton 13 tầng Luyện Khí & trần Đại Thừa-only.
- [x] §3 hub + catalog `foundation/resources/` (phù, đan phương); phiên bản **1.1**.
- [x] `09-shentong-va-cong-phap.md` (resources) + `08-tran-phap.md`; §3.7 Trận pháp; §0 tiêu hao thần thức/linh khí/thể lực; phiên bản **1.3**.

---

*Phiên bản: 1.3 — Thần thông catalog (`09`), trận pháp (`08`), §3.7, §0 tiêu hao; 2026-09-07.*
