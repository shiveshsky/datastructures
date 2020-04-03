from collections import Counter


class Solution:

    def solve(self, A):
        l=0
        r=0
        ag = {}
        cnt = 0
        n=len(A)
        for i in A:
            ag.update({i: 0})
        while r<n:
            if ag.get(A[r])==0:
                ag.update({A[r]: 1})
                r += 1

            else:
                cnt += ((r - l) * (r - l + 1)) // 2
                while ag.get(A[r])==1:
                    ag.update({A[l]: 0})
                    l += 1

        cnt += ((r - l) * (r - l + 1)) // 2
        return cnt

print(Solution().solve([93, 9, 12, 32, 97, 75, 32, 77, 40, 79, 61, 42, 57, 19, 64, 16, 86, 47, 41, 67, 76, 63, 24, 10, 25, 96, 1, 30, 73, 91, 70, 65, 53, 75, 5, 19, 65, 6, 96, 33, 73, 55, 4, 90, 72, 83, 54, 78, 67, 56, 8, 70, 43, 63]))