#! /bin/bash 
###########################################
#
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
source $baseDir/env.sh
source $baseDir/../localrc
# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
 word2vec \
    -train $FILEIN \
    -output  $FILEOUT \
    -size $EMBEDDING_DIM \
    -window $WINDOW \
    -sample $SAMPLE \
    -negative $NEGATIVE \
    -hs $HS \
    -cbow $CBOW \
    -iter $ITER \
    -binary $BINARY \
    -min-count $MINCOUNT \
    -threads $THREADS \
