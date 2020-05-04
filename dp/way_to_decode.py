class Solution:
    # https://www.youtube.com/watch?v=cQX3yHS0cLo
    def numDecodings(self, A):
        dp = [0]*(len(A)+1)
        dp[0] = 1
        dp[1] = (0 if A[0] == "0" else 1)
        for i in range(2, len(A)+1):
            oneDigit = int(A[i-1])
            twoDigit = int(A[i-2]+A[i-1])
            if oneDigit >= 1:
                dp[i] = dp[i-1]
            if twoDigit >=10 and twoDigit<=26:
                dp[i] += dp[i-2]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numDecodings("075361268549483279131"))
