class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        sum = 0
        for x in range(0, len(A)):
            for y in range(0, len(A[0])):
               sum += (x+1)*(y+1)*(len(A[0])-y)*(len(A)-x)*A[x][y]
        return sum


'''
x+1 * y+1 for all top left submatrices containing A[x][y]

M-x * N-y for all bottom right submatrices containing A[x][y]

'''