from unittest import TestCase

from cstyle.rules import RULES


RULES_DICT = {s: dict(r) for s, r in RULES}


def get_rules(cls):
    """`RuleTest` decorator to inject section name."""
    cls.section = cls.__name__.lower()
    cls.rules_dict = RULES_DICT.get(cls.section, {})
    return cls


class RuleTest(TestCase):

    """Base class to test rule definitions."""

    def get_test_rule(self, name):
        """ Return rule with name. Section is implied."""
        if name not in self.rules_dict:
            raise ValueError('Rule not found: %s.%s' % (self.section, name))

        rule = self.rules_dict[name]

        def wrap(*lines, lineno=0):
            nlines = len(lines)
            lineno = lineno if lineno >= 0 else nlines + lineno
            return rule(lines[lineno], {
                'lines': list(zip(range(nlines), lines)),
                'nlines': nlines,
                'lineno': lineno,
                'line_index': lineno,
                'line_prev': lines[lineno - 1] if lineno > 0 else None
            })

        return wrap
