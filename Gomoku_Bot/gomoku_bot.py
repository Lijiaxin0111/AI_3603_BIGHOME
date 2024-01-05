from .minmax import *
import time
from .board import Board


class Gomoku_bot:
    def __init__(self, board_size, first_role = 1, role = 1, depth=4, enableVCT=False):
        self.board = Board(board_size, first_role) # -1 for black, 1 for white, -1 means 2
        self.role = role
        self.depth = depth
        self.enableVCT = enableVCT
        self.player = 0
        self.board_size = board_size

    def set_player_ind(self, p):
        self.player = p

    def set_role(self, first_role = 1, role = 1):
        self.role = role
        self.board = Board(self.board_size, first_role)

    def get_action(self, return_time=True, board = None):

        start = time.time()
        score = minmax(self.board, self.role, self.depth, self.enableVCT)
        end = time.time()
        sim_time = end - start
        move = score[1] # this move starts from left up corner (0,0), however, the move in the game starts from left bottom corner (0,0)
        move = (self.board.size - 1 - move[0], move[1]) # convert the move to the game's coordinate
        # turn tuple into an int
        move = move[0] * self.board.size + move[1]
        print(f"action from gomoku bot, with time: {sim_time}")
        if return_time:
            return move, sim_time
        else:
            return move
