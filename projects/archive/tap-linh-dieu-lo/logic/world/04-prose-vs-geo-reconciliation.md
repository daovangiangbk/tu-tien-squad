# Đối chiếu prose ↔ bản đồ thực địa — Tạp Linh Diêu Lộ
> **Nguồn gốc (canonical):** GeoJSON 4 tầng + `00-world-atlas.md` · `01-region-active.md` · `02-tieu-cuc-index.md`.  
> **Phạm vi prose:** ch.1–112 (`interface/chapters/`).  
> **Campaign:** `T-geo-prose-audit` · agent: `xianxia-prose-writer` (batch).  
> **Cập nhật:** 2026-09-16 · batch-1–**4** prose-writer geo-audit (ch.1–28 · 29–56 · 57–84 · **85–112**) · quét tự động v1.

---

## 1. Quy tắc đối chiếu

| Ưu tiên | Quy tắc |
| --- | --- |
| 1 | **Lệch prose ↔ geo** → sửa **prose** (revise), không sửa `.geojson` trừ human/world-builder. |
| 2 | Hướng tính **từ Thạch Lam** (region hub `LOC-THACH-LAM`); Lan Sa / phế địa **nam–tây nam** hub. |
| 3 | **Phi Vân Tập:** vào **từ tây** (khu phàm); `direction_label`: Nam từ hub. |
| 4 | Khoảng cách: **2–3 ngày** phế ↔ Thạch Lam / Đan Sa (geo `travel_days_*`); «ngàn dặm» = hyperbole nếu không ghi thời gian. |
| 5 | Micro (`arc-01-phi-van-tap`, `arc-01-linh-sa-uyen`) chi tiết layout chợ/uyên — ưu tiên khi cảnh trong micro. |
| 7 | **`chl-ha-gioi-nam.geojson`:** không còn Point Phi Vân / Linh Sa / phế — **region** `reg-thach-lam.geojson` + `reg-lan-sa-chau.geojson` (tách 2026-09-16). |
| 6 | **Tại `LOC-DAN-SA-PHU-MACH`:** «**phụ tây**» / «**đài bắc**» = **phương vị công trường** (hành lang, mõ, khe vá), **không** thay `direction_label` «Đông Nam» **từ** `LOC-THACH-LAM`. **Phế nhánh** / Huyết Sa: cục bộ **dưới** đoạn nhánh #7 sau cắt (TC-008 · `01-region-active.md` §3). |

## 2. Bảng neo bản đồ (region active — chuẩn `LOC-*`)

> Không lấy Phi Vân / Linh Sa / phế từ PNG châu lục; xem [`reg-lan-sa-chau.geojson`](geo/region/reg-lan-sa-chau.geojson) · Thạch Lam → [`reg-thach-lam.geojson`](geo/region/reg-thach-lam.geojson).

| LOC ID | Tên | Hướng (từ Thạch Lam) | Ghi chú geo |
| --- | --- | --- | --- |
| `LOC-BACH-HOA` | Bách Hóa Đường phân điếm | Trung–Đông | Hub đấu giá |
| `LOC-CUU-HUYEN-PHE` | Cửu Huyền Phế Trận | — | — |
| `LOC-DAN-HOI` | Thạch Lam Luyện Đan Hội | Đông | Hội đan III; điểm cống hiến |
| `LOC-DAN-SA-PHU-MACH` | Đan Sa Phụ Mạch | Đông Nam | Nhánh #7; tranh Trúc Cơ |
| `LOC-KIEN-SA` | Kiến Sa Địa | — | Cửa phế Cửu Huyền; coarse trên lục |
| `LOC-LAC-NHAN` | Lạc Nhạn | — | — |
| `LOC-LINH-SA-UYEN` | Linh Sa Uyên | — | Bí cảnh chu kỳ — micro arc-01 |
| `LOC-PHI-VAN-TAP` | Phi Vân Tập | — | — |
| `LOC-THACH-LAM` | Thạch Lam Thành | — | Neo châu lục; region parent_coordinates = điểm này |
| `LOC-THIEN-SA-COT` | Cột Thiên Sa Công Uyên | Tây ngoài thành | Bí cảnh III treo vé; cổng tây |
| `LOC-U-NGO` | U Ngõ | Tây | Hắc thị II; Sát Thủ Các |

## 3. Tóm tắt theo tiểu cục (TC)

| TC | Tiểu cục | Chương prose chính | Khớp bản đồ |
| --- | --- | --- | --- |
| TC-001 | Kiến Sa / Cửu Huyền Phế Trận | 1–14, 34–48, 102–104, 110 | **Khớp** (ARC-REVAMP + review ch.1–4 pass địa lý) |
| TC-002 | Phi Vân Tập · Sa Điêu | 2–8, 11–13 | **Khớp** (vào tây; review ch.3–4 pass) |
| TC-003 | Linh Sa Uyên | 15–28, 20 | **Khớp** (cạnh phế; micro GeoJSON) |
| TC-004–005 | Thạch Lam · U Ngõ | 49–54, 65, 89–99 | **Khớp** (hướng Bách Hóa đông, U Ngõ tây) |
| TC-006 | Đan Sa Phụ Mạch | 55–77, 72 | **Khớp** (layout «phụ tây» = site §1 quy tắc 6; ch.77 **confirm** §4 sau C-01 r1) |
| TC-008 | Phế nhánh / Huyết Sa | 78–84 | **Khớp** (phế sau cắt mạch; review ch.78 meta đã xử lý) |
| TC-009 | Đan Hội Phường | 88–107 | **Khớp** (trong thành; không đảo hướng) |
| TC-007/010 | Thiên Sa · Cửu Huyền leo | 63–65, 102–112 | **Khớp** (cột tây; quay phế nam) |

## 4. Mục lệch / cần prose-writer xác nhận sâu

