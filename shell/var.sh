#!/bin/bash
i=3
# wrong $i++
((i++))
echo $i
echo $((i=i+1))
echo $((i++))
echo $i
