"""Provides abstraction level to translate a style rule into a *rule*.

A *rule* is a function with two parameters: `line` and `info` as defined in
`__main__.py`. It's result is a `bool` indicating whether the `line` did not
follow the *rule*, as it is generally easier to express which lines are invalid
than the other way around.
"""

from . import braces, exp, file, keyword, name


RULES = [
    (mod.section, mod.rules) for mod in (name, file, braces, keyword, exp)
]
