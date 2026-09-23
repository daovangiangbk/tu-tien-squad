# Master Brief — Hầm mỏ — v2 — 2026-09-22

> Khung làm việc cho hệ subagent. Cập nhật version + mục **Changelog** khi đổi phạm vi; `project-orchestrator` đánh dấu artifact stale.

## 0. Work identity

| Trường | Giá trị |
| --- | --- |
| **work_title** | **Hầm mỏ** |
| **work_title_short** | *Hầm mỏ* |
| **work_slug** | `ham-mo` |
| **work_root** | `projects/ham-mo/` |
| **foundation_root** | `foundation/` *(shared — Core tại repo root)* |
| **logic_root** | `projects/ham-mo/logic/` |
| **interface_root** | `projects/ham-mo/interface/` |
| **pipeline** | **A** — sáng tác; **format truyện ngắn** (không epic) |

## 1. Raw intent (user)

> - Một **kẻ phàm nhân không tên**, làm việc khổ sai trong **khu mỏ linh thạch** của một **đại tông môn**, đổi công lấy **bạc** để sinh sống qua ngày.
> - Với **khát khao sinh tồn**, hắn tìm được **cơ duyên khai mở linh căn** sau cuộc **vật lộn sinh tử** trong **vụ sập hầm**, tìm lại sự sống.
> - Chủ đích nghệ thuật: thể hiện **mặt tối** của xã hội, tầng lớp tu tiên, kẻ thống trị.
> - **Kết:** **Tia sáng** lọt qua lớp đá nơi cửa hầm — mở **chương cuộc đời mới** (hy vọng / mở đầu hành trình, không đại kết epic).
> - Format: truyện **ngắn** — thu gọn Phase/Arc/chapter spine.

## 2. Tóm tắt điều hành (5–10 dòng)

Truyện ngắn tiên hiệp, tone **Tru Tiên xám**: phàm nhân **vô danh** trong **mỏ linh thạch** đại tông — lao động nặng, đổi công lấy **bạc phàm**, sống dưới áp bức tầng tu và quản mỏ. Cốt lõi cảm xúc: **sinh tồn** trước **cơ duyên** — vụ **sập hầm** là điểm gãy, trong vật lộn sinh tử hắn **khai linh căn** (bước vào nhập đạo tiềm năng, chưa cần kể tu luyện dài). Kết mở: **tia sáng cửa hầm** = hy vọng / cánh cửa đời mới, **không** đại kết báo thù hay phi thăng. **Một arc**, **4 chương** (~3.000–3.500 chữ/chương, tổng ~12–14k) — **user chốt**. Core shared `foundation/core/`; **waive** `T-world-geo-stack` — chỉ **micro-setting** mỏ + tông placeholder. Không prose cho đến khi spine + naming tối thiểu.

## 3. Mục tiêu & thành công

- **Sản phẩm:** Truyện ngắn markdown trong `projects/ham-mo/interface/chapters/`.
- **Độc giả / tone:** Đọc xong thấy **mặt tối tầng lớp** (kẻ mạnh, quản mỏ, kinh tế hai đẳng cấp) và **một tia sáng** không sentimental quá mức — xám nhưng không vô vọng tuyệt đối.
- **Thành công nội dung:** Đủ beat lao động → áp bức → sập hầm → khai căn → thoát/kết ánh sáng; MC có **vết thương sinh tồn** khớp theme Core `01`; kinh tế **bạc vs linh thạch** nhất quán `03`.
- **Thành công kỹ thuật:** Brief + spine + registry placeholder → prose → review; **không** GeoJSON; **không** sửa Core im lặng.
- **Không làm:** Epic arc, foreshadow dài hơi, power creep sau khai căn, miêu tả graphic tử vong hàng loạt, tiếng Anh trong prose.

## 4. Phạm vi & quy mô

| Hạng mục | Giá trị |
| --- | --- |
| **Format** | **Truyện ngắn** — không multi-arc epic |
| **Phase / arc** | **1 phase · 1 arc** — *Hầm sập · linh căn* |
| **Số chương** | **4 chương** *(user chốt)* |
| **Độ dài/chương** | ~3.000–3.500 chữ `[giả định]` |
| **Tổng ước lượng** | ~12.000–14.000 chữ |
| **Endgame** | **Out of scope** — kết mở; không cam kết tiếp tục series |
| **POV** | Third limited (MC vô danh); không đa POV chính |
| **Định dạng output** | Markdown dưới `projects/ham-mo/interface/` |
| **Ngôn ngữ** | Tiếng Việt; Hán Việt theo `foundation/core/00-glossary.md` |
| **World / geo** | **Micro-setting only** — mô tả mỏ, hầm, cửa ra; **`T-world-geo-stack` waive / out of scope** |

### Plot beats (xương sống — Logic sẽ chi tiết hóa)

