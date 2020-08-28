class TicTacToe(object):

    def __init__(self, n):
        self.n = n
        self.rowv = [0] * n
        self.colv = [0] * n
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row, col, player):
        player_val = 1
        if player == 2:
            player_val = -1

        self.rowv[row] += player_val
        self.colv[col] += player_val

        if row == col:
            self.diag1 += player_val
            if abs(self.diag1) == self.n:
                return player
        if (self.n - 1 - row) == col:
            self.diag2 += player_val
            if abs(self.diag2) == self.n:
                return player

        if abs(self.rowv[row]) == self.n or abs(self.colv[col]) == self.n:
            return player
        else:
            return 0


if __name__ == '__main__':
    tt = TicTacToe(3)
    print(tt.move(0, 0, 1))
    print(tt.move(0, 2, 2))
    print(tt.move(2, 2, 1))
    print(tt.move(1, 1, 2))
    print(tt.move(2, 0, 1))
    print(tt.move(1, 0, 2))
    print(tt.move(2, 1, 1))
