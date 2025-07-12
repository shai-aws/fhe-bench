Example – add (OpenFHE, CKKS)
--------------------------------------

Edit any of the `client_*` / `server_*` sources in
`/submissions`

Example of files produced / consumed. 
client_preprocess and client_decode_decrypt take as argument the test case name.
-------------------------

| Stage executable                | Reads                               | Writes                     |
|---------------------------------|-------------------------------------|----------------------------|
| client_key_generation           | params.yml                          | io/cc.bin pk.bin sk.bin    |
| client_preprocess               | datasets/add.json                   | io/plain_db.bin plain_q.bin |
| client_encode_encrypt_db        | plain_db.bin cc.bin pk.bin          | io/cipher_db.bin            |
| client_encode_encrypt_query     | plain_q.bin cc.bin pk.bin           | io/cipher_q.bin            |
| server_preprocess               | datasets/add.json                   | io/db.bin                  |
| server_encrypted_compute        | cipher_db.bin cipher_q.bin cc.bin   | io/cipher_sum.bin          |
| client_decode_decrypt           | cipher_sum.bin cc.bin sk.bin        | io/plain_sum.bin           |
| client_postprocess              | plain_sum.bin                       | io/result.txt              |

`io/` is deleted and re-created each run, so wire-bytes = total size of
all files in that directory.
