class Solution:
    def solve(self, A, B, C, D):
        sweetness = [B[i] * A[i] for i in range(0, len(A))]
        dp = [[0 for _ in range(D + 1)] for i in range(0, len(C) + 1)]
        for i in range(1, len(C) + 1):
            for j in range(1, D + 1):
                if C[i - 1] <= j:
                    dp[i][j] = max(sweetness[i - 1] + dp[i][j - C[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().solve([1, 2, 3], [2, 2, 10], [2, 3, 9], 8))
