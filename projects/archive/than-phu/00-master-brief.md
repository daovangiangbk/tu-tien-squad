# Master Brief — Thần Phù — v1 — 2026-09-17

> Khung làm việc cho hệ subagent. Cập nhật version + mục **Changelog** khi đổi phạm vi; `project-orchestrator` đánh dấu artifact stale.

## 0. Work identity

| Trường              | Giá trị                                       |
| ------------------- | --------------------------------------------- |
| **work_title**      | **Thần Phù**                            |
| **work_title_short**| *Thần Phù* — rút gọn khi cần                  |
| **work_slug**       | `than-phu`                                    |
| **work_root**       | `projects/than-phu/`                          |
| **foundation_root** | `foundation/` *(shared — Core tại repo root; tách khỏi `tap-linh-dieu-lo`)* |
| **logic_root**      | `projects/than-phu/logic/`                    |
| **interface_root**  | `projects/than-phu/interface/`                |

## 1. Raw intent (user)

> - MC: gia tộc tu tiên giàu có, công tử con một, thiên tư kém, bỏ bê tu hành, thực lực thấp.
> - Gia tộc biến cố — cửu địch thảm sát, người thân ly tán.
> - MC thoát nạn nhờ hi sinh người thân, tỉnh ngộ, báo thù.
> - Vô tình tìm bộ công thức phù tiên gia giấu kỹ → phù sư + nâng thực lực + điều tra kẻ thù.
> - Ma tu bắt cóc trẻ em trong thành luyện huyết — tuyến điều tra mở rộng.
> - Trên đường báo thù khai phá giang hồ tu tiên.

## 2. Tóm tắt điều hành (5–10 dòng)

Tiểu thuyết tiên hiệp dài, tone **Tru Tiên** (triết lý xám, bi kịch, phục bút). **MC contract:** công tử **gia tộc phù / tài phú** — thiên tư kém, bỏ bê tu, **thực lực thấp** lúc mở đầu; biến cố **cửu địch tàn sát** → sống sót nhờ **hi sinh người thân** → vết **tội lỗi sống sót** + động lực **báo thù** (Hữu tình, không slogan). Nhánh sức mạnh khác biệt: **phù đạo / phù sư** từ **công thức gia tộc giấu kỹ** song song **tu thực lực** — phù bù khoảng cách ngắn, tu vi là nền dài; mọi buff bám trade-off Core (`06-phu-luc`, `03` §3.5). **Phase 1 Logic:** 2–3 arc đến **Trúc Cơ kỳ đỉnh phong**; tuyến ma tu **luyện huyết / bắt cóc** mở rộng điều tra trong thành trước khi giang hồ sâu hơn. Core shared `foundation/core/00–03`; tên canon **chưa chốt** — placeholder §8.

## 3. Mục tiêu & thành công

- **Sản phẩm:** Tiểu thuyết markdown trong repo; có thể xuất bản sau.
- **Độc giả / tone:** Quen “cái giá tu luyện”; phe xám; cảm xúc trầm; **phục bút** cửu địch / ma tuyến không payoff sớm.
- **Phase 1 thành công:** Arc outline + wound MC khớp theme Core `01`; phù đạo **không** phá invariant kích phát / cảnh giới (`06` §0); MC đến **Trúc Cơ đỉnh phong** có lộ trình phù + tu vi **có giá** (thần thức, vật liệu, Nghiệp nếu chạm Ma phù).
- **Không làm:** Power creep phù thay đại cảnh giới; miễn phí kích phát; spoil danh tính cửu địch / twist arc xa sớm; sửa Core im lặng; tiếng Anh trong prose chương.

## 4. Phạm vi & quy mô

| Hạng mục | Giá trị |
| --- | --- |
| **Phase 1 (Logic v1)** | **2–3 arc** đến **Trúc Cơ kỳ đỉnh phong** |
| **Quy mô phase 1** | ~80–120 chương; ~2.500–4.000 chữ/chương `[giả định — khớp repo sibling]` |
| **Endgame dài hạn** | Kim Đan+, phi thăng, đại kết báo thù / Nhân-Quả — **deferred** |
| **POV** | Third limited (MC); không đa POV chính |
| **Định dạng output** | Markdown dưới `projects/than-phu/interface/` |
| **Ngôn ngữ** | Tiếng Việt; danh từ riêng Hán Việt theo `foundation/core/00-glossary.md` |

