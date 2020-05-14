import math


class Solve:
    def solve(self, floors, eggs):
        if floors <= 1:
            return floors

        if eggs == 1:
            return floors

        mintmp = math.inf
        for k in range(1, floors + 1):
            tmp = max(self.solve(k - 1, eggs - 1), self.solve(floors - k, eggs)) + 1
            mintmp = min(mintmp, tmp)

        return mintmp


if __name__ == '__main__':
    print(Solve().solve(10, 3))
