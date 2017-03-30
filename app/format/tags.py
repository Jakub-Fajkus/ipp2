from app.regex.exceptions.InvalidRegexException import InvalidRegexException
import re


class HtmlTag:
    def __init__(self, opening: str = '', closing: str = ''):
        self.opening = opening
        self.closing = closing


class BoldTag(HtmlTag):
    def __init__(self):
        super().__init__(r'<b>', r'</b>')


class ItalicTag(HtmlTag):
    def __init__(self):
        super().__init__(r'<i>', r'</i>')


class UnderlineTag(HtmlTag):
    def __init__(self):
        super().__init__(r'<u>', r'</u>')


class TeletypeTag(HtmlTag):
    def __init__(self):
        super().__init__(r'<tt>', r'</tt>')


class FontSizeTag(HtmlTag):
    def __init__(self, size: int):
        if size < 1 or size > 7:
            raise InvalidRegexException('The font size must be between 1 and 7 including')

        super().__init__(r'<font size={1}>', r'</font>'.format(size))


class FontColorTag(HtmlTag):
    def __init__(self, color):
        if not re.match(r'[a-fA-F0-9]{6}', color):
            raise InvalidRegexException('The font color must consist of six hexadecimal letters')

        super().__init__(r'<font color=#{1}>', r'</font>'.format(color))
