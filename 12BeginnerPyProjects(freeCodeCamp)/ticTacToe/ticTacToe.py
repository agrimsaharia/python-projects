import player
import time 

class TicTacToe:

    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def printBoard(self):
        # TODO: optimize this for loop
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # TODO: implement this function if found necessary
    # @staticmethod
    # def printBoardLetters():
    #     letter_board = [[for str(i) in range(j*3, (j+1)*3)]]

    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check rows
        row_idx = square//3
        if all([i==letter for i in self.board[row_idx*3:row_idx*3+3]]):
            return True

        # check columns
        col_idx = square%3
        if all([i==letter for i in [self.board[j] for j in range(col_idx, 9, 3)]]):
            return True

        # check diagonals
        # check for even squares [0, 4, 8] or [2, 4, 6]
        if all([self.board[i] == letter for i in [0,4,8]]):
            return True
        if all([self.board[i] == letter for i in [2, 4, 6]]):
            return True

        #else return False
        return False

def play(game, x_player, o_player, print_game=True):
    letter = 'X'

    if print_game:
        game.printBoard()

    while game.empty_squares():
        if letter=='O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter, "makes a move to the square", square)
                game.printBoard()
                print()

        if game.current_winner:
            if print_game:
                print(letter, "wins!    :)")
            return letter

        letter = 'X' if letter == 'O' else 'O'
        if print_game:
            time.sleep(1)

    if print_game:
        print("it's a tie... :(")

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for i in range(2):
        x_player = player.HumanPlayer('X')
        o_player = player.GeniusComputerPlayer('O')
        t = TicTacToe()
        letter = play(t, x_player, o_player, print_game=True)
        # print(letter)
        if letter == 'X':
            x_wins += 1
        elif letter == 'O':
            o_wins += 1 
        else:
            ties += 1

    print(x_wins, o_wins, ties)
