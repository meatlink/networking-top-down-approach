from unittest import TestCase
from unittest.mock import Mock

from request_processor import RequestProcessor


class TestRequestProcessor(TestCase):

    def setUp(self):
        self.rp = RequestProcessor(
            file_reader=self.create_fake_file_reader()
        )

    def test_process(self):
        req = Mock(["get_url"])
        req.get_url.return_value = "/fake_file_name.html"
        res = self.rp.process(req)
        self.assertEqual(res.get_content(), "fake file content!")

    def create_fake_file_reader(self):
        file_reader = Mock(["read_file"])
        def fake_read_file(fname):
            if fname == "fake_file_name.html":
                return "fake file content!"
            raise Exception("No such file")
        file_reader.read_file.side_effect = fake_read_file
        return file_reader
