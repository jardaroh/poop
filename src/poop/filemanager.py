try:
    import uos as os
except ImportError:
    import os


class FileManager:

    def __init__(self, file_path=None):
        self.file_path = file_path
        self.file = None
        self.current_character = None

        if self.file_path:
            self.open_file(file_path)

    def __del__(self):
        if self.file:
            self.file.close()

    def open_file(self, file_path):
        self.file_path = file_path

        if self.file is not None:
            self.close_file()

        self.file = open(self.file_path, encoding='utf-8')

    def close_file(self):
        self.file.close()

    def read_file(self):
        return self.file.read()

    def readline(self):
        return self.file.readline()

    @staticmethod
    def listdir(path):
        return os.listdir(path)
