# Test for Poco Conan package
# Dmitriy Vetutnev, Odant, 2018


project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)


include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)


configure_file(key.pem bin/key.pem COPYONLY)
configure_file(certificate.pem bin/certificate.pem COPYONLY)


enable_testing()


# Conan imported targets
add_executable(test_Foundation_deflate_CONAN_PKG test_Foundation_deflate.cpp)
target_link_libraries(test_Foundation_deflate_CONAN_PKG CONAN_PKG::poco)
set_target_properties(test_Foundation_deflate_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Foundation_deflate_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Foundation_deflate_CONAN_PKG
)

add_executable(test_Foundation_environment_CONAN_PKG test_Foundation_environment.cpp)
target_link_libraries(test_Foundation_environment_CONAN_PKG CONAN_PKG::poco)
set_target_properties(test_Foundation_environment_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Foundation_environment_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Foundation_environment_CONAN_PKG
)

add_executable(test_Foundation_regex_CONAN_PKG test_Foundation_regex.cpp)
target_link_libraries(test_Foundation_regex_CONAN_PKG CONAN_PKG::poco)
set_target_properties(test_Foundation_regex_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Foundation_regex_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Foundation_regex_CONAN_PKG
)

add_executable(test_Util_CONAN_PKG test_Util.cpp)
target_link_libraries(test_Util_CONAN_PKG CONAN_PKG::poco)
set_target_properties(test_Util_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Util_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Util_CONAN_PKG
)

add_executable(test_Crypto_CONAN_PKG test_Crypto.cpp)
target_link_libraries(test_Crypto_CONAN_PKG CONAN_PKG::poco)
set_target_properties(test_Crypto_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Crypto_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Crypto_CONAN_PKG
)

add_executable(test_Net_CONAN_PKG test_Net.cpp)
target_link_libraries(test_Net_CONAN_PKG CONAN_PKG::poco)
set_target_properties(test_Net_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Net_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Net_CONAN_PKG
)
set_property(TEST test_Net_CONAN_PKG PROPERTY TIMEOUT 10)

add_executable(test_NetSSL_CONAN_PKG test_NetSSL.cpp)
target_link_libraries(test_NetSSL_CONAN_PKG CONAN_PKG::poco)
set_target_properties(test_NetSSL_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_NetSSL_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_NetSSL_CONAN_PKG
)
set_property(TEST test_NetSSL_CONAN_PKG PROPERTY TIMEOUT 10)


# Poco imported targets
find_package(Poco REQUIRED)
add_executable(test_Foundation_deflate test_Foundation_deflate.cpp)
target_link_libraries(test_Foundation_deflate Poco::Foundation)
set_target_properties(test_Foundation_deflate
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Foundation_deflate
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Foundation_deflate
)

add_executable(test_Foundation_environment test_Foundation_environment.cpp)
target_link_libraries(test_Foundation_environment Poco::Foundation)
set_target_properties(test_Foundation_environment
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Foundation_environment
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Foundation_environment
)

add_executable(test_Foundation_regex test_Foundation_regex.cpp)
target_link_libraries(test_Foundation_regex Poco::Foundation)
set_target_properties(test_Foundation_regex
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Foundation_regex
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Foundation_regex
)

add_executable(test_Util test_Util.cpp)
target_link_libraries(test_Util Poco::Util)
set_target_properties(test_Util
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Util
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Util
)

add_executable(test_Crypto test_Crypto.cpp)
target_link_libraries(test_Crypto Poco::Crypto)
set_target_properties(test_Crypto
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Crypto
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Crypto
)

add_executable(test_Net test_Net.cpp)
target_link_libraries(test_Net Poco::Net)
set_target_properties(test_Net
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_Net
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_Net
)
set_property(TEST test_Net PROPERTY TIMEOUT 10)

add_executable(test_NetSSL test_NetSSL.cpp)
target_link_libraries(test_NetSSL Poco::NetSSL)
set_target_properties(test_NetSSL
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_NetSSL
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_NetSSL
)
set_property(TEST test_NetSSL PROPERTY TIMEOUT 10)

