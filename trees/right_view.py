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
        ans = []
        marker = '#'
        queue.append(marker)
        row = []
        flag = True
        while len(queue) > 0:
            ele = queue.popleft()
            if ele != "#":
                if flag:
                    ans.append(ele.val)
                    # row.append(ele.val)
                    flag=False
                if ele.right is not None:
                    queue.append(ele.right)
                if ele.left is not None:
                    queue.append(ele.left)
            else:
                # ans.append(row)
                flag=True
                # row = []
                if len(queue) == 0:
                    break
                queue.append("#")

        return ans
