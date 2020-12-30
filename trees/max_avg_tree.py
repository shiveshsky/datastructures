class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        maxav = 0

        def maxavg(root):
            nonlocal maxav
            if root is None:
                return (0, 0)
            l = (0, 0)
            if root.left:
                l = maxavg(root.left)
            r = (0, 0)
            if root.right:
                r = maxavg(root.right)
            avg = ((l[0] * l[1]) + (r[0] * r[1]) + root.val) / (l[1] + r[1] + 1)
            maxav = max(maxav, avg)
            return (avg, l[1] + r[1] + 1)

        maxavg(root)
        return maxav


if __name__ == '__main__':
    pass
