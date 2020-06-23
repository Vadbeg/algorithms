"""Module with LinkedList"""

# TODO: is not ready yet

from typing import Any


class LinkedList:
    def __init__(self):
        self.first_cell = None

    def append(self, value: Any = None):
        if self.first_cell is None:
            self.first_cell = Cell(next_cell=None, value=value)
        else:
            curr_cell = self.first_cell

            while curr_cell.next_cell is not None:
                curr_cell = curr_cell.next_cell

            curr_cell.next_cell = Cell(next_cell=None, value=value)

    def __str__(self):
        list_str = '['

        curr_cell = self.first_cell
        while curr_cell.next_cell is not None:
            list_str += str(curr_cell.value) + ', '

            curr_cell = curr_cell.next_cell

        list_str += str(curr_cell.value) + ']'

        return list_str


class Cell:
    def __init__(self, next_cell: 'Cell' = None, value: Any = None):
        self.next_cell = next_cell
        self.value = value


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append(4)
    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(46)
    linked_list.append(41)

    print(linked_list)
