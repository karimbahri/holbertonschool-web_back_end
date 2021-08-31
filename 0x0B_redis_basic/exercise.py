#!/usr/bin/env python3
"""exercice module"""
from typing import Union

from redis import Redis
from uuid import uuid4


class Cache:
    """Cache class

        methods:
            * store

        attributes:
            * _redis: private attribute

    """
    def __init__(self):
        """__init__:
            constructor function
        """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store:
            public method
            store data in radis
            return the key of stored data
        """
        _id = str(uuid4())
        self._redis.set(_id, data)
        return _id
