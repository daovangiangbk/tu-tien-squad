# Master Brief — Khổ Hải Tiên Lộ — v2.1 — 2026-10-23

> Khung làm việc cho hệ subagent. Cập nhật version + mục **Changelog** khi đổi phạm vi; `project-orchestrator` đánh dấu artifact stale.

## 0. Work identity

| Trường | Giá trị |
| --- | --- |
| `work_slug` | `kho-hai-tien-lo` |
| `work_title_provisional` | **Khổ Hải Tiên Lộ** *(tên hiển thị tạm; `xianxia-naming-specialist` chuẩn hóa nếu user đổi)* |
| `work_root` | `projects/kho-hai-tien-lo/` |
| `foundation_root` | `foundation/` *(shared repo root — dùng chung Core & World Linh Giới)* |
| `logic_root` | `projects/kho-hai-tien-lo/logic/` |
| `interface_root` | `projects/kho-hai-tien-lo/interface/` |
| `pipeline` | **A** — sáng tác tiểu thuyết tiên hiệp dài kỳ (epic multi-arc) |

## 1. Raw intent (user)

> Khởi tạo dự án mới  
> Phàm nhân bị đẩy vào bi kịch tột cùng, nhặt được bảo vật của trời đất, bước vào con đường tu luyện  
> Vì sống lớn lên trong nghèo khó, cực khổ nên là 1 người có nghị lực, tâm tính, ngộ tính tốt  
> Mặc dù tư chất kém (ngũ linh căn tạp phẩm), nhưng nhờ bảo vật, sống sót ở tầng đáy của tông môn - tạp dịch khu mỏ - dần tăng cường thực lực và có chỗ đứng trong tông môn  
>  
> Câu hỏi triết lý:  
> Cuộc sống này tại sao lại có người sướng lại có người khổ  
> Tu tiên có phải là con đường thoát khổ, tại sao được tu tiên lại khổ hơn cuộc sống phàm nhân

## 2. Tóm tắt điều hành (5–10 dòng)

**Khổ Hải Tiên Lộ** (`kho-hai-tien-lo`) là tiểu thuyết tiên hiệp dài kỳ (epic multi-arc), phong cách **cổ phong trầm mặc, triết lý xám** (tham chiếu tinh thần *Tru Tiên* và dòng phàm nhân tu tiên khắc nghiệt). Nhân vật chính xuất thân phàm nhân nghèo khổ tận đáy, trải qua **bi kịch tột cùng** mất sạch chỗ dựa phàm trần và tình cờ thu được **bảo vật của trời đất** (dị bảo nghịch thiên ẩn tàng). Mang **ngũ linh căn tạp phẩm** — tư chất bét bảng bị giới tu chân khinh rẻ — hắn bước vào tầng đáy của một tông môn tại **Linh Giới** với thân phận **đệ tử tạp dịch khu mỏ linh thạch**. Nhờ **nghị lực sắt đá, tâm tính trầm ổn và ngộ tính cao** được trui rèn từ tháng ngày cơ cực, kết hợp cùng cơ chế hỗ trợ có trả giá của chí bảo, hắn từng bước sống sót qua sự bóc lột tàn khốc nơi hầm mỏ, tích lũy thực lực và giành lấy chỗ đứng trong tông môn. Xuyên suốt hành trình là hai câu hỏi triết lý cắt cứa tâm can: **Vì sao kiếp người kẻ sướng người khổ?** Và **nếu tu tiên là để thoát khổ, cớ sao bước vào tiên lộ rồi lại còn khổ sở, nghiệt ngã gấp vạn lần phàm nhân?** Tác phẩm dùng chung `foundation/` (bối cảnh **Càn Nguyên Tinh — Linh Giới**), miễn trừ rebuild bản đồ vĩ mô ở A1 (`waive_T-world-project: true`), tập trung xây dựng chiều sâu nhân vật, kinh tế tầng đáy tông môn và lộ trình leo tháp quyền lực có cái giá Nhân-Quả rõ ràng.

## 3. Mục tiêu & thành công

