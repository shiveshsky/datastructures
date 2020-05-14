# TODO MCM


class Solution:
    ans = 0

    def solve(self, A, i, j):
        if j - i <= 1:
            return 0
        max_coins = 0
        for k in range(i + 1, j):
            left = self.solve(A, i, k)
            right = self.solve(A, k, j)
            prod = A[i] * A[k] * A[j]
            max_coins = max(left + right + prod, max_coins)
        return max_coins


if __name__ == '__main__':
    print(Solution().solve([1, 3, 1, 5, 8, 1], 0, 5))
