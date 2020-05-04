class Solution:
    def minPathSum(self, A):
        paths = [[0] * len(A[0]) for i in A]
        paths[0][0] = A[0][0]
        for i in range(1, len(A)):
            paths[i][0] = paths[i - 1][0]+A[i][0]
        for j in range(1, len(A[0])):
            paths[0][j] += paths[0][j - 1]+A[0][j]

        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                paths[i][j] = min(paths[i - 1][j], paths[i][j - 1])+A[i][j]
        return paths[-1][-1]


if __name__ == '__main__':
    print(Solution().minPathSum([
        [1, -3, 2],
        [2, 5, 10],
        [5, -5, 1],
     ]))