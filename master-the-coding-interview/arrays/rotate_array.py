"""
Rotate Array

https://leetcode.com/problems/rotate-array/description/
"""


def check_array(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len(arr2):
        return False

    for curr_val1, curr_val2 in zip(arr1, arr2):
        if curr_val1 != curr_val2:
            return False

    return True


def rotate_array(nums: list[int], k: int) -> None:
    k = k % len(nums)

    reverse(nums, 0, len(nums) - k - 1)
    reverse(nums, len(nums) - k, len(nums) - 1)
    reverse(nums, 0, len(nums) - 1)


def reverse(nums: list[int], start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_array(nums=arr, k=k)
    assert check_array(arr1=arr, arr2=[5, 6, 7, 1, 2, 3, 4])

    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    rotate_array(nums=arr, k=k)
    assert check_array(arr1=arr, arr2=[6, 7, 1, 2, 3, 4, 5])

    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 1
    rotate_array(nums=arr, k=k)
    assert check_array(arr1=arr, arr2=[7, 1, 2, 3, 4, 5, 6])

    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 0
    rotate_array(nums=arr, k=k)
    assert check_array(arr1=arr, arr2=[1, 2, 3, 4, 5, 6, 7])

    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 703
    rotate_array(nums=arr, k=k)
    assert check_array(arr1=arr, arr2=[5, 6, 7, 1, 2, 3, 4])

    arr = [1]
    k = 703
    rotate_array(nums=arr, k=k)
    assert check_array(arr1=arr, arr2=[1])

    arr = [1, 2]
    k = 702
    rotate_array(nums=arr, k=k)
    assert check_array(arr1=arr, arr2=[1, 2])

    arr = [1, 2]
    k = 703
    rotate_array(nums=arr, k=k)
    assert check_array(arr1=arr, arr2=[2, 1])

    arr = [0]
    k = 703
    rotate_array(nums=arr, k=k)
    assert check_array(arr1=arr, arr2=[0])

    arr = [-1, -100, 3, 99]
    k = 2
    rotate_array(nums=arr, k=k)
    assert check_array(arr1=arr, arr2=[3, 99, -1, -100])

