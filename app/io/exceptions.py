from app.exceptions import AppException


class InputFileException(AppException):
    def __init__(self, message):
        self.message = message
        self.code = 2


class OutputFileException(AppException):
    def __init__(self, message):
        self.message = message
        self.code = 3
