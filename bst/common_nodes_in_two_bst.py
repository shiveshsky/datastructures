class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution:
    def __init__(self):
        self.inorder = set()
        self.sum = 0

    def solve(self, A, B):
        self.inorder = set()
        self.sum = 0
        # self.inorder_traversal(A)
        # self.nodefinder(B)
        self.printCommon(A, B)
        return self.sum

    def nodefinder(self, root):
        if root is None:
            return
        self.nodefinder(root.left)
        self.nodefinder(root.right)
        if root.val in self.inorder:
            self.sum += root.val

    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        self.inorder.add(root.val)
        self.inorder_traversal(root.right)


    def printCommon(self, root1, root2):
        # Create two stacks for two inorder
        s1 = []
        s2 = []

        while 1:

            # append the Nodes of first
            # tree in stack s1
            if root1:
                s1.append(root1)
                root1 = root1.left

                # append the Nodes of second tree
            # in stack s2
            elif root2:
                s2.append(root2)
                root2 = root2.left

                # Both root1 and root2 are NULL here
            elif len(s1) != 0 and len(s2) != 0:
                root1 = s1[-1]
                root2 = s2[-1]

                # If current keys in two trees are same
                if root1.val == root2.val:
                    self.sum+=root1.val
                    s1.pop(-1)
                    s2.pop(-1)

                    # move to the inorder successor
                    root1 = root1.right
                    root2 = root2.right

                elif root1.val < root2.val:

                    # If Node of first tree is smaller, than
                    # that of second tree, then its obvious
                    # that the inorder successors of current
                    # Node can have same value as that of the
                    # second tree Node. Thus, we pop from s2
                    s1.pop(-1)
                    root1 = root1.right

                    # root2 is set to NULL, because we need
                    # new Nodes of tree 1
                    root2 = None
                elif root1.val > root2.val:
                    s2.pop(-1)
                    root2 = root2.right
                    root1 = None

            # Both roots and both stacks are empty
            else:
                break