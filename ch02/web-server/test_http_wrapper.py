from textwrap import dedent
from unittest import TestCase

from http_wrapper import HTTPRequest, HTTPResponse


sample_request_text = """\
GET /hello-world.html HTTP/1.1\r\n\
Host: localhost:12000\r\n\
User-Agent: curl/7.64.1\r\n\
Accept: */*\r\n\
\r\n\
"""


class TestHTTPRequest(TestCase):

    def setUp(self):
        self.req = HTTPRequest(sample_request_text)

    def test_get_method(self):
        self.assertEqual("GET", self.req.get_method())

    def test_get_url(self):
        self.assertEqual("/hello-world.html", self.req.get_url())


# curl -i http://example.com
sample_response = """\
HTTP/1.1 200 OK\r\n\
Content-Type: text/html; charset=UTF-8\r\n\
Content-Length: 117\r\n\
\r\n\
<html>
    <head>
        <title>Hello world!</title>
    </head>
    <body>
        Hello world!
    </body>
</html>\r\n\
"""


class TestHTTPResponse(TestCase):

    def test_(self):
        content = dedent("""
            <html>
                <head>
                    <title>Hello world!</title>
                </head>
                <body>
                    Hello world!
                </body>
            </html>
        """).strip()
        res = HTTPResponse(
            content=content
        )
        self.assertEqual(sample_response, res.to_text())