# Project status — Khổ Hải Tiên Lộ (`kho-hai-tien-lo`)

**Work slug:** `kho-hai-tien-lo`  
**Work root:** `projects/kho-hai-tien-lo/`  
**auto-approve:** `true` *(human bật auto gate 2026-10-23 cho đến hết Arc 1: prose → review → revise → approve)*  

## Project lifecycle

| Trường | Giá trị |
| --- | --- |
| **lifecycle** | `active` |
| **created_at** | `2026-10-23` |
| **pipeline** | **A** — Sáng tác tiểu thuyết tiên hiệp dài kỳ (epic multi-arc) |
| **workflow hiện tại** | **Arc 2 `CLOSED` (`complete` · ch.19–45 `approved`)** — Sẵn sàng mở **A2 Arc 3** (*Trúc Cơ Phong Vân & Bí Cảnh Cổ*) |
| **foundation_root** | `foundation/` (shared) |
| **world_strategy** | `foundation-fixed` (`TH-LINH-CAN-NGUYEN` · Càn Nguyên Tinh — Linh Giới · `waive_T-world-project: true`) |

## Snapshot

- **Master Brief:** [`00-master-brief.md`](00-master-brief.md) — **v2** (2026-10-23) · **`approved`**
- **Progress map:** [`00-progress-map.md`](00-progress-map.md)
- **World (Foundation shared + Arc 1 delta):** atlas Càn Nguyên · **micro Arc 1 `approved`** — [`logic/world/01-region-active.md`](logic/world/01-region-active.md), [`02-tieu-cuc-index.md`](logic/world/02-tieu-cuc-index.md), [`geo/micro/arc-01-kho-hai-tien-lo.geojson`](logic/world/geo/micro/arc-01-kho-hai-tien-lo.geojson)
- **Characters:** [`logic/characters/01-project-roster.md`](logic/characters/01-project-roster.md) **`canon`** (CHAR-001→012) · tên **`canon`**
- **Naming:** [`interface/naming/registry.md`](interface/naming/registry.md) — batch 1 + **sync delta merged canon** (2026-10-23)
- **Plot:** [`logic/00-story-spine.md`](logic/00-story-spine.md), [`logic/arcs/00-arc-master-outline.md`](logic/arcs/00-arc-master-outline.md) — Tier 1 **`approved`** (D-01→D-08 locked · human 2026-10-23) · audit: [`logic/audits/audit-plot-project.md`](logic/audits/audit-plot-project.md) **`approved with waived PW`** (verdict gốc `revise-logic-first` · PW-01→03 waived for A2 · 2026-10-23)
- **Foreshadow:** [`logic/foreshadowing/00-foreshadow-ledger.md`](logic/foreshadowing/00-foreshadow-ledger.md) — **`canon`** (FS-001→021 · FM-001→012 · **`FS-TBD-VILLAGE-TRUTH`** treo · human 2026-10-23)

---

## Task queue — Pipeline A

### A1 — Khởi tạo dự án (Project Initialization)

| Step | Task ID | State | Owner | Artifact / Ghi chú |
| --- | --- | --- | --- | --- |
| 1 | `T-brief` | **`done (approved)`** | `requirements-briefer` | [`00-master-brief.md`](00-master-brief.md) (v2) — human approved 2026-10-23 |
| 2 | `T-world-project` | **`done (waived)`** | `world-builder` | Skip theo §2.0 (`world_strategy: foundation-fixed`); micro khu mỏ tạo ở A2 `T-world-arc-1` |
| 3 | `T-characters-project` | **`done (approved)`** | `character-architect` | [`00-characters-index.md`](logic/characters/00-characters-index.md), [`01-project-roster.md`](logic/characters/01-project-roster.md) — human approved Phần I · 2026-10-23 |
| 3b | `T-naming-people-project` | **`done (approved)`** | `xianxia-naming-specialist` | [`interface/naming/registry.md`](interface/naming/registry.md) — human approved 2026-10-23 (batch CHAR-001→009) |
| 4 | `T-plot-project` | **`done (approved)`** | `plot-architect` | [`logic/00-story-spine.md`](logic/00-story-spine.md), [`logic/arcs/00-arc-master-outline.md`](logic/arcs/00-arc-master-outline.md) — human approved 2026-10-23 (bundle D-01→D-08) |
| 4b | `T-characters-project-sync` | **`done (approved)`** | `character-architect` | [`01-project-roster.md`](logic/characters/01-project-roster.md) + index — **CHAR-010–012** hồ sơ **`canon`** · human approved 2026-10-23 |
| 4b-n | `T-naming-people-project` *(sync delta)* | **`done (approved)`** | `xianxia-naming-specialist` / orchestrator merge | [`registry.md`](interface/naming/registry.md) — human approved toàn bộ delta 2026-10-23 · index/roster đồng bộ |
| 5 | `T-foreshadow-project` | **`done (approved)`** | `foreshadowing-architect` | [`logic/foreshadowing/00-foreshadow-ledger.md`](logic/foreshadowing/00-foreshadow-ledger.md) — human approved toàn ledger 2026-10-23 · giữ **`FS-TBD-VILLAGE-TRUTH`** treo |
| 6 | `T-audit-plot-project` | **`done (approved)`** | `pro-auditor` | [`logic/audits/audit-plot-project.md`](logic/audits/audit-plot-project.md) — **`approved with waived PW`** · verdict gốc `revise-logic-first` · **PW-01, PW-02, PW-03 waived** for A2 entry (user chấp nhận rủi ro · sửa dần Tier 2 / CP) · human 2026-10-23 |

