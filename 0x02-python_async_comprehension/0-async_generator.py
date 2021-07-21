#!/usr/bin/env python3
"""0-async_generator.py"""
import random
from asyncio import sleep
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """async_generator: a coroutine that wait one second
        and yield a random number 10 times
    """
    for i in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
