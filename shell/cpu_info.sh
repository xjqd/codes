#!/bin/bash
logiccpu=0
physicalcpu=0
corenum=0
logiccpu=$(grep "processor" /proc/cpuinfo|sort -u|wc -l)
corenum=$(grep "cpu cores" /proc/cpuinfo|uniq|awk -F':' '{print $2}'|xargs)
physicalnum=$(grep "physical id" /proc/cpuinfo|sort -u|wc -l)
echo "******CPU Information*********"
echo "Logical CPU Number:  ${logiccpu}"
echo "Physical CPU Number: ${physicalnum}"
echo "CPU cores          : ${corenum}"
echo "******End CPU Information*********"

