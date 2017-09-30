# -*- mode: shell-script; -*-

function bxdev_app_exit()
{
    local error_code=$1
    shift 1
    local error_message="$@"
    if [ "x${error_message}" != "x" ]; then
	echo >&2 "[error] ${error_message}"
    fi
    exit ${error_code}
}


# end
