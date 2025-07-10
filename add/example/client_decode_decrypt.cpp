#include "include/utils.h"

int main(){
    CryptoContext<DCRTPoly> cc;

    if (!Serial::DeserializeFromFile("../io/cc.bin", cc,
                                    SerType::BINARY)) {
        throw std::runtime_error("Failed to get CryptoContext from ../io/cc.bin");
    }

  PrivateKey<DCRTPoly> sk;
  if (!Serial::DeserializeFromFile("../io/sk.bin", sk,
                                   SerType::BINARY)) {
    throw std::runtime_error("Failed to get secret key from ../io/sk.bin");
  }
    Ciphertext<DCRTPoly> ctxt;     
    Serial::DeserializeFromFile("../io/cipher_sum.bin", ctxt, SerType::BINARY);

    Plaintext ptxt; 
    cc->Decrypt(sk, ctxt, &ptxt);
    ptxt->SetLength(1);
    double res = ptxt->GetCKKSPackedValue()[0].real();

    // No post-processing, so write in the result file.
    std::ofstream("../io/result.txt") << res << '\n';

}