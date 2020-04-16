import heapq
from heapq import heapify, heappop


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        heapify(A)
        sum = 0
        while len(A) >= 2:
            rop1 = heappop(A)
            rop2 = heappop(A)
            newrop = rop1+rop2
            sum += (newrop)
            heapq.heappush(A, newrop)
        return sum + heappop(A)+ heappop(A)
