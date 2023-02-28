"""Bubble sort algorithm"""


import random
from typing import List

from tasks.sorting_algorithms.utils import is_sorted


def bubble_sort(array: List[int]):
    for i in range(len(array)):
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]

    return array


if __name__ == '__main__':
    array = [random.randrange(0, 1000) for _ in range(5)]
    print(f'Original array: {array}')

    sorted_array = bubble_sort(array=array)
    print(f'Sorted array: {sorted_array}')

    print(f'is_sorted: {is_sorted(sorted_array)}')
