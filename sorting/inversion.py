class Solution:
    def __init__(self):
        self.count = 0

    def countInversions(self, A):
        self.count=0
        self.partition(A)
        return self.count

    def make_sorted(self, left, right):
        i=0
        j=0
        new = []
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                new.append(left[i])
                i += 1
            else:
                self.count += len(left)-i
                new.append(right[j])
                j += 1
        if i<len(left):
            new += left[i:]
        elif j<len(right):
            new += right[j:]
        return new

    def partition(self, A):
        if len(A) == 1:
            return A
        mid = len(A)//2
        left = self.partition(A[0:mid])
        right = self.partition(A[mid:])
        sorted = self.make_sorted(left, right)
        return sorted
print(Solution().countInversions([4,5,0,3,2,1]))