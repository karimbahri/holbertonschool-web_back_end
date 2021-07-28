#!/usr/bin/env python3
"""0-simple_helper_function.py"""
import typing


def index_range(page, page_size) -> typing.Tuple:
    """index_range:
    function that takes page and page_size
    as arguments and returns a tuple containing
    start index and stop index corresponding to range
    of index
    """
    crr_page = (page - 1) * page_size
    return crr_page, crr_page + page_size
