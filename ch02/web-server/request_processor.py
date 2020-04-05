from http_wrapper import HTTPResponse


class RequestProcessor:

    def __init__(self, file_reader):
        self.file_reader = file_reader

    def process(self, req):
        return HTTPResponse(
            content=self.file_reader.read_file(self.strip_leading_slash(req.get_url()))
        )

    def strip_leading_slash(self, url):
        return url[1:]
