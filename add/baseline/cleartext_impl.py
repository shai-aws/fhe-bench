#!/usr/bin/env python3
"""
Cleartext reference for the “add” workload.

• Reads  datasets    
• Computes a + b 
• Writes the result to expected.txt (# add/baseline/expected.txt)

Run once whenever you change the dataset.
"""

import json
from pathlib import Path

BASELINE_DIR = Path(__file__).resolve().parent        
DATASET_DB_PATH = BASELINE_DIR.parent / "datasets" / "DB.txt"
DATASET_Q_PATH = BASELINE_DIR.parent / "datasets" / "query.txt"
OUT_PATH     = BASELINE_DIR / "expected.txt"

# 1) load dataset
a = float(DATASET_DB_PATH.read_text().strip())
b = float(DATASET_Q_PATH.read_text().strip())

# 2) compute reference result
result = a + b

# 3) write to expected.txt (overwrites if it already exists)
OUT_PATH.write_text(f"{result}\n", encoding="utf-8")
print(f"[baseline] Wrote result to {OUT_PATH.relative_to(Path.cwd())}")