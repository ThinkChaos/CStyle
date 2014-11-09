from .base import is_empty
from .meta.logic import NOT, OR
from .meta.general import ends_with, keep_comments, matches
from .meta.wrapper import line


section = 'file'

rules = [
    ('80cols',
        matches(r'.{81,}', magic=False)),

    ('indentation',
        matches(r'^\s*?\t', magic=False)),

    ('terminate',
        line(-1, NOT(ends_with('\n', strip=False)))),

    ('dos',
        keep_comments(ends_with('\r\n', strip=False))),

    ('trailing',
        ends_with(' ', '\t')),

    ('spurious',
        OR(
            line(0, is_empty),
            line(-1, is_empty))),
]
