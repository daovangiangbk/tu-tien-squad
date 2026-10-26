# Master Brief — Linh điền — v1.2 — 2026-09-24

> Khung làm việc cho hệ subagent. Cập nhật version + mục **Changelog** khi đổi phạm vi; `project-orchestrator` đánh dấu artifact stale.

## 0. Work identity

| Trường | Giá trị |
| --- | --- |
| **work_title** | **Linh điền** |
| **work_title_short** | *Linh điền* |
| **work_slug** | `linh-dien` |
| **work_root** | `projects/archive/linh-dien/` *(archived 2026-10-02)* |
| **foundation_root** | `foundation/` *(shared — Core tại repo root)* |
| **logic_root** | `projects/archive/linh-dien/logic/` |
| **interface_root** | `projects/archive/linh-dien/interface/` |
| **pipeline** | **A** — sáng tác; **1 arc · 5–10 chương** · slice-of-life + **phong cảnh hữu tình** |

## 1. Raw intent (user)

> - **Working title / concept:** Linh điền (Spirit Field)
> - **Genre & tone:** Gentle romance (hữu tình nhẹ nhàng); slice-of-life; **NO** power struggle, **NO** drama tranh đoạt
> - **Primary focus:** Life at a sect's spirit field (linh điền của tông môn)
> - **Emphasis:** landscape/scenery, daily life, diverse spirit herbs (linh thảo), planting, care, harvest, processing (trồng, chăm sóc, thu hoạch, chế biến)
> - **Constraints:** Vietnamese + Hán Việt canon naming; no English in chapter prose; 3-layer architecture; xianxia setting but low conflict — world rules still needed for linh thảo, linh khí, sect field hierarchy

### Raw intent — bổ sung user (2026-09-24, chốt canon)

> - **MC:** Nam · **Đại Thừa** · đã đạt **quyền lực chiến đấu tuyệt đối trong Linh Giới**, chán tranh đấu · trở về quản linh điền tại tông **tự lập** (đã lập nhiều tông lớn nhỏ khắp Linh Giới).
> - **Plot engine:** **Trải nghiệm cuộc sống yên bình** — **trồng linh thảo** trên điền; **thiếu kinh nghiệm linh nông** → bất ngờ / biến cố nhỏ khi trồng trọt (bón dư, nhầm loại, thúc cây bằng linh lực vô vọng, nhịp **chậm hơn** tu trước).
> - **Hữu tình:** **Phong cảnh hữu tình** — không khí / cảnh đẹp gợi cảm xúc dịu; **không** plot quan hệ nam-nữ.
> - **Quy mô:** **1 arc**, **5–10 chương** (<10); **không** bắt buộc kết dramatic.
> - **Geo:** **Micro-only** — không neo Mộc Dương giai đoạn này.
> - **Tên:** Không gợi ý user — foundation hoặc naming specialist sau.
> - **Focus repo:** `active-work.md` → **`linh-dien`**.

## 2. Tóm tắt điều hành (5–10 dòng)

Tiên hiệp **tĩnh** trên **một linh điền** tông **MC tự lập** (Linh Giới): MC **nam**, **Đại Thừa**, đỉnh chiến lực giới Linh nhưng **chọn điền** để **sống yên** — **trồng linh thảo**, **nhàm tranh đấu**; **thiếu kinh nghiệm nông** nên **vấp** việc nhỏ (không drama phe). Nhịp chậm: **cảnh sắc**, **mùa vụ**, trồng–chăm–thu–chế biến; **phong cảnh hữu tình** — **không** romance nhân vật. **1 arc · 5–10 chương**, kết **mềm**. Tone ấm, trong; stakes **điền** (thời tiết, sâu, **sai tay MC**, sai kỳ) — **không** chiến, **không** tranh đoạt. Neo `02-linh-duoc.md`, `10` §3.5, `03` §1.3. **Geo micro-only**. MC ẩn lực / không flex — `CP-001`.

## 3. Mục tiêu & thành công

- **Sản phẩm:** **5–10** chương markdown trong `projects/linh-dien/interface/chapters/`.
- **Độc giả / tone:** **Yên**, **đẹp**, đủ “tu tiện” (linh khí, trận điền, phân cấp) mà **không** căng chính trị hay leo cảnh.
- **Thành công nội dung:** **Yên bình** + **mùa vụ** show qua tay nghề; **sai lầm / sửa** (thiếu kinh nghiệm) **phong phú** mà nhẹ; **phong cảnh hữu tình** xuyên suốt; **không** dùng Đại Thừa giải plot.
- **Thành công kỹ thuật:** Logic (theme, micro-world, MC, spine 5–10) → naming → prose → review; không sửa Core im lặng.
- **Không làm:** Tranh đoạt, đại chiến, power creep arc, báo thù, plot tình, tiếng Anh trong prose.

## 4. Phạm vi & quy mô

