class Solution:
    # @param A : tuple of integers
    # @return a strings

    def largestNumber(self, A):
        # new_arr = map(str, A)
        ans = self.partition(A)
        final =  ''.join(map(str, ans)).lstrip('0')
        if final:
            return final
        else:
            return '0'

    def make_biggest(self, left, right):
        i=0
        j=0
        new = []
        while i<len(left) and j<len(right):
            if int(str(str(left[i]) + str(right[j]))) > int(str(str(right[j])+str(left[i]))):
                new.append(left[i])
                i += 1
            else:
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

        biggest_possible = self.make_biggest(left, right)

        return biggest_possible

print(Solution().largestNumber([0,0,0,0,0]))