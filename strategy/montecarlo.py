from game import *

import time
import random
import itertools
import math


class Node:
    def __init__(self, me, parent=None):
        self.parent = parent
        self.children = {}

        self.me = me

        self.w = 0
        self.n = 0


class MontecarloPlayer:
    c = 0.3
    seconds = 1.

    def __init__(self, game):
        self.me = None

    def getmove(self, game):
        options = []
        for i in range(3):
            for j in range(3):
                if game[i,j] == EMPTY:
                    options.append((i,j))
        return random.choice(options)

    def simulate(self, game):
        turns = 0

        while not game.gameover():
            x, y = random.choice(
                [(x,y) for x in range(3) for y in range(3) if game.board[x][y] == EMPTY]
            )
            turns += 1
            game.play(x, y)

        winner = game.winner()
        value = 1. if winner == self.me else .5 if winner is -1 else 0.

        for _ in range(turns):
            game.rollback()

        return value

    def go(self, node, game, me):
        if node.n == 0 or game.gameover():
            value = self.simulate(game)

            c_node = node

            while not c_node is None:
                c_node.w += value
                c_node.n += 1.
                c_node = c_node.parent

            return

        done = False

        move = None
        value = None

        for x, y in itertools.product(range(3), range(3)):
            if game.board[x][y] != EMPTY:
                continue

            if not (x, y) in node.children:
                node.children[(x,y)] = Node(node.me, node)

                game.play(x,y)
                self.go(node.children[(x,y)], game, not me)
                game.rollback()
                done = True
                break

            else:
                n_node = node.children[(x,y)]
                w = n_node.w if me else n_node.n - n_node.w
                n_value = w / n_node.n + MonteCarloPlayer.c * (math.log(node.n) / n_node.n)**.5

                if value is None or n_value > value:
                    move = (x, y)
                    value = n_value

        if not done:
            game.play(*move)
            self.go(node.children[move], game, not me)
            game.rollback()

    def getmove(self, game):
        if self.me is None:
            self.me = game.player()

        self.root = Node(True)

        start_time = time.time()

        while time.time() < start_time + self.seconds:
            self.go(self.root, game, True)

        bestMove = None
        bestValue = None

        for x in self.root.children:
            value = self.root.children[x].w / self.root.children[x].n
            if bestValue is None or value > bestValue:
                bestValue = value
                bestMove = x

        print("Expected:", bestValue)
        return bestMove

class MonteCarloPlayer:
    c = 0.3

    def __init__(self, me, seconds):
        self.me = me
        self.seconds = seconds

    def update(self, game):
        self.game = game


    def go(self, node, game, me):
        if node.n == 0 or game.finalstate():
            value = self.simulate(game)

            c_node = node

            while not c_node is None:
                c_node.w += value
                c_node.n += 1.
                c_node = c_node.parent

            return

        done = False

        move = None
        value = None

        for x, y in itertools.product(range(3), range(3)):
            if self.game.board[x][y] != EMPTY:
                continue

            if not (x, y) in node.children:
                node.children[(x,y)] = Node(node.me, node)

                game.play(x,y)
                self.go(node.children[(x,y)], game, not me)
                game.rollback()
                done = True
                break

            else:
                n_node = node.children[(x,y)]
                w = n_node.w if me else n_node.n - n_node.w
                n_value = w / n_node.n + MonteCarloPlayer.c * (math.log(node.n) / n_node.n)**.5

                if value is None or n_value > value:
                    move = (x, y)
                    value = n_value

        if not done:
            game.play(*move)
            self.go(node.children[move], game, not me)
            game.rollback()

    def show_tree(self, node, depth, tabs=0):
        if depth < 0: return
        print("{} + {}/{} : {}".format("\t"*tabs, node.w, node.n, node.w / node.n))
        for x in node.children:
            print("{} - {}".format("\t"*tabs, repr(x)))
            self.show_tree(node.children[x], depth - 1, tabs+1)

    def get_move(self):
        self.root = Node(True)

        start_time = time.time()

        while time.time() < start_time + self.seconds:
            self.go(self.root, self.game, True)

        # print("TREE")
        # self.show_tree(self.root, 2)

        bestMove = None
        bestValue = None

        for x in self.root.children:
            value = self.root.children[x].w / self.root.children[x].n
            if bestValue is None or value > bestValue:
                bestValue = value
                bestMove = x

        print("Expected:", bestValue)
        return bestMove
