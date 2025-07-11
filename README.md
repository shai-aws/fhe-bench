## Quick start (OpenFHE)

```console
git clone https://github.com/your-org/fhe-bench.git
cd fhe-bench
./scripts/get-openfhe.sh                     # one-time build
      submission/your_submission
# edit *.cpp, params.yml …
python3 harness/run_submission.py \
        submission
# if PASS, push and open PR
