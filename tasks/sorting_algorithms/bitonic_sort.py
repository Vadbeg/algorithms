"""
Bitonic sorting algorithm | NOT READY YET


:source: https://www.geeksforgeeks.org/bitonic-sort/
@by Vadbeg
"""

import math


def comp_and_swap(arr, i, j, dire):
    if (dire == 1 and arr[i] > arr[j]) or \
            (dire == 0 and arr[i] < arr[j]):

        arr[i], arr[j] = arr[j], arr[i]


def bitonic_merge(arr, low, counter, dire):
    if counter > 1:
        temp_counter = math.ceil(counter / 2)

        for i in range(low, low + temp_counter):
            comp_and_swap(arr, i, i + temp_counter, dire)

        bitonic_merge(arr, low=low, counter=temp_counter, dire=dire)
        bitonic_merge(arr, low=low + temp_counter, counter=temp_counter, dire=dire)


def bitonic_sort_recursion(arr, low, counter, dire):
    if counter > 1:
        temp_counter = math.ceil(counter / 2)

        bitonic_sort_recursion(arr, low, temp_counter, 1)
        bitonic_sort_recursion(arr, low + temp_counter, temp_counter, 0)

        bitonic_merge(arr, low, counter, dire)


def bitonic_sort(arr, counter, up):
    bitonic_sort_recursion(arr=arr, low=0, counter=counter, dire=up)


if __name__ == '__main__':
    arr = [3, 7, 4, 8, 6, 2, 1, 5, 7]
    arr_len = len(arr)
    up = 1

    bitonic_sort(arr=arr, counter=arr_len, up=up)

    print(f'Sorted list: {arr}')

