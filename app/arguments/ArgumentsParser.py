import re
import sys
from app.arguments.exceptions import InvalidArgumentsException


class ArgumentsParser:
    def __init__(self):
        self._processedArguments = []
        self._config = None

    def parse_arguments(self, config):
        """fill the config with some configuration form the command line"""
        self._config = config

        for arg in sys.argv[1:]:  # skip the script path
            print(arg)

            if self._process_argument(r"^--input=(.*)$", arg, 'input'):
                print('match input')
            elif self._process_argument(r"^-i=(.*)$", arg, 'input'):
                print('match i')
            elif self._process_argument(r"^--output=(.*)$", arg, 'output'):
                print('match output')
            elif self._process_argument(r"^-o=(.*)$", arg, 'output'):
                print('match o')
            elif self._process_argument(r"^--help$", arg, 'help', False):
                print('match help')
            elif self._process_argument(r"^-h$", arg, 'help', False):
                print('match h')
            elif self._process_argument(r"^--format=(.*)$", arg, 'format'):
                print('match format')
            elif self._process_argument(r"^-f=(.*)$", arg, 'format'):
                print('match f')
            elif self._process_argument(r"^--br$", arg, 'br', False):
                print('match br')
            elif self._process_argument(r"^-b$", arg, 'br', False):
                print('match b')
            else:
                raise InvalidArgumentsException.InvalidArgumentsException('Unknown argument ' + arg)

        print("config values: ", self._config.values)

    def _process_argument(self, regex: str, arg: str, arg_semantics: str, add_to_config: bool = True) -> bool:
        input_match = re.search(regex, arg)
        if input_match:
            print('match ' + arg_semantics)
            self._add_to_processed(arg_semantics)

            try:
                self._config.values[arg_semantics] = input_match.group(1) if add_to_config else None
            except IndexError:
                raise InvalidArgumentsException.InvalidArgumentsException("Invalid argument: " + arg)

            return True
        else:
            return False

    def _add_to_processed(self, arg_semantics: str):
        if arg_semantics in self._processedArguments:
            raise InvalidArgumentsException.InvalidArgumentsException(
                'Invalid parameters - cannot use the same parameter twice'
            )
        else:
            self._processedArguments.append(arg_semantics)

        print("Processed so far:", self._processedArguments)
