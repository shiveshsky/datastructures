class Solution:
    def solve(self, A, B, C, D):
        parent = [i for i in range(A + 1)]
        size = [1 for _ in range(A + 1)]
        B.insert(0, 0)
        power = [B[i] for i in range(A + 1)]
        for row in C:
            self.union(row[0], row[1], parent, size, power)
        cnt = 0
        visited = set()
        for i in parent:
            roo = self.get_root(i, parent)
            if roo not in visited and power[roo] >= D:
                visited.add(roo)
                cnt += 1
        return cnt

    def get_root(self, i, parent):
        while i != parent[i]:
            i = parent[i]
        return i

    def findUnion(self, i, j, parent):
        return self.get_root(i, parent) == self.get_root(j, parent)

    def union(self, i, j, parent, size, power):
        if self.findUnion(i, j, parent):
            return
        root_i = self.get_root(i, parent)
        root_j = self.get_root(j, parent)
        size_i = size[root_i]
        size_j = size[root_j]
        if size_i > size_j:
            parent[root_j] = root_i
            size[root_i] += size_j
            power[root_i] += power[root_j]
        else:
            parent[root_i] = root_j
            size[root_j] += size_i
            power[root_j] += power[root_i]


if __name__ == '__main__':
    print(Solution().solve(14, [7, 5, 7, 3, 9, 4, 4, 6, 3, 1, 4, 8, 7, 6], [
        [1, 2],
        [2, 6],
        [2, 7],
        [4, 13],
        [5, 8],
        [5, 13],
        [6, 12],
        [7, 10],
        [10, 14],
        [13, 14]
    ], 2))