- **Trải nghiệm cốt lõi & Triết lý:** Khắc họa sống động nghịch lý của **Nghịch Thiên Nhi Hành**: phàm nhân tưởng bước qua cổng tiên môn là thoát cảnh sinh lão bệnh tử và đói nghèo, nhưng thực chất chỉ chuyển từ "cái khổ trăm năm của kiếp phàm" sang "cái khổ vạn năm của kẻ làm cỏ rác dưới luật Cường giả vi tôn". Câu trả lời không nằm ở bài giảng đạo đức mà ở **lựa chọn hành vi của MC** khi từ kẻ bị chà đạp ở khu mỏ dần nắm quyền sinh sát trong tông môn.
- **Nhân vật chính (MC):** Thuyết phục độc giả rằng một kẻ **ngũ linh căn tạp phẩm** có thể đi lên không phải nhờ may mắn vô điều kiện, mà nhờ **Tâm–Trí – Nghị lực – Ngộ tính** (rèn từ khổ nạn phàm trần) cộng hưởng với **chí bảo thiên địa** (có giới hạn, hao phí và nguy cơ "hoài bích kỳ tội").
- **Tích hợp 3 lớp (Foundation → Logic → Interface):**
  - Tuân thủ tuyệt đối hệ thống cảnh giới, điểm nghẽn linh căn, kinh tế linh thạch/đan dược và luật cư trú chung phàm–tu trên **Linh Giới** (`foundation/core/02-world-laws-lore-core.md` Luật 6b & `03-power-system-economy-core.md` §1.2, §2.2, §3.1b).
  - Tuyệt đối không dùng tiếng Anh trong prose chương; văn phong cổ phong, giàu hình ảnh thực cảm (bụi quặng, hàn khí, mùi máu, ánh đèn linh thạch).

## 4. Phạm vi & quy mô

| Hạng mục | Giá trị |
| --- | --- |
| **Định dạng (Format)** | Tiểu thuyết tiên hiệp dài kỳ (**Epic multi-arc**), chia theo Phase / Quyển (Arc) |
| **Quy mô tổng thể (ước tính)** | **4–5 Đại cục (Arcs)** cho phần **Linh Giới** (từ Phàm nhân / Luyện Khí tầng đáy → Trúc Cơ → Kim Đan → Nguyên Anh / Hóa Thần → Độ Kiếp); **Arc 1 (Tạp Dịch Khu Mỏ) ngắn gọn ~15–20 chương** (~3.000–3.500 chữ/chương), nhịp cô đọng |
| **Góc nhìn (POV)** | Ngôi thứ ba giới hạn (**Third-person limited**), bám sát góc nhìn, cảm quan và nội tâm của MC |
| **Cõi giới mở đầu & chủ đạo** | **Linh Giới** — Tinh cầu **Càn Nguyên Tinh** (`TH-LINH-CAN-NGUYEN`), nơi phàm nhân là đa số và tông môn chân tu nắm giữ linh mạch, mỏ linh thạch (theo Luật 6b) |
| **Cảnh giới khởi điểm → mục tiêu Phase 1** | **Phàm nhân** (bi kịch gốc + nhặt bảo vật) → **Luyện Khí tầng 1–3** (tạp dịch khu mỏ) → **Luyện Khí trung/hậu kỳ** (vượt nghẽn ngũ linh căn, thoát ngạch phu mỏ, vào ngoại môn/nội môn) → chạm ngưỡng **Trúc Cơ** |
| **Out of scope (ngoài phạm vi)** | <ul><li>**Độc lập hoàn toàn** với tác phẩm truyện ngắn đã đóng gói tại `projects/archive/ham-mo/` — không dùng lại cốt truyện 4 chương, nhân vật vô danh hay micro-setting cũ của `ham-mo`.</li><li>Không đặt bối cảnh mở đầu ở **Phàm Giới** (vì Luật 6a quy định Phàm Giới là Mạt pháp, không có tông môn chân tu và khu mỏ linh thạch hoạt động lâu dài).</li><li>Không rebuild lại toàn bộ GeoJSON tinh cầu/châu lục ở bước A1 (`waive_T-world-project: true`); chỉ thiết kế địa lý vi mô (tông môn & khu mỏ) ở Phase A2.</li><li>Không viết sẵn chi tiết Tiên Giới / Thần Giới ở giai đoạn này.</li></ul> |

### 4b. Chiến lược thế giới (bắt buộc chốt)

