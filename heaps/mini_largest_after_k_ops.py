from heapq import heapify, heappush, heappop

from heapq import heapify, heappush, heappop

# class CustomVal:
#     def __init__(self, val, oldval):
#         self.val = val
#         self.oldval = oldval
#
#     def __lt__(self, other):
#         return self.val+self.oldval < other.val+other.oldval
#
# class Solution:
#     def solve(self, A, B):
#         minheap = []
#         heapify(minheap)
#         for i in range(0, len(A)):
#             heappush(minheap, CustomVal(A[i], A[i]))
#         while B > 0:
#             custval = heappop(minheap)
#             B-=1
#             heappush(minheap, CustomVal(custval.val+custval.oldval, custval.oldval))
#         ans = -1
#         for ob in minheap:
#             ans = max(ob.val, ans)
#         return ans

class Solution:
    def solve(self, A, B):
        minheap = []
        ans = A.copy()
        heapify(minheap)
        for i in range(0, len(A)):
            heappush(minheap, (2*A[i], i))
        while B > 0:
            val, ind = heappop(minheap)
            ans[ind] = val
            B-=1
            heappush(minheap, (val+A[ind], ind))
        return max(ans)


if __name__ == '__main__':
    print(Solution().solve([1, 2, 3, 4], 3))
    print(Solution().solve([8, 6, 4, 2], 8))
    print(Solution().solve([5, 7, 8], 9))
