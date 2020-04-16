from heapq import heapify, heappop, heappush
from math import floor


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heapify(A)
        if len(A)==1:
            return floor(A[0]/2.0)
        mini = heappop(A)
        sum = 0
        while mini<=B:
            eat = floor(mini/2.0)
            sum += eat
            left = mini-eat
            if len(A)==0:
                return sum
            next_mini = heappop(A)
            next_mini+=left
            heappush(A, next_mini)
            mini = heappop(A)
        return sum

if __name__ == '__main__':
    print(Solution().solve( [3, 2, 3], 4))
    # print(Solution().solve( [ 324, 458, 481, 167, 939, 444, 388, 612, 943, 890, 953, 403, 653, 136, 168, 163, 186, 471 ], 231))
