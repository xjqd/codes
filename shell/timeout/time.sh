#!/bin/bash
timeout() {
waitfor=5
command=$*
echo ${command}
$command >/dev/null 2>&1 &
commandpid=$!

(sleep $waitfor; kill -9 ${commandpid} >/dev/null 2>&1) &
watchdogpid=$!
sleeppid=$(ps $ppid $watchdogpid | awk '{print $1}')
wait ${commandpid}
kill $sleeppid >/dev/null 2>&1
}
