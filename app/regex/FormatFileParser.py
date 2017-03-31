import re
from app.format.tags import HtmlTag
from app.regex.InputRegex import InputRegex
from app.regex.exceptions.InvalidRegexException import InvalidRegexException


class FormatFileParser:
    def __init__(self) -> None:
        pass

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
                regex = regex_match.groups()[0]
                regex_object = InputRegex(regex)
                regex_object.convert_to_python_regex()
                # print("Regex:", regex)

                tags = []
                # the formatting is a list of strings, separated by ',[SPACE\t]*'
                for formatting in regex_match.groups()[2].split(','):  # get the 3rd group and split it by ','
                    # print(formatting)
                    # print(formatting.strip())

                    if not formatting:
                        raise InvalidRegexException('Empty formatting on line: ' + line)

                    tags.append(HtmlTag.create(formatting.strip()))

                formattings.append((regex_object, tags, tuple_number))
                tuple_number += 1

            else:
                raise InvalidRegexException('No match found for line' + line)

        return formattings
