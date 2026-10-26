#!/usr/bin/env python3
"""Loại bỏ ký tự Hán trong tệp văn bản repo — chuyển sang Hán Việt / tiếng Việt."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv"}
TEXT_SUFFIXES = {".md", ".mdc", ".json", ".geojson", ".py", ".txt", ".yml", ".yaml", ".csv"}
HAN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
HAN_ONLY = re.compile(r"^[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\s·•／/、，。：；]+$")

CHAR_HV: dict[str, str] = {
    "Vạn": "Vạn", "Tam": "Tam", "Hạ": "Hạ", "Đông": "Đông", "Trung": "Trung", "Đan": "Đan", "Cửu": "Cửu",
    "Vân": "Vân", "Vong": "Vong", "Giao": "Giao", "Cừu": "Cừu", "Thương": "Thương", "Tiên": "Tiên", "Lệnh": "Lệnh",
    "Hội": "Hội", "Cung": "Cung", "Nguyên": "Nguyên", "Quan": "Quan", "Nội": "Nội", "Băng": "Băng", "Phàm": "Phàm",
    "Sơ": "Sơ", "Chế": "Chế", "Kiếm": "Kiếm", "Câu": "Câu", "Bắc": "Bắc", "Nam": "Nam", "Nguyên": "Nguyên",
    "Phản": "Phản", "Khẩu": "Khẩu", "Cổ": "Cổ", "Đài": "Đài", "Mệnh": "Mệnh", "Thương": "Thương", "Thực": "Thực",
    "Viên": "Viên", "Vi": "Vi", "Quốc": "Quốc", "Địa": "Địa", "Đàn": "Đàn", "Bình": "Bình", "Thành": "Thành",
    "Vực": "Vực", "Đê": "Đê", "Tháp": "Tháp", "Mộ": "Mộ", "Hư": "Hư", "Phục": "Phục", "Hạ": "Hạ", "Ngoại": "Ngoại",
    "Dạ": "Dạ", "Thiên": "Thiên", "Vọng": "Vọng", "Thủ": "Thủ", "An": "An", "Tông": "Tông", "Cung": "Cung",
    "Dung": "Dung", "Tịch": "Tịch", "Mật": "Mật", "Phú": "Phú", "Hàn": "Hàn", "Tự": "Tự", "Phong": "Phong",
    "Trần": "Trần", "Sơn": "Sơn", "Lam": "Lam", "Đảo": "Đảo", "Lĩnh": "Lĩnh", "Ngạn": "Ngạn", "Phong": "Phong",
    "Tuần": "Tuần", "Thị": "Thị", "Đế": "Đế", "Bình": "Bình", "U": "U", "Tự": "Tự", "Khố": "Khố",
    "Đình": "Đình", "Kinh": "Kinh", "Luật": "Luật", "Ngự": "Ngự", "Vi": "Vi", "Tâm": "Tâm", "Vong": "Vong",
    "Đàn": "Đàn", "Chi": "Chi", "Địch": "Địch", "Giáo": "Giáo", "Tản": "Tản", "Phương": "Phương", "Tộc": "Tộc",
    "Nhật": "Nhật", "Hạn": "Hạn", "Minh": "Minh", "Tinh": "Tinh", "Thái": "Thái", "Ám": "Ám", "Bạo": "Bạo",
    "Diệu": "Diệu", "Vọng": "Vọng", "Mộc": "Mộc", "Cực": "Cực", "Lâm": "Lâm", "Giá": "Giá", "Hoành": "Hoành",
    "Tàn": "Tàn", "Điện": "Điện", "Thủy": "Thủy", "Hội": "Hội", "Giang": "Giang", "Trì": "Trì", "Sa": "Sa",
    "Hà": "Hà", "Chiểu": "Chiểu", "Tuyền": "Tuyền", "Pháp": "Pháp", "Lạc": "Lạc", "Châu": "Châu", "Oa": "Oa",
    "Phái": "Phái", "Lưu": "Lưu", "Phù": "Phù", "Hải": "Hải", "Tiêu": "Tiêu", "Hé": "Hé", "Đạm": "Đạm",
    "Uyên": "Uyên", "Độ": "Độ", "Cảng": "Cảng", "Du": "Du", "Hồ": "Hồ", "Nguyên": "Nguyên", "Khê": "Khê",
    "Mạc": "Mạc", "Đàm": "Đàm", "Hỏa": "Hỏa", "Diệt": "Diệt", "Linh": "Linh", "Lô": "Lô", "Viêm": "Viêm",
    "Luyện": "Luyện", "Liệt": "Liệt", "Ngưu": "Ngưu", "Liệp": "Liệp", "Huyền": "Huyền", "Ngọc": "Ngọc", "Hoàn": "Hoàn",
    "Sinh": "Sinh", "Điện": "Điện", "Giới": "Giới", "Đốc": "Đốc", "Thạch": "Thạch", "Bích": "Bích", "Thần": "Thần",
    "Phúc": "Phúc", "Thụ": "Thụ", "Phù": "Phù", "Hồng": "Hồng", "Lạc": "Lạc", "Quần": "Quần", "Mạch": "Mạch",
    "Tích": "Tích", "Tằng": "Tằng", "Hàng": "Hàng", "Tiết": "Tiết", "Hoa": "Hoa", "Viên": "Viên", "Mang": "Mang",
    "Thảo": "Thảo", "Hoang": "Hoang", "Dược": "Dược", "Liên": "Liên", "Mãng": "Mãng", "Phi": "Phi", "Lạc": "Lạc",
    "Lam": "Lam", "Hư": "Hư", "Tây": "Tây", "Ký": "Ký", "Cốc": "Cốc", "Xích": "Xích", "Biên": "Biên",
    "Mê": "Mê", "Tích": "Tích", "Đạo": "Đạo", "Di": "Di", "Diêu": "Diêu", "Bang": "Bang", "Đô": "Đô",
    "Lý": "Lý", "Kim": "Kim", "Rèn": "Rèn", "Trấn": "Trấn", "Môn": "Môn", "Các": "Các", "Dương": "Dương",
    "Tích": "Tích", "Chướng": "Chướng", "Nhan": "Nhan", "Tuyết": "Tuyết", "Lôi": "Lôi", "Vụ": "Vụ", "Thanh": "Thanh",
    "Phong": "Phong", "Dịch": "Dịch", "Cốt": "Cốt", "Hồn": "Hồn", "Ma": "Ma", "Long": "Long", "Quy": "Quy",
    "Lục": "Lục", "Tô": "Tô", "Thiết": "Thiết", "Minh": "Minh", "Hứa": "Hứa", "Trẻ": "Trẻ", "Thâm": "Thâm",
    "Liên": "Liên", "Kỳ": "Kỳ", "Tề": "Tề", "Du": "Du", "Trần": "Trần", "Trương": "Trương", "Giáp": "Giáp",
    "Phan": "Phan", "Phu": "Phu", "Đinh": "Đinh", "Sinh": "Sinh", "Ẩn": "Ẩn", "Thương": "Thương", "Bích": "Bích",
    "Đoạn": "Đoạn", "Ngân": "Ngân", "Minh": "Minh", "Khí": "Khí", "Không": "Không", "Thiên": "Thiên", "Thế": "Thế",
    "Chư": "Chư", "Bí": "Bí", "Cảnh": "Cảnh", "Nghịch": "Nghịch", "Nhi": "Nhi", "Hành": "Hành", "Tự": "Tự",
    "Nhiên": "Nhiên", "Vô": "Vô", "Tình": "Tình", "Hữu": "Hữu", "Cường": "Cường", "Giả": "Giả", "Vi": "Vi",
    "Tôn": "Tôn", "Nhân": "Nhân", "Quả": "Quả", "Luân": "Luân", "Hồi": "Hồi", "Ngũ": "Ngũ", "Âm": "Âm",
    "Dương": "Dương", "Kiếp": "Kiếp", "Tản": "Tản", "Dịch": "Dịch", "Điền": "Điền", "Thể": "Thể", "Trúc": "Trúc",
    "Cơ": "Cơ", "Nguyên": "Nguyên", "Anh": "Anh", "Phi": "Phi", "Thăng": "Thăng", "Hạ": "Hạ", "Bích": "Bích",
    "Mạt": "Mạt", "Phạt": "Phạt", "Chân": "Chân", "Tu": "Tu", "Toái": "Toái", "Dẫn": "Dẫn", "Tiếp": "Tiếp",
    "Bảo": "Bảo", "Niệm": "Niệm", "Mộng": "Mộng", "Phủ": "Phủ", "Sát": "Sát", "Thủ": "Thủ", "Khí": "Khí",
    "Hợp": "Hợp", "Nhãn": "Nhãn", "Trận": "Trận", "Phiên": "Phiên", "Dịch": "Dịch", "Khương": "Khương", "Tồn": "Tồn",
    "Nhất": "Nhất", "Kiệt": "Kiệt", "Chủ": "Chủ", "Mẫu": "Mẫu", "Phái": "Phái", "Thánh": "Thánh", "Nhân": "Nhân",
    "Hồn": "Hồn", "Thẩm": "Thẩm", "Gia": "Gia", "Hộ": "Hộ", "Thu": "Thu", "Cách": "Cách", "Tụ": "Tụ",
    "Bàn": "Bàn", "Hệ": "Hệ", "Tạp": "Tạp", "Lệch": "Lệch", "Hội": "Hội", "Thái": "Thái", "Ất": "Ất",
    "La": "La", "Chí": "Chí", "Thanh": "Thanh", "Phân": "Phân", "Đường": "Đường", "Quyển": "Quyển", "Phiến": "Phiến",
    "Dưỡng": "Dưỡng", "Công": "Công", "Khắc": "Khắc", "Tủy": "Tủy", "Phượng": "Phượng", "Ngưng": "Ngưng", "Lộ": "Lộ",
    "Bình": "Bình", "Kỷ": "Kỷ", "Cá": "Cá", "Hán": "Hán", "Tự": "Tự", "Giá": "Giá", "Thị": "Thị",
    "Đối": "Đối", "Á": "Á", "Châu": "Châu", "Ngữ": "Ngữ", "Ngôn": "Ngôn", "Chi": "Chi", "Trì": "Trì",
    "Đích": "Đích", "Trắc": "Trắc", "Thí": "Thí", "Diện": "Diện", "Mô": "Mô", "Lăng": "Lăng", "Lưỡng": "Lưỡng",
    "Khả": "Khả", "Tưởng": "Tưởng", "Cự": "Cự", "Tuyệt": "Tuyệt", "Thải": "Thải", "Hoặc": "Hoặc", "Nhĩ": "Nhĩ",
    "Hảo": "Hảo", "Thế": "Thế", "Giới": "Giới",
}

TERM_MAP: dict[str, str] = {}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def iter_text_files() -> list[Path]:
    out: list[Path] = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or should_skip(p):
            continue
        if p.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if p.name.endswith(".pyc"):
            continue
        out.append(p)
    return out


def build_term_map_from_repo() -> None:
    pair = re.compile(
        r"\*\*([^*]+?)\*\*\s*\(([\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff0-9\s·•／/、，。：；]+)\)"
    )
    for p in ROOT.rglob("*.md"):
        if should_skip(p):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for m in pair.finditer(text):
            vi = m.group(1).strip()
            inner = m.group(2).strip()
            if not HAN.search(inner):
                continue
            for part in re.split(r"\s*[·•]\s*", inner):
                part = part.strip()
                if part and HAN.search(part) and not re.search(r"[A-Za-z]", part):
                    TERM_MAP.setdefault(part, vi.split("/")[0].split("·")[0].strip())


def han_char_to_hv(ch: str) -> str:
    return CHAR_HV.get(ch, "")


def han_run_to_hv(run: str) -> str:
    if run in TERM_MAP:
        return TERM_MAP[run]
    parts = [han_char_to_hv(c) for c in run]
    if all(parts):
        return " ".join(parts)
    # Ghép liền nếu là tên địa danh ngắn trong name_hv
    joined = "".join(parts)
    if joined:
        return joined
    return ""


def replace_all_han(text: str) -> str:
    def sub_run(m: re.Match[str]) -> str:
        run = m.group(0)
        hv = han_run_to_hv(run)
        return hv if hv else run

    # Cụm dài trước (term map)
    for k in sorted(TERM_MAP, key=len, reverse=True):
        if k in text:
            text = text.replace(k, TERM_MAP[k])
    while HAN.search(text):
        new = HAN.sub(sub_run, text)
        if new == text:
            break
        text = new
    return text


def compact_name_from_vi(name_vi: str) -> str:
    return name_vi.split("·")[0].strip()


def sync_name_hv(props: dict, fallback_name: str | None = None) -> None:
    hv = props.get("name_hv")
    if not isinstance(hv, str) or not HAN.search(hv):
        return
    vi = props.get("name_vi") or fallback_name
    if isinstance(vi, str) and vi.strip():
        props["name_hv"] = compact_name_from_vi(vi)
        return
    converted = han_run_to_hv(hv)
    if converted:
        props["name_hv"] = converted


def process_item_with_name(item: dict) -> None:
    if not isinstance(item, dict):
        return
    props = item.get("properties")
    if isinstance(props, dict):
        sync_name_hv(props, item.get("name") if isinstance(item.get("name"), str) else None)


def process_json_data(data: object) -> None:
    if isinstance(data, dict):
        for key in ("regions", "entities", "features", "nodes", "rivers", "routes"):
            if key in data and isinstance(data[key], list):
                for item in data[key]:
                    if isinstance(item, dict):
                        process_item_with_name(item)
        process_item_with_name(data)
        for v in data.values():
            process_json_data(v)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                process_item_with_name(item)
            process_json_data(item)


def process_markdown(text: str) -> str:
    def drop_han_parens_after_bold(m: re.Match[str]) -> str:
        inner = m.group(2).strip()
        if HAN.search(inner):
            return f"**{m.group(1).strip()}**"
        return m.group(0)

    text = re.sub(
        r"\*\*([^*]+?)\*\*\s*\(([^)]+)\)",
        drop_han_parens_after_bold,
        text,
    )

    def fix_atlas_subtitle(line: str) -> str:
        if "|" not in line or not HAN.search(line):
            return line
        m = re.match(r"^(\| `[^`]+` \| [^·|]+?) · [^|]* \|", line)
        if not m:
            return line
        base = m.group(1)
        name_part = base.split("|", 2)[2].strip()
        if "Tinh hà" in name_part or "tinh hà" in name_part.lower():
            short = name_part.replace("Tinh hà ", "").split("·")[0].strip()
            sub = f"{short} tiên vực" if "TH-TIEN" in line else f"{short} thần vực"
            if "TH-THAN" in line:
                sub = f"{short} thần vực"
            elif "TH-TIEN" in line:
                sub = f"{short} tiên vực"
            else:
                sub = name_part
        elif "`CHL-" in line:
            short = name_part.split("·")[0].strip()
            sub = f"{short} đại lục"
        else:
            sub = name_part
        return re.sub(r"( · )[^|]+(?= \|)", f" · {sub}", line, count=1)

    lines = []
    for line in text.splitlines():
        line = fix_atlas_subtitle(line)
        lines.append(line)
    text = "\n".join(lines)

    text = replace_all_han(text)
    return text


def process_python(text: str) -> str:
    block = re.compile(
        r"\{[^{}]*?['\"]name_vi['\"]\s*:\s*['\"]([^'\"]+)['\"][^{}]*?['\"]name_hv['\"]\s*:\s*['\"]([^'\"]+)['\"][^{}]*?\}",
        re.DOTALL,
    )

    def fix_block(m: re.Match[str]) -> str:
        block_text = m.group(0)
        name_vi = m.group(1)
        if HAN.search(m.group(2)):
            block_text = re.sub(
                r"(['\"])name_hv\1:\s*['\"][^'\"]+['\"]",
                f'"name_hv": "{compact_name_from_vi(name_vi)}"',
                block_text,
                count=1,
            )
        return block_text

    text = block.sub(fix_block, text)
    text = re.sub(
        r"(['\"])name_hv\1:\s*['\"]([^'\"]+)['\"]",
        lambda m: (
            f"{m.group(1)}name_hv{m.group(1)}: {m.group(1)}{han_run_to_hv(m.group(2)) or m.group(2)}{m.group(1)}"
            if HAN.search(m.group(2))
            else m.group(0)
        ),
        text,
    )
    return replace_all_han(text)


def process_file(path: Path, dry_run: bool = False) -> bool:
    suffix = path.suffix.lower()
    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False

    if not HAN.search(raw):
        return False

    if suffix in {".json", ".geojson"} or path.name.endswith(".canvas.json"):
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            new = process_markdown(raw)
        else:
            process_json_data(data)
            new = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    elif suffix == ".py":
        new = process_python(raw)
    else:
        new = process_markdown(raw)

    if new != raw and not dry_run:
        path.write_text(new, encoding="utf-8")
    return new != raw


def count_han() -> tuple[int, int, list[str]]:
    files = 0
    occ = 0
    names: list[str] = []
    for p in iter_text_files():
        try:
            s = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        ms = HAN.findall(s)
        if ms:
            files += 1
            occ += len(ms)
            names.append(str(p.relative_to(ROOT)))
    return files, occ, names


def main() -> int:
    dry = "--dry-run" in sys.argv
    build_term_map_from_repo()
    for _ in range(5):
        changed_any = False
        for p in iter_text_files():
            if process_file(p, dry_run=dry):
                changed_any = True
        if not changed_any:
            break
    f, o, names = count_han()
    print(f"remaining_files={f} remaining_han_chars={o}")
    if names[:10]:
        print("sample:", names[:10])
    return 0 if o == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
