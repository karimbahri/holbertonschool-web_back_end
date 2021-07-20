#!/usr/bin/env python3
"""0-basic_async_syntax.py"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """
    wait_random: asynchronous function that wait a random number
    between 0sec and max_delay argument
    it returns the random number
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
