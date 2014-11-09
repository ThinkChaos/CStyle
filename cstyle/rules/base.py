"""Basic *rules* used as building blocks for other *rules*."""

from .meta.general import indented_by


_indented = indented_by(2, 4)
_unindented = indented_by(-2, -4)


def indented(l, i):
    """Check if line is indented compared to the previous one."""
    return _indented(l, i)


def unindented(l, i):
    """Check if line is unindented compared to the previous one."""
    return _unindented(l, i)


def is_empty(l, _):
    """Check if line is the empty string or a newline."""
    return l in '\n'
