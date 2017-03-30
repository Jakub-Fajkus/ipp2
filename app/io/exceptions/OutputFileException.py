from app.AppException import AppException


class OutputFileException(AppException):
    def __init__(self, message):
        self.message = message
        self.code = 3
