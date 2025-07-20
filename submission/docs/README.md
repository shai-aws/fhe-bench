fetch-by-similarity (OpenFHE, CKKS)
--------------------------------------

Edit any of the `client_*` / `server_*` sources under `/submissions`

Example of files produced / consumed. 
-------------------------

| Stage executable            | Reads                              | Writes                            |
|-----------------------------|------------------------------------|-----------------------------------|
| client_preprocess_dataset   |                                    |                                   |
| client_key_generation       |                                    | io/<size>/keys/ subdirectory      |
| client_encode_encrypt_db    | datasets/<size>/, io/<size>/keys/  | io/<size>/encrypted/ subdirectory |
| client_encode_encrypt_query | datasets/<size>/, io/<size>/keys/  | io/<size>/encrypted/query.bin     |
| server_preprocess_dataset   |                                    |                                   |
| server_encrypted_compute    | io/<size>/[...] subdirectories     | io/<size>/encrypted/results.bin   |
| client_decode_decrypt       | io/<size>/encrypted/results.bin    | io/<size>/results-raw.bin         |
| client_postprocess          | io/<size>/results-raw.bin          | io/<size>/result.txt              |

`io/` is deleted and re-created each run, so wire-bytes = total size of all files in that directory.
