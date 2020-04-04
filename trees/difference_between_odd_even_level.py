from collections import deque
class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    def solve(self, A):
        queue = deque()
        queue.append(A)
        marker = '#'
        queue.append(marker)
        flag = True
        odd_sum = 0
        even_sum = 0
        while len(queue) > 0:
            ele = queue.popleft()
            if ele != "#":
                if flag:
                    odd_sum+=ele.val
                else:
                    even_sum+=ele.val
                if ele.left is not None:
                    queue.append(ele.left)
                if ele.right is not None:
                    queue.append(ele.right)
            else:
                flag = not flag
                if len(queue) == 0:
                    break
                queue.append("#")

        return (odd_sum-even_sum)
