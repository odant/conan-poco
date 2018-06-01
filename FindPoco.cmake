# FindPoco.cmake for POCO Conan Package
# Dmitriy Vetutnev, ODANT 2018


# Include path
find_path(Poco_INCLUDE_DIR
    NAMES Poco/Poco.h
    PATHS ${CONAN_INCLUDE_DIRS_POCO}
    NO_DEFAULT_PATH
)

# Parse version
if(Poco_INCLUDE_DIR AND EXISTS ${Poco_INCLUDE_DIR}/Poco/Version.h)

    file(STRINGS ${Poco_INCLUDE_DIR}/Poco/Version.h DEFINE_POCO_VERSION REGEX "^#define POCO_VERSION +0x[0-9]+..$")

    string(REGEX REPLACE "^.*POCO_VERSION +0x([0-9][0-9]).*$" "\\1" Poco_VERSION_MAJOR ${DEFINE_POCO_VERSION})
    string(REGEX REPLACE "^(0)([0-9])" "\\2" Poco_VERSION_MAJOR ${Poco_VERSION_MAJOR})

    string(REGEX REPLACE "^.*POCO_VERSION +0x[0-9][0-9]([0-9][0-9]).*$" "\\1" Poco_VERSION_MINOR ${DEFINE_POCO_VERSION})
    string(REGEX REPLACE "^(0)([0-9])" "\\2" Poco_VERSION_MINOR ${Poco_VERSION_MINOR})

    string(REGEX REPLACE "^.*POCO_VERSION +0x[0-9][0-9][0-9][0-9]([0-9][0-9]).*$" "\\1" Poco_VERSION_PATCH ${DEFINE_POCO_VERSION})
    string(REGEX REPLACE "^(0)([0-9])" "\\2" Poco_VERSION_PATCH ${Poco_VERSION_PATCH})

    set(Poco_VERSION_STRING "${Poco_VERSION_MAJOR}.${Poco_VERSION_MINOR}.${Poco_VERSION_PATCH}")

    string(REGEX REPLACE "^.*POCO_VERSION +0x[0-9][0-9][0-9][0-9][0-9][0-9](..)$" "\\1" Poco_VERSION_PRERELEASE ${DEFINE_POCO_VERSION})
    if(NOT ${Poco_VERSION_PRERELEASE} STREQUAL "00")
        set(Poco_VERSION_STRING "${Poco_VERSION_STRING}.${Poco_VERSION_PRERELEASE}")
    endif()

    unset(DEFINE_POCO_VERSION)
    mark_as_advanced(Poco_VERSION_MAJOR Poco_VERSION_MINOR Poco_VERSION_TWEAK Poco_VERSION_PRERELEASE)
    mark_as_advanced(Poco_INCLUDE_DIR)

endif()

# Find libaries
find_library(Poco_Foundation_LIBRARY
    NAMES PocoFoundation PocoFoundationd PocoFoundationmd PocoFoundationmdd
    PATHS ${CONAN_LIB_DIRS_POCO}
    NO_DEFAULT_PATH
)

find_library(Poco_Util_LIBRARY
    NAMES PocoUtil PocoUtild PocoUtilmd PocoUtilmdd
    PATHS ${CONAN_LIB_DIRS_POCO}
    NO_DEFAULT_PATH
)

find_library(Poco_Crypto_LIBRARY
    NAMES PocoCrypto PocoCryptod PocoCryptomd PocoCryptomdd
    PATHS ${CONAN_LIB_DIRS_POCO}
    NO_DEFAULT_PATH
)

find_library(Poco_Net_LIBRARY
    NAMES PocoNet PocoNetd PocoNetmd PocoNetmdd
    PATHS ${CONAN_LIB_DIRS_POCO}
    NO_DEFAULT_PATH
)

find_library(Poco_NetSSL_LIBRARY
    NAMES PocoNetSSL PocoNetSSLd PocoNetSSLmd PocoNetSSLmdd
    PATHS ${CONAN_LIB_DIRS_POCO}
    NO_DEFAULT_PATH
)


