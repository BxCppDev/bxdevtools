# -*- mode: python; -*-

import sys
import string
import os
import os.path

class configure_file :
    """Configure an output file by substitution from a input template file."""

    def __init__(self, debug_ = False) :
        self._subs_ = {}
        self._debug_ = debug_
        return

    def add_substitution(self, token_, value_) :
        self._subs_[token_] = value_
        return

    def run(self, infile_, outfile_) :
        ls = os.listdir(".")
        print("ls = %s" % (ls))
        if not os.path.exists(infile_) :
            raise Exception("Input file path '%s' does not exist on this filesystem!" % infile_)
        if os.path.exists(outfile_) :
            raise Exception("Output file path '%s' already exists on this filesystem!" % outfile_)
        if self._debug_ :
            sys.stderr.write("[debug] configure_file.run: input filename  : '%s'\n" % infile_)
        fin = open(infile_) #, "r")
        if self._debug_ :
            sys.stderr.write("[debug] configure_file.run: input file : %s\n" % (fin))
        lines = fin.readlines()
        fin.close()
        if self._debug_ :
            sys.stderr.write("[debug] configure_file.run: input lines : %s\n" % (lines))
            sys.stderr.write("[debug] configure_file.run: input lines : %d\n" % len(lines))
            sys.stderr.write("[debug] configure_file.run: output filename : '%s'\n" % outfile_)
        outfiledir=os.path.abspath(os.path.join(outfile_, os.pardir))
        if not os.path.isdir(outfiledir) :
            os.makedirs(outfiledir)
        fout = open(outfile_, "w")
        for i, line in enumerate(lines) :
            workline = line[:-1]
            if self._debug_ :
                sys.stderr.write("[debug] configure_file.run: input line #%d: <%s>\n" % (i, workline))
            for key in self._subs_.keys() :
                keytag = "@%s@" % key
                if self._debug_ :
                    sys.stderr.write("[debug] configure_file.run: keytag = '%s'\n" % keytag)
                tmp=workline.replace(keytag, self._subs_[key])
                workline=tmp
            subsline=workline
            if self._debug_ :
                sys.stderr.write("[debug] configure_file.run: <%s>\n" % subsline)
            fout.write("%s\n" % subsline)
        fout.close()
        return

    def dump(self, out_ = sys.stderr, title_ = '', indent_ = '') :
        if len(title_) :
            out_.write(indent_ + title_ + '\n')
        out_.write("%s`-- Substitutions: \n" % (indent_))
        lcount = 0
        for key in self._subs_.keys() :
            tag= "|-- "
            if lcount == len(self._subs_.keys()) - 1 :
                tag = "`-- "
            itemtag = "    "
            out_.write("%s%4s%4s%s -> %s\n" % (indent_, itemtag, tag, key ,self._subs_[key]))
            lcount += 1
        return

    @staticmethod
    def test(debug_ = False):
        debug = debug_
        cf = configure_file(debug)
        cf.add_substitution("PACKAGE_NAME", "BxToyPack")
        cf.add_substitution("PACKAGE_VERSION", "0.1.0")
        cf.add_substitution("PACKAGE_DESC", "A dummy package")
        cf.add_substitution("PACKAGE_INSTALL_PREFIX", "/opt/sw")
        cf.dump(sys.stderr, "Configure file: ", "debug: ")
        infile="./test-pybxdev-tools-configure-file.in"
        fin = open(infile, "w")
        fin.write('# Dummy template:\n')
        fin.write('Name="@PACKAGE_NAME@"\n')
        fin.write('Version="@PACKAGE_VERSION@"\n')
        fin.write('PrefixPath="@PACKAGE_INSTALL_PREFIX@/@PACKAGE_NAME@/@PACKAGE_VERSION@"\n')
        fin.write('PackageDataPath="@PACKAGE_INSTALL_PREFIX@/share/@PACKAGE_NAME@-@PACKAGE_VERSION@"\n')
        fin.write('Description="@PACKAGE_DESC@"\n')
        fin.write('Dummy="Test"\n')
        fin.close()
        outfile="./_tmp/test/test-pybxdev-tools-configure-file.out"
        cf.run(infile, outfile)
        return

if __name__ == "__main__" :
    configure_file.test()
    sys.exit(0)
