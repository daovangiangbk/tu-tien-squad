#!/usr/bin/env python3
"""Shim → .cursor/skills/geographic-builder/scripts/normalize_chau_luc.py"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

_TARGET = (
    Path(__file__).resolve().parents[2]
    / ".cursor/skills/geographic-builder/scripts/normalize_chau_luc.py"
)
if __name__ == "__main__":
    sys.argv[0] = str(_TARGET)
    runpy.run_path(str(_TARGET), run_name="__main__")
