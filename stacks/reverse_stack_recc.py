class Solution:

    def reverse(self, A, tmp_stk=[]):
        if len(A)==1:
            tmp_stk.append(A.pop())
            return
        else:
            tmp_stk.append(A.pop())
            self.reverse(A, tmp_stk)
            return tmp_stk

    def solve(self, A):
        aux1 = self.reverse(A, [])
        aux2 = self.reverse(aux1, [])
        self.reverse(aux2, A)
        return


# print(Solution().solve([42, 35, 45, 22, 26, 26, 2, 29, 21]))
print(Solution().solve([1, 2, 3, 4, 5])) # 5 4 3 2 1

