class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, A, B):
        if len(A) == 0 and len(B) == 0:
            return None
        if len(A) == 0:
            return TreeNode(B[0])
        elif len(B) == 0:
            return TreeNode(A[0])
        root = TreeNode(A[0])
        index_root = B.index(A[0])
        left_arr = B[0:index_root]
        root.left = self.buildTree(A[1: 1+len(left_arr)], left_arr)
        right_arr = B[index_root + 1:]
        root.right = self.buildTree(A[len(left_arr)+1: ], right_arr)
        return root

# print(Solution().buildTree([1,2,3], [2,1,3]))


print(Solution().buildTree([ 13, 33, 41, 11, 49, 48, 23 ], [ 41, 33, 11, 13, 48, 49, 23 ]))