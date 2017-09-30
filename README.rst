===========================================================================
BxDevTools - Tools and utilities for package development and management
===========================================================================

The ``bxdevtools`` package provides a collection of tools and utilities
to assist BxDevCpp's software developers and users.

Some semi-automated procedures are available to manage Git based software
development through a specific branch model.

* Package management:

  - create a new software package with Git support
  - setup GitHub based origin for a package

* Git branch management:

  - create a new *feature* branch (from the *develop* branch)
  - terminate a *feature* branch (merge back to the *develop* branch)
  - create a new *release* branch (from the *develop* branch)
  - terminate a *release* branch (merge back to the *master* and *develop* branches)
  - create a new *hotfix* branch (from *develop* or *release* branch)
  - terminate a *hotfix* branch

* Tag management


Download
========


#. From the directory of your choice (here ``${HOME}``):

   .. code:: sh

      $ mkdir -p ${HOME}/BxDevTools
      $ cd ${HOME}/BxDevTools
      $ git clone https://github.com/BxCppDev/bxdevtools.git bxdevtools


Installation
============

WIP

#. From the BxDevTools source directory:

   .. code:: sh

      $ cd ${HOME}/BxDevTools/bxdevtools
      $ mkdir _build.d   # Create a build directory
      $ cd _build.d      # Cd in it


#. Then configure:

   .. code:: sh

      $ cmake -DCMAKE_INSTALL_PREFIX="${HOME}/BxDevTools/bxdevtools/install-devel" ..


#. Build and install:

   .. code:: sh

      $ make
      $ make install


Setup
=====

You must define two environment variables in order to activate BxDevTools' utilities:

.. code:: sh

   $ export PATH=_install.d/bin:${PATH}
   $ export PYTHONPATH=$(bxdevtools-config --libdir):${PYTHONPATH}
..

In your ``.bashrc`` script, it is convenient to add:

.. code:: sh

   function do_bxdevtools_devel_setup()
   {
     if [ -n "${BXDEVTOOLS_INSTALL_PREFIX}" ]; then
       echo >&2 "[warning] do_bxdevtools_devel_setup: BxDevTools/devel is alreadry setup!"
       return 1
     fi
     export BXDEVTOOLS_INSTALL_PREFIX="/bxdevtools/installation/prefix"
     export PATH="${BXDEVTOOLS_INSTALL_PREFIX}/bin:${PATH}"
     export PYTHONPATH="$(bxdevtools-config --libdir):${PYTHONPATH}"
     echo >&2 "[info] do_bxdevtools_devel_setup: BxDevTools/devel is now setup!"
     return 0
   }
   alias bxdevtools_devel_setup='do_bxdevtools_devel_setup'


Invoking the following command will activate BxDevTools' utilities:

.. code:: sh

   $ bxdevtools_devel_setup


.. end
