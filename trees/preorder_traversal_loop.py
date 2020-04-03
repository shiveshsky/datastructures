class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, A):
        stack = []
        stack.append(A)
        ans = []
        while len(stack) > 0:
            ele = stack.pop()
            ans.append(ele.val)
            if ele.right is not None:
                stack.append(ele.right)
            if ele.left is not None:
                stack.append(ele.left)
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
print(Solution().preorderTraversal(root))