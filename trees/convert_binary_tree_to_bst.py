'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


# The given root is the root of the Binary Tree
# Return the root of the generated BST
def inorder_traversal(root):
    inorder = []
    stack = []
    current = root
    while (True):
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack) > 0:
            ele = stack.pop()
            current = ele.right
            inorder.append(ele.data)
        else:
            break
    return inorder


def replace_vals(root, inorder):
    stack = []
    current = root
    i = 0
    while (True):
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack) > 0:
            ele = stack.pop()
            ele.data = inorder[i]
            current = ele.right
            i += 1
        else:
            break
    return root


def binaryTreeToBST(root):
    # code here
    inorder = inorder_traversal(root)
    inorder.sort()
    return replace_vals(root, inorder)
