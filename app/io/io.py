from sys import stdin
from app.arguments.arguments import Config
from app.io.exceptions import InputFileException
from app.io.exceptions import OutputFileException


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


class Output:
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
