class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.inorder = []

    def t2Sum(self, A, B):
        self.inorder = []
        self.inorder_traversal(A)
        i = 0
        j = len(self.inorder) - 1
        while i < j:
            if self.inorder[i] + self.inorder[j] == B:
                return 1
            elif self.inorder[i] + self.inorder[j] < B:
                i += 1
            elif self.inorder[i] + self.inorder[j] > B:
                j -= 1
        return 0

    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        self.inorder.append(root.val)
        self.inorder_traversal(root.right)
