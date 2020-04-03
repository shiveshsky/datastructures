from collections import Counter

# TODO IMPORTANT QUESTION


class Solution:
    def minWindow(self, A, B):
        need = Counter(B)
        l, r, i, j, missing = 0, 0, 0, 0, len(B)
        while r < len(A):
            if need[A[r]] > 0:
                missing -= 1
            need[A[r]] -= 1
            r += 1
            while missing == 0:
                if j == 0 or r - l < j - i:
                    i, j = l, r
                need[A[l]] += 1
                if need[A[l]] > 0:
                    missing += 1
                l += 1
        return A[i:j]


print(Solution().minWindow("ABOBECODEBANC", "ABC"))
# acbdnracbn abn
