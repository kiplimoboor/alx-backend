#!/usr/bin/env python3

"""A basic cache module"""

from functools import lru_cache

from base import BaseCaching


@lru_cache(maxsize=None)
class BasicCache(BaseCaching):
    """
    A simple basic caching implementation
    """

    def put(self, key, item):
        """
        Sets a key in cache
        Args:
           key: the key to be set
           item: the value the key should hold
        """

        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets the value of a key
        Args:
            key: the key value to be retrieved
        Return:
            value held by the key, otherwise None
        """
        return self.cache_data.get(key)
