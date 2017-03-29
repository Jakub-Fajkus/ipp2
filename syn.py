import sys
from app.arguments import ArgumentsParser, Config
from app.arguments.exceptions.InvalidArgumentsException import InvalidArgumentsException

config = Config.Config()
argParser = ArgumentsParser.ArgumentsParser()

try:
    argParser.parseArguments(config=config)
except InvalidArgumentsException as error:
    with open(sys.stderr, 'r') as f:
        f.write(error.message)

    sys.exit(error.code)