class Solution:
    """
        Bottom up – Start from the nodes on the bottom row; the min pathsum for these nodes are the values of the nodes themselves. And after that, minimum pathsum at the ith node of kth row would be the minimum of the pathsum of its two children + the node’s value, i.e.:

        memo[k][i] = min( memo[k+1][i], memo[k+1][i+1]) + A[k][i];
        OR
        Simply set memo as a 1D array, and update it
        this will be space efficient also :

        For the row k :

        memo[i] = min( memo[i], memo[i+1]) + A[k][i];
    """
    def minimumTotal(self, A):
        dp = [i for i in A[-1]]
        for i in range(len(A)-2, -1, -1):
            for j in range(0, len(A[i])):
                dp[j] = A[i][j]+min(dp[j], dp[j+1])
        return dp[0]


if __name__ == '__main__':
    print(Solution().minimumTotal([[2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]]))
