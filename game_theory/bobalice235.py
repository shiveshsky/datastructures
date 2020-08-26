class Solution:
    # @param A : list of integers
    # @return a list of strings
    def solve(self, A):
        dp = [0] * (max(A) + 1)
        dp[2] = 1
        dp[3] = 1
        dp[4] = 1
        dp[5] = 1
        for i in range(6, max(A) + 1):
            dp[i] = (dp[i - 2] & dp[i - 3] & dp[i - 5]) ^ 1
        ans = []
        for i in A:
            if dp[i] == 1:
                ans.append("Alice")
            else:
                ans.append("Bob")
        return ans


if __name__ == '__main__':
    print(Solution().solve([2, 3, 5]))
