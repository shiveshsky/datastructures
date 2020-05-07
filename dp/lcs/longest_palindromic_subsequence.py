class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A):
        B = A[::-1]
        lcs = []
        for row in range(0, len(A)+1):
            ro = []
            for col in range(0, len(B)+1):
                ro.append(0)
            lcs.append(ro)
        A = list(A)
        B = list(B)
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    lcs[i][j] = lcs[i-1][j-1]+1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

        return lcs[-1][-1]
