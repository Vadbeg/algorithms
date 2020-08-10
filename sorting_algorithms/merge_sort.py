"""Module with merge sort"""

import random
from typing import List

from sorting_algorithms.utils import is_sorted


def merge_sort(array: List[int]) -> List[int]:
    """
    Merge sort

    Time: O(n * log(n))
    Memory: O(n) <- but not in mine version

    :source: https://en.wikipedia.org/wiki/Merge_sort
    :param array: given res_array
    :return: sorted res_array
    """

    if len(array) == 1 or len(array) == 0:
        return array

    midpoint = len(array) // 2

    array_1 = merge_sort(array[:midpoint])
    array_2 = merge_sort(array[midpoint:])

    res_array = list()

    array_1_index = 0
    array_2_index = 0

    while array_1_index < len(array_1) or array_2_index < len(array_2):
        first_array_value = array_1[array_1_index] if array_1_index < len(array_1) else None
        second_array_value = array_2[array_2_index] if array_2_index < len(array_2) else None

        if first_array_value is None:
            res_array.append(second_array_value)
            array_2_index += 1

        elif second_array_value is None:
            res_array.append(first_array_value)
            array_1_index += 1

        elif first_array_value <= second_array_value:
            res_array.append(first_array_value)
            array_1_index += 1
        else:
            res_array.append(second_array_value)
            array_2_index += 1

    return res_array


if __name__ == '__main__':
    array = [random.randrange(0, 1000) for _ in range(10000)]

    res_array = merge_sort(array=array)

    print(f'Res res_array: {res_array}')
    print(f'is_sorted: {is_sorted(res_array)}')
