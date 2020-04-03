class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        c = 0
        # max_so_far = -1
        # A.insert(0,0)
        max_so_far = A[0]
        for i in range(0, len(A)):
            max_so_far = max(max_so_far, A[i])
            if max_so_far == i:
                c += 1
        return c


# print(Solution().solve([0, 1, 2, 3, 4]))
# print(Solution().solve([2, 0, 1, 3]))
#                        '''0  1  2  3'//''
# print(Solution().solve([1, 2, 3, 4]))
#
