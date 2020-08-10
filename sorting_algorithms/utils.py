""""""

from typing import List


def is_sorted(array: List[int]) -> bool:
    if len(array) == 0 or len(array) == 1:
        return True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:

            return False

    return True


if __name__ == '__main__':
    array = [1, 15, 15, 48, 115, 618, 4444]

    print(is_sorted(array))
