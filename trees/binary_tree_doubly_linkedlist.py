class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binary_to_dll(root):
    stack = []
    curr = root
    prev = None
    head = None
    while stack or curr:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            curr.left = prev
            if prev is not None:
                prev.right = curr
            else:
                head = curr
            prev = curr
            curr = curr.right
    return head


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(7)
    root.right = TreeNode(5)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(11)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(4)
    h = binary_to_dll(root)
    print(h)
