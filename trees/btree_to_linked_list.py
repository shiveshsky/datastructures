class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solve:
    def __init__(self):
        self.tail = None

    def tree_to_ll(self, A):
        stack = []
        ans = A
        while A is not None or len(stack)>0:
            if A.right is not None:
                stack.append(A.right)
            A.right = A.left
            A.left = None
            if A.right is None and len(stack)>0:
                A.right = stack.pop()
            A = A.right
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(2)
    root.right.right.right = TreeNode(5)
    root.right.right.left = TreeNode(4)
    print(Solve().tree_to_ll(root))