| Trường | Giá trị |
| --- | --- |
| `world_strategy` | `foundation-fixed` *(kèm mở rộng micro-setting khu mỏ & tông môn tại Phase A2)* |
| `foundation_world_paths` | <ul><li>`foundation/core/02-world-laws-lore-core.md` (Luật 1–10, đặc biệt Luật 6b, Luật 9)</li><li>`foundation/logic/world/realms/linh-gioi/00-world-atlas.md`</li><li>`foundation/logic/world/realms/linh-gioi/planets/can-nguyen-tinh/00-world-atlas.md`</li><li>`foundation/logic/world/realms/linh-gioi/01-region-catalog.md`</li><li>`foundation/logic/03-demographics-pham-linh.md`</li></ul> |
| `story_region_start` | Đại lục **Trung Linh** (`CHL-TRUNG-LINH`) — vùng biên viễn giàu mỏ khoáng mạch như **Tây Mạch** (`REG-TL-TAY-MACH`, giáp Hỏa Diễm) *hoặc* Đại lục **Hỏa Diễm** (`CHL-HOA-DIEN`, vùng mỏ `REG-HD-VIEM-QUAN` / `REG-HD-DONG-MACH`) `[giả định: ưu tiên REG-TL-TAY-MACH thuộc CHL-TRUNG-LINH]` |
| `waive_T-world-project` | `true` *(orchestrator bỏ qua bước rebuild bản đồ vĩ mô A1; chỉ giao `world-builder` tạo micro-setting tông môn & khu mỏ ở A2)* |
| *(tùy chọn)* | `projects/kho-hai-tien-lo/logic/world/00-foundation-handoff.md` — mirror link ngắn nối vùng `REG-*` của Càn Nguyên Tinh với địa bàn tông môn |

## 5. Ràng buộc sáng tác

### 5.1. Trục triết lý & Bi kịch (bám sát `foundation/core/01-theme-tragedy-core.md`)
1. **Câu hỏi 1 — *"Cuộc sống này tại sao lại có người sướng, lại có người khổ?"*:**
   - Phản ánh trực diện **Luật 9 (Căn cơ cá nhân không công bằng)** và **Luật 3 (Cường giả vi tôn)**. Ở thế gian này, Thiên Đạo vận hành vô tình ("Thiên địa bất nhân, dĩ vạn vật vi sô cẩu"): có kẻ sinh ra đã mang Thiên Linh Căn hoặc huyết mạch thế gia, ngồi trên linh mạch hưởng đan dược; có kẻ sinh ra làm phàm nhân cày thuê cuốc mướn hoặc mang **ngũ linh căn tạp phẩm** bị coi như phế vật.
   - Sự bất công không chỉ đến từ tự nhiên mà còn bị **cấu trúc hóa bởi tông môn**: kẻ ở thượng tầng nhân danh "thuận thiên, giữ đạo thống" để định đoạt định mức sống chết của kẻ dưới đáy.
2. **Câu hỏi 2 — *"Tu tiên có phải là con đường thoát khổ? Tại sao được tu tiên lại khổ hơn cuộc sống phàm nhân?"*:**
   - Khi còn là phàm nhân, cái khổ là đói rét, tật bệnh, cường hào ác bá và sinh mệnh ngắn ngủi 60–80 năm — nhưng nỗi khổ ấy **hữu hạn**, còn có hơi ấm gia đình, còn có chỗ cho sự chất phác dung thân.
   - Khi bước vào **khu mỏ tạp dịch của tông môn**, MC nhận ra sự thật trần trụi: **nhập đạo không phải là bước lên mây xanh, mà là bước vào một cối xay thịt tinh vi hơn**.
     - **Thân phận & Tự do:** Phàm nhân nghèo còn có thể bỏ làng đi nơi khác; tạp dịch khu mỏ chịu ràng buộc bởi khế ước tông môn, cấm chế, định mức linh thạch hàng tháng — không đủ định mức thì bị phạt cúp đan, giam hầm tối, hoặc phế tu vi.
     - **Cạnh tranh sinh tồn:** Mọi tia linh khí, mỗi viên linh thạch vụn, mỗi cuốn công pháp khuyết đều phải đổi bằng mồ hôi, máu và sự cảnh giác tuyệt đối với chính đồng môn.
     - **Thời gian & Tâm ma:** Tuổi thọ kéo dài hơn phàm nhân nhưng nếu kẹt ở tầng đáy thì chỉ là **kéo dài kiếp nô dịch và nỗi sợ hãi** (sợ cạn thọ nguyên, sợ bị đoạt bảo, sợ bản thân cũng dần biến thành kẻ tàn nhẫn mà mình từng căm ghét).

