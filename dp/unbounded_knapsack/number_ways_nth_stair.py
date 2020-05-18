def countWays(m):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    # code here
    # order does not matter
    dp = [[0 for _ in range(m + 1)] for __ in range(3)]
    weights = [1, 2]
    for i in range(3):
        dp[i][0] = 1
    for i in range(1, 3):
        for j in range(1, m + 1):
            if weights[i - 1] <= j:
                dp[i][j] = dp[i][j - weights[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)


def dudu(m):
    dp = [0 for i in range(m + 1)]

    ans = 0
    wt = [0, 1, 2]
    # Fill dp[] using above recursive formula
    for i in range(m + 1):
        for j in range(3):
            if (wt[j] <= i):
                dp[i] = dp[i] + dp[i - wt[j]]

    print(dp)


'''
    steps = 0  1 2 3 4
    ans =   1  1 2 3 5
'''
if __name__ == '__main__':
    countWays(3)