| # | Beat | Gợi ý chương |
| --- | --- | --- |
| 1 | **Lao động** — ca khai thác, quy củ, đổi công lấy bạc; thân phận phàm | ch.1 |
| 2 | **Áp bức** — tầng tu / quản mỏ / kinh tế linh thạch vs bạc; bất công lộ rõ | ch.2 |
| 3 | **Sập hầm** — vật lộn sinh tử, chết chóc xung quanh; MC sống sót trong kẽ đá | ch.3 |
| 4 | **Khai linh căn · tia sáng** — cơ duyên trong hầm; thoát tới cửa; kết mở ánh sáng | ch.4 |

### Micro-setting (placeholder — naming sau)

| Thành phần | Mô tả tạm |
| --- | --- |
| **Đại tông** | **Placeholder riêng work** — không tái dùng canon shared; tên Hán Việt do `xianxia-naming-specialist` → `interface/naming/registry.md` |
| **Khu mỏ linh thạch** | Hầm sâu, đèn dầu/mỏ, điểm giao bạc; linh thạch thu về kho tông, không vào túi phàm nhân |
| **Nhân vật phụ** | Quản mỏ, giám công, vài phàm cùng ca — roster tối thiểu trong arc |

## 5. Ràng buộc sáng tác

- **Theme ưu tiên:** **Cường giả vi tôn** + **Nhân-Quả** ở tầng thấp (phàm không có quyền tự quyết); **sinh tồn** trước đạo lý (`01-theme-tragedy-core.md`); Chính–Tà theo **ứng xử** quản mỏ / tông, không phe thuần ác/tốt.
- **MC:** Phàm nhân **vô danh đến hết** truyện — prose không gán họ tên hay biệt danh ca làm tên nhân vật; **vô căn thuần** lúc mở đầu → **khai linh căn lần đầu** trong/ sau vật lộn sập hầm (không hữu căn ẩn).
- **MC wound (work-specific):** Gốc = **“chỉ sinh tồn hôm nay mới đáng”** — niềm tin sai: *công bằng không tồn tại, chỉ có trốn hoặc chết*; khai căn không xóa xám ngay — chỉ mở **khả năng** đi tiếp.
- **Cõi arc:** **Linh Giới** — mỏ + đại tông + phu mỏ phàm + quản khu tu ( Luật 6b ). **Không** đặt trên Phàm Giới ( Luật 6a — không chân tu cư trú ).
- **Kinh tế:** Phàm nhân nhận **bạc phàm**; **linh thạch** tiền tệ tu — thu mỏ về tông (`03` §3.1b, resources `01-linh-thach-tien-te.md`). Không cho phàm nhân cầm linh thạch hợp pháp trừ Logic gài vi phạm có **cái giá**.
- **Lao động phu mỏ:** **Lừa dụ chiêu công → ép nợ → ép làm** ( không nô lệ ); phàm **có trí**, **biết bị lừa**, **muốn trốn** — kẹt sổ + gác. Chi tiết `logic/world/00-micro-mo-setting.md` §1.3.
- **Tu vi mốc kết:** Tối đa **Luyện Khí sơ khai / vừa khai linh căn** — không đột phá arc trong truyện ngắn `[giả định]`.
- **Phong cách:** Cổ phong, trầm; **tình cảnh tương sinh** (bụi mỏ, tối hầm, ánh sáng cuối); không bài giảng xã hội học — show qua hành vi quản mỏ và ca lao động.
- **Kết:** **Tia sáng cửa hầm** — hy vọng / mở đầu; không cliffhanger báo thù tông.

## 6. Yêu cầu theo lớp

### Foundation (`foundation_root`)

- [x] Core `00-glossary.md`, `01-theme-tragedy-core.md`, `02-world-laws-lore-core.md`, `03-power-system-economy-core.md` — **đọc, không sửa** cho work khác.
- [x] Tham chiếu phàm nhân / linh căn / kinh tế: `03` §1.1; demographics `foundation/logic/03-demographics-pham-linh.md` nếu cần tỉ lệ vô căn.
- [ ] **`T-theme-mc`** (hoặc character-architect rút gọn): MC wound + sinh tồn — **không** bắt buộc CP/RP trừ khi đặt tên tông/mỏ promotion.
- [ ] **Promotion có tên** (tông, mỏ, địa danh micro): `foundation/resources/` **sau** human gate — ưu tiên giữ trong `interface/naming/registry.md` nếu chỉ dùng một lần.

**Foundation gaps (nhẹ — truyện ngắn):**

| Gap | Hướng xử lý |
| --- | --- |
| Tên đại tông + mỏ | **Naming** → `interface/naming/registry.md`; RP chỉ nếu promotion shared |
| Quy chế mỏ phàm nhân | **Logic/world** micro 1–2 trang; không geo stack |

### Logic — DoD truyện ngắn

