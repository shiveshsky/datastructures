# Possibility of finishing all courses given pre-requisites
# basicalliy this question boils down to finding cycle in graph


class Solution:

    def solve(self, A, B, c):
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
