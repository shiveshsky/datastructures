import math
class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    def __init__(self):
        self.parent = TreeNode(-math.inf)
        self.first = True

    def recoverTree(self, root):
        arr = [None, None]
        self.recover(root, arr)
        return [arr[0].val, arr[1].val]

    def recover(self, root, arr):
        if root is None:
            return
        self.recover(root.left, arr)
        if root.val <= self.parent.val:
            if self.first:
                arr[0] = self.parent
                self.first = False
            arr[1] = root
        self.parent = root
        self.recover(root.right, arr)
