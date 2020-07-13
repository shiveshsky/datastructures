import math


class Solution:
    def numSquares(self, n: int) -> int:
        values = []
        if n == 1:
            return 1
        i = 1
        while i ** 2 <= n:
            values.append(i ** 2)
            i += 1
        dp = [[-1 for _ in range(0, n + 1)] for j in range(0, len(values) + 1)]
        for i in range(len(values) + 1):
            dp[i][0] = 0
        for j in range(0, n + 1):
            dp[0][j] = math.inf - 1
        for k in range(1, (len(values) + 1)):
            for j in range(1, n + 1):
                if values[k - 1] <= j:
                    dp[k][j] = min(dp[k][j - values[k - 1]] + 1, dp[k - 1][j])
                else:
                    dp[k][j] = dp[k - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().numSquares(4))
