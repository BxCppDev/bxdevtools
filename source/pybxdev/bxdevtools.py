# -*- mode: python; -*-

import os
import sys
import subprocess

import package.package

class bxdevtools(package.package) :
    """Package BxDevTools"""

    @staticmethod
    def installation_prefix() :
        proc = subprocess.Popen(["bxdevtools-config", "--prefix"], stdout=subprocess.PIPE)
        out, err = proc.communicate()
        _pybxdev_prefix = out
        return _pybxdev_prefix

    def __init__() :
        super(pybxdev.package.package, self).__init__("BxDevTools")
        set_build_system("cmake")
        add_language("bash")
        add_language("python")
        set_license("GPL3")
        self._prefix_ = pybxdev.installation_prefix()
        return

    def dump(self, out_ = sys.stderr, title_ = '', indent_ = '') :
        super(pybxdev.package.package, self).dump(out_, title_, indent_, True)
        tag = "`-- "
        out_.write("%s%4sPrefix : '%s' \n" % (indent_, tag, self._prefix_))

if __name__ == "__main__" :
    p = pybxdev.bxdevtools()
    p.dump(sys.stdout, "Package BxDevTools: ")
    sys.exit(0)

# end
