import numpy as np
from network import Network
import tensorflow as tf

class Player():
    def __init__(self, id, num_hidden, learning_rate, discount):
        #initialize
        self.id = id
        self.discount = discount
        self.training = True
        self.moves = []
        self.board_states = []
        self.q_values = []
        self.next_max_q_values = []
        self.network = Network(27, num_hidden, learning_rate)
        self.random_moves = 0

    def newGame(self):
        #TODO reset any variables that need to be set per game
        self.moves = []
        self.board_states = []
        self.q_values = []
        self.next_max_q_values = []
        pass

    def calculateTargets(self):
        #TODO apply discount rate to next Q values
        num_moves = len(self.moves)
        targets = []
        for i in range(num_moves):
            target = self.q_values[i]
            target[self.moves[i]] = self.discount * self.next_max_q_values[i]
            targets.append(target)
        return targets

    def getProbabilities(): 
        #TODO accept q values and provide normalized probabilities
        return 0

    def move(self, board, sess):
        input_board = board.reshape(1,27)
        self.board_states.append(board) #Why do .copy()?
        actions = self.network.getOutput(input_board, sess)[0]
        self.q_values.append(actions)
        for i, _ in enumerate(actions):
            if input_board[0,i] == 0:
                actions[i] = 0
        if np.array_equal(actions, np.zeros(9)):
            move = chooseRandom(input_board)
            self.random_moves += 1
        else:

            ### Code to select a move by probability distribution
            #num_possible_moves = 9 - len(game.moves)
            #probabilities = actions/sum(actions)
            #action = tf.multinomial( probabilities, num_samples=1)
            #action_flt = tf.to_float(action)
            #print("Action" + str(action_flt))
            #print(str(self.id) + str(actions))
            move = np.argmax(actions)

        if len(self.moves) > 0:
            self.next_max_q_values.append(actions[move])
        self.moves.append(move)
        self.q_values.append(actions)

        return move

    def finishGame(self, result, sess):
        self.next_max_q_values.append(result)
        if self.training:
            targets = self.calculateTargets()
            predictions = self.board_states
            sess.run([self.network.minimize_loss], 
                feed_dict={
                            self.network.input_layer: predictions, 
                            self.network.target_q_values: targets
                            })
        