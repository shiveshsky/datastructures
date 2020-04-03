from collections import Counter


class Solution:
    def solve(self, A, B):
        my_dic_A = Counter(A)
        ans_A = []
        for i in B:
            if my_dic_A.get(i) is not None:
                ans_A += [i]*my_dic_A.get(i)
                my_dic_A.pop(i)
        ans_ = []
        for k,v in my_dic_A.items():
            ans_ += [k]*v
        ans_.sort()
        return ans_A+ans_
# print(Solution().solve([1, 2, 3, 4, 5], [5, 4, 2]))
# print(Solution().solve([5, 17, 100, 11], [1, 100]))
print(Solution().solve([ 3, 20, 17, 17 ], [ 5, 9, 20, 11, 6, 18, 7, 13 ]))
