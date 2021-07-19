#!/usr/bin/env python3
"""6-sum_mixed_list.py"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """sum_mixed_list: function that return the sum of a list
        it takes as arguments a list of integer and float
        return the sum of the list typed as float
    """
    return sum(mxd_lst)
