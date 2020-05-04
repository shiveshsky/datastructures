import re
class Solution:
    def isMatch(self, A, B):
        B = re.sub(r"\*+", "*", B)
        dp = [[False for x in range(len(B)+1)] for x in range(len(A)+1)]
        dp[0][0] = True
        for i in range(1, len(B)+1):
            if B[i-1] == "*":
                dp[0][i] = dp[0][i-1]
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if B[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif B[j-1] == "?" or A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        return 1 if dp[-1][-1] else 0

if __name__ == '__main__':
    print(Solution().isMatch("abcab", "a*b"))