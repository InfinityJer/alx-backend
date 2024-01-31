#!/usr/bin/env python3
""" LFUCache module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LFU
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        # Cache data stored as an ordered dictionary
        self.cache_data = OrderedDict()
        # List to keep track of keys and their frequencies
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """Reorders the items in this cache based on the most
        recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        # Iterate through the keys_freq list
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            # If the list of max_positions is empty, add the current position
            elif len(max_positions) == 0:
                max_positions.append(i)
            # If the frequency at the current position is less than the last recorded max frequency,
            # add the current position to max_positions
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)
        # Reverse the list of max_positions to iterate from highest to lowest positions
        max_positions.reverse()
        # Iterate through max_positions to find the correct position to insert the most recently used key
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos
        # Remove the most recently used key from its current position and insert it at the correct position
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        # If the key is not in the cache, perform LFU removal if necessary
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # Get the least frequently used key and remove it from the cache and keys_freq list
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            # Add the new key and item to the cache and keys_freq list
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                # Find the position to insert the new key based on frequency
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            # If the key is already in the cache, update the item and reorder the keys_freq list
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        # If the key is not None and exists in the cache, reorder the keys_freq list
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        # Return the item associated with the key, or None if the key is not in the cache
        return self.cache_data.get(key, None)
