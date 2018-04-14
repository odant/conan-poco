// Test for Poco Conan package
// Dmitriy Vetutnev, Odant, 2018


#include <Poco/Crypto/Cipher.h>
#include <Poco/Crypto/CipherFactory.h>
#include <Poco/Crypto/CipherKey.h>


#include <iostream>
#include <cstdlib>
#include <random>
#include <algorithm>
#include <memory>


using namespace Poco::Crypto;

int main(int, char**) {

    std::string plain;
    plain.resize(4096u, '\0');
    auto rd = []() {
        return static_cast<char>(std::rand());
    };
    std::generate(std::begin(plain), std::end(plain), rd);


    auto& factory = CipherFactory::defaultFactory();
    std::unique_ptr<Cipher> cipher{factory.createCipher(CipherKey("aes-256-cbc"))};


    const std::string encrypted = cipher->encryptString(plain);
    const std::string decrypted = cipher->decryptString(encrypted);

    if (decrypted != plain) {

        std::cout << "Encrypt/decrypt failed, decrypted not equal plain" << std::endl;
        std::exit(EXIT_FAILURE);
    }

    std::cout << "Encrypt/decrypt OK." << std::endl;
    std::cout << "Cipher: " << cipher->name() \
              << ", plain lenght: " << plain.length() \
              << ", encrypted length: " << encrypted.length() \
              << std::endl;


    return EXIT_SUCCESS;
}
