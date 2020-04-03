class Solution:
    def solve(self, A):
        aa = A.split()
        aaa = list(map(str.strip, aa))
        return " ".join(aaa[::-1])
print(Solution().solve("this is ib"))



