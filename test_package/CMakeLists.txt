project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()

# CONAN_PKG imported targets
add_executable(test_deflate_CONAN_PKG test_deflate.cpp)
target_link_libraries(test_deflate_CONAN_PKG CONAN_PKG::poco)
set_target_properties(test_deflate_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_deflate_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_deflate_CONAN_PKG
)

