#!/usr/bin/python3
from settings import *
import strategy

import pygame, sys
from pygame.locals import QUIT, MOUSEBUTTONUP

from visual import Board
from game import TicTacToe

def main():
    pygame.init()
    clock = pygame.time.Clock()

    # Create game

    tictactoe = TicTacToe()
    board = Board(tictactoe, **BOARD_ARGS)

    # Initialize players

    player0 = (PLAYER0, strategy.load_player(PLAYER0)(tictactoe))
    player1 = (PLAYER1, strategy.load_player(PLAYER1)(tictactoe))

    ACTIVE_PLAYER = player0
    PASIVE_PLAYER = player1

    pygame.display.update()

    # Start games

    while True:
        if tictactoe.winner() == -2:
            if ACTIVE_PLAYER[0] == USER:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEBUTTONUP:
                        x, y = event.pos
                        if board.process_click(x, y):
                            ACTIVE_PLAYER, PASIVE_PLAYER = PASIVE_PLAYER, ACTIVE_PLAYER
            else:
                pos = ACTIVE_PLAYER[1].getmove(tictactoe.copy())
                if not board.play_turn(pos):
                    raise ValueError("{}: \nInvalid move:{}".format(ACTIVE_PLAYER[0], str(pos)))
                ACTIVE_PLAYER, PASIVE_PLAYER = PASIVE_PLAYER, ACTIVE_PLAYER
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()