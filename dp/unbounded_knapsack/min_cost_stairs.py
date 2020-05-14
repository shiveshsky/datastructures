class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        dp = [0]*(len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
        return min(dp[-1], dp[-2])


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([0, 0, 1, 1]))
    print(Solution().minCostClimbingStairs([10, 15, 20]))