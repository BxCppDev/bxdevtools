# -*- mode: python; -*-

import sys
import string
import os
import os.path
import re

class package :
    """Description of a software package"""

    @staticmethod
    def validate_package_name(name_) :
        name = name_.strip()
        if len(name) == 0 :
            return False
        rgx = r"^[a-zA-Z][a-zA-Z_0-9]*$"
        if not re.match(rgx, name) :
            return False
        return True

    def __init__(self, name_, license_ = "GPL3") :
        if not package.validate_package_name(name_) :
            raise Exception("Invalid package name")
        self._name_ = name_
        self._license_ = license_
        self._languages_ = []
        self._build_system_ = "cmake"
        return

    def has_build_system(self) :
        return len(self._build_system_) > 0

    def match_build_system(self, bs_) :
        return self.has_build_system() and self._build_system_ == bs_

    def set_build_system(self, bs_) :
        self._build_system_ = bs_.strip()
        return

    def add_language(self, language_) :
        self._languages_.append(language_)
        return

    def has_language(self, language_) :
        for lang in self._languages_ :
            if lang == language_ :
                return True
        return False

    def has_license(self):
        return len(self._license_) > 0

    def set_license(self, license_) :
        self._license_ = license_.strip()
        return

    def get_license(self) :
        return self._license_

    def get_name(self) :
        return self._name_

    def get_name_lower(self) :
        return self._name_.lower()

    def get_name_upper(self) :
        return self._name_.upper()

    def dump(self, out_ = sys.stderr, title_ = '', indent_ = '', inherit_ = False) :
        if len(title_) :
            out_.write(indent_ + title_ + '\n')
        out_.write("%s|-- Name : '%s' \n" % (indent_, self._name_))
        out_.write("%s|   |-- NAME : '%s' \n" % (indent_, self.get_name_upper()))
        out_.write("%s|   `-- name : '%s' \n" % (indent_, self.get_name_lower()))
        out_.write("%s|-- Languages: \n" % (indent_))
        lcount = 0
        for lang in self._languages_ :
            tag= "|-- "
            if lcount == len(self._languages_) - 1 :
                tag = "`-- "
            out_.write("%s|   %4s%s\n" % (indent_, tag ,lang))
            lcount += 1
        out_.write("%s|-- Build system : '%s'\n" % (indent_, self._build_system_))
        tag="`-- "
        if inherit_ : tag="|-- "
        out_.write("%s%4sLicense : '%s'\n" % (indent_, tag, self._license_))
        return

    def create_skeleton_dir(self, path_ = "") :
        path = path_
        if len(path) == 0 :
            path="./" + self.get_name_lower()
        if os.path.exists(path) :
            raise Exception("Path '%s' already exists on this filesystem!" % path)
        package_prefix = path
        os.makedirs(path)
        self.create_skeleton_doc_dir(package_prefix)
        if self.match_build_system("cmake") :
            self.create_skeleton_cmake_dir(package_prefix)
        return

    def create_skeleton_doc_dir(self, package_prefix_) :
        package_doc_dir = package_prefix_ + '/' + "documentation"
        os.makedirs(package_doc_dir)
        return

    def create_skeleton_cmake_dir(self, package_prefix_) :
        package_cmake_dir = package_prefix_ + '/' + "cmake"
        os.makedirs(package_cmake_dir)
        return


if __name__ == "__main__" :
    p = package("BxToyPack")
    p.set_build_system("cmake")
    p.add_language("C")
    p.add_language("C++")
    p.add_language("Python")
    p.dump(sys.stderr, "Package: ", "debug: ")
    p.create_skeleton_dir()
    sys.exit(0)

# end
