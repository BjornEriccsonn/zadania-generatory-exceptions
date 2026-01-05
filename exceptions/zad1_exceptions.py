import os


class FileHandler:
    def __init__(self, file_path, no_connectors, max_file_size):
        self.file_path: str = file_path
        self.no_connectors: int = no_connectors
        self.max_file_size: int = max_file_size

    @property
    def file_path(self):
        return self._file_path
    @property
    def no_connectors(self):
        return self._no_connectors
    @property
    def max_file_size(self):
        return self._max_file_size

    @file_path.setter
    def file_path(self, value):
        if not isinstance(value, str) or not value.strip():
            raise InvalidFilePathError
        self._file_path = value

    @no_connectors.setter
    def no_connectors(self, value):
        if value > 10: raise InvalidConnectorCountError(value)
        self._no_connectors = value

    @max_file_size.setter
    def max_file_size(self, value):
        if value < 1000 or value > 9999: raise InvalidFileSizeError
        self._max_file_size = value

    def read_content(self):
        print(f"I AM READING THE FILE: {self.file_path} ")

    def save_to_file(self):
        print(f"I AM SAVING THE FILE: {self.file_path} ")

class FileHandlerError(Exception):
    pass

class InvalidFilePathError(FileHandlerError):
    def __str__(self):
        return "File path cannot be empty and must be a string"

class InvalidFileSizeError(FileHandlerError):
    def __str__(self):
        return "Max file size need to be at least 4 digit"

class InvalidConnectorCountError(FileHandlerError):
    def __init__(self, _no_connectors):
        self.no_connectors: int = _no_connectors

    def __str__(self):
        return f"Max connectors is 10. Number of connectors provided: {self.no_connectors}"

if __name__ == '__main__':
    fh1 = FileHandler("./test.txt", 4, 1000)
    #fh_wrong_path = FileHandler("", 4, 1000)
    #fh_wrong_conn = FileHandler("./wrong_test.txt", 11, 1000)
    #fh_wrong_conn = FileHandler("./wrong_test.txt", 4, 9)
