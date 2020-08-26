def convertToTitle(A):
    ans = ''
    while A > 0:
        A = A - 1
        tmp = A % 26
        A //= 26
        ans += chr(int(tmp + ord('A')))
    return ans[::-1]


if __name__ == '__main__':
    print(convertToTitle(26))
