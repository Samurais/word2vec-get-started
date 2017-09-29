#! /bin/bash 
###########################################
# start notebook server
# deps
# cd tools/word2vec_boostpy
# python setup.py install
# pip install -U numpy matplotlib scipy scikit-learn ipython jupyter 
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
source ~/venv-py2/bin/activate

# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..
jupyter notebook tools/jupyter/word2vec-get-started.ipynb