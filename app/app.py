"""
    File name: app.py
    Author: Jakub Fajkus
    Date created: 14.4.2017
    Date last modified: 18.4.2017
    Python Version: 3.6
"""

from app.arguments.arguments import Config
from app.formatting.formatting import Formatter
from app.io.io import Input
from app.io.io import Output
from app.regex.regex import FormatFileParser
import re


class App:
    """Represents the application itself."""
    def __init__(self, config: Config):
        self._config = config

    def run(self):
        """The starting point of the application."""
        self._config.validate()

        if 'help' in self._config.values:
            self.print_help()
            return

        input_object = Input(config=self._config)
        format_parser = FormatFileParser()
        input_string = input_object.get_input()

        formatting_table = input_object.get_format_table()
        if not formatting_table:
            self.present_output(input_string)

            return

        formatting_table = format_parser.parse_formatting(formatting_table)
        replacer = Formatter(input_string, formatting_table)
        output_string = replacer.format()

        self.present_output(output_string)

    def print_help(self):
        self.present_output("""
        The arguments supported(with abbreviation):
            - input(i)
            - output(o)
            - help(h)
            - format(f)
            - br(b)"""
                            )

    def present_output(self, output_string: str):
        """Write output to the desired destination."""
        output = Output(config=self._config)

        # add br to each line
        if self._config.add_br():
            output.present_output(re.sub(r'\n', '<br />\n', string=output_string))
        else:
            output.present_output(output_string)
