# -*- coding: utf-8 -*-
class Empty(Exception):
    pass


class LinkedList:        
    class _Node:
        __slots__ = '_data', '_prev', '_next'
        def __init__(self, data, prev=None, next_=None):
            self._data = data
            self._prev = prev
            self._next = next_
            
    def __init__(self):
        self._size = 0
        self._head = self._Node(None)
        self._tail = self._Node(None, self._head)
        self._head._next = self._tail
    
    def size(self):
        return self._size
    
    def first(self):
        if not self._size: raise Empty('The list is empty!')
        return self._head._next._data
    
    def last(self):
        if not self._size: raise Empty('The list is empty!')
        return self._tail._prev._data
    
    def _walk(self, key=0):
        if not self._size: raise Empty('The list is empty!')
        if key < self.size():
            walk = 0
            current = self._head
            while walk < key:
                current = current._next
                walk += 1
            return current
        else: raise KeyError('Index out of range')
    
    def get(self, key=0):
        return self._walk(key)._data
        
    def add(self, data, front=False):
        self._size += 1
        elem = self._Node(data)
        if front:
            elem._prev = self._head
            elem._next = self._head._next
            self._head._next._prev = elem
            self._head._next = elem
        else:
            elem._prev = self._tail._prev
            elem._next = self._tail
            self._tail._prev._next = elem
            self._tail._prev = elem
                
    def pop(self, front=True):
        if not self._size: raise Empty('The list is empty!')
        self._size -= 1
        if front:
            elem = self._head._next
            self._head._next = elem._next
            elem._next._prev = self._head
        else:
            elem = self._tail._prev
            self._tail._prev = elem._prev
            elem._prev._next = self._tail
        return elem._data
    
            