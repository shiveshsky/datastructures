class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        if root is None:
            return 0
        ans = [-999999999]
        self.diameter(root, ans)
        return ans[0]

    def diameter(self, root, ans):
        if root is None:
            return 0
        left = self.diameter(root.left, ans)
        rigth = self.diameter(root.right, ans)
        ans[0] = max(ans[0], left+rigth+1)
        return 1+max(left, rigth)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().diameterOfBinaryTree(root))