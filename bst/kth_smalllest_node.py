class Solution:
    def __init__(self):
        self.inorder = []

    def kthsmallest(self, A, B):
        self.inorder = []
        self.inorder_traversal(A)
        return self.inorder[B-1]

    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        self.inorder.append(root.val)
        self.inorder_traversal(root.right)
