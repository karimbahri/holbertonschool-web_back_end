#!/usr/bin/env python3
"""8-make_multiplier.py"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier : a function that takes
        multiplier (typed float) as arg
        and return a function that multiply multiplier by a float
    """
    def multiply(mlt: float):
        return mlt * multiplier
    return multiply
