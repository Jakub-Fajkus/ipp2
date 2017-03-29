from app.arguments.exceptions.InvalidArgumentsException import InvalidArgumentsException


class Config():
    def __init__(self):
        self.values = {}

    def validate(self):
        """validate the configuration"""
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
