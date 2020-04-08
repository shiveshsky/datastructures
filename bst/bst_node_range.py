class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    def solve(self, A, B, C):
        self.count = 0
        self.runner(A, B, C)
        return self.count

    def runner(self, A, B, C):
        if A is None:
            return
        if A.left is not None and A.left.val >= B:
            self.runner(A.left, B, C)
        if A.right is not None and A.right.val <= C:
            self.runner(A.right, B, C)
        if C >= A.val >= B:
            self.count += 1


root = TreeNode(32)
l1 = TreeNode(25)
r1 = TreeNode(46)
r1.left = TreeNode(40)
r1.right = TreeNode(49)
root.left = l1
root.right = r1

root.left.left = TreeNode(17)
root.left.right = TreeNode(27)
root.left.left.left = TreeNode(9)


if __name__ == '__main__':
    print(Solution().solve(root, 11, 26))