include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Poco
    REQUIRED_VARS
        Poco_INCLUDE_DIR
        Poco_Foundation_LIBRARY
        Poco_Util_LIBRARY
        Poco_Crypto_LIBRARY
        Poco_Net_LIBRARY
        Poco_NetSSL_LIBRARY
    VERSION_VAR
        Poco_VERSION_STRING
)


if(Poco_FOUND)

    # Set-up variables
    set(Poco_INCLUDE_DIRS ${Poco_INCLUDE_DIR})
    set(Poco_LIBRARIES
        Poco_Foundation_LIBRARY
        Poco_Util_LIBRARY
        Poco_Crypto_LIBRARY
        Poco_Net_LIBRARY
        Poco_NetSSL_LIBRARY
    )
    mark_as_advanced(
        Poco_INCLUDE_DIR
        Poco_Foundation_LIBRARY
        Poco_Util_LIBRARY
        Poco_Crypto_LIBRARY
        Poco_Net_LIBRARY
        Poco_NetSSL_LIBRARY
    )
    set(Poco_DEFINITIONS ${CONAN_COMPILE_DEFINITIONS_POCO}) # Add defines from package_info

    # Imported targets
    include(CMakeFindDependencyMacro)

    if(NOT TARGET Poco::Foundation)

        add_library(Poco::Foundation UNKNOWN IMPORTED)
        set_target_properties(Poco::Foundation PROPERTIES
            INTERFACE_INCLUDE_DIRECTORIES ${Poco_INCLUDE_DIR}
            IMPORTED_LOCATION ${Poco_Foundation_LIBRARY}
            INTERFACE_COMPILE_DEFINITIONS "${Poco_DEFINITIONS}"
        )

        find_dependency(Threads)
        find_dependency(ZLIB)
        find_dependency(PCRE)
        set_property(TARGET Poco::Foundation
            APPEND PROPERTY INTERFACE_LINK_LIBRARIES Threads::Threads ZLIB::ZLIB PCRE::PCRE
        )

        if(WIN32)
            set_property(TARGET Poco::Foundation
                APPEND PROPERTY INTERFACE_LINK_LIBRARIES "iphlpapi"
            )
        endif()

    endif()

    if(NOT TARGET Poco::Util)

        add_library(Poco::Util UNKNOWN IMPORTED)
        set_target_properties(Poco::Util PROPERTIES
            IMPORTED_LOCATION ${Poco_Util_LIBRARY}
            INTERFACE_LINK_LIBRARIES Poco::Foundation
        )

    endif()

    if(NOT TARGET Poco::Crypto)

        add_library(Poco::Crypto UNKNOWN IMPORTED)
        set_target_properties(Poco::Crypto PROPERTIES
            IMPORTED_LOCATION ${Poco_Crypto_LIBRARY}
            INTERFACE_LINK_LIBRARIES Poco::Foundation
        )

        find_dependency(OpenSSL)
        set_property(TARGET Poco::Crypto
            APPEND PROPERTY INTERFACE_LINK_LIBRARIES OpenSSL::SSL
        )

    endif()

    if(NOT TARGET Poco::Net)

        add_library(Poco::Net UNKNOWN IMPORTED)
        set_target_properties(Poco::Net PROPERTIES
            IMPORTED_LOCATION ${Poco_Net_LIBRARY}
            INTERFACE_LINK_LIBRARIES Poco::Foundation
        )

        if(WIN32)
            set_property(TARGET Poco::Net
                APPEND PROPERTY INTERFACE_LINK_LIBRARIES "ws2_32"
            )
        endif()

    endif()

    if(NOT TARGET Poco::NetSSL)

        add_library(Poco::NetSSL UNKNOWN IMPORTED)
        set_target_properties(Poco::NetSSL PROPERTIES
            IMPORTED_LOCATION ${Poco_NetSSL_LIBRARY}
        )

        set_property(TARGET Poco::NetSSL
            APPEND PROPERTY INTERFACE_LINK_LIBRARIES Poco::Net Poco::Util Poco::Crypto
        )

    endif()

endif()
