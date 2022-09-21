from typing import *

'''
NOTE: we are building this data structure from scratch
please DO NOT use any python's built in data structures 
'''


class BinaryHeap:
    def __init__(self, value, key=None, left=None, right=None) -> None:
        '''
        we define BinaryHeap as a recursive date structure

        Binary Heap is an implementation of the Priority Queue ADT

        the field key is the priority, smaller the key, higher the priority

        the root of a binary heap should have the smallest key

        key doesn't need to be unique, value needs to be unique

        BinaryHeap's property: 
            for every node,
            left.key <= self.key and right.key <= self.key
        '''
        self.key = key if key else value
        self.value = value
        self.left = left
        self.right = right

    # TODO 1
    def pop(self):
        '''
        returns the root's value, then reorganize the heap 
        '''
        pass

    # TODO 2
    def push(self, key, value):
        '''
        add a new key,value pair to the heap
        the heap must still maintain the heap property
        '''
        pass

    @staticmethod
    def default_heap():
        return BinaryHeap(
            0,
            left=BinaryHeap(1,
                            left=BinaryHeap(2),
                            right=BinaryHeap(3)),
            right=BinaryHeap(4,
                             left=BinaryHeap(5),
                             right=BinaryHeap(6))
        )
