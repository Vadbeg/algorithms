"""
Sortig algorithms

@by Vadbeg
"""

from typing import List


def quick_sort(array_to_sort: List[int]) -> List[int]:
    """
    Quick-sort sorting algorithm.

    Time: O(n*log(n))
    Memory: O(n)

    :param array_to_sort: array which we need to sort
    :return: sorted array
    """

    if len(array_to_sort) < 2:
        return array_to_sort

    basic_el = array_to_sort[0]

    lower_els = [el for el in array_to_sort[1:] if el <= basic_el]
    higher_els = [el for el in array_to_sort[1:] if el > basic_el]

    res = quick_sort(lower_els) + [basic_el] + quick_sort(higher_els)

    return res


if __name__ == '__main__':
    array_to_sort = [14, 14,  15, 12, 47, 1, 25, 6, 48, 63, 8, 1]

    res_sorted = quick_sort(array_to_sort)

    print(f'Sorted list: {res_sorted}')
