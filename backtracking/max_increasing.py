from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        maxlen = 1
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                maxlen = max(maxlen, self.dfs(i, j, matrix))
        return maxlen

    def dfs(self, i, j, matrix):
        if i < 0 or j < 0:
            return 0
        if i >= len(matrix) and j >= len(matrix[0]):
            return 0
        t = 0
        d = 0
        l = 0
        r = 0
        if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
            t = self.dfs(i - 1, j, matrix)
        if i + 1 < len(matrix) and matrix[i][j] < matrix[i + 1][j]:
            d = self.dfs(i + 1, j, matrix)
        if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
            l = self.dfs(i, j - 1, matrix)
        if j + 1 < len(matrix[0]) and matrix[i][j] < matrix[i][j + 1]:
            r = self.dfs(i, j + 1, matrix)
        return max(t, d, l, r) + 1


if __name__ == '__main__':
    print(Solution().longestIncreasingPath([[1, 4, 7, 9], [0, 3, 8, 5], [3, 6, 0, 6], [1, 4, 5, 6]]))
