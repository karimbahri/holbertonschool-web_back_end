#!/usr/bin/env python3
"""100-safe_first_element.py"""


# The types of the elements of the input are not know
from typing import Any
from typing import Sequence
from typing import Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe_first_element: annotated function that return the first element
        of list if exist other wise return None
    """
    if lst:
        return lst[0]
    else:
        return None
