#!/usr/bin/env python3
"""4-tasks.py"""
from typing import List
import typing
from asyncio import as_completed

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """wait-n: call the function task_wait_random n times
        returns a list of floats containing random delay
    """
    delay_tasks = list()
    for i in range(n):
        delay = task_wait_random(max_delay)
        delay_tasks += [delay]
    rands = list()
    for promises in as_completed(delay_tasks):
        rands += [await promises]
    return rands
