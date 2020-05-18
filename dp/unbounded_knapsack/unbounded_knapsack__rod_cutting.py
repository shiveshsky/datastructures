class UnboundedKnapsack:
    '''
    in unbounded knapsack we either reject an item or select it
    but if we select it its possible that we again slelct it in future.
    in 0-1 knapsack in either case we decide upon an item only once.
    '''
    def solve(self, weights, vals, W):

        dp = [[-1 for i in range(0, W + 1)] for j in range(0, len(vals) + 1)]
        for i in range(len(vals) + 1):
            dp[i][0] = 0
        for j in range(W + 1):
            dp[0][j] = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if weights[i - 1] <= j:
                    dp[i][j] = max(vals[i - 1] + dp[i][j - weights[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
