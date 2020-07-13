# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        fr = self.findRoot(s, t)
        if fr[0]:
            cn = self.commonNode(fr[1], t)
            return cn
        return False

    def findRoot(self, s, t):
        if s is None:
            return (False, None)
        if s.val == t.val:
            return (True, s)
        left = self.findRoot(s.left, t)
        if left[0]:
            return left
        right = self.findRoot(s.right, t)
        if right[0]:
            return right
        return (False, None)

    def commonNode(self, s, t):
        if s is None and t is None:
            return True
        if s is None and t is not None:
            return False
        if s is not None and t is None:
            return False
        left = self.commonNode(s.left, t.left)
        right = self.commonNode(s.right, t.right)
        if left and right and s.val == t.val:
            return True
        return False


if __name__ == '__main__':
    t1 = TreeNode(3)
    t1.left = TreeNode(4)
    t1.left.left = TreeNode(1)
    t1.left.right = TreeNode(2)
    t1.right = TreeNode(5)

    t2 = TreeNode(4)
    t2.left = TreeNode(1)
    t2.right = TreeNode(2)

    print(Solution().isSubtree(t1, t2)
          )
