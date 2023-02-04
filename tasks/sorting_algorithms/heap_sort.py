import random
from typing import List


def swap(array: List[int], idx_first: int, idx_second: int) -> List[int]:
    array[idx_second], array[idx_first] = array[idx_first], array[idx_second]

    return array


def heapify(array: List[int]) -> List[int]:
    idx = 0

    while idx != len(array):
        inverted_idx = len(array) - idx - 1

        parent_node_idx = (inverted_idx - 1) // 2
        parent_node_idx = parent_node_idx if parent_node_idx >= 0 else 0

        if array[inverted_idx] > array[parent_node_idx]:
            array = swap(array=array, idx_first=inverted_idx, idx_second=parent_node_idx)

            if idx == len(array):
                break

            idx = 0
        else:
            idx += 1

    return array


def heap_sort(array: List[int]) -> List[int]:

    for i in range(len(array)):
        if i == 0:
            array = heapify(array)
        else:
            array[:-i] = heapify(array[:-i])

        array = swap(array=array, idx_first=0, idx_second=len(array) - i - 1)

    return array


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    res_array = heap_sort(array)

    print(f'Res array: {res_array}')
