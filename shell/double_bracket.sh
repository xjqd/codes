#!/bin/bash
#((exp1, exp2))
a=1
b=2
c=3
# size yunsuan
#  x=((a+1))
#  the above line is wrong. but we can not use '$' in the double brackets.
#  we can use whole expression, like a=a+1
# style 1
((a=a+1))
echo $a
# style 2
b=$((b+1))
echo $b
a=$((a+1, b++, c++))
echo $a $b $c
#
((a+1, b++, c++))
echo $a $b $c
# following logic exp
x=1
y="ab"
z=$((x>1?8:9))
echo $z
((y!=x))&& echo "err2"
((x<2))&& echo "ok"

# logic express in control flow
num=10
total=0
for((i=0; i<num; i++))
do
 echo $((total+=i))
done
i=0
while((i<num))
do
  # use , not ;
  ((total+=i, i++))
done
echo $total
