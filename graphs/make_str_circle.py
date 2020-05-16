class Solution:
    def solve(self, A):
        adg = [[] for _ in range(26)]
        for ele in A:
            adg[ord(ele[0]) - 97].append(ord(ele[-1]) - 97)
        print(adg)
        return 1 if all([len(adg[i]) > 0 and self.dfs(i, i, adg, set()) for i in range(26)]) else 0

    def dfs(self, source, destination, adj, visited):
        if destination in visited:
            return True
        visited.add(source)
        for ch in adj[source]:
            if self.dfs(ch, destination, adj, visited):
                return True
        return False


if __name__ == '__main__':
    print(Solution().solve(["abc", "cba"]))
