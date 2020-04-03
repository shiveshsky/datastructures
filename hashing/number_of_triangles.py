from collections import Counter


class Solution:
    def solve(self, A, B):
        count_x = Counter(A)
        count_y = Counter(B)
        ans = 0
        mod = 10 ** 9 + 7
        for i in range(len(A)):
            ans = (((count_x[A[i]] - 1) * (count_y[B[i]] - 1)) % mod + ans % mod) % mod
        return ans


print(Solution().solve([1, 1, 2, 2, 3, 3], [1, 2, 1, 2, 1, 2]))
