def maximizeTheCuts(n, x, y, z):
    dp = [[0 for i in range(n + 1)] for _ in range(4)]
    dp[0][0] = 1
    for i in range(1, 4):
        dp[i][0] = 1
    arr = [x, y, z]
    arr.sort()
    for i in range(1, 4):
        for j in range(1, n + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


if __name__ == '__main__':
    # print(maximizeTheCuts(5, 5, 3, 2))
    print(maximizeTheCuts(4, 2, 1, 1))
