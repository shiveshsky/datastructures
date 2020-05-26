import math


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @param G : list of integers
    # @param H : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F, G, H):
        adg = [[math.inf for __ in range(A + 1)] for _ in range(A + 1)]
        for i in range(B):
            adg[D[i]][E[i]] = F[i]
            adg[E[i]][D[i]] = F[i]

        for k in range(1, A + 1):
            for i in range(1, A + 1):
                for j in range(1, A + 1):
                    if i == j:
                        adg[i][j] = 0
                        continue
                    adg[i][j] = min(adg[i][j], adg[i][k] + adg[k][j])
        ans = []
        for i in range(C):
            ans.append(adg[G[i]][H[i]] if adg[G[i]][H[i]] != math.inf else -1)
        return ans


if __name__ == '__main__':
    print(Solution().solve(3, 3, 2, [1, 2, 1], [2, 3, 3], [3, 1, 1], [2, 1], [3, 2]))
