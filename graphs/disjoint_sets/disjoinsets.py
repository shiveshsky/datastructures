class Disjoinset:

    def __init__(self, n):
        self.parent = [i for i in range(0, n + 1)]
        self.size = [1 for i in range(0, n + 1)]

    def getRoot(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def findset(self, i, j):  # return True if in same set else different set
        return self.getRoot(i) == self.getRoot(j)

    def union(self, i, j):
        if self.findset(i, j):
            # in same set so no need to change
            return
        root_i = self.getRoot(i)
        root_j = self.getRoot(j)
        size_i = self.size[root_i]
        size_j = self.size[root_j]
        if size_i > size_j:
            self.parent[root_j] = root_i
            self.size[root_i] += size_j
        else:
            self.parent[root_i] = root_j
            self.size[root_j] += size_i
