from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.mypoles = defaultdict(list)

    def verticalOrderTraversal(self, A):
        self.mypoles = defaultdict(list)
        # TODO call your runner
        self.vertical_traveller(A, 0, 1)
        ans = []
        for k in sorted(self.mypoles.keys()):
            all_vals = self.mypoles[k]
            all_vals.sort(key=lambda a: a[1])
            row = [i[0] for i in self.mypoles[k]]
            ans.append(row)
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