| Ch | Mức | Prose (tóm tắt) | Bản đồ (canonical) | Hành động đề xuất |
| --- | --- | --- | --- | --- |
| 77 | **confirm** | Hành lang **phụ tây** → khe; sơ đồ lò: điểm son giữa **khe tây nam** & vá phía trên; «**không móc ra trong khe**» (C-01 r1) | `LOC-DAN-SA-PHU-MACH` **Đông Nam** từ hub; **tây nam** = cục bộ khe vá (§1 quy tắc 6) | **Pass** — C-01 đã sửa continuity; giữ «phụ tây» khi MC trên sàn/hành lang (ch.76–78) |
| *phụ tây* | **confirm** | Thuật ngữ **sector** đồn mạch (mõ, tre, cọc leo), lặp ch.55–84 | Không có feature riêng trên `reg-thach-lam.geojson` — **layout in-world** | **Pass** — không retcon geo; đọc theo quy tắc 6, không nhầm «tây» hub Thạch Lam |
| 63 | **confirm** | Ô mười chín · *tây nam, hậu tuyến phụ*; men hành lang **tây nam** | `LOC-THIEN-SA-COT` · **Tây** ngoài thành (hub); MC vẫn tại Đan Sa — **tin vé** / hậu phương | **Pass** — hướng **site** + bí cảnh tây thành, không mâu thuẫn tầng region |
| 65–66 | **confirm** | «**nam**» (xe cát / rời khu) trong arc Đan Sa | Hub: Đan Sa **đông nam**; Thiên Sa **tây** | **Pass** — hướng **nội đồn** & kinh tế vé, không đảo LOC |
| 4 | **note** | «Trước mặt… đường **tây** ra ngoài tập, xa hơn nữa mới tới cát **Kiến Sa**» | `LOC-PHI-VAN-TAP` · ngõ **tây** = ra ngoài; **Kiến Sa** / phế = **đông bắc** sau ngõ (`arc-01-phi-van-tap` · Hứa ch.4) | Revise nhẹ: tách «trước mặt = ngõ tây» vs «Kiến Sa nằm đông bắc / phía đã đi» — tránh đọc Kiến Sa dọc đường tây |
| 14 | **confirm** | Mảnh phản ứng: «chỉ về phía **đông nam**» | Convoy uyên từ Phi Vân: `direction_label` **Tây nam** (`LOC-LINH-SA-UYEN` trên micro Phi Vân); **đông nam** = tuyến tin / địa đồ Thanh Sa (ch.15–16) | **Pass** nếu hiểu là la bàn **thương mại** (tin mua đường), không la bàn hub Thạch Lam; không cần sửa trừ khi muốn thống nhất một hệ la bàn |
| *hyperbole* | note | Nhiều chương «ngàn dặm» cát / về thành (vd. ch.48 rời phế) | ROUTE-PHE-DIA: **2–3 ngày**, không bắt buộc literal ThiênLý | Giữ nếu văn cảnh; tránh số ngày mâu thuẫn |
| 48 | **confirm** | Sát Thủ Các đối diện Bách Hóa trên quảng trường Trung Thành | `LOC-U-NGO` **Tây** hub · Sát Thủ Các trong hắc thị; ch.53 mở rộng **U Ngõ** riêng | **Pass:** ch.48 = mặt tiền liên minh Bách Hóa–Sát Thủ; ch.53 = cửa U Ngõ (không mâu thuẫn tầng region) |
| 53 | **confirm** | «Rời phố Bách Hóa về phía **nam**» → cửa U Ngõ | Hub: U Ngõ **tây** Thạch Lam; Bách Hóa **trung–đông** | **Pass:** đường vòng nội thành / cửa ẩn; không đọc «nam» là hướng hub-west |
| 47 | **confirm** | «Ngã ba đường dẫn về phía **nam**» (chốt Sát Thủ) | Thạch Lam = ánh lam **chân trời** MC hướng tới (từ phế **nam/tây nam** hub) | **Pass:** mô tả **nhánh đường cái** tại trạm, không gán Thạch Lam nằm nam trạm |
| 39 | **note** | Gió **đông** · cát lăn **tây** (kết chương) | Hiện tượng địa khí / phế run (FS-015), không la bàn | Giữ; không revise trừ khi muốn tách «gió thời tiết» vs «sa địa mạch» |
| 86 | **confirm** | «bước **phụ tây**» trên dải phế (sau ca trinh sát **Đoạn**) | MC vẫn trên nhánh **Đan Sa** / tam giác phế — **phụ tây** = sector site (§1 quy tắc 6), không «tây» hub Thạch Lam | **Pass** — cùng họ quy ch.77–84; không mâu thuẫn `LOC-DAN-SA` |
| 89 | **confirm** | Rời **Bách Hóa** → cột **Thiên Sa** «xa **phía tây**» → ngõ **Đan Hội** | `LOC-BACH-HOA` Trung–Đông · `LOC-THIEN-SA-COT` tây ngoài thành · `LOC-DAN-HOI` đông (cạnh Bách Hóa) | **Pass** — trình tự trong ngày: đông (sảnh) → không rẽ tây (cột) → đông (hội phụ); không một câu gộp hướng |
| 96 | **confirm** | «**Bàn tây**» · lô ngoài trong phiên Bách Hóa | Hub region **Trung–Đông**; «tây» = khu bàn/lô **trong** phân điếm, không `direction_label` châu | **Pass** — layout nội sảnh, giống micro chợ (đông/tây nội bộ) |
| 99 | **confirm** | «**Phía tây**, bảng phương» (Hàn Tử Ngư) | Trong sân **Luyện Đan Hội** — vách/bảng phụ; gió cửa lò đẩy khói **bắc** (nội vi) | **Pass** — «phía tây» = góc sân, không đảo `LOC-DAN-HOI` đông |
| 100–103 | **confirm** | Ca **Kiến Sa rìa** · **ba ngày** · về **cổng tây** Thạch Lam | `LOC-KIEN-SA` nam/tây nam hub · `travel_days_*` 2–3 · ca lao = cửa sổ ≥ đi bộ | **Pass** — ch.103 gió/khói «từ Thạch Lam» khi tiến về thành khớp hướng về hub |
| 106–107 | **confirm** | *Đối chiếu* «**nhanh — tây**» / cổng **tây** vs lao tro trong phường | `LOC-THIEN-SA-COT` + tin lậu **U Ngõ** (tây) — «tây» = **miệng trả nhanh**, không bảo MC «ở tây thành» cả arc | **Pass** — kinh tế tin; MC **không** bước cổng tây (chọn chậm) |
| 111–112 | **confirm** | Cột **Thiên Sa** ngoài **cổng tây**; gió **tây** + khói hội | Geo: cột tây · hội đông · MC không vào bí cảnh (vé/hạt) | **Pass** — «Cửu Huyền leo» arc = mảnh/phế nhớ (ch.97–104, 110), không leo phong ấn; không đảo phế nam |
| — | — | *(Batch 57–84 · done)* | `LOC-DAN-SA` · phế TC-008 | §5 ch.57–84; ch.77 **confirm**; §1 quy tắc 6 |

