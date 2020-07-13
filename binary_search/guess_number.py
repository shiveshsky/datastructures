def guess(n):
    if n == 6:
        return 0
    elif n > 6:
        return 1
    else:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            mid = (l + r) // 2
            gu = guess(mid)
            if gu == 0:
                return mid
            elif gu == 1:
                r = mid - 1
            elif gu == -1:
                l = mid + 1


if __name__ == '__main__':
    print(Solution().guessNumber(10))