### 5.2. Thiết kế Nhân vật chính (MC) & Core Wound
- **Xuất thân & Phẩm chất:** Lớn lên trong cảnh nghèo khó cùng cực nơi thôn trang/thị trấn phàm nhân trên Linh Giới, từ nhỏ đã quen nhịn đói, chịu lạnh, nhìn sắc mặt người đời và tự tìm đường sống. Nhờ đó hình thành 3 trụ cột bù đắp căn cơ:
  1. **Nghị lực (Ý chí):** Chịu được nỗi đau thể xác và sự cô độc kéo dài mà tu sĩ xuất thân ấm êm dễ sụp đổ.
  2. **Tâm tính:** Trầm ổn, nhẫn nhịn, không vì một chút sỉ nhục mà bốc đồng mất mạng, nhưng dưới lớp tro lạnh là ngọn lửa bất khuất không chịu nhận mệnh.
  3. **Ngộ tính:** Vì không có sư phụ tận tình chỉ điểm và công pháp thượng thừa, MC quen quan sát quy luật tự nhiên (vân đá, mạch quặng, hơi thở, nhịp búa) để tự suy diễn, đốn ngộ nguyên lý vận khí và pháp thuật cơ bản.
- **Bi kịch gốc (Inciting Tragedy):** Gia đình / người thân duy nhất hoặc cả xóm làng phàm nhân bị hủy diệt hoặc hy sinh oan uổng (do tai vạ từ giao tranh của tu sĩ, hoặc bị trưng thu/hiến tế làm khổ dịch mở mạch cho thế lực tu chân mà không ai thèm nhớ tên — khớp hình mẫu `01` §3.1 & §3.5). Trong tuyệt cảnh thập tử nhất sinh, MC chạm vào **bảo vật của trời đất** và bước chân vào con đường tu luyện.
- **Tư chất:** **Ngũ linh căn tạp phẩm** (Kim – Mộc – Thủy – Hỏa – Thổ đều có nhưng駁 tạp, kinh mạch hẹp, tốc độ dẫn khí và luyện hóa thông thường chỉ bằng 1/5 đến 1/10 tu sĩ đơn/song linh căn; mỗi tiểu cảnh giới đều là một vách đá).

### 5.3. Bảo vật của trời đất (Chí bảo nghịch thiên ẩn tàng)
- **Nguyên tắc Core (`03` §2.2 & `11-thien-phu-ky-nang-an.md` §0):**
  - Bảo vật là **chìa khóa giải bài toán Ngũ linh căn tạp phẩm** ở tầng đáy (ví dụ: cổ vật mang thuộc tính **Hỗn Nguyên / Ngũ Hành tạo hóa** hoặc **Ngưng lộ / Tinh lọc phế khoáng — phế đan**, biến tạp khí Ngũ hành nơi hầm mỏ thành linh dịch tinh thuần hoặc mở không gian thời gian/ngộ đạo vi mô).
  - **Cấm miễn phí (No free lunch):** Bảo vật phải có **điều kiện kích hoạt và cái giá** rõ ràng (cần hấp thu tinh hoa quặng hiếm/linh thạch, tiêu hao tinh huyết/thần thức, hoặc mỗi lần nghịch cải căn cơ đều tích tụ **Nhân-Quả / Thiên oán** khiến Thiên kiếp về sau khốc liệt gấp bội).
  - **Áp lực ẩn tàng:** Hình dáng bề ngoài phàm tục (hòn đá xám, mảnh ngọc mẻ, cổ bội hoặc ấn cổ hòa vào máu thịt) không lộ linh quang trước thần thức tu sĩ bậc thấp–trung, nhưng nếu để lộ dấu vết tài nguyên bất thường sẽ lập tức dẫn họa sát thân (*"Thất phu vô tội, hoài bích kỳ tội"*).

### 5.4. Kinh tế & Sinh thái Tạp dịch Khu mỏ
- Tạp dịch khu mỏ là tầng đáy của tông môn (dưới cả đệ tử ngoại môn): gồm những kẻ **tạp linh căn** hoặc phàm nhân có chút cảm ứng khí bị đẩy xuống đào quặng linh thạch.
- Mỗi tháng phải nộp **định mức linh thạch nguyên khoáng**; phần dư cực ít ỏi mới đổi được **điểm cống hiến / linh thạch vụn / Tụ Khí Đan hạ phẩm (hoặc đan phế)**.
- Phân tầng bóc lột rõ rệt: **Đốc công / Quản sự khu mỏ** (Luyện Khí hậu kỳ – Trúc Cơ) → **Đầu mục lán trại** (Luyện Khí tầng 4–6) → **Tạp dịch đào mỏ** (Luyện Khí tầng 1–3) → **Phu mỏ phàm nhân** (vô căn, chỉ đổi bạc/lương thực, chết trong hầm không ai chôn). Sự hiện diện của cả phu mỏ phàm nhân lẫn tạp dịch tu sĩ ngay trong một hầm mỏ sẽ là tấm gương phản chiếu trực tiếp hai câu hỏi triết lý của truyện.

