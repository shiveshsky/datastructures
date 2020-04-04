class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isMirror(self, A, B):
        if A is None and B is None:
            return 1
        elif A is None:
            return 0
        elif B is None:
            return 0

        left = self.isMirror(A.left, B.right)
        right = self.isMirror(A.right, B.left)

        # if left and right: # this is correct but was giving TLE
        #     if A.val == B.val:
        #         return 1
        #     else:
        #         return 0
        # else:
        #     return 0
        if left and right:
            return 1
        return 0

    def isSymmetric(self, A):
        # mirror = self.mirror_tree(A)
        return self.isMirror(A, A)


root = TreeNode(1)
a = TreeNode(2)
a.right = TreeNode(3)
root.left = a
root.right = TreeNode(2).right = TreeNode(3)
print(Solution().isSymmetric(root))