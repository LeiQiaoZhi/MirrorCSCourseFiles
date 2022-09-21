from mimetypes import init
from typing import *

'''
NOTE: we are building this data structure from scratch
please DO NOT use any python's built in data structures (especially dictionary in this case)
'''


class BinarySearchTree:
    def __init__(self, key, value=None, left=None, right=None) -> None:
        '''
        we define BinarySearchTree as a recursive date structure

        since we use the tree is an implementation of dictionary, the tree head has key and value
        left is its left child, which is also a Binary Tree
        right is its right child, a Binary Tree as well

        BST's property: left.key <= self.key <= right.key
        '''
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    # TODO 1
    def get(self, key, default=None):
        '''
        return the value given a key, just like a python dictionary query: dic[key]
        return default if key is not in the tree
        '''
        pass

    # TODO 2
    def update(self, key, value) -> None:
        '''
        equivalent to the operation: dic[key] = value
        if key does not exist in tree, the key,value pair is added
        '''
        pass

    # TODO 3
    def delete(self, key) -> None:
        '''
        delete the tree with matching key
        '''
        pass

    @staticmethod
    def default_tree():
        '''
        returns a hard coded bst, used for testing
        '''
        return BinarySearchTree(
            16, 16,
            left=BinarySearchTree(
                8, 8,
                left=BinarySearchTree(4, 4,
                                      left=BinarySearchTree(2, 2,),
                                      right=BinarySearchTree(6, 6,)),
                right=BinarySearchTree(12, 12, left=BinarySearchTree(10, 10,),
                                       right=BinarySearchTree(14, 14,))),
            right=BinarySearchTree(
                24, 24,
                left=BinarySearchTree(20, 20, left=BinarySearchTree(18, 18,),
                                      right=BinarySearchTree(22, 22,)),
                right=BinarySearchTree(28, 28, left=BinarySearchTree(26, 26,),
                                       right=BinarySearchTree(30, 30,)))
        )
