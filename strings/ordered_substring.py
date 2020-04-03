class Solution:
    def solve(self, A):
        A.sort(key=lambda x: len(x))
        for i in range(0, len(A)-1):
            if A[i+1].find(A[i])<0:
                return ["NO"]
        return A

print(Solution().solve(["abc", "abcd", "a", "abc"]))