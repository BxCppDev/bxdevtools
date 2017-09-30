# - Top level CMakeLists.txt for BxDevTools package

cmake_minimum_required(VERSION 3.3 FATAL_ERROR)
project(BxDevTools)

if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})
  message(STATUS "${PROJECT_NAME} requires an out-of-source build.")
  message(STATUS "Please remove these files from ${CMAKE_BINARY_DIR} first:")
  message(STATUS "  CMakeCache.txt")
  message(STATUS "  CMakeFiles")
  message(STATUS "Once these files are removed, create a separate directory")
  message(STATUS "and run CMake from there, pointing it to:")
  message(STATUS "  ${CMAKE_SOURCE_DIR}")
  message(FATAL_ERROR "in-source build detected")
endif()

# - Load Custom Modules
list(INSERT CMAKE_MODULE_PATH 0 ${PROJECT_SOURCE_DIR}/cmake)

# - Version number management utilities:
include(BxVersionManager)

# - Versioning only giving major and minor. Patch number is
#   automatically deduced from an external file.
bx_version_set(BxDevTools 0 1)

#-----------------------------------------------------------------------
# - Standard UNIX Tool install paths, including relative paths for use
# by applications requiring resources
include(GNUInstallDirs)

# - Validate that certain paths are relative, otherwise relocation may fail
foreach(_dir BINDIR LIBDIR INCLUDEDIR DATAROOTDIR)
  if(IS_ABSOLUTE "${CMAKE_INSTALL_${_dir}}")
    message(FATAL_ERROR "Absolute path for CMAKE_INSTALL_${_dir} not allowed")
  endif()
endforeach()

set(BxDevTools_TAG BxDevTools-${BxDevTools_VERSION})
message(STATUS "BxDevTools_TAG = ${BxDevTools_TAG}")

#-----------------------------------------------------------------------

configure_file(source/libbxdev/libbxdev.bash.in
  ${PROJECT_BINARY_DIR}/source/libbxdev/libbxdev.bash
  @ONLY)

configure_file(${PROJECT_SOURCE_DIR}/source/scripts/bxdevtools-config.in
  ${PROJECT_BINARY_DIR}/source/scripts/bxdevtools-config
  @ONLY)

install( FILES
  ${PROJECT_BINARY_DIR}/source/libbxdev/libbxdev.bash
  DESTINATION ${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/${BxDevTools_TAG}/
  PERMISSIONS OWNER_READ OWNER_WRITE
  GROUP_READ
  WORLD_READ
  )

install( FILES
  ${PROJECT_SOURCE_DIR}/source/scripts/bxdevtools
  ${PROJECT_BINARY_DIR}/source/scripts/bxdevtools-config
  ${PROJECT_SOURCE_DIR}/source/scripts/configure_file
  ${PROJECT_SOURCE_DIR}/source/scripts/bxgit_create_feature_branch
  DESTINATION ${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_BINDIR}/
  PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE
  GROUP_READ GROUP_EXECUTE
  WORLD_READ WORLD_EXECUTE
  )

set(_bxdev_lib_modules
  ${PROJECT_SOURCE_DIR}/source/libbxdev/_bxdev_app.bash
  ${PROJECT_SOURCE_DIR}/source/libbxdev/_bxdev_message.bash
  ${PROJECT_SOURCE_DIR}/source/libbxdev/_bxdev_version.bash
  ${PROJECT_SOURCE_DIR}/source/libbxdev/_bxdev_git.bash
  )

install( FILES
  ${_bxdev_lib_modules}
  DESTINATION ${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/${BxDevTools_TAG}/modules/
  )

#-----------------------------------------------------------------------
# - Python API

configure_file(${PROJECT_SOURCE_DIR}/source/pybxdev/__init__.py.in
  ${PROJECT_BINARY_DIR}/source/pybxdev/__init__.py
  @ONLY)

install( FILES
  ${PROJECT_BINARY_DIR}/source/pybxdev/__init__.py
  DESTINATION ${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/${BxDevTools_TAG}/pybxdev/
  )

install( DIRECTORY ${PROJECT_SOURCE_DIR}/source/pybxdev
  DESTINATION ${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/${BxDevTools_TAG}/
  FILE_PERMISSIONS OWNER_READ GROUP_READ WORLD_READ
  DIRECTORY_PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE
  GROUP_READ GROUP_EXECUTE
  WORLD_READ WORLD_EXECUTE
  FILES_MATCHING PATTERN "*.py"
  )

# set(_bxdev_pybxdev_modules
#   ${PROJECT_BINARY_DIR}/source/pybxdev/__init__.py.in
#   source/pybxdev/package
#   source/pybxdev/_bxdev_version.bash
#   )

# set(_bxdev_pybxdev_modules
#   ${PROJECT_BINARY_DIR}/source/pybxdev/version.py
#   source/pybxdev/package
#   source/pybxdev/_bxdev_version.bash
#   )


# - end