## 6. Yêu cầu theo lớp

### Foundation (paths dưới `foundation_root: foundation/`)
- Đọc và tuân thủ `foundation/core/00-glossary.md`, `01-theme-tragedy-core.md`, `02-world-laws-lore-core.md`, `03-power-system-economy-core.md`.
- Tham chiếu `foundation/resources/01-linh-thach-tien-te.md`, `04-dan-duoc.md`, `11-thien-phu-ky-nang-an.md` để chuẩn hóa kinh tế khu mỏ, đan dược Luyện Khí – Trúc Cơ và cơ chế bảo vật.
- **Không tự ý sửa Core.** Nếu về sau phát sinh định chế tông môn hoặc loại khoáng thạch/chí bảo mới muốn đưa vào kho chung, tạo đề xuất tại `projects/kho-hai-tien-lo/core-proposals/CP-*.md` chờ human duyệt.

### Logic (paths dưới `logic_root: projects/kho-hai-tien-lo/logic/`)
- `logic/world/00-foundation-handoff.md` *(tùy chọn)* & `logic/world/01-region-active.md` / `02-tieu-cuc-index.md` (ở Phase A2 `T-world-arc-1`): Neo vị trí tông môn vào một `REG-*` trên **Càn Nguyên Tinh**; thiết kế cấu trúc tông môn (Tạp dịch khu mỏ → Ngoại môn → Nội môn → Chân truyền), quy chế định mức linh thạch, các tầng hầm mỏ và hiểm địa dưới lòng đất (`world-builder`).
- `logic/characters/00-characters-index.md` & `logic/characters/01-project-roster.md` (Phase A1 `T-characters-project`) + `logic/characters/arc-1-roster.md` (Phase A2 `T-characters-arc-1`): Hồ sơ Dual-View (Phần I Chân dung sống + Phần II Spec) cho MC (bi kịch gốc, 3 phẩm chất nghị lực/tâm tính/ngộ tính, ngũ linh căn tạp phẩm, cơ chế + cái giá của **Bảo vật trời đất**) và dàn nhân vật dài hạn / khu mỏ (`character-architect`).
- `logic/00-story-spine.md` & `logic/arcs/00-arc-master-outline.md` (Phase A1 `T-plot-project`), `logic/arcs/01-arc1-beats.md` (Phase A2 `T-plot-arc-1`), `logic/chapters/00-chapter-spine-arc-1-kho-hai-tien-lo.md` (Phase A2 `T-spine-arc-1`): Blueprint 3 tầng (Macro → Arc → Chapter) Dual-View (`plot-architect`).
- `logic/foreshadowing/00-foreshadow-ledger.md` (Phase A1 `T-foreshadow-project`): Sổ cái phục bút cho nguồn gốc Bảo vật trời đất, kẻ gây ra bi kịch phàm trần của MC, bí mật dưới đáy mỏ linh thạch và các móc xích triết lý (`foreshadowing-architect`).
- `logic/audits/audit-plot-project.md` (Phase A1 `T-audit-plot-project`): Kiểm định kiến trúc cốt truyện toàn dự án trước khi mở A2 (`pro-auditor`).

### Interface (paths dưới `interface_root: projects/kho-hai-tien-lo/interface/`)
- Naming canon: `xianxia-naming-specialist` → `projects/kho-hai-tien-lo/interface/naming/registry.md` (tên chính thức tác phẩm, tên MC, tên Bảo vật, tên Tông môn, Khu mỏ, công pháp, nhân vật phụ — chạy khi có `naming pending`).
- Mục lục chương: `projects/kho-hai-tien-lo/interface/chapters/00-index.md`.
- Prose: `xianxia-prose-writer` → `projects/kho-hai-tien-lo/interface/chapters/chapter-NN-*.md`.
- Review (read-only, sau mỗi chương): `xianxia-chapter-reviewer` → `projects/kho-hai-tien-lo/interface/chapter-view/review-chapter-NN-*.md`.
- Revise prose: **sau human confirm** → `xianxia-prose-writer` (do `project-orchestrator` điều phối).
- Đọc thử cuối arc: `experimental-reader` → `projects/kho-hai-tien-lo/interface/chapter-view/reader-comment/reader-arc-N-kho-hai-tien-lo.md`.

## 7. Deliverables & đường dẫn

