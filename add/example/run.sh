#!/usr/bin/env bash
set -e
DIR=$(dirname "$0")
cd "$DIR"

# clean + recreate IO dir relative to workload
rm -rf ../io && mkdir ../io

./build/client_key_generation
./build/client_preprocess
./build/client_encode_encrypt_db
./build/client_encode_encrypt_query
./build/server_preprocess
./build/server_encrypted_compute
./build/client_decode_decrypt
./build/client_postprocess