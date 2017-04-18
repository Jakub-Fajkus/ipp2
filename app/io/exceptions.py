"""
    File name: exceptions.py
    Author: Jakub Fajkus
    Date created: 14.4.2017
    Date last modified: 18.4.2017
    Python Version: 3.6
"""

from app.exceptions import AppException


class InputFileException(AppException):
    """Exception for input file errors.

    This exception is thrown when the input file could not be opened or the content could not be read.
    """
    def __init__(self, message):
        self.message = message
        self.code = 2


class OutputFileException(AppException):
    """Exception for output file errors.

    This exception is thrown when the output file could not be written.
    """
    def __init__(self, message):
        self.message = message
        self.code = 3
