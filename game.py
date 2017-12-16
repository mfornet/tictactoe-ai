EMPTY = '.'
PLAYER0 = 'O'
PLAYER1 = 'X'


class TicTacToe:
    FINAL = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]

    def __init__(self):
        self.board = [[EMPTY] * 3 for i in range(3)]
        self.curplayer = 0
        self.history = []

    def play(self, x, y):
        if self[x,y] == EMPTY:
            self.history.append((x,y))
            self.board[x][y] = (PLAYER0, PLAYER1)[self.curplayer]
            self.curplayer ^= 1
            return True
        else:
            return False

    def rollback(self):
        x,y = self.history.pop()
        self.curplayer ^= 1
        self.board[x][y] = EMPTY

    def copy(self):
        cgame = TicTacToe()
        cgame.board = [row[:] for row in self.board]
        cgame.curplayer = self.curplayer
        return cgame

    def player(self):
        return self.curplayer

    def __getitem__(self, pos):
        x, y = pos
        return self.board[x][y]

    def winner(self):
        """
            0 if player0 is winner
            1 if player1 is winner
            -1 if game ends in a tie
            -2 if game has not ended yet
        """
        for row in TicTacToe.FINAL:
            p0, p1, p2 = row
            if EMPTY != self[p0] == self[p1] == self[p2]:
                if self[p0] == PLAYER0:
                    return 0
                else:
                    return 1

        return -1 if sum(1 for row in self.board for x in row if x == EMPTY) == 0 else -2

    def gameover(self):
        return self.winner() != -2

    def __hash__(self):
        return ((x for x in row) for row in self.board)

    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.board)