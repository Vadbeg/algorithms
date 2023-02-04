import math
import time
import random
from typing import List


def interpolation_search(sorted_list: List[int], value_to_find) -> int:
    min_idx = 0
    max_idx = len(sorted_list) - 1

    while min_idx <= max_idx:
        factor = (value_to_find - sorted_list[min_idx]) / (sorted_list[max_idx] - sorted_list[min_idx])
        index_additional = (max_idx - min_idx) * factor

        mid_idx = min_idx + int(index_additional)

        if sorted_list[mid_idx] == value_to_find:
            return mid_idx

        elif sorted_list[mid_idx] > value_to_find:
            max_idx = mid_idx - 1
        elif sorted_list[mid_idx] < value_to_find:
            min_idx = mid_idx + 1

    return -1


if __name__ == '__main__':
    IDX = random.randrange(0, 100_000)

    array = sorted([random.randrange(0, 1_000_000) for _ in range(100_000)])
    NUM_TO_TEST = array[IDX]

    print(f'Generated array')

    start = time.time_ns()
    res_idx = interpolation_search(sorted_list=array, value_to_find=NUM_TO_TEST)
    end = time.time_ns()
    print(f'Simple binary search in ns: {end - start}')

    print(f'True idx: {IDX}')
    print(f'Resulted idx: {res_idx}')