| Hạng mục | Giá trị |
| --- | --- |
| **Format** | **Một arc** slice-of-life — **5–10 chương** (user chốt: dưới 10) |
| **Phase / arc** | **1 phase · 1 arc** — *Một mùa / giai đoạn trên linh điền* (Logic đặt tên) |
| **Số chương** | **5–10** *(chốt trong `00-chapter-spine-linh-dien.md`)* |
| **Độ dài/chương** | ~2.500–4.000 chữ/chương `[giả định]` |
| **Endgame** | **Không bắt buộc** kết dramatic — arc có thể dừng giữa nhịp điền / sau một mùa |
| **POV** | Third limited (MC) — **chốt** |
| **Định dạng output** | Markdown dưới `projects/linh-dien/interface/` |
| **Ngôn ngữ** | Tiếng Việt; Hán Việt theo glossary + registry |
| **World / geo** | **Micro-only** — một linh điền + tông MC lập; **`T-world-geo-stack` waive**; **không** Mộc Dương |

### MC (user chốt — Logic chi tiết hóa)

| Trường | Giá trị |
| --- | --- |
| **Giới** | Nam |
| **Cảnh giới** | **Đại Thừa** — neo `03` §1.3 |
| **Chiến lực (work)** | **Tuyệt đối trong phạm vi Linh Giới** (narrative framing; vẫn có **Độ Kiếp / Tiên** ở meta Core — không kể làm plot) |
| **Lịch sử** | Đã lập **nhiều** tông lớn nhỏ; quay lại **tự quản** một linh điền tông “tình cờ” / quen thuộc |
| **Động cơ** | **Yên bình** — **trồng linh thảo** trên điền; **nhàm** tranh đấu |
| **Plot phụ** | **Thiếu kinh nghiệm linh nông** → biến cố nhỏ khi trồng trọt |
| **Wound / theme** | **Không** bi kịch Tru Tiên — **yên + chậm + sai tay**; `00-theme-slice-light.md` |
| **Narrative rule** | **Ẩn / thu lực / không uy áp** — immersion low-stakes; xem `CP-001` |

### Trọng tâm nội dung (xương sống — Logic chi tiết hóa)

| Trục | Nội dung |
| --- | --- |
| **Cảnh** | Sương, luống, trận tụ linh, kho sơ chế — **phong cảnh hữu tình** |
| **Linh thảo** | **Sống cùng** thảo trên điền (`02-linh-duoc.md`) — học **kỳ, chăm** qua **việc + sửa lỗi**, không “săn catalog” |
| **Công việc** | Gieo, bón, tưới, thu, phơi, bảo quản, giao Đan các (nhẹ) |
| **Hữu tình** | **Cảnh & không khí** — **không** pairing, **không** tam giác |
| **Xung đột** | **Thấp** — thiên, sâu, linh khí lệch, deadline giao dược nhỏ; **không** tranh mạch / chiến |

### Micro-setting (naming sau)

| Thành phần | Mô tả tạm |
| --- | --- |
| **Tông môn** | Do MC **tự lập** — tên Hán Việt qua `T-naming` |
| **Linh điền** | Khu MC trực tiếp quản; trận tụ linh; có thể ít đệ tử / linh nông phàm nhân |
| **Nhân vật phụ** | Tối thiểu — thu mua dược, vài linh nông; **không** love interest bắt buộc |

## 5. Ràng buộc sáng tác

- **Theme:** **Yên bình · sinh trưởng chậm · thiếu kinh nghiệm**; Nhân-Quả nhẹ (sai kỳ / sai tay → sửa bằng công); **không** ép bi kịch `01`.
- **Tone:** Cổ phong, **ấm**, **tĩnh**; **tình cảnh tương sinh** + **phong cảnh hữu tình**.
- **Tu vi / power:** MC **đã Đại Thừa** — **không** leo cảnh arc; **cấm** combat set-piece / flex sức mạnh làm payoff. Uy lực chỉ **nền** (che giấu, không ai ép được MC).
- **Cõi:** **Linh Giới** — Luật 6b; **linh nông phàm nhân** có thể trên điền (`10` §3.5).
- **Kinh tế:** Cống hiến / giao dược — nhẹ; MC không tranh tài nguyên.
- **Đối lập `ham-mo`:** OUT xám mỏ, áp bức, sinh tử hầm.
- **Thuật ngữ:** **ca làm việc trên linh điền**; **phàm nhân** / **linh nông phàm nhân** (không *phàm* một mình); **bạc** (không *bạc phàm*) — xem `logic/README.md`.

### Out of scope (cứng)

| Loại | Ghi chú |
| --- | --- |
| Tranh đoạt linh điền / linh mạch | Event III+ |
| Đại chiến, tông chiến, Ma giáo | Không arc chính |
| Plot romance nam-nữ | User chốt: **phong cảnh hữu tình only** |
| Power creep, báo thù, nội đấu | Không |
| Geo Mộc Dương / atlas vùng | **Waive** giai đoạn này |

## 6. Yêu cầu theo lớp

### Foundation (`foundation_root`)

