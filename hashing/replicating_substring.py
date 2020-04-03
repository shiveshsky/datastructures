from collections import Counter


class Solution:
    def solve(self, A, B):
        counter = Counter(A)
        for v in counter.values():
            if v % B != 0:
                return -1
        return 1
