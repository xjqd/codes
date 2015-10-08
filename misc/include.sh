#!/bin/bash

#. ../shell/tip2.sh
#source ../shell/tip2.sh
PATH="$PATH:/home/xjian/codes/shell/"
source tip2.sh # 通过PATH找tip2.sh
basedir=$(dirname $0)
filename=$(basename $0)
echo $basedir
echo $filename
echo $PATH
# wrong with $ for export
# export $PATH
export PATH
DEBUG_ON=true
function check {
	echo $PATH
	echo "check the functionality"
	debug $*
}

check "name" "hi"
echo "run something in sub-shell"
(echo $PATH; ls;)
