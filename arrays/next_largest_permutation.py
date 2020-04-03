# Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        i=len(A)-1
        while i>=0:
            if A[i-1]>A[i]:
                i-=1
            else:
                break
        index = i-1 if i>0 else 0
        if len(A)>1:
            min_diff = A[index+1]-A[index]
            min_ind = index+1
            # we are searching in the right direction in our slope for the min value
            # to swap because we want to generate next bigger value.
            for i in range(index+1, len(A)):
                if A[i]-A[index]>0:
                    if min_diff>A[i]-A[index]:
                        min_diff = A[i]-A[index]
                        min_ind = i
            A[index], A[min_ind] = A[min_ind], A[index]

            # A[index], A[-1] = A[-1], A[index]
            A =A[0:index+1]+ sorted(A[index+1:])
        return A


print(Solution().nextPermutation([1, 4, 3, 2]))