import random
from typing import List

from tasks.sorting_algorithms.insertion_sort import insertion_sort
from tasks.sorting_algorithms.utils import is_sorted


def bucket_sort(array: List[int], bins=10):
    buckets = [[]] * bins

    for el in array:
        bucket_index = el // bins

        buckets[bucket_index].append(el)

    buckets_res = list()

    for curr_bucket in buckets:
        if len(curr_bucket) != 0:
            curr_bucket = insertion_sort(curr_bucket)

            buckets_res.extend(curr_bucket)

    return buckets_res


if __name__ == '__main__':
    array = [random.randrange(0, 1000) for _ in range(10000)]

    res_array = insertion_sort(array=array)

    print(f'Start array: {array}')
    print(f'Res array: {res_array}')

    print(f'is_sorted: {is_sorted(res_array)}')
