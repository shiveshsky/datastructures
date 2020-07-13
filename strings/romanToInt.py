class Solution:

    def value(self, r):
        if r == 'I':
            return 1
        if r == 'V':
            return 5
        if r == 'X':
            return 10
        if r == 'L':
            return 50
        if r == 'C':
            return 100
        if r == 'D':
            return 500
        if r == 'M':
            return 1000
        return -1

    def romanToInt(self, A):
        res = 0
        i = 0
        while i < len(A):
            str1 = self.value(A[i])
            if i + 1 < len(A):
                str2 = self.value(A[i + 1])
                if str1 >= str2:
                    res = res + str1
                    i += 1
                else:
                    res = res + (str2 - str1)
                    i += 2
            else:
                res = res+str1
                i += 1
        return res


if __name__ == '__main__':
    print(Solution().romanToInt("VXX"))
