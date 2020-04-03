# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, A):
        queue = []
        queue.append(A)
        ans = []
        marker = '#'
        queue.append(marker)
        row = []
        while len(queue) > 0:
            ele = queue.pop(0)
            if ele != "#":
                row.append(ele.val)
                if ele.left is not None:
                    queue.append(ele.left)
                if ele.right is not None:
                    queue.append(ele.right)
            else:
                ans.append(row)
                row = []
                if len(queue) == 0:
                    break
                queue.append("#")
        return ans


root = TreeNode(3)
e1 = TreeNode(9)
e2 = TreeNode(20)
root.left = e1
root.right = e2
e3 = TreeNode(15)
e2.left = e3
e2.right = TreeNode(7)
print(Solution().levelOrder(root))