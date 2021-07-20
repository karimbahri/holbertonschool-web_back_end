#!/usr/bin/env python3
"""2-measure_runtime.py"""
from time import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time: a function that execute wait-n and
        mesure the execution time
    """
    prev_time = time()
    run(wait_n(n, max_delay))
    return (time() - prev_time) / n
