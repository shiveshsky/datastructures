from functools import reduce
from heapq import heapify, heappush, heappop


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # TODO try to take lcm and do to take less memory.
        max_heap = []
        lcm = reduce(lambda x, y: x * y, A, 1)
        heapify(max_heap)
        mymap = {}
        if len(A)<=2:
            return [1, A[0]]
        for i in range(0, len(A)):
            for j in range (i+1, len(A)):
                if len(max_heap)<B:
                    heappush(max_heap, -(A[i]/A[j]))
                    mymap.update({-1*(A[i]/A[j]): [A[i], A[j]]})
                else:
                    top = heappop(max_heap)
                    if -1*(A[i]/A[j])> top:
                        heappush(max_heap, -1*(A[i]/A[j]))
                        mymap.update({-1*(A[i] / A[j]): [A[i], A[j]]})
                    else:
                        heappush(max_heap, top)
        return mymap[heappop(max_heap)]

if __name__ == '__main__':
    print(Solution().solve([1, 2, 3, 5], 3))
