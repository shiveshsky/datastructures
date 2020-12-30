class Solution:
    def solve(self, arr, SUM):
        dp = [[False for i in range(0, SUM + 1)] for j in range(0, len(arr) + 1)]
        # empty subsets
        for i in range(len(arr)+1):
            dp[i][0] = True
        for j in range(1, SUM+1):  # no number to choose from array
            dp[0][j] = False
        for i in range(1, len(arr)+1):
            for j in range(1, SUM+1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[i-1][j-1]
