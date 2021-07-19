#!/usr/bin/env python3
"""101-safely_get_value.py"""
from typing import Any
from typing import TypeVar
from typing import Mapping
from typing import Union


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('T'), None]) -> Union[Any, TypeVar('T')]:
    """return element of dict by key if exist
        otherwise return default
    """
    if key in dct:
        return dct[key]
    else:
        return default
