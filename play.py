## Idea: break up the code so that people can submit a player type that takes certain inputs,
#  so people ca try to have the player that learns the fastest

####### Libraries #######

import sys
import numpy as np
import tensorflow as tf
from game import Game
from match import Match
from player import Player
from network import Network

####### Functions #######

def parseArgs():
    for arg in sys.args():
        # Do some stuff
        pass

def chooseRandom(board):
    #TODO make this only look at available moves
    print("Choosing a random move....")
    while True:
        move = np.random.randint(0,9)
        if board[move] == 1:
            break
    return move

####### Main #######
if __name__ == "__main__":
    p1 = Player(1, 243, 0.2, 0.95)
    p2 = Player(2, 243, 0.2, 0.95)
    match = Match(100, p1, p2)
    print("Match Summary:",
        "\n\tPlayer 1 wins:",match.p1_wins,
        "\n\tPlayer 2 wins:",match.p2_wins,
        "\n\tDraws:",match.draws)