class Solution:
    def solve(self, A):
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == 'O':
                    A[i][j] = '-'
        for i in range(len(A)):
            if A[i][0] == '-':
                self.floodfill(A, i, 0, '-', 'O')
        for i in range(len(A)):
            if A[i][(len(A[0])) - 1] == '-':
                self.floodfill(A, i, len(A[0]), '-', 'O')
        for i in range(len(A[0])):
            if A[0][i] == '-':
                self.floodfill(A, 0, i, '-', 'O')

        for i in range(len(A[0])):
            if A[len(A) - 1][i] == '-':
                self.floodfill(A, len(A) - 1, i, '-', 'O')

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == '-':
                    A[i][j] = 'X'
        return A

    def floodfill(self, arr, x, y, prevV, newV):
        if x < 0 or x > len(arr) or y < 0 or y > len(arr[0]):
            return
        if arr[x][y] != prevV:
            return
        arr[x][y] = newV
        self.floodfill(arr, x + 1, y, prevV, newV)
        self.floodfill(arr, x - 1, y, prevV, newV)
        self.floodfill(arr, x, y + 1, prevV, newV)
        self.floodfill(arr, x, y - 1, prevV, newV)
