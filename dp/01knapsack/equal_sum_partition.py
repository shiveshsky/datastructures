class EqualSumPartition:
    def solve(self, arr):
        sumarr = sum(arr)
        if sumarr % 2 != 0:
            return False
        else:
            expected_sum = sumarr // 2
            dp = [[False for i in range(expected_sum + 1)] for j in range(len(arr) + 1)]
            for i in range(expected_sum + 1):
                dp[0][i] = False
            for j in range(len(arr) + 1):
                dp[j][0] = True

            for i in range(1, len(arr) + 1):
                for j in range(1, expected_sum + 1):
                    if arr[i - 1] <= j:
                        dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]
            return dp[-1][-1]


if __name__ == '__main__':
    print(EqualSumPartition().solve([478, 757, 314, 471, 729, 100, 459, 618]))
