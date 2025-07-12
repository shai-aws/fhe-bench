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

# 0. Generate queries for all test cases and the expected results
baseline_py = ROOT / "baseline" / "cleartext_impl.py"
subprocess.run(["python3", baseline_py], check=True)

# 1. Build submission
subprocess.run([ROOT/"scripts/build_task.sh", str(sub_dir)], check=True)

# For each test case, run the submission overwriting the intermediate files
test_cases = ["small", "medium", "large"]
for test in test_cases:
    print("\nTest case: ", test)

    # 2. Wipe IO dir (co-located with workload for isolation)
    io_dir   = TASK_DIR.parent/"io"

    shutil.rmtree(io_dir, ignore_errors=True)
    io_dir.mkdir()

    # 3. Run submission
    t0 = time.perf_counter()
    subprocess.run([str(sub_dir/"run.sh"), test], check=True, cwd=sub_dir)
    lat = (time.perf_counter()-t0)*1e3

    # 4. Correctness check via verify_result.py
    exp = TASK_DIR.parent / "baseline" / f"expected_{test}.txt"
    got = TASK_DIR.parent / "io" / f"result_{test}.txt"

    res = subprocess.run(["python3", TASK_DIR/"verify_result.py", exp, got])
    if res.returncode != 0:
        raise RuntimeError("Verification failed; see message above")

    # 5. Measure latency and bandwidth
    bytes_ = int(subprocess.check_output(
                    [MEASURE_BIN],
                    cwd=TASK_DIR.parent).decode())

    json.dump({"latency_ms": lat, "bytes": bytes_},
            open(sub_dir/f"results_{test}.json","w"))
    print("[latency]", lat, "ms", bytes_, "bytes")
