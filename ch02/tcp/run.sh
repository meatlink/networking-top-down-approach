#!/bin/sh

python3 tcp-server.py &
srv_pid="$!"
echo "sleeping for 1 sec to let server start" ; sleep 1
while true ; do
    python3 tcp-client.py
    echo "repeat? (y/n): "
    read a
    if test "$a" != "y" ; then
        break
    fi
done
kill -3 "$srv_pid"
