import sys
from app import App
from app.io.Input import Input
from app.arguments import ArgumentsParser, Config
from app.arguments.exceptions.InvalidArgumentsException import InvalidArgumentsException
from app.io.exceptions.InputFileException import InputFileException
from app.io.exceptions.OutputFileException import OutputFileException
from app.regex.FormatFileParser import FormatFileParser

config = Config.Config()
argParser = ArgumentsParser.ArgumentsParser()
app = App.App(config)

# regex = InputRegex(input_regex='%s %a %d %l %L%w%W%t%n%|%!%*%+ %(%) %%')
# regex2 = InputRegex(input_regex=r'mame zere %Wmaso %!')
# regex.convert_to_python_regex()
# regex2.convert_to_python_regex()

parser = FormatFileParser()
parser.parse_formatting("""a	bold
b	italic 
ccd		underline, 	 bold
d	teletype
e	size:1
f	size:7
g	color:000000
h	color:FFFFFF
""")

try:
    argParser.parse_arguments(config=config)
    app.run()
except (InvalidArgumentsException, InputFileException, OutputFileException) as error:
    print("********************************syn.py here, caught an exception:********************************",
          file=sys.stderr)
    print(error.message, file=sys.stderr)

    sys.exit(error.code)
except:
    print("********************************syn.py here, caught an UNKNOWN exception:********************************",
          file=sys.stderr)
    raise

    sys.exit(100)

sys.exit(0)
