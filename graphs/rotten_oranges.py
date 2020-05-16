from collections import deque


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        queue = deque()
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == 2:
                    queue.append((i, j, 0))
        k = 0
        while len(queue) > 0:
            tup = queue.popleft()
            if tup[0] + 1 < len(A) and A[tup[0] + 1][tup[1]] == 1:
                A[tup[0] + 1][tup[1]] = 2
                queue.append((tup[0] + 1, tup[1], tup[2] + 1))
            if tup[0] - 1 >= 0 and A[tup[0] - 1][tup[1]] == 1:
                A[tup[0] - 1][tup[1]] = 2
                queue.append((tup[0] - 1, tup[1], tup[2] + 1))
            if tup[1] + 1 < len(A[0]) and A[tup[0]][tup[1] + 1] == 1:
                A[tup[0]][tup[1] + 1] = 2
                queue.append((tup[0], tup[1] + 1, tup[2] + 1))
            if tup[1] - 1 >= 0 and A[tup[0]][tup[1] - 1] == 1:
                A[tup[0]][tup[1] - 1] = 2
                queue.append((tup[0], tup[1] - 1, tup[2] + 1))
            k = max(k, tup[2])

        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == 1:
                    return -1
        return k


if __name__ == '__main__':
    print(Solution().solve([[2, 1, 1],
                            [1, 1, 0],
                            [0, 1, 1]]))
