from app.exceptions import AppException


class InvalidArgumentsException(AppException):
    def __init__(self, message):
        self.message = message
        self.code = 1