| Artifact | Path | Owner agent |
| --- | --- | --- |
| Master Brief | `projects/kho-hai-tien-lo/00-master-brief.md` | `requirements-briefer` |
| Bản đồ tiến độ | `projects/kho-hai-tien-lo/00-progress-map.md` | `project-orchestrator` |
| Trạng thái & Queue | `projects/kho-hai-tien-lo/status.md` | `project-orchestrator` |
| Character Web (Project) | `projects/kho-hai-tien-lo/logic/characters/00-characters-index.md`, `01-project-roster.md` | `character-architect` |
| Story Spine & Master Outline | `projects/kho-hai-tien-lo/logic/00-story-spine.md`, `logic/arcs/00-arc-master-outline.md` | `plot-architect` |
| Sổ cái Phục bút (Foreshadow) | `projects/kho-hai-tien-lo/logic/foreshadowing/00-foreshadow-ledger.md` | `foreshadowing-architect` |
| Audit Plot (Project) | `projects/kho-hai-tien-lo/logic/audits/audit-plot-project.md` | `pro-auditor` |
| Bối cảnh Micro Arc 1 | `projects/kho-hai-tien-lo/logic/world/01-region-active.md`, `02-tieu-cuc-index.md` | `world-builder` |
| Beats & Chapter Spine (Arc 1) | `projects/kho-hai-tien-lo/logic/arcs/01-arc1-beats.md`, `logic/chapters/00-chapter-spine-arc-1-kho-hai-tien-lo.md` | `plot-architect` |
| Bảng tên chuẩn (Naming Registry) | `projects/kho-hai-tien-lo/interface/naming/registry.md` | `xianxia-naming-specialist` |
| Bản thảo chương (Prose) | `projects/kho-hai-tien-lo/interface/chapters/chapter-NN-*.md` | `xianxia-prose-writer` |
| Báo cáo đọc duyệt (Review) | `projects/kho-hai-tien-lo/interface/chapter-view/review-chapter-NN-*.md` | `xianxia-chapter-reviewer` |

### Task queue sơ bộ (Handoff cho `project-orchestrator` — chuẩn Pipeline A1 → A2 → A3)

| Task ID | Agent | Input paths | Output paths | DoD (Tiêu chí hoàn thành) | Deps |
| --- | --- | --- | --- | --- | --- |
| `T-brief` | `requirements-briefer` | Raw intent + `foundation/core/*` | `projects/kho-hai-tien-lo/00-master-brief.md` | Đầy đủ §0–§10, chốt §4b `world_strategy: foundation-fixed`, câu hỏi mở & giả định | — |
| `T-world-project` | `world-builder` | `00-master-brief.md` §4b | *(waived — dùng thẳng `foundation/` Linh Giới `TH-LINH-CAN-NGUYEN`)* | Skip theo §2.0 orchestrator (`world_strategy: foundation-fixed`) | `T-brief` |
| `T-characters-project` | `character-architect` | `00-master-brief.md`, `01-theme-tragedy-core.md`, `11-thien-phu-ky-nang-an.md` | `logic/characters/00-characters-index.md`, `logic/characters/01-project-roster.md` | Mode `project` Dual-View: MC (bi kịch gốc, 3 phẩm chất, ngũ linh căn tạp phẩm, cơ chế + cái giá Bảo vật trời đất) + 4–8 cast dài hạn; gắn `naming pending` | `T-brief` |
| `T-naming-people-project` | `xianxia-naming-specialist` | `01-project-roster.md` (`naming pending`), `00-glossary.md` | `interface/naming/registry.md` | Đặt tên Hán Việt cổ kính cho MC, Bảo vật, Tông môn và cast dài hạn | `T-characters-project` |
| `T-plot-project` | `plot-architect` | `00-master-brief.md`, `01-project-roster.md`, world atlas | `logic/00-story-spine.md`, `logic/arcs/00-arc-master-outline.md` | Mode `Design Tier 1` Dual-View: đại cục 4–5 Arcs gắn tiến hóa 2 câu hỏi triết lý | `T-characters-project` |
| `T-foreshadow-project` | `foreshadowing-architect` | `00-arc-master-outline.md`, `01-project-roster.md`, `foundation/core/01–03` | `logic/foreshadowing/00-foreshadow-ledger.md` | Gài mầm nguồn gốc Bảo vật, chân tướng bi kịch gốc MC, bí ẩn đáy mỏ & đối trọng Chính–Tà | `T-plot-project` |
| `T-audit-plot-project` | `pro-auditor` | `00-story-spine.md`, `00-arc-master-outline.md`, `01-project-roster.md`, `00-foreshadow-ledger.md` | `logic/audits/audit-plot-project.md` | Mode `plot-architecture`: verdict `plot-ready` trước khi mở Phase A2 (Arc 1) | `T-foreshadow-project` |

