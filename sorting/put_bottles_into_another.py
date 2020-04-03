class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=True)
        ans = [A[0]]
        for i in range(1, len(A)):
            if A[i] >= ans[-1]:
                ans.append(A[i])
        return ans


print(Solution().solve([1, 2, 3]))
