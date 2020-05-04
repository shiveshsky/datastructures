class CountSubsetGivenSum:
    def solve(self, arr, givensum):
        dp = [[False for i in range(givensum + 1)] for j in range(len(arr))]
        for i in range(givensum + 1):
            dp[0][i] = 0
        for j in range(len(arr)):
            dp[j][0] = 1
        for i in range(1, len(arr)+1):
            for j in range(1, givensum+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
