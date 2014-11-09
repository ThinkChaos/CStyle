"""General *meta rules*, all goes."""

from re import compile

from .logic import NOT
from .wrapper import not_line


_INDENT_PTRN = compile(r'^( +)?\S')


# Helpers

def _first_non_space(s):
    """Find the position of the first non-space character in the given string.

    Position ranges from `1` to `len(s)`. When there is no non-space character,
    it is `0`.
    """
    m = _INDENT_PTRN.match(s)
    return m.end() if m is not None else 0


def _indent_diff(l, i):
    """The indent difference compared to the previous line."""
    return _first_non_space(l) - _first_non_space(i['line_prev'] or '')


# Meta Rules

def equals(s, strip=True):
    """Check if `line` (ignoring surrounding whitespace) is equal to `s`."""
    return lambda l, _: (l.strip() if strip else l) == s


def ends_with(*s, strip=True):
    """Check if `line` (skipping newline characters) ends with one of s."""
    s = tuple(s)
    return lambda l, _: (l.rstrip('\r\n') if strip else l).endswith(s)


def indented_by(*n):
    """Check if `line` is indented by one of `n` compared to the previous one.

    No-op on first line."""
    return not_line(0, lambda l, i: _indent_diff(l, i) in n)


def keep_comments(rule):
    """Mark `rule` to operate even on comment lines."""
    rule._keep_comments = True
    return rule


def matches(regex, magic=True):
    """Check if `line` matches `regex`.

    `magic` toggles formatting `regex` into `r'^ *?(%s)$'.`
    """
    pattern = compile(r'^ *?(%s)$' % regex if magic else regex)
    return lambda l, _: pattern.search(l) is not None


def doesnt_match(regex):
    """Opposite of `matches`."""
    return NOT(matches(regex))


def starts_with(*s, strip=True):
    """Check if `line` (skipping spaces) starts with one of s."""
    s = tuple(s)
    return lambda l, _: (l.lstrip(' ') if strip else l).startswith(s)


def starts_with_rgx(regex, strip=True):
    """Check if `line` (skipping spaces) starts with one of s."""
    pattern = compile(r'^ *(%s)' % regex if strip else regex)
    return lambda l, _: pattern.match(l) is not None
