from collections import deque


class Solution:
    def knight(self, A, B, Q, R, E, F):
        board = [[0 for _ in range(B)] for __ in range(A)]
        queue = deque()
        queue.append((Q - 1, R - 1, 0))
        visited = set()
        while len(queue) > 0:
            src = queue.popleft()
            C = src[0]
            D = src[1]
            if (src[0], src[1]) == (E - 1, F - 1):
                return src[2]
            if C - 1 >= 1 and D - 2 >= 0 and (C - 1, D - 2) not in visited:
                queue.append((C - 1, D - 2, src[2] + 1))
                board[C - 1][D - 2] = src[2] + 1
                visited.add((C - 1, D - 2))
            if C - 2 >= 0 and D - 1 >= 0 and (C - 2, D - 1) not in visited:
                queue.append((C - 2, D - 1, src[2] + 1))
                board[C - 2][D - 1] = src[2] + 1
                visited.add((C - 2, D - 1))
            if C - 1 >= 0 and D + 2 < len(board[0]) and (C - 1, D + 2) not in visited:
                queue.append((C - 1, D + 2, src[2] + 1))
                board[C - 1][D + 2] = src[2] + 1
                visited.add((C - 1, D + 2))
            if C - 2 >= 0 and D + 1 < len(board[0]) and (C - 2, D + 1) not in visited:
                queue.append((C - 2, D + 1, src[2] + 1))
                board[C - 2][D + 1] = src[2] + 1
                visited.add((C - 2, D + 1))
            if C + 2 < len(board) and D + 1 < len(board[0]) and (C + 2, D + 1) not in visited:
                queue.append((C + 2, D + 1, src[2] + 1))
                board[C + 2][D + 1] = src[2] + 1
                visited.add((C + 2, D + 1))
            if C + 1 < len(board) and D + 2 < len(board[0]) and (C + 1, D + 2) not in visited:
                queue.append((C + 1, D + 2, src[2] + 1))
                board[C + 1][D + 2] = src[2] + 1
                visited.add((C + 1, D + 2))
            if C + 2 < len(board) and D - 1 >= 0 and (C + 2, D - 1) not in visited:
                queue.append((C + 2, D - 1, src[2] + 1))
                board[C + 2][D - 1] = src[2] + 1
                visited.add((C + 2, D - 1))
            if C + 1 < len(board) and D - 2 >= 0 and (C + 1, D - 2) not in visited:
                queue.append((C + 1, D - 2, src[2] + 1))
                board[C + 1][D - 2] = src[2] + 1
                visited.add((C + 1, D - 2))
        return -1


if __name__ == '__main__':
    print(Solution().knight(3, 11, 3, 11, 2, 11))
