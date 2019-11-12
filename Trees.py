#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 08:49:25 2019

@author: ybsemeny
"""
import random

class NodeError(Exception):
    pass


class AbstractTree:
    class _Node:
        def __init__(self, data, parent):
            self._data = data
            self._parent = parent
            self._children = []
        
        def __iter__(self):
            # must be implemented by children
            pass
        
        def _get_children(self):
            # must be implemented by children
            return self._children
        
        def _add_child(self, child):
            self._children.append(child)
            
        def _remove_child(self, child):
            self._children.pop(self._children.find(child))
            
        def is_leaf(self):
            # must be implemented by children
            return len(self._children) == 0
        
        def __len__(self):
            # must be implemented by children
            return len(self._children)
        
        def get(self):
            return self._data
        
        def __str__(self):
            children_str = ""
            for child in self._children:
                strings = str(child).split('\n')
                for string in strings:
                    children_str += "\n-{0}".format(string)            
            return "[{data}]{children_data}".format(data = self._data, children_data = children_str)
    
    def __init__(self):
        self._data = []
        self._root = None
        
    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        pass
    
    def add(self, data, parent):
        pass
    
    def find(self, value):
        for i in self:
            if i.get() == value:
                return i
            
    def remove(self, p):
        if self._root != p:
            p.parent.pop(p)
        else:
            self._root = None
            
    def get(self, p):
        return p.get()
    
    def get_root(self):
        return self._root
            
    def __str__(self): 
        return str(self.__class__) + ": \n" + str(self._root)
            
    
        
    
    

class SimpleTree(AbstractTree):
    class _Node(AbstractTree._Node):
        def __init__(self, data, parent):
            super().__init__(data, parent)
            self._children = []
            if self._parent is not None:
                self._parent._add_child(self)
            self._counter = 0
                
        def __iter__(self):
            return self.__walk__()

        def __walk__(self):
            yield self
            for child in self._children: yield from child
        
        def pop(self, key):
            self._children.remove(key)
        
    def __init__(self):
        super().__init__()
        
    def __len__(self):
        return len(self._data)
        
    def add(self, data, p=None):
        if p is None and self._root is not None:
            raise KeyError('Tree is not empty and parent is missing!')
        elem = self._Node(data, p)
        if not self._root: self._root = elem
        self._data.append(elem)
        return elem
        
    def __iter__(self):
        return iter(self._root)
    
    def remove(self, p):
        if self._root != p:
            p._parent.pop(p)
        else:
            self._root = None
    
    def gen_test_data(self):
        root = self.add(11)
        p = self.add(21, root)
        p = self.add(22, root)
        p2 = self.add(31, p)
        p3 = self.add(32, p)
        p2 = self.add(41, p2)


class BinaryTree(AbstractTree):
    class _Node(AbstractTree._Node):
        def __init__(self, data, parent):
            super().__init__(data, parent)
            self._children = [None, None]
            self.LeftChild = self._children[0]
            self.RightChild = self._children[1]
            
        def _add_child(self, data, p=None):
            raise NotImplementedError
            
        def addLeft(self, child):
            self._children[0] = child
        
        def addRight(self, child):
            self._children[1] = child
            
        def _hasLeft(self):
            return self._children[0] is not None
        
        def _hasRight(self):
            return self._children[1] is not None
        
        def is_leaf(self):
            return !(self._hasLeft() or self._hasRight())
        
        def full(self):
            return self._hasLeft and self._hasRight
                
        def __str__(self):
            children_str = ""
            for child in self._children:
                if child is not None:
                    strings = str(child).split('\n')
                    for string in strings:
                        children_str += "\n-{0}".format(string)            
            return "[{data}]{children_data}".format(data = self._data, children_data = children_str)
        
            
    def __init__(self):
        super().__init__()
        
    def add(self, data):
        if self._root is None:
            self._root = self._Node(data, None)
            return self._root
        else:
            raise NodeError('Already has root')
            
    def addLeft(self, data, parent):
        if parent._hasLeft():
            print(parent)
            raise KeyError('This slot is not empty!')
        elem = self._Node(data, parent)
        parent.addLeft(elem)
        return elem
    
    def addRight(self, data, parent):
        if parent._hasRight():
            print(parent)
            raise KeyError('This slot is not empty!')
        elem = self._Node(data, parent)
        parent.addRight(elem)
        return elem
    
    def gen_test_data(self):
        b = self
        b.add(1)
        l1 = b.addLeft(2, b.get_root())
        r1 = b.addRight(3, b.get_root())
        l11 = b.addLeft(4, l1)
        l12 = b.addRight(5, l1)
        r11 = b.addLeft(6, r1)
        r12 = b.addRight(7, r1)
        l21 = b.addLeft(8, l11)
        l22 = b.addRight(9, l11)
        l23 = b.addLeft(10, l12)
        l24 = b.addRight(11, l12)


class BinaryHeap(BinaryTree):
    class _Node(BinaryTree._Node):
        def bubbleDown(self, data):
            if data > self._data: 
                result = self._data
                if self.is_leaf(): self._data = data
                else:
                    target = self.LeftChild if not self.full else max([i._data for i in self._children])
                    self._data = target.bubbleDown(data)
            else:
                result = data
            return result
            
        def bubbleUp(self, data):
            if data >= self._data or self._parent is None:
                result = data
            else:
                result = self._data
                self._data = parent.bubbleUp(data)
            return result
                 
    def __init__(self):
        super().__init__()
        self._storage_stack = []
        
    def add(self, data):
        if self._root is None:
            self._root = self._Node(data, None)
        else:
            
            
    


if __name__ == "__main__":
    divider = "============"
    s = SimpleTree()
    s.gen_test_data()
    print(s)
    print(divider)
    to_delete = s.find(22)
    print(to_delete)
    print(divider)
    s.remove(to_delete)
    print(s)
    print(divider)
    print(divider)
    b = BinaryTree()
    b.gen_test_data()
    print(b)