### Risk register (Quản trị rủi ro sáng tác)

| # | Rủi ro | Mức độ | Biện pháp phòng ngừa / Kiểm soát |
| --- | --- | --- | --- |
| 1 | **Bảo vật quá bá đạo (OP) làm mất chất "khổ hải" và vô hiệu hóa nhược điểm Ngũ linh căn tạp phẩm** | Cao | Khóa chặt cơ chế đánh đổi trong `T-char-mc`: bảo vật đòi hỏi nguyên liệu/khoáng chất hoặc hao tổn tâm lực để vận hành; MC vẫn phải dùng **nghị lực, ngộ tính và mưu trí** để kiếm nguyên liệu nuôi bảo vật và tự lĩnh ngộ pháp quyết. |
| 2 | **Triết lý "vì sao người sướng kẻ khổ / tu tiên khổ hơn phàm nhân" bị viết thành văn nghị luận khô khan** | Trung bình – Cao | Cấm giảng đạo lý trực tiếp. Bắt buộc thể hiện qua **tình huống tương phản cụ thể**: bữa cơm của phàm nhân vs viên đan mốc của tạp dịch; một câu nói nhẹ tênh của đệ tử nội môn quyết định mạng sống hàng chục phu mỏ. |
| 3 | **Nhầm lẫn hoặc trùng lặp cảm giác với truyện ngắn `projects/archive/ham-mo/`** | Trung bình | Tách biệt rõ ngay từ mở đầu: MC của `kho-hai-tien-lo` **có tên họ, có gia cảnh & bi kịch phàm trần cụ thể trước khi vào mỏ**, sở hữu **Ngũ linh căn tạp phẩm + Chí bảo thiên địa**, và mục tiêu là **leo lên nắm chỗ đứng trong tông môn** (epic nhiều quyển) chứ không dừng ở việc thoát khỏi cửa hầm. |
| 4 | **Mâu thuẫn luật Cõi giới (đặt nhầm tông môn ở Phàm Giới)** | Thấp | Đã khóa cứng trong §4b: bối cảnh đặt tại **Càn Nguyên Tinh (Linh Giới)** theo Luật 6b — nơi phàm nhân và tu sĩ sống chung. |

## 8. DECISIONS — LOCKED / APPROVED (User chốt 2026-10-23)

| # | Hạng mục | Quyết định đã khóa (LOCKED) |
| --- | --- | --- |
| 1 | **Chế độ điều phối** | `auto-approve: false` — duyệt từng bước qua human gate |
| 2 | **Tên tác phẩm & Tên MC** | Giữ tên hiển thị tạm **Khổ Hải Tiên Lộ** (`kho-hai-tien-lo`); giao `xianxia-naming-specialist` đề xuất tên Hán Việt cổ kính, trầm mặc cho MC (và hệ thống tên riêng) ở bước `T-naming-people-project` |
| 3 | **Cơ chế "Bảo vật của trời đất"** | **Kết hợp (A) Tinh lọc phế khoáng/đan ở tầng thấp + (C) Cân bằng & Dung hợp Ngũ hành ở cảnh giới cao** (mở khóa theo tầng): Giai đoạn đầu ở khu mỏ (Luyện Khí), bảo vật chỉ lọc sát khí/tạp chất từ phế khoáng & đan hạ phẩm thành linh dịch Ngũ hành cân bằng; lên cảnh giới cao mới mở khả năng dung hợp Ngũ hành căn. Luôn có điều kiện/nguyên liệu kích hoạt và cái giá theo Core `03` |
| 4 | **Điểm mở màn Chương 1** | **Mở màn 1–2 chương ở thôn trang phàm trần** (khắc họa cuộc sống cơ cực nhưng ấm áp → bi kịch tột cùng ập đến + nhặt bảo vật) rồi mới bị đẩy vào khu mỏ tạp dịch của tông môn |
| 5 | **Tính chất Tông môn khởi điểm** | **Chính đạo danh môn địa phương** trên đại lục Trung Linh (`CHL-TRUNG-LINH`) — bề ngoài quang minh chính đại, giữ đạo thống, nhưng tầng đáy bóc lột hợp pháp và tàn khốc bằng môn quy/khế ước |
| 6 | **Quy mô Arc 1 (Tạp Dịch Khu Mỏ)** | **Ngắn gọn (~15–20 chương)**, nhịp cô đọng, đẩy nhanh tiến độ từ bi kịch phàm trần → sống sót và tích lũy ở khu mỏ → vượt biến cố/khảo hạch bước vào ngoại/nội môn và có chỗ đứng trong tông môn |

