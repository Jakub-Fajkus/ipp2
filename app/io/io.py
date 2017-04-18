"""
    File name: io.py
    Author: Jakub Fajkus
    Date created: 14.4.2017
    Date last modified: 18.4.2017
    Python Version: 3.6
"""

from sys import stdin
from app.arguments.arguments import Config
from app.io.exceptions import InputFileException
from app.io.exceptions import OutputFileException


class Input:
    """Acting as a input endpoint to the aplication.
    
    The class is used to read the input data as well as the formatting file.
    """
    def __init__(self, config: Config):
        self._config = config

    def get_input(self):
        """Get input for the application. Use Config to determine the source of the data."""
        if self._config.use_stdin():
            return stdin.read()
        else:
            try:
                with open(self._config.values['input'], 'r') as f:
                    return f.read()
            except:
                raise InputFileException('Error opening and reading the input')

    def get_format_table(self):
        """Get the content of the formatting file"""
        try:
            with open(self._config.values['format'], 'r') as f:
                return f.read()
        except:
            return None


class Output:
    """Responsible for writing the output to a file or stdout."""
    def __init__(self, config: Config):
        self._config = config

    def present_output(self, output: str):
        """Print the output to the console or to a file"""

        if self._config.use_stdout():
            print(output, flush=True, end='')
        else:
            try:
                # print("OUTPUT FILE IS THERE!!!!", self._config.values['output'])
                with open(self._config.values['output'], mode='w', newline='') as f:
                    # print("PRINITNG OUTPUT>>>>"+output+"<<<<<")
                    f.write(output)
                    # print("OUTPUT FILE IS THERE!!!!", "After write")
            except:
                raise OutputFileException('Error writing the output')
