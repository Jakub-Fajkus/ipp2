class AppException(Exception):
    def __init__(self, message):
        self.message = message
        self.code = 100
