class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if root is None:
            return None
        ser = []
        ser.append(root.val)
        ser.append(self.serialize(root.left))
        ser.append(self.serialize(root.right))
        return ser

    def deserialize(self, data):
        if data is None:
            return
        root = TreeNode(data[0])
        root.left = self.deserialize(data[1])
        root.right = self.deserialize(data[2])
        return root


if __name__ == '__main__':
    rot = TreeNode(1)
    rot.left = TreeNode(2)
    rot.right = TreeNode(3)
    rot.right.left = TreeNode(4)
    rot.right.right = TreeNode(5)
    print(Codec().serialize(rot))
    root = Codec().deserialize([1, [2, None, None], [3, [4, None, None], [5, None, None]]])
    print(root)
