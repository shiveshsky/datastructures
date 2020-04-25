# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

	def inorderTraversal(self, A):
		stack = []
		ans = []
		current = A
		while True:
			if current is not None:
				stack.append(current)
				current = current.left
			elif len(stack) > 0:
				current = stack.pop()
				ans.append(current.val)
				current = current.right
			else:
				break
		return ans
