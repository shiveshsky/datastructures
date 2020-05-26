class Disjoint:

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


class Solution:

    def kruskal(self, A, B):
        e = 0
        anssum = [0] * (len(B))
        graph = []
        for i, row in enumerate(B):
            graph.append([row[0], row[1], row[2], i])
        graph.sort(key=lambda x: x[2])
        disjoint = Disjoint(A)
        i = 0
        while e < A - 1 and i < len(graph):
            u, v, w, ind = graph[i]
            i += 1
            x = disjoint.getRoot(u)
            y = disjoint.getRoot(v)
            if x != y:
                e += 1
                anssum[ind] = 1
                disjoint.union(u, v)
        print(disjoint.parent)
        return anssum


if __name__ == '__main__':
    print(Solution().kruskal(52, [[44, 50, 42],
                                  [23, 26, 468],
                                  [20, 45, 335],
                                  [4, 26, 501],
                                  [12, 33, 170],
                                  [9, 41, 725],
                                  [30, 51, 479],
                                  [2, 26, 359],
                                  [2, 23, 963],
                                  [16, 18, 465],
                                  [32, 51, 706],
                                  [30, 49, 146],
                                  [46, 52, 282],
                                  [13, 31, 828],
                                  [2, 37, 962],
                                  [11, 44, 492],
                                  [22, 23, 996],
                                  [31, 40, 943],
                                  [1, 5, 828],
                                  [13, 44, 437],
                                  [6, 13, 392],
                                  [23, 37, 605],
                                  [29, 37, 903],
                                  [8, 43, 154],
                                  [13, 37, 293],
                                  [30, 36, 383],
                                  [11, 39, 422],
                                  [11, 42, 717],
                                  [29, 32, 719],
                                  [28, 32, 896],
                                  [26, 37, 448],
                                  [28, 45, 727],
                                  [7, 31, 772],
                                  [15, 46, 539],
                                  [31, 51, 870],
                                  [15, 19, 913],
                                  [22, 36, 668],
                                  [6, 47, 300],
                                  [10, 48, 36],
                                  [19, 27, 895],
                                  [2, 19, 704],
                                  [11, 40, 812],
                                  [33, 35, 323],
                                  [8, 38, 334],
                                  [38, 43, 674],
                                  [3, 36, 665],
                                  [1, 16, 142],
                                  [22, 32, 712],
                                  [18, 20, 254],
                                  [31, 43, 869],
                                  [18, 44, 548],
                                  [5, 33, 645],
                                  [21, 42, 663],
                                  [17, 29, 758],
                                  [2, 51, 38],
                                  [12, 19, 860],
                                  [13, 47, 724],
                                  [18, 38, 742],
                                  [22, 27, 530],
                                  [15, 21, 779],
                                  [10, 31, 317],
                                  [16, 20, 36],
                                  [44, 45, 191],
                                  [2, 11, 843],
                                  [7, 36, 289],
                                  [8, 47, 107],
                                  [25, 38, 41],
                                  [10, 36, 943],
                                  [1, 41, 265],
                                  [5, 49, 649],
                                  [11, 38, 447],
                                  [32, 40, 806],
                                  [32, 37, 891],
                                  [17, 45, 730],
                                  [6, 37, 371],
                                  [2, 10, 351],
                                  [13, 48, 7],
                                  [3, 26, 102],
                                  [5, 9, 394],
                                  [43, 50, 549],
                                  [17, 52, 630],
                                  [2, 42, 624],
                                  [10, 27, 85],
                                  [24, 37, 955],
                                  [37, 51, 757],
                                  [10, 29, 841],
                                  [24, 46, 967],
                                  [38, 46, 377],
                                  [46, 51, 932],
                                  [14, 44, 309],
                                  [6, 39, 945],
                                  [31, 35, 440],
                                  [39, 41, 627],
                                  [2, 15, 324],
                                  [3, 13, 538],
                                  [16, 27, 539],
                                  [20, 23, 119],
                                  [16, 28, 83],
                                  [12, 20, 930],
                                  [3, 4, 542],
                                  [26, 35, 834],
                                  [12, 50, 116],
                                  [35, 41, 640],
                                  [21, 30, 659],
                                  [27, 52, 705],
                                  [2, 45, 931],
                                  [23, 45, 978],
                                  [14, 51, 307]]))
