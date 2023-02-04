"""
Contains Duplicate

https://leetcode.com/problems/contains-duplicate/description/
"""


def contains_duplicate_hash(nums: list[int]) -> bool:
    nums_values = set()

    for curr_num in nums:
        if curr_num not in nums_values:
            nums_values.add(curr_num)
        else:
            return True

    return False


if __name__ == '__main__':
    contains_duplicate_func = contains_duplicate_hash

    _nums = [1, 2, 3, 1]
    res = contains_duplicate_func(nums=_nums)
    assert res is True

    _nums = [1, 2, 3]
    res = contains_duplicate_func(nums=_nums)
    assert res is False

    _nums = [1, 2, 3, 4]
    res = contains_duplicate_func(nums=_nums)
    assert res is False

    _nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    res = contains_duplicate_func(nums=_nums)
    assert res is True

    _nums = []
    res = contains_duplicate_func(nums=_nums)
    assert res is False

    _nums = [1, 1]
    res = contains_duplicate_func(nums=_nums)
    assert res is True

    _nums = [1, 2]
    res = contains_duplicate_func(nums=_nums)
    assert res is False
