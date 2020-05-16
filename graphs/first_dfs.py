class Solution:
    def solve(self, A, B, C):
        adj = [[] for _ in range(len(A) + 1)]
        for i in range(1, len(A)):
            adj[A[i]].append(i + 1)
        visited = set()
        source = C
        destination = B
        return self.dfs(adj, visited, source, destination)

    def dfs(self, adj, visited, source, destination):
        if source == destination:
            return 1
        visited.add(source)
        for ch in adj[source]:
            if ch not in visited:
                visited.add(ch)
                if self.dfs(adj, visited, ch, destination):
                    return 1
        return 0


if __name__ == '__main__':
    print(Solution().solve([1, 1, 2], 2, 1))
