#include "include/utils.h"

int main(){
    CryptoContext<DCRTPoly> cc;

    if (!Serial::DeserializeFromFile("../io/cc.bin", cc,
                                    SerType::BINARY)) {
        throw std::runtime_error("Failed to get CryptoContext from ../io/cc.bin");
    }
    PublicKey<DCRTPoly> pk;
    if (!Serial::DeserializeFromFile("../io/pk.bin", pk,
                                    SerType::BINARY)) {
        throw std::runtime_error("Failed to get public key from ../io/pk.bin");
    }

    double x; 
    std::ifstream("../io/plain_q.bin",std::ios::binary).read((char*)&x, sizeof(double));
    std::vector<double> query = {x};
    auto ptxt = cc->MakeCKKSPackedPlaintext(query);
    auto ctxt = cc->Encrypt(pk, ptxt);

    Serial::SerializeToFile("../io/cipher_q.bin", ctxt, SerType::BINARY);
}