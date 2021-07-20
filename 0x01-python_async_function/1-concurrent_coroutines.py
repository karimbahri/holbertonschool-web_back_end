#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""
from typing import List
import typing
from asyncio import as_completed

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """wait-n: call the function wait_random n times
        returns a list of floats containing random delay
    """
    delay_tasks = list()
    for i in range(n):
        delay = wait_random(max_delay)
        delay_tasks += [delay]
    rands = list()
    for promises in as_completed(delay_tasks):
        rands += [await promises]
    return rands
