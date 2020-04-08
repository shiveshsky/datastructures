import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_size = 0

    def solve(self, A):
        self.max_size = 0
        self.largest_bst(A)
        return self.max_size

    def largest_bst(self, A):
        if A is None:
            return True, -math.inf, math.inf, 0
        left = self.largest_bst(A.left)
        right = self.largest_bst(A.right)
        if A.val < left[1] or A.val >= right[2]:
            return False, 0, 0, 0
        if left[0] and right[0]:
            self.max_size = max(self.max_size, left[-1] + right[-1] + 1)
        return True, max(A.val, right[1]), min(A.val, left[2]), left[-1] + right[-1] + 1


root = TreeNode(7)
l1 = TreeNode(28)
r1 = TreeNode(43)

ll1 = TreeNode(19)
ll1.left = TreeNode(9)
ll1.right = TreeNode(23)
l1.left = ll1
l1.right = TreeNode(31)

r1.left = TreeNode(27)
r1.right = TreeNode(42)
root.left = l1
root.right = r1
# root = TreeNode(9)
# l1 = TreeNode(10)
# r1 = TreeNode(6)
# l1.left = TreeNode(3)
# r1.right = TreeNode(3)
# r1.right = TreeNode(7)
# root.left = l1
# root.right = r1
if __name__ == "__main__":
    print(Solution().solve(root))
