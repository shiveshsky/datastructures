from collections import defaultdict


class Solution:
    def __init__(self):
        self.mypoles = dict()

    def topview(root):

        if (root == None):
            return
        q = []
        m = dict()
        hd = 0
        root.hd = hd

        # push node and horizontal
        # distance to queue
        q.append(root)

        while (len(q)):
            root = q[0]
            hd = root.hd

            # count function returns 1 if the
            # container contains an element
            # whose key is equivalent to hd,
            # or returns zero otherwise.
            if hd not in m:
                m[hd] = root.val
            if (root.left):
                root.left.hd = hd - 1
                q.append(root.left)

            if (root.right):
                root.right.hd = hd + 1
                q.append(root.right)

            q.pop(0)
        ans = []
        for i in sorted(m):
            ans.append(m[i])
        return ans

