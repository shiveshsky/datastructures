class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolveDiameter:
    def solve(self, root, ans):
        if root is None:
            return 0
        left = self.solve(root.left, ans)
        right = self.solve(root.right, ans)
        ans[0] = max(ans[0], left + right + 1)
        return max(left, right) + 1


if __name__ == '__main__':
    ans = [0]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(SolveDiameter().solve(root, ans))
