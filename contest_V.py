from collections import Counter


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        counterA = Counter(A)
        counterB = Counter(B)
        if counterA == counterB:
            return 1
        diff = counterA - counterB
        isdiv1 = True
        for k,v in diff.items():
            if v%2 != 0:
                isdiv1 = False
        diff2 = counterB - counterA
        isdiv2 = True
        for k,v in diff2.items():
            if v%2 != 0:
                isdiv2 = False
        if isdiv1 and isdiv2:
            return 1
        return 0
if __name__ == '__main__':
    print(Solution().solve("accd", "abbbd"))
