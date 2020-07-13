import math


class Solution:
    def solve(self, num):
        # here we need to minimize sum as close to mid val to get minimum difference

        weight = sum(num) // 2
        dp = [math.inf for _ in range(weight + 1)]
        dp[0] = 0

        for i in range(1, len(num) + 1):
            for j in range(1, weight + 1):
                if num[i - 1] <= j:
                    # TODO take into consideration j-num[i-1] is positive index
                    # else in python it will come from other side :
                    dp[j] = min(dp[j - num[i - 1]] + 1, dp[j])
        for i in range(weight // 2, 0, -1):
            if dp[i] != math.inf:
                return dp[i]


if __name__ == '__main__':
    print(Solution().solve([15, 10, 6]))
