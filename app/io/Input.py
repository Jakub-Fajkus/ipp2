from sys import stdin
from app.arguments.Config import Config

class Input:
    def __init__(self, config: Config):
        self._config = config

    def get_input(self):
        if self._config.use_stdin():
            return stdin.read()
        else:
            with open(self._config.values['input'], 'r') as f:
                return f.read()
