import math


class MCM:
    def solve_recc(self, arr, i, j):
        if j <= i:
            return 0
        tmp = math.inf
        for k in range(i, j):
            tmp = min(self.solve_recc(arr, i, k) + self.solve_recc(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j], tmp)
        return tmp


if __name__ == '__main__':
    arr = [[]]
    print(MCM().solve_recc(arr, 1, len(arr) - 1))
