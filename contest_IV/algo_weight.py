class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def __init__(self):
        self.dp = []

    def solve(self, A, B):
        self.dp = [[-1] * len(B) for _ in range(len(B))]
        return self.wightlifting(A, B, 0, len(B) - 1)

    def wightlifting(self, A, B, i, j):
        if i > j:
            return 0
        if B[i] > A and B[j] > A:
            self.dp[i][j] = 0
            return 0
        l = 0
        r = 0
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        if B[i] <= A:
            l = self.wightlifting(A, B, i + 1, j)
        if B[j] <= A:
            r = self.wightlifting(A, B, i, j - 1)
        self.dp[i][j] = max(l, r) + 1
        return self.dp[i][j]
