import math


class CoinChangeMaxWays:
    def solve(self, coins, amount):
        dp = [[-1 for i in range(0, amount + 1)] for j in range(0, len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 0
        for j in range(0, amount + 1):
            dp[0][j] = math.inf -1

        for i in range(1, len(coins)):
            for j in range(1, len(amount+1)):
                if coins[i - 1] <= j:
                    dp[i][j] = min(dp[i][j - amount[i - 1]] + 1, dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    print(CoinChangeMaxWays().solve([1, 2, 5], 11))
