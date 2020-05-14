class Solve:
    def solve(self, root, ans):
        if root is None:
            return 0
        left = self.solve(root.left, ans)
        right = self.solve(root.right, ans)
        tmp = max(left, right) + root.val

        is_possible_ans = max(tmp, left + right + root.val)
        ans[0] = max(ans[0], is_possible_ans)
        return tmp

    ans = 0

    def solve(self, node):
        global ans
        if node is None:
            return 0
        left = node.left
        right = node.right
        tmp = max(left, right) + node.val
        ans = max(ans, left + right + node.val, tmp)
        return tmp
