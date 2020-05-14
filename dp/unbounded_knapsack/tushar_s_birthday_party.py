import math


class Solution:
    def solve(self, A, B, C):
        ans = 0
        for total_capacity in A:

            dp = [[0 for _ in range(total_capacity + 1)] for i in range(0, len(C) + 1)]
            for i in range(1, total_capacity + 1):
                dp[0][i] = math.inf

            for i in range(1, len(C) + 1):
                for j in range(1, total_capacity + 1):
                    if B[i - 1] <= j:
                        dp[i][j] = min(C[i - 1] + dp[i][j - B[i - 1]], dp[i - 1][j])
                    else:
                        dp[i][j] = dp[i - 1][j]
            ans += dp[-1][-1]
        return ans


if __name__ == '__main__':
    print(Solution().solve([65, 641, 821, 316, 518, 285, 69, 699, 384, 90, 301, 369],
                           [1, 90, 2, 89, 24, 142, 290, 479, 478, 394, 759, 111, 942, 887, 211, 649, 439, 534, 588, 503,
                            175, 128, 818, 693, 131, 605, 111, 515, 414, 411, 602, 948, 500, 604, 37, 242, 464, 327,
                            721, 942],
                           [720, 199, 771, 381, 86, 982, 748, 243, 235, 56, 745, 410, 183, 283, 821, 33, 606, 931, 266,
                            20, 61, 867, 967, 560, 471, 5, 521, 935, 331, 960, 596, 769, 159, 367, 868, 963, 68, 617,
                            206, 22]))
