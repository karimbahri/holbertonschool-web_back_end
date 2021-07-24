#!/usr/bin/env python3
"""0-basic_cache.py"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache: class that inherit from
        BaseCaching
        attributes:
            cache_data: dictionary
    """
    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """put:
            instance method: insert item into cache_data
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get:
            instance method: retrieve item from cache_data
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
