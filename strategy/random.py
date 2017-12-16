from game import *
import random


class RandomPlayer:
    def __init__(self, game):
        pass

    def getmove(self, game):
        options = []
        for i in range(3):
            for j in range(3):
                if game[i,j] == EMPTY:
                    options.append((i,j))
        return random.choice(options)
