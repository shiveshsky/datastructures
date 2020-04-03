import bisect


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def isfiesible(self, A, mid, B):
        n = len(A)
        cnt = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                val = mid - (A[i] + A[j])
                if val <= 0:
                    break
                it = bisect.bisect_left(A, val)
                if it == 0:
                    continue
                it -= 1
                idx = it - 0
                if idx > j:
                    cnt += idx - j
        if cnt < B:
            return True
        return False

    def solve(self, A, B):
        A.sort()
        l = A[0]
        h = A[-1] + A[-2] + A[-3]
        aa = 0
        while l <= h:
            mid = (l + h) // 2
            if self.isfiesible(A, mid, B):
                aa = max(aa, l)
                l = mid+1
            else:
                h = mid-1
        print(mid, l, h)
        return min(l,h)
# print(Solution().solve([2,4,3,2], 3))
print(Solution().solve([18, 23, 11, 16, 5, 23, 7, 20, 20, 10 ], 105))