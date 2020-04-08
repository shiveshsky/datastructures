import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isValidBST(self, A, mini=-math.inf, maxi=math.inf):
        if A is None:
            return True
        if A.val < mini or A.val > maxi:
            return False
        left = self.bst_validator(A.left, mini, A.val)
        right = self.bst_validator(A.right, A.val+1, maxi)
        return left and right
