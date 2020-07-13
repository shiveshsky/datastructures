class SubsetsWithGivenDiff:
    def solve(self, arr, diff):
        '''
            :logic
            s1 + s2 = sumarr ----(1)
            s1 - s2 = diff ------(2)
          ---------------------
            2s1 = sumarr - diff
            s1  = (sumarr - diff)//2
            so this reduces to count subsets with given sum
        '''
        sumarr = sum(arr)
        req_sum = (sumarr - diff)//2
        dp = [[0 for _ in range(0, req_sum+1)] for i in range(0, len(arr)+1)]
        for i in range(req_sum + 1):
            dp[0][i] = 0
        for j in range(len(arr)):
            dp[j][0] = 1
        for i in range(1, len(arr)+1):
            for j in range(1, req_sum+1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

