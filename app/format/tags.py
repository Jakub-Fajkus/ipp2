"""
    File name: tags.py
    Author: Jakub Fajkus
    Date created: 14.4.2017
    Date last modified: 17.4.2017
    Python Version: 3.6
"""

from app.regex.exceptions import InvalidRegexException
import re


class HtmlTag:
    """Base tag class. Defines the two instance properties."""

    def __init__(self, opening: str = '', closing: str = ''):
        self.opening = opening
        self.closing = closing


class BoldTag(HtmlTag):
    def __init__(self):
        super().__init__('<b>', '</b>')


class ItalicTag(HtmlTag):
    def __init__(self):
        super().__init__('<i>', '</i>')


class UnderlineTag(HtmlTag):
    def __init__(self):
        super().__init__('<u>', '</u>')


class TeletypeTag(HtmlTag):
    def __init__(self):
        super().__init__('<tt>', '</tt>')


class FontSizeTag(HtmlTag):
    def __init__(self, size: str):
        font_size = int(size)
        if font_size < 1 or font_size > 7:
            raise InvalidRegexException('The font size must be between 1 and 7 including')

        super().__init__('<font size={0}>'.format(font_size), '</font>')


class FontColorTag(HtmlTag):
    def __init__(self, color: str):
        if not re.match(r'[a-fA-F0-9]{6}', color):
            raise InvalidRegexException('The font color must consist of six hexadecimal letters')

        super().__init__('<font color=#{0}>'.format(color), '</font>')


class TagFactory:
    """Factory class for the tags."""

    @staticmethod
    def create(format_string: str):
        """Create and return a tag object according to the 'format' string.  
        
        :param format_string: String which defines the format.
            Supported format:
                - bold
                - intalic
                - underline
                - teletype
                - size:D, where D is a number from 1 to 7
                - color:XXXXXX, where X is any hexadecimal character
        :return: 
        """
        if format_string == 'bold':
            return BoldTag()
        elif format_string == 'italic':
            return ItalicTag()
        elif format_string == 'underline':
            return UnderlineTag()
        elif format_string == 'teletype':
            return TeletypeTag()
        else:
            match = re.match(r'size:([1-7])', format_string)
            if match:
                return FontSizeTag(match.groups()[0])

            match = re.match(r'color:([a-fA-F0-9]{6})', format_string)
            if match:
                return FontColorTag(match.groups()[0])

        raise InvalidRegexException('Invalid format:' + format_string)
