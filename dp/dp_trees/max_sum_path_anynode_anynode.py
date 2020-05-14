class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solve:
    def solve(self, root, ans):
        if root is None:
            return 0
        left = self.solve(root.left, ans)
        right = self.solve(root.right, ans)
        tmp = max(max(left, right) + root.val, root.val)
        is_possible_ans = max(tmp, left + right + root.val)
        ans[0] = max(ans[0], is_possible_ans)
        return tmp


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(-9)

    ans = [0]
    Solve().solve(root, ans)
    print(ans[0])
