from sys import stdin
from app.arguments.Config import Config
from app.io.exceptions.InputFileException import InputFileException

class Input:
    def __init__(self, config: Config):
        self._config = config

    def get_input(self):
        if self._config.use_stdin():
            return stdin.read()
        else:
            try:
                with open(self._config.values['input'], 'r') as f:
                    return f.read()
            except:
                raise InputFileException('Error opening and reading the input')

    def get_format_table(self):
        try:
            with open(self._config.values['format'], 'r') as f:
                return f.read()
        except:
            return None

