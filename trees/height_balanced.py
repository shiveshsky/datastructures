class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        ans = self.isBalancedRunner(A)
        return ans[0]

    def isBalancedRunner(self, A):
        if A is None:
            return (1, -1)
        is_left_bal = self.isBalancedRunner(A.left)
        is_right_bal = self.isBalancedRunner(A.right)
        if is_left_bal[0] and is_right_bal[0]:
            if abs(is_left_bal[1]-is_right_bal[1]) <=1:
                return (1, max(is_left_bal[1], is_right_bal[1])+1)
            else:
                return (0, max(is_left_bal[1], is_right_bal[1])+1)
        else:
            return (0, max(is_left_bal[1], is_right_bal[1])+1)

root = TreeNode(3)
e1 = TreeNode(9)
e2 = TreeNode(20)
root.left = e1
root.right = e2
e3 = TreeNode(15)
e2.left = e3
e2.right = TreeNode(7)
print(Solution().isBalanced(root))