### 8b. Ràng buộc tự sự Arc 1 *(đồng bộ `T-plot-arc-1` · 2026-10-23 · chờ human duyệt cùng Phần I beats)*

> Neo: [`logic/arcs/00-arc-master-outline.md`](logic/arcs/00-arc-master-outline.md) §E1 (R-02, R-03, R-04) · [`logic/arcs/01-arc1-beats.md`](logic/arcs/01-arc1-beats.md) §E2. Không đổi 6 quyết định LOCKED ở §8.

| Mã | Ràng buộc | Phạm vi | Chi tiết áp dụng trong beats |
| --- | --- | --- | --- |
| **R-02** | **Phàm mở:** ch.1–2 ở thôn phàm trần; gia đình hiện bằng chi tiết đời thường; không nhồi lore; vào hầm chậm nhất cuối ch.4 | Arc 1 ch.1–2 *(ch.3–4 khổ dịch)* | B01–B03; ch.1 có điềm nhỏ, ch.2 là đỉnh arc |
| **R-03** | **Band 1–18:** Arc 1 ~15–20 chương, chốt **ch.1–18**; Đinh lão chết ch.15 *(cuối)* – ch.16 *(tang, mộ)* theo D-08 | Arc 1 | 20 beat B01–B20; hạ nhiệt ở ch.17–18 |
| **R-04** | **Mật độ sức mạnh Arc 1:** chỉ Bậc 0 và Bậc A của ấn, cùng **dấu hiệu A-cao** *(ấn đòi hệ thiếu)*; không mở C-sơ trọn vẹn, không nêu C-cao; Hàn kết arc **Luyện Khí tầng 4** *(sổ ghi tầng 3)*; đối thủ trực tiếp cao nhất là Lương Khôn Luyện Khí tầng 9 | Arc 1 | §A2a-2 ngân sách ấn; hai lần dừng bắt buộc; điểm nghẽn 3→4 giải bằng ngộ tính |

## 9. Giả định đã chốt tạm

- Dùng chung `foundation_root: foundation/`; bối cảnh đặt tại **Càn Nguyên Tinh (`TH-LINH-CAN-NGUYEN`) — Linh Giới**, vùng biên mỏ khoáng `REG-TL-TAY-MACH` thuộc đại lục **Trung Linh** (`CHL-TRUNG-LINH`).
- Miễn trừ `T-world-project` (`waive_T-world-project: true`) ở Phase A1; không chạy pipeline sinh GeoJSON mới ở A1.
- Ngôi kể: **Ngôi thứ ba giới hạn (MC)** xuyên suốt; văn phong cổ phong trầm mặc, giàu chi tiết đời thường và thực cảm tu luyện, không dùng tiếng Anh.
- Độ dài chuẩn mỗi chương: **~3.000–3.500 chữ**.

## 10. Changelog brief

| Version | Date | Thay đổi |
| --- | --- | --- |
| v1 | 2026-10-23 | Khởi tạo Master Brief cho dự án tiểu thuyết dài kỳ `kho-hai-tien-lo` (**Khổ Hải Tiên Lộ**) từ raw intent của User; đối chiếu Foundation Core & World (`TH-LINH-CAN-NGUYEN`); chốt `world_strategy: foundation-fixed` (`waive_T-world-project: true`); thiết lập 5 câu hỏi DECISION NEEDED, Task queue sơ bộ và Risk register. |
| v2 | 2026-10-23 | **User APPROVED `T-brief`:** khóa 6 quyết định tại §8 (tên tạm + naming sau; Bảo vật kết hợp A+C mở khóa theo tầng; mở màn 1–2 chương ở thôn trang phàm trần; Tông môn Chính đạo ngoài sáng trong tối; quy mô Arc 1 rút gọn cô đọng **~15–20 chương**; `auto-approve: false`). |
| v2.1 | 2026-10-23 | Thêm **§8b** ràng buộc tự sự Arc 1 (R-02 phàm mở · R-03 band 1–18 · R-04 mật độ sức mạnh) từ `T-plot-arc-1`; không đổi §8 LOCKED. |
