from app.arguments.arguments import Config
from app.replacing.replacing import Replacer
from app.io.io import Input
from app.io.io import Output
from app.regex.regex import FormatFileParser
import re


class App:
    def __init__(self, config: Config):
        self._config = config

    def run(self):
        self._config.validate()

        if 'help' in self._config.values:
            self.print_help()
            return

        input_object = Input(config=self._config)
        format_parser = FormatFileParser()
        input_string = input_object.get_input()

        formatting = input_object.get_format_table()
        if not formatting:
            self.present_output(input_string)

            return

        formatting = format_parser.parse_formatting(formatting)
        replacer = Replacer(input_string, formatting)
        output_string = replacer.replace_all()

        self.present_output(output_string)

    @staticmethod
    def print_help():
        # todo: print help!
        print("Printing some help...\nHELP!!!!\nHELP MEEEE!\nI am drowning in a pool!\n...")

    def present_output(self, output_string: str):
        output = Output(config=self._config)

        # add br to each line
        if self._config.add_br():
            output.present_output(re.sub(r'\n', '<br />\n', string=output_string))
        else:
            output.present_output(output_string)
