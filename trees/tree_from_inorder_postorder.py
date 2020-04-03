# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, A, B):  # inorder, postorder
        if len(A) == 0 and len(B) == 0:
            return None
        if len(A) == 0:
            return TreeNode(B[0])
        elif len(B) == 0:
            return TreeNode(A[0])
        root = TreeNode(B[-1])
        index_root = A.index(B[-1])
        left_arr_inorder = A[0: index_root]
        right_arr_inorder = A[index_root+1: ]
        right_arr_postorder = B[-1*(len(right_arr_inorder)+1):-1]
        left_arr_postorder = B[0: len(left_arr_inorder)]
        root.left = self.buildTree(left_arr_inorder, left_arr_postorder)
        root.right = self.buildTree(right_arr_inorder, right_arr_postorder)
        return root


print(Solution().buildTree([7, 5, 6, 2, 3, 1, 4], [5, 6, 3, 1, 4, 2, 7]))