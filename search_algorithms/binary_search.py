import time
from typing import List, Optional

import numpy as np


def binary_search(sorted_list: List[int], value_to_find: int) -> Optional[int]:
    """
    Must have. Works really fast.
    Time: O(log(n))
    Memory: O(n)

    :param sorted_list: list with sorted elements (ascending)
    :param value_to_find: value which we're trying to find in sorted list
    :return: idx
    """

    start_idx = 0
    end_idx = len(sorted_list) - 1

    while start_idx <= end_idx:
        idx = (start_idx + end_idx) // 2

        if sorted_list[idx] < value_to_find:
            start_idx = idx + 1
        elif sorted_list[idx] > value_to_find:
            end_idx = idx - 1
        else:
            return idx

    return None


def binary_search_recursion(sorted_list: List[int], value_to_find: int) -> Optional[int]:
    """
    Binary search using recursion. Dumb, but funny.

    :param sorted_list: list with sorted elements (ascending)
    :param value_to_find: value which we're trying to find in sorted list
    :return: idx
    """

    start_idx = 0
    end_idx = len(sorted_list) - 1

    idx = (start_idx + end_idx) // 2

    if len(sorted_list) == 0:
        return None

    if sorted_list[idx] < value_to_find:
        start_idx = idx + 1

        deep_sorted_list = sorted_list[start_idx: end_idx + 1]
        res_rec = binary_search_recursion(sorted_list=deep_sorted_list, value_to_find=value_to_find)

        if res_rec is None:
            return None

        return idx + res_rec + 1

    elif sorted_list[idx] > value_to_find:
        end_idx = idx

        deep_sorted_list = sorted_list[start_idx: end_idx]
        res_rec = binary_search_recursion(sorted_list=deep_sorted_list, value_to_find=value_to_find)

        if res_rec is None:
            return None

        return idx - len(deep_sorted_list) + res_rec

    return idx


if __name__ == '__main__':
    sorted_list = sorted(list(np.random.randint(0, 150000000, size=500000)))

    NUM_TO_TEST = sorted_list[456813]

    start = time.time_ns()
    res = binary_search(sorted_list=sorted_list, value_to_find=NUM_TO_TEST)
    end = time.time_ns()
    print(f'Simple binary search in ns: {end - start}')

    start = time.time_ns()
    res_rec = binary_search_recursion(sorted_list=sorted_list, value_to_find=NUM_TO_TEST)
    end = time.time_ns()
    print(f'Recursion binary search in ns: {end - start}')

    print(f'Binary search result: {res}')
    print(f'Recursion binary search result: {res_rec}')
