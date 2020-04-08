class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    # The below is O(n) and can be improved by following the below solution
    # def solve(self, A, B, C):
    #     pathA = []
    #     self.inorder(A, B, pathA)
    #     pathB = []
    #     self.inorder(A, C, pathB)
    #
    #     pathA.reverse()
    #     pathB.reverse()
    #     i=0
    #     while i<len(pathA) and i<len(pathB):
    #         if pathA[i]!=pathB[i]:
    #             break
    #         i+=1
    #     return len(pathA)+len(pathB)-2*(i)
    #
    # def inorder(self, root, num, path):
    #     if root == None:
    #         return False
    #     if num < root.val:
    #         left = self.inorder(root.left, num, path)
    #         if left:
    #             path.append(root.val)
    #             return True
    #     elif num > root.val:
    #         right = self.inorder(root.right, num, path)
    #         if right:
    #             path.append(root.val)
    #             return True
    #     elif num == root.val:
    #         path.append(num)
    #         return True
    #     return False
    def solve(self, A, B, C):
        if B > C:
            B, C = C, B
        return self.distance_between_2_nodes(A, B, C)

    def distance_from_root(self, root, A):
        if root is None:
            return 0
        if root.val == A:
            return 0
        if A<root.val:
            return 1+ self.distance_from_root(root.left, A)
        return 1+self.distance_from_root(root.right, A)

    def distance_between_2_nodes(self, root, B, C):
        if root is None:
            return 0
        # both keys lie on left
        if root.val>B and root.val>C:
            return self.distance_between_2_nodes(root.left, B, C)
        # both keys lie on right
        if root.val<B and root.val<C:
            return self.distance_between_2_nodes(root.right, B, C)
        # if one on left and one on right

        if root.val >= B and root.val <= C:
            return self.distance_from_root(root, B)+self.distance_from_root(root, C)



root = TreeNode(32)
root.left = TreeNode(25)
root.left.left = TreeNode(17)
root.left.right = TreeNode(27)
root.left.left.left = TreeNode(9)
root.right = TreeNode(46)
root.right.right = TreeNode(49)
root.right.left = TreeNode(40)
if __name__ == '__main__':
    print(Solution().solve(root, 32, 9))