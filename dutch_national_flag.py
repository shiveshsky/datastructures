def dnf(arr):
    l = 0
    mid = 0
    h = len(arr) - 1
    while mid <= h:
        if arr[mid] == 0:
            arr[l], arr[mid] = arr[mid], arr[l]
            mid += 1
            l += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[h], arr[mid] = arr[mid], arr[h]
            h -= 1
    return arr


if __name__ == "__main__":
    print(dnf([2, 0, 1]))
