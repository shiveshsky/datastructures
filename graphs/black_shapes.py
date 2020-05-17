class Solution:
    def black(self, A):
        adg = [list(i) for i in A]
        cnt = 0
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if adg[i][j] == 'X':
                    cnt += 1
                    self.dfs(adg, i, j)
        return cnt

    def dfs(self, A, i, j):
        if i < 0 or i >= len(A):
            return
        if j < 0 or j >= len(A[0]):
            return
        if A[i][j] == 'X':
            A[i][j] = 'O'
            self.dfs(A, i + 1, j)
            self.dfs(A, i - 1, j)
            self.dfs(A, i, j + 1)
            self.dfs(A, i, j - 1)
        return


if __name__ == '__main__':
    print(Solution().black(["XO", "OX"]))
