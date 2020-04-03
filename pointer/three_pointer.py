def find_common(a, b, c):
    ii, jj, kk = 0, 0, 0
    results = []
    while ii < len(a):
        if a[ii] > b[jj]:
            while jj < len(b) and b[jj] < a[ii]:
                jj += 1
        if a[ii] > c[kk]:
            while kk < len(c) and c[kk] < a[ii]:
                kk += 1
        if jj < len(b) and kk < len(c) and a[ii] == b[jj] == c[kk]:
            results.append(a[ii])

        ii += 1
    return results


# a = [1, 6, 10, 20, 40, 80]
# b = [6, 7, 20, 80, 100]
# c = [3, 6, 15, 20, 30, 70, 80, 120]
a = [12,30,50]
b = [10,30,50]
c = [25,30]
print(find_common(a,b,c))