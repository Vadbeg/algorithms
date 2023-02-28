"""Calculate fibonacci sequence"""


def calculate_fibonacci_recursive(idx: int) -> int:
    if idx == 0:
        return 0

    if idx == 1:
        return 1

    num = calculate_fibonacci_recursive(idx=idx-1) + calculate_fibonacci_recursive(idx=idx-2)

    return num


def calculate_fibonacci_iterative(idx: int) -> int:
    if idx == 0:
        return 0

    if idx == 1:
        return 1

    first_value = 0
    second_value = 1

    number = 0

    for _ in range(2, idx + 1):
        number = first_value + second_value
        first_value = second_value
        second_value = number

    return number


if __name__ == '__main__':

    res_recursive = []
    for i in range(10):
        curr_num = calculate_fibonacci_recursive(idx=i)
        res_recursive.append(str(curr_num))

    res_iterative = []
    for i in range(10):
        curr_num = calculate_fibonacci_iterative(idx=i)
        res_iterative.append(str(curr_num))

    print('res_recursive',  ' '.join(res_recursive))
    print('res_iterative', ' '.join(res_iterative))
