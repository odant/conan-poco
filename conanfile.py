# Poco Conan package
# Dmitriy Vetutnev, ODANT, 2018-2020
# Arkady Yudintsev, ODANT, 2021-2025 

from conan import ConanFile, tools
from collections import namedtuple
import os, re


class PocoConan(ConanFile):
    name = "poco"
    version = "1.13.3+2"
    license = "Boost Software License Version 1.0. https://pocoproject.org/license.html"
    description = "Modern, powerful open source C++ class libraries for building network- and internet-based applications that run on desktop, server, mobile and embedded systems."
    url = "https://github.com/odant/conan-poco"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "ninja": [True, False],
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "ninja": True,
        "shared": False,
        "fPIC": True
    }
    exports_sources = "src/*"
    no_copy_source = True
    build_policy = "missing"
    package_type = "library"
    
    def layout(self):
        tools.cmake.cmake_layout(self, src_folder="src")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        # Only C++11
        if self.settings.compiler.get_safe("libcxx") == "libstdc++":
            raise Exception("This package is only compatible with libstdc++11")
        if self.options.shared:
            self.options.rm_safe("fPIC")
        if tools.microsoft.is_msvc(self) and self.options.shared and tools.microsoft.is_msvc_static_runtime(self):
            raise ConanInvalidConfiguration("Cannot build shared poco libraries with MT(d) runtime")            

    def build_requirements(self):
        if self.options.ninja:
            self.tool_requires("ninja/[>=1.12.1]")

    def requirements(self):
        self.requires("zlib-ng/[>=2.2.4]@%s/stable" % self.user)
        self.requires("pcre2/[>=10.43]@%s/stable" % self.user)
        self.requires("openssl/[>=3.0.16]@%s/stable" % self.user)

    def source(self):
        # Disable install compiler runtime
        tools.files.replace_in_file(self, os.path.join(self.source_folder, "CMakeLists.txt"), "include(InstallRequiredSystemLibraries)", "")
        tools.files.replace_in_file(self, os.path.join(self.source_folder, "Foundation", "CMakeLists.txt"), "Pcre2::Pcre2", "PCRE2::PCRE2")
        
    def generate(self):
        benv = tools.env.VirtualBuildEnv(self)
        benv.generate()
        renv = tools.env.VirtualRunEnv(self)
        renv.generate()
        if tools.microsoft.is_msvc(self):
            vc = tools.microsoft.VCVars(self)
            vc.generate()
        deps = tools.cmake.CMakeDeps(self)    
        deps.set_property("openssl", "cmake_additional_variables_prefixes", ["OPENSSL"])
        deps.generate()
        cmakeGenerator = "Ninja" if self.options.ninja else None
        tc = tools.cmake.CMakeToolchain(self, generator=cmakeGenerator)
        tc.variables["CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS_SKIP"] = True
        tc.variables["BUILD_SHARED_LIBS"] = self.options.shared
        tc.variables["DISABLE_CPP14"] = "OFF"
        tc.variables["DISABLE_CPP11"] = "OFF"
        tc.variables["POCO_UNBUNDLED"] = "ON"
        if self.settings.os != "Windows":
            tc.variables["CMAKE_POSITION_INDEPENDENT_CODE"] = "ON"
        if self.settings.os == "Windows" and self.settings.compiler == "msvc":
            tc.variables["POCO_MT"] = tools.microsoft.is_msvc_static_runtime(self)
            tc.variables["ENABLE_MSVC_MP"] = "OFF"
        #
        tc.variables["ENABLE_ACTIVERECORD"] = "OFF"
        tc.variables["ENABLE_ACTIVERECORD_COMPILER"] = "OFF"
        tc.variables["ENABLE_ENCODINGS"] = "ON"
        tc.variables["ENABLE_ENCODINGS_COMPILER"] = "OFF"
        tc.variables["ENABLE_XML"] = "OFF"
        tc.variables["ENABLE_JSON"] = "ON"
        tc.variables["ENABLE_JWT"] = "ON"
        tc.variables["ENABLE_MONGODB"] = "OFF"
        tc.variables["ENABLE_REDIS"] = "OFF"
        tc.variables["ENABLE_PDF"] = "OFF"
        tc.variables["ENABLE_UTIL"] = "ON"
        tc.variables["ENABLE_NET"] = "ON"
        tc.variables["ENABLE_NETSSL"] = "ON"
        tc.variables["ENABLE_NETSSL_WIN"] = "OFF"
        tc.variables["ENABLE_CRYPTO"] = "ON"
        tc.variables["ENABLE_DATA"] = "OFF"
        tc.variables["ENABLE_DATA_SQLITE"] = "OFF"
        tc.variables["ENABLE_DATA_MYSQL"] = "OFF"
        tc.variables["ENABLE_DATA_POSTGRESQL"] = "OFF"
        tc.variables["ENABLE_DATA_ODBC"] = "OFF"
        tc.variables["ENABLE_SEVENZIP"] = "OFF"
        tc.variables["ENABLE_ZIP"] = "OFF"
        tc.variables["ENABLE_APACHECONNECTOR"] = "OFF"
        tc.variables["ENABLE_CPPPARSER"] = "OFF"
        tc.variables["ENABLE_POCODOC"] = "OFF"
        tc.variables["ENABLE_PAGECOMPILER"] = "OFF"
        tc.variables["ENABLE_PAGECOMPILER_FILE2PAGE"] = "OFF"
        tc.variables["ENABLE_TESTS"] = "OFF"
        tc.generate()
        
    def build(self):
        cmake = tools.cmake.CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = tools.cmake.CMake(self)
        cmake.install()
        # Remove autogenerated CMake scripts
        tools.files.rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))
        # CMake script
        tools.files.copy(self, "FindPoco.cmake", dst=self.package_folder, src=self.source_folder, keep_path=False)
        # PDB
        if self.settings.os == "Windows":
            tools.files.copy(self, "*.pdb", src=self.build_folder, dst=os.path.join(self.package_folder, "bin"), keep_path=False)
        
    def package_id(self):
        self.info.requires["zlib-ng"].full_version_mode()
        self.info.requires["openssl"].full_version_mode()
        self.info.requires["pcre2"].full_package_mode()

    _PocoLib = namedtuple("_PocoLib", ("lib_mask", "dependencies"))
    _PocoLibs = {
        "Headers":      _PocoLib(None,                                []),
        "Foundation":   _PocoLib("(?:lib)?PocoFoundation.*",          ["Headers", "pcre2::pcre2", "zlib-ng::zlib-ng"]),
        "Crypto":       _PocoLib("(?:lib)?PocoCrypto.*",              ["Headers", "Foundation", "openssl::openssl"]),
        "Encodings":    _PocoLib("(?:lib)?PocoEncodings.*",           ["Headers", "Foundation"]),
        "Net":          _PocoLib("(?:lib)?PocoNet(?:$|[^S]{1}.*)",    ["Headers", "Foundation"]),
        "NetSSL":       _PocoLib("(?:lib)?PocoNetSSL.*",              ["Headers", "Foundation", "Crypto", "Util", "Net"]),
        "JSON":         _PocoLib("(?:lib)?PocoJSON.*",                ["Headers", "Foundation"]),
        "Util":         _PocoLib("(?:lib)?PocoUtil.*",                ["Headers", "Foundation", "JSON"]),
        "JWT":          _PocoLib("(?:lib)?PocoJWT.*",                 ["Headers", "Foundation", "Crypto", "JSON"]),
        "Prometheus":   _PocoLib("(?:lib)?PocoPrometheus.*",          ["Headers", "Foundation", "Net"]),
    }   
    
    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "both")
        self.cpp_info.set_property("cmake_file_name", "Poco")
        self.cpp_info.set_property("cmake_target_name", "Poco::Poco")
        
        all_libs = tools.files.collect_libs(self)
        for libname, desc in self._PocoLibs.items():
            libs = []
            if not desc.lib_mask is None:
                pattern = re.compile(desc.lib_mask)
                libs = [lib for lib in all_libs if pattern.match(lib)]
                if not libs:
                    continue;
            self.cpp_info.components[libname].libs = libs
            self.cpp_info.components[libname].set_property(f"cmake_target_name", f"Poco::{libname}")
            self.cpp_info.components[libname].requires = desc.dependencies
        
        # Defines
        if tools.microsoft.is_msvc(self):
            self.cpp_info.components["Headers"].defines.append("POCO_NO_AUTOMATIC_LIBS")
        if not self.options.shared:    
            self.cpp_info.components["Headers"].defines.append("POCO_STATIC")
        self.cpp_info.components["Headers"].defines.append("POCO_UNBUNDLED")    
        
        # Sys libs
        if self.settings.os == "Windows":
            self.cpp_info.components["Foundation"].system_libs.extend(["ws2_32", "iphlpapi"])
        else:    
            self.cpp_info.components["Foundation"].system_libs.extend(["pthread", "dl", "rt"])
           

            

       