## 5. Bảng chương (quét tự động + phân loại)

**Chú thích trạng thái:** `pass` = có địa lý, không heuristic lệch · `none` = gần như không mô tả địa · `note`/`flag` = xem cột Ghi chú.

| Ch | Slug | TC gợi ý | Địa danh trong prose | Hướng / thời gian (trích) | TT | Ghi chú |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `kien-sa` | TC-001 | Kiến Sa, Cửu Huyền, Phi Vân, Lan Sa, Sa Điêu | phía đông (sáng); — | pass | Mở phế địa; «phía đông» = hướng rời bãi về chợ, khớp tuyến Kiến Sa → Phi Vân trên lục/châu. |
| 2 | `thuan-thien-tan` | TC-001/002 | Kiến Sa, Phi Vân, Cửu Huyền | phía đông; vào Phi Vân **từ tây** | pass | Vào tập qua khu phàm tây khớp `LOC-PHI-VAN-KHU-PHAM-TAY` · vòng tránh đám đông phế. |
| 3 | `tam-he-huyet` | TC-002 | Phi Vân, Cửu Huyền, Kiến Sa | lách **phía tây** trong tập | pass | Layout nội tập; không mâu thuẫn hướng region. |
| 4 | `phi-van-tap` | TC-002 | Phi Vân Tập, Kiến Sa, Sa Điêu, ngõ tây | tây / đông / nam / bắc / **đông bắc** (Hứa) | note | La bàn Hứa khớp micro Phi Vân; một câu mở «đường tây… tới Kiến Sa» dễ đọc nhầm — xem §4 ch.4. |
| 5 | `sa-dieu-do` | TC-001/002 | Sa Điêu, Kiến Sa, Phi Vân | cột đông/tây; hướng rút **tây nam** (tin trận) | pass | Trại **rìa Kiến Sa** (reg/micro); ch.4 suất phế = Sa Điêu. |
| 6 | `bao-ho-phi` | TC-001/002 | Sa Điêu, Kiến Sa | cột **tây** / cánh **đông**; giếng **nam** (ch.7 echo) | pass | Cột tây mép Kiến Sa = layout săn/khai; không đảo LOC hub. |
| 7 | `san-yeu-ha` | TC-002 | Sa Điêu, Phi Vân, Kiến Sa | giếng **nam**; săn **tây**; Sa Điêu rìa Kiến Sa | pass | Giếng nam Hứa ≠ hướng trại; trại sát bãi Kiến Sa (geo 2026-09-17). |
| 8 | `linh-thach-dem` | TC-002 | Phi Vân, ngõ tây, Kiến Sa, Sa Điêu | **tây** (ngõ); — | pass | Giao dịch đêm quanh ngõ tây — micro pass. |
| 9 | `an-phap-so` | TC-002 | Phi Vân Tập, ngõ tây, quầy **đông** | tây / đông | pass | Nội bộ chợ; không xung đột region. |
| 10 | `yeu-dan-doi` | TC-002 | Phi Vân, Sa Điêu, Kiến Sa | cát đỏ **tây** Phi Vân; mép **nam** Kiến Sa (vết lông) | pass | Suy luận vi mô địa hình, không gán Kiến Sa «phía nam» Phi Vân. |
| 11 | `ho-than-phu` | TC-001/002 | Cửu Huyền, Phi Vân | về phế **tây** | pass | Tuyến ngõ tây → Kiến Sa (đông bắc sau ngõ). |
| 12 | `da-hanh-lech` | TC-002 | Phi Vân, dãy lò **phía nam** trong tập | phía nam (nội tập) | pass | Dãy lò nội bộ; không nhầm Sa Điêu ngoài bắc. |
| 13 | `than-thuc-moi` | TC-002 | Phi Vân Tập, ngõ, Kiến Sa | ngõ; **Ba ngày** (dưỡng thần) | pass | «u ngõ» quét tự động = substring **ngõ**; không có U Ngõ thành. |
| 14 | `manh-cuu-huyen-tran` | TC-001/002 | Phi Vân, Kiến Sa, lò; mảnh → **đông nam** | tây / bắc (vòng); đông nam (mảnh) | confirm | Mảnh đông nam = tin thương mại (§4); vòng lò + ngõ tây pass. |
| 15 | `linh-sa-uyen-tin` | TC-003 | Phi Vân, ngõ **tây**, Linh Sa (tin) | gió ngõ tây; tin **đông nam** vs xương không có đông nam | pass | MC thử «đông nam?» — text tự hiệu chỉnh; Thanh Sa «mua đường đông» = kinh tế tin, convoy thực **tây nam** (micro). |
| 16 | `thanh-sa-gia` | TC-003 | Phi Vân, mép **đông** giàn đèn, ngõ **bắc** nội bộ | đông / tây (ngõ) | pass | Khớp `LOC-PHI-VAN-DUONG-DONG` · giếng ngõ bắc nội bộ (≠ giếng nam săn). |
| 17 | `hop-doi-lenh` | TC-003 | Phi Vân, Linh Sa (tin) | giếng ngõ **bắc**; câu đố đông/tây **trong uyên** (ứng viên) | pass | Ngõ bắc nội bộ; đông/tây ở ch.17 là kịch bản lệnh, chưa vào uyên. |
| 18 | `phuong-ngu-han` | TC-003 | Phi Vân → convoy | **11 dặm** cọc 1; **bắc** / **tây bắc** dấu; trạm ngoài | pass | Convoy Phi Vân → `LOC-LSU-TRAM-NGOAI` · hướng dấu khớp micro uyên/trạm. |
| 19 | `toa-do-mua` | TC-003 | Linh Sa Uyên, điểm giao | **mép bắc**, khe xương khô, **tây bắc**; vòng đá dời **nam** | pass | Khớp `arc-01-linh-sa-uyen` (LOC-LSU-MEP-BAC, LSU-KHE-XUONG-KHO). |
| 20 | `vao-uyen` | TC-003 | Linh Sa Uyên | **mép bắc** slot; ba lối dốc | pass | Layout cửa trên / vòng đá I — micro pass. |
| 21 | `tran-slot` | TC-003 | Linh Sa Uyên | **mép bắc** khe; phí slot | pass | `LOC-LSU-MEP-BAC` · ch.21 tranh slot. |
| 22 | `phong-buoc` | TC-003 | Linh Sa Uyên | Phong Bộ / vách (nội uyên) | pass | `LOC-LSU-PHONG-BO-COT` hướng tây — cảnh nội bộ. |
| 23 | `thanh-phong-lien` | TC-003 | Linh Sa Uyên (hang) | hang / dốc (nội uyên) | pass | «Ba ngày» = khí vị lệnh, không thời gian đi bộ region. |
| 24 | `vong-vay` | TC-003 | Linh Sa Uyên | bãi đá / đàn thú (nội uyên) | pass | Không mô tả hướng hub. |
| 25 | `dao-keo` | TC-003 | Linh Sa Uyên | một đêm (nội uyên) | pass | — |
| 26 | `mat-tin` | TC-003 | Linh Sa Uyên | sâu uyên → về phía thoát | pass | Hướng nội micro; cọc Thanh Sa hướng lên = thoát dần. |
| 27 | `loot-chia` | TC-003 | Linh Sa Uyên, Phi Vân; **Thạch Lam** (giá tin) | **ba ngày** (linh dược / suất) | pass | Thạch Lam chỉ là **giá ẩn danh** xa (2–3 ngày hub), MC chưa vào thành. |
| 28 | `ra-uyen` | TC-003 | Thoát uyên → Phi Vân | **3 dặm** vạch trắng, rẽ **đông**; Phương **bắc** | pass | Khớp `LOC-LSU-COC-TRANG` · route «~3 dặm rẽ đông về tập» (micro). |
| 29 | `moi-yeu` | TC-001/004 | Cửu Huyền, Lan Sa, Linh Sa, Linh Sa Uyên, Phi Vân, Phi Vân Tập… | bắc, đông, phía tây, phía nam; Ba dặm, Một đêm, Một ngày | pass | Thoát uyên: cọc trắng → giếng → rẽ **đông** (echo ch.28 micro); đường **bắc** Phương Ngự Hàn = nhánh phế, không đảo hub. |
| 30 | `cuu-hay-khong` | TC-001/004 | Linh Sa, Linh Sa Uyên, Phi Vân | —; Ba dặm | pass | Hậu uyên / Lan Sa; gần như không mô tả hướng region — không heuristic lệch. |
| 31 | `huu-tinh-gia` | TC-001/004 | Lan Sa, Linh Sa, Linh Sa Uyên, Phi Vân | phía nam, phía tây, nam, đông; — | pass | Hang nước lệch **tây nam**; giếng/cọc **đông** về tập — vi mô sa mạch, khớp tuyến Phi Vân sau uyên. |
| 32 | `mat-loi` | TC-001/004 | Cửu Huyền, Lan Sa, Linh Sa, Linh Sa Uyên, Phi Vân | nam, phía bắc, phía đông, đông; một dặm, ba dặm, một ngày | pass | Dẫn hướng sao + Phi Vân **đông bắc**; tránh phế ngoài — nhất quán ch.28–31. |
| 33 | `tam-ma-mam` | TC-001/004 | Cửu Huyền, Kiến Sa, Lan Sa, linh sa, Linh Sa Uyên, Phi Vân | bắc, phía đông, tây, bắc; một dặm, một ngày | pass | Men chân núi **tây bắc** tránh uyên / đường kéo — không gán LOC hub sai. |
| 34 | `ve-phe-dia` | TC-001/004 | Cửu Huyền, Kiến Sa, linh sa, Linh Sa, Linh Sa Uyên, Phi Vân… | bắc, phía đông, nam, phía đông; một đêm, một đêm | pass | Sa Điêu **đông nam** từ Kiến Sa; hốc phế **tây bắc** — layout phế, không xung đột region. |
| 35 | `tu-linh-vi-tran` | TC-001/004 | Cửu Huyền, Kiến Sa, linh sa, Linh Sa, Phi Vân, Phi Vân Tập | phía tây, phía nam, phía tây, phía đông; một đêm, một đêm | pass | Trận đĩa nội phế; «phía đông» = sáng địa mạch trong trận, không tuyến Thạch Lam. |
| 36 | `lk-that-cuu` | TC-001/004 | Cửu Huyền, Kiến Sa, Linh Sa Uyên, Phi Vân, Sa Điêu | phía tây, đông, phía đông, phía tây; một đêm, một ngày, một đêm | pass | Gió Kiến Sa; điểm dẫn trận **tây**; cảm tri **tây bắc** — cảnh khe/phế TC-001. |
| 37 | `mac-lao-mat` | TC-001/004 | Cửu Huyền, Kiến Sa, Linh Sa, Linh Sa Uyên, Phi Vân, Sa Điêu | phía nam, tây, phía đông, bắc; một ngày, một đêm | pass | Truy kích nội Kiến Sa / Cửu Huyền; hướng tương đối trong phế, không đảo LOC. |
| 38 | `nghich-thien-mi` | TC-001/004 | Cửu Huyền, Kiến Sa, Lan Sa, Linh Sa Uyên, Phi Vân, Phi Vân Tập… | phía đông, phía bắc; Một đêm, một đêm, một đêm | pass | Mép Phi Vân / Lan Sa; bóng **bắc** — không mô tả hub Thạch Lam. |
| 39 | `gia-tri-khai-thac` | TC-001/004 | Cửu Huyền, Kiến Sa, Lan Sa, linh sa, Linh Sa, Linh sa… | tây, nam, bắc, tây; Ba ngày, một đêm, ba ngày | note | Sa Điêu: khe **tây nam** tầng cột IV; **ba ngày** chuyến cửa bắc khớp pacing phế. Kết: gió đông / cát tây = địa khí (§4 ch.39). |
| 40 | `tran-rung` | TC-001/004 | Cửu Huyền, Kiến Sa, Linh Sa, Phi Vân, Phi Vân Tập, Sa Điêu | nam, đông, bắc, đông; ba ngày, ba ngày, Ba ngày | pass | Tầng cột IV · lối **tây**; cửa **bắc** Sa Điêu; điểu bay về Phi Vân — khớp TC-001/002. |
| 41 | `lop-duoi` | TC-001/004 | Cửu Huyền, Sa Điêu | phía tây, bắc, đông; — | pass | Hố sụp dưới tầng cột — hướng nội địa hình, pass. |
| 42 | `lech-khi-ngoc` | TC-001/004 | Cửu Huyền, Sa Điêu, Thạch Lam | đông; — | pass | Thạch Lam chỉ **giá tin / khế** (FS-004); không MC di chuyển hub. |
| 43 | `khe-chua-ky` | TC-001/004 | Cửu Huyền, linh sa, Linh Sa Uyên, Phi Vân, Phi Vân Tập, Thạch Lam | —; ba ngày | pass | Hầm phế → thoát; Thạch Lam trong khế vay — xa 2–3 ngày, không mô tả hướng sai. |
| 44 | `ban-tin` | TC-001/004 | Cửu Huyền, Linh Sa Uyên | phía đông; — | pass | Tin / ống phù nội phế; một «phía đông» không mâu thuẫn atlas. |
| 45 | `ep-cong` | TC-001/004 | Cửu Huyền, Kiến Sa, linh sa, thiên sa | đông; — | pass | «Thiên sa» = khí/tin Thiên Sa Công Uyên, chưa vào **LOC-THIEN-SA-COT** (tây thành). |
| 46 | `tran-tan-mot-nhip` | TC-001/004 | Cửu Huyền, Kiến Sa, Lan Sa | —; — | pass | Đấu nội phế; không mô tả địa lý region. |
| 47 | `lk-vien-man` | TC-001/004 | Bách Hóa, Cửu Huyền, Kiến Sa, Lan Sa, Linh Sa, Phi Vân Tập… | đông, phía tây, phía nam; một dặm, ba dặm | confirm | Ngã ba **nam** = chốt trạm (§4); MC hướng **ánh lam Thạch Lam** — khớp phế → thành nam/tây nam hub. |
| 48 | `thach-lam-an` | TC-001/004 | Bách Hóa, Cửu Huyền, Kiến Sa, Lan Sa, linh sa, Linh Sa… | bắc, phía đông, đông; ba ngày, ba ngày | confirm | «Ngàn dặm» hyperbole; cống **tây** Hạ Thành; Bách Hóa **đông** vs Sát Thủ quảng trường (§4 ch.48). |
| 49 | `cua-thach-lam` | TC-004/005 | Cửu Huyền, Kiến Sa, Lan Sa, Thạch Lam | —; — | pass | Hắc thị → bậc **tây** → Cửa Thăng; né **Nam Môn** la bàn — nhất quán lớp thành, không sửa geo. |
| 50 | `dan-tren-khe` | TC-004/005 | Cửu Huyền, Phi Vân, Thạch Lam | —; một đêm, một đêm, ba ngày | pass | Nội Thạch Lam / khế ty; thời hạn phòng — không tuyến liên vùng. |
| 51 | `bach-hoa-doi` | TC-004/005 | Bách Hóa, Cửu Huyền, Kiến Sa, Lan Sa, Linh Sa, Linh Sa Uyên… | đông; một đêm | pass | **LOC-BACH-HOA** trung–đông hub; cảnh trong phân điếm. |
| 52 | `monopoly-dot-pha` | TC-004/005 | Bách Hóa, Cửu Huyền, Kiến Sa, linh sa, Thạch Lam, U Ngõ… | nam; Hai ngày, hai ngày, Ba ngày | pass | Đấu giá Bách Hóa; mầm khế **ứng mạch** — hướng «nam» không gán LOC; hook U Ngõ ch.53. |
| 53 | `hac-thi-sat-thu` | TC-004/005 | Bách Hóa, Cửu Huyền, Lan Sa, Phi Vân Tập, Thiên Sa, Thạch Lam… | phía nam, bắc, bắc, phía đông; Hai ngày, Hai ngày, ba ngày | confirm | Vào **U Ngõ** qua **nam** từ phố Bách Hóa (§4); thẻ tin **đông nam** → **LOC-DAN-SA-PHU-MACH**; Thiên Sa **tây** hub (treo vé). |
| 54 | `ky-khe-mach` | TC-004/005 | Bách Hóa, Cửu Huyền, Thanh Vi, Thạch Lam, Đan Sa Phụ Mạch | đông, phía đông, phía bắc, đông; hai ngày | pass | Cửa **đông nam** rời thành → Đan Sa; khớp `direction_label` **Đông Nam** + `travel_days` 2–3. |
| 55 | `khe-thue-mach` | TC-006/008 | Bách Hóa, Cửu Huyền, Huyết Sa, Kiến Sa, Lan Sa, Linh Sa… | đông, phía đông, nam, đông; ba ngày, ba dặm, ba ngày | pass | **Cổng đông** · đường đất đỏ **đông nam**; cờ **Lạc Nhạn bắc** · Huyền Lôi **đông** — khớp `01-region-active` §2–3. |
| 56 | `dan-sa-phu` | TC-006/008 | Bách Hóa, Cửu Huyền, Lan Sa, Thanh Vi, đan sa, Đan Sa… | đông, đông, phía nam, phía bắc; — | pass | Layout mạch: lò **nam**, Thanh Vi **bắc**, Huyền Lôi **đông**; khe #3 **tây nam** về Lan Sa (FS-015) — canonical nhánh #7. |
| 57 | `luat-dai-cuc` | TC-006 | Bách Hóa, Lan Sa, Thanh Vi, Thạch Lam… | bắc; một ngày (ca) | pass | Khe số 3 · Tạ Hàm Nguyệt — **cục bộ** `LOC-DAN-SA`; Thạch Lam chỉ hậu quả kinh tế vùng. |
| 58 | `tru-co-dan` | TC-006 | Bách Hóa, Thanh Vi, Thạch Lam, Đan Sa | đông / tây (cột) | pass | Kho đan · khế Bách Hóa; «về Thạch Lam» = nợ tương lai, MC vẫn tại đồn. |
| 59 | `manh-ghep` | TC-006 | Bách Hóa, Lan Sa, Phi Vân, Thanh Vi | đông / bắc / nam (nội khe) | pass | Tranh slot; Phi Vân = tin/echo, không scene tập. |
| 60 | `tran-slot-mach` | TC-006 | Kiến Sa, Thanh Vi, Thạch Lam | bắc (Lạc Nhạn) | pass | Cờ **bắc** khớp `LOC-LAC-NHAN` · Kim Đan gián tiếp trên geo. |
| 61 | `ep-dot-pha` | TC-006 | Kiến Sa, Thanh Vi, Đan Sa | xiên **đông nam** | pass | Trinh sát **layout site**, không hướng về Thạch Lam. |
| 62 | `tru-co-so` | TC-006 | Thiên Sa, Thanh Vi | bắc / đông | pass | Trúc Cơ sơ · tin vé treo; chưa vào `LOC-THIEN-SA-COT`. |
| 63 | `ve-bi-canh` | TC-006/007 | Thiên Sa, Thạch Lam, Đan Sa | **tây nam** (hành lang) | pass | Ô 19 hậu tuyến · §4 ch.63; men **tây nam** khớp bí cảnh **tây** hub. |
| 64 | `phong-an-tin` | TC-006 | Thiên Sa, Thanh Vi | bắc; **Ba ngày** (tin) | pass | «Ba ngày» = chu kỳ tin/phong ấn tin, không `travel_days` region. |
| 65 | `monopoly-ve` | TC-006/007 | Phi Vân, Thiên Sa, Thanh Vi | nam (nội đồn) | pass | Vé Thiên Sa · §4 ch.65–66; «nam» = xe/hướng nội, không đảo LOC. |
| 66 | `hai-cuoc` | TC-006 | Thiên Sa, U Ngõ, Thạch Lam | nam / đông | pass | Echo nợ Thạch Lam · U Ngõ kinh tế; MC tại Đan Sa. |
| 67 | `sat-thu-phi` | TC-006 | Phi Vân, U Ngõ, Đan Sa | **tây nam** (thẻ ô 19) | pass | Sát Thủ thẻ · hậu phương site; U Ngõ = mối Thạch Lam, không teleport. |
| 68 | `khach-thue` | TC-006 | Linh Sa Uyên, U Ngõ, Thanh Vi | tây; ba ngày (tin) | pass | Thuê dọn mạch; uyên chỉ **tin**/khế chéo arc 1. |
| 69 | `hop-dong-can` | TC-006 | Thiên Sa, U Ngõ | **tây nam** (ô 19 · phụ mắt) | pass | Leo cọc vs hậu tuyến; phụ mắt **đông** ưu tiên nội bộ phe. |
| 70 | `giu-slot` | TC-006 | Thanh Vi | đông / tây (cọc) | pass | Giữ slot nhánh bảy — toàn cảnh đồn. |
| 71 | `vi-dai-cuc` | TC-006 | Cửu Huyền, Kiến Sa, Thanh Vi | bắc / tây | pass | Mảnh Cửu Huyền echo; không quay phế trong cảnh chính. |
| 72 | `bia-khong-ten` | TC-006 | Cửu Huyền, Kiến Sa, Thanh Vi | bắc / đông | pass | Bia Lục · đài bắc layout; không đảo region. |
| 73 | `hon-loan` | TC-006 | Lan Sa, Linh Sa Uyên, Phi Vân | nam / tây | pass | Loạn ca; Lan Sa/Linh Sa = **tin** & hàng, không march về phế. |
| 74 | `on-trung` | TC-006 | Thiên Sa, Đan Sa | xiên **đông nam** (tụ khí) | pass | Đường tụ Trung cục bộ; tránh phụ mắt — site pass. |
| 75 | `ta-ham-nguyet` | TC-006 | Sa Điêu, Thiên Sa, Đan Sa | **phụ tây** | pass | Tạ Hàm Nguyệt đài · sector «phụ tây» (quy tắc 6). |
| 76 | `phuong-tin` | TC-006 | Phi Vân, Thiên Sa | phụ tây / đài tin | pass | «Móc trên phụ tây» đúng khi MC trên sàn; chuẩn bị C-01 ch.77. |
| 77 | `mach-doan` | TC-006/008 | Cửu Huyền, Thanh Vi, Thiên Sa | phụ tây → khe **tây nam** | pass | §4 ch.77 **confirm** · C-01: «trong khe»; sơ đồ lò khớp layout. |
| 78 | `khi-sut` | TC-008 | Cửu Huyền, Thanh Vi, Thiên Sa | phụ tây; khe tây nam; đài **bắc** | pass | Khí sụt · phế mầm; Kim xa trên nhánh vá **bắc** — site, không hub. |
| 79 | `phe-dia-moi` | TC-008 | Cửu Huyền, Huyết Sa, Lan Sa, Thanh Vi | phụ tây; phế nhánh | pass | Cắt nhánh #7 · sơ đồ tre; Huyết Sa = mầm tin, chưa scene chính. |
| 80 | `nhan-qua-vung` | TC-008 | Cửu Huyền, Huyết Sa, Thanh Vi, Thạch Lam | phụ tây; phế cục bộ | pass | Nhân–Quả vùng · phế **dưới** mạch sống; Thạch Lam = giá/nợ echo. |
| 81 | `huyet-sa` | TC-008 | Cửu Huyền, Huyết Sa, Thanh Vi | phụ tây; sợi **tây nam** | pass | Tên **Huyết Sa** trên sổ; tam giác **Đoạn**; khí phế tây nam — TC-008 khớp atlas. |
| 82 | `hut-linh` | TC-008 | Cửu Huyền, Huyết Sa, Thạch Lam | phụ tây / phế | pass | Hút rìa · cấm trên mõ; không lan tam giác — cục bộ sau cắt. |
| 83 | `shortcut-ma` | TC-008 | Huyết Sa, Thạch Lam | điểm đổi **tây nam** | pass | Sa Hồng Phàm · hang tro ngoài tam giác; tre phế ≠ tre đài. |
| 84 | `cuu-vung` | TC-008 | Cửu Huyền, Huyết Sa, Thanh Vi, Thạch Lam | phụ tây; phế | pass | *Cứu vùng* treo; Beat 8 — phế chưa khai trên mõ, vẫn gắn `LOC-DAN-SA` site. |
| 85 | `linh-dich-lech` | TC-009 | Cửu Huyền, Thạch Lam, Bách Hóa, U Ngõ | phía **nam** (tam giác phế); — | pass | Còn trên phế/Ma; «phía nam» = hố sâu hơn, không nhìn — khớp nam/tây nam hub; Thạch Lam chỉ tin/ nợ. |
| 86 | `tam-ma-nhe` | TC-009 | Cửu Huyền, Thạch Lam, Thiên Sa, đan sa | phụ **tây**; một ngày | confirm | «Phụ tây» nhánh mạch phế — §4; *rút về thành* mầm, chưa vào Thạch Lam. |
| 87 | `hao-than` | TC-009 | Cửu Huyền, Thạch Lam, Thiên Sa, Bách Hóa | **cổng tây** **Đoạn**; một ngày | pass | Rút qua cổng tây phế (treo tin Thạch Lam) — song song cổng tây thành sau ch.88. |
| 88 | `can-dan-su` | TC-009 | Thạch Lam, Bách Hóa, U Ngõ | **cổng tây** thành; một đêm | pass | Vào Thạch Lam **cổng tây** — khớp `LOC-THIEN-SA` / U Ngõ tây; không đảo hub. |
| 89 | `cua-dan-hoi` | TC-009 | Bách Hóa, Thiên Sa, Đan Hội, Thạch Lam | tây (cột); đông (hội) | confirm | Bách Hóa sáng → bỏ cột tây → ngõ **Luyện Đan Hội** đông — §4 ch.89. |
| 90 | `le-phi-cong-hien` | TC-009 | Thạch Lam Luyện Đan Hội, Thiên Sa, Bách Hóa | —; — | pass | Trong thành; cột Thiên Sa treo cọc — không di chuyển region. |
| 91 | `diem-dan-hoi` | TC-009 | Đan Hội, Bách Hóa, Thiên Sa | đông (phố); hai–ba ngày (canh) | pass | «Đi ngang Bách Hóa» = tránh đông đấu giá — hub đông nhất quán. |
| 92 | `gian-lan-diem` | TC-009 | Đan Hội, Cửu Huyền, Bách Hóa | —; ba ngày | pass | Sân hội Thạch Lam; Cửu Huyền chỉ mảnh trong ngực. |
| 93 | `lo-luyen` | TC-009 | Đan Hội, Bách Hóa | vách **bắc** (treo tin) | pass | Vách bắc sân = layout nội, không hướng châu. |
| 94 | `phuong-so` | TC-009 | Đan Hội, U Ngõ, Bách Hóa | bắc (vách); đông (Bách Hóa) | pass | Tin **U Ngõ** trên vách hội — tây thành; MC không sang U Ngõ. |
| 95 | `lau-phuong-tin` | TC-009 | Đan Hội, U Ngõ, Bách Hóa | bắc; đông | pass | Quán rìa bắc trong thành; tre U Ngõ vs giấy hội. |
| 96 | `dinh-linh-chan` | TC-009/010 | Bách Hóa, Đan Hội, Thiên Sa | **bàn tây**; bắc (vách hội) | confirm | Bàn tây = nội Bách Hóa — §4 ch.96. |
| 97 | `truc-co-hau` | TC-009/010 | Đan Hội, Cửu Huyền, Bách Hóa | bắc (tre); **Hậu** (cửa hội) | pass | Mảnh Cửu Huyền phản xa phế — không mở bản đồ phế mới. |
| 98 | `mot-tang-on` | TC-009/010 | Đan Hội, Bách Hóa, Thiên Sa | bắc; nam (vách lò phụ) | pass | «Ổn một tầng» phương — nội thành. |
| 99 | `noi-bo-hoi` | TC-009 | Đan Hội, Bách Hóa, Thiên Sa | **phía tây** (bảng phương); bắc (khói) | confirm | Góc sân hội — §4 ch.99; chiều tránh Bách Hóa đông. |
| 100 | `thue-nop` | TC-009/010 | Bách Hóa, Kiến Sa, Thạch Lam | đông (phân điếm); **ba ngày** ca | confirm | Ca Kiến Sa rìa — §4; Phương Ngự Hàn **không** vào thành. |
| 101 | `dan-su-xam` | TC-009/010 | Kiến Sa, Thạch Lam, Đan Hội | **ba ngày**; cổng tây hội | pass | Khởi ca tập Kiến Sa — xuất từ Thạch Lam. |
| 102 | `phe-dia-ve` | TC-009/010 | Kiến Sa, Cửu Huyền, Thạch Lam | **ba ngày** ca; Sát «trên thành» | pass | Rìa Kiến Sa + Trầm Hội Sa; phế nhớ/mảnh. |
| 103 | `re-rung` | TC-009/010 | Kiến Sa, Thạch Lam, Cửu Huyền | về **cổng tây**; gió Thạch Lam | pass | Hồi thành sau rung phế; tro route khớp 2–3 ngày hub↔phế. |
| 104 | `manh-sang` | TC-009/010 | Thạch Lam, Bách Hóa, Cửu Huyền | trong phường | pass | Manh phế trên khay leo — echo Kiến Sa, không GEO mới. |
| 105 | `sa-hoi` | TC-009/010 | Thạch Lam, **cổng tây**, U Ngõ (tin) | tây (cột / Ma ngoài) | pass | Sa Hồng Phàm ngoài cột — «tây» = miệng nhanh, MC từ chối. |
| 106 | `duong-tat-hoi` | TC-009/010 | Đan Hội, Bách Hóa, Thiên Sa, U Ngõ | **tây** (đối chiếu); ba ngày ca | confirm | Tin *nhanh — tây* vs chậm tro — §4; không vào U Ngõ. |
| 107 | `vien-man-huong` | TC-009/010 | Thạch Lam, Bách Hóa, Thiên Sa, Cửu Huyền | tây (giấy rách); **hướng** ĐVM (tu) | pass | Tiêu đề = hướng tu luyện; geo: góc Bách Hóa, cột xa tây. |
| 108 | `tam-ma-day` | TC-009/010 | Đan Hội, Bách Hóa, Thiên Sa | tây (cổng/cột); **bốn ngày** tro | pass | «Bốn ngày» = canh lò trong thành, không đè 2–3 ngày sa biên. |
| 109 | `linh-dich-che` | TC-009/010 | Đan Hội, Thiên Sa, Bách Hóa | tây (ngõ/cổng) | pass | Liều che — nội phường; Thiên Sa treo ngoài sổ. |
| 110 | `nhan-qua-tich` | TC-009/010 | Thạch Lam, Thiên Sa, Cửu Huyền, U Ngõ | **nam** (vách lò phụ); tây (cột) | pass | Đi bộ trong thành; cột Thiên Sa Canh Tuất — khớp LOC. |
| 111 | `thien-sa-dem` | TC-010 | Thiên Sa, Đan Hội, Thạch Lam | **cổng tây**; gió **tây** | confirm | Mở cửa vé — MC không vào — §4 ch.111. |
| 112 | `den-sap-tat` | TC-010 | Thiên Sa, Bách Hóa, Đan Hội, Cửu Huyền | **cổng tây** / cột | pass | Khép Phase 1 trong thành; Cửu Huyền mảnh im — không leo phế. |

