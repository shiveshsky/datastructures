class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        cnt = 0
        dp = [{} for i in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[i].get(diff, 0) + 1 + dp[j].get(diff, 0)
                cnt += dp[j].get(diff, 0)
        return cnt


if __name__ == '__main__':
    print(Solution().solve([1, 3, 5, 7, 9, 10, 15]))
