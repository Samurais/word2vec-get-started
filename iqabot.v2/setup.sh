#! /bin/bash 
###########################################
# Setup Environments
# Deps
#  * docker v17.*
#  * docker-compose v1.14.*
#  * Python v2.7
#  * virtualenv v15.1.0
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
# create python2
if [ ! -d ~/venv-py2 ]; then
    virtualenv --no-site-packages -p /usr/local/bin/python2.7 ~/venv-py2
fi
source ~/venv-py2/bin/activate

cd $baseDir/..
# start elasticsearch and hanlp api services, run in background
docker-compose up --force-recreate -d
echo "Wait for elasticsearch service alive ..."
sleep 20
# use "docker-compose logs" for logging

cd $baseDir
echo "Install requirements"
pip install -r Requirement.txt
echo "Pipe data to elasticsearch"
python bot.py --pipe-to-es
echo "Search with elasticsearch client"
set -x
python bot.py --query="为什么要获得医疗保险补充保险"
echo "Done."

# echo "Shutdown docker services in 3 seconds"
# sleep 3
# docker-compose down
