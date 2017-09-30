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


Setup
=====

.. code:: sh

   $ export PATH=_install.d/bin:${PATH}
   $ export PYTHONPATH=$(bxdevtools-config --libdir):${PYTHONPATH}
..


In your ``.bashrc`` script, add:

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
..
