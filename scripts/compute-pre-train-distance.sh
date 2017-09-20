#! /bin/bash 
###########################################
#
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
corpusDir=$baseDir/../corpus/wikidata/zhwiki-latest-pages-articles/
V=$corpusDir/chs.normalized.wordseg.w2v.vocab
M=$corpusDir/chs.normalized.wordseg.w2v
. $baseDir/env.sh
# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..
echo "" > words
while IFS= read -r var
do
  for x in $var; do
    echo $x  >> words
    break
  done
done < "$V"
echo "done"
