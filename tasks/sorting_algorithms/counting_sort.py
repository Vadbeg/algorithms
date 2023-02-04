import random
from typing import List

from tasks.sorting_algorithms.utils import is_sorted


def counting_sort(array: List[int]):
    counting_list = [0] * (max(array) + 1)

    for el in array:
        counting_list[el] += 1

    sorted_array = []

    for idx, element in enumerate(counting_list):
        sorted_array.extend([idx] * element)

    return sorted_array


if __name__ == '__main__':
    array = [random.randrange(0, 1000) for _ in range(10000)]
    print(f'Original array: {array}')

    sorted_array = counting_sort(array=array)
    print(f'Sorted array: {sorted_array}')

    print(f'is_sorted: {is_sorted(sorted_array)}')