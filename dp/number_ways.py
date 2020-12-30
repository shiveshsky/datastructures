def noway(m, arr):
    if m < 0: return 0
    if m == 0: return 1
    if m > 0 and len(arr) == 0: return 1
    cnt = 0
    for i in range(0, len(arr)):
        if m - arr[i] >= 0:
            cnt += noway(m - arr[i], arr[i + 1:])
        else:
            return 1

    return cnt


if __name__ == '__main__':
    print(noway(8, [1, 3, 5, 4, 2]))
