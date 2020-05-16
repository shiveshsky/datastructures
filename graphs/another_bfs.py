from collections import deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        dum = 0

        for i in B:
            dum = max(dum, i[0], i[1])

        for i in B:
            n1, n2, weight = i[0], i[1], i[2]
            if weight == 2:
                dum += 1
                i[1] = dum
                i[2] = 1
                B.append([dum, n2, 1])

        # print(B)

        adj = []

        for _ in range(dum + 1):
            adj.append([])

        for i in B:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])

        # print(adj)

        map = {}
        q = deque()
        q.append([C, 0])

        while q:
            node = q.popleft()
            n, d = node[0], node[1]

            if n == D:
                return d

            if n not in map:
                map[n] = 1
                for all in adj[n]:
                    q.append([all, d + 1])

        return -1


if __name__ == '__main__':
    print(Solution().solve(A=6,
                           B=[[2, 5, 1],
                              [1, 3, 1],
                              [0, 5, 2],
                              [0, 2, 2],
                              [1, 4, 1],
                              [0, 1, 1]],
                           C=3,
                           D=2))
