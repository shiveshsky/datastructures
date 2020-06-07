class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dp = [0] * (len(A) + 1)
        dp[1] = 0
        if len(A) > 2:
            dp[2] = min(dp[0], dp[1]) + B * abs(A[1] - A[0])
            for i in range(3, len(A) + 1):
                one = 0
                two = 0
                one = dp[i - 1] + B * abs(A[i - 1] - A[i - 2])
                two = dp[i - 2] + C * abs(A[i - 3] - A[i - 1])
                dp[i] = min(one, two)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().solve([1, 2, 3], 2, 3))
