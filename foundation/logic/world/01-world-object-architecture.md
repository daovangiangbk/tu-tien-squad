# Kiến trúc đối tượng thế giới

> Quy ước chính thức cho hồ sơ kiến thế. Bốn giới Phàm · Linh · Tiên · Thần là các giới diện vật chất song song thuộc **Nhân Giới**, không phải bốn vũ trụ riêng.

## 1. Hai hệ phân tầng song hành

```text
realm → planet/system → continent → region → site → micro
giới      tinh cầu/       châu lục    khu vực   điểm      tiểu cục
          tinh hệ
```

Đây là **phân tầng logic** của hồ sơ. Nó không thay schema hay hình học GeoJSON hiện hành.

| Tầng logic | Cách biểu diễn |
| --- | --- |
| `realm` | Thư mục, atlas và chỉ mục domain của giới; không nhất thiết là polygon và không sở hữu geometry đã thuộc một planet. |
| `planet/system` | Hồ sơ logic bọc atlas `geo/00-tinh-ha.geojson`. Planet active sở hữu thư mục `geo/` của chính nó. Với Phàm/Linh, atlas cũ là không gian bản đồ quanh **một tinh cầu chính**; mọi `CHL-*` đang vẽ là châu lục trên tinh cầu ấy, tuyệt đối không diễn giải sáu châu lục thành sáu tinh cầu. |
| `continent` | Tiếp tục dùng `geo/chau-luc/*.geojson` và ID `CHL-*` hiện có. |
| `region` | Tiếp tục dùng `geo/region/*.geojson`. |
| `site` | Hồ sơ logic cho thành, trấn, tông môn, giáo phái hoặc địa điểm có chức năng tương đương; nằm giữa region và micro. Chỉ cần Point hoặc feature trong region/micro, không bắt buộc thêm scope GeoJSON. Phe không có lãnh thổ có thể chỉ có hồ sơ logic. |
| `micro` | Tiếp tục dùng `geo/micro/*.geojson`; là tiểu cục phục vụ arc/cảnh. |

Chuỗi scope GeoJSON cũ `tinh_ha → chau_luc → region → micro` vẫn nguyên vẹn. `tinh_ha` là tên scope bản đồ tương thích, có thể biểu đạt quần vực quanh tinh cầu chính hoặc quần tinh; nó không thay thế tầng logic `planet/system`.

## 2. Metadata chuẩn

Mỗi đối tượng có khối metadata:

```yaml
---
id: OBJ-ON-DINH
type: realm | planet | system | continent | region | site | micro
parent_id: ID-CHA
parent_path: ../duong-dan-ho-so-cha.md
scope: active | deferred
status: draft | active | locked | deprecated
visibility: public | mc_phase1 | hidden_logic
canon_source:
  - ../../duong-dan-nguon.md
child_index:
  - id: ID-CON
    path: ../duong-dan-con.md
---
```

- `id` ổn định; không thay ID atlas cũ.
- `parent_id` và `parent_path` bắt buộc trừ đối tượng gốc.
- `scope` nói mức đầu tư hồ sơ; `status` nói vòng đời canon.
- `canon_source` dẫn tới luật, atlas hoặc catalog làm nguồn.
- `child_index` là danh mục con trực tiếp; đối tượng chưa có con dùng `[]`.

## 3. Sáu miền mô tả bắt buộc

Mỗi đối tượng active có sáu miền đúng tên:

1. `geo`: thế giới vật lý, vị trí, ranh giới và đường nối.
2. `power-system`: sức mạnh, tu luyện, kỹ nghệ và giới hạn vận hành.
3. `bio`: chủng tộc, sinh linh, sinh thái.
4. `social`: xã hội, văn hóa, tổ chức và quan hệ cộng đồng.
5. `history`: lịch sử, truyền thuyết và dấu tích còn hiệu lực.
6. `economy`: tài nguyên, trao đổi, chính trị và luật thực thi.

Mỗi miền chỉ có **5–10 gạch đầu dòng cấp cao**, kèm nguồn, trạng thái, `parent` và `children`. Không viết bách khoa toàn thư. Chi tiết chỉ được mở khi arc cần.

**Khung điền mẫu (5 tầng tu tiên → sáu miền):** [`_templates/README.md`](_templates/README.md) và [`_templates/object/`](_templates/object/README.md).

## 4. Quy tắc liên kết xuống

- Realm link tới planet hoặc system.
- Planet link tới continent.
- Continent link tới region.
- Region link tới site.
- Site link tới micro.
- Cha chỉ tóm tắt con trong 1–2 dòng rồi dẫn link; không sao chép nội dung của con lên cha.
- Mỗi hồ sơ con phải dẫn ngược về cha. `child_index` và liên kết trong nội dung phải thống nhất.

