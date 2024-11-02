#!/usr/bin/env python3
'''

FIFO cache

'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''implements FIFO caching'''
    def __init__(self):
        super().__init__()
        self.__order = []

    def put(self, key, item):
        '''adds an item'''
        if not key or not item:
            return
        if len(self.__order) < self.MAX_ITEMS or key in self.cache_data.keys():
            self.__order.append(key)
            self.cache_data[key] = item
        else:
            discarded = self.__order[0]
            print(f'DISCARD: {discarded}')
            del self.cache_data[discarded]
            self.__order = self.__order[1:]
            self.__order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''gets an item'''
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
