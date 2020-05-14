import re
class Solution:
    def isMatch(self, A, B):
        B = re.sub(r"\*+", "*", B)
        dp = [[False for x in range(len(B)+1)] for x in range(len(A)+1)]
        dp[0][0] = True
        for i in range(1, len(B)+1):
            if B[i-1] == "*":
                dp[0][i] = dp[0][i-1]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if B[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif B[j - 1] == "?" or A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False
        return 1 if dp[-1][-1] else 0

    def isMatchRecc(self, string, pattern, m, n):
        # works if only one * is present that is replace extra *** with single *
        if m == 0 and n == 0:
            return True
        if m == 0 and n == 1 and pattern[n - 1] == '*':
            return True
        if m == 1 and n == 1 and pattern[n - 1] == '?':
            return True
        if m > 0 and n == 0:
            return False
        if m == 0 and n > 0:
            return False
        if string[m - 1] == pattern[n - 1]:
            return self.isMatchRecc(string, pattern, m - 1, n - 1)
        elif pattern[n - 1] == '?':
            return self.isMatchRecc(string, pattern, m - 1, n - 1)
        elif pattern[n - 1] == '*':
            part1 = self.isMatchRecc(string, pattern, m - 1, n)
            part2 = self.isMatchRecc(string, pattern, m, n - 1)
            return part1 or part2
        return False


if __name__ == '__main__':
    print(Solution().isMatchRecc("abcab", "a*b", 5, 3))
    # print(Solution().isMatch("abcab", "a*b"))
