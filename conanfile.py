from conans import ConanFile, CMake


class PocoConan(ConanFile):
    name = "poco"
    version = "1.8.1"
    license = "Boost Software License Version 1.0. https://pocoproject.org/license.html"
    description = "Modern, powerful open source C++ class libraries for building network- and internet-based applications that run on desktop, server, mobile and embedded systems."
    url = "https://github.com/odant/conan-poco"
    settings = {
        "os": ["Windows", "Linux"],
        "compiler": ["Visual Studio", "gcc"],
        "build_type": ["Debug", "Release"],
        "arch": ["x86_64", "x86"]
    }
    generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt"
    no_copy_source = True
    build_policy = "missing"

    def configure(self):
        # Only C++11
        if self.settings.compiler.get_safe("libcxx") == "libstdc++":
            raise Exception("This package is only compatible with libstdc++11")

    def requirements(self):
        self.requires("zlib/[~=1.2.11]@%s/stable" % self.user)
        self.requires("openssl/[~=1.1.0g]@%s/testing" % self.user)

    def build(self):
        cmake = CMake(self)
        #
        cmake.definitions["CMAKE_INSTALL_PREFIX:STRING"] = self.package_folder.replace("\\", "/")
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE:BOOL"] = "ON"
        #cmake.definitions["BUILD_SHARED_LIBS:BOOL"] = "OFF"
        #
        cmake.definitions["ENABLE_CPPUNIT:BOOL"] = "OFF"
        cmake.definitions["ENABLE_ENCODING:BOOL"] = "OFF"
        cmake.definitions["ENABLE_ENCODING_COMPILER:BOOL"] = "OFF"
        cmake.definitions["ENABLE_XML:BOOL"] = "ON"
        cmake.definitions["ENABLE_JSON:BOOL"] = "ON"
        cmake.definitions["ENABLE_MONGO:BOOL"] = "OFF"
        cmake.definitions["ENABLE_PDF:BOOL"] = "OFF"
        cmake.definitions["ENABLE_UTIL:BOOL"] = "ON"
        cmake.definitions["ENABLE_NET:BOOL"] = "ON"
        cmake.definitions["DISABE_INTERNAL_OPENSSL:BOOL"] = "ON"
        cmake.definitions["ENABLE_SQL:BOOL"] = "OFF"
        cmake.definitions["ENABLE_SQL_SQLITE:BOOL"] = "OFF"
        cmake.definitions["ENABLE_SQL_MYSQL:BOOL"] = "OFF"
        cmake.definitions["ENABLE_SQL_POSTGRESQL:BOOL"] = "OFF"
        cmake.definitions["ENABLE_SQL_ODBC:BOOL"] = "OFF"
        cmake.definitions["ENABLE_SEVENZIP:BOOL"] = "OFF"
        cmake.definitions["ENABLE_ZIP:BOOL"] = "ON"
        cmake.definitions["ENABLE_APACHECONNECTOR:BOOL"] = "OFF"
        cmake.definitions["ENABLE_CPPPARSER:BOOL"] = "OFF"
        cmake.definitions["ENABLE_POCODOC:BOOL"] = "OFF"
        cmake.definitions["ENABLE_PAGECOMPILER:BOOL"] = "OFF"
        cmake.definitions["ENABLE_PAGECOMPILER_FILE2PAGE:BOOL"] = "OFF"
        cmake.definitions["ENABLE_REDIS:BOOL"] = "OFF"
        cmake.definitions["ENABLE_TESTS:BOOL"] = "OFF"
        cmake.definitions["ENABLE_SAMPLES:BOOL"] = "OFF"
        #
        cmake.definitions["DISABLE_CPP14:BOOL"] = "ON"
        cmake.definitions["POCO_UNBUNDLED:BOOL"] = "ON"
        cmake.definitions["POCO_STATIC:BOOL"] = "ON"
        #
        cmake.configure()
        cmake.build()
        
    def package_info(self):
        self.cpp_info.defines = ["POCO_DISABLE_CPP14", "POCO_STATIC"]
