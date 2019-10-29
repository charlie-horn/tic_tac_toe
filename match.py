import tensorflow as tf
from game import Game

class Match():
    def __init__(self, max_games, p1, p2):
        self.games = []
        self.max_games = max_games
        self.p1 = p1
        self.p1_wins = 0
        self.p2 = p2
        self.p2_wins = 0
        self.draws = 0
        self.startMatch()

    def startMatch(self):
        init = tf.global_variables_initializer()
        with tf.Session() as sess:
            init.run()
            i = 0
            while i < self.max_games:
                i += 1
                print("Playing Game " + str(i))
                self.p1.newGame()
                self.p2.newGame()
                game = Game(self.p1, self.p2)
                game.playGame(sess)
                if game.winner == self.p1:
                    self.p1_wins += 1
                elif game.winner == self.p2:
                    self.p2_wins += 1
                else:
                    self.draws += 1
                #self.games.append(game)
        sess.close()