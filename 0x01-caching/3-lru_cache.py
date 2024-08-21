#!/usr/bin/env python3

"""A LRU Module"""

from collections import deque

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A simple LRU Cache implementation"""

    def __init__(self):
        super().__init__()
        self.access = deque()

    def put(self, key, item):
        """
        Sets a key in the cache dictionary, and removes the least used
        if set cache limit is reached
        Args:
            key: the key to be set in the dictionary
            item: the value to be set for the key
        """
        cache = self.cache_data

        if key in cache:
            self.access.remove(key)
        elif len(cache) >= self.MAX_ITEMS:
            oldest = self.access.popleft()
            del cache[oldest]
            print('DISCARD: ' + oldest)
        cache[key] = item
        self.access.append(key)

    def get(self, key):
        """
        Gets a key from the cache dictionary
        Args:
            key: the key to be accessed
        Return:
            the value linked to the key, None otherwise
        """

        if key not in self.cache_data:
            return

        self.access.remove(key)
        self.access.append(key)
        return self.cache_data.get(key)
