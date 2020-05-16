class Solution:
    def solve(self, A):
        cnt = 0
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == 1:
                    cnt += 1
                    self.dfs(A, i, j)
        return cnt

    def dfs(self, A, i, j):
        if i < 0 or i >= len(A):
            return
        if j < 0 or j >= len(A[0]):
            return
        if A[i][j] == 1:
            A[i][j] = 0
            self.dfs(A, i - 1, j - 1)
            self.dfs(A, i + 1, j + 1)
            self.dfs(A, i - 1, j)
            self.dfs(A, i + 1, j)
            self.dfs(A, i, j - 1)
            self.dfs(A, i, j + 1)
            self.dfs(A, i + 1, j - 1)
            self.dfs(A, i - 1, j + 1)
        return


if __name__ == '__main__':
    print(Solution().solve([
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]))
