import math


class Solution:
    def solve(self, A, B, C, D):
        # left max array
        left_max = [0]*len(A)
        left_max[0] = B*A[0]
        for i in range(1, len(A)):
            left_max[i] = max(left_max[i - 1], B*A[i])
        right_max = [0] * len(A)
        right_max[-1] = D*A[-1]
        for i in range(len(A)-2, -1, -1):
            right_max[i] = max(A[i]*D, right_max[i+1])
        ans = -math.inf
        for i in range(0, len(A)):
            ans = max(ans, left_max[i] + C*A[i] + right_max[i])
        return ans

if __name__ == '__main__':
    print(Solution().solve())

