import sys
from app import App
from app.io.Input import Input
from app.arguments import ArgumentsParser, Config
from app.arguments.exceptions.InvalidArgumentsException import InvalidArgumentsException

config = Config.Config()
argParser = ArgumentsParser.ArgumentsParser()
app = App.App(config)

try:
    argParser.parse_arguments(config=config)
    app.run()
except InvalidArgumentsException as error:
    with open(sys.stderr, 'r') as f:
        f.write(error.message)

    sys.exit(error.code)

sys.exit(0)
