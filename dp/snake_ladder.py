import collections


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        board_2 = [0]
        rows, cols = len(board), len(board[0])
        row = rows - 1

        while row >= 0:
            for col in range(cols):
                board_2.append(board[row][col])
            row -= 1
            if row >= 0:
                for col in range(cols - 1, -1, -1):
                    board_2.append(board[row][col])
                row -= 1

        visited = [0 for i in range(len(board_2))]
        que = collections.deque()
        # que = []
        que.append([1, 0])
        while que:
            curr_ind, curr_dist = que.popleft()
            for i in range(1, 7):
                next_ind = min(rows * cols, curr_ind + i)
                if board_2[next_ind] != -1:
                    next_ind = board_2[next_ind]
                if next_ind == rows * cols:
                    return curr_dist + 1
                if visited[next_ind] == 0:
                    visited[next_ind] = 1
                    que.append([next_ind, curr_dist + 1])

        return -1


if __name__ == '__main__':
    print(Solution().snakesAndLadders([
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]))
    # print(Solution().snakesAndLadders([[-1,7,-1],[-1,6,9],[-1,-1,2]]))
