import math


class Solution:
    def solve(self, num):
        weight = sum(num) // 2
        dp = [[math.inf for _ in range(weight + 1)] for _ in range(0, len(num) + 1)]
        dp[0][0] = 0
        for i in range(1, len(num) + 1):
            dp[i][0] = 0
        for i in range(1, len(num) + 1):
            for j in range(1, weight + 1):
                if num[i - 1] <= j:
                    # TODO take into consideration j-num[i-1] is positive index
                    dp[j] = min(dp[i - 1][j - num[i - 1]], dp[i - i][j + num[i - 1]])
        for i in range(weight // 2, 0, -1):
            if dp[i] != math.inf:
                return dp[i]


if __name__ == '__main__':
    print(Solution().solve([15, 10, 6]))
