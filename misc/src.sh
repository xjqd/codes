#!/bin/bash
echo $name
source $(dirname $0)/include.sh
echo "==================check in src========"
echo $PATH
(echo $PATH; ls;)
