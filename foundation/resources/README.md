# Foundation / Resources — Catalog tài nguyên & kinh tế

**Lớp:** Foundation — chi tiết hóa `foundation/core/03-power-system-economy-core.md` §3.  
**Không** viết arc; mọi mục phải khớp **Luật 1–5** (`02-world-laws-lore-core.md`).

## Cách đọc catalog

Mỗi file dùng cột hoặc mục theo trục:

| Trục | Ý nghĩa |
| --- | --- |
| **Nguồn** | Linh mạch, bí cảnh, linh điền, yêu lâm, di tích, chế tạo… |
| **Công dụng** | Đan / phù / pháp bảo / đột phá / chiến đấu |
| **Cảnh giới** | Ai dùng được (ước); không thay bảng §1 core |
| **Hiếm** | Thấp → Cực hiếm (tương đối Hạ Giới) |
| **Trade-off** | Thọ nguyên, Nghiệp, đan độc, hao phí, tâm ma |

**Nhãn nguồn:** `[nguồn V2]` · `[nguồn power]` · `[bổ sung sáng tác]`

## Chỉ mục

| File | Nội dung |
| --- | --- |
| [01-linh-thach-tien-te.md](01-linh-thach-tien-te.md) | Linh thạch, quy đổi, giao dịch |
| [02-linh-duoc.md](02-linh-duoc.md) | Linh dược |
| [03-dan-duoc.md](03-dan-duoc.md) | Đan dược |
| [04-dan-phuong.md](04-dan-phuong.md) | Đan phương |
| [05-phap-bao.md](05-phap-bao.md) | Pháp bảo danh xưng |
| [06-phu-luc.md](06-phu-luc.md) | Phù lục |
| [07-yeu-dan-va-vat-lieu.md](07-yeu-dan-va-vat-lieu.md) | Yêu đan & vật liệu phụ |
| [08-tran-phap.md](08-tran-phap.md) | Trận pháp |
| [09-shentong-va-cong-phap.md](09-shentong-va-cong-phap.md) | Thần thông & công pháp (tiêu hao §0) |
| [10-phu-nghe-tu-tien.md](10-phu-nghe-tu-tien.md) | Phụ nghề — đan, khí, trận, phù, linh điền, sủng thú, bói toán… |
| [11-thien-phu-ky-nang-an.md](11-thien-phu-ky-nang-an.md) | Pool lore — thiên phú dị bẩm, kỹ năng ẩn, pháp bảo nghịch thiên |

**Hub Core:** [§3 Phân cấp tài nguyên](../core/03-power-system-economy-core.md#3-phân-cấp-tài-nguyên)

---

## Biên tập nguồn

| Nguồn | Vai trò trong catalog |
| --- | --- |
| `foundation/sources/Xây dựng thế giới tu tiên V2.md` §8–10 | Phụ nghề (Luyện Đan, Phù Lục), tiền tệ, đan/dược tên, thang pháp bảo, loại trang bị |
| `foundation/sources/Hệ Thống Cấp Bậc Sức Mạnh.md` | Gắn cảnh giới, kiếp nạn (đan hỗ trợ Lục Cửu / Cửu Cửu — sketch) |
| `foundation/core/03-power-system-economy-core.md` | Trần chiến lực, vòng kinh tế, Ma shortcut |
| `foundation/core/02-world-laws-lore-core.md` | Luật 1–5: Ma khí, Nhân-Quả, kiếp nạn, địa danh kiểu |
| `foundation/core/00-glossary.md` | Chuẩn Hán Việt (Linh thạch, Yêu đan, Thiên kiếp…) |

**Quy ước:** Mục V2/power giữ nhãn; mở rộng có logic kinh tế & cảnh giới được đánh dấu `[bổ sung sáng tác]`. Đan **Ma / Cấm** ghi **Nhân-Quả** khi nuốt trực tiếp hoặc luyện bằng hiến tế.

## Promotion từ tác phẩm ( làm giàu Foundation )

Khi sáng tác (prose, naming registry) **tạo yếu tố mới** có tên canon (công pháp, phù, pháp bảo, địa danh lặp lại…):

| Bước | Việc | Đích file |
| --- | --- | --- |
| 1 | Kiểm tra **đã có** trong `foundation/resources/` hoặc `00-glossary.md` | Tránh trùng |
| 2 | **Không** ghi tên riêng vào `foundation/core/` trừ ticket (Core = luật/invariant) | Giữ Core ổn định |
| 3 | Thêm **một dòng catalog** (hoặc mục) vào resource đúng loại | Xem bảng dưới |
| 4 | Gắn nhãn `[bổ sung sáng tác]` + `work_slug` / chương xuất hiện | Traceability |
| 5 | Cập nhật `interface/naming/registry.md` → cột Notes trỏ `foundation/resources/…` | Interface ↔ Foundation |

| Loại yếu tố | File catalog |
| --- | --- |
| Công pháp, thân pháp, thuật, thần thông (tên) | `09-shentong-va-cong-phap.md` §2.1 / §3 |
| Phù lục | `06-phu-luc.md` |
| Pháp bảo / pháp khí | `05-phap-bao.md` |
| Trận pháp / trận đĩa | `08-tran-phap.md` |
| Đan / đan phương | `03-dan-duoc.md`, `04-dan-phuong.md` |
| Linh dược, vật liệu, yêu đan | `02`, `07` |
| Phụ nghề (nghề nghiệp) | `10-phu-nghe-tu-tien.md` |
| Thiên phú / variant căn | `11-thien-phu-ky-nang-an.md` |
| Thuật ngữ hệ thống chung | `../core/00-glossary.md` |

*Catalog phiên bản: 1.4 — 2026-09-07; thêm quy trình promotion từ tác phẩm.*
