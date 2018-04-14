// Test for Poco Conan package
// Dmitriy Vetutnev, Odant, 2018


#include <Poco/RegularExpression.h>


#include <iostream>
#include <cstdlib>


int main(int, char**) {

    Poco::RegularExpression re{"^(POST|GET).*$"};

    if (!re.match("GET /dir/file.html")) {
        std::cout << "Failed re.match(\"GET /dir/file.html\"" << std::endl;
        std::exit(EXIT_FAILURE);
    }


    if (re.match("PUT /dir/file.html")) {
        std::cout << "Failed re.match(\"PUT /dir/file.html\"" << std::endl;
        std::exit(EXIT_FAILURE);
    }

    return EXIT_SUCCESS;
}
