#include "utils.h"

int main(){
    CryptoContext<DCRTPoly> cc;

    if (!Serial::DeserializeFromFile("../io/cc.bin", cc,
                                    SerType::BINARY)) {
        throw std::runtime_error("Failed to get CryptoContext from ../io/cc.bin");
    }

    Ciphertext<DCRTPoly> ctxt_db, ctxt_q;
    Serial::DeserializeFromFile("../io/cipher_db.bin", ctxt_db, SerType::BINARY);
    Serial::DeserializeFromFile("../io/cipher_q.bin", ctxt_q, SerType::BINARY);

    auto ctxtSum = cc->EvalAdd(ctxt_db, ctxt_q);
    Serial::SerializeToFile("../io/cipher_sum.bin", ctxtSum, SerType::BINARY);
}