### A2 — Khởi tạo Arc 1 (sau khi A1 hoàn tất)

| Step | Task ID | State | Owner | Artifact / Ghi chú |
| --- | --- | --- | --- | --- |
| 1 | `T-world-arc-1` | **`done (approved)`** | `world-builder` | Human **`approve T-world-arc-1`** 2026-10-23 · [`00-foundation-handoff.md`](logic/world/00-foundation-handoff.md), [`01-region-active.md`](logic/world/01-region-active.md), [`02-tieu-cuc-index.md`](logic/world/02-tieu-cuc-index.md), [`geo/micro/arc-01-kho-hai-tien-lo.geojson`](logic/world/geo/micro/arc-01-kho-hai-tien-lo.geojson) |
| 1b | `T-naming-places-arc-1` | **`backlog`** *(naming pending · optional parallel)* | `xianxia-naming-specialist` | Pending: **Xích Thạch Lĩnh** (micro) · **Bạch Thổ Thôn** vẫn `[giả định]` — plot có thể dùng tên tạm; không chặn `T-plot-arc-1` |
| 2 | `T-plot-arc-1` | **`done (approved)`** | `plot-architect` | Human **`approve T-plot-arc-1`** 2026-10-23 · [`logic/arcs/01-arc1-beats.md`](logic/arcs/01-arc1-beats.md) (Dual-View · B01–B20 · band 1–18 · **`approved`**) |
| 3 | `T-characters-arc-1` | **`done (approved)`** | `character-architect` | Human **`approve T-characters-arc-1`** 2026-10-23 · [`logic/characters/arc-1-roster.md`](logic/characters/arc-1-roster.md) (**`approved`**) · **naming pending** NPC arc (→ step 3b) |
| 3b | `T-naming-people-arc-1` | `backlog` | `xianxia-naming-specialist` | `interface/naming/registry.md` (NPC khu mỏ / ngoại môn Arc 1) |
| 4 | `T-spine-arc-1` | **`done (approved)`** | `plot-architect` | Human **`approve T-spine-arc-1`** 2026-10-23 · [`logic/chapters/00-chapter-spine-arc-1-kho-hai-tien-lo.md`](logic/chapters/00-chapter-spine-arc-1-kho-hai-tien-lo.md) (**`approved`**) · [`interface/chapters/00-index.md`](interface/chapters/00-index.md) |

### A3 — Prose Arc 1 (sau khi A2 hoàn tất)

