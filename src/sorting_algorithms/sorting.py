from typing import *


def selection_sort(list_to_sort: List[int]) -> None:
    '''
    this function is provided as an example
    note: the sort is in_place, sorting takes place via side effects
    '''
    for i in range(len(list_to_sort)):
        # find min
        min_index = i
        for j in range(i, len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[min_index]:
                min_index = j
        # swap min_item and current item
        temp = list_to_sort[i]
        list_to_sort[i] = list_to_sort[min_index]
        list_to_sort[min_index] = temp


# TODO 1
def insertion_sort(list_to_sort: List[int]) -> None:
    pass


# TODO 2
def bubble_sort(list_to_sort: List[int]) -> None:
    pass


# TODO 3
def merge_sort(list_to_sort: List[int]) -> List[int]:
    '''
    Note: this algorithm is not in-place
    sorting is not done in place
    return the sorted list
    '''
    pass


# TODO 4
def quick_sort(list_to_sort: List[int]) -> None:
    pass


### Week 2 -- Linear Sorts ###

def count_sort(list_to_sort: List[int], key_fn=lambda x: x) -> List[int]:
    '''
    key_fn is a function we use to get the key for comparision
    for example, if we are to compare item x and y, we compare key_fn(x) and key_fn(y)
    it is useful in radix sort, when we need to compare numbers based on a digit
    '''
    pass


def radix_sort(list_to_sort: List[int]) -> List[int]:
    '''
    find max number of digits before sorting
    we can just use the count_sort implemented above, by giving it a suitable key_fn 
    '''
    pass
