# -*- mode: shell-script; -*-

. $(bxdevtools-config --moduledir)/_bxdev_message.bash

function bxdev_package_create()
{
    local error_code=0
    local package_name="$1"
    shift 1
    local package_dir="$1"
    shift 1



    return ${error_code}
}


# end
