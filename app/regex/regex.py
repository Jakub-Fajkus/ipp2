"""
    File name: regex.py
    Author: Jakub Fajkus
    Date created: 14.4.2017
    Date last modified: 17.4.2017
    Python Version: 3.6
"""

import re
from app.format.tags import TagFactory
from app.regex.exceptions import InvalidRegexException


class FormatFileParser:
    """Parses the content of the formatting file and represents it as a set of tags and regular expressions."""
    def parse_formatting(self, formatting_string: str):
        # iterate over lines '\n'
        # for each line, separate the regex and the formatting
        formattings = []

        tuple_number = 0

        for line in str.split(formatting_string, '\n'):
            if len(line) == 0:
                continue

            # the regex and the formatting is separeted by \t+
            # get the regex(before first '\t+'
            regex_match = re.match(r'^(.*?)(\t+)(.*$)', line)
            if regex_match:
                regex_var = regex_match.groups()[0]
                regex_object = InputRegex(regex_var)
                regex_object.convert_to_python_regex()

                tags = []
                # the formatting is a list of strings, separated by ',[SPACE\t]*'
                for formatting_var in regex_match.groups()[2].split(','):  # get the 3rd group and split it by ','

                    if not formatting_var:
                        raise InvalidRegexException('Empty formatting on line: ' + line)

                    tags.append(TagFactory.create(formatting_var.strip()))

                formattings.append((regex_object, tags, tuple_number))
                tuple_number += 1

            else:
                raise InvalidRegexException('No match found for line' + line)

        return formattings


class InputRegex:
    """Represents the input regex from the file.

    Each file has 1 regex per line. 
    """
    allowed_special_expressions = {
        '%s': r'([{0}\s])',
        '%a': r'({0}.)',
        '%d': r'([{0}0-9])',
        '%l': r'([{0}a-z])',
        '%L': r'([{0}A-Z])',
        '%w': r'([{0}a-zA-Z])',
        '%W': r'([{0}a-zA-Z0-9])',
        '%t': r'([{0}\t])',
        '%n': r'([{0}\n])',
        '%.': r'([{0}.])',
        '%|': r'([{0}|])',
        '%!': r'([{0}!])',
        '%*': r'([{0}*])',
        '%+': r'([{0}+])',
        '%(': r'([{0}(])',
        '%)': r'([{0})])',
        '%%': r'([{0}%])',
    }

    def __init__(self, input_regex: str):
        self.input_regex: str = input_regex
        self.python_regex: str = input_regex

    def convert_to_python_regex(self):
        """Convert the input_regex into the python's regex.

        :raises InvalidRegexException When the regex contains invalid or unsupported characters and constructs.
        """
        self._validate()

        self._convert_special_expressions()

        self.negate_non_special_characters()

        pass

    def _validate(self):
        """Go through the regex and try to determine whether it has the right format."""

        match = re.search(r'\.{2,}', self.python_regex)
        if match:
            raise InvalidRegexException('Regex can not contain A.(.+)A')

    def _convert_special_expressions(self):
        """Convert the special regular expressions into classical python regular expressions"""

        self.python_regex = re.sub(r'(?<!%)\.', '', self.python_regex)  # negative lookbehind

        # escape special characters
        self.python_regex = re.sub(r'([\\?\[^\]${\}<>\-])', r'\\\1', self.python_regex)

        # get all special regexes (char % and another char)
        for special in re.finditer(r'(%.)', self.python_regex):
            # print(special)
            if special.groups()[0] not in self.allowed_special_expressions:
                raise InvalidRegexException('Invalid special expression: ' + special.groups()[0])
            else:
                # replace the special character for it's python representation in the output regex

                # check for pos and endpos of the special - look, if there is a ! before
                new_regex = self.allowed_special_expressions[special.groups()[0]]
                if special.start() != 0 and special.string[special.start() - 1:special.start()] == '!':

                    # negate the group
                    new_regex = new_regex.format('^')
                    self.python_regex = self.python_regex.replace(special.groups()[0], new_regex)
                    self.python_regex = self.python_regex.replace('!' + new_regex, new_regex)

                else:
                    new_regex = new_regex.format('')
                    self.python_regex = self.python_regex.replace(special.groups()[0], new_regex)

    def negate_non_special_characters(self):
        """Find all '!' no preceeding and no succeeding '%' ."""
        self.python_regex = re.sub(r'(?<!%\[)!([^%\]])', r'[^\1]', self.python_regex)
