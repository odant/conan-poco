# Test for Poco Conan package
# Dmitriy Vetutnev, Odant, 2018


project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)


include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)


enable_testing()


# CONAN_PKG imported targets

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

