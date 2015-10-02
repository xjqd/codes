#!/bin/bash
string="this is a string"
read -r -a words <<<"$string"
# equal ${words[0]}
echo $words
#arry length
echo ${#words[@]}
#arry contents
echo ${words[*]}
for word in ${words[*]}
do
	echo $word
done
