## Quick start (OpenFHE)

```console
git clone https://github.com/your-org/fhe-bench.git
cd fhe-bench
./scripts/get-openfhe.sh                     # one-time build
cp -r add/example \
      add/submissions/<you>/add-openfhe
# edit *.cpp, params.yml …
python3 add/harness/run_submission.py \
        add/submissions/<you>/add-openfhe
# if PASS, push and open PR
