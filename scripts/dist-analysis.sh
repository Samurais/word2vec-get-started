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
FILEIN=$1
FILEOUT=$FILEIN.distance
cat corpus/iqa.ngram.vocab \
    | src/distance $FILEIN > \
    $FILEOUT