| Step | Task ID | State | Owner | Artifact / Ghi chú |
| --- | --- | --- | --- | --- |
| 1 | `T-prose-1` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve T-prose-1`** 2026-10-23 · [`interface/chapters/chapter-01-on-nhat-thach-khe.md`](interface/chapters/chapter-01-on-nhat-thach-khe.md) — Ôn Nhật Thạch Khê · B01 · ~3k từ |
| 2 | `T-review-01` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve T-review-01`** 2026-10-23 · r1 **`suggest_pass`** · ch.1 **`approved`** |
| 3 | `T-prose-2` | **`done (approved)`** | `xianxia-prose-writer` | [`chapter-02-diem-chi-da.md`](interface/chapters/chapter-02-diem-chi-da.md) — *Điểm Chỉ Dạ* · B02+B03 · **re-approved post pivot** 2026-10-23 |
| 4 | `T-review-02` | **`done (approved)`** | `xianxia-chapter-reviewer` | r1 **`suggest_pass`** · ch.2 **`approved`** *(pre-pivot)* · prose pivot human **re-approve** 2026-10-23 |
| 5 | `T-prose-3` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve T-prose-3`** 2026-10-23 · [`chapter-03-doi-dan-ba.md`](interface/chapters/chapter-03-doi-dan-ba.md) — *Dời Dân Bạ* · B04 · **CP-A1-FAMILY-REUNION** |
| 5b | `T-revise-ch2-3-pivot` | **`done (approved)`** | orchestrator / inline | O-S1-09 · ch.2–3 prose khớp **TC-KHTL-A1-VIL** · human 2026-10-23 |
| 6 | `T-review-03` | **`done (approved)`** | `xianxia-chapter-reviewer` | r1 **`suggest_revise`** · [`review-chapter-03-doi-dan-ba.md`](interface/chapter-view/review-chapter-03-doi-dan-ba.md) · C-01→C-03 applied · **`approved`** (auto-gate) |
| 7 | `T-prose-4` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve T-prose-4`** 2026-10-23 · [`chapter-04-thu-thach-ha-khoang.md`](interface/chapters/chapter-04-thu-thach-ha-khoang.md) · *Thử Thạch Hạ Khoáng* · B05 *(revised C-01–C-02)* |
| 8 | `T-review-04` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve T-review-04`** 2026-10-23 · [`review-chapter-04-thu-thach-ha-khoang.md`](interface/chapter-view/review-chapter-04-thu-thach-ha-khoang.md) · r1 fixes C-01–C-02 applied · ch.4 **`approved`** |
| 9 | `T-prose-5` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve 5`** 2026-10-23 · [`interface/chapters/chapter-05-thinh-thach-bac-tuyen.md`](interface/chapters/chapter-05-thinh-thach-bac-tuyen.md) · *Thính Thạch Bắc Tuyến* · B06 *(revised C-01–C-05)* |
| 10 | `T-review-05` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve 5`** 2026-10-23 · [`review-chapter-05-thinh-thach-bac-tuyen.md`](interface/chapter-view/review-chapter-05-thinh-thach-bac-tuyen.md) · r1 fixes C-01→C-05 applied · ch.5 **`approved`** |
| 11 | `T-prose-6` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve 6`** 2026-10-23 · [`interface/chapters/chapter-06-khai-mach-co-da.md`](interface/chapters/chapter-06-khai-mach-co-da.md) · *Khai Mạch Cơ Dạ* · B07 *(revised C-01–C-05)* |
| 12 | `T-review-06` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve 6`** 2026-10-23 · [`review-chapter-06-khai-mach-co-da.md`](interface/chapter-view/review-chapter-06-khai-mach-co-da.md) · r1 fixes C-01→C-05 applied · ch.6 **`approved`** |
| 13 | `T-prose-7` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve 7`** 2026-10-23 · [`interface/chapters/chapter-07-qua-do.md`](interface/chapters/chapter-07-qua-do.md) · *Quá Độ* · B08 *(revised C-01–C-04)* |
| 14 | `T-review-07` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve 7`** 2026-10-23 · [`review-chapter-07-qua-do.md`](interface/chapter-view/review-chapter-07-qua-do.md) · r1 fixes C-01→C-04 applied · ch.7 **`approved`** |
| 15 | `T-prose-8` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve 8`** 2026-10-23 · [`interface/chapters/chapter-08-phe-khoang-hu-xac.md`](interface/chapters/chapter-08-phe-khoang-hu-xac.md) · *Phế Khoáng Hư Xác* · B09 *(revised C-01–C-05)* |
| 16 | `T-review-08` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve 8`** 2026-10-23 · [`review-chapter-08-phe-khoang-hu-xac.md`](interface/chapter-view/review-chapter-08-phe-khoang-hu-xac.md) · r1 fixes C-01→C-05 applied · ch.8 **`approved`** |
| 17 | `T-prose-9` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve 9`** 2026-10-23 · [`interface/chapters/chapter-09-bo-khuyet-khe.md`](interface/chapters/chapter-09-bo-khuyet-khe.md) · *Bổ Khuyết Khê* · B10 *(revised C-01–C-04)* |
| 18 | `T-review-09` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve 9`** 2026-10-23 · [`review-chapter-09-bo-khuyet-khe.md`](interface/chapter-view/review-chapter-09-bo-khuyet-khe.md) · r1 fixes C-01→C-04 applied · ch.9 **`approved`** |
| 19 | `T-prose-10` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve 10`** 2026-10-23 · [`interface/chapters/chapter-10-tuyen-menh.md`](interface/chapters/chapter-10-tuyen-menh.md) · *Tuyển Mệnh* · B11 · ~2,9k–3k từ |
| 20 | `T-review-10` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve 10`** *(waived/approved directly by human)* 2026-10-23 · ch.10 **`approved`** |
| 21 | `T-prose-11` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve 11`** 2026-10-23 · [`interface/chapters/chapter-11-liet-bich-quang-thach.md`](interface/chapters/chapter-11-liet-bich-quang-thach.md) · *Liệt Bích Quang Thạch* · B12 *(revised C-01–C-05)* |
| 22 | `T-review-11` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve 11`** 2026-10-23 · [`review-chapter-11-liet-bich-quang-thach.md`](interface/chapter-view/review-chapter-11-liet-bich-quang-thach.md) · r1 fixes C-01→C-05 applied · ch.11 **`approved`** |
| 23 | `T-prose-12` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve 12`** 2026-10-23 · [`interface/chapters/chapter-12-hau-lan-khich.md`](interface/chapters/chapter-12-hau-lan-khich.md) · *Hậu Lán Khích* · B13 *(revised C-01–C-04)* |
| 24 | `T-review-12` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve 12`** 2026-10-23 · [`review-chapter-12-hau-lan-khich.md`](interface/chapter-view/review-chapter-12-hau-lan-khich.md) · r1 fixes C-01→C-04 applied · ch.12 **`approved`** |
| 25 | `T-prose-13` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve 13`** 2026-10-23 · [`interface/chapters/chapter-13-kiem-khoang.md`](interface/chapters/chapter-13-kiem-khoang.md) · *Kiểm Khoáng* · B14 *(revised C-01–C-04)* |
| 26 | `T-review-13` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve 13`** 2026-10-23 · [`review-chapter-13-kiem-khoang.md`](interface/chapter-view/review-chapter-13-kiem-khoang.md) · r1 fixes C-01→C-04 applied · ch.13 **`approved`** |
| 27 | `T-prose-14` | **`done (approved)`** | `xianxia-prose-writer` | Human **`approve 14`** 2026-10-23 · [`interface/chapters/chapter-14-mai-nhan.md`](interface/chapters/chapter-14-mai-nhan.md) · *Mãi Nhân* · B15 *(revised C-01–C-05)* |
| 28 | `T-review-14` | **`done (approved)`** | `xianxia-chapter-reviewer` | Human **`approve 14`** 2026-10-23 · [`review-chapter-14-mai-nhan.md`](interface/chapter-view/review-chapter-14-mai-nhan.md) · r1 fixes C-01→C-05 applied · ch.14 **`approved`** |
| 29 | `T-prose-15` | **`done (approved)`** | `xianxia-prose-writer` | Auto-gate **`approved`** 2026-10-23 · [`interface/chapters/chapter-15-bat-nhi-ky.md`](interface/chapters/chapter-15-bat-nhi-ky.md) · *Bất Nhị Ký* · B16+B17 *(revised C-01–C-04 · ~3,18k từ)* |
| 30 | `T-review-15` | **`done (approved)`** | `xianxia-chapter-reviewer` | Auto-gate **`approved`** 2026-10-23 · [`review-chapter-15-bat-nhi-ky.md`](interface/chapter-view/review-chapter-15-bat-nhi-ky.md) · C-01→C-04 applied · ch.15 **`approved`** |
| 31 | `T-prose-16` | **`done (approved)`** | `xianxia-prose-writer` | Auto-gate **`approved`** 2026-10-23 · [`interface/chapters/chapter-16-mo-huu-danh.md`](interface/chapters/chapter-16-mo-huu-danh.md) · *Mộ Hữu Danh* · B18 · ~3,16k từ |
| 32 | `T-review-16` | **`done (approved)`** | `xianxia-chapter-reviewer` | Auto-gate **`approved`** 2026-10-23 · [`review-chapter-16-mo-huu-danh.md`](interface/chapter-view/review-chapter-16-mo-huu-danh.md) · r1 **`suggest_pass`** · ch.16 **`approved`** |
| 33 | `T-prose-17` | **`done (approved)`** | `xianxia-prose-writer` | Auto-gate **`approved`** 2026-10-23 · [`interface/chapters/chapter-17-thuong-son-le.md`](interface/chapters/chapter-17-thuong-son-le.md) · *Thượng Sơn Lễ* · B19 · ~3,08k từ |
| 34 | `T-review-17` | **`done (approved)`** | `xianxia-chapter-reviewer` | Auto-gate **`approved`** 2026-10-23 · [`review-chapter-17-thuong-son-le.md`](interface/chapter-view/review-chapter-17-thuong-son-le.md) · r1 **`suggest_pass`** · ch.17 **`approved`** |
| 35 | `T-prose-18` | **`done (approved)`** | `xianxia-prose-writer` | Auto-gate **`approved`** 2026-10-23 · [`interface/chapters/chapter-18-don-but.md`](interface/chapters/chapter-18-don-but.md) · *Đốn Bút* · B20 · ~2,98k từ |
| 36 | `T-review-18` | **`done (approved)`** | `xianxia-chapter-reviewer` | Auto-gate **`approved`** 2026-10-23 · [`review-chapter-18-don-but.md`](interface/chapter-view/review-chapter-18-don-but.md) · r1 **`suggest_pass`** · ch.18 **`approved`** |
| 37 | `T-reader-arc-1` | **`done (approved)`** | `experimental-reader` | [`interface/chapter-view/reader-comment/reader-arc-1-kho-hai-tien-lo.md`](interface/chapter-view/reader-comment/reader-arc-1-kho-hai-tien-lo.md) · End-of-Arc Beta Read (18/18 ch) · 2026-10-23 |
| 38 | `T-char-sync-arc-1` | **`done (approved)`** | `character-architect` | [`logic/characters/phase-01-roster-delta.md`](logic/characters/phase-01-roster-delta.md) · Phase 1 Roster Delta (khép Arc 1 → bàn giao Arc 2) · 2026-10-23 |

### A2 — Khởi tạo Arc 2: Ngoại Môn & Mạch Ngầm Tông Môn (Chương 19–45)

| Step | Task ID | State | Owner | Artifact / Ghi chú |
| --- | --- | --- | --- | --- |
| 1 | `T-world-arc-2` | **`done (approved)`** | `world-builder` | [`logic/world/01-region-active.md`](logic/world/01-region-active.md) §8 · [`02-tieu-cuc-index.md`](logic/world/02-tieu-cuc-index.md) §5–§9 (`MICRO-ARC02-TAY-MACH` / `TC-KHTL-A2`: Ngoại môn, Chấp pháp đường, Vệ Thủy Ngân phủ, Cạn Mạch Thành, Cựu Mạch Hầm) · 2026-10-23 |
| 2 | `T-plot-arc-2` | **`done (approved)`** | `plot-architect` | [`logic/arcs/02-arc2-beats.md`](logic/arcs/02-arc2-beats.md) (Dual-View · B21–B47 · ch.19–45 · khóa `PW-01`, `PW-02`, `PW-04`, `PW-07`) · 2026-10-23 |
| 3 | `T-characters-arc-2` | **`done (approved)`** | `character-architect` | [`logic/characters/arc-2-roster.md`](logic/characters/arc-2-roster.md) (Dual-View · cast Arc 2 + off-screen flags) · 2026-10-23 |
| 4 | `T-spine-arc-2` | **`done (approved)`** | `plot-architect` | [`logic/chapters/00-chapter-spine-arc-2-kho-hai-tien-lo.md`](logic/chapters/00-chapter-spine-arc-2-kho-hai-tien-lo.md) · [`interface/chapters/00-index.md`](interface/chapters/00-index.md) (ch.19–45 `approved`) · 2026-10-23 |

### A3 — Prose Arc 2 (Chương 19–45 · Auto Gate)

| Step | Task ID | State | Owner | Artifact / Ghi chú |
| --- | --- | --- | --- | --- |
| 1 | `T-prose-19..25` & `T-review-19..25` | **`done (approved)`** | `xianxia-prose-writer` + `xianxia-chapter-reviewer` | **Hồi I (Ch.19–25):** [`chapter-19-ngoai-vien-khe.md`](interface/chapters/chapter-19-ngoai-vien-khe.md) → [`chapter-25-ngu-hanh-khuyet-nhat.md`](interface/chapters/chapter-25-ngu-hanh-khuyet-nhat.md) + `review-chapter-19..25-*.md` (`approved` · 2026-10-23) |
| 2 | `T-prose-26..32` & `T-review-26..32` | **`done (approved)`** | `xianxia-prose-writer` + `xianxia-chapter-reviewer` | **Hồi II (Ch.26–32):** [`chapter-26-thanh-moc-tam.md`](interface/chapters/chapter-26-thanh-moc-tam.md) → [`chapter-32-dem-ghep-mach-do.md`](interface/chapters/chapter-32-dem-ghep-mach-do.md) + `review-chapter-26..32-*.md` (`approved` · 2026-10-23) |
| 3 | `T-prose-33..40` & `T-review-33..40` | **`done (approved)`** | `xianxia-prose-writer` + `xianxia-chapter-reviewer` | **Hồi III (Ch.33–40):** [`chapter-33-tinh-that-vo-danh.md`](interface/chapters/chapter-33-tinh-that-vo-danh.md) → [`chapter-40-tro-lao-giu-lo.md`](interface/chapters/chapter-40-tro-lao-giu-lo.md) + `review-chapter-33..40-*.md` (`approved` · 2026-10-23) |
| 4 | `T-prose-41..45` & `T-review-41..45` | **`done (approved)`** | `xianxia-prose-writer` + `xianxia-chapter-reviewer` | **Hồi IV (Ch.41–45):** [`chapter-41-cong-thuy-ngan-phu.md`](interface/chapters/chapter-41-cong-thuy-ngan-phu.md) → [`chapter-45-chuong-mo-bi-canh.md`](interface/chapters/chapter-45-chuong-mo-bi-canh.md) + `review-chapter-41..45-*.md` (`approved` · 2026-10-23) |
| 5 | `T-reader-arc-2` | **`done (approved)`** | `experimental-reader` | [`interface/chapter-view/reader-comment/reader-arc-2-kho-hai-tien-lo.md`](interface/chapter-view/reader-comment/reader-arc-2-kho-hai-tien-lo.md) · End-of-Arc Beta Read (27/27 ch) · 2026-10-23 |
| 6 | `T-char-sync-arc-2` | **`done (approved)`** | `character-architect` | [`logic/characters/phase-02-roster-delta.md`](logic/characters/phase-02-roster-delta.md) · Phase 2 Roster Delta (khép Arc 2 → bàn giao Arc 3) · 2026-10-23 |

**Current task:** **Arc 2 — Ngoại Môn & Mạch Ngầm Tông Môn (`ch.19–45`) ĐÃ KHÉP (`CLOSED / COMPLETE`)**

**A1:** **`complete`** (2026-10-23).

**Arc 1 (A2 + A3 · ch.1–18):** **`CLOSED / COMPLETE`** (2026-10-23).

**Arc 2 (A2 + A3 · ch.19–45):** **`CLOSED / COMPLETE`** (2026-10-23) — toàn bộ **Chương 19 → Chương 45** (`approved`), **`T-reader-arc-2`** (`approved`), **`T-char-sync-arc-2`** (`phase-02-roster-delta.md` `approved`).

**Kế tiếp:** Khi sẵn sàng, mở **Arc 3 — Trúc Cơ Phong Vân & Bí Cảnh Cổ (`ch.46–75`)**: `T-world-arc-3` → `T-plot-arc-3` → `T-characters-arc-3` → `T-spine-arc-3`.

**Naming sync delta:** **Approved** 2026-10-23 — CHAR-010→012 + LOC merged vào registry canon.

---

## Candidate CP/RP

- *(none queued)* — **`CP-A1-FAMILY-REUNION`** **locked in prose** (ch.2–3 approved 2026-10-23); payoff **FS-A1-FAMILY-REUNION** vẫn hoãn.

## Blocked / defer

- **PW-01, PW-02, PW-03** *(audit critical)* — **waived for A2 entry** (2026-10-23): user chấp nhận rủi ro; khóa dần ở **`T-plot-arc-1`** Tier 2 hoặc **CP** sau. PW-04→09 vẫn theo khuyến nghị audit khi Tier 2/plot arc.
