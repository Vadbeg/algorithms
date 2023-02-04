"""Module for checking have list cycle or have not using Floyd Hare and Tortoise algorithm"""

from typing import Tuple
from tasks.data_structures.linked_list import Cell


def get_str_list(first_cell: Cell) -> str:
    """
    Returns str(list) like string with elements of LinkedList

    :param first_cell: first cell of LinkedList
    :return: str with LinkedList elements
    """

    list_str = '['

    visited_nodes = list()

    curr_cell = first_cell
    while curr_cell.next_cell is not None and curr_cell not in visited_nodes:
        visited_nodes.append(curr_cell)

        list_str += str(curr_cell.value) + ', '

        curr_cell = curr_cell.next_cell

    list_str += str(curr_cell.value) + ']'

    return list_str


def floyd_have_cycle(first_cell: Cell) -> Tuple[int, int]:
    """
    Find length and staring node of cycle if there is one.
    If there is no cycle returns Tuple[-1, -1]

    :source: https://en.wikipedia.org/wiki/Cycle_detection
    :youtube: https://www.youtube.com/watch?v=LUm2ABqAs1w
    :param first_cell: starting cell of the linked list
    :return: length of the cycle, starting index of the cycle
    """
    tortoise = first_cell.next_cell
    hare = first_cell.next_cell.next_cell

    while tortoise != hare:
        tortoise = tortoise.next_cell

        if hare.next_cell is None or hare.next_cell.next_cell is None:
            return -1, -1

        hare = hare.next_cell.next_cell

    mu = 0
    tortoise = first_cell

    while tortoise != hare:
        tortoise = tortoise.next_cell
        hare = hare.next_cell

        mu += 1

    lam = 1
    hare = tortoise.next_cell
    while tortoise != hare:
        hare = hare.next_cell
        lam += 1

    return lam, mu


if __name__ == '__main__':
    cell_i = Cell(next_cell=None, value='i')
    cell_h = Cell(next_cell=cell_i, value='h')
    cell_g = Cell(next_cell=cell_h, value='g')
    cell_f = Cell(next_cell=cell_g, value='f')
    cell_e = Cell(next_cell=cell_f, value='e')
    cell_d = Cell(next_cell=cell_e, value='d')
    cell_c = Cell(next_cell=cell_d, value='c')
    cell_b = Cell(next_cell=cell_c, value='b')
    cell_a = Cell(next_cell=cell_b, value='a')
    cell_1 = Cell(next_cell=cell_a, value='a')
    cell_2 = Cell(next_cell=cell_1, value='a')

    cell_d.next_cell = cell_d

    str_list = get_str_list(first_cell=cell_2)

    # cell_i.next_cell = cell_d

    lam, mu = floyd_have_cycle(first_cell=cell_a)
    if lam != -1 and mu != -1:
        print('List have cycle')
    else:
        print('There is no cycle')

    print(f'Length of the cycle: {lam}')
    print(f'Number of cycle starting node : {mu}')

    str_list = get_str_list(first_cell=cell_a)
    print(f'List after checking: {str_list}')

