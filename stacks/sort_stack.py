class Solution:
    def solve(self, A):
        B = []
        B.append(A.pop())
        while len(A) > 0:
            ele = A.pop()
            if ele < B[-1]:
                while len(B) > 0 and B[-1] > ele:
                    A.append(B.pop())
                B.append(ele)
            else:
                B.append(ele)
        return B


print(Solution().solve([5, 17, 100, 11]))
