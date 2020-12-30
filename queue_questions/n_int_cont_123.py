# class Solution:
#     def solve(self, A):
#         digits = [1, 2, 3]
#         queue = [1, 2, 3]
#         ans = [1, 2, 3]
#         cnt = 3
#         begin = 0
#         while len(ans) <= A:
#             end = cnt+begin
#             for i in digits:
#                 for j in range(begin, end, 1):
#                     ans.append(int(str(i)+str(queue[j])))
#                     if len(ans)==A:
#                         return ans
#                     queue.append(ans[-1])
#             begin = end
#             cnt = (cnt*3)
#         return ans[0:A]

from copy import copy


class Solution:
    def solve(self, A):
        digits = [1, 2, 3]
        queue = copy(digits)
        ans = []
        for i in range(A):
            ele = queue.pop(0)
            ans.append(ele)
            for k in digits:
                queue.append(int(str(ele) + str(k)))
        return ans


if __name__ == '__main__':
    print(Solution().solve(4))
