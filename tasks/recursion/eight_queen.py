"""Module with eight queen algorithm"""


from typing import List, Union, Tuple
from pprint import pprint


def is_under_attack(chess_board: List[List[Union[bool, int]]],
                    row_idx: int,
                    col_idx: int) -> bool:

    # vertical bottom line
    for row_idx_temp in range(row_idx + 1, len(chess_board)):
        if chess_board[row_idx_temp][col_idx]:
            return True

    # horizontal right line
    for col_idx_temp in range(col_idx + 1, len(chess_board[0])):
        if chess_board[row_idx][col_idx_temp]:
            return True

    # vertical top line
    for row_idx_temp in range(0, row_idx):
        if chess_board[row_idx_temp][col_idx]:
            return True

    # horizontal left line
    for col_idx_temp in range(0, col_idx):
        if chess_board[row_idx][col_idx_temp]:
            return True

    # diagonal left top line
    row_idx_temp = row_idx - 1
    col_idx_temp = col_idx - 1

    while row_idx_temp >= 0 and col_idx_temp >= 0:
        if chess_board[row_idx_temp][col_idx_temp]:
            return True

        row_idx_temp = row_idx_temp - 1
        col_idx_temp = col_idx_temp - 1

    # diagonal right bottom line
    row_idx_temp = row_idx + 1
    col_idx_temp = col_idx + 1

    while row_idx_temp < len(chess_board) and col_idx_temp < len(chess_board[0]):
        if chess_board[row_idx_temp][col_idx_temp]:
            return True

        row_idx_temp = row_idx_temp + 1
        col_idx_temp = col_idx_temp + 1

    # diagonal left bottom line
    row_idx_temp = row_idx + 1
    col_idx_temp = col_idx - 1

    while row_idx_temp < len(chess_board) and col_idx_temp >= 0:
        if chess_board[row_idx_temp][col_idx_temp]:
            return True

        row_idx_temp = row_idx_temp + 1
        col_idx_temp = col_idx_temp - 1

    # diagonal right top line
    row_idx_temp = row_idx - 1
    col_idx_temp = col_idx + 1

    while row_idx_temp >= 0 and col_idx_temp < len(chess_board[0]):
        if chess_board[row_idx_temp][col_idx_temp]:
            return True

        row_idx_temp = row_idx_temp - 1
        col_idx_temp = col_idx_temp + 1

    return False


def is_legal(chess_board: List[List[Union[bool, int]]]) -> bool:
    for row_idx, row in enumerate(chess_board):
        for col_idx, row_element in enumerate(row):
            if row_element:
                if is_under_attack(chess_board, row_idx, col_idx):
                    return False

    return True


def eight_queen(chess_board: List[List[Union[bool, int]]],
                num_queens_positioned: int = 0) -> bool:
    if not is_legal(chess_board=chess_board):
        return False

    if num_queens_positioned == 8:
        return True

    for row_idx, row in enumerate(chess_board):
        for col_idx, row_element in enumerate(row):
            if not chess_board[row_idx][col_idx]:
                chess_board[row_idx][col_idx] = True

                got_eight_queens = eight_queen(chess_board=chess_board,
                                               num_queens_positioned=num_queens_positioned + 1)

                if got_eight_queens:
                    return True

                chess_board[row_idx][col_idx] = False

    return False


if __name__ == '__main__':
    chess_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0]]

    # under_attack = is_under_attack(chess_board=chess_board, row_idx=0, col_idx=1)
    # print(f'Is under attack: {under_attack}')
    # exit()

    res = eight_queen(chess_board=chess_board, num_queens_positioned=0)

    print(res)

    sum_num = 0

    for row_idx in range(len(chess_board)):
        for col_odx in range(len(chess_board[0])):
            chess_board[row_idx][col_odx] = int(chess_board[row_idx][col_odx])

    pprint(chess_board)

    for row in chess_board:
        for el in row:
            sum_num += el

    print(f'Sum num: {sum_num}')
    print(f'Is legal chess board: {is_legal(chess_board=chess_board)}')