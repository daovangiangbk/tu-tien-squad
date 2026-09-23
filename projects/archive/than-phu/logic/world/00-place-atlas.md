# Place atlas — Thần Phù (Logic · naming khung)

> **Trạng thái:** `canon` naming · geo **Arc 1–2 micro done** · 2026-09-17  
> **Registry:** `interface/naming/registry.md` · **Convention:** `foundation/logic/00-geojson-world-map-convention.md` v2

## Tinh hà & châu lục

| ID geo | Tên Việt | Hán | Ghi chú |
| --- | --- | --- | --- |
| `CHL-PHU-VIEN` | Phù Viên đại lục · Hạ Giới | 符元大陆 | Lục địa riêng work `than-phu`; không nhầm Hạ Giới Nam của `tap-linh-dieu-lo`. |
| `LOC-THACH-LAM` | *(hub ref trong geo)* | — | Neo bản đồ; **không** trùng **Thạch Lam Thành** (tác phẩm khác) trong prose — ở đây là hub tọa độ canvas. |

## Vùng & điểm (Arc 1 — Phù Lĩnh)

| ID geo | Tên canon | Arc | Vai trò cốt |
| --- | --- | --- | --- |
| `REG-GIA-TOC-PHU-GIAU` | Địa phận **Thẩm thị · Phù Lĩnh phú** | 1 | Lãnh địa phù gia giàu; linh mạch phù. |
| `LOC-GIA-TOC-HUB` | **Phù Lĩnh Lệnh** | 1 | Trung tâm lệnh; massacre; mật thất **Thần Phù Cổ Phổ**. |
| *(feature)* | **Phù Lĩnh · long mạch phù** | 1 | Nguồn mực / linh sa phù; địa lợi tộc. |
| *(feature)* | **Tây Lam · rừng biên phù gia** | 1 | Đường thoát / truy sát sau biến cố. |
| `REG-BIEN-CUU-DICH` | **Biên cửu địch · áp lực bắc** | 1 | Plant **Hàn Diệp Liên**; quân sứ chưa vào sâu. |
| *(feature)* | **Phù Giang** | 1–2 | Thủy lộ xuống thành; chuyển cảnh Arc 2. |

## Thành & hắc thị (Arc 2 — Thanh Phù)

| ID geo | Tên canon | Arc | Vai trò cốt |
| --- | --- | --- | --- |
| `CHAU-THANH-PHU-VIEN` | Châu thành phù · **Thanh Phù Thành** | 2 | Điều tra **U Huyết Các**; bắt cóc trẻ. |
| `LOC-THANH-PLACEHOLDER` | **Thanh Phù Thành** (青符城) | 2 | ID geo giữ slug cũ; **name_vi** đã canon. |
| `LOC-U-NGO` | **U Ngõ · Thanh Phù** | 2 | Hắc thị; micro [`arc-02-u-ngo.geojson`](geo/micro/arc-02-u-ngo.geojson) · **TC-TP-004**. |

## Nam hoang (Arc 3)

| ID geo | Tên canon | Arc | Vai trò cốt |
| --- | --- | --- | --- |
| `LOC-NAM-HOANG-KHAU` | **Khẩu Nam hoang** · cầu canh | 3 | Rời **Thanh Phù** (ch.75–76); trạm đếm xác · **Nam hoang đạo**. |
| **TC-TP-005** | **Nam hoang · giang hồ Phù Viên** | 3 | Micro [`arc-03-nam-hoang.geojson`](geo/micro/arc-03-nam-hoang.geojson) · **Phù Giang** hạ lưu. |

| Vùng (deferred) | Tên | Ghi chú |
| --- | --- | --- |
| `REG-DONG-HAI` | **Đông Hải dung · cửa biển** | Xuất hải — Phase 2+ stub. |

## Liên kết tổ chức ↔ địa

```text
Thiên Phù Các (đại lục)
    └── Thanh Phù phân điếm @ Thanh Phù Thành
Thẩm thị · Phù Lĩnh (cống hiến lịch sử) ──×── Hàn Diệp Liên (cửu địch, biên bắc)
U Huyết Các (ma) ── che bởi hắc thị / quan hệ xám trong thành
```

## Cập nhật GeoJSON (đã sync 2026-09-17)

- `chl-phu-vien.geojson`: thay placeholder **Thẩm thị / Thanh Phù Thành** trên `name_vi` region + Point.
- **Arc 2 micro:** [`arc-02-thanh-phu-thanh.geojson`](geo/micro/arc-02-thanh-phu-thanh.geojson) (**TC-TP-003**) · [`arc-02-u-ngo.geojson`](geo/micro/arc-02-u-ngo.geojson) (**TC-TP-004**).
- **Arc 3 micro:** [`arc-03-nam-hoang.geojson`](geo/micro/arc-03-nam-hoang.geojson) (**TC-TP-005**).
- **Deferred:** `reg-thanh-phu-vien.geojson` — micro tạm parent `chl-phu-vien`.
