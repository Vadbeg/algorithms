"""Recursive solving of tower of hanoi puzzle"""


def tower_of_hanoi(n: int, from_rod: str, to_rod: str, help_rod: str):
    """
    Easy solving of tower of hanoi puzzle.
    I have induction proof in Algorithms p.1 notebook

    :source: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
    :param n: number of discs
    :param from_rod: from which rod move
    :param to_rod: to which rod move
    :param help_rod: helping rod
    :return: None
    """

    if n == 1:
        print(f'Move {n} disk from {from_rod} to {to_rod}')
        return

    tower_of_hanoi(n - 1, from_rod, help_rod, to_rod)
    print(f'Move disk: {n} from {from_rod} to: {to_rod}')
    tower_of_hanoi(n - 1, help_rod, to_rod, from_rod)


if __name__ == '__main__':
    n = 2
    from_rod_main = 'A'
    help_rod_main = 'B'
    to_rod_main = 'C'

    tower_of_hanoi(n=n, from_rod=from_rod_main,
                   to_rod=to_rod_main,
                   help_rod=help_rod_main)


