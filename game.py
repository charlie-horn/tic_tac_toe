import numpy as np
import tensorflow as tf

class Game():
    def __init__(self, p1, p2):
        #TODO change board to 1x27 and change winning criteria [[true where empty][true where X][true where O]]
        self.board = np.zeros(27)
        self.board[:9] = [1,1,1,1,1,1,1,1,1]
        self.moves = []
        self.p1 = p1
        self.p2 = p2
        self.winner = None
        self.over = False

    def isOver(self):
        if np.array_equal(self.board[0:9], np.zeros(9)):
            self.over = True
            self.winner = None
            return (self.over, self.winner)
        offset = 9
        p1_lines = [
            # Rows
                self.board[offset+0:offset+3],
                self.board[offset+3:offset+6],
                self.board[offset+6:offset+9],
            # Columns
                [self.board[offset+0],self.board[offset+3],self.board[offset+6]],
                [self.board[offset+1],self.board[offset+4],self.board[offset+7]],
                [self.board[offset+2],self.board[offset+5],self.board[offset+8]],
            # Diagonals
                [self.board[offset+0],self.board[offset+4],self.board[offset+8]],
                [self.board[offset+2],self.board[offset+4],self.board[offset+6]],
                ]
        offset = 18
        p2_lines = [
            # Rows
                self.board[offset+0:offset+3],
                self.board[offset+3:offset+6],
                self.board[offset+6:offset+9],
            # Columns
                [self.board[offset+0],self.board[offset+3],self.board[offset+6]],
                [self.board[offset+1],self.board[offset+4],self.board[offset+7]],
                [self.board[offset+2],self.board[offset+5],self.board[offset+8]],
            # Diagonals
                [self.board[offset+0],self.board[offset+4],self.board[offset+8]],
                [self.board[offset+2],self.board[offset+4],self.board[offset+6]],
                ]

        # Check if P1 won
        for line in p1_lines:
            if np.array_equal(line, [1,1,1]):
                self.over = True
                self.winner = self.p1
                break

        # Check if P2 won
        for line in p2_lines:
            if np.array_equal(line, [1,1,1]):
                self.over = True
                self.winner = self.p2
                break
        
        return (self.over, self.winner)
    
    def playGame(self, sess):
        ## Play a game
        j = 0
        while not self.over:
            result = tf.Variable(0)
            if j % 2 == 0:
                move = self.p1.move(self.board, sess)
                self.move(move, 1)
            else:
                move = self.p2.move(self.board, sess)
                self.move(move, 2)
            j += 1
        
        if self.winner == self.p1:
            self.p1.finishGame(1, sess)
            self.p2.finishGame(0, sess)
        elif self.winner == self.p2:
            self.p1.finishGame(0, sess)
            self.p2.finishGame(1, sess)
        else: 
            self.p1.finishGame(0.5, sess)
            self.p2.finishGame(0.5, sess)

    def move(self, move, id):
        self.board[move] = 0
        if id == 1:
            self.board[9+move] = 1
            self.moves.append(9+move)
        elif id == 2:
            self.board[18+move] = 1
            self.moves.append(18+move)
        return self.isOver()

    def show(self):
        print("|" + "" + "" )