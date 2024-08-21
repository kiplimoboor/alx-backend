#!/usr/bin/env python3

"""A basic cache module"""

from functools import lru_cache

BaseCaching = __import__('base').BaseCaching


@lru_cache(maxsize=None)
class BasicCache(BaseCaching):
    """
    A simple basic caching implementation
    """

    def __init__(self):
        """
        Construct from the super class
        """
        super().__init__()

    def put(self, key, item):
        """
        Sets a key in cache
        Args:
           key: the key to be set
           item: the value the key should hold
        """

        if key and item:
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
