import sys

sys.setrecursionlimit(10000)


class Solution:
    def solve(self, A, B, C, D, E, F):
        adg_matrix = [[1 for _ in range(B + 1)] for i in range(A + 1)]

        for i in range(C):
            self.invalidate_grids(adg_matrix, (E[i], F[i]), D + 1)
        if adg_matrix[A][B] == 0:
            return "NO"
        if adg_matrix[0][0] == 0:
            return "NO"
        return "YES" if self.dfs(adg_matrix, (0, 0), (A, B), set()) else "NO"

    def dfs(self, adg_matrix, source, destination, visited):
        if source not in visited:
            if source == destination:
                return True
            visited.add(source)
            if source[0] + 1 < len(adg_matrix) and adg_matrix[source[0] + 1][source[1]] != 0:
                if self.dfs(adg_matrix, (source[0] + 1, source[1]), destination, visited):
                    return True
            if source[0] - 1 >= 0 and adg_matrix[source[0] - 1][source[1]] != 0:
                if self.dfs(adg_matrix, (source[0] - 1, source[1]), destination, visited):
                    return True
            if source[1] + 1 < len(adg_matrix[0]) and adg_matrix[source[0]][source[1] + 1] != 0:
                if self.dfs(adg_matrix, (source[0], source[1] + 1), destination, visited):
                    return True
            if source[1] - 1 >= 0 and adg_matrix[source[0]][source[1] - 1] != 0:
                if self.dfs(adg_matrix, (source[0], source[1] - 1), destination, visited):
                    return True
            if source[0] + 1 < len(adg_matrix) and source[1] + 1 < len(adg_matrix[0]) and adg_matrix[source[0] + 1][
                source[1] + 1] != 0:
                if self.dfs(adg_matrix, (source[0] + 1, source[1] + 1), destination, visited):
                    return True
            if source[0] + 1 < len(adg_matrix) and source[1] - 1 >= 0 and adg_matrix[source[0] + 1][source[1] - 1] != 0:
                if self.dfs(adg_matrix, (source[0] + 1, source[1] - 1), destination, visited):
                    return True
            if source[0] - 1 >= 0 and source[1] + 1 < len(adg_matrix[0]) and adg_matrix[source[0] - 1][
                source[1] + 1] != 0:
                if self.dfs(adg_matrix, (source[0] - 1, source[1] + 1), destination, visited):
                    return True
            if source[0] - 1 >= 0 and source[1] - 1 >= 0 and adg_matrix[source[0] - 1][source[1] - 1] != 0:
                if self.dfs(adg_matrix, (source[0] - 1, source[1] - 1), destination, visited):
                    return True

        return False

    def invalidate_grids(self, arr, centre, radius):
        for i in range(centre[0], min(radius + 1, len(arr))):
            arr[i][centre[1]] = 0
        for i in range(0, max((centre[0] - radius), -1)):
            arr[centre[0] - i][centre[1]] = 0
        for i in range(centre[1], min(radius + 1, len(arr[0]))):
            arr[centre[0]][i] = 0
        for i in range(centre[1], max((centre[1] - radius), -1)):
            arr[centre[0]][centre[1] - i]
        i = 0
        while i < radius:
            if centre[0] + i < len(arr):
                if centre[1] + i < len(arr[0]):
                    arr[centre[0] + i][centre[1] + i] = 0
            i += 1
        i = 0
        while i < radius:
            if centre[0] - i >= 0:
                if centre[1] - i >= 0:
                    arr[centre[0] - i][centre[1] - i] = 0
            i += 1
        i = 0
        while i < radius:
            if centre[0] - i >= 0:
                if centre[1] + i < len(arr[0]):
                    arr[centre[0] - i][centre[1] + i] = 0
            i += 1
        i = 0
        while i < radius:
            if centre[0] + i < len(arr):
                if centre[1] - i >= 0:
                    arr[centre[0] + i][centre[1] - i] = 0
            i += 1


if __name__ == '__main__':
    print(Solution().solve(61, 88, 2, 9, [3, 55], [18, 83]))
