import math


class Solution:
    def newKthpermut(self, n, rank, prev_fixed, ans):
        if rank==1:
            ans+=prev_fixed
            ans+=n
            return
        if rank==2:
            n[-1], n[-2] = n[-2], n[-1]
            ans+=prev_fixed
            ans+=n
            return

        n_1_fact = math.factorial(len(n)-1)
        for i in range(0, len(n)):
            if rank>n_1_fact:
                rank-=n_1_fact
            else:
                prev_fixed.append(n[i])
                self.newKthpermut(n[0:i]+n[i+1:], rank, prev_fixed, ans)
                return

ans = []
Solution().kthpermutation([1, 2, 3], [], [0], 4, ans)