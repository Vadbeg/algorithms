import random
from typing import List
from copy import deepcopy

from tasks.sorting_algorithms.utils import is_sorted


def move_els(array: List[int], start_index, remove_index):

    for i in range(remove_index - start_index):
        array[remove_index - i] = array[remove_index - i - 1]

    return array


def insertion_sort(array: List[int]):
    res_array = deepcopy(array)

    for i in range(len(res_array)):
        for j in range(i):

            if res_array[i] < res_array[j]:
                temp_value = deepcopy(res_array[i])

                res_array = move_els(array=res_array, start_index=j, remove_index=i)

                res_array[j] = temp_value

                break

    return res_array


if __name__ == '__main__':
    # array = [random.randrange(0, 1000) for _ in range(10000)]
    array = [random.randrange(0, 100) for _ in range(30)]

    res_array = insertion_sort(array=array)

    print(f'Start array: {array}')
    print(f'Start array length: {len(array)}')
    print(f'Res array: {res_array}')
    print(f'Res array length: {len(res_array)}')
    print(f'Is sorted: {is_sorted(res_array)}')

