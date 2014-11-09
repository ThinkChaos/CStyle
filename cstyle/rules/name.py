from .meta.logic import OR
from .meta.general import matches


section = 'name'

rules = [
    ('reserved',
        OR(
            matches(r'\S+ _\S+ = \S+.*'),
            matches(r'#define +_\S+ +\S+.*')))
]
