"""
Google Coding Interview Question
from https://www.youtube.com/watch?v=XKu_SEDAykw
"""

from typing import Optional


def find_sum_of_pairs_in_array(arr: list, sum_value: int) -> Optional[tuple[int, int]]:
    second_value_by_first = {}

    for curr_value in arr:
        second_value_from_pair = sum_value - curr_value

        if second_value_by_first.get(second_value_from_pair, None):
            return curr_value, second_value_from_pair

        second_value_by_first[curr_value] = second_value_from_pair

    return None


def test_cases():
    arr = [1, 2, 3, 9]
    sum_value = 8
    assert find_sum_of_pairs_in_array(arr=arr, sum_value=sum_value) is None

    arr = [1, 2, 4, 4]
    sum_value = 8
    assert find_sum_of_pairs_in_array(arr=arr, sum_value=sum_value) == (4, 4)

    arr = [1, 2, 4]
    sum_value = 8
    assert find_sum_of_pairs_in_array(arr=arr, sum_value=sum_value) is None

    arr = [1, 2, 3, 4, 4, 5]
    sum_value = 8
    assert find_sum_of_pairs_in_array(arr=arr, sum_value=sum_value) == (4, 4) or \
           find_sum_of_pairs_in_array(arr=arr, sum_value=sum_value) == (4, 4)

    arr = [1]
    sum_value = 8
    assert find_sum_of_pairs_in_array(arr=arr, sum_value=sum_value) is None


if __name__ == '__main__':
    test_cases()
