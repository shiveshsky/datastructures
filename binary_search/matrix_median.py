from bisect import bisect_right, bisect_left


class Solution:
    
    def binaryMedian(self, A):
        mi = A[0][0]
        mx = 0
        r = len(A)
        d = len(A[0])
        for i in range(r):
            if A[i][0] < mi:
                mi = A[i][0]
            if A[i][d - 1] > mx:
                mx = A[i][d - 1]

        desired = (r * d + 1) // 2

        while (mi < mx):
            mid = (mi + mx) // 2
            place = [0];

            # Find count of elements smaller than mid
            for i in range(r):
                j = bisect_right(A[i], mid)
                place[0] = place[0] + j
            if place[0] < desired:
                mi = mid + 1
            else:
                mx = mid

        return mi
