"""
    File name: exceptions.py
    Author: Jakub Fajkus
    Date created: 14.4.2017
    Date last modified: 18.4.2017
    Python Version: 3.6
"""

class AppException(Exception):
    """Base application exception.

    All other exceptions should be subclasses of this class.
    """
    def __init__(self, message):
        self.message = message
        self.code = 100
