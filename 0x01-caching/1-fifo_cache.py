#!/usr/bin/env python3
"""FIFO Caching Implementation"""


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Cache method implementation
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Sets value of key in the cache
        Args:
            key: the key in the cache
            item: value for which the key will contain
        """
        if key is None or item is None:
            pass

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = next(iter(self.cache_data.keys()))
            del self.cache_data[first]
            print(f"DISCARD: {first}")

    def get(self, key):
        """
        Gets value of key in the cache
        Args:
            key: the key as in the cache
        Return:
            value of item in the key of cache
        """

        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
