#!/usr/bin/env python3

"""A FIFO Module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A simple FIFO Cache implementation"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Sets a key in the cache dictionary
        Args:
            key: the key to be set in the dictionary
            item: the value to be set for the key
        """

        if key and item:
            cache = self.cache_data
            cache[key] = item
            if len(cache) > self.MAX_ITEMS:
                discarded = list(cache.keys())[0]
                del (cache[discarded])
                print(f'DISCARD: {discarded}')

    def get(self, key):
        """
        Gets a key from the cache dictionary
        Args:
            key: the key to be accessed
        Return:
            the value linked to the key, None otherwise
        """

        return self.cache_data.get(key)
