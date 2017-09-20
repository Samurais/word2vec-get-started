# constants
baseDir=$(cd `dirname "$0"`;pwd)
export PATH=$PATH:$baseDir/../src
# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
