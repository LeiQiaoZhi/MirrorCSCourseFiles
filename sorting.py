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


def insertion_sort(list_to_sort: List[int]) -> List[int]:
    pass
