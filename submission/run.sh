#!/usr/bin/env bash
set -e
DIR=$(dirname "$0")
cd "$DIR"

TEST_CASE="$1"

# clean + recreate IO dir relative to workload
rm -rf ../io && mkdir ../io

# make sure to pass the test cases to all relevant executables
./build/client_key_generation
./build/client_preprocess $TEST_CASE
./build/client_encode_encrypt_db
./build/client_encode_encrypt_query
./build/server_preprocess
./build/server_encrypted_compute
./build/client_decode_decrypt $TEST_CASE
./build/client_postprocess