- [x] **Đọc, không sửa:** `00-glossary`, `01`, `02`, `03` — Đại Thừa §1.3
- [x] **Tham chiếu:** `02-linh-duoc.md`, `10-phu-nghe-tu-tien.md` §3.5, `01-event-scale-system.md` (scale **I**)
- [ ] **`CP-001`** — work instantiation MC peak · **deferred** Core (`core-proposals/CP-001-dai-thua-slice-instantiation.md`)

**Foundation gaps (work):**

| Gap | Hướng xử lý |
| --- | --- |
| Phân cấp linh điền tông MC lập | `00-micro-linh-dien-setting.md` |
| MC ẩn cư / không flex | Logic MC + micro-world § narrative |
| Tên tông, điền, thảo | ✅ `interface/naming/registry.md` |
| Quy trình sơ chế trên điền | Logic; **RP** tùy chọn sau |

### Logic — DoD trước prose

- [x] **`logic/00-theme-slice-light.md`** — theme nhẹ, ranh giới power, phong cảnh hữu tình
- [x] **`logic/world/00-micro-linh-dien-setting.md`** — điền, mùa, hierarchy, **MC trên điền**
- [x] **`logic/characters/00-mc-profile.md`** — Đại Thừa, động cơ, **không** romance lead bắt buộc
- [x] **`logic/00-story-spine.md`** + **`logic/chapters/00-chapter-spine-linh-dien.md`** — **8** ch
- [x] **Foreshadow:** waive hoặc tối thiểu
- [x] **Waive:** `T-world-geo-stack`, Mộc Dương

### Interface — DoD trước prose

- [x] `T-naming` → `interface/naming/registry.md`
- [x] `interface/chapters/00-index.md`
- [ ] Prose / review sau spine + naming

## 7. Deliverables & đường dẫn

| Artifact | Path | Owner agent |
| --- | --- | --- |
| Master Brief | `projects/linh-dien/00-master-brief.md` | requirements-briefer / orchestrator |
| Progress map | `projects/linh-dien/00-progress-map.md` | project-orchestrator |
| Trạng thái | `projects/linh-dien/status.md` | project-orchestrator |
| CP-001 | `projects/linh-dien/core-proposals/CP-001-*.md` | orchestrator |
| Theme slice | `logic/00-theme-slice-light.md` | character-architect |
| Micro world | `logic/world/00-micro-linh-dien-setting.md` | world-builder |
| MC | `logic/characters/00-mc-profile.md` | character-architect |
| Story / chapter spine | `logic/00-story-spine.md`, `logic/chapters/00-chapter-spine-linh-dien.md` | plot-architect |
| Registry | `interface/naming/registry.md` | xianxia-naming-specialist |

### Task queue (orchestrator)

| Task ID | Agent | Output | Deps |
| --- | --- | --- | --- |
| `T-brief` | requirements-briefer | brief v1 | — |
| **`T-brief-v1.1`** | orchestrator | brief v1.1 + active-work | user decisions |
| **`T-foundation-slice-read`** | world-builder | `00-micro-linh-dien-setting.md` (draft đầy đủ) | brief v1.1 |
| **`T-theme-slice-light`** | character-architect | `00-theme-slice-light.md`, `00-mc-profile.md` seed | brief v1.1 |
| `T-spine` | plot-architect | spine 5–10 ch | world + MC |
| `T-naming` | naming specialist | registry | spine |
| `T-prose-N` | prose writer | chapters | naming |

## 8. Quyết định đã chốt (user — 2026-09-24)

| # | Chủ đề | Quyết định |
| --- | --- | --- |
| 1 | **MC** | Nam · **Đại Thừa** · chán đấu · **yên bình + trồng thảo** trên điền tông **tự lập** · biến cố = **thiếu kinh nghiệm nông** (user 2026-09-24) |
| 2 | **Hữu tình** | **Phong cảnh hữu tình** — **không** plot quan hệ nam-nữ |
| 3 | **Tên** | Không gợi ý user — foundation + **T-naming** |
| 4 | **Quy mô** | **1 arc**, **5–10 chương** |
| 5 | **Kết arc** | Không bắt buộc kết dramatic |
| 6 | **Focus** | **`active-work.md` → `linh-dien`** |
| 7 | **Geo** | **Micro-only** — không Mộc Dương |

## 9. Giả định còn lại

- `[giả định]` **Độ dài/chương** ~2.500–4.000 chữ.
- `[giả định]` MC **tên** do naming — brief không gán tên.
- `[giả định]` **Event scale I** — một điền, không leo scale.
- `[giả định]` **Human gate** review trước revise (Pipeline A mặc định).

## 10. Changelog brief

| Version | Date | Thay đổi |
| --- | --- | --- |
| v1 | 2026-09-24 | Khởi tạo work; DECISION NEEDED §8 |
| v1.1 | 2026-09-24 | User chốt MC Đại Thừa, phong cảnh hữu tình, 5–10 ch, micro geo, active-work; §8 locked; CP-001 deferred |
| v1.2 | 2026-09-24 | Plot engine → **yên bình + trồng thảo**; biến cố **thiếu kinh nghiệm**; sync theme / world / MC profile |
