class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def solve(self, A):
        queue = []
        queue.append(A)
        ans = []
        marker = '#'
        queue.append(marker)
        flag = True
        while len(queue) > 0:
            ele = queue.pop(0)
            if ele != "#":
                if flag:
                    ans.append(ele.val)
                    # row.append(ele.val)
                    flag=False
                if ele.left is not None:
                    queue.append(ele.left)
                if ele.right is not None:
                    queue.append(ele.right)
            else:
                flag=True
                if len(queue) == 0:
                    break
                queue.append("#")

        return ans
