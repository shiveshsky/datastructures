class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    marker = "$"
    def solve(self, A):
        return 0 if self.duplicate_solver(A, set()) else 1

    def duplicate_solver(self, root, subtree_set):
        s = ""
        if root is None:
            return s + self.marker

        sleft = self.duplicate_solver(root.left, subtree_set)
        if sleft == s:
            return s
        sright = self.duplicate_solver(root.right, subtree_set)
        if sright == s:
            return s
        s = s + str(root.val) + sleft + sright
        if len(s)>3 and s in subtree_set:
            return ""
        subtree_set.add(s)
        return s


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(2)
    root.right.right.right = TreeNode(5)
    root.right.right.left = TreeNode(4)
    print(Solution().solve(root))
