#!/bin/bash
function reverse()
{
  if [ ! -d $1 ]
  then
      if [[ $1 =~ (.)*(go) ]] 
      then
         echo "$1 match "
      else
         echo "$1 not match"
         if [[ $1 != "revers.sh" ]]
         then
            #echo "$1 match for $dirname"
            $(rm $1)
         fi
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
