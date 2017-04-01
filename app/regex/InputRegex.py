from app.regex.exceptions.InvalidRegexException import InvalidRegexException
import re
import string


class InputRegex():
    """representing the input regex from the file
    
    each file has 1 regex per line 
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
        """convert the input_regex into the python's regex
            
            :raises InvalidRegexException
        """

        self._validate()

        self._convert_special_expressions()

        self.negate_non_special_characters()

        #  todo: add parentesis?
        pass

    def _validate(self):
        """go through the regex and try to determine whether it has the right format"""
        #     todo! validate the regex..

        match = re.search(r'\.{2,}', self.python_regex)
        if match:
            raise InvalidRegexException('Regex can not contain A.(.+)A')
        # self.python_regex = re.escape(self.python_regex)

        # self.python_regex = re.sub(r'\.', '', self.python_regex)
        # remove dot which is not after percent sign
        self.python_regex = re.sub(r'(?<!%)\.', '', self.python_regex)  # negative lookbehind

        # substitude common regex symbols
        # escape
        # self._escape(r'({.*?})')  # a{3}
        # self._escape(r'(\[.*?\])')  # [...]
        # self.python_regex = self.python_regex.replace('^', '\^')  # ^test$
        # self.python_regex = self.python_regex.replace('$', '\$')  #
        # self.python_regex = self.python_regex.replace('?', '\?')  #
        # self.python_regex = self.python_regex.replace('{', '\{')  #
        # self.python_regex = self.python_regex.replace('}', '\}')  #
        # self.python_regex = self.python_regex.replace('[', '\[')  #
        # self.python_regex = self.python_regex.replace(']', '\]')  #
        # self.python_regex = self.python_regex.replace(r"\n", r"\\n")  #
        self.python_regex = re.sub(r'([\\\?\[\^\]\$\{\}\<\>\-])', r'\\\1', self.python_regex)

        pass
        # self.python_regex = re.sub(r'!%.', repl=r'', string=self.python_regex)

    def _convert_special_expressions(self):
        """convert the special regular expressions"""

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
                    # print("found negated special! HAH!")
                    # negate the group
                    # todo: this will not with !%a

                    new_regex = new_regex.format('^')
                    self.python_regex = self.python_regex.replace(special.groups()[0], new_regex)
                    self.python_regex = self.python_regex.replace('!' + new_regex, new_regex)

                    # print("new:", new_regex)
                else:
                    new_regex = new_regex.format('')
                    self.python_regex = self.python_regex.replace(special.groups()[0], new_regex)

                    # print(self.python_regex)

    def _escape(self, input_regex: str):
        finds = re.findall(input_regex, self.python_regex)
        for find in finds:
            self.python_regex = self.python_regex.replace(find, re.escape(find))

    def negate_non_special_characters(self):
        # [ ^ %]![ ^ %]

        # find all ! - no preceeding and no succeeding %
        self.python_regex = re.sub(r'(?<!%\[)!([^%\]])', r'[^\1]', self.python_regex)
