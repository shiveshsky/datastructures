class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        A.sort()
        B.sort()
        sumA = 0
        sumB = 0
        for i in range(0, len(A)):
            if A[i] < B[i]:
                sumB+=B[i]-A[i]
            elif A[i]>B[i]:
                sumA+=A[i]-B[i]
        return 0 if sumB>sumA else 1


print(Solution().solve([2, 4, 3, 2], [2, 4, 3, 2]))