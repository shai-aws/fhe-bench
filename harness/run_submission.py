#!/usr/bin/env python3
import subprocess, pathlib, json, shutil, time, sys, os

TASK_DIR = pathlib.Path(__file__).parents[0]          # .../harness
ROOT     = TASK_DIR.parents[0]                        # repo root
MEASURE_BIN = ROOT/"measure_io/io_size"
MEASURE_SRC = ROOT/"measure_io/io_size.cpp"          

# ---------- build io_size if missing -------------------------------
if not MEASURE_BIN.exists():
    print("[run]  compiling measure_io/io_size …")
    MEASURE_BIN.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["g++", "-std=c++17", "-O2", "-s",
                    "-o", str(MEASURE_BIN), str(MEASURE_SRC)],
                   check=True)

sub_dir  = pathlib.Path(sys.argv[1]).resolve()
build_dir= sub_dir/"build"

# 0. wipe IO dir (co-located with workload for isolation)
io_dir   = TASK_DIR.parent/"io"

shutil.rmtree(io_dir, ignore_errors=True)
io_dir.mkdir()

# 1. build submission
subprocess.run([ROOT/"scripts/build_task.sh", str(sub_dir)], check=True)

# 2. run submission
t0 = time.perf_counter()
subprocess.run([str(sub_dir/"run.sh")], check=True, cwd=sub_dir)
lat = (time.perf_counter()-t0)*1e3

# 3. correctness check via verify_result.py
exp = TASK_DIR.parent/"baseline/expected.txt"
got = TASK_DIR.parent/"io/result.txt"

res = subprocess.run(["python3", TASK_DIR/"verify_result.py", exp, got])
if res.returncode != 0:
    raise RuntimeError("Verification failed; see message above")

# 4. measure latency and bandwidth
bytes_ = int(subprocess.check_output(
                [MEASURE_BIN],
                cwd=TASK_DIR.parent).decode())

json.dump({"latency_ms": lat, "bytes": bytes_},
          open(sub_dir/"results.json","w"))
print("[latency]", lat, "ms", bytes_, "bytes")
