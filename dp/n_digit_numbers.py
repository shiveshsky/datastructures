class Solution:
    def solve(self, A, B):
        dp = [[-1 for _ in range(0, B+1)] for i in range(0, A+1)]
        self.solve_memo(A, B, 1, dp)
        return dp[-1][-1]

    def solve_memo(self, A, B, start, dp):
        if A<=1:
            dp[A][B] = 1
            return 1
        if B<=0:
            dp[A][B] = 1
            return 1
        else:
            allsum = 0
            if dp[A][B] != -1:
                return dp[A][B]
            for i in range(start, 10):
                if B-i >= 0:
                    allsum += self.solve_recc(A-1, B-i, 0)
            dp[A][B] = allsum
            return allsum

    def solve_recc(self, A, B, start):
        if A <= 1:
            return 1
        if B <= 0:
            return 1
        else:
            allsum = 0
            for i in range(start, 10):
                if B-i>=0:
                    allsum += self.solve_recc(A-1, B-i, 0)
        return allsum


if __name__ == '__main__':
    print(Solution().solve_recc(2, 9, 1))
    print(Solution().solve(2, 9))