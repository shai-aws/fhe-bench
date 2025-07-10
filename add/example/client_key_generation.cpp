#include "include/utils.h"

using namespace lbcrypto;

int main(){

    // Step 1: Setup CryptoContext
    uint32_t multDepth = 1;
    uint32_t scaleModSize = 50;

    CCParams<CryptoContextCKKSRNS> parameters;
    parameters.SetMultiplicativeDepth(multDepth);
    parameters.SetScalingModSize(scaleModSize);

    CryptoContext<DCRTPoly> cc = GenCryptoContext(parameters);
    cc->Enable(PKE);
    cc->Enable(LEVELEDSHE);

    // Step 2: Key Generation
    auto keys = cc->KeyGen();

    // Step 3: Serialize cryptocontext and keys
    if (!Serial::SerializeToFile("../io/cc.bin", cc,
                                SerType::BINARY) ||
        !Serial::SerializeToFile("../io/pk.bin",
                                keys.publicKey, SerType::BINARY) ||
        !Serial::SerializeToFile("../io/sk.bin",
                                keys.secretKey, SerType::BINARY)) {
        throw std::runtime_error("Failed to write keys to ../io/");
    }
}