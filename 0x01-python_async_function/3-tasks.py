#!/usr/bin/env python3
"""3-tasks.py"""
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    task_wait_random: regular function
    it takes an integer as arg (max_delay)
    it return asyncio.Task
    """
    return Task(wait_random(max_delay))
