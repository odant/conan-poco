#include <Poco/Environment.h>

#include <iostream>
#include <cstdlib>


int main(int, char**) {
    std::cout << "Poco::Environment::osName(): " << Poco::Environment::osName() << std::endl;
    return EXIT_SUCCESS;
}