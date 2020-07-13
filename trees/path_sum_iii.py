class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int, ans=0) -> int:
        if root is None:
            return 0
        else:
            ans += self.checksum(root, sum, 0)
            ans += self.pathSum(root.left, sum, 0)
            ans += self.pathSum(root.right, sum, 0)
            return ans

    def checksum(self, root, sum, cnt):
        if root is None and sum == 0:
            return 1
        if sum == 0:
            cnt += 1
            return cnt
        if sum == root.val:
            return 1
        l = self.checksum(root.left, sum - root.val, cnt)
        r = self.checksum(root.right, sum - root.val, cnt)
        return (cnt + l + r)


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.right = TreeNode(-3)
    root.right.right = TreeNode(11)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(1)
    print(Solution().pathSum(root, 8))
