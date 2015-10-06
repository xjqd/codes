#!/bin/bash
function reverse()
{
   if [[ -d $1 ]]
   then
	for name in $(ls $1)
	do
	    if [[ -d $name ]]
	    then
		reverse $1"/"$name
	    elif [[ $name = "me" ]]
            then
		echo "find me"
		#$(rm ${1}"/"$name)
		#return 1
	    else
		echo "else"
		#return 1
	    fi
	done
   fi
}
for name in $(ls)
do
    reverse $name
done
