import sys
from app.arguments.arguments import ArgumentsParser, Config
from app.arguments.exceptions import InvalidArgumentsException
from app.io.exceptions import InputFileException, OutputFileException
from app.regex.exceptions import InvalidRegexException
from app.app import App

config = Config()
argParser = ArgumentsParser()
app = App(config)


try:
    argParser.parse_arguments(config=config)
    app.run()
except (InvalidArgumentsException, InputFileException, OutputFileException, InvalidRegexException) as error:
    print("********************************syn.py here, caught an exception:********************************",
          file=sys.stderr)
    print(error.message, file=sys.stderr)

    sys.exit(error.code)
except:
    print("********************************syn.py here, caught an UNKNOWN exception:********************************",
          file=sys.stderr)

    sys.exit(100)

sys.exit(0)
