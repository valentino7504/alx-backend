#!/usr/bin/env python3
'''

implements the basic cache class

'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''the basic cache class'''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''Add item to the cache'''
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''gets an item'''
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
