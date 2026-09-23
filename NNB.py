#!/usr/bin/env python3

import sys
import importlib.util
from pathlib import Path

BASE = Path(__file__).resolve().parent

PYTHON_MODULES = {
    (3, 13): "ASAS.so",
    (3, 11): "SASA.so",
}

version = (sys.version_info.major, sys.version_info.minor)

if version not in PYTHON_MODULES:
    print(f"[!] Python {version[0]}.{version[1]} supported nahi hai.")
    print("[!] Supported: Python 3.11 / 3.13")
    sys.exit(1)

so_name = PYTHON_MODULES[version]
so_path = BASE / so_name

if not so_path.exists():
    print(f"[!] {so_name} nahi mili.")
    sys.exit(1)

print(f"[+] Python: {version[0]}.{version[1]}")
print(f"[+] Loading: {so_name}")

spec = importlib.util.spec_from_file_location("AUTO_file", str(so_path))

if spec is None or spec.loader is None:
    print("[!] Module load nahi ho saka.")
    sys.exit(1)

ASAS = importlib.util.module_from_spec(spec)
sys.modules["AUTO_file"] = AUTO_file

try:
    spec.loader.exec_module(AUTO_file)
    print("[✓] Module successfully loaded.")
except Exception as e:
    print(f"[!] Module error: {e}")
    sys.exit(1)

# ==================================================
# Yahan NNB.py ka baqi original code rakho
# ==================================================
