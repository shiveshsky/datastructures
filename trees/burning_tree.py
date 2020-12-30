'''
              1
          /      \
       2            3
     /   \         /
    4     5       6
   /     / \
  8     9   10
       /
      11
In the above tree, if we set the leaf node 11 at fire.




In 1s, the fire will reach node 9.
In 2s, the fire will reach node 5.
In 3rd second, the fire will reach node 2 and 10. Here comes an observation:
In 2s fire reached node 5. For node 5, the initial burned leaf is in it’s left subtree, so the time taken to burn right subtree will be the height of the right subtree which is 1. Therefore, fire reaches to node 10 in (2+1) = 3s.
Again, for the node 2. Fire reached to node 2 in 3s from right subtree. Therefore, time taken to burn left subtree will be it’s height.
So the solution is to apply recursion and for every node calculate the below-required values:

Left Depth.
Right Depth.
The time required for fire to reach the current node.
Is the current subtree conatins initial burnt leaf node.
So, for the minimum time required to burn any subtree will be:

The time required for fire to reach the root node from initial burnt leaf + depth of the opposite side

Therefore, to find time required to burn the complete tree, we need to calculate the above value for every node, and take maximum of that value.

ans = max(ans, (time required for fire to reach current node + depth of other subtree))

Below is the implementation of the above approach:
'''


class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None


class Data:
    def __init__(self):
        self.left_depth = 0
        self.right_depth = 0
        self.contains = False
        self.time = 0


def getResult(root, data, target, res):
    if root is None:
        return
    if root.left is None and root.right is None:
        if root.val == target:
            data.contains = True
            data.time = 0
        return
    # info about left child
    data_left = Data()
    getResult(root.left, data_left, target)

    # info about right child
    data_right = Data()
    getResult(root.right, data_right, target)

    data.time = data_left.time + 1 if data_left.contains else -1
    if data.time == -1:
        data.time = data_right.time + 1 if data_right.contains else -1

    data.contains = data_right.contains or data_left.contains

    data.left_depth = max(data_left.left_depth, data_left.right_depth) + 1 if root.left else 0
    data.right_depth = max(data_right.left_depth, data_right.right_depth) + 1 if root.right else 0

    # calculating answer
    if data.contains:
        # if left subtree exists and it contains fired node
        if data_left.contains:
            # calc answer
            res[0] = max(res[0], data.time + data.right_depth)
        if data_right.contains:
            # calc answer
            res[0] = max(res[0], data.time + data.left_depth)
