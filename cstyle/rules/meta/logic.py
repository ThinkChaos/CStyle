"""*Meta rules* handling logical operations."""


def AND(r, s):
    """Apply logical and to rules."""
    return lambda l, i: r(l, i) and s(l, i)


def ANY(*R):
    """Apply logical and to rules."""
    return lambda l, i: any(r(l, i) for r in R)


def OR(r, s):
    """Apply logical or to rules."""
    return lambda l, i: r(l, i) or s(l, i)


def NOT(r):
    """Apply logical not to rule."""
    return lambda l, i: not r(l, i)
