#!/bin/sh

cat >hello-world.html <<EOF
<html>
    <head>
        <title> Hello world! </title>
        <link rel="icon" href="data:,">
    </head>
    <body>
        <h1> Hello world! </h1>
    </body>
</html>
EOF

echo "http://localhost:12000/hello-world.html"
python3 web-server.py
