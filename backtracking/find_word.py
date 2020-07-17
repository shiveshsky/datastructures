class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(i, j, word, 0, board):
                    return True

        return False

    def dfs(self, i, j, w, c, board):
        if c == len(w):
            return True

        if (
                i < 0
                or j >= len(board[0])
                or i >= len(board)
                or j < 0
                or board[i][j] != w[c]
        ):
            return False

        temp = board[i][j]
        board[i][j] = " "

        found = (
                self.dfs(i + 1, j, w, c + 1, board)
                or self.dfs(i - 1, j, w, c + 1, board)
                or self.dfs(i, j + 1, w, c + 1, board)
                or self.dfs(i, j - 1, w, c + 1, board)
        )

        board[i][j] = temp

        return found


if __name__ == "__main__":
    print(Solution().exist([["a", "b"], ["c", "d"]], "cdba"))
    # print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
# "ABCB"))
