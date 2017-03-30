from app.AppException import AppException


class InputFileException(AppException):
    def __init__(self, message):
        self.message = message
        self.code = 2
