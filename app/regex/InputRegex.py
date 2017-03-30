from app.regex.exceptions.InvalidRegexException import InvalidRegexException
import re
import string


class InputRegex():
    """representing the input regex from the file
    
    each file has 1 regex per line 
    """
    allowed_special_expressions = {
        '%s': r'([\t\n\r\f\v])',
        '%a': r'(.)',
        '%d': r'([0-9])',
        '%l': r'([a-z])',
        '%L': r'([A-Z])',
        '%w': r'([a-zA-Z])',
        '%W': r'([a-zA-Z0-9])',
        '%t': r'(\t)',
        '%n': r'(\n)',
        '%.': r'(\.)',
        '%|': r'(\|)',
        '%!': r'(!)',
        '%*': r'(\*)',
        '%+': r'(\+)',
        '%(': r'(\()',
        '%)': r'(\))',
        '%%': r'(%)',
    }

    def __init__(self, input_regex: str):
        self.input_regex: str = input_regex
        self.python_regex = ''

    def convert_to_python_regex(self):
        """convert the input_regex into the python's regex
            
            :raises InvalidRegexException
        """

        # convert the special regular expressions
        # get all special regexes (char % and another char)
        specials = re.findall(r'(%.)', self.input_regex)

        for special in specials:
            print(special)
            if special not in self.allowed_special_expressions:
                raise InvalidRegexException('Invalid special expression: ' + special)
            else:
                self.input_regex = self.input_regex.replace(special, self.allowed_special_expressions[special])

        print(self.input_regex)