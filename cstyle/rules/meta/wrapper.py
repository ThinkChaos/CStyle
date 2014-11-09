"""*Meta rules* that wrap rules."""


def line(n, rule):
    """Apply rule to `n`th `line` only."""
    return lambda l, i: (
        i['lineno'] == (n if n >= 0 else i['nlines'] + n) and rule(l, i)
    )


def not_line(n, rule):
    """Apply rule to all but `n`th `line`."""
    return lambda l, i: (
        i['lineno'] != (n if n >= 0 else i['nlines'] + n) and rule(l, i)
    )


def shift_line(n, rule, skip_comments=True):
    """Move by `n` lines in file. No-op when moving out of bounds."""
    def wrap(line, info):
        old_index = info['line_index']
        new_index = old_index + n

        if 0 <= new_index < info['nlines']:
            new_lineno, new_line = info['lines'][new_index]
            info['line_index'] = new_index
            old_lineno, info['lineno'] = info['lineno'], new_lineno
            res = rule(new_line, info)
            info['lineno'], info['line_index'] = old_lineno, old_index
            return res
        return False

    return wrap


def next_line(rule):
    """Apply `rule` to next line of the file. No-op on last line."""
    return shift_line(1, rule)


def prev_line(rule):
    """Apply `rule` to previous line of the file. No-op on first line."""
    return shift_line(-1, rule)
