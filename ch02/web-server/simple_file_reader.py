import os.path


class SimpleFileReader:
    def __init__(self, dir):
        self.dir = dir

    def read_file(self, fname):
        with open(os.path.join(self.dir, fname)) as f:
            return f.read()
