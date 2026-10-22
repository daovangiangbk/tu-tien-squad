#!/usr/bin/env python3
"""Generate 7 Tàn Mộ region GeoJSON files (T-foundation-pham-1e)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "planets" / "bich-lac-tinh" / "geo" / "region"

# Shared chl coordinates (for cross-region LOC ids)
CHL = {
    "LOC-TM-KHE-GIOI": (76.0, 340.0),
    "LOC-TM-CO-TU": (350.0, 620.0),
    "LOC-TM-OA-TUYEN": (870.0, 560.0),
    "LOC-TM-SA-HAI-CUA": (294.0, 382.0),  # khe local [218,42] + (76,340)
}


def local(chl_xy, parent_xy):
    return [chl_xy[0] - parent_xy[0], chl_xy[1] - parent_xy[1]]


def fc(region_id, hub_id, parent, note, features):
    return {
        "type": "FeatureCollection",
        "world:schema": "tien-hiep-novel/geo/v2",
        "world:scope": "region",
        "world:work_slug": "foundation-canon",
        "world:hub_id": hub_id,
        "world:region_id": region_id,
        "world:parent_scope": "chau_luc",
        "world:parent_feature_id": region_id,
        "world:parent_file": "chau-luc/chl-tan-mo.geojson",
        "world:parent_coordinates": list(parent),
        "world:coordinateNote": note,
        "features": features,
    }


def pt(x, y):
    return {"type": "Point", "coordinates": [x, y]}


def poly(ring):
    return {"type": "Polygon", "coordinates": [ring]}


def line(coords):
    return {"type": "LineString", "coordinates": coords}


def feat(props, geom):
    return {"type": "Feature", "properties": props, "geometry": geom}


REGIONS = {}


def add_region(slug, data):
    REGIONS[slug] = data


# --- REG-TM-NAM-QUAN ---
P = (512.0, 97.0)
add_region(
    "reg-tm-nam-quan",
    fc(
        "REG-TM-NAM-QUAN",
        "LOC-TM-NAM-QUAN",
        P,
        "Vùng Nam Quan · gốc LOC-TM-NAM-QUAN [0,0]; neo parent (512,97) trên chl-tan-mo — centroid REG; ải nam thu phí lữ khách vào Tàn Mộ.",
        [
            feat(
                {
                    "id": "REG-TM-NAM-QUAN-AREA",
                    "name_vi": "Phạm vi Nam Quan",
                    "name_hv": "南关域",
                    "kind": "polity",
                    "visibility": "public",
                    "linh_khi_tier": "cực_mỏng",
                },
                poly(
                    [
                        [-95, 35],
                        [95, 38],
                        [98, 0],
                        [92, -42],
                        [-92, -40],
                        [-95, 35],
                    ]
                ),
            ),
            feat(
                {
                    "id": "LOC-TM-NAM-QUAN",
                    "name_vi": "Nam Quan · ải chính",
                    "name_hv": "南关",
                    "kind": "hub",
                    "visibility": "public",
                    "faction": "Quan ải Tàn Mộ",
                    "notes": "Hub vùng; thu **12–18%** hàng vào sa mạc.",
                },
                pt(0, 0),
            ),
            feat(
                {
                    "id": "LOC-TM-NAM-TRAM",
                    "name_vi": "Trạm lữ · phía nam",
                    "name_hv": "旅站",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Nam",
                },
                pt(-12, -55),
            ),
            feat(
                {
                    "id": "LOC-TM-NAM-THAP",
                    "name_vi": "Tháp canh · đông bắc",
                    "name_hv": "南关塔",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Đông bắc",
                },
                pt(48, 22),
            ),
            feat(
                {
                    "id": "LOC-TM-NAM-GIENG",
                    "name_vi": "Giếng mặn · hiếm",
                    "name_hv": "咸井",
                    "kind": "resource",
                    "visibility": "public",
                    "direction_label": "Tây",
                    "linh_khi_tier": "vô_lin",
                    "notes": "Nước đắt; tranh giành trước khi vào Sa Hải.",
                },
                pt(-58, 8),
            ),
            feat(
                {
                    "id": "BRR-TM-NAM-LO",
                    "name_vi": "Ải lộ · đèo nam",
                    "name_hv": "南隘",
                    "kind": "barrier",
                    "visibility": "public",
                },
                poly([[-75, 30], [-40, 32], [-38, 48], [-72, 45], [-75, 30]]),
            ),
            feat(
                {
                    "id": "LOC-TM-SA-HAI-RIM-S",
                    "name_vi": "Rìa Sa Hải · phía bắc ải",
                    "name_hv": "沙海南缘",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Bắc",
                    "notes": "Biên REG-TM-SA-HAI; nối ROUTE-TM-NAM-SA-HAI.",
                },
                pt(8, 185),
            ),
            feat(
                {
                    "id": "ROUTE-TM-NAM-SA-HAI",
                    "name_vi": "Đạo vào Sa Hải",
                    "name_hv": "入沙海道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-NAM-QUAN",
                    "to_id": "LOC-TM-SA-HAI-RIM-S",
                    "hazard": "nắng; phí ải",
                    "travel_days_walk": "2-3",
                },
                line([[0, 0], [2, 45], [5, 95], [8, 185]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-NAM-NGOAI",
                    "name_vi": "Lộ phía nam · ra khỏi lục",
                    "name_hv": "南外道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-NAM-TRAM",
                    "to_id": "LOC-TM-NAM-QUAN",
                    "hazard": "cướp lữ",
                    "travel_days_walk": "1",
                },
                line([[-12, -55], [-8, -28], [0, 0]]),
            ),
            feat(
                {
                    "id": "LOC-TM-NAM-PHU",
                    "name_vi": "Phụ ải · tây",
                    "name_hv": "西关",
                    "kind": "settlement",
                    "visibility": "mc_phase1",
                    "direction_label": "Tây",
                    "notes": "Lối lách; thu phí riêng — không chính thức.",
                },
                pt(-72, -5),
            ),
            feat(
                {
                    "id": "LOC-TM-NAM-MANH",
                    "name_vi": "Manh mạch · dưới ải",
                    "name_hv": "关下脉",
                    "kind": "resource",
                    "visibility": "hidden_logic",
                    "linh_khi_tier": "manh_mach_rải",
                    "notes": "Gia tộc võ giữ cục bộ; manh mạch rò khí — không chân tu cư trú.",
                },
                pt(18, -22),
            ),
            feat(
                {
                    "id": "RIVER-TM-NAM-CAN",
                    "name_vi": "Khe khô · cố đô nam",
                    "name_hv": "涸溪",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-NAM-GIENG",
                    "to_id": "LOC-TM-SA-HAI-RIM-S",
                    "hazard": "không nước",
                },
                line([[-58, 8], [-25, 55], [8, 120], [8, 185]]),
            ),
            feat(
                {
                    "id": "LOC-TM-NAM-SO",
                    "name_vi": "Sổ ải · kho quan",
                    "name_hv": "关册",
                    "kind": "dungeon",
                    "visibility": "hidden_logic",
                    "notes": "Danh sách tu sĩ qua ải — đồng bộ Khe Giới.",
                },
                pt(32, -18),
            ),
            feat(
                {
                    "id": "ROUTE-TM-NAM-DONG-OA",
                    "name_vi": "Biên đạo đông · tới Oa",
                    "name_hv": "东洼道",
                    "kind": "route",
                    "visibility": "mc_phase1",
                    "from_id": "LOC-TM-NAM-THAP",
                    "to_id": "LOC-TM-OA-TUYEN",
                    "hazard": "cát; thu gom phe",
                    "travel_days_walk": "6-8",
                    "notes": "Shared LOC-TM-OA-TUYEN trên REG-TM-DONG-OA.",
                },
                line(
                    [
                        [48, 22],
                        [120, 85],
                        [200, 180],
                        [358, 463],
                    ]
                ),
            ),
        ],
    ),
)

# --- REG-TM-SA-HAI ---
P = (565.0, 327.0)
add_region(
    "reg-tm-sa-hai",
    fc(
        "REG-TM-SA-HAI",
        "LOC-TM-SA-HAI-TAM",
        P,
        "Vùng Sa Hải · gốc LOC-TM-SA-HAI-TAM [0,0]; neo parent (565,327) centroid REG; shared LOC-TM-SA-HAI-CUA [-271,55] = (294,382) lục; cổ khí vụn · cấm đi bộ một mình.",
        [
            feat(
                {
                    "id": "REG-TM-SA-HAI-AREA",
                    "name_vi": "Phạm vi Sa Hải",
                    "name_hv": "沙海域",
                    "kind": "wilderness",
                    "visibility": "public",
                    "linh_khi_tier": "cực_mỏng",
                    "notes": "Đại sa mạc; SUB-PATCH-MA-TAN-MO rìa tây khi khe dao động.",
                },
                poly(
                    [
                        [-280, 195],
                        [250, 200],
                        [255, -195],
                        [-275, -190],
                        [-280, 195],
                    ]
                ),
            ),
            feat(
                {
                    "id": "LOC-TM-SA-HAI-TAM",
                    "name_vi": "Sa Hải · trung tâm cát",
                    "name_hv": "沙海心",
                    "kind": "hub",
                    "visibility": "public",
                    "notes": "Hub vùng; không có thành — chỉ mốc cát.",
                },
                pt(0, 0),
            ),
            feat(
                {
                    "id": "LOC-TM-SA-HAI-CUA",
                    "name_vi": "Cửa Sa Hải · lối đông",
                    "name_hv": "沙海口",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Đông · mép Khe",
                    "notes": "Shared id; parent (294,382) lục.",
                },
                pt(*local(CHL["LOC-TM-SA-HAI-CUA"], P)),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TU",
                    "name_vi": "Cổ Tu · trung tâm di tích",
                    "name_hv": "古墟",
                    "kind": "hub",
                    "visibility": "public",
                    "direction_label": "Đông bắc",
                    "notes": "Shared id; parent (350,620).",
                },
                pt(*local(CHL["LOC-TM-CO-TU"], P)),
            ),
            feat(
                {
                    "id": "LOC-TM-SA-CO-KHI",
                    "name_vi": "Mỏ cổ khí · dune",
                    "name_hv": "古器丘",
                    "kind": "resource",
                    "visibility": "public",
                    "direction_label": "Tây nam",
                    "notes": "Mảnh đồng vụn; Tàn Tu bang tranh.",
                },
                pt(-120, -85),
            ),
            feat(
                {
                    "id": "LOC-TM-SA-LUU",
                    "name_vi": "Lữ trại đoàn · nam",
                    "name_hv": "商队营",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Nam",
                    "faction": "Thương đội liên minh",
                },
                pt(15, -165),
            ),
            feat(
                {
                    "id": "LOC-TM-SA-MA-RIM",
                    "name_vi": "Rìa Ma uyên · tây",
                    "name_hv": "魔渊缘",
                    "kind": "wilderness",
                    "visibility": "hidden_logic",
                    "direction_label": "Tây",
                    "notes": "SUB-PATCH-MA-TAN-MO; liên Khe/Tây Ma.",
                },
                pt(-245, 12),
            ),
            feat(
                {
                    "id": "BRR-TM-SA-DUNE",
                    "name_vi": "Cồn cát · hố lún",
                    "name_hv": "流沙丘",
                    "kind": "barrier",
                    "visibility": "public",
                },
                poly([[-80, 45], [40, 50], [35, 95], [-85, 90], [-80, 45]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-SA-KHE",
                    "name_vi": "Lối Khe Giới",
                    "name_hv": "界隙道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-SA-HAI-TAM",
                    "to_id": "LOC-TM-SA-HAI-CUA",
                    "hazard": "cát lún",
                    "travel_days_walk": "4-6",
                },
                line([[0, 0], [-85, 22], [-180, 42], [-271, 55]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-SA-CO-TU",
                    "name_vi": "Đạo Cổ Tu",
                    "name_hv": "古墟道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-SA-HAI-TAM",
                    "to_id": "LOC-TM-CO-TU",
                    "hazard": "cướp; phế địa",
                    "travel_days_walk": "3-5",
                },
                line([[0, 0], [-55, 95], [-120, 180], [-215, 293]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-SA-NAM",
                    "name_vi": "Lối Nam Quan",
                    "name_hv": "南关道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-SA-LUU",
                    "to_id": "LOC-TM-NAM-QUAN",
                    "hazard": "phí ải",
                    "travel_days_walk": "2-3",
                    "notes": "Neo LOC-TM-NAM-QUAN trên reg-tm-nam-quan [0,0] → chl (512,97); local tại đích ~[-53,-230].",
                },
                line([[15, -165], [10, -120], [5, -75], [0, -230]]),
            ),
            feat(
                {
                    "id": "LOC-TM-SA-MANH",
                    "name_vi": "Manh mạch cát · ẩn",
                    "name_hv": "沙脉",
                    "kind": "resource",
                    "visibility": "hidden_logic",
                    "linh_khi_tier": "manh_mach_rải",
                },
                pt(88, -35),
            ),
            feat(
                {
                    "id": "LOC-TM-KHE-GIOI",
                    "name_vi": "Khe Giới · cửa vết nứt",
                    "name_hv": "界隙",
                    "kind": "hub",
                    "visibility": "hidden_logic",
                    "direction_label": "Tây · qua cửa",
                    "notes": "Shared id; parent (76,340).",
                },
                pt(*local(CHL["LOC-TM-KHE-GIOI"], P)),
            ),
            feat(
                {
                    "id": "RIVER-TM-SA-CAN",
                    "name_vi": "Rãnh cổ · khô",
                    "name_hv": "古涸",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-SA-CO-KHI",
                    "to_id": "LOC-TM-SA-HAI-TAM",
                    "hazard": "ma phù",
                },
                line([[-120, -85], [-65, -42], [0, 0]]),
            ),
        ],
    ),
)

# --- REG-TM-TAY-MA ---
P = (177.0, 588.0)
add_region(
    "reg-tm-tay-ma",
    fc(
        "REG-TM-TAY-MA",
        "LOC-TM-MA-UUYEN",
        P,
        "Vùng Tây Ma · gốc LOC-TM-MA-UUYEN [0,0]; neo parent (177,588) centroid REG; E-PHAM-MA-PATCH · SUB-PATCH-MA-TAN-MO; shared LOC-TM-KHE-GIOI [-101,-248].",
        [
            feat(
                {
                    "id": "REG-TM-TAY-MA-AREA",
                    "name_vi": "Phạm vi Tây Ma",
                    "name_hv": "西魔域",
                    "kind": "wilderness",
                    "visibility": "hidden_logic",
                    "linh_khi_tier": "ma_khi_vệt",
                    "notes": "Vệt Ma khí; không Ma Giới đầy đủ (06-subsidiary-realms).",
                },
                poly([[-42, 28], [38, 30], [40, -32], [-40, -30], [-42, 28]]),
            ),
            feat(
                {
                    "id": "LOC-TM-MA-UUYEN",
                    "name_vi": "Ma Uyên · lõi vệt",
                    "name_hv": "魔渊",
                    "kind": "hub",
                    "visibility": "hidden_logic",
                    "notes": "Hub vùng; SUB-PATCH-MA-TAN-MO.",
                },
                pt(0, 0),
            ),
            feat(
                {
                    "id": "LOC-TM-MA-PHONG",
                    "name_vi": "Phong ấn · đá nứt",
                    "name_hv": "魔封",
                    "kind": "dungeon",
                    "visibility": "hidden_logic",
                    "direction_label": "Trung tâm",
                },
                pt(5, 8),
            ),
            feat(
                {
                    "id": "LOC-TM-MA-CANH",
                    "name_vi": "Trạm canh · nam",
                    "name_hv": "魔哨",
                    "kind": "settlement",
                    "visibility": "public",
                    "faction": "Quan ải Tàn Mộ",
                    "notes": "Canh khi ma khí tăng; liên Khe.",
                },
                pt(-8, -22),
            ),
            feat(
                {
                    "id": "LOC-TM-KHE-GIOI",
                    "name_vi": "Khe Giới · cửa vết nứt",
                    "name_hv": "界隙",
                    "kind": "hub",
                    "visibility": "hidden_logic",
                    "notes": "Shared id; parent (76,340).",
                },
                pt(*local(CHL["LOC-TM-KHE-GIOI"], P)),
            ),
            feat(
                {
                    "id": "LOC-TM-MA-VET-LINK",
                    "name_vi": "Vệt Ma · sát khe",
                    "name_hv": "魔迹",
                    "kind": "wilderness",
                    "visibility": "hidden_logic",
                    "notes": "Neo logic LOC-TM-MA-VET trên Khe Giới; cùng patch.",
                },
                pt(-28, -185),
            ),
            feat(
                {
                    "id": "BRR-TM-MA-BICH",
                    "name_vi": "Bích đá · tây",
                    "name_hv": "魔壁",
                    "kind": "barrier",
                    "visibility": "public",
                },
                poly([[-38, 18], [-32, 18], [-30, -18], [-36, -18], [-38, 18]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-TAY-KHE",
                    "name_vi": "Biên đạo Khe Giới",
                    "name_hv": "界隙魔道",
                    "kind": "route",
                    "visibility": "hidden_logic",
                    "from_id": "LOC-TM-MA-UUYEN",
                    "to_id": "LOC-TM-KHE-GIOI",
                    "hazard": "ma khí; không lộ trình quan",
                    "travel_days_walk": "2-3",
                },
                line([[0, 0], [-35, -95], [-75, -175], [-101, -248]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-TAY-CO-TU",
                    "name_vi": "Rìa Cổ Tu",
                    "name_hv": "古墟魔缘",
                    "kind": "route",
                    "visibility": "hidden_logic",
                    "from_id": "LOC-TM-MA-UUYEN",
                    "to_id": "LOC-TM-CO-TU",
                    "hazard": "ma + cát",
                    "travel_days_walk": "4-5",
                },
                line([[0, 0], [45, 18], [95, 28], [173, 32]]),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TU",
                    "name_vi": "Cổ Tu · trung tâm di tích",
                    "name_hv": "古墟",
                    "kind": "hub",
                    "visibility": "public",
                    "notes": "Shared id; parent (350,620).",
                },
                pt(*local(CHL["LOC-TM-CO-TU"], P)),
            ),
            feat(
                {
                    "id": "LOC-TM-MA-DAN",
                    "name_vi": "Mỏ ma sa · lộ",
                    "name_hv": "魔砂",
                    "kind": "resource",
                    "visibility": "hidden_logic",
                    "notes": "Ma tu thu gom — Thiên oán.",
                },
                pt(22, -8),
            ),
            feat(
                {
                    "id": "LOC-TM-MA-TU",
                    "name_vi": "Am tu · tàn dư",
                    "name_hv": "魔庵",
                    "kind": "settlement",
                    "visibility": "hidden_logic",
                    "faction": "Ma tu lẻ",
                },
                pt(-18, 12),
            ),
            feat(
                {
                    "id": "RIVER-TM-MA-CAN",
                    "name_vi": "Khe khô · rìa ma",
                    "name_hv": "魔涸",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-MA-CANH",
                    "to_id": "LOC-TM-MA-VET-LINK",
                    "hazard": "ma khí",
                },
                line([[-8, -22], [-15, -85], [-28, -185]]),
            ),
            feat(
                {
                    "id": "LOC-TM-SA-HAI-RIM-W",
                    "name_vi": "Rìa Sa Hải · tây",
                    "name_hv": "沙海西缘",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Đông",
                },
                pt(388, -256),
            ),
            feat(
                {
                    "id": "ROUTE-TM-TAY-SA",
                    "name_vi": "Biên Sa Hải",
                    "name_hv": "沙海魔界",
                    "kind": "route",
                    "visibility": "mc_phase1",
                    "from_id": "LOC-TM-MA-UUYEN",
                    "to_id": "LOC-TM-SA-HAI-RIM-W",
                    "hazard": "cát + ma",
                    "travel_days_walk": "3-4",
                },
                line([[0, 0], [120, -85], [250, -180], [388, -256]]),
            ),
        ],
    ),
)

# --- REG-TM-BAC-HAN ---
P = (512.0, 614.0)
add_region(
    "reg-tm-bac-han",
    fc(
        "REG-TM-BAC-HAN",
        "LOC-TM-BAC-HAN-RIM",
        P,
        "Vùng Bắc Hạn · gốc LOC-TM-BAC-HAN-RIM [0,0]; neo parent (512,614) centroid REG; rìa bắc lạnh · linh khí cực mỏng.",
        [
            feat(
                {
                    "id": "REG-TM-BAC-HAN-AREA",
                    "name_vi": "Phạm vi Bắc Hạn",
                    "name_hv": "北旱域",
                    "kind": "wilderness",
                    "visibility": "public",
                    "linh_khi_tier": "cực_mỏng",
                },
                poly([[-235, 105], [260, 108], [258, -102], [-238, -100], [-235, 105]]),
            ),
            feat(
                {
                    "id": "LOC-TM-BAC-HAN-RIM",
                    "name_vi": "Rìa Bắc Hạn · cửa nam",
                    "name_hv": "北旱口",
                    "kind": "hub",
                    "visibility": "public",
                    "notes": "Hub vùng; lối xuống Cổ Tu / Hạn Cốc.",
                },
                pt(0, 0),
            ),
            feat(
                {
                    "id": "LOC-TM-BAC-TRAM",
                    "name_vi": "Trạm gió · bắc",
                    "name_hv": "风站",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Bắc",
                },
                pt(12, 75),
            ),
            feat(
                {
                    "id": "LOC-TM-BAC-CO",
                    "name_vi": "Cổ tháp · đông",
                    "name_hv": "北塔",
                    "kind": "dungeon",
                    "visibility": "public",
                    "direction_label": "Đông",
                },
                pt(95, 35),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TU",
                    "name_vi": "Cổ Tu · trung tâm di tích",
                    "name_hv": "古墟",
                    "kind": "hub",
                    "visibility": "public",
                    "notes": "Shared id; parent (350,620).",
                },
                pt(*local(CHL["LOC-TM-CO-TU"], P)),
            ),
            feat(
                {
                    "id": "LOC-TM-HAN-COC-MOUTH",
                    "name_vi": "Cửa Hạn Cốc · tây",
                    "name_hv": "旱谷口",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Tây",
                    "notes": "Biên REG-TM-HAN-COC.",
                },
                pt(0, -76),
            ),
            feat(
                {
                    "id": "BRR-TM-BAC-GIO",
                    "name_vi": "Vành gió · bắc",
                    "name_hv": "北风环",
                    "kind": "barrier",
                    "visibility": "public",
                },
                poly([[-180, 85], [180, 88], [175, 102], [-175, 98], [-180, 85]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-BAC-CO-TU",
                    "name_vi": "Đạo Cổ Tu",
                    "name_hv": "北墟道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-BAC-HAN-RIM",
                    "to_id": "LOC-TM-CO-TU",
                    "hazard": "gió; lạnh đêm",
                    "travel_days_walk": "2-3",
                },
                line([[0, 0], [-45, 5], [-162, 6]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-BAC-HAN-COC",
                    "name_vi": "Lối Hạn Cốc",
                    "name_hv": "旱谷道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-BAC-HAN-RIM",
                    "to_id": "LOC-TM-HAN-COC-MOUTH",
                    "hazard": "khô",
                    "travel_days_walk": "1-2",
                },
                line([[0, 0], [-28, -42], [0, -76]]),
            ),
            feat(
                {
                    "id": "LOC-TM-OA-TUYEN",
                    "name_vi": "Oa Tuyền · giếng đông",
                    "name_hv": "洼泉",
                    "kind": "hub",
                    "visibility": "public",
                    "direction_label": "Đông",
                    "notes": "Shared id; parent (870,560).",
                },
                pt(*local(CHL["LOC-TM-OA-TUYEN"], P)),
            ),
            feat(
                {
                    "id": "ROUTE-TM-BAC-DONG-OA",
                    "name_vi": "Biên đạo Oa Tuyền",
                    "name_hv": "洼泉北道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-BAC-CO",
                    "to_id": "LOC-TM-OA-TUYEN",
                    "hazard": "cát gió",
                    "travel_days_walk": "3-4",
                },
                line([[95, 35], [180, 15], [280, -8], [358, -54]]),
            ),
            feat(
                {
                    "id": "LOC-TM-BAC-MANH",
                    "name_vi": "Manh mạch · đá lạnh",
                    "name_hv": "寒脉",
                    "kind": "resource",
                    "visibility": "hidden_logic",
                    "linh_khi_tier": "manh_mach_rải",
                },
                pt(-45, 42),
            ),
            feat(
                {
                    "id": "LOC-TM-BAC-PHU",
                    "name_vi": "Phế trại · tây bắc",
                    "name_hv": "北废营",
                    "kind": "settlement",
                    "visibility": "mc_phase1",
                    "direction_label": "Tây bắc",
                },
                pt(-165, 55),
            ),
            feat(
                {
                    "id": "RIVER-TM-BAC-CAN",
                    "name_vi": "Rãnh băng khô",
                    "name_hv": "涸冰",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-BAC-TRAM",
                    "to_id": "LOC-TM-BAC-PHU",
                    "hazard": "lạnh",
                },
                line([[12, 75], [-45, 68], [-165, 55]]),
            ),
        ],
    ),
)

# --- REG-TM-DONG-OA ---
P = (870.0, 560.0)
add_region(
    "reg-tm-dong-oa",
    fc(
        "REG-TM-DONG-OA",
        "LOC-TM-OA-TUYEN",
        P,
        "Vùng Đông Oa · gốc LOC-TM-OA-TUYEN [0,0]; neo parent (870,560) trên chl-tan-mo; ốc đảo · phe thu gom cổ khí.",
        [
            feat(
                {
                    "id": "REG-TM-DONG-OA-AREA",
                    "name_vi": "Phạm vi Đông Oa",
                    "name_hv": "东洼域",
                    "kind": "polity",
                    "visibility": "public",
                    "linh_khi_tier": "cực_mỏng",
                    "notes": "Ốc đảo quanh giếng; thu gom mạnh.",
                },
                poly([[-112, 95], [105, 98], [108, -92], [-110, -90], [-112, 95]]),
            ),
            feat(
                {
                    "id": "LOC-TM-OA-TUYEN",
                    "name_vi": "Oa Tuyền · giếng đông",
                    "name_hv": "洼泉",
                    "kind": "hub",
                    "visibility": "public",
                    "notes": "Hub vùng; nước hiếm — thu phí.",
                },
                pt(0, 0),
            ),
            feat(
                {
                    "id": "LOC-TM-OA-CHOD",
                    "name_vi": "Chợ Oa · thu gom",
                    "name_hv": "洼市",
                    "kind": "settlement",
                    "visibility": "public",
                    "faction": "Liên bang thu gom",
                    "notes": "Hoa hồng **20–30%** cổ khí.",
                },
                pt(28, -18),
            ),
            feat(
                {
                    "id": "LOC-TM-OA-KHO",
                    "name_vi": "Kho đông · phe",
                    "name_hv": "洼库",
                    "kind": "resource",
                    "visibility": "mc_phase1",
                    "direction_label": "Đông",
                },
                pt(72, 12),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TA-RIM",
                    "name_vi": "Rìa Cổ Ta · nam",
                    "name_hv": "古塔缘",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Nam",
                    "notes": "Biên REG-TM-CO-TA.",
                },
                pt(7, -122),
            ),
            feat(
                {
                    "id": "LOC-TM-BAC-HAN-RIM",
                    "name_vi": "Rìa Bắc Hạn · cửa nam",
                    "name_hv": "北旱口",
                    "kind": "hub",
                    "visibility": "public",
                    "direction_label": "Tây bắc",
                    "notes": "Shared hub id reg-tm-bac-han; parent (512,614).",
                },
                pt(*local((512.0, 614.0), P)),
            ),
            feat(
                {
                    "id": "BRR-TM-OA-CAT",
                    "name_vi": "Vành cát · đông",
                    "name_hv": "东沙环",
                    "kind": "barrier",
                    "visibility": "public",
                },
                poly([[85, -45], [102, -42], [100, 55], [82, 52], [85, -45]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-OA-CO-TA",
                    "name_vi": "Lối Cổ Ta",
                    "name_hv": "古塔道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-OA-TUYEN",
                    "to_id": "LOC-TM-CO-TA-RIM",
                    "hazard": "cát",
                    "travel_days_walk": "2",
                },
                line([[0, 0], [5, -55], [7, -122]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-OA-BAC",
                    "name_vi": "Đạo Bắc Hạn",
                    "name_hv": "北旱洼道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-OA-TUYEN",
                    "to_id": "LOC-TM-BAC-HAN-RIM",
                    "hazard": "gió",
                    "travel_days_walk": "3-4",
                },
                line([[0, 0], [-120, 22], [-240, 42], [-358, 54]]),
            ),
            feat(
                {
                    "id": "LOC-TM-OA-MANH",
                    "name_vi": "Manh mạch · dưới giếng",
                    "name_hv": "泉脉",
                    "kind": "resource",
                    "visibility": "hidden_logic",
                    "linh_khi_tier": "manh_mach_rải",
                },
                pt(-8, -5),
            ),
            feat(
                {
                    "id": "LOC-TM-OA-HAI",
                    "name_vi": "Mép đông · biển cát",
                    "name_hv": "东漠",
                    "kind": "wilderness",
                    "visibility": "public",
                    "direction_label": "Đông",
                },
                pt(95, 5),
            ),
            feat(
                {
                    "id": "RIVER-TM-OA-LUU",
                    "name_vi": "Oa lưu · cố đô khô",
                    "name_hv": "洼流",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-OA-TUYEN",
                    "to_id": "LOC-TM-OA-CHOD",
                    "hazard": "thu phí",
                    "notes": "Neo RIVER-TM-OA-LUU trên chl.",
                },
                line([[0, 0], [12, -8], [28, -18]]),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TU",
                    "name_vi": "Cổ Tu · trung tâm di tích",
                    "name_hv": "古墟",
                    "kind": "hub",
                    "visibility": "public",
                    "notes": "Shared id; parent (350,620).",
                },
                pt(*local(CHL["LOC-TM-CO-TU"], P)),
            ),
            feat(
                {
                    "id": "ROUTE-TM-OA-CO-TU",
                    "name_vi": "Đường vòng Cổ Tu",
                    "name_hv": "古墟洼道",
                    "kind": "route",
                    "visibility": "mc_phase1",
                    "from_id": "LOC-TM-OA-TUYEN",
                    "to_id": "LOC-TM-CO-TU",
                    "hazard": "phế địa",
                    "travel_days_walk": "4-5",
                },
                line([[0, 0], [-85, 35], [-200, 55], [-520, 60]]),
            ),
            feat(
                {
                    "id": "LOC-TM-OA-AN",
                    "name_vi": "Hầm thu · ẩn",
                    "name_hv": "洼暗仓",
                    "kind": "dungeon",
                    "visibility": "hidden_logic",
                    "notes": "Cổ khí không qua chợ.",
                },
                pt(-35, 25),
            ),
        ],
    ),
)

# --- REG-TM-CO-TA ---
P = (877.0, 438.0)
add_region(
    "reg-tm-co-ta",
    fc(
        "REG-TM-CO-TA",
        "LOC-TM-CO-TA-TAP",
        P,
        "Vùng Cổ Ta · gốc LOC-TM-CO-TA-TAP [0,0]; neo parent (877,438) centroid REG; phế tháp lang thang · shared LOC-TM-OA-TUYEN [-7,122].",
        [
            feat(
                {
                    "id": "REG-TM-CO-TA-AREA",
                    "name_vi": "Phạm vi Cổ Ta",
                    "name_hv": "古塔域",
                    "kind": "wilderness",
                    "visibility": "public",
                    "linh_khi_tier": "cực_mỏng",
                },
                poly([[-85, 82], [92, 85], [95, -78], [-88, -75], [-85, 82]]),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TA-TAP",
                    "name_vi": "Cổ Ta · trại tháp",
                    "name_hv": "古塔营",
                    "kind": "hub",
                    "visibility": "public",
                    "notes": "Hub vùng; tháp đổ xếp hàng.",
                },
                pt(0, 0),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TA-1",
                    "name_vi": "Tháp một · nghiêng",
                    "name_hv": "古塔一",
                    "kind": "dungeon",
                    "visibility": "public",
                    "direction_label": "Bắc",
                },
                pt(-22, 38),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TA-2",
                    "name_vi": "Tháp hai · vỡ nửa",
                    "name_hv": "古塔二",
                    "kind": "dungeon",
                    "visibility": "public",
                    "direction_label": "Đông",
                },
                pt(35, 18),
            ),
            feat(
                {
                    "id": "LOC-TM-OA-TUYEN",
                    "name_vi": "Oa Tuyền · giếng đông",
                    "name_hv": "洼泉",
                    "kind": "hub",
                    "visibility": "public",
                    "direction_label": "Bắc",
                    "notes": "Shared id; parent (870,560).",
                },
                pt(*local(CHL["LOC-TM-OA-TUYEN"], P)),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TU",
                    "name_vi": "Cổ Tu · trung tâm di tích",
                    "name_hv": "古墟",
                    "kind": "hub",
                    "visibility": "public",
                    "notes": "Shared id; parent (350,620).",
                },
                pt(*local(CHL["LOC-TM-CO-TU"], P)),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TA-KHI",
                    "name_vi": "Đống cổ khí · nam",
                    "name_hv": "塔器堆",
                    "kind": "resource",
                    "visibility": "public",
                    "direction_label": "Nam",
                },
                pt(8, -48),
            ),
            feat(
                {
                    "id": "BRR-TM-CO-TA-VO",
                    "name_vi": "Tường tháp · vòng",
                    "name_hv": "塔墙",
                    "kind": "barrier",
                    "visibility": "public",
                },
                poly([[-55, 55], [55, 58], [52, 68], [-52, 65], [-55, 55]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-CO-TA-OA",
                    "name_vi": "Lối Oa Tuyền",
                    "name_hv": "洼泉塔道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-CO-TA-TAP",
                    "to_id": "LOC-TM-OA-TUYEN",
                    "hazard": "cát",
                    "travel_days_walk": "2",
                },
                line([[0, 0], [-4, 55], [-7, 122]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-CO-TA-CO-TU",
                    "name_vi": "Đạo Cổ Tu",
                    "name_hv": "古墟塔道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-CO-TA-TAP",
                    "to_id": "LOC-TM-CO-TU",
                    "hazard": "lang thang đao khách",
                    "travel_days_walk": "3-4",
                },
                line([[0, 0], [-120, 95], [-280, 165], [-527, 182]]),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TA-LUU",
                    "name_vi": "Lữ khách · tây",
                    "name_hv": "塔旅",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Tây",
                },
                pt(-58, -12),
            ),
            feat(
                {
                    "id": "LOC-TM-SA-HAI-RIM-E",
                    "name_vi": "Rìa Sa Hải · đông",
                    "name_hv": "沙海东缘",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Tây nam",
                },
                pt(-312, -111),
            ),
            feat(
                {
                    "id": "ROUTE-TM-CO-TA-SA",
                    "name_vi": "Biên Sa Hải",
                    "name_hv": "沙海塔道",
                    "kind": "route",
                    "visibility": "mc_phase1",
                    "from_id": "LOC-TM-CO-TA-TAP",
                    "to_id": "LOC-TM-SA-HAI-RIM-E",
                    "hazard": "cát lún",
                    "travel_days_walk": "5-6",
                },
                line([[0, 0], [-95, -45], [-210, -85], [-312, -111]]),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TA-MANH",
                    "name_vi": "Manh mạch · tháp gãy",
                    "name_hv": "塔脉",
                    "kind": "resource",
                    "visibility": "hidden_logic",
                    "linh_khi_tier": "manh_mach_rải",
                },
                pt(15, 42),
            ),
            feat(
                {
                    "id": "RIVER-TM-CO-TA-CAN",
                    "name_vi": "Rãnh khô · giữa tháp",
                    "name_hv": "塔涸",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-CO-TA-1",
                    "to_id": "LOC-TM-CO-TA-2",
                    "hazard": "đá rơi",
                },
                line([[-22, 38], [5, 28], [35, 18]]),
            ),
        ],
    ),
)

# --- REG-TM-HAN-COC ---
P = (411.0, 526.0)
add_region(
    "reg-tm-han-coc",
    fc(
        "REG-TM-HAN-COC",
        "LOC-TM-HAN-COC-DHE",
        P,
        "Vùng Hạn Cốc · gốc LOC-TM-HAN-COC-DHE [0,0]; neo parent (411,526) centroid REG; cốc khô vô lin · nối Bắc Hạn / Cổ Tu.",
        [
            feat(
                {
                    "id": "REG-TM-HAN-COC-AREA",
                    "name_vi": "Phạm vi Hạn Cốc",
                    "name_hv": "旱谷域",
                    "kind": "wilderness",
                    "visibility": "public",
                    "linh_khi_tier": "vô_lin",
                    "notes": "Khớp chl-tan-mo; không nuôi tu.",
                },
                poly([[-121, 62], [128, 65], [125, -58], [-118, -55], [-121, 62]]),
            ),
            feat(
                {
                    "id": "LOC-TM-HAN-COC-DHE",
                    "name_vi": "Hạn Cốc · đáy khô",
                    "name_hv": "旱谷底",
                    "kind": "hub",
                    "visibility": "public",
                    "notes": "Hub vùng; gió nóng ban ngày.",
                },
                pt(0, 0),
            ),
            feat(
                {
                    "id": "LOC-TM-HAN-COC-MOUTH",
                    "name_vi": "Cửa Hạn Cốc · đông",
                    "name_hv": "旱谷口",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Đông",
                    "notes": "Shared id; parent chl (512,538) qua parent (411,526)+local.",
                },
                pt(101, 12),
            ),
            feat(
                {
                    "id": "LOC-TM-CO-TU",
                    "name_vi": "Cổ Tu · trung tâm di tích",
                    "name_hv": "古墟",
                    "kind": "hub",
                    "visibility": "public",
                    "notes": "Shared id; parent (350,620).",
                },
                pt(*local(CHL["LOC-TM-CO-TU"], P)),
            ),
            feat(
                {
                    "id": "LOC-TM-BAC-HAN-RIM",
                    "name_vi": "Rìa Bắc Hạn · cửa nam",
                    "name_hv": "北旱口",
                    "kind": "hub",
                    "visibility": "public",
                    "direction_label": "Bắc",
                    "notes": "Shared id; parent (512,614).",
                },
                pt(*local((512.0, 614.0), P)),
            ),
            feat(
                {
                    "id": "BRR-TM-HAN-Than",
                    "name_vi": "Vách cốc · hai bên",
                    "name_hv": "谷壁",
                    "kind": "barrier",
                    "visibility": "public",
                },
                poly([[-115, 45], [-105, 45], [-102, -40], [-112, -38], [-115, 45]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-HAN-CO-TU",
                    "name_vi": "Lối lên Cổ Tu",
                    "name_hv": "谷墟道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-HAN-COC-DHE",
                    "to_id": "LOC-TM-CO-TU",
                    "hazard": "nắng; vô lin",
                    "travel_days_walk": "1-2",
                },
                line([[0, 0], [-25, 45], [-61, 94]]),
            ),
            feat(
                {
                    "id": "ROUTE-TM-HAN-BAC",
                    "name_vi": "Lối Bắc Hạn",
                    "name_hv": "谷北道",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-HAN-COC-DHE",
                    "to_id": "LOC-TM-BAC-HAN-RIM",
                    "hazard": "gió cốc",
                    "travel_days_walk": "1",
                },
                line([[0, 0], [45, 42], [101, 88]]),
            ),
            feat(
                {
                    "id": "LOC-TM-HAN-XAC",
                    "name_vi": "Xác cát · phế",
                    "name_hv": "谷骸",
                    "kind": "dungeon",
                    "visibility": "mc_phase1",
                    "direction_label": "Tây",
                },
                pt(-75, -8),
            ),
            feat(
                {
                    "id": "LOC-TM-HAN-TRAM",
                    "name_vi": "Trạm nước · nam (hết)",
                    "name_hv": "谷站",
                    "kind": "settlement",
                    "visibility": "public",
                    "direction_label": "Nam",
                },
                pt(5, -52),
            ),
            feat(
                {
                    "id": "LOC-TM-KHE-GIOI",
                    "name_vi": "Khe Giới · cửa vết nứt",
                    "name_hv": "界隙",
                    "kind": "hub",
                    "visibility": "hidden_logic",
                    "notes": "Shared id; parent (76,340).",
                },
                pt(*local(CHL["LOC-TM-KHE-GIOI"], P)),
            ),
            feat(
                {
                    "id": "ROUTE-TM-HAN-KHE",
                    "name_vi": "Đường vòng Khe",
                    "name_hv": "谷界道",
                    "kind": "route",
                    "visibility": "hidden_logic",
                    "from_id": "LOC-TM-HAN-COC-DHE",
                    "to_id": "LOC-TM-KHE-GIOI",
                    "hazard": "vô lin; giám sát",
                    "travel_days_walk": "4-5",
                },
                line([[0, 0], [-120, -85], [-250, -145], [-335, -186]]),
            ),
            feat(
                {
                    "id": "LOC-TM-HAN-CO",
                    "name_vi": "Cổ mộ khô · đáy",
                    "name_hv": "谷墓",
                    "kind": "resource",
                    "visibility": "hidden_logic",
                    "notes": "Cổ khí không linh — chỉ vật lý.",
                },
                pt(-18, -28),
            ),
            feat(
                {
                    "id": "RIVER-TM-HAN-CAN",
                    "name_vi": "Rãnh cốc · khô",
                    "name_hv": "谷涸",
                    "kind": "route",
                    "visibility": "public",
                    "from_id": "LOC-TM-HAN-COC-MOUTH",
                    "to_id": "LOC-TM-HAN-COC-DHE",
                    "hazard": "nắng",
                },
                line([[101, 12], [55, 8], [0, 0]]),
            ),
            feat(
                {
                    "id": "LOC-TM-OA-TUYEN",
                    "name_vi": "Oa Tuyền · giếng đông",
                    "name_hv": "洼泉",
                    "kind": "hub",
                    "visibility": "public",
                    "direction_label": "Đông nam",
                    "notes": "Shared id; parent (870,560).",
                },
                pt(*local(CHL["LOC-TM-OA-TUYEN"], P)),
            ),
        ],
    ),
)

# Fix typo in HAN-COC barrier id
for f in REGIONS["reg-tm-han-coc"]["features"]:
    if f["properties"].get("id") == "BRR-TM-HAN-Than":
        f["properties"]["id"] = "BRR-TM-HAN-VACH"

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    counts = {}
    for slug, data in REGIONS.items():
        path = OUT / f"{slug}.geojson"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        counts[slug] = len(data["features"])
    print("Written:", counts)
