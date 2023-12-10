from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    square_nums = []

    split_idx = len(nums)

    for idx, curr_num in enumerate(nums):
        if curr_num >= 0:
            split_idx = idx
            break

    neg_idx = split_idx - 1
    pos_idx = split_idx

    while len(square_nums) != len(nums):
        neg_square_num = None
        pos_square_num = None

        print(neg_idx, pos_idx)

        if neg_idx < len(nums) and neg_idx >= 0:
            neg_square_num = nums[neg_idx] ** 2

        if pos_idx < len(nums) and pos_idx >= 0:
            pos_square_num = nums[pos_idx] ** 2

        if neg_square_num is None and pos_square_num is None:
            break
        elif neg_square_num is None and pos_square_num is not None:
            square_nums.append(pos_square_num)
            pos_idx += 1
        elif neg_square_num is not None and pos_square_num is None:
            square_nums.append(neg_square_num)
            neg_idx -= 1
        else:
            if pos_square_num < neg_square_num:
                square_nums.append(pos_square_num)
                pos_idx += 1
            else:
                square_nums.append(neg_square_num)
                neg_idx -= 1

    return square_nums


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    print(sorted_squares(nums=nums))
