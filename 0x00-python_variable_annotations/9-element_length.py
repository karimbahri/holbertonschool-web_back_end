#!/usr/bin/env python3
"""9-element_length.py"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
                    typing.List[typing.Tuple[typing.Sequence, int]]:
    """element_length: return length of each item in lst"""
    return [(i, len(i)) for i in lst]
