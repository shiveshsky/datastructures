class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, A):
        stack1 = []

        stack1.append(A)
        stack2 = []
        while len(stack1) > 0:
            ele = stack1.pop()
            stack2.append(ele.val)
            if ele.left is not None:
                stack1.append(ele.left)
            if ele.right is not None:
                stack1.append(ele.right)
        return stack2[::-1]

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