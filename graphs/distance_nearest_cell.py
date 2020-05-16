from collections import deque


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        queue = deque()
        visited = set()

        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j] == 1:
                    A[i][j] = 0
                    visited.add((i, j))
                    queue.append((i, j, 0))
        while len(queue) > 0:
            tup = queue.popleft()
            if tup[0] + 1 < len(A) and (tup[0] + 1, tup[1]) not in visited and A[tup[0] + 1][tup[1]] == 0:
                A[tup[0] + 1][tup[1]] = tup[2] + 1
                queue.append((tup[0] + 1, tup[1], tup[2] + 1))
            if tup[0] - 1 >= 0 and (tup[0] - 1, tup[1]) not in visited and A[tup[0] - 1][tup[1]] == 0:
                A[tup[0] - 1][tup[1]] = tup[2] + 1
                queue.append((tup[0] - 1, tup[1], tup[2] + 1))
            if tup[1] + 1 < len(A[0]) and (tup[0], tup[1] + 1) not in visited and A[tup[0]][tup[1] + 1] == 0:
                A[tup[0]][tup[1] + 1] = tup[2] + 1
                queue.append((tup[0], tup[1] + 1, tup[2] + 1))
            if tup[1] - 1 >= 0 and (tup[0], tup[1] - 1) not in visited and A[tup[0]][tup[1] - 1] == 0:
                A[tup[0]][tup[1] - 1] = tup[2] + 1
                queue.append((tup[0], tup[1] - 1, tup[2] + 1))
            visited.add((tup[0], tup[1]))
        return A


if __name__ == '__main__':
    print(Solution().solve([
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]))
