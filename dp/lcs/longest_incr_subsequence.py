class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A):

        dp = [1 for _ in range(len(A)+1)]

        for i in range(0, len(A)):
            for j in range(i-1, -1, -1):
                if A[i] > A[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

if __name__ == '__main__':
    print(Solution().solve([10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]))
