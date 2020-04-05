#!/bin/sh

python3 udp-server.py &
srv_pid="$!"
echo "sleeping for 1 sec to let server start" ; sleep 1
python3 udp-client.py
kill "$srv_pid"
