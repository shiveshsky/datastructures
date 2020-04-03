class Solution:
    def solve(self, A, B, C):
        prefix_arr = []
        cnt = 0

        for i in range(0, len(A)):
            if i==0:
                prefix_arr.append(A[i])
            else:
                prefix_arr.append(prefix_arr[-1]+A[i])

            if B <= prefix_arr[-1] <= C:
                cnt += 1
        for i in range(0, len(prefix_arr)):
            for j in range(0, i):
                if B<=prefix_arr[i]-prefix_arr[j]<=C:
                    cnt+=1
        return cnt

print(Solution().solve([1,-10, 5, 3, 4], 8,10))