### Phase 1 — đại cục arc (canon địa danh 2026-09-17)

| Arc | Trọng tâm | Mốc tu vi (ước) |
| --- | --- | --- |
| **Arc 1 — Phù Lĩnh Huyết Dạ** | **Phù Lĩnh Lệnh** · biến cố **Thẩm thị**; **Thần Phù Cổ Phổ**; sinh tồn; manh **Hàn Diệp Liên** | Phàm / LK sơ — LK trung (phù hạ làm then chốt sinh tồn) |
| **Arc 2 — Thanh Phù U Huyết** | **Thanh Phù Thành**; điều tra **U Huyết Các** / luyện huyết, bắt cóc trẻ; **Thiên Phù Các phân điếm** xám | LK hậu — Trúc Cơ sơ |
| **Arc 3 — Phù Giang Báo** | Giang hồ **Phù Viên**; báo thù + phù nâng cấp; payoff cửu địch / ma tuyến | Trúc Cơ trung → **đỉnh phong** |

*Chi tiết beat / chương:* Logic sau `arc-planner`; không viết prose trước arc + foreshadow.

## 5. Ràng buộc sáng tác

- **Theme ưu tiên:** Nghịch Thiên Nhi Hành; **Hữu tình** (máu thân, báo thù) vs áp lực **Vô tình** khi tu nhanh; Chính–Tà theo **ứng xụ**; Cường giả vi tôn; Nhân-Quả (`01-theme-tragedy-core.md`).
- **MC wound (work-specific, bám Core):** Gốc = **người thân hy sinh để cứu “phế”** → vết *“ta đáng bị thay thế”* / *“nợ máu không trả hết”*; niềm tin sai: *chỉ sức mạnh + trả thù mới xứng sống* — mirror §3.1 nhưng xuất thân **giàu / danh** thay vùng nghèo.
- **Luật phù & tu:** `foundation/resources/06-phu-luc.md` (vẽ · kích · hao); phụ nghề `10-phu-nghe-tu-tien.md`; Ma phù / luyện huyết → **Luật 4** (`02-world-laws-lore-core.md`).
- **Khác biệt vs Tru Tiên / vs `tap-linh-dieu-lo`:** Cùng xám + phục bút; khác **gia tộc phù**, **công thức độc quyền**, MC **phế danh tiếng** (không tán tu tạp căn); trục **điều tra + báo thù** rõ hơn cơ duyên lang bạt.
- **Nội dung nhạy cảm:** Tàn sát gia tộc, hi sinh người thân, bắt cóc trẻ — **trên trang có cái giá & không miêu tả graphic**; ma tu hành vi **logic xám**, không phe thuần ác vô lý (`01` §3.4).

## 6. Yêu cầu theo lớp

### Foundation (`foundation_root`)

- [x] Core `00-glossary.md`, `01-theme-tragedy-core.md`, `02-world-laws-lore-core.md`, `03-power-system-economy-core.md` — **dùng chung**, không ghi đè cho work khác.
- [x] Hub phù / phụ nghề: `resources/06-phu-luc.md`, `resources/10-phu-nghe-tu-tien.md` — invariant đủ cho phase 1 **nếu** công thức gia tộc map vào phẩm phù / hạng sư có sẵn.
- [ ] **`T-init-cp-rp` (orchestrator):** Core Proposals + Resource Proposals trước Foundation pass — xem **Foundation gaps** dưới đây.
- [ ] **Promotion có tên** (phù riêng, ấn pháp tộc, đan/vật liệu arc): `foundation/resources/` theo [`foundation/resources/README.md`](../../foundation/resources/README.md) — **sau** human gate CP/RP.

**Foundation gaps (đầu vào CP/RP — không invent canon trong brief):**

