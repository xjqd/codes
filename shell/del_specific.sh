#!/bin/bash
function reverse()
{
  if [ -f $1 ]
  then
      if [[ $1 =~ "me" ]] 
      then
            $(rm $1)
      fi
      # the different exit and return 
      # exit 1
      return 1
  fi
  #filename=${filename}${1}"/"
  filename=${1}
  for name in $(ls $filename)
  do
     reverse ${1}"/"${name}
  done
}

for name in $(ls)
do
    reverse $name
done
