#!/usr/bin/env python3
"""
verify_result.py - correctness oracle for add-two-ints
  Usage:  python3 verify_result.py  <expected_file>  <result_file>
  Returns exit-code 0 if equal, 1 otherwise.
  Prints a message so the caller can log it.
"""

import sys
from pathlib import Path

if len(sys.argv) != 3:
    sys.exit("Usage: verify_result.py <expected> <result>")

expected_file = Path(sys.argv[1])
result_file   = Path(sys.argv[2])

try:
    exp = float(expected_file.read_text().strip())
    res = float(result_file.read_text().strip())
except Exception as e:
    print(f"[verify] failed to read files: {e}")
    sys.exit(1)

EPS = 1e-5                 # tolerance for doubles
if abs(exp - res) <= EPS:
    print(f"[verify] PASS  (expected={exp}, got={res})")
    sys.exit(0)
else:
    print(f"[verify] FAIL  (expected={exp}, got={res})")
    sys.exit(1)
