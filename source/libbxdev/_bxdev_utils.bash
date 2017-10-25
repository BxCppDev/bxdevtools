# -*- mode: shell-script; -*-

readonly BXDEV_UTILS_SUCCESS=0
readonly BXDEV_UTILS_FAILURE=1
readonly BXDEV_UTILS_TRUE=0
readonly BXDEV_UTILS_FALSE=1

function bxdev_utils_check_integer()
{
    local token="$1"
    if [ -z "${token}" ] ; then
	return $BXDEV_UTILS_FALSE
    fi
    local check="`echo ${token} | sed -e 's@[0-9]@@g'`"
    if  [ "x${check}" != "x" ] ; then
	return $BXDEV_UTILS_FALSE
    fi
    return $BXDEV_UTILS_TRUE
}
