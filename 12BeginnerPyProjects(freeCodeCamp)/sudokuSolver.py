import numpy as np
import time

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r,c] == -1:
                return r,c
    return None, None


def solve(puzzle):
    row, col = find_next_empty(puzzle)
    if row==None:
        return True
    
    for guess in range(1, 10):
        if isvalid(puzzle, guess, row, col):
            puzzle[row,col] = guess
            if solve(puzzle):
                return True   
        puzzle[row,col] = -1

    return False

def isvalid(puzzle, guess, row, col):
    if guess in puzzle[row]: return False
    elif guess in puzzle[:,col]: return False

    grid_r = (row//3)*3
    grid_c = (col//3)*3
    if guess in puzzle[grid_r:grid_r+3, grid_c:grid_c+3]: return False
    
    return True


if __name__ == '__main__':
    example_board = np.array([
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ])
    print(solve(example_board))
    print(example_board)
