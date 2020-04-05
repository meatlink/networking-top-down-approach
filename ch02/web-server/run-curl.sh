#!/bin/sh

cat >hello-world.html <<EOF
<html>
    <head>
        <title> Hello world! </title>
    </head>
    <body>
        <h1> Hello world! </h1>
    </body>
</html>
EOF

python3 web-server.py &
srv_pid="$!"
echo kill -9 "$srv_pid"
sleep 1
curl localhost:12000/hello-world.html
kill -9 "$srv_pid"
