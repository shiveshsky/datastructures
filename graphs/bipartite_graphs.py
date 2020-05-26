from collections import deque


class Solution:
    def solve(self, A, B):
        adj = [list() for _ in range(A)]
        for row in B:
            adj[row[0]].append(row[1])
            adj[row[1]].append(row[0])
        for i in range(A):
            blue_set = set()
            red_set = set()
            visited = set()
            queue = deque()
            queue.append((0, 1))
            blue_set.add(0)
            visited.add(0)
            while len(queue) > 0:
                ele = queue.popleft()
                for child in adj[ele[0]]:
                    if child not in visited:
                        if ele[1] == 1:
                            if child not in red_set:
                                red_set.add(child)
                                queue.append((child, 2))
                        elif ele[1] == 2:
                            if child not in blue_set:
                                blue_set.add(child)
                                queue.append((child, 1))
                        visited.add(child)
                    if ele[1] == 1 and child in blue_set:
                        return 0
                    elif ele[1] == 2 and child in red_set:
                        return 0
        return 1


if __name__ == '__main__':
    print(Solution().solve(10, [[7, 8],
                                [1, 2],
                                [0, 9],
                                [1, 3],
                                [6, 7],
                                [0, 3],
                                [2, 5],
                                [3, 8],
                                [4, 8]]))
