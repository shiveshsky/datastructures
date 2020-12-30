class ZeroOneKnapsack:

    def solve(self, vals, weights, W):
        pass

    def recc(self, vals, weights, W):

        if len(weights) == 0 or W == 0:
            return 0
        else:
            if weights[-1] <= W:
                return max(
                    vals[-1] + self.recc(vals[0:-1], weights[0:-1], W - weights[-1]),
                    self.recc(vals[:-1], weights[:-1], W),
                )
            else:
                return self.recc(vals[0:-1], weights[0:-1], W)

    def memoization_runner(self, vals, weights, W):
        dp = [[-1 for i in range(0, len(weights) + 1)] for j in range(0, len(vals) + 1)]
        return self.memoization(vals, weights, W, dp)

    def memoization(self, vals, weights, W, dp):
        # here we make a dp matrix to memoize
        if len(weights) == 0 or W == 0:
            return 0
        else:
            if dp[vals[-1]][weights[-1]] != -1:
                return dp[vals[-1]][weights[-1]]

            if weights[-1] <= W:
                dp[vals[-1]][weights[-1]] = max(
                    self.recc(vals[0:-1], weights[0:-1], W - weights[0], dp),
                    self.recc(vals[:-1], weights[:-1], W, dp),
                )
                return dp[vals[-1]][weights[-1]]
            else:
                dp[vals[-1]][weights[-1]] = self.recc(vals[0:-1], weights[0:-1], W, dp)
                return dp[vals[-1]][weights[-1]]

    def top_down(self, vals, weights, W):
        dp = [[-1 for _ in range(0, W + 1)] for __ in range(0, len(vals) + 1)]
        for i in range(len(vals)+1):
            dp[i][0] = 0
        for j in range(W+1):
            dp[0][j] = 0
        for i in range(1,len(dp)):
            for j in range(1, len(dp[0])):
                if weights[i-1] <= j:
                    dp[i][j] = max(vals[i-1]+dp[i-1][j-weights[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

