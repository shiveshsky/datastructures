class Solution:
    def solve(self, A, B):
        adj = [[] for i in range(A + 1)]
        for row in B:
            adj[row[0]].append(row[1])
        return self.dfs(adj, set(), 1, A)

    def dfs(self, adj, visited, source, destination):
        if source == destination:
            return True
        visited.add(source)
        for ch in adj[source]:
            if ch not in visited:
                visited.add(ch)
                if self.dfs(adj, visited, ch, destination):
                    return True
        return False


if __name__ == '__main__':
    print(Solution().solve(5, [[1, 2],
                               [2, 3],
                               [3, 4],
                               [4, 5]]))
