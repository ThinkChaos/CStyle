from .meta.logic import OR
from .meta.general import matches

section = 'exp'


#from re import escape
#bin_tern_ops = '|'.join(escape(op) for op in [
#    '=',  '==',
#    '!',  '!=',
#    '>',  '>=',
#    '<',  '<=',
#    '+',  '+=',
#    '-',  '-=',
#          '*=',  # Don't fail for pointers
#    '/',  '/=',
#    '%',  '%=',
#          '&=',  # address
#    '|',  '|=',
#    '^',  '^=',
#    '<<', '<<=',
#    '>>', '>>=',
#    '&&',
#    '||',
#    '?'
#])


rules = [
    #('padding',
    #    # I couldn't write a satisfying regex -> disabled
    #    ANY(
    #        #matches(r'^\S+( {2,})?(%s) ?[^+-]\S*' % bin_tern_ops),
    #        #matches(r'[^\s+-]+ ?(%s)( {2,})?[^ ]\S*' % bin_tern_ops),
    #        matches(r'.*?[^ +-]( {2,})?(%s)( |[^+-=]).*' % bin_tern_ops),
    #        #matches(r'.*?[^ +-](%s)( {2,})?[^ +-=].*' % bin_tern_ops),
    #        #matches(r'.*[^ +-](%s)[^ +-=]' % bin_tern_ops),
    #        )),

    ('nopadding',
        OR(
            matches(r'.*\S +(\.|->) ?\S.*'),
            matches(r'.*\S ?(\.|->) +\S.*')))
]
