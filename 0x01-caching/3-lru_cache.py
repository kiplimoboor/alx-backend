#!/usr/bin/env python3

"""A simple LRU Module"""

from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A simple LRU Cache implementation"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Sets a key in the cache dictionary, and removes the least used
        if set cache limit is reached
        Args:
            key: the key to be set in the dictionary
            item: the value to be set for the key
        """
        if not key or not item:
            return

        cache = self.cache_data

        if len(cache) == self.MAX_ITEMS and key not in cache:
            oldest, _ = cache.popitem(last=False)
            print('DISCARD: ' + oldest)

        cache[key] = item
        cache.move_to_end(key)

    def get(self, key):
        """
        Gets a key from the cache dictionary
        Args:
            key: the key to be accessed
        Return:
            the value linked to the key, None otherwise
        """

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
