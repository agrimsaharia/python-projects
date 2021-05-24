import random
import math

class Player:

    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        return random.choice(game.available_moves())

class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        val = None
        while True:
            square = input(self.letter + '\'s turn \nInput Move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                break
            except:
                print("Invalid square, try again!")
        return val

class GeniusComputerPlayer(Player):

    # memo = {}

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = self.minimax(game, self.letter)
        return square['position']
    
    def minimax(self, state, player):
        # if (tuple(state.board), state.current_winner, player) in self.memo: 
        #    return self.memo[(tuple(state.board), state.current_winner, player)]
           
        max_player = self.letter                        # player that should win the game
        other_player = 'O' if player == 'X' else 'X'    # player that has the next turn

        if state.current_winner == other_player:
            return {'position':None,                    # no position can be chosen now and score is the quickness of win/lose
                    'score':1*(state.num_empty_squares() + 1) if other_player==max_player else -1*(state.num_empty_squares() + 1)}

        elif not state.empty_squares():                 # tied game
            return {'position':None, 'score': 0}
        
        if player==max_player:
            best = {'position':None, 'score':-math.inf}
        else:
            best = {'position':None, 'score':math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)

            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            if player==max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        # self.memo[(tuple(state.board), state.current_winner, player)] = best
        return best

