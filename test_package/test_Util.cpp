// Test for Poco Conan package
// Dmitriy Vetutnev, Odant, 2018


#include <Poco/AutoPtr.h>
#include <Poco/Util/SystemConfiguration.h>


#include <iostream>
#include <cstdlib>


using Poco::AutoPtr;
using Poco::Util::SystemConfiguration;


int main(int, char**) {

    AutoPtr<SystemConfiguration> systemConfig = new SystemConfiguration;

    std::cout << "system.osName: " << systemConfig->getString("system.osName") << std::endl;
    std::cout << "system.osVersion: " << systemConfig->getString("system.osVersion") << std::endl;
    std::cout << "system.osArchitecture: " << systemConfig->getString("system.osArchitecture") << std::endl;
    std::cout << "system.currentDir: " << systemConfig->getString("system.currentDir") << std::endl;
    std::cout << "system.dateTime: " << systemConfig->getString("system.dateTime") << std::endl;
    std::cout << "system.pid: " << systemConfig->getUInt("system.pid") << std::endl;

    return EXIT_SUCCESS;
}
