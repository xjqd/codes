#!/bin/bash
dir=$(pwd)
echo $dir
cd $dir
$(cd /)
`cd /`
echo $(pwd)
# no double quota it still works
# echo is program, the laters are the parameters
echo runing command $dir
filename=$(cat emp.data | awk  '{print $NF}')
echo $filename
for name in $filename
do
	echo $name
done

