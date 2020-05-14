def longest_chain(arr, n):
    dp = [1] * n
    arr.sort(lambda pair: (pair.a, pair.b))
    for i in range(0, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[i].a > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
