def minSwaps(a, n):
    # Code here
    arrPos = []

    for i in range(n):
        arrPos.append([a[i], i])
    arrPos.sort()

    vis = [0 for i in range(n)]

    ans = 0

    for i in range(n):
        if (vis[i] or arrPos[i][1] == i):
            continue

        cycle_size = 0
        j = i

        while (not vis[j]):
            vis[j] = 1
            j = arrPos[j][1]
            cycle_size += 1
        ans += cycle_size - 1
    return ans


if __name__ == '__main__':
    minSwaps([4, 3, 2, 1], 4)
