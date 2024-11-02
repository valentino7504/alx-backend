#!/usr/bin/env python3
'''

LIFO cache

'''
from base_caching import BaseCaching


class Stack:
    '''creates a stack'''
    def __init__(self) -> None:
        '''init of stack class'''
        self.__data = []

    def push(self, item):
        '''add item to stack'''
        self.__data.append(item)

    def pop(self):
        '''remove item from stack'''
        discarded = self.__data[-1]
        self.__data = self.__data[:-1]
        return discarded

    def __len__(self):
        '''gets length of stack'''
        return len(self.__data)


class LIFOCache(BaseCaching):
    '''implements FIFO caching'''
    def __init__(self):
        super().__init__()
        self.__stack = Stack()

    def put(self, key, item):
        '''adds an item'''
        if not key or not item:
            return
        if len(self.__stack) < self.MAX_ITEMS or key in self.cache_data.keys():
            self.__stack.push(key)
            self.cache_data[key] = item
        else:
            discarded = self.__stack.pop()
            print(f'DISCARD: {discarded}')
            del self.cache_data[discarded]
            self.cache_data[key] = item
            self.__stack.push(key)

    def get(self, key):
        '''gets an item'''
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
