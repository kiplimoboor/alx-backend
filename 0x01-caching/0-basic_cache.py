#!/usr/bin/env python3

"""A basic cache module"""

from functools import lru_cache


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")


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
