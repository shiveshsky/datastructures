class Solution:
    def solve(self, A):
        digits = [1, 2, 3]
        queue = [1, 2, 3]
        ans = [1, 2, 3]
        cnt = 3
        begin = 0
        while len(ans)<=A:
            end = cnt+begin
            for i in digits:
                for j in range(begin, end, 1):
                    ans.append(int(str(i)+str(queue[j])))
                    if len(ans)==A:
                        return ans
                    queue.append(ans[-1])
            begin = end
            cnt = (cnt*3)
        return ans[0:A]
print(Solution().solve(586))

