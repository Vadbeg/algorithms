"""Calcluate the factorial of a number."""


def calculate_factorial_recursion(num: int = 5) -> int:
    if num < 0:
        raise ValueError()

    if num == 1 or num == 0:
        return num

    res = num * calculate_factorial_recursion(num=num - 1)

    return res


def calculate_factorial_iterative(num: int = 5) -> int:
    if num == 0:
        return num
    elif num < 0:
        raise ValueError()

    res = 1

    while num != 1:
        res = res * num
        num = num - 1

    return res


if __name__ == '__main__':
    res_recursion = calculate_factorial_recursion(num=1)
    res_iterative = calculate_factorial_iterative(num=1)

    print(res_recursion, res_iterative)


