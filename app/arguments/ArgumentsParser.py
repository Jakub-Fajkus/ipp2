import re
import sys

from app.arguments.Config import Config
from app.arguments.exceptions import InvalidArgumentsException


class ArgumentsParser:
    def __init__(self):
        self._processed_arguments = []
        self._config = None

    def parse_arguments(self, config: Config) -> None:
        """
            Fill the config with some configuration form the command line.
        :param config: Config object which will be filled.
        :raise InvalidArgumentsException when an argument is not know.
        """
        self._config = config

        for arg in sys.argv[1:]:  # skip the script path
            # print(arg)

            if self._process_argument(r"^--input=(.*)$", arg, 'input'):
                pass
            elif self._process_argument(r"^-i=(.*)$", arg, 'input'):
                pass
            elif self._process_argument(r"^--output=(.*)$", arg, 'output'):
                pass
            elif self._process_argument(r"^-o=(.*)$", arg, 'output'):
                pass
            elif self._process_argument(r"^--help$", arg, 'help', False):
                pass
            elif self._process_argument(r"^-h$", arg, 'help', False):
                pass
            elif self._process_argument(r"^--format=(.*)$", arg, 'format'):
                pass
            elif self._process_argument(r"^-f=(.*)$", arg, 'format'):
                pass
            elif self._process_argument(r"^--br$", arg, 'br', False):
                pass
            elif self._process_argument(r"^-b$", arg, 'br', False):
                pass
            else:
                raise InvalidArgumentsException.InvalidArgumentsException('Unknown argument ' + arg)

    def _process_argument(self, regex: str, arg: str, arg_semantics: str, add_to_config: bool = True) -> bool:
        """
            Try to process the argument
        :param regex: Regex to match the argument
        :param arg: Argument string
        :param arg_semantics: Semantics of the argument. 
            This is used to check whether the argument with the same semantics was used twice - 
            support for short argument names, e.g. --help -> -h
        :param add_to_config: Define, whether the argument has a value which should be added to the config.
            If false, the key 'arg_semantics' is added to the config with value of None.
        :return: 
        """
        input_match = re.search(regex, arg)
        if input_match:
            self._add_to_processed(arg_semantics)

            try:
                self._config.values[arg_semantics] = input_match.group(1) if add_to_config else None
            except IndexError:
                raise InvalidArgumentsException.InvalidArgumentsException("Invalid argument: " + arg)

            return True
        else:
            return False

    def _add_to_processed(self, arg_semantics: str):
        """add to processes arguments and check whether the argument was already used
            :raise InvalidArgumentsException When the argument was already used.
        """
        if arg_semantics in self._processed_arguments:
            raise InvalidArgumentsException.InvalidArgumentsException(
                'Invalid parameters - cannot use the same parameter twice'
            )
        else:
            self._processed_arguments.append(arg_semantics)
