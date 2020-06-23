"""Module for checking have list cycle or have not"""

from data_structures.linked_list import Cell, LinkedList


def reverse(first_cell: Cell):
    """
    Reverse list

    :param first_cell: starting cell of list
    :return: new first cell
    """

    prev_cell = None
    curr_cell = first_cell

    while curr_cell is not None:
        next_cell = curr_cell.next_cell

        curr_cell.next_cell = prev_cell

        prev_cell = curr_cell
        curr_cell = next_cell

    return prev_cell


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


def have_cycle(first_cell: Cell) -> bool:
    """
    Checks if list have cycle or have not

    :param first_cell: first cell of LinkedList
    :return: if have True, else False
    """

    reversed_first_cell = reverse(first_cell=first_cell)
    reverse(first_cell=reversed_first_cell)  # returns list to state before reverse

    if reversed_first_cell == first_cell:
        return True

    return False


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

    cell_i.next_cell = cell_d

    str_list = get_str_list(first_cell=cell_a)
    print(str_list)

    have_cycle_bool = have_cycle(first_cell=cell_a)
    if have_cycle_bool:
        print('List have cycle')
    else:
        print('There is not cycle')

    str_list = get_str_list(first_cell=cell_a)
    print(f'List after checking: {str_list}')

