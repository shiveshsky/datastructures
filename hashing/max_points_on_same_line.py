# TODO FIX IT
class Solution:
    def gcd(self, A, B):
        if A == 0:
            return B
        if B == 0:
            return A
        return self.gcd(B % A, A)

    def solve(self, A, B):
        line_dic = {}
        for i in range(0, len(A)-1):
            for j in range(i+1, len(A)):
                mx = (A[j]-A[i])
                my = (B[j]-B[i])
                gc = self.gcd(mx, my)
                mx = mx//gc
                my = my//gc
                if mx != 0:
                    c = (B[i] - (my/mx)*A[i])
                else:
                    c = 1.0
                key = ((mx, my), c)
                if line_dic.get(key) is None:
                    line_dic[key] = {(A[j], B[j])}
                    line_dic[key].add((A[i], B[i]))
                else:
                    line_dic[key].add((A[j], B[j]))
                    line_dic[key].add((A[i], B[i]))
        return max([len(se) for se in line_dic.values()])


# print(Solution().solve([-1, 0, 1, 2, 3, 3],  [1, 0, 1, 2, 3, 4]))
print(Solution().solve([3, 1, 4, 5, 7, -9, -8, 6], [4, -8, -3, -2, -1, 5, 7, -4]))
