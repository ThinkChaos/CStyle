from .meta.logic import OR
from .meta.general import matches, starts_with_rgx


section = 'keyword'

rules = [
    (None,
        OR(
            starts_with_rgx(r'(for|if|switch|while)(\s{2,})?\('),
            starts_with_rgx(r'(break|continue)\s+;$'))),

    ('return',
        matches(r'return (\(.*\);|[^\(;]*)')),

    ('goto',
        matches(r'goto [^\s;]+;')),
]
