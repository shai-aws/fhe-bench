#include "openfhe.h"
// header files needed for de/serialization
#include "ciphertext-ser.h"
#include "cryptocontext-ser.h"
#include "key/key-ser.h"
#include "scheme/ckksrns/ckksrns-ser.h"

using namespace lbcrypto;


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

    return 0;
}