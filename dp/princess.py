import math
'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0’s) or contain magic orbs that increase the knight’s health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight’s minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path

RIGHT-> RIGHT -> DOWN -> DOWN.

Dungeon Princess: Example 1
'''

class Solution:
        def calculateMinimumHP(self, A):
            M, N = len(A), len(A[0])

            hp = [[math.inf] * (N + 1) for _ in range(M + 1)]

            hp[M][N - 1] = 1
            hp[M - 1][N] = 1

            for i in range(M - 1, -1, -1):
                for j in range(N - 1, -1, -1):
                    need = min(hp[i + 1][j], hp[i][j + 1]) - A[i][j]
                    if need <= 0:
                        hp[i][j] = 1
                    else:
                        hp[i][j] = need

            return hp[0][0]


if __name__ == '__main__':
    print(Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
