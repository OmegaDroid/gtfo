import random
from django import template

register = template.Library()


def _lower_and_upper(a, b):
    a = a or 0

    if a and not b:
        b = 0
    elif not (a or b):
        b = 1

    return min(a, b), max(a, b)


@register.simple_tag()
def rand_float(a=None, b=None):
    lower, upper = _lower_and_upper(a, b)
    return lower + (upper - lower) * random.random()


@register.simple_tag()
def rand_int(a=None, b=None):
    return random.randint(*_lower_and_upper(a, b))


@register.simple_tag()
def rand_from(*args):
    if not args:
        raise ValueError("At least one argument must be given to chose from")

    return random.choice(args)
