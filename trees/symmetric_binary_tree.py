class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isMirror(self, A, B):
        if A is None and B is None:
            return 1
        elif A is None or B is None:
            return 0

        left = self.isMirror(A.left, B.right)
        right = self.isMirror(A.right, B.left)

        if left and right:  # this is correct but was giving TLE
            if A.val == B.val:
                return 1
            else:
                return 0
        else:
            return 0

    def isSymmetric(self, A):
        # mirror = self.mirror_tree(A)
        return self.isMirror(A, A)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(Solution().isSymmetric(root))
