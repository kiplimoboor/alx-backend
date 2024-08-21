#!/usr/bin/env python3

"""A LIFO Module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A simple LIFO Cache implementation"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Sets a key in the cache dictionary, and removes last key
        if cache limit is reached
        Args:
            key: the key to be set in the dictionary
            item: the value to be set for the key
        """

        if key and item:
            data = self.cache_data
            if (len(data) >= self.MAX_ITEMS):
                discarded = key if key in data else list(data.keys())[-1]
                if key not in data:
                    print('DISCARD: ' + discarded)
                del (data[discarded])
            data[key] = item

    def get(self, key):
        """
        Gets a key from the cache dictionary
        Args:
            key: the key to be accessed
        Return:
            the value linked to the key, None otherwise
        """

        return self.cache_data.get(key)
