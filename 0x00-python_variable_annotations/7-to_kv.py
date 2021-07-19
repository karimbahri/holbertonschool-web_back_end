#!/usr/bin/env python3
"""7-to_kv.pt"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    to_kv a function that takes as argument a string k,
    an Union of int and float v and return a tuple containig
    k and the result cube of v
    """
    return (k, v ** 2)
