from textwrap import dedent


class HTTPRequest:

    def __init__(self, text):
        self.text = text
        self.method = None

    def get_method(self):
        if self.method == None:
            self.method = self.extract_word(0, 0)
        return self.method

    def get_url(self):
        return self.extract_word(0, 1)

    def extract_word(self, line_n, word_n):
        line = self.get_lines()[line_n]
        word = line.split()[word_n]
        return word

    def get_lines(self):
        return self.text.split("\r\n")


class HTTPResponse:

    def __init__(self, content):
        self.content = content

    def to_text(self):
        pattern = dedent("""\
            HTTP/1.1 200 OK\r\n\
            Content-Type: text/html; charset=UTF-8\r\n\
            Content-Length: {content_len}\r\n\
            \r\n\
            {content}\r\n\
        """)
        return pattern.format(
            content=self.content,
            content_len=len(self.content)
        )

    def get_content(self):
        return self.content
