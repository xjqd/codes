#!/bin/bash
source ./time.sh
run()
{
   while ((1))
   do
      echo "hello"
   done
}

run1()
{
 echo "nihao"
 sleep 10
}

#timeout ("run1") 不能加括号
timeout "run1"
