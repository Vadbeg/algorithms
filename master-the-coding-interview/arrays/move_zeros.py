"""Moves all zeros of the array to the end"""


def check_array(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len(arr2):
        return False

    for curr_val1, curr_val2 in zip(arr1, arr2):
        if curr_val1 != curr_val2:
            return False

    return True


def move_zeros_dummy(nums: list[int]) -> None:
    num_of_zeros: int = 0

    idx = 0
    while idx < len(nums) - num_of_zeros:
        curr_item = nums[idx]

        if curr_item == 0:
            nums.pop(idx)
            nums.append(0)

            num_of_zeros += 1
        else:
            idx += 1

        if idx == len(nums) - num_of_zeros:
            break


def move_zeros(nums: list[int]) -> None:
    num_of_values = 0

    # Add all non-zero elements to the end
    idx = 0
    while idx < len(nums) - num_of_values:
        if nums[idx] != 0:
            nums.append(nums[idx])
            num_of_values += 1

        idx += 1

    idx = 0
    while idx < len(nums) - num_of_values:
        if nums[idx] == 0:
            nums.append(0)
            num_of_values += 1

        idx += 1

    del nums[:-num_of_values]


def move_zeros_optimal(nums: list[int]) -> None:
    idx_zero = 0
    idx_curr = 0

    while idx_curr < len(nums):
        if nums[idx_curr] != 0:
            nums[idx_curr], nums[idx_zero] = nums[idx_zero], nums[idx_curr]
            idx_zero += 1

        idx_curr += 1


if __name__ == '__main__':
    move_zeros_func = move_zeros_optimal

    _arr = [0, 1, 0, 3, 12]
    move_zeros_func(nums=_arr)
    print(_arr)
    assert check_array(arr1=_arr, arr2=[1, 3, 12, 0, 0])

    _arr = [0]
    move_zeros_func(nums=_arr)
    assert check_array(arr1=_arr, arr2=[0])

    _arr = []
    move_zeros_func(nums=_arr)
    assert check_array(arr1=_arr, arr2=[])

    _arr = [0, 0]
    move_zeros_func(nums=_arr)
    assert check_array(arr1=_arr, arr2=[0, 0])

    _arr = [0, 1]
    move_zeros_func(nums=_arr)
    assert check_array(arr1=_arr, arr2=[1, 0])
