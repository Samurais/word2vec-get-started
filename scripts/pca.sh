#! /bin/bash 
###########################################
# start notebook server
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
source ~/venv-py2/bin/activate

# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..
jupyter notebook tools/jupyter/word2vec-get-started.ipynb