#!/bin/bash
DEBUG_ON=false
LOG_FILE=1.txt

debug() {
if $DEBUG_ON
then
   echo "DEBUG: $*" | tee -a $LOG_FILE
fi
}
