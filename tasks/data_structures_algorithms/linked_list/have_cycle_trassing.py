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


def has_cycle_retracing(first_cell: Cell):
    cell = first_cell

    while cell.next_cell is not None:
        tracer = first_cell

        while tracer != cell:
            if tracer.next_cell == cell.next_cell:
                print(f'Cell value: {cell.value}')
                cell.next_cell = None

                return True

            tracer = tracer.next_cell

        cell = cell.next_cell

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
    cell_1 = Cell(next_cell=cell_a, value='1')
    cell_2 = Cell(next_cell=cell_1, value='2')
    cell_3 = Cell(next_cell=cell_2, value='3')
    cell_4 = Cell(next_cell=cell_3, value='4')

    cell_i.next_cell = cell_d

    str_list = get_str_list(first_cell=cell_4)
    print(str_list)

    have_cycle_bool = has_cycle_retracing(first_cell=cell_4)
    if have_cycle_bool:
        print('List have cycle')
    else:
        print('There is no cycle')

    str_list = get_str_list(first_cell=cell_4)
    print(f'List after checking: {str_list}')

