from collections import defaultdict


class Solution:
    def __init__(self):
        self.mypoles = defaultdict(list)

    def solve_my_approach(self, A):
        self.mypoles = defaultdict(list)
        self.vertical_traveller(A, 0, 1)
        ans = []
        for k in sorted(self.mypoles.keys()):
            all_vals = self.mypoles[k]
            all_vals.sort(key=lambda a: a[1])
            row = [i[0] for i in self.mypoles[k]]
            ans.append(row)
        final = [i[0] for i in ans]
        return ans

    def vertical_traveller(self, A, distance_from_root, level):
        if A is None:
            return
        self.mypoles[distance_from_root].append((A.val, level))
        if A.left is not None:
            self.vertical_traveller(A.left, distance_from_root-1, level+1)
        if A.right is not None:
            self.vertical_traveller(A.right, distance_from_root+1, level+1)
        return

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

