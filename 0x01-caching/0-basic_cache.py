#!/usr/bin/env python3
""" BaseCaching module
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching class
    """

    def put(self, key, item):
        """
        Puts data into the cache
        Args:
            key: the key of the data
            item: the value of the data
        """

        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets data from cache
        Args:
            key: the key as contained in the cache
        Returns:
            Value in cache linked to the key
        """

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