## 6. Batch prose-writer (queue)

| Task | Phạm vi | Trạng thái | Output |
| --- | --- | --- | --- |
| `T-geo-audit-batch-1` | ch.1–28 | **done** | §4: ch.4 (note), ch.14 (confirm); §5: ghi chú writer ch.1–28; không lệch critical trong batch |
| `T-geo-audit-batch-2` | ch.29–56 | **done** | §4: ch.39 (note), ch.47–48–53 (confirm); §5: ghi chú writer ch.29–56; không lệch critical mới |
| `T-geo-audit-batch-3` | ch.57–84 | **done** | §1 quy tắc 6 «phụ tây»; §4: ch.77·63·65–66 **confirm**; §5: ghi chú writer ch.57–84; không lệch critical mới |
| `T-geo-audit-batch-4` | ch.85–112 | **done** | §4: confirm ch.86, 89, 96, 99, 100–103, 106–107, 111–112; §5: ghi chú writer; **không** critical mới |

## 7. Tham chiếu file bản đồ

- [`geo/00-tinh-ha.geojson`](geo/00-tinh-ha.geojson)
- [`geo/chau-luc/chl-ha-gioi-nam.geojson`](geo/chau-luc/chl-ha-gioi-nam.geojson)
- [`geo/region/reg-thach-lam.geojson`](geo/region/reg-thach-lam.geojson) · [`geo/region/reg-lan-sa-chau.geojson`](geo/region/reg-lan-sa-chau.geojson)
- [`geo/micro/arc-01-phi-van-tap.geojson`](geo/micro/arc-01-phi-van-tap.geojson)
- [`geo/micro/arc-01-linh-sa-uyen.geojson`](geo/micro/arc-01-linh-sa-uyen.geojson)

