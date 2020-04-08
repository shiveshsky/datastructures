class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, A):
        if len(A)==0:
            return None
        if len(A)==1:
            return TreeNode(A[0])
        mid = (len(A))//2
        left = self.sortedArrayToBST(A[0:mid])
        right = self.sortedArrayToBST(A[mid+1:])
        node = TreeNode(A[mid])
        node.left = left
        node.right = right
        return node

if __name__ == '__main__':
    Solution().sortedArrayToBST([1, 2, 3])
