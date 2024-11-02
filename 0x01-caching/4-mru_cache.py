#!/usr/bin/env python3
'''

implements MRU Cache

'''
from base_caching import BaseCaching


class DLLNode():
    '''creates a node in a doubly linked list'''
    def __init__(self, data) -> None:
        '''init method'''
        self.data = data
        self.next: DLLNode = None
        self.prev: DLLNode = None


class DoublyLinkedList():
    '''implements a doubly linked list'''
    def __init__(self) -> None:
        self.__head: DLLNode = None
        self.__tail: DLLNode = None
        self.__hash = {}

    def insert(self, data):
        '''inserts a node'''
        node = DLLNode(data)
        if self.__head is None:
            self.__head = node
        if self.__tail is not None:
            node.prev = self.__tail
            node.prev.next = node
        self.__tail = node
        self.__hash[data] = node
        return node

    def bump(self, data):
        '''bumps an item up to the top of the list'''
        node: DLLNode = self.__hash[data]
        if node == self.__tail:
            return
        if node == self.__head:
            self.__head = node.next
            self.__head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = None
        node.prev = self.__tail
        self.__tail.next = node
        self.__tail = node
        return node

    def delete(self):
        '''deletes an item'''
        if self.__head is None:
            return
        node = self.__tail
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = node.prev
            self.__tail.next = None
        del self.__hash[node.data]
        return node

    def __len__(self):
        '''gets length of dll'''
        return len(self.__hash.keys())


class MRUCache(BaseCaching):
    '''MRUCache class'''
    def __init__(self):
        '''init method'''
        super().__init__()
        self.__dll = DoublyLinkedList()

    def put(self, key, item):
        '''adds an item'''
        if not key or not item:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.__dll.bump(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                deleted = self.__dll.delete()
                print(f'DISCARD: {deleted.data}')
                del self.cache_data[deleted.data]
            self.__dll.insert(key)
            self.cache_data[key] = item

    def get(self, key):
        '''gets an item'''
        if not key or key not in self.cache_data.keys():
            return None
        self.__dll.bump(key)
        return self.cache_data[key]
