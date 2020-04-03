class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort()
        max_diff = 0
        j=len(A)-1
        for i in range(0, len(A)//2):
            max_diff+=(A[j]-A[i])
            j-=1
        min_diff = 0
        for i in range(1, len(A), 2):
            min_diff+=(A[i]-A[i-1])
        return [max_diff, min_diff]
print(Solution().solve([3, 11, -1, 5]))
