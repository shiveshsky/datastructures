class Solution:
    def minDistance(self, A, B):
        dp = [[0 for x in range(len(A)+1)] for x in range(len(B)+1)]
        for i in range(0, len(dp)):
            dp[i][0] = i
        for j in range(0, len(dp[0])):
            dp[0][j] = j
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if A[j-1] == B[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+ min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().minDistance("Anshuman", "Antihuman"))

