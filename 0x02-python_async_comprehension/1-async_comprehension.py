#!/usr/bin/env python3
"""1-async_comprehension"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """async_comprehension:
        collect 10 random numbers using async comprehension
        Return: list of the 10 random number
    """
    return [number async for number in async_generator()]
