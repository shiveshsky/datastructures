class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def removehalflings(root):
    if root is None:
        return
    root.left = removehalflings(root.left)
    root.right = removehalflings(root.right)
    if root.left is None and root.right is None:
        return root
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left
    return root


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(7)
    root.right = TreeNode(5)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(11)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(4)
    removehalflings(root)
    print(root)
