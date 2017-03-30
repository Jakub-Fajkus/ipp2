import re


class FormatFileParser:
    def __init__(self) -> None:
        pass

    def parse_formatting(self, formatting_string: str):
        pass
        # iterate over lines '\n'
        # for each line, separate the regex and the formatting
        for line in str.split(formatting_string, '\n'):
            print('Line length:', len(line))
            if len(line) == 0:
                print("SKIPPING EMPTY LINE")
                continue

            # the regex and the formatting is separeted by \t+
            # get the regex(before first '\t+'
            regex_match = re.match(r'^(.*?)\t+()', line)
            if regex_match:
                regex = regex_match.groups(0)
                print('Found regex:', regex[0])

                # line = line[regex.]
            else:
                print('No match for line: ', line)
                # todo: throw invalid format?!?!??!?!?


                # the formatting is a list of strings, separated by ',[SPACE\t]*'
                # todo: how to get the formatting strings? :D as in ipp1?
                # if re.search()
