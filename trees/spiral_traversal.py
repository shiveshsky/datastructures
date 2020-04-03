# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, A):
        stak1 = []
        stak2 = []
        ans = []
        stak1.append(A)
        while len(stak1) > 0 or len(stak2) > 0:
            if len(stak1) > 0:
                row = []
                while len(stak1) > 0:
                    node = stak1.pop()
                    row.append(node.val)
                    if node.left is not None:
                        stak2.append(node.left)
                    if node.right is not None:
                        stak2.append(node.right)
                ans.append(row)
            elif len(stak2) > 0:
                row = []
                while len(stak2) > 0:
                    node = stak2.pop()
                    row.append(node.val)
                    if node.right is not None:
                        stak1.append(node.right)
                    if node.left is not None:
                        stak1.append(node.left)
                ans.append(row)
        return ans


root = TreeNode(4)
e1 = TreeNode(2)
e2 = TreeNode(3)
root.left = e1
root.right = e2
e3 = TreeNode(8)
e2.left = e3
e2.right = TreeNode(0)
e1.left = TreeNode(5)
e1.right = TreeNode(6)
print(Solution().zigzagLevelOrder(root))