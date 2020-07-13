# multi source and multidestination
import math

# https://www.youtube.com/watch?v=oNI0rf2P9gE
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == -1:
                    A[i][j] = math.inf
        for k in range(1, len(A)):
            for i in range(0, len(A)):
                for j in range(0, len(A[0])):
                    if i == j:
                        continue
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])

        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == math.inf:
                    A[i][j] = -1
        return A