| Gap | Ghi chú | Hướng xử lý đề xuất |
| --- | --- | --- |
| **Hệ công thức phù gia tộc Thẩm thị · Phù Lĩnh** | Catalog `06` §9.1 + **Thần Phù Cổ Phổ** (work) | **RP** chi tiết phù tộc khi arc chốt; registry `interface/naming/registry.md` |
| **Song hành phù sư + tu vi (MC kém căn)** | `10` §1: phụ nghề không thay cảnh giới; `06`: phù không nâng đại cảnh giới — **thiếu** guideline pacing “phế tu + công thức mạnh” cho arc planner | **Logic** (`logic/characters/`, arc beats); **CP nhẹ** chỉ nếu công thức vượt chuẩn Hoàng–Huyền cần luật riêng |
| **Luyện huyết / bắt cóc trẻ (tuyến thành)** | Ma phù (`Huyết Sát`, v.v.) + Luật 4 có; **quy mô điều tra đô thị** (ai che chở, quan phủ, hắc thị) chưa map work | **Logic/world** + tham chiếu `foundation/logic/01-event-scale-system.md`; CP nếu cần phe mới cấp vùng |
| **Gia tộc giàu / Phù các vs tộc nhà** | Glossary + `03` § kinh tế gia tộc; **chưa** liên kết “phù gia tộc giàu” với cống hiến Phù các | **RP** `06` hoặc Logic kinh tế arc 1–2 |
| **Cửu địch & thảm sát quy mô lớn** | Theme + event scale — **tên phe / lịch sử** thuộc naming & Logic | **Không** Core trừ alliance cấp lục địa user chốt sau |
| **Thiên phú kém (con một)** | Pool `11-thien-phu-ky-nang-an.md` — variant “căn kém + tài sản gia tộc” | **Logic character**; không bắt buộc Core |

### Logic — DoD phase 1

- [x] `character-architect` → `logic/characters/` — khung MC + gia tộc + silhouette (2026-09-17)
- [ ] `arc-planner` → `logic/arcs/00-arc-master-outline.md` — 2–3 arc → Trúc Cơ đỉnh phong; arc 2 gắn thành + luyện huyết
- [ ] `logic/arcs/01-arc1-beats.md` (khuyến nghị) — biến cố, công thức, hook chương 1
- [ ] `foreshadowing-architect` → `logic/foreshadowing/00-foreshadow-ledger.md` — cửu địch, công thức, ma tuyến; không payoff sớm
- [ ] `world-builder` → `logic/world/` — vùng gia tộc, thành, geo nếu cần (campaign `T-world-geo-stack`)
- [ ] Tham chiếu quy mô: `foundation/logic/01-event-scale-system.md`

### Interface — DoD trước chương 1

- [x] `xianxia-naming-specialist` → `interface/naming/registry.md` — khung canon MC / Thẩm thị / Thanh Phù Thành (2026-09-17)
- [ ] `interface/chapters/00-index.md` — cập nhật khi có chapter spine
- [ ] `xianxia-prose-writer` → `interface/chapters/` — **sau** arc beats + naming + consistency
- [ ] Review: `xianxia-chapter-reviewer` → `interface/chapter-view/review-chapter-NN-*.md`

## 7. Deliverables & đường dẫn

| Artifact | Path | Owner agent |
| --- | --- | --- |
| Master Brief | `projects/than-phu/00-master-brief.md` | requirements-briefer |
| Progress map | `projects/than-phu/00-progress-map.md` | project-orchestrator |
| Execution plan | `projects/than-phu/01-execution-plan.md` | user / orchestrator |
| Trạng thái | `projects/than-phu/status.md` | project-orchestrator |
| Core proposals | `projects/than-phu/core-proposals/CP-*.md`, `RP-*.md` | orchestrator → Foundation |
| Character roster | `projects/than-phu/logic/characters/` | character-architect |
| Arc outline | `projects/than-phu/logic/arcs/` | arc-planner |
| Foreshadow ledger | `projects/than-phu/logic/foreshadowing/` | foreshadowing-architect |
| World / geo | `projects/than-phu/logic/world/` | world-builder |
| Tên canon | `projects/than-phu/interface/naming/registry.md` | xianxia-naming-specialist |
| Chương | `projects/than-phu/interface/chapters/` | xianxia-prose-writer |
| Core (shared) | `foundation/core/00–03`, `foundation/resources/06`, `10` | Foundation agents (sau CP) |

### Task queue sơ bộ (handoff orchestrator)

