from app.regex.exceptions import InvalidRegexException
import re


class HtmlTag:
    def __init__(self, opening: str = '', closing: str = ''):
        self.opening = opening
        self.closing = closing

    @staticmethod
    def create(formatting: str):
        if formatting == 'bold':
            return BoldTag()
        elif formatting == 'italic':
            return ItalicTag()
        elif formatting == 'underline':
            return UnderlineTag()
        elif formatting == 'teletype':
            return TeletypeTag()
        else:
            match = re.match(r'size:([1-7])', formatting)
            if match:
                return FontSizeTag(match.groups()[0])

            match = re.match(r'color:([a-fA-F0-9]{6})', formatting)
            if match:
                return FontColorTag(match.groups()[0])

        raise InvalidRegexException('Invalid formatting:' + formatting)


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
    def __init__(self, size: str):
        font_size = int(size)
        if font_size < 1 or font_size > 7:
            raise InvalidRegexException('The font size must be between 1 and 7 including')

        super().__init__(r'<font size={0}>'.format(font_size), r'</font>')


class FontColorTag(HtmlTag):
    def __init__(self, color: str):
        if not re.match(r'[a-fA-F0-9]{6}', color):
            raise InvalidRegexException('The font color must consist of six hexadecimal letters')

        super().__init__(r'<font color=#{0}>'.format(color), r'</font>')