---

## 8. Tóm tắt điều hành (campaign `T-geo-prose-audit`)

**Canonical:** GeoJSON 4 tầng + atlas/region/tiểu cục (§7) — audit **read-only**; lệch → revise **prose**, không sửa `.geojson`.

### 8.1. Toàn phạm vi ch.1–112 (§5 · cột TT)

| TT | Số chương | Ghi chú |
| --- | ---: | --- |
| **pass** | **98** | Không lệch hub region sau batch-1–4 + quét v1 |
| **confirm** | **11** | ch.14, 47, 48, 53, 86, 89, 96, 99, 100, 106, 111 (+ mục §4 gom) |
| **note** | **2** | ch.4, ch.39 |
| **confirm** (§4) | **+1** | ch.77 — §1 quy tắc 6 · C-01 r1 đã sửa; **pass** site Đan Sa (batch-3) |

### 8.2. Batch-4 (ch.85–112) — hội đan · Kiến Sa rìa · Thiên Sa

| | |
| --- | --- |
| Chương | **28** |
| **pass** | **21** |
| **confirm** | **7** (86, 89, 96, 99, 100, 106, 111) |
| **note / flag / critical mới** | **0** |

**Mạch địa:** phế dư (85–87) → **cổng tây** Thạch Lam (88) → **Bách Hóa đông** + **Luyện Đan Hội** (89–99) → ca **Kiến Sa rìa** 3 ngày (100–103) → tro / *đối chiếu* (104–109) → **cột Thiên Sa tây**, MC không vào bí cảnh (110–112). Cửu Huyền = mảnh/phế nhớ/leo nguyên liệu — không payoff phong ấn.

### 8.3. Revise prose — ưu tiên

| Ưu tiên | Ch | Hành động |
| --- | ---: | --- |
| **P0** | 77 | Revise «phụ tây» (C-01) **hoặc** hạ **flag** theo §1 quy tắc 6 |
| **P2** | 4 | Tách ngõ tây Phi Vân vs hướng Kiến Sa |
| **P3** | 39, 14 | Tùy chọn |
| — | 85–112 | **Không** revise bắt buộc |

### 8.4. Queue campaign

| Task | Trạng thái |
| --- | --- |
| batch-1 · batch-2 · batch-3 · **batch-4** | **done** |
| Đóng campaign prose ↔ geo (arc 1–112) | **done** — revise tùy chọn P2 ch.4 |