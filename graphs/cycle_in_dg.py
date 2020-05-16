import sys

sys.setrecursionlimit(10000000)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj = [[] for i in range(A + 1)]
        for row in B:
            adj[row[0]].append(row[1])
        return 1 if any([self.dfs(adj, set(), i) for i in range(1, A + 1)]) else 0

    def dfs(self, adj, visited, source):
        visited.add(source)
        for ch in adj[source]:
            if ch not in visited:
                visited.add(ch)
                va = self.dfs(adj, visited, ch)
                if va:
                    return va
            else:
                return True
        return False


if __name__ == '__main__':
    print(Solution().solve(5, [[1, 2],
                               [2, 3],
                               [3, 4],
                               [4, 5]]))
