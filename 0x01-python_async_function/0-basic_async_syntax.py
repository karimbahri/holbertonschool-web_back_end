#!/usr/bin/env python3
"""0-basic_async_syntax.py"""
from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int=10) -> float:
    """
    wait_random: asynchronous function that wait a random number
    between 0sec and max_delay argument
    it returns the random number
    """
    rand = uniform(0, max_delay)
    await sleep(rand)
    return rand
