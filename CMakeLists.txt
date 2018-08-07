# Dmitriy Vetutnev, ODNAT 2018

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(WIN32)
    add_definitions(
        -D_WIN32_WINNT=0x0600
        -DNTDDI_VERSION=0x06000000
    )
endif()

add_subdirectory(src)
