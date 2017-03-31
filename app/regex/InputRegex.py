from app.regex.exceptions.InvalidRegexException import InvalidRegexException
import re
import string


class InputRegex():
    """representing the input regex from the file
    
    each file has 1 regex per line 
    """
    allowed_special_expressions = {
        '%s': r'(\s)',
        '%a': r'(.)',
        '%d': r'([0-9])',
        '%l': r'([a-z])',
        '%L': r'([A-Z])',
        '%w': r'([a-zA-Z])',
        '%W': r'([a-zA-Z0-9])',
        '%t': r'(\t)',
        '%n': r'(\n)',
        '%.': r'(\.)',
        '%|': r'(|)',
        '%!': r'(!)',
        '%*': r'(\*)',
        '%+': r'(\+)',
        '%(': r'(\()',
        '%)': r'(\))',
        '%%': r'(%)',
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

        #  todo: add parentesis?
        pass

    def _validate(self):
        """go through the regex and try to determine whether it has the right format"""
    #     todo! validate the regex..

        match = re.search(r'\.{2,}', self.python_regex)
        if match:
            raise InvalidRegexException('Regex can not contain A..+A')

        self.python_regex = re.sub(r'\.', '', self.python_regex)

        self.python_regex = re.sub(r'!%.', repl=r'', string=self.python_regex)



    def _convert_special_expressions(self):
        """convert the special regular expressions"""

        # get all special regexes (char % and another char)
        specials = re.findall(r'(%.)', self.python_regex)


        for special in specials:
            print(special)
            if special not in self.allowed_special_expressions:
                raise InvalidRegexException('Invalid special expression: ' + special)
            else:
                # replace the special character for it's python representation in the output regex
                # todo: negate!?
                self.python_regex = self.python_regex.replace(special, self.allowed_special_expressions[special])
