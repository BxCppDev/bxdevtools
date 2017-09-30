# -*- mode: shell-script; -*-

function _bxdev_message()
{
    local what="$1"
    if [ "x${what}" != "x" ]; then
	shift 1
	echo -n >&2 "[${what}] "
    fi
    echo >&2 "$@"
    return
}

function bxdev_message_error()
{
    _bxdev_message error $@
    return
}

function bxdev_message_warning()
{
    _bxdev_message warning $@
    return
}

function bxdev_message_info()
{
    _bxdev_message info $@
    return
}

function bxdev_message_debug()
{
    _bxdev_message debug $@
    return
}

function bxdev_message_trace()
{
    _bxdev_message trace $@
    return
}

function bxdev_message_fatal()
{
    _bxdev_message fatal $@
    return
}

# end
