"""Module for checking is number prime"""


import math
import time

from typing import List


def is_prime_simple(num: int) -> bool:
    """
    Finds prime number

    Time: O(n)

    :param num: int number
    :return: is prime
    """

    if num == 1 or num == 2:
        return True

    for i in range(2, num - 1):
        if num % i == 0:
            return True

    return False


def is_prime_fancy(num: int, with_even=False) -> bool:
    """
    Finds prime number

    Time: O(sqrt(n))

    :param num: int number
    :param with_even: checks is it even in start
    :return: is prime
    """

    if num == 1 or num == 2:
        return True

    step = 1

    if with_even:
        if num % 2 == 0:
            step = 2

    for i in range(2, int(math.sqrt(num)), step):
        if num % i == 0:
            return True

    return False


def eratophen_sieve(max_number: int) -> List:
    """
    Erastophen sieve algorithm for finding out prime numbers

    Time: N x log(log(N))
    Space: N

    :param max_number: maybe maximum prime number
    :return: list with prime numbers
    """

    is_composite_list = [False for i in range(max_number + 1)]

    for i in range(4, max_number, 2):
        is_composite_list[i] = True

    stop_at = int(math.sqrt(max_number))
    next_prime = 3

    while next_prime < stop_at:
        for i in range(next_prime * 2, max_number, next_prime):
            is_composite_list[i] = True

        next_prime += 2
        while next_prime < stop_at and is_composite_list[next_prime]:
            next_prime += 2

    res_prime = [idx for idx in range(max_number) if not is_composite_list[idx]]

    return res_prime


if __name__ == '__main__':
    # num = 997141
    #
    # start = time.time_ns()
    # res = is_prime_simple(num=num)
    # end = time.time_ns()
    #
    # print(f'Is prime simple: {res}')
    # print(f'Time in ns: {end - start}')
    # print('-' * 10)
    #
    # start = time.time_ns()
    # res = is_prime_fancy(num=num)
    # end = time.time_ns()
    #
    # print(f'Is prime fancy: {res}')
    # print(f'Time in ns: {end - start}')
    # print('-' * 10)
    #
    # start = time.time_ns()
    # res = is_prime_fancy(num=num, with_even=True)
    # end = time.time_ns()
    #
    # print(f'Is prime simple with even: {res}')
    # print(f'Time in ns: {end - start}')
    # print('-' * 10)

    res_prime = eratophen_sieve(50)
    print(f'Prime numbers: {res_prime}')
