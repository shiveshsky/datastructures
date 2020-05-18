def optimalStrategyOfGame(arr, n, turn=1):
    '''
    :param arr: given array
    :param n: given size of array
    :return: Integer
    '''
    # code here
    if n == 1:
        if turn == 1:
            return arr[0]
        else:
            return 0
    if n == 2:
        if turn == 1:
            return max(arr[0], arr[1])
        else:
            return min(arr[0], arr[1])
    if turn == 1:
        return max(arr[0] + optimalStrategyOfGame(arr[1:], n - 1, 2),
                   arr[-1] + optimalStrategyOfGame(arr[0:-1], n - 1, 2))
    else:
        # here turn 2 wla is not calculating anything for himself
        return min(optimalStrategyOfGame(arr[1:], n - 1, 1), optimalStrategyOfGame(arr[0:-1], n - 1, 1))


def table(arr, n):
    table = [[0 for i in range(n)]
             for i in range(n)]

    # Fill table using above recursive
    # formula. Note that the table is
    # filled in diagonal fashion
    # (similar to http:// goo.gl/PQqoS),
    # from diagonal elements to
    # table[0][n-1] which is the result.
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap

            # Here x is value of F(i+2, j),
            # y is F(i+1, j-1) and z is
            # F(i, j-2) in above recursive
            # formula
            x = 0
            if ((i + 2) <= j):
                x = table[i + 2][j]
            y = 0
            if ((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if (i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y),
                              arr[j] + min(y, z))
    return table[0][n - 1]


if __name__ == '__main__':
    print(optimalStrategyOfGame([7, 3, 5, 10], 4))
