#!/bin/bash
function reverse()
{
  if [ -d $1 ]
  then
	cat >"./"${1}"/"me <<- End
	"hello"
	"world"
	End
  filename=${1}
  for name in $(ls $filename)
  do
     reverse ${1}"/"${name}
  done
 fi
}

for name in $(ls)
do
    reverse $name
done
