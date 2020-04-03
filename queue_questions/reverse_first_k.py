from queue import Queue


class Solution:
    def solve(self, A, B):
        queue = Queue(len(A))
        for i in A:
            queue.put(i)
        stk = []
        for i in range(0, B):
            stk.append(queue.get())
        ans = []

        while len(stk)>0:
            ans.append(stk.pop())

        while not queue.empty():
            ans.append(queue.get())
        return ans


print(Solution().solve([1, 2, 3, 4, 5], 3))