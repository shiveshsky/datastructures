# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import defaultdict


class Solution:
    def __init__(self):
        self.parents = defaultdict(0)
        self.count = 0

    def solve(self, A, B):
        self.parents = defaultdict(0)
        self.count = 0
        self.solver(A, B)
        return self.count

    def count_in_range(self, l, r):
        count = 0
        for i in range(l, r+1, 1):
            if self.parents[i]>0:
                count+=1
        # count = 0
        # for i in self.parents:
        #     if i>=l and i<=r:
        #         count+=1
        # return count

    def solver(self, A, B):
        if A is None:
            return
        self.count+=self.count_in_range(A-B, A+B)
        self.parents[A.val]+=1
        self.solver(A.left, B)
        self.solver(A.right, B)
        self.parents[A.val]-=1
        # self.parents.remove(A.val)

