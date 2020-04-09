class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.left = []
        self.leaf = []
        self.right = []

    def left_boundary(self, A):
        if A is None:
            return
        if A.left is not None or A.right is not None:
            self.left.append(A.val)
        if A.left is not None and A.right is None:
            self.left_boundary(A.left)
        if A.right is not None and A.left is None:
            self.left_boundary(A.right)
        if A.left and A.right:
            self.left_boundary(A.left)

    def leaf_boundary(self, A):
        if A is None:
            return
        self.leaf_boundary(A.left)
        self.leaf_boundary(A.right)
        if A.left is None and A.right is None:
            self.left.append(A.val)

    def right_boundary(self, A):
        if A is None:
            return

        if A.left is not None and A.right is None:
            self.right_boundary(A.left)
        if A.right is not None and A.left is None:
            self.right_boundary(A.right)
        if A.left and A.right:
            self.right_boundary(A.right)

        if A.left is not None or A.right is not None:
            self.right.append(A.val)

    def solve(self, A):
        self.left_boundary(A)
        self.leaf_boundary(A)
        self.right_boundary(A)
        return self.left+self.leaf+self.right[0:-1]

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(9)
    root.right.left.right = TreeNode(10)
    print(Solution().solve(root))
