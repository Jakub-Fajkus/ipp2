from app.arguments.Config import Config
from app.io.exceptions.OutputFileException import OutputFileException


class Output:
    def __init__(self, config: Config):
        self._config = config

    def present_output(self, output: str):
        """Print the output to the console or to a file"""

        if self._config.use_stdout():
            print(output, flush=True)
        else:
            try:
                with open(self._config.values['output'], 'w') as f:
                    f.write(str)
            except:
                raise OutputFileException('Error writing the output')





