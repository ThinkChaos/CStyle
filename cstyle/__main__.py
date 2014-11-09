# Warning: This code warrants a rewrite

from __future__ import print_function
from re import compile
from sys import argv

import os.path

try:
    # python /path/to/cstyle
    from rules import RULES
except ImportError:
    # python -m cstyle
    from .rules import RULES


_COMMENT_PATTERN = compile(r'^\s*(//|/\*.*\*/)')
_BLOCK_BEG_PATTERN = compile(r'^\s*/\*\*?')
_BLOCK_END_PATTERN = compile(r'^\s*\*/')


def check(info, rules):
    """Generate `info` `dict` instances for every *rule*.

    The generated `dict` instances have the following keys:
        - `filename`: path to file as received by the program
        - `all_lines`: list of lines from the examined file
        - `nall_lines`: length of `all_lines`
        - `lines`: list of `(lineno, line)` tuples from the examined file
        - `nlines`: length of `lines`
        - `section`: name of the rule category being checked
        - `rule`: name of the rule being checked, can be `None`
        - `wrong_lines`: list of line numbers corresponding to those that
                didn't obey the current rule

    Rules do not have access to `wrong_lines`.
    Rules have access to the following extra keys:
        - `lineno`: current line number
        - `line_index`: index of current line in `lines`
        - `line_prev`: the previous `line` `str`, `None` when checking first
                non comment line
    """
    info['lines'] = list(skip_comments(info['all_lines']))
    info['nlines'] = len(info['lines'])
    for section, sec_rules in rules:
        info['section'] = section
        for name, rule in sec_rules:
            info['rule'] = name
            info['line_prev'] = None
            wrong_lines = []
            if hasattr(rule, '_keep_comments'):
                for lineno, line in enumerate(lines):
                    info['line_index'] = lineno
                    info['lineno'] = lineno
                    if rule(line, info):
                        wrong_lines.append(lineno)
                    info['line_prev'] = line
            else:
                for i, (lineno, line) in enumerate(info['lines']):
                    info['line_index'] = i
                    info['lineno'] = lineno
                    if rule(line, info):
                        wrong_lines.append(lineno)
                    info['line_prev'] = line

            info['wrong_lines'] = wrong_lines
            info.pop('lineno')
            info.pop('line_prev')
            yield info
            info.pop('wrong_lines')


def skip_comments(lines):
    """Skip indexes of comments in `lines`."""
    is_block = False
    for i, line in enumerate(lines):
        if _COMMENT_PATTERN.match(line):
            continue

        if is_block:
            if _BLOCK_END_PATTERN.match(line):
                is_block = False
        elif _BLOCK_BEG_PATTERN.match(line):
            is_block = True
        else:
            yield (i, line)


def format_wrong_lines(wrong_lines, nlines):
    """ Translate `int`s to `str` of comma seperated `int`s and ranges."""
    prev, r_beg, ranges = wrong_lines[0], wrong_lines[0], []

    for lineno in wrong_lines[1:] + [-1]:  # Consume last elenent
        if lineno != prev + 1:
            if prev != r_beg:
                ranges.append('%d-%d' % (r_beg + 1, prev + 1))
            else:
                ranges.append(str(prev + 1))
            r_beg = lineno
        prev = lineno

    return 'ALL' if ranges[0] == '1-%d' % nlines else ', '.join(ranges)


def print_results(check_results):
    """Format `check_results` in a human readable way."""
    once = True
    for info in check_results:
        if info['wrong_lines']:
            if once:
                once = False
                print(info['filename'] + ':')

            print('  {}{}: {}'.format(
                info['section'],
                '.' + info['rule'] if info['rule'] is not None else '',
                format_wrong_lines(info['wrong_lines'], info['nlines'])
            ))

    if once:
        print(info['filename'] + ': OK')


for filename in argv[1:]:
    filepath = os.path.expanduser(os.path.expandvars(filename))

    if not os.path.isfile(filepath):
        print(filename + ': ERROR - Not a file')
        continue

    # Open without newline translation
    with open(filepath, newline='') as f:
        lines = f.readlines()

    info = {
        'filename': filename,
        'all_lines': lines,
        'nall_lines': len(lines)
    }
    print_results(check(info, RULES))
