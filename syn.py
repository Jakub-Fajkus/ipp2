import sys
from app import App
from app.io.Input import Input
from app.arguments import ArgumentsParser, Config
from app.arguments.exceptions.InvalidArgumentsException import InvalidArgumentsException
from app.regex.InputRegex import InputRegex

config = Config.Config()
argParser = ArgumentsParser.ArgumentsParser()
app = App.App(config)

regex = InputRegex(input_regex='%s %a %d %l %L%w%W%t%n%|%!%*%+ %(%) %%')
regex.convert_to_python_regex()

try:
    argParser.parse_arguments(config=config)
    app.run()
except InvalidArgumentsException as error:
    with open(sys.stderr, 'r') as f:
        f.write(error.message)

    sys.exit(error.code)

sys.exit(0)
