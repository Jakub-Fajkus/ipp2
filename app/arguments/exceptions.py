"""
    File name: exceptions.py
    Author: Jakub Fajkus
    Date created: 14.4.2017
    Date last modified: 18.4.2017
    Python Version: 3.6
"""

from app.exceptions import AppException


class InvalidArgumentsException(AppException):
    """Exception for invalid arguments application error.
    
    This exception is thrown when there are unknown arguments or the combination of them is not valid.
    """
    def __init__(self, message):
        self.message = message
        self.code = 1
