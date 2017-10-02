# -*- mode: shell-script; -*-

function bxdev_git_default_origin_host()
{
    echo "https://github.com/BxCppDev/"
    return 0
}

# Check if a topic for branch name is valid.
# Return 0 is yes, 1 if no
function bxdev_git_check_feature_name()
{
    local name="$1"
    shift 1
    if [ "x${name}" = "x" ]; then
	return 1
    fi
    echo "${name}" | grep "^[[:alpha:]][[:alnum:]-_]*$"
    if  [ $? -ne 0 ]; then
	return 1
    fi
    return 0
}

# Check if directory is a base Git directory.
# Return 0 is yes, 1 if no
function bxdev_git_check_repository()
{
    if [ ! -d ".git" ]; then
	return 1
    fi
    return 0
}

# Return the name of the current branch
function bxdev_git_current_branch_name()
{
    bn=$(git branch -l | grep "^* " | cut -d' ' -f2)
    echo ${bn}
    return
}

# Check if a Git local branch with given name exists.
# Return 0 is yes, 1 if no
function bxdev_git_local_branch_exists()
{
    local brname="$1"
    shift 1
    check_br=$(git branch --list | grep " ${brname}\$")
    if [ "x${check_br}" != "x" ]; then
	return 0
    fi
    return 1
}

# Check if a Git origin branch with given name exists.
# Return 0 is yes, 1 if no
function bxdev_git_remote_branch_exists()
{
    local brname="$1"
    shift 1
    check_br=$(git branch --list -r | grep " origin/${brname}\$")
    if [ "x${check_br}" != "x" ]; then
	return 0
    fi
    return 1
}

# end
