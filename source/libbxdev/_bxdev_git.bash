# -*- mode: shell-script; -*-

function bxdev_git_default_origin_host()
{
    local _bxdev_git_default_origin_hostname="https://github.com/BxCppDev/"
    if [ "x${BXDEV_GIT_DEFAULT_ORIGIN_HOSTNAME}" != "x" ]; then
	_bxdev_git_default_origin_hostname="${BXDEV_GIT_DEFAULT_ORIGIN_HOSTNAME}"
    fi
    echo ${_bxdev_git_default_origin_hostname}
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

# Check if a branch name is for feature branch.
# Return 0 is yes, 1 if no
function bxdev_git_check_feature_branch_name()
{
    local branch_name="$1"
    if [ "x${branch_name:0:9}" = "x_feature-" ]; then
	return 0
    elif [ "x${branch_name:0:8}" = "xfeature-" ]; then
	return 0
    fi
    return 1
}

# Check if a branch name is master.
# Return 0 is yes, 1 if no
function bxdev_git_check_master_branch_name()
{
    local branch_name="$1"
    if [ "x${branch_name}" = "xmaster" ]; then
	return 0
    fi
    return 1
}

# Check if a branch name is develop.
# Return 0 is yes, 1 if no
function bxdev_git_check_develop_branch_name()
{
    local branch_name="$1"
    if [ "x${branch_name}" = "xdevelop" ]; then
	return 0
    fi
    return 1
}

# Check if directory is in a Git repository.
# Return 0 is yes, 1 if no
function bxdev_git_check_repository()
{
    git rev-parse --is-inside-work-tree > /dev/null 2>&1
    if [ $? -ne 0 ]; then
	return 1
    fi
    return 0
}

# Check if directory is a base Git directory.
# Return 0 is yes, 1 if no
function bxdev_git_check_base_repository()
{
    bxdev_git_check_repository
    if [ $? -ne 0 ]; then
	return 1
    fi
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
