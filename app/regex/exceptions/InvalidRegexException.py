from app.AppException import AppException


class InvalidRegexException(AppException):
    def __init__(self, message):
        self.message = message
        self.code = 4