- [ ] **MC theme / wound** — `logic/characters/00-mc-profile.md` (hoặc tương đương) — owner: character-architect / theme pass
- [ ] **`logic/00-story-spine.md`** — 4 beat + emotional through-line
- [ ] **`logic/chapters/00-chapter-spine-ham-mo.md`** — bảng 4 chương, hook cuối ch.4 = tia sáng
- [ ] **`logic/world/00-micro-mo-setting.md`** — mỏ, hầm, quy củ bạc; **không** GeoJSON
- [ ] **Skip / waive:** `arc-planner` epic, `foreshadowing-architect` ledger dài, **`T-world-geo-stack`**

### Interface — DoD trước prose

- [ ] `xianxia-naming-specialist` → `interface/naming/registry.md` — tông/mỏ/quản mỏ (work-only); MC **không** đặt tên trong registry
- [ ] `interface/chapters/00-index.md` — 4 chương planned
- [ ] `xianxia-prose-writer` → `interface/chapters/chapter-NN-*.md` — **sau** spine + naming
- [ ] Review: `xianxia-chapter-reviewer` → `interface/chapter-view/review-chapter-NN-*.md`

## 7. Deliverables & đường dẫn

| Artifact | Path | Owner agent |
| --- | --- | --- |
| Master Brief | `projects/ham-mo/00-master-brief.md` | requirements-briefer |
| Progress map | `projects/ham-mo/00-progress-map.md` | project-orchestrator |
| Trạng thái | `projects/ham-mo/status.md` | project-orchestrator |
| Story spine | `projects/ham-mo/logic/00-story-spine.md` | arc-planner / orchestrator |
| Chapter spine | `projects/ham-mo/logic/chapters/00-chapter-spine-ham-mo.md` | arc-planner / orchestrator |
| Micro world | `projects/ham-mo/logic/world/00-micro-mo-setting.md` | world-builder (micro only) |
| MC profile | `projects/ham-mo/logic/characters/00-mc-profile.md` | character-architect |
| Tên canon | `projects/ham-mo/interface/naming/registry.md` | xianxia-naming-specialist |
| Chương | `projects/ham-mo/interface/chapters/` | xianxia-prose-writer |
| Review | `projects/ham-mo/interface/chapter-view/review-chapter-NN-*.md` | xianxia-chapter-reviewer |

### Task queue sơ bộ (handoff orchestrator)

| Task ID | Agent | Input | Output | DoD | Deps |
| --- | --- | --- | --- | --- | --- |
| `T-brief-init` | requirements-briefer | Raw intent | `00-master-brief.md` | §0–10 đầy đủ | — |
| `T-theme-mc` | character-architect | brief §5, Core `01` | `logic/characters/00-mc-profile.md` | Wound + desire + không tên canon | `T-brief-init` |
| `T-micro-world` | world-builder | brief §4 micro | `logic/world/00-micro-mo-setting.md` | Mỏ, bạc/linh thạch, quy củ; no geo | `T-brief-init` |
| `T-spine-short` | arc-planner | brief beats | `logic/00-story-spine.md`, `logic/chapters/00-chapter-spine-*.md` | 4 chương + hook kết | `T-theme-mc`, `T-micro-world` |
| `T-naming` | xianxia-naming-specialist | spine + micro | `interface/naming/registry.md` | Tông, mỏ, biệt danh MC | `T-spine-short` |
| `T-prose-1..4` | xianxia-prose-writer | spine, registry | `interface/chapters/chapter-NN-*.md` | Khớp beat; xám; không EN | `T-naming` |
| `T-review-N` | xianxia-chapter-reviewer | prose N | `interface/chapter-view/review-*` | Read-only review | mỗi `T-prose-N` |

## 8. DECISION — user chốt (2026-09-22)

| # | Câu hỏi | Quyết định |
| --- | --- | --- |
| 1 | Title / slug | **Hầm mỏ** · `ham-mo` |
| 2 | Cấu trúc | **4 chương** (~12–14k) |
| 3 | MC | **Vô danh đến hết** |
| 4 | Linh căn | **Vô căn thuần** → khai lần đầu sau sập hầm |
| 5 | Tông môn | **Placeholder riêng work** (registry, không promotion shared trừ human sau) |

## 9. Giả định còn lại

- `[giả định]` ~3.000–3.500 chữ/chương, **1 arc**.
- `[giả định]` **foundation_root: `foundation/`** — luật tu/kinh tế shared; tên tông/mỏ work-only.
- `[giả định]` **Waive `T-world-geo-stack`** — chỉ micro-setting Logic.
- `[giả định]` Kết **tia sáng cửa hầm** = mở đầu hành trình, không series bắt buộc.
- `[giả định]` Sau sập ở mức **vừa khai linh căn** (chưa cần chiến đấu tu tiên).

## 10. Changelog brief

| Version | Date | Thay đổi |
| --- | --- | --- |
| v1 | 2026-09-22 | Khởi tạo — truyện ngắn Pipeline A; raw intent user; waive geo stack |
| v2 | 2026-09-22 | User chốt §8: `ham-mo`, 4 chương, vô danh, vô căn thuần, tông work-only |
| v2.1 | 2026-09-22 | Sync Luật 6b: arc **Linh Giới** ( không Phàm ); bạc phàm trên Linh |
