class Solution:
    def solve(self, A, B, C):
        dix = {}
        for i in A:
            val = (i ** 3) % C - ((i % C * B % C) % C)
            if dix.get(val):
                dix.update({val: dix[val] + 1})
            else:
                dix[val] = 1
        ans = max(dix, key=dix.get)
        return dix[ans]

'''
x2 + y2 + x*y = B mod C
(x2 + y2 + xy)(x-y) = (x-y)BmodC
x3    - y3  = (Bx mod c- yBmodc)mod c
x3 -xB mod c = y3- yB mod C
'''
# print(Solution().solve([ 26, 31, 15, 38, 27, 7, 45, 10, 44, 52, 28, 33, 25, 41, 39, 29, 30, 42 ], 9, 53))
# print(Solution().solve( [9, 17, 10, 16], 1, 19))
print(Solution().solve([34, 15, 23, 32, 37, 22, 14, 48, 55, 6, 33, 25], 10, 263))
