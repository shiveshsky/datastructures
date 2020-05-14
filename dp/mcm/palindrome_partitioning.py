import math


class PalindromePartitioning:
    def is_palindrome(self, strinput):
        i = 0
        j = len(strinput) - 1
        while i < j:
            if strinput[i] != strinput[j]:
                return False
            i += 1
            j -= 1
        return True

    def solve(self, A, i, j):
        if i >= j:
            return 0
        if self.is_palindrome(A[i:j + 1]):
            return 0
        ans = math.inf
        for k in range(i, j):
            ans = min((self.solve(A, i, k) + self.solve(A, k + 1, j) + 1), ans)
        return ans


if __name__ == '__main__':
    print(PalindromePartitioning().solve("ababbbabbababa", 0, 13))
