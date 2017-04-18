"""
    File name: arguments.py
    Author: Jakub Fajkus
    Date created: 14.4.2017
    Date last modified: 18.4.2017
    Python Version: 3.6
"""

import re
import sys
from app.arguments.exceptions import InvalidArgumentsException


class Config:
    """Represents the configuration of the application."""

    def __init__(self):
        self.values = {}

    def validate(self):
        """Validate the state of the current configuration.
            
        There is a rule that the "help" parameter can not be used with any other argument.
        """
        # can not use help with any other arguments
        if 'help' in self.values and len(self.values) > 1:
            raise InvalidArgumentsException('Can not use argument "help" with any other argument')

    def print_help(self) -> bool:
        return 'help' in self.values

    def use_stdin(self) -> bool:
        return 'input' not in self.values

    def use_stdout(self) -> bool:
        return 'output' not in self.values

    def add_br(self) -> bool:
        return 'br' in self.values


class ArgumentsParser:
    """Parses the command line arguments and constructs the Config object.
    
    The arguments supported(with abbreviation):
        - input(i)
        - output(o)
        - help(h)
        - format(f)
        - br(b)

    @:raise InvalidArgumentsException when the argument is not supported.        
    """

    def __init__(self):
        self._processed_arguments = []
        self._config = None

    def parse_arguments(self, config: Config) -> None:
        """Fill the config with some configuration form the command line.
        
        :param config: Config object which will be filled.
        :raise InvalidArgumentsException when an argument is not know.
        """
        self._config = config

        for arg in sys.argv[1:]:  # skip the script path

            if self._process_argument(regex=r"^--input=(.*)$", arg=arg, arg_semantics='input'):
                pass
            elif self._process_argument(regex=r"^-i=(.*)$", arg=arg, arg_semantics='input'):
                pass
            elif self._process_argument(regex=r"^--output=(.*)$", arg=arg, arg_semantics='output'):
                pass
            elif self._process_argument(regex=r"^-o=(.*)$", arg=arg, arg_semantics='output'):
                pass
            elif self._process_argument(regex=r"^--help$", arg=arg, arg_semantics='help', add_to_config=False):
                pass
            elif self._process_argument(regex=r"^-h$", arg=arg, arg_semantics='help', add_to_config=False):
                pass
            elif self._process_argument(regex=r"^--format=(.*)$", arg=arg, arg_semantics='format'):
                pass
            elif self._process_argument(regex=r"^-f=(.*)$", arg=arg, arg_semantics='format'):
                pass
            elif self._process_argument(regex=r"^--br$", arg=arg, arg_semantics='br', add_to_config=False):
                pass
            elif self._process_argument(regex=r"^-b$", arg=arg, arg_semantics='br', add_to_config=False):
                pass
            else:
                raise InvalidArgumentsException(message='Unknown argument ' + arg)

    def _process_argument(self, regex: str, arg: str, arg_semantics: str, add_to_config: bool = True) -> bool:
        """Try to process the argument.
        
        :param regex: Regex to match the argument.
        :param arg: Argument string.
        :param arg_semantics: Semantics of the argument. 
            This is used to check whether the argument with the same semantics was used twice - 
            support for short argument names, e.g. --help -> -h.
        :param add_to_config: Define, whether the argument has a value which should be added to the config.
            If false, the key 'arg_semantics' is added to the config with value of None.
        :return: bool True when the argument was processed, False otherwise.
        """
        input_match = re.search(regex, arg)
        if input_match:
            self._add_to_processed(arg_semantics=arg_semantics)

            try:
                self._config.values[arg_semantics] = input_match.group(1) if add_to_config else None
            except IndexError:
                raise InvalidArgumentsException(message="Invalid argument: " + arg)

            return True
        else:
            return False

    def _add_to_processed(self, arg_semantics: str) -> None:
        """Add to processes arguments and check whether the argument was already used.
        
        :raise InvalidArgumentsException When the argument was already used.
        """
        if arg_semantics in self._processed_arguments:
            raise InvalidArgumentsException(
                'Invalid parameters - cannot use the same parameter twice'
            )
        else:
            self._processed_arguments.append(arg_semantics)
