class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def buildTree(self, A, B):  # preorder and inorder
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

    def postorderTraversal(self, A):
        stack1 = []

        stack1.append(A)
        stack2 = []
        while len(stack1) > 0:
            ele = stack1.pop()
            stack2.append(ele.val)
            if ele.left is not None:
                stack1.append(ele.left)
            if ele.right is not None:
                stack1.append(ele.right)
        return stack2[::-1]

    def solve(self, A, B, C):
        try:
            root = self.buildTree(A, B)
        except Exception:
            print('error')
            return 0
        postorder = self.postorderTraversal(root)
        if C == postorder:
            return 1
        else:
            return 0

print(Solution().solve([ 13, 33, 41, 11, 49, 48, 23 ], [ 41, 33, 11, 13, 48, 49, 23 ], [ 41, 11, 33, 48, 23, 49, 13 ]))