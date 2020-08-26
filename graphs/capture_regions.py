# class Solution:
#     def solve(self, A):
#         for i in range(0, len(A)):
#             for j in range(0, len(A[0])):
#                 if A[i][j] == 'O':
#                     A[i][j] = '-'
#         for i in range(len(A)):
#             if A[i][0] == '-':
#                 self.floodfill(A, i, 0, '-', 'O')
#         for i in range(len(A)):
#             if A[i][(len(A[0])) - 1] == '-':
#                 self.floodfill(A, i, len(A[0]), '-', 'O')
#         for i in range(len(A[0])):
#             if A[0][i] == '-':
#                 self.floodfill(A, 0, i, '-', 'O')
#
#         for i in range(len(A[0])):
#             if A[len(A) - 1][i] == '-':
#                 self.floodfill(A, len(A) - 1, i, '-', 'O')
#
#         for i in range(len(A)):
#             for j in range(len(A[0])):
#                 if A[i][j] == '-':
#                     A[i][j] = 'X'
#         return A
#
#     def floodfill(self, arr, x, y, prevV, newV):
#         if x < 0 or x > len(arr) or y < 0 or y > len(arr[0]):
#             return
#         if arr[x][y] != prevV:
#             return
#         arr[x][y] = newV
#         self.floodfill(arr, x + 1, y, prevV, newV)
#         self.floodfill(arr, x - 1, y, prevV, newV)
#         self.floodfill(arr, x, y + 1, prevV, newV)
#         self.floodfill(arr, x, y - 1, prevV, newV)
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(0, len(board)):
            if board[i][0] == 'O':
                self.dfs(i, 0, board)
        for i in range(0, len(board[0])):
            if board[0][i] == 'O':
                self.dfs(0, i, board)
        for j in range(0, len(board)):
            if board[j][len(board[0]) - 1] == 'O':
                self.dfs(j, len(board[0]) - 1, board)
        for j in range(0, len(board[0])):
            if board[len(board) - 1][j] == 'O':
                self.dfs(len(board) - 1, j, board)

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == '$':
                    board[i][j] = 'O'
        return board

    def dfs(self, i, j, board):
        if i < 0 or j < 0:
            return
        if i > len(board) - 1 or j > len(board[0]) - 1:
            return
        if board[i][j] == 'X' or board[i][j] == '$':
            return
        if board[i][j] == 'O':
            board[i][j] = '$'
        self.dfs(i + 1, j, board)
        self.dfs(i, j + 1, board)
        self.dfs(i - 1, j, board)
        self.dfs(i, j - 1, board)


if __name__ == '__main__':
    print(Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
