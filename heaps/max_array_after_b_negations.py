from heapq import heapify, heappop, heappush


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heapify(A)
        mini=heappop(A)
        while mini<0 and B>0:
            B -= 1
            mini = -1*mini
            heappush(A, mini)
            mini = heappop(A)
        if B>0:
            if B%2==0:
                heappush(A, mini)
            else:
                heappush(A, -1*mini)
        else:
            heappush(A, mini)
        return sum(A)

if __name__ == '__main__':
    print(Solution().solve([ -20, 73, 89, -35, -20, 12, 25, -17, 93 ], 3))
    print(Solution().solve([57, 3, -14, -87, 42, 38, 31, -7, -28, -61], 10))
