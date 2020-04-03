'''
Given an array of integers (not necessarily distinct) A,
if we split the array into some number of "chunks" (partitions),
 and individually sort each chunk. After concatenating them,
 the result equals the sorted array.
What is the most number of chunks we could have made?
'''


class Solution:
    def solve(self, A):
        copyA = A.copy()
        copyA.sort()
        max_so_far = A[0]
        min_range = copyA[0]

        i=0
        c=0
        while i < len(A):
            if A[i] >= min_range:
                max_so_far = max(max_so_far, A[i])
                if max_so_far == copyA[i]:
                    c+=1
                    if i+1<len(A):
                        min_range = copyA[i+1]
                        max_so_far = A[i+1]
            else:
                return c
            i+=1
        return c

print(Solution().solve([2,0,1,2]))
