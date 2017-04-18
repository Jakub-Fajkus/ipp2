"""
    File name: exceptions.py
    Author: Jakub Fajkus
    Date created: 14.4.2017
    Date last modified: 18.4.2017
    Python Version: 3.6
"""

from app.exceptions import AppException


class InvalidRegexException(AppException):
    """Exception for input regex errors.

    This exception is thrown when the formatting regex is not valid.
    """
    def __init__(self, message):
        self.message = message
        self.code = 4