## 5. Chính sách theo giới

### Phàm Giới

- Chỉ **Bích Lạc Tinh** là tinh cầu chính active và được mô tả sâu — **một tinh cầu = toàn bộ Phàm Giới** trong hồ sơ Logic hiện tại.
- `TH-PHAM-BICH-LAC` là ID bản đồ/quần vực cũ bọc tinh cầu này.
- **Sáu miền** (geo, power-system, bio, social, history, economy) nằm tại `realms/pham-gioi/planets/bich-lac-tinh/` — **không** nhân đôi ở cấp `realms/pham-gioi/<miền>/`.
- Realm `pham-gioi/` chỉ giữ **00-object-index**, **00-world-atlas**, **01-region-catalog**, **02-tieu-cuc-index**, **scripts/**.
- Không tạo tinh cầu thứ hai nếu chưa có điểm kiểm soát hoặc user duyệt.

### Linh Giới

- Chỉ **Càn Nguyên Tinh** là tinh cầu chính active và được mô tả sâu.
- `TH-LINH-CAN-NGUYEN` là ID bản đồ/quần vực cũ bọc tinh cầu này.
- Path chuẩn của geometry tinh cầu là `realms/linh-gioi/planets/can-nguyen-tinh/geo/`; realm không sở hữu geometry đã thuộc planet.
- Các “tinh hà láng giềng” cũ là quần vực deferred hoặc dữ liệu nền; không tự chuyển thành tinh cầu có hồ sơ chi tiết.

### Tiên Giới và Thần Giới

- Tổ chức theo realm rồi tinh hệ/quần tinh; atlas `TH-TIEN-*` và `TH-THAN-*` là mô tả bao quát.
- Chỉ tạo hồ sơ planet khi arc thực sự đi tới; chỉ tạo châu lục của planet theo nhu cầu.
- Atlas hiện hữu được giữ tại realm/system như bản đồ quy ước của quần vực chủ; chỉ tách sang `planets/<planet>/geo/` khi planet được instantiate theo nhu cầu, không khởi tạo hàng loạt.

## 6. Hồ sơ đầy đủ và hồ sơ chờ

- Realm active và planet active: có đủ sáu thư mục miền, index con và nguồn.
- System active: có đủ sáu miền khi trở thành bàn cờ chính; system chỉ làm mục lục có thể giữ hồ sơ bao quát.
- Continent, region, site hoặc micro active: tạo đủ sáu miền khi cần quản trị xuyên miền.
- Đối tượng deferred: chỉ cần `00-overview.md`, metadata và liên kết con đã biết; không tạo sáu file rỗng.
- Không tạo hàng loạt scaffold cho Tiên/Thần để “đủ cây”.

## 7. Tương thích và chuyển đổi dữ liệu hiện tại

| Dữ liệu hiện tại | Diễn giải logic mới | Hành động |
| --- | --- | --- |
| `realms/<giới>/` | `realm` | Giữ nguyên; bổ sung index và sáu miền. |
| `realms/<giới>/planets/<planet>/geo/00-tinh-ha.geojson` Phàm/Linh | Bản đồ legacy quanh một planet chính | Giữ tên, ID và hình học; planet sở hữu atlas. |
| `TH-PHAM-BICH-LAC` | Parent map của Bích Lạc Tinh | Không đổi ID; không coi là một vũ trụ. |
| `TH-LINH-CAN-NGUYEN` | Parent map của Càn Nguyên Tinh | Không đổi ID; các `CHL-*` là châu lục của Càn Nguyên Tinh. |
| `TH-TIEN-*`, `TH-THAN-*` | Tinh hệ/quần tinh ở mức bao quát | Gắn vào system index; planet sinh theo nhu cầu. |
| `planets/<planet>/geo/chau-luc/*.geojson` | `continent` | Giữ nguyên file, ID, hình học và neo. |
| `planets/<planet>/geo/region/*.geojson` | `region` | Giữ nguyên file, ID, hình học và neo. |
| Thành/trấn/tông môn/giáo phái hiện có | `site` | Dùng feature/Point sẵn có hoặc hồ sơ logic; không thêm scope. |
| `planets/<planet>/geo/micro/*.geojson` | `micro` | Giữ nguyên schema và chuỗi neo. |

Mọi chuyển đổi là **lớp liên kết bọc ngoài**. Khi relocation được duyệt, chỉ đổi owner/path; không đổi tên file, ID, hình học, PNG hoặc canvas hiện hữu.
