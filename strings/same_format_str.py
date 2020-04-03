class Solution:
    def solve(self, A, B):
        # two pointer se kar lo sale
        i = 0
        j = 0
        while i < len(A):
            if A[i] != B[j]:
                return 0
            else:
                while j < len(B) and A[i] == B[j]:
                    j += 1
                if len(B) == j and i < len(A)-1:
                    return 0
            i += 1
        if i == len(A) and j < len(B):
            return 0
        return 1


print(Solution().solve("HIRED", "HHHIIIRRRRREEEEEDDDDD"))
print(Solution().solve("HIR", "HIRE"))
print(Solution().solve("HIRE", "HIR"))
