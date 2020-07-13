class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, A):
        if A is None:
            return 0
        elif A.left is None and A.right is None:
            return 1
        elif A.left is None and A.right is not None:
            return self.minDepth(A.right) + 1
        elif A.right is None and A.left is not None:
            return self.minDepth(A.left) + 1
        else:
            left = self.minDepth(A.left)
            right = self.minDepth(A.right)
            return min(left, right) + 1


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    print(Solution().minDepth(r))
