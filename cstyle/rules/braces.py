from .base import indented, is_empty, unindented
from .meta.general import equals, ends_with, indented_by, matches, starts_with
from .meta.logic import AND, NOT, OR
from .meta.wrapper import next_line, not_line, prev_line, shift_line


section = 'braces'

rules = [
    (None,
        # Checking } would cause too many false positives
        matches(r'(else|enum|for|if|struct|switch|union|while).*{$')),

    ('open',
        # Check line 0 before indent: we don't want to return True on line 0:
        # NOT(indented_by()(line 0)) is True
        AND(equals('{'), not_line(0, NOT(indented_by(0, 2))))),

    ('indent',
        # Only checks first and last line of block
        OR(
            AND(
                AND(prev_line(ends_with('{')), NOT(starts_with('}'))),
                NOT(indented)),
            AND(
                AND(prev_line(NOT(OR(is_empty, ends_with('{')))), starts_with('}')),
                NOT(unindented)))),

    ('dowhile',
        AND(equals('do'), next_line(starts_with('{')))),

    ('useless',
        AND(
            shift_line(-2, starts_with('else', 'for', 'if', 'while')),
            AND(prev_line(ends_with('{')), next_line(starts_with('}'))))),
]
