from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


ma = defaultdict(int)


def cnt(root, parent):
    if root is None:
        return
    cnt(root.left, root)
    cnt(root.right, root)
    if parent and root.val == parent.val:
        ma[root.val] += 1
    elif (root.left and root.val == root.left.val) or (root.right and root.val == root.right.val):
        ma[root.val] += 1


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(2)
    root.left.left.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    root.right.left = TreeNode(4)
    root.right.left.left = TreeNode(4)
    root.right.left.left.left = TreeNode(4)
    root.right.left.right = TreeNode(4)

    print(cnt(root, None))
    print(ma)
