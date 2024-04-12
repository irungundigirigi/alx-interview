#!/usr/bin/python3
'''N Queens Challenge'''

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if board_size < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    queens_positions = []  # coordinates format [row, column]
    stop = False
    current_row = 0
    current_column = 0

    # iterate through rows
    while current_row < board_size:
        go_back = False
        # iterate through columns
        while current_column < board_size:
            # check if current column is safe
            is_safe = True
            for cord in queens_positions:
                col = cord[1]
                if col == current_column or col + (current_row - cord[0]) == current_column or col - (current_row - cord[0]) == current_column:
                    is_safe = False
                    break

            if not is_safe:
                if current_column == board_size - 1:
                    go_back = True
                    break
                current_column += 1
                continue

            # place queen
            cords = [current_row, current_column]
            queens_positions.append(cords)
            # if last row, append solution and reset all to last unfinished row
            # and last safe column in that row
            if current_row == board_size - 1:
                solutions.append(queens_positions[:])
                for cord in queens_positions:
                    if cord[1] < board_size - 1:
                        current_row = cord[0]
                        current_column = cord[1]
                for i in range(board_size - current_row):
                    queens_positions.pop()
                if current_row == board_size - 1 and current_column == board_size - 1:
                    queens_positions = []
                    stop = True
                current_row -= 1
                current_column += 1
            else:
                current_column = 0
            break
        if stop:
            break
        # on fail: go back to previous row
        # and continue from last safe column + 1
        if go_back:
            current_row -= 1
            while current_row >= 0:
                current_column = queens_positions[current_row][1] + 1
                del queens_positions[current_row]  # delete previous queen coordinates
                if current_column < board_size:
                    break
                current_row -= 1
            if current_row < 0:
                break
            continue
        current_row += 1

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)

