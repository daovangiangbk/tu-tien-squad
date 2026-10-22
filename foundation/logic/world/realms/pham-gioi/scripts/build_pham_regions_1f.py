#!/usr/bin/env python3
"""Generate region GeoJSON for Hàn Phương · Phù Tảo · Lô Hàng (T-foundation-pham-1f)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "planets" / "bich-lac-tinh" / "geo" / "region"


def slug(region_id: str) -> str:
    return "reg-" + region_id.split("-", 1)[1].lower()


def local(chl_xy, parent_xy):
    return [chl_xy[0] - parent_xy[0], chl_xy[1] - parent_xy[1]]


def fc(region_id, hub_id, parent_file, parent, note, features):
    return {
        "type": "FeatureCollection",
        "world:schema": "tien-hiep-novel/geo/v2",
        "world:scope": "region",
        "world:work_slug": "foundation-canon",
        "world:hub_id": hub_id,
        "world:region_id": region_id,
        "world:parent_scope": "chau_luc",
        "world:parent_feature_id": region_id,
        "world:parent_file": parent_file,
        "world:parent_coordinates": [float(parent[0]), float(parent[1])],
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


def box_area(rid, kind="wilderness", tier="cực_mỏng", w=90, h=70):
    return feat(
        {
            "id": f"{rid}-AREA",
            "name_vi": f"Phạm vi {rid.split('-', 2)[-1].replace('-', ' ')}",
            "kind": kind,
            "visibility": "public",
            "linh_khi_tier": tier,
        },
        poly([[-w, h], [w, h], [w, -h], [-w, -h], [-w, h]]),
    )


def hub_feat(loc_id, name_vi, name_hv, kind="hub", **extra):
    p = {
        "id": loc_id,
        "name_vi": name_vi,
        "name_hv": name_hv,
        "kind": kind,
        "visibility": extra.pop("visibility", "public"),
    }
    p.update(extra)
    return feat(p, pt(0, 0))


def shared(chl, parent, loc_id, name_vi, name_hv, **extra):
    p = {
        "id": loc_id,
        "name_vi": name_vi,
        "name_hv": name_hv,
        "kind": extra.pop("kind", "hub"),
        "visibility": extra.pop("visibility", "public"),
        "notes": f"Shared id; parent chl {chl[loc_id]}.",
    }
    p.update(extra)
    return feat(p, pt(*local(chl[loc_id], parent)))


def route(rid, name_vi, name_hv, coords, **extra):
    p = {
        "id": rid,
        "name_vi": name_vi,
        "name_hv": name_hv,
        "kind": "route",
        "visibility": extra.pop("visibility", "public"),
    }
    p.update(extra)
    return feat(p, line(coords))


def settlement(loc_id, name_vi, name_hv, x, y, **extra):
    p = {
        "id": loc_id,
        "name_vi": name_vi,
        "name_hv": name_hv,
        "kind": "settlement",
        "visibility": "public",
    }
    p.update(extra)
    return feat(p, pt(x, y))


def barrier(bid, name_vi, name_hv, ring):
    return feat(
        {"id": bid, "name_vi": name_vi, "name_hv": name_hv, "kind": "barrier", "visibility": "public"},
        poly(ring),
    )


def build_region(region_id, hub_id, hub_vi, hub_hv, parent_file, parent, chl_shared, note, extras=None):
    feats = [
        box_area(region_id, kind="polity" if "TRAN" in region_id or "TINH" in region_id or "QUAN" in region_id else "wilderness"),
        hub_feat(hub_id, hub_vi, hub_hv),
        settlement(f"LOC-{region_id.split('-', 1)[1]}-TRAM", "Trạm biên · nam", "驿站", -15, -55),
        settlement(f"LOC-{region_id.split('-', 1)[1]}-CANH", "Tháp canh · đông", "望塔", 42, 22),
        barrier(
            f"BRR-{region_id.split('-', 1)[1]}-RIM",
            "Vành địa · rìa",
            "缘障",
            [[-75, 58], [75, 60], [72, 68], [-72, 65], [-75, 58]],
        ),
    ]
    for loc_id, vi, hv in chl_shared:
        feats.append(shared({loc_id: CHL_ALL[loc_id]}, parent, loc_id, vi, hv))
    if extras:
        feats.extend(extras)
    note_full = f"{note} · gốc {hub_id} [0,0]; neo parent ({parent[0]:g},{parent[1]:g}) trên {parent_file.split('/')[-1]}."
    return fc(region_id, hub_id, parent_file, parent, note_full, feats)


CHL_HP = {
    "LOC-HP-HAN-TINH": (430.0, 720.0),
    "LOC-HP-PHONG-MO": (240.0, 620.0),
}
CHL_PT = {
    "LOC-PT-PHU-TRAN": (300.0, 720.0),
    "LOC-PT-KHE-U": (280.0, 560.0),
}
CHL_LH = {
    "LOC-LH-CANG-TIEN": (290.0, 220.0),
    "LOC-LH-THUONG-HOI": (520.0, 380.0),
}
CHL_ALL = {**CHL_HP, **CHL_PT, **CHL_LH}

HP_FILE = "chau-luc/chl-han-phuong.geojson"
PT_FILE = "chau-luc/chl-phu-tao.geojson"
LH_FILE = "chau-luc/chl-lo-hang.geojson"

SPECS = [
    # --- Hàn Phương ---
    ("REG-HP-NAM-CAN", "LOC-HP-NAM-CAN-RIM", "Nam Cạn · rìa ấm", "南旱口", HP_FILE, (435.6, 75.8),
     [("LOC-HP-HAN-TINH", "Hàn Tinh Quan", "寒庭关")], "Vùng Nam Cạn"),
    ("REG-HP-BANG-HA", "LOC-HP-BANG-HA-LO", "Băng Hà · lộ băng", "冰河路", HP_FILE, (447.2, 181.5),
     [("LOC-HP-HAN-TINH", "Hàn Tinh Quan", "寒庭关")], "Vùng Băng Hà"),
    ("REG-HP-NOI-DIA", "LOC-HP-NOI-DIA-HUB", "Nội Địa · đồng bằng", "内地", HP_FILE, (739.3, 152.3),
     [("LOC-HP-HAN-TINH", "Hàn Tinh Quan", "寒庭关")], "Vùng Nội Địa"),
    ("REG-HP-TUYET-LAM", "LOC-HP-TUYET-LAM-TAM", "Tuyết Lâm · trại rừng", "雪林营", HP_FILE, (347.0, 357.3),
     [("LOC-HP-PHONG-MO", "Phong Mộ Cốc", "封墓谷")], "Vùng Tuyết Lâm"),
    ("REG-HP-PHONG-MO", "LOC-HP-PHONG-MO", "Phong Mộ Cốc", "封墓谷", HP_FILE, (240.0, 620.0),
     [("LOC-HP-HAN-TINH", "Hàn Tinh Quan", "寒庭关")], "Vùng Phong Mộ · hook di tích"),
    ("REG-HP-BANG-YUAN", "LOC-HP-BANG-YUAN-MACH", "Băng Nguyên · mạch kiệt", "冰原脉", HP_FILE, (417.5, 669.1),
     [("LOC-HP-HAN-TINH", "Hàn Tinh Quan", "寒庭关")], "Vùng Băng Nguyên · Luyện Thể"),
    ("REG-HP-HAN-TINH", "LOC-HP-HAN-TINH", "Hàn Tinh Quan", "寒庭关", HP_FILE, (430.0, 720.0),
     [("LOC-HP-PHONG-MO", "Phong Mộ Cốc", "封墓谷")], "Vùng Hàn Tinh · phàm quốc hub lục"),
    ("REG-HP-BAC-HUYEN", "LOC-HP-BAC-HUYEN-RIM", "Bắc Huyền · cực bắc", "北玄口", HP_FILE, (592.4, 783.2),
     [("LOC-HP-HAN-TINH", "Hàn Tinh Quan", "寒庭关")], "Vùng Bắc Huyền"),
    ("REG-HP-TAY-PHONG", "LOC-HP-TAY-PHONG-AN", "Tây Phong · ải tây", "西风隘", HP_FILE, (138.2, 326.2),
     [("LOC-HP-PHONG-MO", "Phong Mộ Cốc", "封墓谷")], "Vùng Tây Phong"),
    ("REG-HP-DONG-HUYEN", "LOC-HP-DONG-HUYEN-HUB", "Đông Huyền · trung đông", "东玄", HP_FILE, (446.4, 445.0),
     [("LOC-HP-HAN-TINH", "Hàn Tinh Quan", "寒庭关"), ("LOC-HP-PHONG-MO", "Phong Mộ Cốc", "封墓谷")],
     "Vùng Đông Huyền · mc_phase1"),
    ("BRR-HP-HAN-SON", "LOC-HP-HAN-SON-PASS", "Hàn Sơn · đèo chính", "寒山隘", HP_FILE, (244.9, 341.7),
     [("LOC-HP-PHONG-MO", "Phong Mộ Cốc", "封墓谷")], "Dãy Hàn Sơn · barrier polygon"),
    # --- Phù Tảo ---
    ("REG-PT-NAM-HA", "LOC-PT-NAM-HA-CUA", "Nam Hải · cửa đầm", "南海口", PT_FILE, (610.3, 77.9),
     [("LOC-PT-PHU-TRAN", "Phù Trấn", "浮镇")], "Vùng Nam Hải"),
    ("REG-PT-DAO-LAM", "LOC-PT-DAO-LAM-DAO", "Đảo Lam · trung tâm", "岛林", PT_FILE, (482.4, 187.4),
     [("LOC-PT-PHU-TRAN", "Phù Trấn", "浮镇")], "Vùng Đảo Lam · linh thảo sơ"),
    ("REG-PT-NAM-BINH", "LOC-PT-NAM-BINH-DE", "Nam Bình · đê nam", "南坪", PT_FILE, (771.7, 192.1),
     [("LOC-PT-PHU-TRAN", "Phù Trấn", "浮镇")], "Vùng Nam Bình"),
    ("REG-PT-TRUNG-DAM", "LOC-PT-TRUNG-DAM-TAM", "Trung Đầm · lõi trũng", "中沼心", PT_FILE, (412.2, 373.0),
     [("LOC-PT-KHE-U", "Khe U", "幽谷"), ("LOC-PT-PHU-TRAN", "Phù Trấn", "浮镇")], "Vùng Trung Đầm"),
    ("REG-PT-PHU-TRAN", "LOC-PT-PHU-TRAN", "Phù Trấn · chợ dược", "浮镇", PT_FILE, (300.0, 720.0),
     [("LOC-PT-KHE-U", "Khe U", "幽谷")], "Vùng Phù Trấn · hub lục"),
    ("REG-PT-NGOAI-DAO", "LOC-PT-NGOAI-DAO-BEN", "Ngoại Đảo · bến ngoài", "外岛", PT_FILE, (659.2, 384.9),
     [("LOC-PT-PHU-TRAN", "Phù Trấn", "浮镇")], "Vùng Ngoại Đảo"),
    ("REG-PT-BAC-MANG", "LOC-PT-BAC-MANG-RIM", "Bắc Mang · rìa sậy", "北茫", PT_FILE, (603.4, 834.4),
     [("LOC-PT-PHU-TRAN", "Phù Trấn", "浮镇")], "Vùng Bắc Mang"),
    ("REG-PT-TAY-LAM", "LOC-PT-TAY-LAM-RUNG", "Tây Lâm · rừng đầm", "西林", PT_FILE, (148.3, 408.4),
     [("LOC-PT-KHE-U", "Khe U", "幽谷")], "Vùng Tây Lâm"),
    ("REG-PT-KHE-U", "LOC-PT-KHE-U", "Khe U · sương độc", "幽谷", PT_FILE, (280.0, 560.0),
     [("LOC-PT-PHU-TRAN", "Phù Trấn", "浮镇")], "Vùng Khe U · hook dược quý"),
    ("REG-PT-DONG-U", "LOC-PT-DONG-U-SUONG", "Đông U · sương đông", "东雾", PT_FILE, (483.9, 504.0),
     [("LOC-PT-PHU-TRAN", "Phù Trấn", "浮镇"), ("LOC-PT-KHE-U", "Khe U", "幽谷")], "Vùng Đông U"),
    ("BRR-PT-LOI-DI", "LOC-PT-LOI-DI-PASS", "Lôi Đê · đê khô", "雷堤隘", PT_FILE, (244.7, 340.1),
     [("LOC-PT-KHE-U", "Khe U", "幽谷")], "Dãy Lôi Đê · đê xuyên đầm"),
    # --- Lô Hàng ---
    ("REG-LH-NAM-HAI", "LOC-LH-NAM-HAI-CUA", "Nam Hải · hư không hải", "南海口", LH_FILE, (456.9, 69.8),
     [("LOC-LH-CANG-TIEN", "Cảng Tiên Sa", "仙沙港")], "Vùng Nam Hải"),
    ("REG-LH-CANG-TIEN", "LOC-LH-CANG-TIEN", "Cảng Tiên Sa", "仙沙港", LH_FILE, (290.0, 220.0),
     [("LOC-LH-THUONG-HOI", "Thương hội · trạm", "商会")], "Vùng Cảng Tiên · hub lục · thuế quan"),
    ("REG-LH-TRUNG-DAO", "LOC-LH-TRUNG-DAO-TAM", "Trung Đảo · đảo chính", "中岛", LH_FILE, (332.0, 349.9),
     [("LOC-LH-CANG-TIEN", "Cảng Tiên Sa", "仙沙港"), ("LOC-LH-THUONG-HOI", "Thương hội · trạm", "商会")],
     "Vùng Trung Đảo"),
    ("REG-LH-QUAN-DAO", "LOC-LH-QUAN-DAO-LO", "Quần Đảo · hải tặc", "群岛", LH_FILE, (528.7, 176.6),
     [("LOC-LH-CANG-TIEN", "Cảng Tiên Sa", "仙沙港")], "Vùng Quần Đảo Lô"),
    ("REG-LH-HAI-PHONG", "LOC-LH-HAI-PHONG-AN", "Hải Phong · phong ấn", "海封", LH_FILE, (125.9, 471.9),
     [("LOC-LH-CANG-TIEN", "Cảng Tiên Sa", "仙沙港")], "Vùng Hải Phong · hook phong ấn tu Linh"),
    ("REG-LH-TAY-AN", "LOC-LH-TAY-AN-VUC", "Tây An · hải yên", "西安", LH_FILE, (159.6, 610.8),
     [("LOC-LH-CANG-TIEN", "Cảng Tiên Sa", "仙沙港")], "Vùng Tây An"),
    ("REG-LH-BAC-HAI", "LOC-LH-BAC-HAI-LUU", "Bắc Hải · hành lang bắc", "北海", LH_FILE, (531.8, 496.3),
     [("LOC-LH-CANG-TIEN", "Cảng Tiên Sa", "仙沙港"), ("LOC-LH-THUONG-HOI", "Thương hội · trạm", "商会")],
     "Vùng Bắc Hải · nối Xích Hạ"),
    ("REG-LH-DONG-LUU", "LOC-LH-DONG-LUU-TRAM", "Đông Lưu · trạm neo", "东流", LH_FILE, (688.5, 218.4),
     [("LOC-LH-THUONG-HOI", "Thương hội · trạm", "商会")], "Vùng Đông Lưu · hành lang thương"),
    ("REG-LH-LO-QUAN", "LOC-LH-LO-QUAN-NOI", "Lô Quan · nội cảng", "络关", LH_FILE, (463.5, 719.0),
     [("LOC-LH-CANG-TIEN", "Cảng Tiên Sa", "仙沙港")], "Vùng Lô Quan · hộ thương"),
    ("BRR-LH-LONG-QUY", "LOC-LH-LONG-QUY-PASS", "Long Quy · đèo hải sơn", "龙龟隘", LH_FILE, (289.5, 607.1),
     [("LOC-LH-CANG-TIEN", "Cảng Tiên Sa", "仙沙港")], "Dãy Long Quy · barrier"),
]

# Cross-border rim for LH-BAC-HAI → Xích Hạ (catalog)
LH_BAC_HAI_EXTRA = [
    settlement(
        "LOC-LH-XICH-HA-RIM",
        "Rìa Xích Hạ · hải bắc",
        "赤夏缘",
        95,
        35,
        direction_label="Bắc",
        notes="Cross-link REG-XH-DONG-HAI / hải thương; không micro Xích Hạ trong batch 1f.",
    ),
    route(
        "ROUTE-LH-BAC-XICH",
        "Hành lang hải · Xích Hạ",
        "赤夏海道",
        [[0, 0], [45, 25], [95, 35]],
        from_id="LOC-LH-BAC-HAI-LUU",
        to_id="LOC-LH-XICH-HA-RIM",
        hazard="thuế liên cảng",
        travel_days_walk="5-7",
        visibility="mc_phase1",
    ),
]

REGIONS = {}


def build_brr(spec):
    rid, hub, hvi, hhv, pfile, parent, shared_list, note = spec
    feats = [
        feat(
            {
                "id": f"{rid}-AREA",
                "name_vi": hvi,
                "name_hv": hhv,
                "kind": "barrier",
                "visibility": "public",
                "notes": "Khớp polygon BRR trên chau_luc; một ô phân vùng — không LineString.",
            },
            poly([[-65, 42], [65, 45], [62, -42], [-62, -40], [-65, 42]]),
        ),
        hub_feat(hub, hvi, hhv, kind="settlement", notes="Hub đèo barrier [0,0]."),
        barrier(
            rid,
            hvi,
            hhv,
            [[-50, 28], [50, 30], [48, -28], [-48, -26], [-50, 28]],
        ),
    ]
    for loc_id, vi, hv in shared_list:
        feats.append(shared({loc_id: CHL_ALL[loc_id]}, parent, loc_id, vi, hv))
    note_full = f"{note} · gốc {hub} [0,0]; neo parent ({parent[0]:g},{parent[1]:g}) trên {pfile.split('/')[-1]}."
    return fc(rid, hub, pfile, parent, note_full, feats)


for spec in SPECS:
    rid = spec[0]
    if rid.startswith("BRR-"):
        REGIONS[slug(rid)] = build_brr(spec)
        continue
    hub, hvi, hhv, pfile, parent, shared_list, note = spec[1], spec[2], spec[3], spec[4], spec[5], spec[6], spec[7]
    extras = list(LH_BAC_HAI_EXTRA) if rid == "REG-LH-BAC-HAI" else None
    REGIONS[slug(rid)] = build_region(rid, hub, hvi, hhv, pfile, parent, shared_list, note, extras)

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    counts = {}
    for name, data in sorted(REGIONS.items()):
        path = OUT / f"{name}.geojson"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        counts[name] = len(data["features"])
    print(f"Written {len(counts)} region files")
    for k, v in counts.items():
        print(f"  {k}: {v} features")
