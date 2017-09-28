#! /bin/bash 
###########################################
#
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..
docker run -it --rm -v $PWD:/workspace \
    --name ubuntu-dev \
    samurais/ubuntu-dev:1.0.2 \
    zsh