| Task ID | Agent | Input | Output | DoD | Deps |
| --- | --- | --- | --- | --- | --- |
| T-init-cp-rp | orchestrator | Brief §6 gaps | `core-proposals/CP-*.md`, `RP-*.md` | Proposal có invariant + không trùng tap-linh canon | T-init-brief |
| T-init-foundation | theme / world-laws / power | CP approved | `foundation/core|resources/` | Merge không phá invariant `06` | T-init-cp-rp |
| T-world-geo-stack | world-builder | Brief §4, Logic region | `logic/world/` | Atlas 4 tầng hoặc markdown tương đương | T-init-foundation (partial OK) |
| T-init-characters | character-architect | Brief §2–5 | `logic/characters/` | MC wound + antagonist silhouette | T-init-cp-rp |
| T-init-arc | arc-planner | characters + world sketch | `logic/arcs/` | Mốc Trúc Cơ đỉnh phong | T-init-characters |
| T-init-fs | foreshadowing-architect | arc outline | `logic/foreshadowing/` | Ledger arc 1–3 | T-init-arc |
| T-init-naming | xianxia-naming-specialist | §8 decisions | `interface/naming/registry.md` | MC, gia tộc, thành canon | User §8 |
| T-init-status | project-orchestrator | pipeline | `status.md` | Queue rõ, không blocker giả | — |

### Risk register (ngắn)

1. **Phù quá mạnh sớm** — phá §0 `06`; arc planner phải gắn hao thần / vật liệu / phẩm phù.
2. **Công thức gia tộc = Deus ex** — cần CP/RP giới hạn cấp & điều kiện truyền trước prose.
3. **Tuyến bắt cóc trẻ** — dễ trượt tone; giữ xám, không miêu tả graphic; Ma phù = Nghiệp.
4. **Trùng DNA `tap-linh-dieu-lo`** — tách rõ gia tộc phù vs tán tu đa nghề; path & naming tách biệt.
5. **§8 chưa chốt tên** — block registry & chương 1; placeholder OK trong Logic đến naming task.

## 8. DECISION NEEDED / Open questions

| # | Chủ đề | Trạng thái | Ghi chú |
| --- | --- | --- | --- |
| 1 | **Tên MC** | **Chốt** | **Thẩm Vô Ngọc** — registry |
| 2 | **Tên gia tộc tu tiên** | **Chốt** | **Thẩm thị · Phù Lĩnh** — **Phù Lĩnh Lệnh** |
| 3 | **Tên thành trì (arc ma tu / luyện huyết)** | **Chốt** | **Thanh Phù Thành** |
| 4 | **Danh tính / tên cửu địch** | **Silhouette** | Liên minh **Hàn Diệp Liên** — **đầu não chưa tên** (arc 2+) |
| 5 | **Quan hệ tình (NC)** | **Chốt trì hoãn** | Không NC arc 1; có thể gài đồng minh xám arc 2+ — **không** tam giác sớm |
| 6 | **Công thức phù — cấp tối đa phase 1** | **Chốt** | **Huyền phẩm band** (`03` §3.5 + CP-001); **không** mở Địa phase 1 trừ RP riêng |
| 8 | **Mộ Thanh Y post-massacre** | **Chốt** | **Sống sót** · gặp MC beat 8 (Tây Lam) — `arc-1-beats` |
| 7 | **Human gate CP/RP** | ON (2026-09-17) | User: auto-approve hợp lý phù sư / công thức phù |

## 9. Giả định đã chốt tạm

- `foundation_root: foundation/` là canon shared; **không** sửa artifact `tap-linh-dieu-lo`.
- Phase 1 ceiling: **Trúc Cơ kỳ đỉnh phong**; endgame full bộ deferred.
- POV: third limited MC; prose tiếng Việt, không tiếng Anh trong chương.
- MC **không** bắt đầu mạnh; phù đạo tăng dần qua công thức + luyện, tu vi song hành có trade-off.
- Workflow: Brief → CP/RP → Foundation (nếu approve) → World ∥ Characters → Arc → Foreshadow → Naming → Chapter spine → Prose.

## 10. Changelog brief

- **v1.1 (2026-09-17):** Chốt khung naming — MC **Thẩm Vô Ngọc**, **Thẩm thị · Phù Lĩnh**, **Thanh Phù Thành**, silhouette **Hàn Diệp Liên** / **U Huyết Các**; registry + characters + `00-place-atlas.md`.
- **v1 (2026-09-17):** Khởi tạo từ raw intent user; work `than-phu`; baseline Foundation `core/00–03`, `resources/06-phu-luc`, `10-phu-nghe-tu-tien`; §6 Foundation gaps cho CP/RP; §8 placeholder MC / gia tộc / thành.
