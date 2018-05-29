# FindPoco.cmake for POCO Conan Package
# Dmitriy Vetutnev, ODANT 2018


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


include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Poco
    REQUIRED_VARS Poco_INCLUDE_DIR
    VERSION_VAR Poco_VERSION_STRING
)

