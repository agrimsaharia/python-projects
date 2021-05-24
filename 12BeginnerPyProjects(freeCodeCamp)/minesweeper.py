import random
import numpy as np
class Board:

    def __init__(self, dimsize, num_bombs):
        self.dug = set()
        self.dimsize = dimsize
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values()

    
    def make_new_board(self):
        board = np.zeros((self.dimsize, self.dimsize), dtype='int8')
        loc = np.asarray(random.sample(range(0, self.dimsize**2), self.num_bombs), dtype='int8')
        self.bomb_col = loc % self.dimsize
        self.bomb_row = loc // self.dimsize
        board[self.bomb_row, self.bomb_col] = -self.num_bombs-1
        return board


    def clip(self, x, idx=True):  # this is a private method
        if x > self.dimsize-1:
            return self.dimsize-1
        elif x < 0:
            return 0
        else:
            return x


    def assign_values(self):
        for row, col in zip(self.bomb_row, self.bomb_col):
            self.board[self.clip(row-1):self.clip(row+1)+1, self.clip(col-1):self.clip(col+1)+1] += 1
        

    def dig(self, row, col):
        if (row, col) in self.dug:
            print("You already dug that!! Duh!?")
            return True
        if self.board[row, col] < 0:
            return False
        elif self.board[row, col] > 0:
            self.dug.add((row, col))
            return True
        else:
            self.dug.add((row, col))
            for r in range(-1, 2):
                for c in range(-1, 2):
                    if (self.clip(row+r), self.clip(col+c)) in self.dug: continue
                    self.dig(self.clip(row+r), self.clip(col+c))
            return True

    # def __str__(self):
    #     visible = [[' | -' for _ in range(self.dimsize)] for _ in range(self.dimsize)]
    #     for row in range(self.dimsize):
    #         for col in range(self.dimsize):
    #             if (row,col) in self.dug:
    #                 visible[row][col] = ' | ' + str(self.board[row, col])
    #     return f'{visible}'

    def printBoard(self, win=False):
        for row in range(-1,self.dimsize):
            if row!=-1: print(row,'->', end='')
            else: print('*','-> ', end='')
            for col in range(self.dimsize):
                if row == -1:
                    print(' \''+str(col), end='\'')
                else:
                    if (row, col) in self.dug:
                        print(' | ' + str(self.board[row, col]), end='')
                    else:
                        if win==True: print(' | *', end='')
                        else: print(' | _', end='')
            if row!=-1: print(' |')
            else: print()



def play(dimsize=10, num_bombs=10):
    board = Board(dimsize, num_bombs)

    while len(board.dug) != dimsize**2 - num_bombs:
        board.printBoard()
        try:
            row,col = (map(int, input("input the row and column separated by space: ").strip().split()))
            if board.clip(row) != row or board.clip(col) != col:
                raise ValueError
        except KeyboardInterrupt:
            return None
        except:
            print("input correct value please!")
            continue

        if not board.dig(row,col):
            print("BOOOOOM!!!!!\n\nYou lose!")
            return None
    board.printBoard(win=True)
    print("Yay! you Won! :)")
    return None
play(10, 10)
