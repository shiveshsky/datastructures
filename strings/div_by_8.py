class Solution:
    def solve(self, A):
        if len(A)>3:
            last_3 = A[-3:]
            return 1 if int(last_3)%8==0 else 0
        else:
            return 1 if int(A) % 8 == 0 else 0


print(Solution().solve("9240"))
