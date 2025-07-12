## Running the "add two numbers" workload

```console
git clone https://github.com/andreea-alexandru/fhe-bench
cd fhe-bench
./scripts/get-openfhe.sh                     # one-time build
python3 harness/run_submission.py submission
