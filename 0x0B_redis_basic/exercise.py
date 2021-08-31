#!/usr/bin/env python3
"""exercice module"""
from typing import Union
from typing import Optional
from typing import Callable
from typing import Any

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

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """public method:
            takes key (string) as argument
            and an optional callable function
            to convert data format
        """
        d = self._redis.get(key)

        if fn is None:
            return d
        else:
            return fn(d)

    def get_str(self, id):
        """get_str: public method
            change data format to string
        """
        converted = self.get(id)
        return converted

    def get_int(self, id):
        """get_int: public method
            change data format to integer
        """
        converted = int(self.get(id))
        return converted
