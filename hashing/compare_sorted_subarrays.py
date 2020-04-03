import random


class Solution:
    def solve(self, A, B):
        ans = []
        new_assign = {}
        rand_Set = set()
        prefix_sum = []
        for i in A:
            if i not in new_assign:
                rand_val = int(random.randrange(0, 100000000))
                while rand_val in rand_Set:
                    rand_val = int(random.randrange(0, 100000000))
                rand_Set.add(rand_val)
                new_assign[i] = rand_val
            if len(prefix_sum) == 0:
                prefix_sum.append(new_assign[i])
            else:
                prefix_sum.append(prefix_sum[-1]+new_assign[i])
        for q in B:
            l1 = q[0]
            r1 = q[1]
            l2 = q[2]
            r2 = q[3]
            left_subarray = 0
            right_subarray = 0
            if l1 == 0:
                left_subarray = prefix_sum[r1]
            else:
                left_subarray = prefix_sum[r1]-prefix_sum[l1-1]
            if l2 == 0:
                right_subarray = prefix_sum[r2]
            else:
                right_subarray = prefix_sum[r2]-prefix_sum[l2-1]
            if left_subarray == right_subarray:
                ans.append(1)
            else:
                ans.append(0)
        return ans

print(Solution().solve([1, 7, 11, 8, 11, 7, 1], [[0, 2, 4, 6]]))
