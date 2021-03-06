class LongestCommonSubstring:
    def solve(self, A, B):
        lcs = []
        for row in range(0, len(A) + 1):
            ro = []
            for col in range(0, len(B) + 1):
                ro.append(0)
            lcs.append(ro)
        A = list(A)
        B = list(B)
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = 0
        return lcs[-1][-1]
