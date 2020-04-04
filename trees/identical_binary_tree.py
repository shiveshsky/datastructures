class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, A, B):
        return self.concurrent_traveller(A, B)

    def concurrent_traveller(self, A, B):
        if A is None and B is None:
            return 1
        elif A is None:
            return 0
        elif B is None:
            return 0

        left = self.concurrent_traveller(A.left, B.left)
        right = self.concurrent_traveller(A.right, B.right)

        if left and right:
            if A.val == B.val:
                return 1
            else:
                return 0
        else:
            return 0
